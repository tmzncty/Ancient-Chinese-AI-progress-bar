#!/usr/bin/env python3
"""Validate the machine-readable Ancient Chinese AI capability matrix."""

from __future__ import annotations

import sys
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
PROGRESS_FILE = ROOT / "progress.yaml"


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)


def main() -> int:
    data = yaml.safe_load(PROGRESS_FILE.read_text(encoding="utf-8"))
    errors = 0

    if data.get("policy", {}).get("aggregate_score") is not False:
        fail("policy.aggregate_score must remain false")
        errors += 1

    capabilities = data.get("capabilities")
    sources = data.get("sources")

    if not isinstance(capabilities, list) or not capabilities:
        fail("capabilities must be a non-empty list")
        return 1
    if not isinstance(sources, dict) or not sources:
        fail("sources must be a non-empty mapping")
        return 1

    seen_ids: set[str] = set()

    for index, item in enumerate(capabilities, start=1):
        prefix = f"capabilities[{index}]"
        if not isinstance(item, dict):
            fail(f"{prefix} must be a mapping")
            errors += 1
            continue

        capability_id = item.get("id")
        if not isinstance(capability_id, str) or not capability_id.strip():
            fail(f"{prefix}.id must be a non-empty string")
            errors += 1
        elif capability_id in seen_ids:
            fail(f"duplicate capability id: {capability_id}")
            errors += 1
        else:
            seen_ids.add(capability_id)

        level = item.get("level")
        if not isinstance(level, int) or not 0 <= level <= 5:
            fail(f"{prefix}.level must be an integer from 0 to 5")
            errors += 1

        confidence = item.get("confidence")
        if confidence not in {"low", "medium", "high"}:
            fail(f"{prefix}.confidence must be low, medium, or high")
            errors += 1

        evidence = item.get("evidence")
        if not isinstance(evidence, list):
            fail(f"{prefix}.evidence must be a list")
            errors += 1
            continue

        if isinstance(level, int) and level > 0 and not evidence:
            fail(f"{prefix} has level {level} but no evidence")
            errors += 1

        for source_id in evidence:
            if source_id not in sources:
                fail(f"{prefix} references unknown source: {source_id}")
                errors += 1

    for source_id, source in sources.items():
        if not isinstance(source, dict):
            fail(f"source {source_id} must be a mapping")
            errors += 1
            continue
        if not source.get("title"):
            fail(f"source {source_id} has no title")
            errors += 1
        url = source.get("url")
        if not isinstance(url, str) or not url.startswith(("https://", "http://")):
            fail(f"source {source_id} has an invalid URL")
            errors += 1
        if not source.get("type"):
            fail(f"source {source_id} has no type")
            errors += 1

    if errors:
        print(f"progress.yaml validation failed with {errors} error(s).", file=sys.stderr)
        return 1

    print(
        f"progress.yaml OK: {len(capabilities)} capabilities, "
        f"{len(sources)} evidence sources."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
