from pathlib import Path
import json
import unittest

ROOT = Path(__file__).resolve().parents[2]
DECISION_ID = "OMW-DEC-20260806-PLANNING-CURRENT-MAPRUN-ECONOMY-AND-PRESSURE-BASELINE-V1"

AUTHORITY = ROOT / "docs/design/APPROVED_OMENWARD_CURRENT_MAPRUN_ECONOMY_AND_PRESSURE_BASELINE_2026-08-06.md"
BASELINE = ROOT / "docs/analysis/barracks_simulation/current_maprun_economy_pressure_baseline.v1.json"
REVIEW = ROOT / "docs/reviews/ADVERSARIAL_CURRENT_MAPRUN_ECONOMY_AND_PRESSURE_BASELINE_REVIEW_2026-08-06.md"
SPEC = ROOT / "docs/superpowers/specs/2026-08-06-current-maprun-economy-pressure-baseline-design.md"
PLAN = ROOT / "docs/superpowers/plans/2026-08-06-current-maprun-economy-pressure-baseline.md"
ACTIVE = ROOT / "docs/ACTIVE_CONTEXT.md"
PENDING = ROOT / "docs/DECISIONS_PENDING.md"
LEDGER = ROOT / "docs/PROJECT_CANON_DECISION_LEDGER.md"
MAP = ROOT / "docs/DOCUMENTATION_MAP.md"
LIFECYCLE = ROOT / "docs/DOCUMENT_LIFECYCLE_REGISTRY.md"


class CurrentMapRunEconomyPressureBaselineTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.authority = AUTHORITY.read_text(encoding="utf-8")
        cls.baseline = json.loads(BASELINE.read_text(encoding="utf-8"))
        cls.review = REVIEW.read_text(encoding="utf-8")
        cls.spec = SPEC.read_text(encoding="utf-8")
        cls.plan = PLAN.read_text(encoding="utf-8")
        cls.active = ACTIVE.read_text(encoding="utf-8")
        cls.pending = PENDING.read_text(encoding="utf-8")
        cls.ledger = LEDGER.read_text(encoding="utf-8")
        cls.map = MAP.read_text(encoding="utf-8")
        cls.lifecycle = LIFECYCLE.read_text(encoding="utf-8")

    def test_authority_is_approved_third_gate_and_smoke_only(self) -> None:
        self.assertIn(f"decision_id: {DECISION_ID}", self.authority)
        self.assertIn("status: APPROVED_SIMULATION_BASELINE", self.authority)
        self.assertIn("approval_count: 3_OF_10", self.authority)
        self.assertIn("SIMULATION_RUNNABLE = TRUE_FOR_SMOKE_ONLY", self.authority)
        self.assertIn("DECISION_SWEEP = BLOCKED_UNTIL_SMOKE_PASS", self.authority)
        self.assertIn("PRODUCT_IMPLEMENTATION = NOT_AUTHORIZED", self.authority)

    def test_foundation_and_stage2_gold_contracts_are_exact(self) -> None:
        economy = self.baseline["economy"]
        required = economy["required_stage1_t1_costs_gold"]
        self.assertEqual(sum(required.values()), 250)
        self.assertEqual(economy["maprun_starting_foundation_gold"], 250)
        self.assertEqual(economy["stage1_operational_gold_grant_after_foundation"], 20)
        self.assertEqual(economy["base_spin_cost_gold"], 20)
        self.assertEqual(economy["stage2_first_t2_cost_gold"], 50)
        self.assertEqual(economy["stage2_reserved_gold_grant"], 50)
        self.assertEqual(economy["kill_gold"], 0)
        self.assertEqual(economy["wave_clear_gold"], 0)

    def test_income_and_timer_rules_use_active_combat_time(self) -> None:
        economy = self.baseline["economy"]
        self.assertEqual(economy["base_income"], {"gold": 3, "interval_active_combat_seconds": 20})
        self.assertEqual(economy["vault_t1_income"], {"gold": 3, "interval_active_combat_seconds": 20})
        self.assertEqual(economy["midpoint_control_income"], {"gold_per_point": 4, "interval_active_combat_seconds": 60})
        self.assertEqual(economy["income_timer_scope"], "MAPRUN_PERSISTENT_PAUSED_OUTSIDE_ACTIVE_COMBAT")

    def test_maintenance_clock_matrix_prevents_afk_farming(self) -> None:
        matrix = self.baseline["maintenance_clock_matrix"]
        self.assertEqual(matrix["baseline_active_decision_seconds"], 30)
        self.assertFalse(matrix["passive_gold_income"])
        self.assertFalse(matrix["midpoint_control_income"])
        self.assertFalse(matrix["unit_auto_production"])
        self.assertTrue(matrix["construction_upgrade_repair_progress"])
        self.assertFalse(matrix["mana_regeneration_and_cooldowns"])
        self.assertFalse(matrix["damage_healing_status_ticks"])
        self.assertTrue(matrix["accessibility_pause_suspends_all_maintenance_clocks"])

    def test_production_intervals_resolve_general_and_five_special_units(self) -> None:
        production = self.baseline["production_intervals_active_combat_seconds"]
        self.assertEqual(production["basic_infantry"], 50)
        self.assertEqual(production["shield"], 65)
        self.assertEqual(production["archer"], 65)
        self.assertEqual(production["assassin"], 75)
        self.assertEqual(production["priest"], 80)
        self.assertEqual(production["mage"], 90)
        self.assertEqual(production["flying_unit"], 100)
        self.assertEqual(production["giant"], 110)

    def test_first_five_stage_timeline_fits_onboarding_window(self) -> None:
        stages = self.baseline["stage_1_to_5_pressure_baseline"]
        active_seconds = sum(stage["expected_active_combat_seconds"] for stage in stages)
        total = active_seconds + self.baseline["onboarding_timeline"]["foundation_setup_expected_seconds"] + 4 * self.baseline["maintenance_clock_matrix"]["baseline_active_decision_seconds"]
        self.assertEqual(active_seconds, 660)
        self.assertEqual(total, 830)
        self.assertGreaterEqual(total, 600)
        self.assertLessEqual(total, 900)
        self.assertEqual([stage["pressure"] for stage in stages], ["MASS", "ARMORED", "FLYING", "INFILTRATION", "SIEGE"])
        self.assertEqual([stage["wave_threat_budgets_tu"] for stage in stages], [[8, 12, 16], [7, 12, 17], [6, 11, 16], [7, 13, 19], [10, 18, 28]])

    def test_wave_start_rule_avoids_forced_overlap_before_stage9(self) -> None:
        self.assertEqual(self.baseline["wave_start_rule"], "MAX_TARGET_OFFSET_OR_PREVIOUS_CLEAR_PLUS_8_SECONDS")
        self.assertFalse(self.baseline["forced_overlap_before_stage9"])
        for stage in self.baseline["stage_1_to_5_pressure_baseline"]:
            self.assertEqual(len(stage["wave_target_offsets_seconds"]), 3)
            self.assertEqual(stage["wave_target_offsets_seconds"][0], 0)

    def test_opportunity_cost_is_vector_not_fake_single_score(self) -> None:
        opportunity = self.baseline["opportunity_cost"]
        self.assertEqual(opportunity["food_cap_start"], 12)
        self.assertEqual(opportunity["farm_t1_food_cap_bonus"], 6)
        self.assertEqual(opportunity["post_foundation_optional_node_budget_baseline"], 2)
        self.assertEqual(opportunity["food_equivalent_formula"], "unit_food_cost / 6")
        self.assertEqual(opportunity["node_equivalent_formula"], "occupied_optional_nodes / 2")
        self.assertEqual(opportunity["comparison_form"], "VECTOR_GOLD_TIME_FOOD_NODE_NO_SINGLE_WEIGHTED_SCORE")

    def test_adversarial_review_names_stop_ship_risks(self) -> None:
        for marker in (
            "MANDATORY_VAULT_INCOME_DOUBLE_COUNT_RISK",
            "FOUNDATION_GRANT_SURPLUS_LEAK_RISK",
            "MAINTENANCE_AFK_FARM_RISK",
            "SPECIAL_BARRACKS_DOUBLE_VALUE_DOMINANCE_RISK",
            "FIRST_FIVE_STAGE_FORCED_OVERLAP_RISK",
            "THREAT_UNIT_FALSE_PRECISION_RISK",
            "SMOKE_PASS_ESCALATION_WITHOUT_REVIEW = FORBIDDEN",
        ):
            with self.subTest(marker=marker):
                self.assertIn(marker, self.review)

    def test_router_documents_point_to_third_gate(self) -> None:
        for text in (self.active, self.pending, self.ledger, self.map, self.lifecycle):
            self.assertIn(DECISION_ID, text)
        self.assertIn("current_grill_me_count: 3_OF_10", self.active)
        self.assertIn("NEXT_GATE = BARRACKS_SMOKE_SWEEP_EXECUTION", self.active)
        self.assertIn("[현행]", self.lifecycle)

    def test_spec_plan_and_product_boundary_are_explicit(self) -> None:
        self.assertIn("HYBRID_ABSOLUTE_ONBOARDING_AND_NORMALIZED_THREAT_BASELINE", self.spec)
        self.assertIn("tests/python/test_current_maprun_economy_pressure_baseline.py", self.plan)
        self.assertIn("Do not modify GDScript, Scene, Resource, project.godot, or gameplay data", self.plan)
        for text in (self.authority, self.review):
            self.assertIn("PRODUCT_CODE = UNCHANGED", text)
            self.assertIn("LOCAL_GODOT_PROJECT = UNCHANGED", text)


if __name__ == "__main__":
    unittest.main()
