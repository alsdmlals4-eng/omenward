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

    def test_current_gate_is_robustness_review_with_user_approval_next(self) -> None:
        gate = self.state["entry_gate"]
        self.assertEqual(self.state["last_gate_update_decision"], BARRACKS_ROBUSTNESS_REVIEW_DECISION)
        self.assertEqual(self.state["source_repository_main_sha"], "4da8ed64baaa66b15d110490f1b15fd9be20aee0")
        self.assertEqual(self.state["base_current_main_observed"], "cf4c7a60c5b31b042043f91b268f381372fec69a")
        self.assertIn("BARRACKS_10000_ROBUSTNESS_EXECUTION_USER_APPROVAL_REQUIRED", gate["blocking_reasons"])
        self.assertIn("BARRACKS_10000_ROBUSTNESS_DEDICATED_RUNNER_REQUIRED", gate["blocking_reasons"])
        self.assertIn("BARRACKS_FUNCTIONAL_VALUE_COMBAT_NUMERICS_REQUIRED", gate["blocking_reasons"])
        self.assertEqual(gate["allowed_next_actions"][0], "BARRACKS_10000_SEED_ROBUSTNESS_EXECUTION_PACKAGE_USER_APPROVAL")
        self.assertIn("BARRACKS_10000_SEED_ROBUSTNESS_EXECUTION", gate["forbidden_actions"])
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
        self.assertIsNone(obs["final_parameter_vector"])
        self.assertEqual(obs["parameter_selection_10000"], "NOT_AUTHORIZED")

    def test_robustness_review_is_nonexecuting_and_nonfinal(self) -> None:
        review = self.state["barracks_10000_robustness_review"]
        self.assertEqual(review["decision_id"], BARRACKS_ROBUSTNESS_REVIEW_DECISION)
        self.assertEqual(review["parent_decision_id"], BARRACKS_OBSERVABLES_DECISION)
        self.assertEqual(review["current_runner_for_durable_10k"], "UNSAFE_EVIDENCE_PROVENANCE")
        self.assertEqual(review["robustness_envelope"], "V00_BASELINE_COST_INTERVAL_ONLY")
        self.assertEqual(review["execution_contract"], "DEDICATED_RUNNER_REQUIRED")
        self.assertEqual(review["execution_user_approval"], "REQUIRED")
        self.assertEqual(review["actual_10000_execution"], "NOT_RUN")
        self.assertEqual(review["parameter_selection_10000"], "NOT_AUTHORIZED")
        self.assertEqual(review["confirmation_sweep_50000"], "BLOCKED")
        self.assertIsNone(review["final_parameter_vector"])
        self.assertEqual(review["continuous_work_state_after_review"], "STOPPED_USER_DECISION")

    def test_tool_roles_and_local_boundary_remain(self) -> None:
        tools = self.state["tool_authority"]
        self.assertEqual(tools["higodot"]["authority"], "SOLE_PERSISTENT_GODOT_AUTHORING_AUTHORITY")
        self.assertEqual(tools["gut"]["authority"], "DETERMINISTIC_GDSCRIPT_TEST_AUTHORITY_WHEN_ADOPTED")
        self.assertEqual(tools["hera"]["role"], "LIVE_QA_AND_OBSERVABILITY_ONLY")
        self.assertEqual(tools["hera"]["persistent_source_mutation"], "FORBIDDEN")
        self.assertEqual(self.state["local_delivery"]["status"], "BLOCKED_UNVERIFIED")


if __name__ == "__main__":
    unittest.main()
