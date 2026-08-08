from __future__ import annotations

import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[2]
PARENT_AUTHORITY = ROOT / "docs/design/APPROVED_OMENWARD_BARRACKS_FUNCTIONAL_VALUE_COMBAT_NUMERICS_DEFINITION_REVIEW_2026-08-09.md"
AUTHORITY = ROOT / "docs/design/APPROVED_OMENWARD_BARRACKS_FUNCTIONAL_VALUE_MEASUREMENT_SCENARIOS_2026-08-09.md"
STATE = ROOT / "docs/operations/ACTIVE_INTEGRATED_CONTRACT_STATE.v1.json"

DECISION = "OMW-DEC-20260809-PLANNING-BARRACKS-FUNCTIONAL-VALUE-MEASUREMENT-SCENARIOS-DEFINITION-V1"
PARENT_DECISION = "OMW-DEC-20260809-PLANNING-BARRACKS-FUNCTIONAL-VALUE-COMBAT-NUMERICS-DEFINITION-REVIEW-V1"
FIXTURE_IDS = (
    "shield_guard",
    "greatsword_warrior",
    "archer",
    "assassin",
    "priest",
    "mage",
    "flier",
    "giant",
)
SCENARIO_IDS = (
    "FV-COMMON-01",
    "FV-PRIEST-01",
    "FV-MAGE-01",
    "FV-FLIER-01",
    "FV-GIANT-01",
)


class BarracksFunctionalValueMeasurementScenariosTest(unittest.TestCase):
    def test_fixture_archetype_resources_exist(self) -> None:
        for archetype in FIXTURE_IDS:
            path = ROOT / f"data/units/{archetype}.tres"
            self.assertTrue(path.is_file(), f"missing fixture resource: {path.relative_to(ROOT)}")
            text = path.read_text(encoding="utf-8")
            self.assertIn(f'archetype_id = &"{archetype}"', text)

    def test_parent_review_pre_registers_role_vector_and_runtime_blocker(self) -> None:
        text = PARENT_AUTHORITY.read_text(encoding="utf-8")
        for marker in (
            PARENT_DECISION,
            "FUNCTIONAL_VALUE_COMPARISON = ROLE_SPECIFIC_VECTOR_NO_SINGLE_WEIGHTED_SCORE",
            "POST_HOC_WEIGHT_TUNING = FORBIDDEN",
            "BARRACKS_ROLE_OUTPUT_RUNTIME_IMPLEMENTATION_REQUIRED",
            "BARRACKS_FUNCTIONAL_VALUE_MEASUREMENT_SCENARIOS_REQUIRED",
            "NEXT_GATE = BARRACKS_FUNCTIONAL_VALUE_MEASUREMENT_SCENARIOS_DEFINITION",
        ):
            self.assertIn(marker, text)

    def test_measurement_scenario_authority_freezes_deterministic_fixtures_and_blocked_outputs(self) -> None:
        self.assertTrue(AUTHORITY.is_file(), f"missing scenario authority: {AUTHORITY.relative_to(ROOT)}")
        text = AUTHORITY.read_text(encoding="utf-8")
        for marker in (
            DECISION,
            "FIXTURE_POLICY = DETERMINISTIC_SAME_INPUT",
            "FUNCTIONAL_VALUE_COMPARISON = ROLE_SPECIFIC_VECTOR_NO_SINGLE_WEIGHTED_SCORE",
            "POST_HOC_WEIGHT_TUNING = FORBIDDEN",
            "BLOCKED_RUNTIME_OUTPUT = NEVER_SYNTHESIZE_AS_ZERO",
            "FINAL_FUNCTIONAL_VALUE_INDEX = NOT_SELECTED",
            "FINAL_PARAMETER_VECTOR = NOT_SELECTED",
        ):
            self.assertIn(marker, text)
        for scenario_id in SCENARIO_IDS:
            self.assertIn(scenario_id, text)
        self.assertIn("archer sustained single-target", text.lower())
        self.assertIn("assassin single-target burst", text.lower())
        self.assertIn("flier backline-pressure duration", text.lower())
        self.assertIn("giant survival/aoe/siege", text.lower())
        self.assertIn("priest", text.lower())

    def test_scenario_authority_classifies_role_defining_outputs_without_fake_values(self) -> None:
        self.assertTrue(AUTHORITY.is_file(), f"missing scenario authority: {AUTHORITY.relative_to(ROOT)}")
        text = AUTHORITY.read_text(encoding="utf-8")
        for blocked in (
            "EFFECTIVE_HEALING_HP = BLOCKED_RUNTIME_OUTPUT",
            "COLLATERAL_AOE_DAMAGE = BLOCKED_RUNTIME_OUTPUT",
            "FLIER_TIME_TO_BACKLINE_CONTACT = BLOCKED_RUNTIME_OUTPUT",
            "SLAM_TARGETS_HIT = BLOCKED_RUNTIME_OUTPUT",
        ):
            self.assertIn(blocked, text)
        self.assertNotIn("BLOCKED_RUNTIME_OUTPUT = 0", text)

    def test_durable_state_closes_only_measurement_scenario_blocker(self) -> None:
        state = json.loads(STATE.read_text(encoding="utf-8"))
        self.assertEqual(state["last_gate_update_decision"], DECISION)
        gate = state["entry_gate"]
        self.assertNotIn("BARRACKS_FUNCTIONAL_VALUE_MEASUREMENT_SCENARIOS_REQUIRED", gate["blocking_reasons"])
        self.assertIn("BARRACKS_ROLE_OUTPUT_RUNTIME_IMPLEMENTATION_REQUIRED", gate["blocking_reasons"])
        self.assertEqual(gate["allowed_next_actions"][0], "BARRACKS_ROLE_OUTPUT_RUNTIME_IMPLEMENTATION_PACKAGE")
        self.assertEqual(gate["decision"], "BLOCK")
        scenarios = state["barracks_functional_value_measurement_scenarios"]
        self.assertEqual(scenarios["decision_id"], DECISION)
        self.assertEqual(scenarios["parent_decision_id"], PARENT_DECISION)
        self.assertEqual(scenarios["fixture_policy"], "DETERMINISTIC_SAME_INPUT")
        self.assertEqual(scenarios["functional_value_comparison"], "ROLE_SPECIFIC_VECTOR_NO_SINGLE_WEIGHTED_SCORE")
        self.assertEqual(scenarios["scenario_ids"], list(SCENARIO_IDS))
        self.assertIsNone(scenarios["final_functional_value_index"])
        self.assertIsNone(scenarios["final_parameter_vector"])
        self.assertEqual(scenarios["product_implementation"], "NOT_AUTHORIZED")


if __name__ == "__main__":
    unittest.main()
