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
BARRACKS_ROBUSTNESS_REVIEW_DECISION = "OMW-DEC-20260808-PLANNING-BARRACKS-10000-SEED-ROBUSTNESS-ONLY-REVIEW-V1"
BARRACKS_ROBUSTNESS_EXECUTION_DECISION = "OMW-DEC-20260809-PLANNING-BARRACKS-10000-SEED-ROBUSTNESS-EXECUTION-V1"
BASE_RECOVERY_SHA = "fa69a77a14f923a756064f6ae151d34cadb374f7"
CURRENT_SOURCE_MAIN_SHA = "02260589e1aa374c19005d19e47ba1f3b27332bd"
CURRENT_BASE_MAIN_OBSERVED = "cf4c7a60c5b31b042043f91b268f381372fec69a"
ADAPTER_BASELINE_MAIN = "1f23981fdfc3e965ff46c8866e978c4701eb3d4e"
PROTECTED_POLICY_SHA = "1c36c4180b85d6bd97f4e7cdba908cc73298f529d368aa07e0dffde6e1e8ec52"
RECONCILIATION_BRANCH = "planning/barracks-10000-robustness-execution-20260809"
SOURCE_2K_JSON_SHA = "a02c4e0bad6a7113937fbd23f4521c364d109944c7f05c94eb5839b9119d00e2"
SOURCE_2K_CSV_SHA = "3b6a164a4ca847d29b82d73b3841100f246cdc36b9b86f30198bfcfe586f6560"
ROBUSTNESS_10K_JSON_SHA = "1675d5068d6299c618df2f5b27cca4cf6fb06990729d622cedf9c36282c8d3c3"
ROBUSTNESS_10K_CSV_SHA = "e7324cb7a46cdab3d765011890d38a234c541c9e28741a2e6af6d3bf2bbc0e8b"

REQUIRED_BLOCKERS = {
    "BARRACKS_FUNCTIONAL_VALUE_COMBAT_NUMERICS_REQUIRED",
    "GUT_ADOPTION_SPEC_PR155_NOT_MERGED",
    "HIGODOT_EXACT_SOURCE_OR_VERSION_UNVERIFIED",
    "HERA_PRESENT_BUT_ADOPTION_NOT_VERIFIED",
    "DIRECT_MAIN_HERA_IMPORT_NOT_YET_DISPOSITIONED",
    "LOCAL_GODOT_AND_AUDIO_VAULT_UNAVAILABLE",
}
COMPLETED_BLOCKERS = {
    "BARRACKS_10000_ROBUSTNESS_EXECUTION_USER_APPROVAL_REQUIRED",
    "BARRACKS_10000_ROBUSTNESS_DEDICATED_RUNNER_REQUIRED",
    "BARRACKS_10000_SEED_DECISION_SWEEP_REVIEW_REQUIRED",
    "BARRACKS_PARAMETER_SELECTION_IDENTIFIABILITY_REQUIRED",
}


def load_state() -> dict[str, Any]:
    return json.loads(STATE_PATH.read_text(encoding="utf-8"))


