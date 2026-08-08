from __future__ import annotations

import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DECISION = "OMW-DEC-20260808-PLANNING-BARRACKS-CAPABILITY-PROXY-AND-MULTI-SPECIAL-TOKEN-BURST-REMEDIATION-V1"
SPEC = ROOT / "docs/design/APPROVED_OMENWARD_BARRACKS_CAPABILITY_PROXY_AND_MULTI_SPECIAL_TOKEN_BURST_REMEDIATION_2026-08-08.md"
MODEL = ROOT / "docs/analysis/barracks_simulation/remediation_model.v1.json"
SMOKE_EVIDENCE = ROOT / "docs/design/APPROVED_OMENWARD_BARRACKS_SMOKE_SWEEP_RESULTS_2026-08-06.md"
LEDGER = ROOT / "docs/PROJECT_CANON_DECISION_LEDGER.md"
STATE = ROOT / "docs/operations/ACTIVE_INTEGRATED_CONTRACT_STATE.v1.json"


class BarracksConditionalFailRemediationTests(unittest.TestCase):
    def test_remediation_authority_exists_and_is_analysis_only(self) -> None:
        text = SPEC.read_text(encoding="utf-8")
        self.assertIn(DECISION, text)
        self.assertIn("APPROVED_REMEDIATION_CONTRACT", text)
        self.assertIn("PRODUCT_IMPLEMENTATION = NOT_AUTHORIZED", text)
        self.assertIn("DECISION_SWEEP_10000 = BLOCKED_UNTIL_RERUN_PASS", text)
        self.assertIn("CONFIRMATION_SWEEP_50000 = BLOCKED", text)

    def test_non_identifiable_combat_power_is_not_a_balance_gate(self) -> None:
        data = json.loads(MODEL.read_text(encoding="utf-8"))
        self.assertEqual(DECISION, data["decision_id"])
        proxy = data["player_capability_proxy"]
        self.assertEqual("STRUCTURAL_CHANNEL_VECTOR", proxy["mode"])
        self.assertEqual("FORBIDDEN", proxy["combat_power_scalar"])
        self.assertEqual("DIAGNOSTIC_NON_IDENTIFIABLE", proxy["general_path_validity_rate"])
        self.assertEqual("DIAGNOSTIC_NON_IDENTIFIABLE", proxy["each_special_outcome_path_validity_rate"])
        self.assertEqual(["DEFENSE_TOWER", "COMMAND_AURA", "MANA_TACTIC", "FRONTLINE_STATE"], proxy["channels"])

    def test_second_special_token_source_obeys_physical_reel_cap(self) -> None:
        data = json.loads(MODEL.read_text(encoding="utf-8"))
        rule = data["multi_special_token_source"]
        self.assertEqual("PHYSICAL_TOKEN_INSTANCES_PER_REEL", rule["probability_axis"])
        self.assertEqual(1, rule["tokens_per_active_source_per_reel"])
        self.assertEqual(3, rule["second_special_min_non_special_active_sources"])
        self.assertEqual("DEFERRED_WHILE_GUARD_FALSE", rule["second_special_activation"])
        self.assertLessEqual(float(rule["max_special_share_when_two_special_sources_active"]), 0.45)
        self.assertAlmostEqual(0.40, float(rule["max_special_share_when_two_special_sources_active"]), places=9)
        self.assertEqual("FORBIDDEN", rule["fractional_token_weight_workaround"])

    def test_prior_4_of_10_smoke_evidence_is_recovered_on_current_main_path(self) -> None:
        text = SMOKE_EVIDENCE.read_text(encoding="utf-8")
        self.assertIn("APPROVED_SMOKE_RESULT / CONDITIONAL_FAIL", text)
        self.assertIn("MODEL_IDENTIFIABILITY_FAIL", text)
        self.assertIn("SPECIAL_TOKEN_SHARE_BURST_MAX = 0.500000", text)

    def test_durable_gate_moves_to_smoke_rerun_not_product_work(self) -> None:
        ledger = LEDGER.read_text(encoding="utf-8")
        state = json.loads(STATE.read_text(encoding="utf-8"))
        self.assertIn(DECISION, ledger)
        self.assertIn("BARRACKS_2000_SEED_SMOKE_RERUN", ledger)
        self.assertNotIn("PR #154 conditional fail / unmerged", ledger)
        self.assertEqual(DECISION, state["last_gate_update_decision"])
        self.assertIn("BARRACKS_2000_SEED_SMOKE_RERUN", state["entry_gate"]["allowed_next_actions"])
        self.assertIn("PRODUCT_IMPLEMENTATION", state["entry_gate"]["forbidden_actions"])


if __name__ == "__main__":
    unittest.main()
