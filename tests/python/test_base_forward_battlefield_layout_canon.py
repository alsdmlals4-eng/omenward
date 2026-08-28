from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[2]
LAYOUT = ROOT / "docs/design/APPROVED_OMENWARD_BASE_FORWARD_BATTLEFIELD_CONSTRUCTION_LAYOUT_2026-08-28.md"
DECISIONS = ROOT / "docs/CURRENT_CONFIRMED_DECISIONS.md"
FTUE = ROOT / "docs/design/APPROVED_OMENWARD_FIRST5_FTUE_MASTERY_LADDER_2026-08-20.md"
TIER_LINEAGE = ROOT / "docs/design/APPROVED_OMENWARD_BUILDING_TIER_REALIGNMENT_2026-08-06.md"


class BaseForwardBattlefieldLayoutCanonTest(unittest.TestCase):
    def test_layout_owner_locks_the_user_approved_counts_and_boundaries(self) -> None:
        text = LAYOUT.read_text(encoding="utf-8")
        for marker in (
            "OMW-PLAN-20260828-BASE-FORWARD-BATTLEFIELD-CONSTRUCTION-LAYOUT-01",
            "HOME_BASE_CONSTRUCTION_NODE_COUNT_PER_FACTION = 4",
            "HOME_BASE_FIXED_AUTO_ATTACK_TOWER_COUNT_PER_FACTION = 2",
            "FORWARD_BASE_CONSTRUCTION_NODE_COUNT_PER_BASE = 2",
            "FORWARD_BASE_FIXED_AUTO_ATTACK_TOWER_COUNT_PER_BASE = 1",
            "FORWARD_BASE_FIXED_DEFENSE_STACK = FORWARD_BARRICADE + AUTO_ATTACK_TOWER",
            "TOTAL_CONSTRUCTION_NODE_CAPACITY_PER_FACTION = 10",
            "HOME_BASE_PREBUILT_PRODUCTION_BUILDINGS = NONE",
            "FIXED_DEFENSE_SOLO_CLEAR = FORBIDDEN",
            "PHASE_2_PRODUCT_CODE_AUTHORITY = NONE",
        ):
            self.assertIn(marker, text)

    def test_current_summaries_route_to_the_new_layout_owner(self) -> None:
        expected = "docs/design/APPROVED_OMENWARD_BASE_FORWARD_BATTLEFIELD_CONSTRUCTION_LAYOUT_2026-08-28.md"
        self.assertIn(expected, DECISIONS.read_text(encoding="utf-8"))
        self.assertIn(expected, FTUE.read_text(encoding="utf-8"))

    def test_stage_one_no_longer_claims_visible_barracks_or_farm_at_home(self) -> None:
        text = FTUE.read_text(encoding="utf-8")
        self.assertIn("STAGE_1_WARD_CITADEL_PREBUILT_PRODUCTION_BUILDINGS = NONE", text)
        self.assertNotIn("STAGE_1_WARD_CITADEL = GENERAL_BARRACKS x1 + FARM x1", text)

    def test_tier_lineage_keeps_tiers_but_cannot_restore_stage_one_visible_production_buildings(self) -> None:
        text = TIER_LINEAGE.read_text(encoding="utf-8")
        self.assertIn("STAGE_1_VISIBLE_PRODUCTION_BUILDINGS = NONE", text)
        self.assertIn("STAGE_1_HOME_COMMAND_ROOT = 4_LOCKED_CONSTRUCTION_NODES + 2_FIXED_AUTO_ATTACK_TOWERS", text)
        self.assertNotIn("STAGE_1_PREBUILT_FACILITY_TYPES = GENERAL_BARRACKS / FARM / FORWARD_BASE_DEFENSE_SYSTEM", text)


if __name__ == "__main__":
    unittest.main()
