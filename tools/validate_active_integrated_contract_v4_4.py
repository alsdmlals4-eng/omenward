#!/usr/bin/env python3
"""Validate the active OMENWARD integrated contract v4.4 reconciliation state."""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
STATE_PATH = ROOT / "docs/operations/ACTIVE_INTEGRATED_CONTRACT_STATE.v1.json"
DECISION_ID = "OMW-DEC-20260808-PROCESS-ACTIVATE-INTEGRATED-CONTRACT-V4-4-AND-RECONCILE-ENTRY-STATE-V1"
BASE_RECOVERY_DECISION = "OMW-DEC-20260807-PROCESS-BASE-REPOSITORY-SKILL-MAP-AND-LOCAL-VERIFICATION-PACK-V1"
BASE_SHA = "fa69a77a14f923a756064f6ae151d34cadb374f7"
SOURCE_MAIN_SHA = "7b41923628b68c7c1477b286584973d8516eab6d"
RECONCILIATION_BRANCH = "process/v4-4-entry-reconciliation-20260808"

REQUIRED_BLOCKERS = {
    "PROJECT_BASE_ADAPTER_FRESHNESS_FIX_REQUIRED",
    "PR154_CONDITIONAL_FAIL_UNMERGED",
    "GUT_ADOPTION_SPEC_PR155_NOT_MERGED",
    "HIGODOT_EXACT_SOURCE_OR_VERSION_UNVERIFIED",
    "HERA_PRESENT_BUT_ADOPTION_NOT_VERIFIED",
    "DIRECT_MAIN_HERA_IMPORT_NOT_YET_DISPOSITIONED",
    "LOCAL_GODOT_AND_AUDIO_VAULT_UNAVAILABLE",
}


def load_state() -> dict[str, Any]:
    return json.loads(STATE_PATH.read_text(encoding="utf-8"))


def validate_state(data: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    if data.get("decision_id") != DECISION_ID:
        errors.append("Decision ID mismatch")
    if data.get("last_gate_update_decision") != BASE_RECOVERY_DECISION:
        errors.append("last gate update Decision mismatch")
    if data.get("source_repository_main_sha") != SOURCE_MAIN_SHA:
        errors.append("source main SHA mismatch")
    if data.get("base_repository_main_sha") != BASE_SHA:
        errors.append("Base main SHA mismatch")
    if "working_branch" in data:
        errors.append("working_branch must not persist in durable active state")
    if data.get("reconciliation_branch") != RECONCILIATION_BRANCH:
        errors.append("reconciliation branch provenance mismatch")

    active = data.get("active_contract", {})
    if active.get("version") != "4.4":
        errors.append("active contract version must be 4.4")
    if active.get("binding_status") != "ACTIVE":
        errors.append("contract binding must be ACTIVE")
    if active.get("activation_authority") != "USER_DIRECT_APPROVAL_IN_CURRENT_CONVERSATION":
        errors.append("contract activation authority mismatch")

    gate = data.get("entry_gate", {})
    if gate.get("decision") != "BLOCK":
        errors.append("entry gate must remain BLOCK")
    if gate.get("decision_ledger_readback", {}).get("status") != "RECONCILED_BY_V4_4_DECISION_AND_PR159_GATE_UPDATE":
        errors.append("Decision Ledger reconciliation status mismatch")
    blockers = set(gate.get("blocking_reasons", []))
    allowed = set(gate.get("allowed_next_actions", []))
    if "RECONCILIATION_DECISION_NOT_MERGED" in blockers:
        errors.append("self-stale reconciliation merge blocker must not persist")
    if "BASE_RECOVERY_PR159_DRAFT_INCOMPLETE" in blockers:
        errors.append("merged PR159 Base recovery blocker must not persist")
    if "PR159_BASE_RECOVERY_COMPLETION" in allowed:
        errors.append("completed PR159 action must not persist")
    if "PROJECT_BASE_ADAPTER_FRESHNESS_RECONCILIATION" not in allowed:
        errors.append("project Base adapter freshness action missing")
    if gate.get("unresolved_list_readback", {}).get("status") != "CURRENT_10_OF_10_NEXT_SIMULATION_GATE":
        errors.append("unresolved list current status mismatch")
    image = gate.get("image_review_sheet_readback", {})
    if image.get("ready_count") != 0 or image.get("awaiting_count") != 0:
        errors.append("image READY/AWAITING counts must remain zero")
    if not REQUIRED_BLOCKERS.issubset(blockers):
        errors.append("entry blockers incomplete")

    recovery = data.get("base_recovery", {})
    if recovery.get("decision_id") != BASE_RECOVERY_DECISION:
        errors.append("Base recovery Decision mismatch")
    if recovery.get("status") != "COMPLETE" or recovery.get("blocker_cleared") is not True:
        errors.append("Base recovery completion not propagated")
    if recovery.get("tracked_file_classification") != "ZERO_UNCLASSIFIED":
        errors.append("Base tracked-file classification status mismatch")
    if recovery.get("followup") != "PROJECT_BASE_ADAPTER_FRESHNESS_FIX_REQUIRED":
        errors.append("Base recovery followup mismatch")

    actions = data.get("github_actions", {})
    if "current_reconciliation_head" in actions:
        errors.append("self-stale exact-head status must not persist in active state")
    if actions.get("repository_visibility") != "PUBLIC_CONFIRMED":
        errors.append("repository visibility status mismatch")

    tools = data.get("tool_authority", {})
    if tools.get("higodot", {}).get("authority") != "SOLE_PERSISTENT_GODOT_AUTHORING_AUTHORITY":
        errors.append("HiGodot authority mismatch")
    if tools.get("gut", {}).get("authority") != "DETERMINISTIC_GDSCRIPT_TEST_AUTHORITY_WHEN_ADOPTED":
        errors.append("GUT authority mismatch")
    if tools.get("hera", {}).get("role") != "LIVE_QA_AND_OBSERVABILITY_ONLY":
        errors.append("Hera role mismatch")
    if tools.get("hera", {}).get("persistent_source_mutation") != "FORBIDDEN":
        errors.append("Hera persistent mutation must be forbidden")

    local = data.get("local_delivery", {})
    if local.get("status") != "BLOCKED_UNVERIFIED":
        errors.append("local delivery must remain BLOCKED_UNVERIFIED")
    return errors


def main() -> int:
    try:
        data = load_state()
    except (OSError, json.JSONDecodeError) as exc:
        print(f"active_contract_v4_4=FAILED error={exc}")
        return 1
    errors = validate_state(data)
    if errors:
        print("active_contract_v4_4=FAILED")
        for error in errors:
            print(f"- {error}")
        return 1
    print("active_contract_v4_4=PASS application_binding=ACTIVE entry_gate=BLOCK base_recovery=COMPLETE")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
