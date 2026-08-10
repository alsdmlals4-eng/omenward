#!/usr/bin/env python3
"""Validate the exact bounded file surface for the approved v4.5 canon-freshness transition."""
from __future__ import annotations

import argparse
import subprocess
from typing import Iterable

PROTECTED_PREFIXES = ("data/", "scripts/", "scenes/", "assets/", "addons/")
HISTORICAL_V44_AUTHORITY = {
    "docs/process/ACTIVE_INTEGRATED_CONTRACT_BINDING_2026-08-06.md",
    "docs/operations/ACTIVE_INTEGRATED_CONTRACT_STATE.v1.json",
}
APPROVED_FILES = {
    ".github/workflows/validate-active-integrated-contract-v4-4.yml",
    ".github/workflows/validate-canon-freshness-v4-5.yml",
    "AGENTS.md",
    "docs/ACTIVE_CONTEXT.md",
    "docs/CURRENT_IMPLEMENTATION_STATUS.md",
    "docs/DECISIONS_PENDING.md",
    "docs/DOCUMENTATION_MAP.md",
    "docs/DOCUMENT_LIFECYCLE_REGISTRY.md",
    "docs/OMENWARD_GDD_CURRENT_CANON.md",
    "docs/ONBOARDING_PLANNING_CURRENT_AUTHORITY.md",
    "docs/PROJECT_CANON_DECISION_LEDGER.md",
    "docs/PROJECT_CORE.md",
    "docs/PROJECT_GOOGLE_SHEET_WORKBOOK.md",
    "docs/design/APPROVED_OMENWARD_BUILDING_TIER_REALIGNMENT_2026-08-06.md",
    "docs/operations/ACTIVE_INTEGRATED_CONTRACT_STATE.v2.json",
    "docs/operations/CANON_FRESHNESS_V45_SHEET_SYNC_EVIDENCE_2026-08-11.json",
    "docs/process/ACTIVE_INTEGRATED_CONTRACT_BINDING_2026-08-11.md",
    "docs/process/APPROVED_OMENWARD_CANON_FRESHNESS_AND_V4_5_THIN_ADAPTER_2026-08-11.md",
    "docs/process/PROJECT_TOTAL_PLANNING_IMPLEMENTATION_AND_DELIVERY_INSTRUCTION_v4.5_r2.md",
    "docs/superpowers/plans/2026-08-11-canon-freshness-v45-routing.md",
    "tests/python/test_canon_freshness_v45_routing.py",
    "tests/python/test_canon_freshness_v45_scope.py",
    "tools/validate_canon_freshness_v45_scope.py",
}
REQUIRED_ANCHORS = {
    "docs/process/ACTIVE_INTEGRATED_CONTRACT_BINDING_2026-08-11.md",
    "docs/operations/ACTIVE_INTEGRATED_CONTRACT_STATE.v2.json",
    "docs/process/PROJECT_TOTAL_PLANNING_IMPLEMENTATION_AND_DELIVERY_INSTRUCTION_v4.5_r2.md",
    "docs/operations/CANON_FRESHNESS_V45_SHEET_SYNC_EVIDENCE_2026-08-11.json",
    "tests/python/test_canon_freshness_v45_routing.py",
    "tests/python/test_canon_freshness_v45_scope.py",
}


def _normalize(paths: Iterable[str]) -> set[str]:
    return {path.strip().replace("\\", "/") for path in paths if path.strip()}


def _is_protected_product(path: str) -> bool:
    return path == "project.godot" or path.startswith(PROTECTED_PREFIXES)


def validate_canon_freshness_scope(changed_files: Iterable[str]) -> list[str]:
    changed = _normalize(changed_files)
    errors: list[str] = []

    historical_mutations = sorted(changed & HISTORICAL_V44_AUTHORITY)
    if historical_mutations:
        errors.append(f"historical v4.4 authority mutation is forbidden: {historical_mutations}")

    protected = sorted(path for path in changed if _is_protected_product(path))
    if protected:
        errors.append(f"protected product paths are forbidden in v4.5 canon freshness scope: {protected}")

    unexpected = sorted(changed - APPROVED_FILES)
    if unexpected:
        errors.append(f"v4.5 canon freshness transition contains unapproved files: {unexpected}")

    missing = sorted(REQUIRED_ANCHORS - changed)
    if missing:
        errors.append(f"missing required v4.5 anchors: {missing}")

    return errors


def changed_files_from_git(base: str, head: str) -> list[str]:
    result = subprocess.run(
        ["git", "diff", "--name-only", f"{base}...{head}"],
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        check=False,
    )
    if result.returncode:
        raise RuntimeError(result.stderr.strip() or "git diff failed")
    return result.stdout.splitlines()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base", required=True)
    parser.add_argument("--head", default="HEAD")
    args = parser.parse_args()

    changed = changed_files_from_git(args.base, args.head)
    errors = validate_canon_freshness_scope(changed)
    if errors:
        print("canon_freshness_v45_scope=FAIL")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"canon_freshness_v45_scope=PASS changed_files={len(_normalize(changed))}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
