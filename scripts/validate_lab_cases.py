#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import sys
import yaml

ROOT = Path(__file__).resolve().parents[1]
CASES = ROOT / "lab" / "cases.yaml"


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def main() -> None:
    with CASES.open("r", encoding="utf-8") as fh:
        data = yaml.safe_load(fh)

    if data.get("schema_version") != 1:
        fail("lab/cases.yaml schema_version must be 1")

    cases = data.get("cases") or []
    if not cases:
        fail("lab/cases.yaml must contain cases")

    allowed_scoring = set((data.get("scoring_modes") or {}).keys())
    ids = set()
    categories = set()

    for case in cases:
        case_id = case.get("id")
        if not case_id:
            fail("every lab case needs id")
        if case_id in ids:
            fail(f"duplicate lab case id: {case_id}")
        ids.add(case_id)

        category = case.get("category")
        if not category:
            fail(f"case {case_id}: missing category")
        categories.add(category)

        if not case.get("title") or not case.get("prompt"):
            fail(f"case {case_id}: missing title or prompt")

        oracle = case.get("oracle") or {}
        if oracle.get("scoring") not in allowed_scoring:
            fail(f"case {case_id}: invalid scoring mode {oracle.get('scoring')!r}")
        if len(oracle) < 2:
            fail(f"case {case_id}: oracle needs behavior/invariant constraints")

        failures = case.get("failure_if") or []
        if not failures:
            fail(f"case {case_id}: must define at least one explicit failure condition")

    print(f"lab/cases.yaml OK: {len(cases)} cases across {len(categories)} failure categories.")


if __name__ == "__main__":
    main()
