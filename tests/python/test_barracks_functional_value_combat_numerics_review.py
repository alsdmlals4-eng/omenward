from __future__ import annotations

import json
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[2]
STATE = ROOT / "docs/operations/ACTIVE_INTEGRATED_CONTRACT_STATE.v1.json"
AUTHORITY = ROOT / "docs/design/APPROVED_OMENWARD_BARRACKS_FUNCTIONAL_VALUE_COMBAT_NUMERICS_DEFINITION_REVIEW_2026-08-09.md"
UNIT_TREE = ROOT / "docs/design/APPROVED_BARRACKS_AND_SPECIAL_CORPS_UNIT_TREE_V5.md"
LINEAGES = ROOT / "docs/design/APPROVED_PLAYER_TEN_UNIT_LINEAGES_POC_V1.md"
SHARED = ROOT / "docs/design/APPROVED_SHARED_UNIT_ARCHETYPE_AND_FACTION_VISUAL_DATA_V1.md"
SMOKE_MODEL = ROOT / "docs/analysis/barracks_simulation/smoke_model_assumptions.v1.json"
ARCHETYPE_PROFILE = ROOT / "scripts/data/unit_archetype_profile.gd"
UNIT_INSTANCE = ROOT / "scripts/battle/unit_instance.gd"
LANE_STATE = ROOT / "scripts/battle/lane_state.gd"
BATTLE = ROOT / "scripts/battle/battle_simulator.gd"
ATTACK_PROFILE = ROOT / "scripts/data/attack_profile.gd"
BOOTSTRAP = ROOT / "data/bootstrap_catalog.tres"

DECISION = "OMW-DEC-20260809-PLANNING-BARRACKS-FUNCTIONAL-VALUE-COMBAT-NUMERICS-DEFINITION-REVIEW-V1"
MEASUREMENT_DECISION = "OMW-DEC-20260809-PLANNING-BARRACKS-FUNCTIONAL-VALUE-MEASUREMENT-SCENARIOS-DEFINITION-V1"
SPECIAL_CORPS = ("priest", "mage", "flier", "giant")


def unit_resource(archetype: str) -> str:
    return (ROOT / f"data/units/{archetype}.tres").read_text(encoding="utf-8")


