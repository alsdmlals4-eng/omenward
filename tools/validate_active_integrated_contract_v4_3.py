#!/usr/bin/env python3
"""Validate the active OMENWARD integrated contract v4.3 binding."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Iterable

ROOT = Path(__file__).resolve().parents[1]
STATE_PATH = Path("docs/operations/ACTIVE_INTEGRATED_CONTRACT_STATE.v1.json")
DECISION_ID = "OMW-DEC-20260806-PROCESS-ACTIVATE-INTEGRATED-CONTRACT-V4-3-V1"
CONTRACT_NAME = "PROJECT_TOTAL_PLANNING_IMPLEMENTATION_AND_DELIVERY_INSTRUCTION"
CONTRACT_VERSION = "4.3"
CONTRACT_STATUS = "ACTIVE_INTEGRATED_AUDIT_IMPLEMENTATION_DELIVERY_CONTRACT"
REPOSITORY_MAIN_SHA = "7588317f294d602cfad5f7f15bfebcf849b8a77b"
BASE_MAIN_SHA = "4f98f968a377f7b6a11aafa4fc94d11bddbebedc"
AUDIO_VAULT_PATH = "C:/Users/user/Documents/GitHub/shered audio vault"
REVIEW_MODEL = "GPT_ROLE_SEPARATED_PLUS_USER_DECISION_AUTHORITY"

REQUIRED_BLOCKERS = {
    "BASE_WHOLE_REPOSITORY_AND_SKILL_RECOVERY_NOT_COMPLETED",
    "CANON_LEDGER_STALE",
    "PENDING_DECISIONS_STALE",
    "PR154_CONDITIONAL_FAIL_UNMERGED",
    "IMAGE_REVIEW_NOT_CLOSED",
    "GUT_ADOPTION_SPEC_NOT_MERGED",
    "PR155_V4_3_SCOPE_ALIGNMENT_REQUIRED",
    "PR156_SEQUENCE_BLOCKED_UNTIL_ADOPTION_SPEC_MERGED",
    "HIGODOT_SOURCE_OR_VERSION_UNVERIFIED",
    "GODOT_EXACT_4_7_VERSION_UNVERIFIED",
    "AUDIO_VAULT_PATH_UNVERIFIED",
    "GITHUB_ACTIONS_BILLING_PRE_START",
}
REQUIRED_FORBIDDEN_ACTIONS = {
    "PRODUCT_IMPLEMENTATION",
    "GODOT_AUTHORING_MUTATION",
    "FORMAL_GUT_EXECUTION",
    "GUT_PLUGIN_ENABLEMENT",
    "AUDIO_ASSET_IMPORT_OR_RUNTIME_REFERENCE",
    "MARK_PR155_OR_PR156_READY",
    "MERGE_PR155_OR_PR156",
    "LOCAL_MAIN_SYNC",
    "GODOT_RUNTIME_CLAIM",
}


def load_state(root: Path = ROOT) -> dict[str, Any]:
    return json.loads((root / STATE_PATH).read_text(encoding="utf-8"))


def validate_state(data: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    if data.get("decision_id") != DECISION_ID:
        errors.append("Decision ID mismatch")
    if data.get("repository_main_sha") != REPOSITORY_MAIN_SHA:
        errors.append("repository main SHA mismatch")
    if data.get("base_repository_main_sha") != BASE_MAIN_SHA:
        errors.append("Base main SHA mismatch")

    active = data.get("active_contract", {})
    if active.get("name") != CONTRACT_NAME:
        errors.append("active contract name mismatch")
    if active.get("version") != CONTRACT_VERSION:
        errors.append("active contract version must be 4.3")
    if active.get("declared_status") != CONTRACT_STATUS:
        errors.append("active contract declared status mismatch")
    if active.get("binding_status") != "ACTIVE":
        errors.append("contract binding must be ACTIVE")
    if active.get("activation_authority") != "USER_DIRECT_APPROVAL_IN_CURRENT_CONVERSATION":
        errors.append("contract activation authority mismatch")
    if active.get("counter") != "NON_COUNTER":
        errors.append("contract binding must be NON_COUNTER")

    superseded = data.get("superseded_contracts", [])
    if not superseded or superseded[0].get("version") != "4.2":
        errors.append("v4.2 supersession record missing")
    elif superseded[0].get("status") != "HISTORICAL_COMPARISON_ONLY":
        errors.append("v4.2 must be historical comparison only")

    gate = data.get("entry_gate", {})
    if gate.get("decision") != "BLOCK":
        errors.append("entry gate must remain BLOCK")
    if gate.get("status") != "ENTRY_STATE_RECONCILIATION_BLOCKING_GATE_ACTIVE":
        errors.append("entry blocking gate status mismatch")
    if gate.get("decision_ledger_readback", {}).get("status") != "STALE_CANON_CONFLICT":
        errors.append("Decision Ledger stale conflict must remain explicit")
    if gate.get("unresolved_list_readback", {}).get("status") != "STALE_RELATIVE_TO_PR154_4_OF_10":
        errors.append("unresolved list stale status mismatch")
    image = gate.get("image_review_sheet_readback", {})
    if image.get("ready_count") != 0 or image.get("awaiting_count") != 0:
        errors.append("image review READY/AWAITING counts must reflect readback")
    if image.get("in_review_not_generated_count") != 1:
        errors.append("image review in-review count mismatch")
    if image.get("rejected_project_mismatch_count") != 6:
        errors.append("image rejection count mismatch")

    blockers = set(gate.get("blocking_reasons", []))
    if not REQUIRED_BLOCKERS.issubset(blockers):
        errors.append("entry blockers incomplete")
    forbidden = set(gate.get("forbidden_actions", []))
    if not REQUIRED_FORBIDDEN_ACTIONS.issubset(forbidden):
        errors.append("forbidden action set incomplete")

    authority = data.get("tool_authority", {})
    higodot = authority.get("higodot", {})
    gut = authority.get("gut", {})
    if higodot.get("authority") != "SINGLE_GODOT_SCENE_NODE_RESOURCE_PROJECT_SETTINGS_AUTHOR":
        errors.append("HiGodot authoring authority mismatch")
    if higodot.get("status") != "HIGODOT_SOURCE_OR_VERSION_UNVERIFIED":
        errors.append("HiGodot must remain unverified")
    if gut.get("version") != "9.7.1" or gut.get("source_branch") != "godot_4_7":
        errors.append("GUT version/source branch mismatch")
    if gut.get("adoption_spec_merge_status") != "NOT_MERGED":
        errors.append("GUT adoption spec must remain not merged")
    if gut.get("formal_execution_status") != "BLOCKED_BY_GUT_ADOPTION_SPEC":
        errors.append("formal GUT execution must remain blocked")
    if gut.get("bootstrap_python_test_status") != "BOOTSTRAP_CONTRACT_TEST_ONLY_NOT_FORMAL_GUT":
        errors.append("bootstrap Python tests must not be called formal GUT")
    if authority.get("role_overlap") != "FORBIDDEN":
        errors.append("HiGodot/GUT role overlap must be FORBIDDEN")
    if authority.get("production_mutation_by_gut") != "FORBIDDEN":
        errors.append("GUT production mutation must be forbidden")

    review = data.get("review_authority", {})
    if review.get("model") != REVIEW_MODEL:
        errors.append("review model mismatch")
    if review.get("external_independent_reviewer") != "NOT_PLANNED_SOLO_DEVELOPMENT":
        errors.append("external reviewer status mismatch")

    audio = data.get("audio_vault", {})
    if audio.get("path") != AUDIO_VAULT_PATH:
        errors.append("audio Vault path must preserve user spelling")
    if audio.get("status") != "BLOCKED_UNVERIFIED":
        errors.append("audio Vault must remain blocked-unverified")
    if audio.get("runtime_reference_policy") != "COPY_APPROVED_ASSETS_INTO_RES_NOT_ABSOLUTE_PATH":
        errors.append("audio runtime reference policy mismatch")

    local = data.get("local_delivery", {})
    if local.get("local_sync") != "LOCAL_SYNC_BLOCKED_NO_LOCAL_ACCESS":
        errors.append("local sync access boundary mismatch")
    if local.get("godot_run") != "GODOT_RUN_BLOCKED_NO_LOCAL_ACCESS":
        errors.append("Godot run access boundary mismatch")
    return errors


def main(argv: Iterable[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--contract", action="store_true")
    args = parser.parse_args(list(argv) if argv is not None else None)
    try:
        state = load_state(ROOT)
    except (OSError, json.JSONDecodeError) as exc:
        print(f"active_contract=FAILED error={exc}")
        return 1
    errors = validate_state(state)
    if errors:
        print("active_contract=FAILED")
        for error in errors:
            print(f"- {error}")
        return 1
    print("active_contract=PASS version=4.3 application_binding=ACTIVE entry_gate=BLOCK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
