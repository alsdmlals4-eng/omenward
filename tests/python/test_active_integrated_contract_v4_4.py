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

    def test_v4_4_is_active(self) -> None:
        self.assertEqual(self.state["active_contract"]["version"], "4.4")
        self.assertEqual(self.state["active_contract"]["binding_status"], "ACTIVE")

    def test_entry_gate_stays_blocked(self) -> None:
        mutated = copy.deepcopy(self.state)
        mutated["entry_gate"]["decision"] = "PASS"
        self.assertIn("entry gate must remain BLOCK", self.validator.validate_state(mutated))

    def test_reconciled_state_is_durable_after_10k_review(self) -> None:
        gate = self.state["entry_gate"]
        self.assertEqual(
            gate["decision_ledger_readback"]["status"],
            "RECONCILED_BY_V4_4_PR159_ADAPTER_BARRACKS_5_OF_10_AND_10K_REVIEW",
        )
        self.assertEqual(
            gate["unresolved_list_readback"]["status"],
            "CURRENT_PARAMETER_SELECTION_IDENTIFIABILITY_GATE",
        )
        self.assertNotIn("current_reconciliation_head", self.state["github_actions"])
        self.assertNotIn("working_branch", self.state)
        self.assertEqual(
            self.state["reconciliation_branch"],
            "planning/barracks-10000-decision-sweep-review-20260808",
        )

    def test_base_recovery_and_adapter_remain_propagated(self) -> None:
        gate = self.state["entry_gate"]
        blockers = set(gate["blocking_reasons"])
        allowed = set(gate["allowed_next_actions"])
        recovery = self.state["base_recovery"]
        adapter = self.state["project_base_adapter"]
        self.assertNotIn("BASE_RECOVERY_PR159_DRAFT_INCOMPLETE", blockers)
        self.assertNotIn("PROJECT_BASE_ADAPTER_FRESHNESS_FIX_REQUIRED", blockers)
        self.assertNotIn("PR159_BASE_RECOVERY_COMPLETION", allowed)
        self.assertNotIn("PROJECT_BASE_ADAPTER_FRESHNESS_RECONCILIATION", allowed)
        self.assertEqual(recovery["decision_id"], BASE_RECOVERY_DECISION)
        self.assertEqual(recovery["status"], "COMPLETE")
        self.assertTrue(recovery["blocker_cleared"])
        self.assertEqual(adapter["decision_id"], ADAPTER_FRESHNESS_DECISION)
        self.assertEqual(adapter["gdd_sheet_sync_status"], "CURRENT")
        self.assertEqual(adapter["status"], "FRESHNESS_RECONCILED")
        self.assertTrue(adapter["blocker_cleared"])

    def test_barracks_5_of_10_pass_remains_propagated(self) -> None:
        barracks = self.state["barracks_remediation"]
        self.assertEqual(barracks["decision_id"], BARRACKS_REMEDIATION_DECISION)
        self.assertEqual(barracks["smoke_rerun_status"], "PASS")
        self.assertEqual(barracks["failed_decision_gates"], [])
        self.assertEqual(barracks["confirmation_sweep_50000"], "BLOCKED")
        self.assertIsNone(barracks["selected_parameter_vector"])
        self.assertEqual(barracks["product_implementation"], "NOT_AUTHORIZED")

    def test_10k_review_closes_review_blocker_without_authorizing_execution(self) -> None:
        gate = self.state["entry_gate"]
        blockers = set(gate["blocking_reasons"])
        review = self.state["barracks_10000_review"]
        self.assertEqual(self.state["last_gate_update_decision"], BARRACKS_10K_REVIEW_DECISION)
        self.assertNotIn("BARRACKS_10000_SEED_DECISION_SWEEP_REVIEW_REQUIRED", blockers)
        self.assertIn("BARRACKS_PARAMETER_SELECTION_IDENTIFIABILITY_REQUIRED", blockers)
        self.assertEqual(gate["allowed_next_actions"][0], "BARRACKS_PARAMETER_SELECTION_OBSERVABLES_DEFINITION")
        self.assertIn("BARRACKS_10000_SEED_PARAMETER_SELECTION_EXECUTION", gate["forbidden_actions"])
        self.assertEqual(review["decision_id"], BARRACKS_10K_REVIEW_DECISION)
        self.assertEqual(review["parameter_selection"], "NOT_IDENTIFIABLE_WITH_CURRENT_DECISION_METRICS")
        self.assertEqual(review["decision_sweep_10000_execution"], "NOT_AUTHORIZED")
        self.assertEqual(review["robustness_only_10000"], "OPTIONAL_AFTER_SEPARATE_APPROVAL")
        self.assertEqual(review["confirmation_sweep_50000"], "BLOCKED")
        self.assertIsNone(review["final_parameter_vector"])
        self.assertEqual(review["status"], "REVIEW_COMPLETE_EXECUTION_NOT_AUTHORIZED")

    def test_sheet_readback_has_no_ready_or_awaiting_images(self) -> None:
        image = self.state["entry_gate"]["image_review_sheet_readback"]
        self.assertEqual(image["ready_count"], 0)
        self.assertEqual(image["awaiting_count"], 0)

    def test_higodot_gut_hera_roles_do_not_overlap(self) -> None:
        tools = self.state["tool_authority"]
        self.assertEqual(tools["higodot"]["authority"], "SOLE_PERSISTENT_GODOT_AUTHORING_AUTHORITY")
        self.assertEqual(tools["gut"]["authority"], "DETERMINISTIC_GDSCRIPT_TEST_AUTHORITY_WHEN_ADOPTED")
        self.assertEqual(tools["hera"]["role"], "LIVE_QA_AND_OBSERVABILITY_ONLY")
        self.assertEqual(tools["hera"]["persistent_source_mutation"], "FORBIDDEN")

    def test_local_delivery_remains_unverified(self) -> None:
        self.assertEqual(self.state["local_delivery"]["status"], "BLOCKED_UNVERIFIED")


if __name__ == "__main__":
    unittest.main()
