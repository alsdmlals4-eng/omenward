from __future__ import annotations

import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[2]
DECISION = "OMW-DEC-20260808-PLANNING-BARRACKS-10000-SEED-ROBUSTNESS-ONLY-REVIEW-V1"
REVIEW = ROOT / "docs/design/APPROVED_OMENWARD_BARRACKS_10000_SEED_ROBUSTNESS_ONLY_REVIEW_2026-08-08.md"
STATE = ROOT / "docs/operations/ACTIVE_INTEGRATED_CONTRACT_STATE.v1.json"
RUNNER = ROOT / "docs/analysis/barracks_simulation/run_barracks_remediation_smoke.py"
ANALYSIS = ROOT / "docs/analysis/barracks_simulation"


class Barracks10000RobustnessReviewTest(unittest.TestCase):
    def test_current_runner_is_not_safe_durable_10k_evidence_writer(self) -> None:
        text = RUNNER.read_text(encoding="utf-8")
        self.assertIn('stem="smoke_sweep_2000.v2"', text)
        self.assertIn('output_dir or analysis_dir', text)
        self.assertIn('DECISION_ID = "OMW-DEC-20260808-PLANNING-BARRACKS-CAPABILITY-PROXY-AND-MULTI-SPECIAL-TOKEN-BURST-REMEDIATION-V1"', text)

    def test_no_10k_evidence_has_been_persisted(self) -> None:
        names = {p.name for p in ANALYSIS.iterdir() if p.is_file()}
        self.assertFalse(any("10000" in name for name in names))

    def test_review_authority_records_blocked_execution_contract(self) -> None:
        self.assertTrue(REVIEW.is_file(), f"missing review authority: {REVIEW.relative_to(ROOT)}")
        text = REVIEW.read_text(encoding="utf-8")
        self.assertIn(DECISION, text)
        self.assertIn("ROBUSTNESS_10000 = RECOMMENDED_AFTER_DEDICATED_EXECUTION_CONTRACT_AND_USER_APPROVAL", text)
        self.assertIn("CURRENT_RUNNER_FOR_DURABLE_10K = UNSAFE_EVIDENCE_PROVENANCE", text)
        self.assertIn("ACTUAL_10000_EXECUTION = NOT_RUN", text)
        self.assertIn("FINAL_PARAMETER_VECTOR = NOT_SELECTED", text)

    def test_durable_state_advances_review_without_authorizing_run(self) -> None:
        state = json.loads(STATE.read_text(encoding="utf-8"))
        self.assertEqual(state["last_gate_update_decision"], DECISION)
        review = state["barracks_10000_robustness_review"]
        self.assertEqual(review["decision_id"], DECISION)
        self.assertEqual(review["actual_10000_execution"], "NOT_RUN")
        self.assertEqual(review["execution_contract"], "DEDICATED_RUNNER_REQUIRED")
        self.assertEqual(review["execution_user_approval"], "REQUIRED")
        self.assertEqual(review["parameter_selection_10000"], "NOT_AUTHORIZED")
        self.assertEqual(review["confirmation_sweep_50000"], "BLOCKED")
        self.assertIsNone(review["final_parameter_vector"])
        self.assertEqual(state["entry_gate"]["decision"], "BLOCK")


if __name__ == "__main__":
    unittest.main()
