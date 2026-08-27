#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import sys
import yaml

ROOT = Path(__file__).resolve().parents[1]
VERIFICATION = ROOT / "verification.yaml"
PROGRESS = ROOT / "progress.yaml"


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def load_yaml(path: Path):
    with path.open("r", encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def main() -> None:
    v = load_yaml(VERIFICATION)
    p = load_yaml(PROGRESS)

    if v.get("schema_version") != 1:
        fail("verification.yaml schema_version must be 1")

    expected_levels = {"L0", "L1", "L2", "L3", "L4"}
    levels = set((v.get("verification_scale") or {}).keys())
    if levels != expected_levels:
        fail(f"verification_scale must define exactly {sorted(expected_levels)}")

    access_values = set(v.get("access_values") or [])
    required_access = {"public", "gated", "partial", "unavailable", "unknown", "not_applicable"}
    if not required_access.issubset(access_values):
        fail("verification.yaml is missing required access values")

    reproduction_values = set(v.get("reproduction_values") or [])
    required_reproduction = {
        "not_attempted",
        "blocked",
        "partial",
        "independent_report",
        "reproduced_here",
        "not_applicable",
    }
    if not required_reproduction.issubset(reproduction_values):
        fail("verification.yaml is missing required reproduction values")

    sources = v.get("sources") or {}
    if not sources:
        fail("verification.yaml must contain sources")

    for source_id, source in sources.items():
        if not isinstance(source, dict):
            fail(f"source {source_id!r} must be a mapping")
        if source.get("level") not in expected_levels:
            fail(f"source {source_id!r} has invalid verification level")
        if not source.get("title") or not source.get("primary"):
            fail(f"source {source_id!r} needs title and primary")
        for field in ("paper", "code", "data", "model"):
            value = source.get(field)
            if value not in access_values:
                fail(f"source {source_id!r}.{field} has invalid access value {value!r}")
        reproduction = source.get("reproduction")
        if reproduction not in reproduction_values:
            fail(f"source {source_id!r} has invalid reproduction value {reproduction!r}")
        if source.get("level") == "L4" and reproduction != "reproduced_here":
            fail(f"source {source_id!r} is L4 without reproduced_here")

    progress_sources = set((p.get("sources") or {}).keys())
    missing_audits = progress_sources - set(sources)
    if missing_audits:
        fail(f"progress sources lack verification entries: {sorted(missing_audits)}")

    claims = v.get("claims") or {}
    for claim_id, claim in claims.items():
        if not isinstance(claim, dict):
            fail(f"claim {claim_id!r} must be a mapping")
        source_id = claim.get("source")
        if source_id not in sources:
            fail(f"claim {claim_id!r} references unknown source {source_id!r}")
        if "value" not in claim or not claim.get("unit") or not claim.get("status"):
            fail(f"claim {claim_id!r} needs value, unit and status")
        if claim.get("reproduced_here") not in (True, False):
            fail(f"claim {claim_id!r}.reproduced_here must be boolean")

    reproduced = set(v.get("reproduced_here") or [])
    unknown_reproduced = reproduced - set(claims)
    if unknown_reproduced:
        fail(f"reproduced_here references unknown claims: {sorted(unknown_reproduced)}")

    for claim_id, claim in claims.items():
        if claim.get("reproduced_here") and claim_id not in reproduced:
            fail(f"claim {claim_id!r} says reproduced_here but is absent from reproduced_here list")
        if claim_id in reproduced and not claim.get("reproduced_here"):
            fail(f"claim {claim_id!r} is in reproduced_here list but boolean is false")

    print(
        "verification.yaml OK: "
        f"{len(sources)} audited sources, {len(claims)} explicit claims, "
        f"{len(reproduced)} reproduced here."
    )


if __name__ == "__main__":
    main()
