#!/usr/bin/env python3
"""Validate the bounded file surface for the approved barracks runtime transition."""
from __future__ import annotations

import argparse
import json
import subprocess
from pathlib import Path
from typing import Iterable

RUNTIME_ACTION = "BARRACKS_ROLE_OUTPUT_RUNTIME_IMPLEMENTATION_PACKAGE"
PROTECTED_PREFIXES = ("data/", "scripts/", "scenes/", "assets/", "addons/")
APPROVED_RUNTIME_PROTECTED = {
    "scripts/battle/battle_simulator.gd",
    "scripts/battle/lane_state.gd",
    "scripts/battle/unit_instance.gd",
}
APPROVED_RUNTIME_SUPPORT = {
    ".gitattributes",
    ".github/workflows/validate-active-integrated-contract-v4-4.yml",
    ".github/workflows/validate-base-v9-adoption.yml",
    ".github/workflows/validate-project-base-adapter.yml",
    "tests/gut/test_barracks_role_output.gd",
    "tests/gut/test_barracks_role_output.gd.uid",
    "tests/headless/barracks_role_output_fv_test.gd",
    "tests/headless/barracks_role_output_fv_test.gd.uid",
    "tests/python/test_barracks_functional_value_combat_numerics_review.py",
    "tests/python/test_barracks_godot_471_preflight.py",
    "tests/python/test_barracks_role_output_runtime_implementation_package.py",
    "tests/python/test_base_recovery_map.py",
    "tests/python/test_runtime_transition_scope.py",
    "tools/invoke_barracks_role_output_executor.ps1",
    "tools/reconcile_and_invoke_barracks_role_output_executor.ps1",
    "tools/validate_runtime_transition_scope.py",
}
APPROVED_RUNTIME_FILES = APPROVED_RUNTIME_PROTECTED | APPROVED_RUNTIME_SUPPORT


def _is_protected(path: str) -> bool:
    return path == "project.godot" or path.startswith(PROTECTED_PREFIXES)


def validate_runtime_transition(state: dict, changed_files: Iterable[str]) -> list[str]:
    changed = {path.strip().replace("\\", "/") for path in changed_files if path.strip()}
    gate = state.get("entry_gate", {})
    allowed = gate.get("allowed_next_actions", [])
    if RUNTIME_ACTION not in allowed:
        return [f"active gate does not authorize {RUNTIME_ACTION}"]

    errors: list[str] = []
    unexpected = sorted(changed - APPROVED_RUNTIME_FILES)
    if unexpected:
        errors.append(f"runtime transition contains unapproved files: {unexpected}")

    protected = {path for path in changed if _is_protected(path)}
    unexpected_protected = sorted(protected - APPROVED_RUNTIME_PROTECTED)
    if unexpected_protected:
        errors.append(f"runtime transition contains unapproved protected paths: {unexpected_protected}")
    if not (protected & APPROVED_RUNTIME_PROTECTED):
        errors.append("runtime transition does not contain an approved runtime protected-path change")
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
    parser.add_argument(
        "--state",
        type=Path,
        default=Path("docs/operations/ACTIVE_INTEGRATED_CONTRACT_STATE.v1.json"),
    )
    parser.add_argument("--base", required=True)
    parser.add_argument("--head", default="HEAD")
    args = parser.parse_args()

    state = json.loads(args.state.read_text(encoding="utf-8"))
    changed = changed_files_from_git(args.base, args.head)
    errors = validate_runtime_transition(state, changed)
    if errors:
        print("approved_runtime_transition=FAIL")
        for error in errors:
            print(f"- {error}")
        return 1
    protected_count = sum(1 for path in changed if _is_protected(path))
    print(
        "approved_runtime_transition=PASS "
        f"changed_files={len(changed)} protected_runtime_paths={protected_count}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
