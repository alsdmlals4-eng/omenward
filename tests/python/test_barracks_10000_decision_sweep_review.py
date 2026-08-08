from __future__ import annotations

import csv
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DECISION = "OMW-DEC-20260808-PLANNING-BARRACKS-10000-SEED-DECISION-SWEEP-REVIEW-V1"
REVIEW = ROOT / "docs/design/APPROVED_OMENWARD_BARRACKS_10000_SEED_DECISION_SWEEP_REVIEW_2026-08-08.md"
STATE = ROOT / "docs/operations/ACTIVE_INTEGRATED_CONTRACT_STATE.v1.json"
PENDING = ROOT / "docs/DECISIONS_PENDING.md"
CSV = ROOT / "docs/analysis/barracks_simulation/smoke_sweep_2000.v2.csv"

DECISION_METRICS = (
    "special_token_share_10_min",
    "special_token_share_burst_max",
    "second_special_marginal_value_ratio",
)


class Barracks10000DecisionSweepReviewTest(unittest.TestCase):
    def test_2k_has_decision_metric_ties_that_more_seeds_cannot_define_away(self) -> None:
        rows = list(csv.DictReader(CSV.read_text(encoding="utf-8").splitlines()))
        signatures: dict[tuple[str, ...], list[str]] = {}
        for row in rows:
            signature = tuple(row[name] for name in DECISION_METRICS)
            signatures.setdefault(signature, []).append(row["vector_id"])
        tied_groups = sorted(group for group in signatures.values() if len(group) > 1)
        self.assertIn(["V03_CHEAP_SLOW_LOW", "V04_CHEAP_SLOW_HIGH"], tied_groups)
        self.assertIn(["V05_EXPENSIVE_FAST_LOW", "V06_EXPENSIVE_FAST_HIGH", "V07_EXPENSIVE_SLOW_LOW", "V08_EXPENSIVE_SLOW_HIGH"], tied_groups)

    def test_review_authority_blocks_false_parameter_selection_precision(self) -> None:
        text = REVIEW.read_text(encoding="utf-8")
        self.assertIn(DECISION, text)
        self.assertIn("REVIEW_COMPLETE", text)
        self.assertIn("PARAMETER_SELECTION_NOT_IDENTIFIABLE", text)
        self.assertIn("DECISION_SWEEP_10000_EXECUTION = NOT_AUTHORIZED", text)
        self.assertIn("ROBUSTNESS_ONLY_10000 = OPTIONAL_AFTER_SEPARATE_APPROVAL", text)
        self.assertIn("FINAL_PARAMETER_VECTOR = NOT_SELECTED", text)

    def test_review_completion_remains_durable_when_later_gates_advance(self) -> None:
        state = json.loads(STATE.read_text(encoding="utf-8"))
        gate = state["entry_gate"]
        review = state["barracks_10000_review"]
        self.assertNotIn("BARRACKS_10000_SEED_DECISION_SWEEP_REVIEW_REQUIRED", gate["blocking_reasons"])
        self.assertEqual(review["decision_id"], DECISION)
        self.assertEqual(review["status"], "REVIEW_COMPLETE_EXECUTION_NOT_AUTHORIZED")
        self.assertEqual(review["parameter_selection"], "NOT_IDENTIFIABLE_WITH_CURRENT_DECISION_METRICS")
        self.assertEqual(review["decision_sweep_10000_execution"], "NOT_AUTHORIZED")
        self.assertEqual(review["confirmation_sweep_50000"], "BLOCKED")
        self.assertIsNone(review["final_parameter_vector"])
        self.assertIn("BARRACKS_10000_SEED_PARAMETER_SELECTION_EXECUTION", gate["forbidden_actions"])

    def test_pending_decisions_preserves_review_history_without_stale_zero_of_ten(self) -> None:
        text = PENDING.read_text(encoding="utf-8")
        self.assertIn("5_OF_10 = REMEDIATION_SMOKE_PASS", text)
        self.assertIn("6_OF_10_REVIEW = 10000_DECISION_SWEEP_REVIEW_COMPLETE", text)
        self.assertIn(DECISION, (ROOT / "docs/PROJECT_CANON_DECISION_LEDGER.md").read_text(encoding="utf-8"))
        self.assertNotIn("current_grill_me_count: 0_OF_10", text)
        self.assertNotIn("next_gate: BARRACKS_ECONOMY_PRODUCTION_AND_TOKEN_SOURCE_SIMULATION_CONTRACT", text)


if __name__ == "__main__":
    unittest.main()
