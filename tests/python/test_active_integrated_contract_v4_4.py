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

    def test_reconciled_state_is_durable_after_merge(self) -> None:
        gate = self.state["entry_gate"]
        self.assertEqual(
            gate["decision_ledger_readback"]["status"],
            "RECONCILED_BY_V4_4_DECISION",
        )
        self.assertNotIn("RECONCILIATION_DECISION_NOT_MERGED", gate["blocking_reasons"])
        self.assertNotIn("current_reconciliation_head", self.state["github_actions"])
        self.assertNotIn("working_branch", self.state)
        self.assertEqual(
            self.state["reconciliation_branch"],
            "process/v4-4-entry-reconciliation-20260808",
        )

    def test_pr159_base_recovery_completion_is_propagated(self) -> None:
        gate = self.state["entry_gate"]
        blockers = set(gate["blocking_reasons"])
        allowed = set(gate["allowed_next_actions"])
        self.assertEqual(self.state["last_gate_update_decision"], BASE_RECOVERY_DECISION)
        self.assertNotIn("BASE_RECOVERY_PR159_DRAFT_INCOMPLETE", blockers)
        self.assertNotIn("PR159_BASE_RECOVERY_COMPLETION", allowed)
        self.assertIn("PROJECT_BASE_ADAPTER_FRESHNESS_FIX_REQUIRED", blockers)
        self.assertIn("PROJECT_BASE_ADAPTER_FRESHNESS_RECONCILIATION", allowed)

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