class BarracksFunctionalValueCombatNumericsReviewTest(unittest.TestCase):
    def test_product_special_corps_have_real_base_combat_numeric_resources(self) -> None:
        for archetype in SPECIAL_CORPS:
            text = unit_resource(archetype)
            for marker in ("max_health", "attack", "armor", "magic_resistance", "move_speed", "attack_range"):
                self.assertIn(marker, text, f"{archetype} missing {marker}")
        self.assertIn('structure_damage_tags = PackedStringArray("siege")', unit_resource("giant"))
        self.assertIn("capture_power = 0.0", unit_resource("flier"))

    def test_product_taxonomy_and_historical_simulation_label_set_are_not_the_same_set(self) -> None:
        unit_tree = UNIT_TREE.read_text(encoding="utf-8")
        self.assertRegex(unit_tree, r"기본 병영\s*\n1\. 방패병\n2\. 대검전사\n3\. 암살자")
        self.assertRegex(unit_tree, r"특수병단\s*\n1\. 사제\n2\. 마법사\n3\. 거인\n4\. 비행병")
        model = json.loads(SMOKE_MODEL.read_text(encoding="utf-8"))
        self.assertEqual(model["scenario_matrix"]["fixed_special_outcomes"], ["assassin", "priest", "mage", "flying_unit", "giant"])

    def test_canon_contains_role_specific_poc_numerics_but_marks_them_as_poc_hypotheses(self) -> None:
        text = LINEAGES.read_text(encoding="utf-8")
        self.assertIn("수치·이름은 첫 PoC 가설", text)
        for marker in (
            "치유 기도`: 같은 라인 아군 1기 최대 HP 10%+40 회복, 재사용 8초",
            "폭발 구체`: 중심 60, 주변 45 마법 피해, 최대 5기, 재사용 7초",
            "급강하`: 100거리 돌진, 70피해, 재사용 8초",
            "HP 900, 물리 방어 80, 마법저항 20",
            "공격 120, 간격 2.80초, 준비 1.10초",
        ):
            self.assertIn(marker, text)

    def test_runtime_is_not_role_complete_for_functional_value_measurement(self) -> None:
        profile = ARCHETYPE_PROFILE.read_text(encoding="utf-8")
        shared = SHARED.read_text(encoding="utf-8")
        lane = LANE_STATE.read_text(encoding="utf-8")
        unit = UNIT_INSTANCE.read_text(encoding="utf-8")
        attack = ATTACK_PROFILE.read_text(encoding="utf-8")
        bootstrap = BOOTSTRAP.read_text(encoding="utf-8")
        battle = BATTLE.read_text(encoding="utf-8")
        for approved_field in ("movement_layer", "passive_ids", "skill_ids", "targeting_profile_id", "threat_cost"):
            self.assertIn(approved_field, shared)
            self.assertNotIn(f"var {approved_field}", profile)
        self.assertIn("target_priority_tags", profile)
        self.assertNotIn("target_priority_tags", lane)
        self.assertIn("attacker.distance_to(left)", lane)
        self.assertIn("magic_resistance", unit_resource("mage"))
        receive_damage = re.search(r"func receive_damage\(.*?\n\n", unit, flags=re.S)
        self.assertIsNotNone(receive_damage)
        self.assertIn('get("armor"', receive_damage.group(0))
        self.assertNotIn("magic_resistance", receive_damage.group(0))
        self.assertIn("preparation_ms: int = 100", attack)
        self.assertIn("hit_ms: int = 100", attack)
        self.assertIn("recovery_ms: int = 100", attack)
        self.assertNotIn("preparation_ms =", bootstrap)
        self.assertNotIn("hit_ms =", bootstrap)
        self.assertNotIn("recovery_ms =", bootstrap)
        self.assertIn("request_assassin_bypass", battle)
        self.assertIn("unit.is_siege_damage()", battle)
        self.assertNotIn("healing", battle.lower())
        self.assertNotIn("movement_layer", battle)
        self.assertNotIn("target_layers", battle)

    def test_review_authority_exists_and_refines_the_blocker_without_selecting_a_scalar(self) -> None:
        self.assertTrue(AUTHORITY.is_file(), f"missing review authority: {AUTHORITY.relative_to(ROOT)}")
        text = AUTHORITY.read_text(encoding="utf-8")
        for marker in (
            DECISION,
            "PRODUCT_BASE_COMBAT_NUMERICS = PRESENT",
            "ROLE_COMPLETE_PRODUCT_OUTPUT_NUMERICS = PARTIAL_INSUFFICIENT",
            "PRODUCT_SPECIAL_CORPS = PRIEST_MAGE_FLIER_GIANT",
            "HISTORICAL_SIMULATION_SPECIAL_OUTCOME_LABEL_SET = ASSASSIN_PRIEST_MAGE_FLYING_GIANT",
            "FUNCTIONAL_VALUE_COMPARISON = ROLE_SPECIFIC_VECTOR_NO_SINGLE_WEIGHTED_SCORE",
            "FINAL_FUNCTIONAL_VALUE_INDEX = NOT_SELECTED",
            "FINAL_PARAMETER_VECTOR = NOT_SELECTED",
        ):
            self.assertIn(marker, text)

    def test_review_state_remains_durable_after_measurement_scenario_gate(self) -> None:
        state = json.loads(STATE.read_text(encoding="utf-8"))
        gate = state["entry_gate"]
        review = state["barracks_functional_value_combat_numerics_review"]
        scenarios = state["barracks_functional_value_measurement_scenarios"]
        self.assertNotIn("BARRACKS_FUNCTIONAL_VALUE_COMBAT_NUMERICS_REQUIRED", gate["blocking_reasons"])
        self.assertNotIn("BARRACKS_FUNCTIONAL_VALUE_MEASUREMENT_SCENARIOS_REQUIRED", gate["blocking_reasons"])
        self.assertIn("BARRACKS_ROLE_OUTPUT_RUNTIME_IMPLEMENTATION_REQUIRED", gate["blocking_reasons"])
        self.assertEqual(gate["decision"], "BLOCK")
        self.assertEqual(review["decision_id"], DECISION)
        self.assertEqual(review["product_base_combat_numerics"], "PRESENT")
        self.assertEqual(review["role_complete_product_output_numerics"], "PARTIAL_INSUFFICIENT")
        self.assertEqual(review["product_special_corps"], ["priest", "mage", "flier", "giant"])
        self.assertIsNone(review["final_functional_value_index"])
        self.assertIsNone(review["final_parameter_vector"])
        self.assertEqual(scenarios["decision_id"], MEASUREMENT_DECISION)
        self.assertEqual(scenarios["measurement_scenario_blocker"], "CLOSED_BY_THIS_DECISION")
        self.assertEqual(scenarios["role_output_runtime_blocker"], "REMAINS")


if __name__ == "__main__":
    unittest.main()
