#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import re
import sys
import yaml

ROOT = Path(__file__).resolve().parents[1]
RUN_DIR = ROOT / "experiments" / "runs"
VERIFICATION = ROOT / "verification.yaml"
SHA256_RE = re.compile(r"^[0-9a-fA-F]{64}$")
COMMIT_RE = re.compile(r"^[0-9a-fA-F]{7,64}$")


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def load_yaml(path: Path):
    with path.open("r", encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def nonempty(value) -> bool:
    return value is not None and value != "" and value != [] and value != {}


def main() -> None:
    verification = load_yaml(VERIFICATION)
    claims = verification.get("claims") or {}
    sources = verification.get("sources") or {}
    reproduced_here = set(verification.get("reproduced_here") or [])

    runs = sorted(RUN_DIR.glob("*.yaml")) if RUN_DIR.exists() else []
    seen_ids: set[str] = set()
    reproduced_by_runs: set[str] = set()

    allowed_types = {"smoke_test", "partial_reproduction", "claim_reproduction", "independent_test"}
    allowed_outcomes = {"success", "partial", "mismatch", "failed", "blocked"}

    for path in runs:
        run = load_yaml(path)
        prefix = f"{path.relative_to(ROOT)}"
        if run.get("schema_version") != 1:
            fail(f"{prefix}: schema_version must be 1")
        run_id = run.get("id")
        if not nonempty(run_id):
            fail(f"{prefix}: missing id")
        if run_id in seen_ids:
            fail(f"duplicate run id {run_id!r}")
        seen_ids.add(run_id)

        run_type = run.get("run_type")
        outcome = run.get("outcome")
        if run_type not in allowed_types:
            fail(f"{prefix}: invalid run_type {run_type!r}")
        if outcome not in allowed_outcomes:
            fail(f"{prefix}: invalid outcome {outcome!r}")

        source = run.get("source_project")
        if source not in sources:
            fail(f"{prefix}: unknown source_project {source!r}")

        claim = run.get("target_claim")
        if run_type in {"partial_reproduction", "claim_reproduction"} and claim not in claims:
            fail(f"{prefix}: reproduction run must reference a known target_claim")

        code = run.get("code") or {}
        if run_type != "independent_test":
            if not nonempty(code.get("repository")) or not nonempty(code.get("commit")):
                fail(f"{prefix}: reproduction runs require code repository and commit")
            if not COMMIT_RE.match(str(code.get("commit"))):
                fail(f"{prefix}: code.commit does not look like a commit SHA")

        if outcome in {"success", "partial", "mismatch"}:
            execution = run.get("execution") or {}
            metric = run.get("metric") or {}
            artifacts = run.get("artifacts") or {}
            for field, value in {
                "execution.command": execution.get("command"),
                "metric.name": metric.get("name"),
                "metric.observed_value": metric.get("observed_value"),
                "artifacts.raw_output_sha256": artifacts.get("raw_output_sha256"),
            }.items():
                if not nonempty(value):
                    fail(f"{prefix}: {field} required for outcome {outcome}")
            if not SHA256_RE.match(str(artifacts.get("raw_output_sha256"))):
                fail(f"{prefix}: raw_output_sha256 must be a 64-hex SHA256")

        if run_type == "claim_reproduction" and outcome in {"success", "mismatch"}:
            reproduced_by_runs.add(claim)

    missing_run = reproduced_here - reproduced_by_runs
    if missing_run:
        fail(
            "verification.yaml marks claims reproduced_here without a matching "
            f"successful/mismatch claim_reproduction run: {sorted(missing_run)}"
        )

    print(f"experiment records OK: {len(runs)} committed runs, {len(reproduced_by_runs)} claim reproductions.")


if __name__ == "__main__":
    main()
