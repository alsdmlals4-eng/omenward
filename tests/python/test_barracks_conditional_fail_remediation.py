from __future__ import annotations

import hashlib
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DECISION = "OMW-DEC-20260808-PLANNING-BARRACKS-CAPABILITY-PROXY-AND-MULTI-SPECIAL-TOKEN-BURST-REMEDIATION-V1"
REVIEW_DECISION = "OMW-DEC-20260808-PLANNING-BARRACKS-10000-SEED-DECISION-SWEEP-REVIEW-V1"
SPEC = ROOT / "docs/design/APPROVED_OMENWARD_BARRACKS_CAPABILITY_PROXY_AND_MULTI_SPECIAL_TOKEN_BURST_REMEDIATION_2026-08-08.md"
RESULT_AUTHORITY = ROOT / "docs/design/APPROVED_OMENWARD_BARRACKS_REMEDIATION_SMOKE_RERUN_RESULTS_2026-08-08.md"
MODEL = ROOT / "docs/analysis/barracks_simulation/remediation_model.v1.json"
SMOKE_EVIDENCE = ROOT / "docs/design/APPROVED_OMENWARD_BARRACKS_SMOKE_SWEEP_RESULTS_2026-08-06.md"
RESULT_JSON = ROOT / "docs/analysis/barracks_simulation/smoke_sweep_2000.v2.json"
RESULT_CSV = ROOT / "docs/analysis/barracks_simulation/smoke_sweep_2000.v2.csv"
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
        diagnostics = set(data["screening_semantics"]["diagnostic_only_combat_metrics"])
        self.assertIn("WORST_SPECIAL_REGRET_RATE", diagnostics)

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

    def test_exact_2k_result_is_persisted_and_hash_bound(self) -> None:
        result = json.loads(RESULT_JSON.read_text(encoding="utf-8"))
        authority = RESULT_AUTHORITY.read_text(encoding="utf-8")
        self.assertEqual(DECISION, result["decision_id"])
        self.assertEqual("SMOKE_RERUN_PASS", result["status"])
        self.assertEqual([], result["failed_gates"])
        self.assertEqual(2000, result["seed_count"])
        self.assertAlmostEqual(0.333333, result["baseline_vector"]["primary_kpis"]["SPECIAL_TOKEN_SHARE_BURST_MAX"], places=6)
        json_hash = hashlib.sha256(RESULT_JSON.read_bytes()).hexdigest()
        csv_hash = hashlib.sha256(RESULT_CSV.read_bytes()).hexdigest()
        self.assertEqual("a02c4e0bad6a7113937fbd23f4521c364d109944c7f05c94eb5839b9119d00e2", json_hash)
        self.assertEqual("3b6a164a4ca847d29b82d73b3841100f246cdc36b9b86f30198bfcfe586f6560", csv_hash)
        self.assertIn(json_hash, authority)
        self.assertIn(csv_hash, authority)

    def test_remediation_pass_remains_durable_after_later_review_gate(self) -> None:
        ledger = LEDGER.read_text(encoding="utf-8")
        state = json.loads(STATE.read_text(encoding="utf-8"))
        barracks = state["barracks_remediation"]
        self.assertIn(DECISION, ledger)
        self.assertIn(REVIEW_DECISION, ledger)
        self.assertEqual("APPROVED_5_OF_10_REMEDIATION_SMOKE_PASS", barracks["status"])
        self.assertEqual("PASS", barracks["smoke_rerun_status"])
        self.assertEqual([], barracks["failed_decision_gates"])
        self.assertEqual("STRUCTURAL_CHANNEL_VECTOR", barracks["capability_proxy"])
        self.assertEqual("FORBIDDEN", barracks["combat_power_scalar"])
        self.assertAlmostEqual(0.333333, barracks["observed_baseline_special_token_share_burst_max"], places=6)
        self.assertEqual("NOT_AUTHORIZED", barracks["product_implementation"])
        self.assertEqual(REVIEW_DECISION, state["last_gate_update_decision"])
        self.assertNotIn("BARRACKS_10000_SEED_DECISION_SWEEP_REVIEW_REQUIRED", state["entry_gate"]["blocking_reasons"])
        self.assertIn("BARRACKS_PARAMETER_SELECTION_IDENTIFIABILITY_REQUIRED", state["entry_gate"]["blocking_reasons"])
        self.assertEqual("BARRACKS_PARAMETER_SELECTION_OBSERVABLES_DEFINITION", state["entry_gate"]["allowed_next_actions"][0])
        self.assertIn("PRODUCT_IMPLEMENTATION", state["entry_gate"]["forbidden_actions"])


if __name__ == "__main__":
    unittest.main()
