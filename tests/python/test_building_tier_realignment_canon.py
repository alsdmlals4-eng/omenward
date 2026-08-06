from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[2]
TIER = ROOT / "docs/design/APPROVED_OMENWARD_BUILDING_TIER_REALIGNMENT_2026-08-06.md"
FINAL = ROOT / "docs/design/APPROVED_OMENWARD_ONBOARDING_COMPLETION_MINIMUM_VALID_PATHS_AND_HUMAN_STOP_SHIP_2026-08-06.md"

class BuildingTierFinalLifecycleTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tier = TIER.read_text(encoding="utf-8")
        cls.final = FINAL.read_text(encoding="utf-8")

    def test_current_tier_contract(self):
        for marker in (
            "SPECIAL_T1_TOKEN_SOURCE = NONE",
            "SPECIAL_T2_TOKEN_SOURCE = SELECTED_SPECIAL_UNIT",
            "DEFENSE_TOWER_T2 = ARTILLERY / DEFENSE_ENHANCEMENT / SNIPER",
            "LINEAR_TIER_BUILDINGS = VAULT / FARM / COMMAND_POST / MANA_TOWER",
        ):
            self.assertIn(marker, self.tier)

    def test_planning_lifecycle_is_complete(self):
        self.assertIn("DECISION_STATUS = APPROVED_10_OF_10", self.final)
        self.assertIn("PARENT_FIRST_10_15_MINUTES_FLOW = PLANNING_COMPLETE", self.final)
        self.assertNotIn("NEXT_DECISION = FIRST_STAGE2_T2_CANDIDATES_AND_GOLD_RULES", self.final)

    def test_product_boundary_remains_closed(self):
        self.assertIn("PRODUCT_CODE = UNCHANGED", self.final)
        self.assertIn("LOCAL_GODOT_PROJECT = UNCHANGED", self.final)

if __name__ == "__main__":
    unittest.main()
