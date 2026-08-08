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
ADAPTER_FRESHNESS_DECISION = "OMW-DEC-20260808-PROCESS-PROJECT-BASE-ADAPTER-FRESHNESS-RECONCILIATION-V1"
BARRACKS_REMEDIATION_DECISION = "OMW-DEC-20260808-PLANNING-BARRACKS-CAPABILITY-PROXY-AND-MULTI-SPECIAL-TOKEN-BURST-REMEDIATION-V1"
BARRACKS_10K_REVIEW_DECISION = "OMW-DEC-20260808-PLANNING-BARRACKS-10000-SEED-DECISION-SWEEP-REVIEW-V1"
BARRACKS_OBSERVABLES_DECISION = "OMW-DEC-20260808-PLANNING-BARRACKS-PARAMETER-SELECTION-OBSERVABLES-DEFINITION-V1"
BASE_RECOVERY_SHA = "fa69a77a14f923a756064f6ae151d34cadb374f7"
SOURCE_MAIN_SHA = "25c4a5953d57acce450c93db1a8b5f0281937586"
BASE_CURRENT_OBSERVED = "a912cc001ff4d4e3415fb4b4931723c49eb08d9a"
ADAPTER_BASELINE_MAIN = "1f23981fdfc3e965ff46c8866e978c4701eb3d4e"
PROTECTED_POLICY_SHA = "1c36c4180b85d6bd97f4e7cdba908cc73298f529d368aa07e0dffde6e1e8ec52"
RECONCILIATION_BRANCH = "planning/barracks-parameter-selection-observables-20260808-final"
RESULT_JSON_SHA = "a02c4e0bad6a7113937fbd23f4521c364d109944c7f05c94eb5839b9119d00e2"
RESULT_CSV_SHA = "3b6a164a4ca847d29b82d73b3841100f246cdc36b9b86f30198bfcfe586f6560"

