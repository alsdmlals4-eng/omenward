from __future__ import annotations

import copy
import importlib.util
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[2]
VALIDATOR_PATH = ROOT / "tools/validate_active_integrated_contract_v4_4.py"
STATE_PATH = ROOT / "docs/operations/ACTIVE_INTEGRATED_CONTRACT_STATE.v1.json"
BASE_RECOVERY_DECISION = "OMW-DEC-20260807-PROCESS-BASE-REPOSITORY-SKILL-MAP-AND-LOCAL-VERIFICATION-PACK-V1"
ADAPTER_FRESHNESS_DECISION = "OMW-DEC-20260808-PROCESS-PROJECT-BASE-ADAPTER-FRESHNESS-RECONCILIATION-V1"
BARRACKS_REMEDIATION_DECISION = "OMW-DEC-20260808-PLANNING-BARRACKS-CAPABILITY-PROXY-AND-MULTI-SPECIAL-TOKEN-BURST-REMEDIATION-V1"
BARRACKS_10K_REVIEW_DECISION = "OMW-DEC-20260808-PLANNING-BARRACKS-10000-SEED-DECISION-SWEEP-REVIEW-V1"
BARRACKS_OBSERVABLES_DECISION = "OMW-DEC-20260808-PLANNING-BARRACKS-PARAMETER-SELECTION-OBSERVABLES-DEFINITION-V1"
BARRACKS_ROBUSTNESS_REVIEW_DECISION = "OMW-DEC-20260808-PLANNING-BARRACKS-10000-SEED-ROBUSTNESS-ONLY-REVIEW-V1"
BARRACKS_ROBUSTNESS_EXECUTION_DECISION = "OMW-DEC-20260809-PLANNING-BARRACKS-10000-SEED-ROBUSTNESS-EXECUTION-V1"
BARRACKS_FUNCTIONAL_REVIEW_DECISION = "OMW-DEC-20260809-PLANNING-BARRACKS-FUNCTIONAL-VALUE-COMBAT-NUMERICS-DEFINITION-REVIEW-V1"
BARRACKS_MEASUREMENT_DECISION = "OMW-DEC-20260809-PLANNING-BARRACKS-FUNCTIONAL-VALUE-MEASUREMENT-SCENARIOS-DEFINITION-V1"