def validate_state(data: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    if data.get("decision_id") != DECISION_ID:
        errors.append("Decision ID mismatch")
    if data.get("last_gate_update_decision") != BARRACKS_ROBUSTNESS_EXECUTION_DECISION:
        errors.append("last gate update Decision mismatch")
    if data.get("source_repository_main_sha") != CURRENT_SOURCE_MAIN_SHA:
        errors.append("source main SHA mismatch")
    if data.get("base_repository_main_sha") != BASE_RECOVERY_SHA:
        errors.append("Base recovery SHA mismatch")
    if data.get("base_current_main_observed") != CURRENT_BASE_MAIN_OBSERVED:
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
    if gate.get("decision_ledger_readback", {}).get("status") != "RECONCILED_BY_V4_4_THROUGH_BARRACKS_9_OF_10_ROBUSTNESS_EXECUTION":
        errors.append("Decision Ledger reconciliation status mismatch")
    if gate.get("unresolved_list_readback", {}).get("status") != "CURRENT_FUNCTIONAL_VALUE_COMBAT_NUMERICS_DEFINITION_REVIEW_GATE":
        errors.append("unresolved list current status mismatch")
    blockers = set(gate.get("blocking_reasons", []))
    if not REQUIRED_BLOCKERS.issubset(blockers):
        errors.append("entry blockers incomplete")
    for stale in COMPLETED_BLOCKERS:
        if stale in blockers:
            errors.append(f"completed barracks blocker must not persist: {stale}")
    allowed = gate.get("allowed_next_actions", [])
    if not allowed or allowed[0] != "BARRACKS_FUNCTIONAL_VALUE_COMBAT_NUMERICS_DEFINITION_REVIEW":
        errors.append("functional-value combat-numerics review must be first next action")
    forbidden = set(gate.get("forbidden_actions", []))
    for required in (
        "PRODUCT_IMPLEMENTATION",
        "GODOT_AUTHORING_MUTATION",
        "BARRACKS_10000_SEED_PARAMETER_SELECTION_EXECUTION",
        "BARRACKS_50000_SEED_CONFIRMATION",
    ):
        if required not in forbidden:
            errors.append(f"required forbidden action missing: {required}")
    if "BARRACKS_10000_SEED_ROBUSTNESS_EXECUTION" in forbidden:
        errors.append("completed robustness execution must not remain forbidden")
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
    if barracks.get("result_json_sha256") != SOURCE_2K_JSON_SHA or barracks.get("result_csv_sha256") != SOURCE_2K_CSV_SHA:
        errors.append("barracks 2k evidence hash mismatch")

    review = data.get("barracks_10000_review", {})
    if review.get("decision_id") != BARRACKS_10K_REVIEW_DECISION or review.get("parent_decision_id") != BARRACKS_REMEDIATION_DECISION:
        errors.append("10k review Decision lineage mismatch")
    if review.get("decision_sweep_10000_execution") != "NOT_AUTHORIZED" or review.get("confirmation_sweep_50000") != "BLOCKED":
        errors.append("10k review execution boundary mismatch")

    obs = data.get("barracks_parameter_selection_observables", {})
    if obs.get("decision_id") != BARRACKS_OBSERVABLES_DECISION or obs.get("parent_decision_id") != BARRACKS_10K_REVIEW_DECISION:
        errors.append("observables Decision lineage mismatch")
    if obs.get("comparison_form") != "VECTOR_GOLD_TIME_FOOD_NODE_NO_SINGLE_WEIGHTED_SCORE" or obs.get("selection_mode") != "HARD_FILTER_THEN_PARETO":
        errors.append("observables comparison/selection contract mismatch")
    if obs.get("economy_production_envelope") != "V00_BASELINE_COST_INTERVAL_ONLY":
        errors.append("economy-production envelope mismatch")
    if obs.get("special_functional_value_index") != "DEFERRED_UNTIL_PRODUCT_COMBAT_NUMERICS" or obs.get("final_parameter_vector") is not None:
        errors.append("observables functional/final boundary mismatch")

    robustness_review = data.get("barracks_10000_robustness_review", {})
    if robustness_review.get("decision_id") != BARRACKS_ROBUSTNESS_REVIEW_DECISION or robustness_review.get("parent_decision_id") != BARRACKS_OBSERVABLES_DECISION:
        errors.append("robustness review Decision lineage mismatch")
    if robustness_review.get("actual_10000_execution") != "NOT_RUN":
        errors.append("8-of-10 point-in-time review must retain NOT_RUN")
    if robustness_review.get("execution_contract") != "DEDICATED_RUNNER_REQUIRED" or robustness_review.get("execution_user_approval") != "REQUIRED":
        errors.append("8-of-10 review prerequisites must remain durable")

    execution = data.get("barracks_10000_robustness_execution", {})
    if execution.get("decision_id") != BARRACKS_ROBUSTNESS_EXECUTION_DECISION or execution.get("parent_decision_id") != BARRACKS_ROBUSTNESS_REVIEW_DECISION:
        errors.append("robustness execution Decision lineage mismatch")
    if execution.get("baseline_main") != CURRENT_SOURCE_MAIN_SHA or execution.get("base_current_main_observed") != CURRENT_BASE_MAIN_OBSERVED:
        errors.append("robustness execution provenance mismatch")
    if execution.get("runner") != "docs/analysis/barracks_simulation/run_barracks_robustness_10000.py" or execution.get("output_stem") != "robustness_sweep_10000.v1":
        errors.append("dedicated 10k runner/output identity mismatch")
    if execution.get("seed_count") != 10000 or execution.get("parameter_vector_count") != 1 or execution.get("common_random_numbers") is not True:
        errors.append("10k execution seed/vector/random-number contract mismatch")
    if execution.get("robustness_envelope") != "V00_BASELINE_COST_INTERVAL_ONLY":
        errors.append("10k robustness envelope mismatch")
    if float(execution.get("robustness_special_barracks_cost_gold", 0)) != 60.0 or float(execution.get("robustness_special_interval_multiplier", 0)) != 1.70:
        errors.append("10k robustness envelope numerics mismatch")
    if execution.get("special_functional_value_index") != "DEFERRED_UNTIL_PRODUCT_COMBAT_NUMERICS":
        errors.append("10k execution must keep functional value deferred")
    if execution.get("result_json_sha256") != ROBUSTNESS_10K_JSON_SHA or execution.get("result_csv_sha256") != ROBUSTNESS_10K_CSV_SHA:
        errors.append("10k evidence hash mismatch")
    if execution.get("source_2k_json_sha256") != SOURCE_2K_JSON_SHA or execution.get("source_2k_csv_sha256") != SOURCE_2K_CSV_SHA:
        errors.append("10k execution source 2k evidence mismatch")
    if execution.get("failed_decision_gates") != []:
        errors.append("10k robustness decision gates must pass")
    if float(execution.get("special_token_share_10_min", 1.0)) > 0.35 or float(execution.get("special_token_share_burst_max", 1.0)) > 0.45:
        errors.append("10k token-share robustness cap exceeded")
    if execution.get("second_special_token_source_guard", {}).get("minimum_non_special_active_sources") != 3:
        errors.append("second-special guard mismatch")
    if execution.get("second_special_token_source_guard", {}).get("status") != "PRESERVED_AND_OBSERVED":
        errors.append("second-special guard was not observed")
    if execution.get("identifiability") != "DIAGNOSTIC_NON_IDENTIFIABLE":
        errors.append("combat diagnostics must remain non-identifiable")
    if execution.get("parameter_selection_10000") != "NOT_AUTHORIZED" or execution.get("confirmation_sweep_50000") != "BLOCKED":
        errors.append("post-10k parameter-selection/50k boundary mismatch")
    if execution.get("final_parameter_vector") is not None or execution.get("final_product_numerics") != "NOT_APPROVED":
        errors.append("10k robustness must not finalize product numerics")
    if execution.get("product_implementation") != "NOT_AUTHORIZED" or execution.get("godot_authoring") != "NOT_AUTHORIZED":
        errors.append("product/Godot implementation must remain unauthorized")
    if execution.get("status") != "APPROVED_9_OF_10_ROBUSTNESS_10000_PASS":
        errors.append("10k robustness execution status mismatch")

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
    print("active_contract_v4_4=PASS application_binding=ACTIVE entry_gate=BLOCK barracks_5_of_10=SMOKE_PASS review_6_of_10=COMPLETE observables_7_of_10=DEFINED robustness_review_8_of_10=COMPLETE robustness_execution_9_of_10=PASS next=FUNCTIONAL_VALUE_COMBAT_NUMERICS_DEFINITION_REVIEW")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
