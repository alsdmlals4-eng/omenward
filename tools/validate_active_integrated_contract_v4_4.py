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
BARRACKS_FUNCTIONAL_REVIEW_DECISION = "OMW-DEC-20260809-PLANNING-BARRACKS-FUNCTIONAL-VALUE-COMBAT-NUMERICS-DEFINITION-REVIEW-V1"
BASE_RECOVERY_SHA = "fa69a77a14f923a756064f6ae151d34cadb374f7"
CURRENT_SOURCE_MAIN_SHA = "890a68c1c573ce11b21d397d7c3ec88bae191b7f"
CURRENT_BASE_MAIN_OBSERVED = "2a6ced23f6d6de1fb6e0a281c7138beb03f1a13b"
ADAPTER_BASELINE_MAIN = "1f23981fdfc3e965ff46c8866e978c4701eb3d4e"
PROTECTED_POLICY_SHA = "1c36c4180b85d6bd97f4e7cdba908cc73298f529d368aa07e0dffde6e1e8ec52"
RECONCILIATION_BRANCH = "planning/barracks-functional-value-combat-numerics-review-20260809"
SOURCE_2K_JSON_SHA = "a02c4e0bad6a7113937fbd23f4521c364d109944c7f05c94eb5839b9119d00e2"
SOURCE_2K_CSV_SHA = "3b6a164a4ca847d29b82d73b3841100f246cdc36b9b86f30198bfcfe586f6560"
ROBUSTNESS_10K_JSON_SHA = "1675d5068d6299c618df2f5b27cca4cf6fb06990729d622cedf9c36282c8d3c3"
ROBUSTNESS_10K_CSV_SHA = "e7324cb7a46cdab3d765011890d38a234c541c9e28741a2e6af6d3bf2bbc0e8b"