def load_validator():
    spec = importlib.util.spec_from_file_location("active_contract_v44", VALIDATOR_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("validator import unavailable")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class ActiveIntegratedContractV44Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.validator = load_validator()
        cls.state = json.loads(STATE_PATH.read_text(encoding="utf-8"))

    def test_truthful_active_but_blocked_state_passes(self) -> None:
        self.assertEqual(self.validator.validate_state(self.state), [])

    def test_v4_4_is_active_and_entry_gate_stays_blocked(self) -> None:
        self.assertEqual(self.state["active_contract"]["version"], "4.4")
        self.assertEqual(self.state["active_contract"]["binding_status"], "ACTIVE")
        mutated = copy.deepcopy(self.state)
        mutated["entry_gate"]["decision"] = "PASS"
        self.assertIn("entry gate must remain BLOCK", self.validator.validate_state(mutated))

    def test_measurement_scenarios_close_only_their_blocker_and_advance_runtime_package(self) -> None:
        gate = self.state["entry_gate"]
        self.assertEqual(self.state["schema_version"], "2.0")
        self.assertEqual(self.state["last_gate_update_decision"], BARRACKS_MEASUREMENT_DECISION)
        self.assertEqual(self.state["source_repository_main_sha"], "02b803b075d5e44f5aa3db895c5dad025d048148")
        self.assertEqual(self.state["base_current_main_observed"], "2a6ced23f6d6de1fb6e0a281c7138beb03f1a13b")
        self.assertNotIn("BARRACKS_FUNCTIONAL_VALUE_MEASUREMENT_SCENARIOS_REQUIRED", gate["blocking_reasons"])
        self.assertIn("BARRACKS_ROLE_OUTPUT_RUNTIME_IMPLEMENTATION_REQUIRED", gate["blocking_reasons"])
        self.assertEqual(gate["allowed_next_actions"][0], "BARRACKS_ROLE_OUTPUT_RUNTIME_IMPLEMENTATION_PACKAGE")
        self.assertIn("PRODUCT_IMPLEMENTATION", gate["forbidden_actions"])
        self.assertIn("GODOT_AUTHORING_MUTATION", gate["forbidden_actions"])
        self.assertIn("BARRACKS_10000_SEED_PARAMETER_SELECTION_EXECUTION", gate["forbidden_actions"])
        self.assertIn("BARRACKS_50000_SEED_CONFIRMATION", gate["forbidden_actions"])

    def test_base_recovery_and_adapter_remain_durable(self) -> None:
        recovery = self.state["base_recovery"]
        adapter = self.state["project_base_adapter"]
        self.assertEqual(recovery["decision_id"], BASE_RECOVERY_DECISION)
        self.assertEqual(recovery["status"], "COMPLETE")
        self.assertTrue(recovery["blocker_cleared"])
        self.assertEqual(adapter["decision_id"], ADAPTER_FRESHNESS_DECISION)
        self.assertEqual(adapter["gdd_sheet_sync_status"], "CURRENT")
        self.assertEqual(adapter["status"], "FRESHNESS_RECONCILED")
        self.assertTrue(adapter["blocker_cleared"])

    def test_barracks_lower_gates_remain_durable(self) -> None:
        rem = self.state["barracks_remediation"]
        review = self.state["barracks_10000_review"]
        obs = self.state["barracks_parameter_selection_observables"]
        robustness_review = self.state["barracks_10000_robustness_review"]
        execution = self.state["barracks_10000_robustness_execution"]
        functional = self.state["barracks_functional_value_combat_numerics_review"]
        self.assertEqual(rem["decision_id"], BARRACKS_REMEDIATION_DECISION)
        self.assertEqual(rem["smoke_rerun_status"], "PASS")
        self.assertEqual(review["decision_id"], BARRACKS_10K_REVIEW_DECISION)
        self.assertEqual(review["decision_sweep_10000_execution"], "NOT_AUTHORIZED")
        self.assertEqual(obs["decision_id"], BARRACKS_OBSERVABLES_DECISION)
        self.assertEqual(obs["selection_mode"], "HARD_FILTER_THEN_PARETO")
        self.assertEqual(robustness_review["decision_id"], BARRACKS_ROBUSTNESS_REVIEW_DECISION)
        self.assertEqual(robustness_review["actual_10000_execution"], "NOT_RUN")
        self.assertEqual(execution["decision_id"], BARRACKS_ROBUSTNESS_EXECUTION_DECISION)
        self.assertEqual(execution["seed_count"], 10000)
        self.assertEqual(execution["failed_decision_gates"], [])
        self.assertEqual(execution["identifiability"], "DIAGNOSTIC_NON_IDENTIFIABLE")
        self.assertEqual(functional["decision_id"], BARRACKS_FUNCTIONAL_REVIEW_DECISION)
        self.assertEqual(functional["role_complete_product_output_numerics"], "PARTIAL_INSUFFICIENT")
        self.assertIsNone(functional["final_functional_value_index"])

    def test_measurement_scenario_contract_is_deterministic_blocked_not_zero_and_nonfinal(self) -> None:
        scenarios = self.state["barracks_functional_value_measurement_scenarios"]
        self.assertEqual(scenarios["decision_id"], BARRACKS_MEASUREMENT_DECISION)
        self.assertEqual(scenarios["parent_decision_id"], BARRACKS_FUNCTIONAL_REVIEW_DECISION)
        self.assertEqual(scenarios["fixture_policy"], "DETERMINISTIC_SAME_INPUT")
        self.assertEqual(scenarios["functional_value_comparison"], "ROLE_SPECIFIC_VECTOR_NO_SINGLE_WEIGHTED_SCORE")
        self.assertEqual(scenarios["post_hoc_weight_tuning"], "FORBIDDEN")
        self.assertEqual(scenarios["blocked_runtime_output_policy"], "NEVER_SYNTHESIZE_AS_ZERO")
        self.assertEqual(scenarios["scenario_ids"], ["FV-COMMON-01", "FV-PRIEST-01", "FV-MAGE-01", "FV-FLIER-01", "FV-GIANT-01"])
        self.assertEqual(scenarios["measurement_scenario_blocker"], "CLOSED_BY_THIS_DECISION")
        self.assertEqual(scenarios["role_output_runtime_blocker"], "REMAINS")
        self.assertIsNone(scenarios["final_functional_value_index"])
        self.assertIsNone(scenarios["final_parameter_vector"])
        self.assertEqual(scenarios["final_product_numerics"], "NOT_APPROVED")
        self.assertEqual(scenarios["product_implementation"], "NOT_AUTHORIZED")
        self.assertEqual(scenarios["godot_authoring"], "NOT_AUTHORIZED")
        self.assertEqual(scenarios["next_gate"], "BARRACKS_ROLE_OUTPUT_RUNTIME_IMPLEMENTATION_PACKAGE")

    def test_tool_roles_and_local_boundary_remain_until_separate_tool_sync(self) -> None:
        tools = self.state["tool_authority"]
        self.assertEqual(tools["higodot"]["authority"], "SOLE_PERSISTENT_GODOT_AUTHORING_AUTHORITY")
        self.assertEqual(tools["gut"]["authority"], "DETERMINISTIC_GDSCRIPT_TEST_AUTHORITY_WHEN_ADOPTED")
        self.assertEqual(tools["hera"]["role"], "LIVE_QA_AND_OBSERVABILITY_ONLY")
        self.assertEqual(tools["hera"]["persistent_source_mutation"], "FORBIDDEN")
        self.assertEqual(self.state["local_delivery"]["status"], "BLOCKED_UNVERIFIED")


if __name__ == "__main__":
    unittest.main()
