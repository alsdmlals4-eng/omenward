from __future__ import annotations

import copy
import importlib.util
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[2]
VALIDATOR_PATH = ROOT / "tools/validate_active_integrated_contract_v4_3.py"
STATE_PATH = ROOT / "docs/operations/ACTIVE_INTEGRATED_CONTRACT_STATE.v1.json"


def load_validator():
    spec = importlib.util.spec_from_file_location("active_contract_v43", VALIDATOR_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("validator import unavailable")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class ActiveIntegratedContractV43Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.validator = load_validator()
        cls.state = json.loads(STATE_PATH.read_text(encoding="utf-8"))

    def test_truthful_active_but_blocked_state_passes(self) -> None:
        self.assertEqual(self.validator.validate_state(self.state), [])

    def test_contract_v4_3_is_active_and_v4_2_is_historical(self) -> None:
        self.assertEqual(self.state["active_contract"]["version"], "4.3")
        self.assertEqual(self.state["active_contract"]["binding_status"], "ACTIVE")
        self.assertEqual(self.state["superseded_contracts"][0]["version"], "4.2")
        self.assertEqual(self.state["superseded_contracts"][0]["status"], "HISTORICAL_COMPARISON_ONLY")

    def test_entry_gate_cannot_be_opened_by_contract_activation(self) -> None:
        mutated = copy.deepcopy(self.state)
        mutated["entry_gate"]["decision"] = "PASS"
        errors = self.validator.validate_state(mutated)
        self.assertIn("entry gate must remain BLOCK", errors)

    def test_gut_formal_execution_requires_merged_spec(self) -> None:
        mutated = copy.deepcopy(self.state)
        mutated["tool_authority"]["gut"]["formal_execution_status"] = "READY"
        errors = self.validator.validate_state(mutated)
        self.assertIn("formal GUT execution must remain blocked", errors)

    def test_higodot_and_gut_mutation_overlap_is_forbidden(self) -> None:
        mutated = copy.deepcopy(self.state)
        mutated["tool_authority"]["role_overlap"] = "ALLOWED"
        errors = self.validator.validate_state(mutated)
        self.assertIn("HiGodot/GUT role overlap must be FORBIDDEN", errors)

    def test_audio_vault_original_path_is_preserved(self) -> None:
        self.assertEqual(
            self.state["audio_vault"]["path"],
            "C:/Users/user/Documents/GitHub/shered audio vault",
        )
        self.assertEqual(self.state["audio_vault"]["status"], "BLOCKED_UNVERIFIED")

    def test_review_model_is_role_separated_gpt_plus_user_authority(self) -> None:
        self.assertEqual(
            self.state["review_authority"]["model"],
            "GPT_ROLE_SEPARATED_PLUS_USER_DECISION_AUTHORITY",
        )
        self.assertEqual(
            self.state["review_authority"]["external_independent_reviewer"],
            "NOT_PLANNED_SOLO_DEVELOPMENT",
        )

    def test_product_and_godot_authoring_remain_forbidden(self) -> None:
        forbidden = set(self.state["entry_gate"]["forbidden_actions"])
        self.assertIn("PRODUCT_IMPLEMENTATION", forbidden)
        self.assertIn("GODOT_AUTHORING_MUTATION", forbidden)
        self.assertIn("FORMAL_GUT_EXECUTION", forbidden)
        self.assertIn("MERGE_PR155_OR_PR156", forbidden)


if __name__ == "__main__":
    unittest.main()
