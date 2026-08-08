from __future__ import annotations

import json
import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[2]
MODEL = ROOT / "docs" / "analysis" / "barracks_simulation" / "smoke_model_assumptions.v1.json"
BASELINE = ROOT / "docs" / "analysis" / "barracks_simulation" / "current_maprun_economy_pressure_baseline.v1.json"
STATE = ROOT / "docs" / "operations" / "ACTIVE_INTEGRATED_CONTRACT_STATE.v1.json"
SPEC = ROOT / "docs" / "design" / "APPROVED_OMENWARD_BARRACKS_PARAMETER_SELECTION_OBSERVABLES_2026-08-08.md"

DECISION_ID = "OMW-DEC-20260808-PLANNING-BARRACKS-PARAMETER-SELECTION-OBSERVABLES-DEFINITION-V1"


class BarracksParameterSelectionObservablesTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.model = json.loads(MODEL.read_text(encoding="utf-8"))
        cls.baseline = json.loads(BASELINE.read_text(encoding="utf-8"))
        cls.state = json.loads(STATE.read_text(encoding="utf-8"))

    def test_current_grid_exposes_canon_interval_violation(self) -> None:
        general_max = max(
            float(self.baseline["production_intervals_active_combat_seconds"][name])
            for name in ("basic_infantry", "shield", "archer")
        )
        special_base = [
            float(self.baseline["production_intervals_active_combat_seconds"][name])
            for name in ("assassin", "priest", "mage", "flying_unit", "giant")
        ]
        failed = []
        passed = []
        for vector in self.model["parameter_vectors"]:
            scale = float(vector["special_interval_multiplier"]) / 1.70
            min_special = min(value * scale for value in special_base)
            (passed if min_special > general_max else failed).append(vector["vector_id"])
        self.assertEqual(
            failed,
            [
                "V01_CHEAP_FAST_LOW",
                "V02_CHEAP_FAST_HIGH",
                "V05_EXPENSIVE_FAST_LOW",
                "V06_EXPENSIVE_FAST_HIGH",
            ],
        )
        self.assertEqual(
            passed,
            [
                "V00_BASELINE",
                "V03_CHEAP_SLOW_LOW",
                "V04_CHEAP_SLOW_HIGH",
                "V07_EXPENSIVE_SLOW_LOW",
                "V08_EXPENSIVE_SLOW_HIGH",
            ],
        )

    def test_approved_baseline_forbids_single_weighted_opportunity_score(self) -> None:
        opportunity = self.baseline["opportunity_cost"]
        self.assertEqual(
            opportunity["comparison_form"],
            "VECTOR_GOLD_TIME_FOOD_NODE_NO_SINGLE_WEIGHTED_SCORE",
        )
        self.assertEqual(opportunity["gold_equivalent_formula"], "investment_gold / 40")
        self.assertEqual(opportunity["time_equivalent_formula"], "first_unit_wait_active_combat_seconds / 50")
        self.assertEqual(opportunity["food_equivalent_formula"], "unit_food_cost / 6")
        self.assertEqual(opportunity["node_equivalent_formula"], "occupied_optional_nodes / 2")

    def test_observable_authority_exists_and_defers_functional_value(self) -> None:
        self.assertTrue(SPEC.is_file(), f"missing observable authority: {SPEC.relative_to(ROOT)}")
        text = SPEC.read_text(encoding="utf-8")
        for marker in (
            DECISION_ID,
            "SPECIAL_INTERVAL_CANON_GATE = STRICTLY_LONGER_THAN_RELEVANT_GENERAL_INTERVAL",
            "COMPARISON_FORM = VECTOR_GOLD_TIME_FOOD_NODE_NO_SINGLE_WEIGHTED_SCORE",
            "SPECIAL_FUNCTIONAL_VALUE_INDEX = DEFERRED_UNTIL_PRODUCT_COMBAT_NUMERICS",
            "ECONOMY_PRODUCTION_ENVELOPE = V00_BASELINE_COST_INTERVAL_ONLY",
            "FINAL_PARAMETER_VECTOR = NOT_SELECTED",
            "ROBUSTNESS_ONLY_10000 = READY_FOR_SEPARATE_APPROVAL",
        ):
            self.assertIn(marker, text)

    def test_durable_gate_advances_without_authorizing_10k(self) -> None:
        self.assertEqual(self.state["last_gate_update_decision"], DECISION_ID)
        gate = self.state["entry_gate"]
        self.assertNotIn("BARRACKS_PARAMETER_SELECTION_IDENTIFIABILITY_REQUIRED", gate["blocking_reasons"])
        self.assertIn("BARRACKS_FUNCTIONAL_VALUE_COMBAT_NUMERICS_REQUIRED", gate["blocking_reasons"])
        self.assertEqual(gate["allowed_next_actions"][0], "BARRACKS_10000_SEED_ROBUSTNESS_ONLY_REVIEW")
        self.assertIn("BARRACKS_10000_SEED_PARAMETER_SELECTION_EXECUTION", gate["forbidden_actions"])
        self.assertIn("BARRACKS_50000_SEED_CONFIRMATION", gate["forbidden_actions"])


if __name__ == "__main__":
    unittest.main()
