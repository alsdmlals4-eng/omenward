#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STATE_PATH = ROOT / "docs/operations/BASE_WHOLE_REPOSITORY_AND_SKILL_MAP.v1.json"
MATRIX_PATH = ROOT / "docs/operations/LOCAL_VERIFICATION_MATRIX.v1.json"

DECISION_ID = "OMW-DEC-20260807-PROCESS-BASE-REPOSITORY-SKILL-MAP-AND-LOCAL-VERIFICATION-PACK-V1"
BASE_SHA = "4f98f968a377f7b6a11aafa4fc94d11bddbebedc"
OMENWARD_SHA = "93c388ad1c50581671f8ea059357c863d8d8e0f7"
EXPECTED_ENV_IDS = {
    "windows-py311", "windows-py312", "windows-py313", "wsl2-ubuntu-py312"
}


def validate(root: Path = ROOT) -> list[str]:
    errors: list[str] = []
    state = json.loads((root / STATE_PATH.relative_to(ROOT)).read_text(encoding="utf-8"))
    matrix = json.loads((root / MATRIX_PATH.relative_to(ROOT)).read_text(encoding="utf-8"))

    checks = [
        (state.get("decision_id") == DECISION_ID, "decision_id mismatch"),
        (state.get("base_repository_commit") == BASE_SHA, "Base commit mismatch"),
        (state.get("omenward_repository_base_commit") == OMENWARD_SHA, "OMENWARD base mismatch"),
        (state.get("recovery_status") == "INCOMPLETE", "recovery must remain INCOMPLETE"),
        (state.get("base_recovery_blocker_cleared") is False, "Base blocker must remain uncleared"),
        (state.get("entry_gate") == "BLOCK", "entry gate must remain BLOCK"),
        (state.get("root_inventory_count") == len(state.get("root_inventory", [])), "root count mismatch"),
        (state.get("skill_entrypoint_count") == len(state.get("skill_entrypoints", [])), "skill count mismatch"),
        (state.get("workflow_count") == len(state.get("workflow_files", [])), "workflow count mismatch"),
        (bool(state.get("unread_or_partially_read_surfaces")), "unread list must not be empty"),
        (matrix.get("decision_id") == DECISION_ID, "matrix Decision mismatch"),
        (matrix.get("entry_gate") == "BLOCK", "matrix entry gate must remain BLOCK"),
    ]
    errors.extend(message for ok, message in checks if not ok)

    unread = state.get("unread_or_partially_read_surfaces", [])
    if any(row.get("gate_effect") != "BLOCKED" for row in unread):
        errors.append("every unread surface must block the gate")

    environments = matrix.get("environments", [])
    if {row.get("environment_id") for row in environments} != EXPECTED_ENV_IDS:
        errors.append("local environment matrix mismatch")
    if any(row.get("execution_status") != "NOT_RUN_USER_LOCAL" for row in environments):
        errors.append("user-local execution status must remain NOT_RUN_USER_LOCAL in canonical matrix")

    required = [
        "tools/run_local_verification_pack.py",
        "tools/run_local_verification_pack.ps1",
        "tools/run_local_verification_pack_wsl.sh",
        "tests/python/test_base_recovery_and_local_verification_pack.py",
    ]
    for relative in required:
        if not (root / relative).is_file():
            errors.append(f"missing required file: {relative}")
    return errors


def main() -> int:
    errors = validate()
    if errors:
        for error in errors:
            print(f"base_recovery_local_pack=FAIL {error}")
        return 1
    print(
        "base_recovery_local_pack=PASS "
        "recovery=INCOMPLETE local=NOT_RUN_USER_LOCAL entry_gate=BLOCK"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
