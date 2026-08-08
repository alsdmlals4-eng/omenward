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

    def test_current_gate_is_robustness_execution_with_functional_review_next(self) -> None:
        gate = self.state["entry_gate"]
        self.assertEqual(self.state["last_gate_update_decision"], BARRACKS_ROBUSTNESS_EXECUTION_DECISION)
        self.assertEqual(self.state["source_repository_main_sha"], "02260589e1aa374c19005d19e47ba1f3b27332bd")
        self.assertEqual(self.state["base_current_main_observed"], "cf4c7a60c5b31b042043f91b268f381372fec69a")
        self.assertNotIn("BARRACKS_10000_ROBUSTNESS_EXECUTION_USER_APPROVAL_REQUIRED", gate["blocking_reasons"])
        self.assertNotIn("BARRACKS_10000_ROBUSTNESS_DEDICATED_RUNNER_REQUIRED", gate["blocking_reasons"])
        self.assertIn("BARRACKS_FUNCTIONAL_VALUE_COMBAT_NUMERICS_REQUIRED", gate["blocking_reasons"])
        self.assertEqual(gate["allowed_next_actions"][0], "BARRACKS_FUNCTIONAL_VALUE_COMBAT_NUMERICS_DEFINITION_REVIEW")
        self.assertNotIn("BARRACKS_10000_SEED_ROBUSTNESS_EXECUTION", gate["forbidden_actions"])
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
        self.assertEqual(rem["decision_id"], BARRACKS_REMEDIATION_DECISION)
        self.assertEqual(rem["smoke_rerun_status"], "PASS")
        self.assertEqual(rem["failed_decision_gates"], [])
        self.assertEqual(review["decision_id"], BARRACKS_10K_REVIEW_DECISION)
        self.assertEqual(review["decision_sweep_10000_execution"], "NOT_AUTHORIZED")
        self.assertEqual(review["confirmation_sweep_50000"], "BLOCKED")
        self.assertIsNone(review["final_parameter_vector"])
        self.assertEqual(obs["decision_id"], BARRACKS_OBSERVABLES_DECISION)
        self.assertEqual(obs["selection_mode"], "HARD_FILTER_THEN_PARETO")
        self.assertEqual(obs["economy_production_envelope"], "V00_BASELINE_COST_INTERVAL_ONLY")
        self.assertEqual(obs["special_functional_value_index"], "DEFERRED_UNTIL_PRODUCT_COMBAT_NUMERICS")
        self.assertEqual(robustness_review["decision_id"], BARRACKS_ROBUSTNESS_REVIEW_DECISION)
        self.assertEqual(robustness_review["actual_10000_execution"], "NOT_RUN")
        self.assertEqual(robustness_review["execution_contract"], "DEDICATED_RUNNER_REQUIRED")
        self.assertEqual(robustness_review["execution_user_approval"], "REQUIRED")

    def test_robustness_execution_is_v00_only_pass_and_nonfinal(self) -> None:
        execution = self.state["barracks_10000_robustness_execution"]
        self.assertEqual(execution["decision_id"], BARRACKS_ROBUSTNESS_EXECUTION_DECISION)
        self.assertEqual(execution["parent_decision_id"], BARRACKS_ROBUSTNESS_REVIEW_DECISION)
        self.assertEqual(execution["seed_count"], 10000)
        self.assertEqual(execution["parameter_vector_count"], 1)
        self.assertTrue(execution["common_random_numbers"])
        self.assertEqual(execution["robustness_envelope"], "V00_BASELINE_COST_INTERVAL_ONLY")
        self.assertEqual(float(execution["robustness_special_barracks_cost_gold"]), 60.0)
        self.assertEqual(float(execution["robustness_special_interval_multiplier"]), 1.70)
        self.assertEqual(execution["failed_decision_gates"], [])
        self.assertAlmostEqual(float(execution["special_token_share_10_min"]), 0.296265)
        self.assertAlmostEqual(float(execution["special_token_share_burst_max"]), 0.333333)
        self.assertEqual(execution["second_special_token_source_guard"]["deferred_observations"], 82181)
        self.assertEqual(execution["identifiability"], "DIAGNOSTIC_NON_IDENTIFIABLE")
        self.assertEqual(execution["raw_diagnostics"]["general_path_validity_rate"], 0.0)
        self.assertEqual(execution["raw_diagnostics"]["worst_special_regret_rate"], 1.0)
        self.assertEqual(execution["special_functional_value_index"], "DEFERRED_UNTIL_PRODUCT_COMBAT_NUMERICS")
        self.assertEqual(execution["parameter_selection_10000"], "NOT_AUTHORIZED")
        self.assertEqual(execution["confirmation_sweep_50000"], "BLOCKED")
        self.assertIsNone(execution["final_parameter_vector"])
        self.assertEqual(execution["final_product_numerics"], "NOT_APPROVED")
        self.assertEqual(execution["product_implementation"], "NOT_AUTHORIZED")

    def test_tool_roles_and_local_boundary_remain(self) -> None:
        tools = self.state["tool_authority"]
        self.assertEqual(tools["higodot"]["authority"], "SOLE_PERSISTENT_GODOT_AUTHORING_AUTHORITY")
        self.assertEqual(tools["gut"]["authority"], "DETERMINISTIC_GDSCRIPT_TEST_AUTHORITY_WHEN_ADOPTED")
        self.assertEqual(tools["hera"]["role"], "LIVE_QA_AND_OBSERVABILITY_ONLY")
        self.assertEqual(tools["hera"]["persistent_source_mutation"], "FORBIDDEN")
        self.assertEqual(self.state["local_delivery"]["status"], "BLOCKED_UNVERIFIED")


if __name__ == "__main__":
    unittest.main()