REQUIRED_BLOCKERS = {
    "BARRACKS_FUNCTIONAL_VALUE_COMBAT_NUMERICS_REQUIRED",
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
    if data.get("last_gate_update_decision") != BARRACKS_OBSERVABLES_DECISION:
        errors.append("last gate update Decision mismatch")
    if data.get("source_repository_main_sha") != SOURCE_MAIN_SHA:
        errors.append("source main SHA mismatch")
    if data.get("base_repository_main_sha") != BASE_RECOVERY_SHA:
        errors.append("Base recovery SHA mismatch")
    if data.get("base_current_main_observed") != BASE_CURRENT_OBSERVED:
        errors.append("Base current observed SHA mismatch")
    if data.get("reconciliation_branch") != RECONCILIATION_BRANCH:
        errors.append("reconciliation branch provenance mismatch")
    if "working_branch" in data:
        errors.append("working_branch must not persist in durable active state")

    active = data.get("active_contract", {})
    if active.get("version") != "4.4" or active.get("binding_status") != "ACTIVE":
        errors.append("active v4.4 binding mismatch")
    if active.get("activation_authority") != "USER_DIRECT_APPROVAL_IN_CURRENT_CONVERSATION":
        errors.append("contract activation authority mismatch")

    gate = data.get("entry_gate", {})
    if gate.get("decision") != "BLOCK":
        errors.append("entry gate must remain BLOCK")
    if gate.get("decision_ledger_readback", {}).get("status") != "RECONCILED_BY_V4_4_THROUGH_BARRACKS_7_OF_10_OBSERVABLES":
        errors.append("Decision Ledger reconciliation status mismatch")
    if gate.get("unresolved_list_readback", {}).get("status") != "CURRENT_ROBUSTNESS_REVIEW_AND_FUNCTIONAL_VALUE_DEFERRED_GATE":
        errors.append("unresolved list current status mismatch")
    blockers = set(gate.get("blocking_reasons", []))
    if not REQUIRED_BLOCKERS.issubset(blockers):
        errors.append("entry blockers incomplete")
    for stale in ("BARRACKS_10000_SEED_DECISION_SWEEP_REVIEW_REQUIRED", "BARRACKS_PARAMETER_SELECTION_IDENTIFIABILITY_REQUIRED"):
        if stale in blockers:
            errors.append(f"completed barracks blocker must not persist: {stale}")
    allowed = gate.get("allowed_next_actions", [])
    if not allowed or allowed[0] != "BARRACKS_10000_SEED_ROBUSTNESS_ONLY_REVIEW":
        errors.append("robustness-only 10k review must be first allowed action")
    forbidden = set(gate.get("forbidden_actions", []))
    for required in (
        "PRODUCT_IMPLEMENTATION",
        "GODOT_AUTHORING_MUTATION",
        "BARRACKS_10000_SEED_PARAMETER_SELECTION_EXECUTION",
        "BARRACKS_50000_SEED_CONFIRMATION",
    ):
        if required not in forbidden:
            errors.append(f"required forbidden action missing: {required}")
    image = gate.get("image_review_sheet_readback", {})
    if image.get("ready_count") != 0 or image.get("awaiting_count") != 0:
        errors.append("image READY/AWAITING counts must remain zero")

    recovery = data.get("base_recovery", {})
    if recovery.get("decision_id") != BASE_RECOVERY_DECISION or recovery.get("base_exact_commit") != BASE_RECOVERY_SHA:
        errors.append("Base recovery identity mismatch")
    if recovery.get("status") != "COMPLETE" or recovery.get("blocker_cleared") is not True:
        errors.append("Base recovery completion not propagated")

    adapter = data.get("project_base_adapter", {})
    if adapter.get("decision_id") != ADAPTER_FRESHNESS_DECISION:
        errors.append("project Base adapter Decision mismatch")
    if adapter.get("protected_baseline_commit") != ADAPTER_BASELINE_MAIN or adapter.get("protected_policy_sha256") != PROTECTED_POLICY_SHA:
        errors.append("project Base adapter protected baseline mismatch")
    if adapter.get("gdd_sheet_sync_status") != "CURRENT" or adapter.get("status") != "FRESHNESS_RECONCILED" or adapter.get("blocker_cleared") is not True:
        errors.append("project Base adapter freshness completion not propagated")

    barracks = data.get("barracks_remediation", {})
    if barracks.get("decision_id") != BARRACKS_REMEDIATION_DECISION:
        errors.append("barracks remediation Decision mismatch")
    if barracks.get("smoke_rerun_status") != "PASS" or barracks.get("failed_decision_gates") != []:
        errors.append("barracks 2k remediation PASS must remain propagated")
    if float(barracks.get("observed_baseline_special_token_share_burst_max", 1.0)) > 0.45:
        errors.append("barracks token burst exceeds approved cap")
    if barracks.get("result_json_sha256") != RESULT_JSON_SHA or barracks.get("result_csv_sha256") != RESULT_CSV_SHA:
        errors.append("barracks evidence hash mismatch")
    if barracks.get("confirmation_sweep_50000") != "BLOCKED" or barracks.get("selected_parameter_vector") is not None:
        errors.append("barracks final selection boundary mismatch")
    if barracks.get("product_implementation") != "NOT_AUTHORIZED":
        errors.append("product implementation must remain unauthorized")

    review = data.get("barracks_10000_review", {})
    if review.get("decision_id") != BARRACKS_10K_REVIEW_DECISION or review.get("parent_decision_id") != BARRACKS_REMEDIATION_DECISION:
        errors.append("10k review Decision lineage mismatch")
    if review.get("decision_sweep_10000_execution") != "NOT_AUTHORIZED" or review.get("confirmation_sweep_50000") != "BLOCKED":
        errors.append("10k review execution boundary mismatch")
    if review.get("final_parameter_vector") is not None:
        errors.append("10k review must not select final parameter vector")

    obs = data.get("barracks_parameter_selection_observables", {})
    if obs.get("decision_id") != BARRACKS_OBSERVABLES_DECISION or obs.get("parent_decision_id") != BARRACKS_10K_REVIEW_DECISION:
        errors.append("observables Decision lineage mismatch")
    if obs.get("baseline_main") != SOURCE_MAIN_SHA or obs.get("base_current_main_observed") != BASE_CURRENT_OBSERVED:
        errors.append("observables provenance mismatch")
    if obs.get("comparison_form") != "VECTOR_GOLD_TIME_FOOD_NODE_NO_SINGLE_WEIGHTED_SCORE":
        errors.append("observables comparison form mismatch")
    if obs.get("selection_mode") != "HARD_FILTER_THEN_PARETO":
        errors.append("observables selection mode mismatch")
    if obs.get("special_interval_canon_gate") != "STRICTLY_LONGER_THAN_RELEVANT_GENERAL_INTERVAL":
        errors.append("special interval canon gate mismatch")
    if obs.get("excluded_vectors_interval_fail") != ["V01_CHEAP_FAST_LOW", "V02_CHEAP_FAST_HIGH", "V05_EXPENSIVE_FAST_LOW", "V06_EXPENSIVE_FAST_HIGH"]:
        errors.append("interval-fail exclusion set mismatch")
    if obs.get("pareto_dominated_vectors") != ["V07_EXPENSIVE_SLOW_LOW", "V08_EXPENSIVE_SLOW_HIGH"]:
        errors.append("Pareto dominated vector set mismatch")
    if obs.get("economy_production_envelope") != "V00_BASELINE_COST_INTERVAL_ONLY":
        errors.append("economy-production envelope mismatch")
    if float(obs.get("robustness_special_barracks_cost_gold", 0)) != 60.0 or float(obs.get("robustness_special_interval_multiplier", 0)) != 1.70:
        errors.append("robustness envelope numeric mismatch")
    if obs.get("special_functional_value_index") != "DEFERRED_UNTIL_PRODUCT_COMBAT_NUMERICS":
        errors.append("functional value must remain deferred")
    if obs.get("final_parameter_vector") is not None:
        errors.append("observables gate must not select final 3D vector")
    if obs.get("robustness_only_10000") != "READY_FOR_SEPARATE_APPROVAL":
        errors.append("robustness-only readiness mismatch")
    if obs.get("parameter_selection_10000") != "NOT_AUTHORIZED" or obs.get("confirmation_sweep_50000") != "BLOCKED":
        errors.append("post-observables execution boundary mismatch")
    if obs.get("next_gate") != "BARRACKS_10000_SEED_ROBUSTNESS_ONLY_REVIEW":
        errors.append("observables next gate mismatch")

    tools = data.get("tool_authority", {})
    if tools.get("higodot", {}).get("authority") != "SOLE_PERSISTENT_GODOT_AUTHORING_AUTHORITY":
        errors.append("HiGodot authority mismatch")
    if tools.get("gut", {}).get("authority") != "DETERMINISTIC_GDSCRIPT_TEST_AUTHORITY_WHEN_ADOPTED":
        errors.append("GUT authority mismatch")
    if tools.get("hera", {}).get("role") != "LIVE_QA_AND_OBSERVABILITY_ONLY" or tools.get("hera", {}).get("persistent_source_mutation") != "FORBIDDEN":
        errors.append("Hera role boundary mismatch")
    if data.get("local_delivery", {}).get("status") != "BLOCKED_UNVERIFIED":
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
    print("active_contract_v4_4=PASS application_binding=ACTIVE entry_gate=BLOCK barracks_5_of_10=SMOKE_PASS review_6_of_10=COMPLETE observables_7_of_10=DEFINED next=ROBUSTNESS_ONLY_10K_REVIEW")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