REQUIRED_BLOCKERS = {
    "BARRACKS_ROLE_OUTPUT_RUNTIME_IMPLEMENTATION_REQUIRED",
    "BARRACKS_FUNCTIONAL_VALUE_MEASUREMENT_SCENARIOS_REQUIRED",
    "GUT_ADOPTION_SPEC_PR155_NOT_MERGED",
    "HIGODOT_EXACT_SOURCE_OR_VERSION_UNVERIFIED",
    "HERA_PRESENT_BUT_ADOPTION_NOT_VERIFIED",
    "DIRECT_MAIN_HERA_IMPORT_NOT_YET_DISPOSITIONED",
    "LOCAL_GODOT_AND_AUDIO_VAULT_UNAVAILABLE",
}
COMPLETED_BLOCKERS = {
    "BARRACKS_FUNCTIONAL_VALUE_COMBAT_NUMERICS_REQUIRED",
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
    if data.get("last_gate_update_decision") != BARRACKS_FUNCTIONAL_REVIEW_DECISION:
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

    gate = data.get("entry_gate", {})
    if gate.get("decision") != "BLOCK":
        errors.append("entry gate must remain BLOCK")
    if gate.get("decision_ledger_readback", {}).get("status") != "RECONCILED_BY_V4_4_THROUGH_BARRACKS_FUNCTIONAL_VALUE_COMBAT_NUMERICS_REVIEW":
        errors.append("Decision Ledger reconciliation status mismatch")
    if gate.get("unresolved_list_readback", {}).get("status") != "CURRENT_FUNCTIONAL_VALUE_MEASUREMENT_SCENARIOS_GATE":
        errors.append("unresolved list current status mismatch")
    blockers = set(gate.get("blocking_reasons", []))
    if not REQUIRED_BLOCKERS.issubset(blockers):
        errors.append("entry blockers incomplete")
    for stale in COMPLETED_BLOCKERS:
        if stale in blockers:
            errors.append(f"completed or superseded barracks blocker must not persist: {stale}")
    allowed = gate.get("allowed_next_actions", [])
    if not allowed or allowed[0] != "BARRACKS_FUNCTIONAL_VALUE_MEASUREMENT_SCENARIOS_DEFINITION":
        errors.append("functional-value measurement scenarios must be first next action")
    forbidden = set(gate.get("forbidden_actions", []))
    for required in ("PRODUCT_IMPLEMENTATION", "GODOT_AUTHORING_MUTATION", "BARRACKS_10000_SEED_PARAMETER_SELECTION_EXECUTION", "BARRACKS_50000_SEED_CONFIRMATION"):
        if required not in forbidden:
            errors.append(f"required forbidden action missing: {required}")
    image = gate.get("image_review_sheet_readback", {})
    if image.get("ready_count") != 0 or image.get("awaiting_count") != 0:
        errors.append("image READY/AWAITING counts must remain zero")

    recovery = data.get("base_recovery", {})
    if recovery.get("decision_id") != BASE_RECOVERY_DECISION or recovery.get("base_exact_commit") != BASE_RECOVERY_SHA or recovery.get("status") != "COMPLETE":
        errors.append("Base recovery mismatch")
    adapter = data.get("project_base_adapter", {})
    if adapter.get("decision_id") != ADAPTER_FRESHNESS_DECISION:
        errors.append("project Base adapter Decision mismatch")
    if adapter.get("protected_baseline_commit") != ADAPTER_BASELINE_MAIN or adapter.get("protected_policy_sha256") != PROTECTED_POLICY_SHA:
        errors.append("project Base adapter protected baseline mismatch")
    if adapter.get("gdd_sheet_sync_status") != "CURRENT" or adapter.get("status") != "FRESHNESS_RECONCILED":
        errors.append("project Base adapter freshness mismatch")

    barracks = data.get("barracks_remediation", {})
    if barracks.get("decision_id") != BARRACKS_REMEDIATION_DECISION or barracks.get("smoke_rerun_status") != "PASS" or barracks.get("failed_decision_gates") != []:
        errors.append("barracks 2k remediation durability mismatch")
    if barracks.get("result_json_sha256") != SOURCE_2K_JSON_SHA or barracks.get("result_csv_sha256") != SOURCE_2K_CSV_SHA:
        errors.append("barracks 2k evidence hash mismatch")

    review = data.get("barracks_10000_review", {})
    if review.get("decision_id") != BARRACKS_10K_REVIEW_DECISION or review.get("decision_sweep_10000_execution") != "NOT_AUTHORIZED":
        errors.append("10k parameter-selection review durability mismatch")

    obs = data.get("barracks_parameter_selection_observables", {})
    if obs.get("decision_id") != BARRACKS_OBSERVABLES_DECISION or obs.get("comparison_form") != "VECTOR_GOLD_TIME_FOOD_NODE_NO_SINGLE_WEIGHTED_SCORE":
        errors.append("observables durability mismatch")
    if obs.get("economy_production_envelope") != "V00_BASELINE_COST_INTERVAL_ONLY" or obs.get("final_parameter_vector") is not None:
        errors.append("observables envelope/final boundary mismatch")

    robustness_review = data.get("barracks_10000_robustness_review", {})
    if robustness_review.get("decision_id") != BARRACKS_ROBUSTNESS_REVIEW_DECISION or robustness_review.get("actual_10000_execution") != "NOT_RUN":
        errors.append("8-of-10 point-in-time review durability mismatch")

    execution = data.get("barracks_10000_robustness_execution", {})
    if execution.get("decision_id") != BARRACKS_ROBUSTNESS_EXECUTION_DECISION:
        errors.append("robustness execution Decision mismatch")
    if execution.get("seed_count") != 10000 or execution.get("failed_decision_gates") != []:
        errors.append("10k robustness execution result mismatch")
    if execution.get("result_json_sha256") != ROBUSTNESS_10K_JSON_SHA or execution.get("result_csv_sha256") != ROBUSTNESS_10K_CSV_SHA:
        errors.append("10k evidence hash mismatch")
    if execution.get("identifiability") != "DIAGNOSTIC_NON_IDENTIFIABLE":
        errors.append("10k combat diagnostics must remain non-identifiable")
    if execution.get("parameter_selection_10000") != "NOT_AUTHORIZED" or execution.get("confirmation_sweep_50000") != "BLOCKED":
        errors.append("post-10k selection/50k boundary mismatch")

    functional = data.get("barracks_functional_value_combat_numerics_review", {})
    if functional.get("decision_id") != BARRACKS_FUNCTIONAL_REVIEW_DECISION or functional.get("parent_decision_id") != BARRACKS_ROBUSTNESS_EXECUTION_DECISION:
        errors.append("functional review Decision lineage mismatch")
    if functional.get("baseline_main") != CURRENT_SOURCE_MAIN_SHA or functional.get("base_current_main_observed") != CURRENT_BASE_MAIN_OBSERVED:
        errors.append("functional review provenance mismatch")
    if functional.get("product_base_combat_numerics") != "PRESENT":
        errors.append("product base combat numeric recovery mismatch")
    if functional.get("poc_role_numeric_hypotheses") != "PRESENT_NONFINAL":
        errors.append("PoC role numeric hypothesis status mismatch")
    if functional.get("role_complete_product_output_numerics") != "PARTIAL_INSUFFICIENT":
        errors.append("role-complete product output status mismatch")
    if functional.get("product_special_corps") != ["priest", "mage", "flier", "giant"]:
        errors.append("product special-corps taxonomy mismatch")
    if functional.get("historical_simulation_special_outcome_label_set") != ["assassin", "priest", "mage", "flying_unit", "giant"]:
        errors.append("historical simulation label set mismatch")
    if functional.get("functional_value_comparison") != "ROLE_SPECIFIC_VECTOR_NO_SINGLE_WEIGHTED_SCORE" or functional.get("post_hoc_weight_tuning") != "FORBIDDEN":
        errors.append("functional-value comparison contract mismatch")
    if functional.get("final_functional_value_index") is not None or functional.get("final_parameter_vector") is not None:
        errors.append("functional review must not select final values")
    if functional.get("product_implementation") != "NOT_AUTHORIZED" or functional.get("next_gate") != "BARRACKS_FUNCTIONAL_VALUE_MEASUREMENT_SCENARIOS_DEFINITION":
        errors.append("functional review implementation/next-gate boundary mismatch")

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
    print("active_contract_v4_4=PASS application_binding=ACTIVE entry_gate=BLOCK robustness_9_of_10=PASS functional_value_review=COMPLETE role_output_runtime=PARTIAL next=FUNCTIONAL_VALUE_MEASUREMENT_SCENARIOS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
