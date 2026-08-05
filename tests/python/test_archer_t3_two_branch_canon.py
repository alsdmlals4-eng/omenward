from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[2]
AUTHORITY = ROOT / "docs/design/APPROVED_OMENWARD_UNIT_BUILDING_TIER_MATRIX_AND_ARCHER_T3_CORRECTION_2026-08-06.md"
REVIEW = ROOT / "docs/reviews/ADVERSARIAL_ARCHER_T3_TWO_BRANCH_REVIEW_2026-08-06.md"


class ArcherT3TwoBranchCanonTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.authority = AUTHORITY.read_text(encoding="utf-8")
        cls.review = REVIEW.read_text(encoding="utf-8")

    def test_decision_and_sheet_authority_are_explicit(self) -> None:
        self.assertIn(
            "decision_id: OMW-DEC-20260806-PLANNING-UNIT-BUILDING-TIER-MATRIX-V1",
            self.authority,
        )
        self.assertIn("UNIT_MATRIX_SHEET = 42_병종_Tier_등급", self.authority)
        self.assertIn("BUILDING_MATRIX_SHEET = 43_건물_Tier_효과", self.authority)

    def test_archer_t3_has_exactly_two_current_branches(self) -> None:
        self.assertIn(
            "ARCHER_T3_BRANCHES\n= CROSSBOW_ARCHER / RAPID_FIRE_ARCHER",
            self.authority,
        )
        self.assertIn(
            "ANTI_AIR_ARCHER_T3\n= SUPERSEDED / REMOVED / IMPLEMENTATION_INPUT_FORBIDDEN",
            self.authority,
        )
        self.assertNotIn("= CROSSBOW_ARCHER / ANTI_AIR_ARCHER", self.authority)

    def test_removed_branch_cannot_reenter_product_surfaces(self) -> None:
        required_markers = (
            "T3_ANTI_AIR_ARCHER_BUILDING_BRANCH = FORBIDDEN",
            "T3_ANTI_AIR_ARCHER_AUTO_PRODUCTION = FORBIDDEN",
            "T3_ANTI_AIR_ARCHER_TOKEN_SOURCE = FORBIDDEN",
            "T3_ANTI_AIR_ARCHER_REWARD_CANDIDATE = FORBIDDEN",
            "T3_ANTI_AIR_ARCHER_UNIT_ID = FORBIDDEN",
        )
        for marker in required_markers:
            with self.subTest(marker=marker):
                self.assertIn(marker, self.authority)

    def test_t2_archer_keeps_basic_flying_response(self) -> None:
        self.assertIn("비행 적 우선 타기팅", self.authority)
        self.assertIn("ARCHER_T3_REQUIRED_FOR_BASIC_ANTI_AIR\n= FALSE", self.authority)
        self.assertIn("FLYING_PRIMARY_UNIT_PATHS\n= T2 궁병 / 비행병", self.authority)

    def test_grade_skills_and_named_hero_are_retained(self) -> None:
        for marker in (
            "ARCHER_ELITE",
            "ARCHER_HERO_SKILL",
            "ARCHER_LEGENDARY_SKILL",
            "ARCHER_INITIAL_NAMED_HERO\n= 1",
            "UNIQUE_SKILL_2\n= RETAINED",
        ):
            with self.subTest(marker=marker):
                self.assertIn(marker, self.authority)

    def test_legacy_conflict_and_adversarial_gates_are_documented(self) -> None:
        for legacy_path in (
            "APPROVED_PLAYER_TEN_UNIT_LINEAGES_POC_V1.md",
            "APPROVED_BARRACKS_TIER3_EVOLUTION_AND_GRADE_SKILLS.md",
            "APPROVED_BARRACKS_TIER2_TIER3_INTEGRATED_TREE_V2.md",
        ):
            with self.subTest(legacy_path=legacy_path):
                self.assertIn(legacy_path, self.authority)
        self.assertIn("STOP_SHIP", self.review)
        self.assertIn("대공궁병을 현재 T3 후보·TokenSource·보상·유닛 ID에서 제거", self.review)

    def test_product_and_numeric_boundaries_remain_closed(self) -> None:
        for marker in (
            "PRODUCT_CODE = UNCHANGED",
            "SCENE_RESOURCE_DATA = UNCHANGED",
            "EXACT_NUMERICS = PENDING_SIMULATION",
            "SIMULATION = NOT_RUN",
            "RUNTIME = NOT_RUN",
            "HUMAN_QA = NOT_RUN",
        ):
            with self.subTest(marker=marker):
                self.assertIn(marker, self.authority)


if __name__ == "__main__":
    unittest.main()
