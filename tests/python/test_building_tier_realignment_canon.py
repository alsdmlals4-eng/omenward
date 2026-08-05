from __future__ import annotations

import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[2]
DECISION_ID = "OMW-DEC-20260806-PLANNING-BUILDING-TIER-REALIGNMENT-V1"
PARENT_DECISION_ID = "OMW-DEC-20260805-PLANNING-FIRST-10-15-MINUTES-FLOW-V1"
SPEC = ROOT / "docs/superpowers/specs/2026-08-06-building-tier-realignment-design.md"
PLAN = ROOT / "docs/superpowers/plans/2026-08-06-building-tier-realignment.md"
CANON = ROOT / "docs/design/APPROVED_OMENWARD_BUILDING_TIER_REALIGNMENT_2026-08-06.md"
REVIEW = ROOT / "docs/reviews/ADVERSARIAL_BUILDING_TIER_REALIGNMENT_REVIEW_2026-08-06.md"
OLD_CANON = ROOT / "docs/design/APPROVED_OMENWARD_SIX_BUILDING_T2_T3_BRANCHES_AND_COUNTERS_2026-08-05.md"
ONBOARDING = ROOT / "docs/design/APPROVED_OMENWARD_FIRST_10_15_MINUTES_FLOW_2026-08-05.md"

CENTRAL_FILES = (
    ROOT / "docs/ACTIVE_CONTEXT.md",
    ROOT / "docs/DOCUMENTATION_MAP.md",
    ROOT / "docs/DOCUMENT_LIFECYCLE_REGISTRY.md",
    ROOT / "docs/PROJECT_CANON_DECISION_LEDGER.md",
    ROOT / "docs/OMENWARD_GDD_CURRENT_CANON.md",
    ROOT / "docs/DECISIONS_PENDING.md",
    ROOT / "docs/HANDOFF_CONTEXT.md",
    ROOT / "docs/PROJECT_GOOGLE_SHEET_WORKBOOK.md",
)

GENERAL_T2 = ("방패병", "대검병", "창병", "궁병", "기병")
SPECIAL_T2 = ("마도사", "사제", "암살자", "비행병", "거인")
LINEAR_BUILDINGS = ("금고", "농장", "지휘소", "마력탑")


def read(path: pathlib.Path) -> str:
    return path.read_text(encoding="utf-8")


class BuildingTierRealignmentCanonTests(unittest.TestCase):
    def test_authority_files_exist(self) -> None:
        for path in (SPEC, PLAN, CANON, REVIEW, OLD_CANON, ONBOARDING):
            self.assertTrue(path.is_file(), f"missing authority file: {path.relative_to(ROOT)}")

    def test_general_barracks_auto_production_and_token_source_are_explicit(self) -> None:
        text = read(CANON)
        self.assertIn(DECISION_ID, text)
        self.assertIn("GENERAL_T1_AUTO_PRODUCTION = BASIC_INFANTRY", text)
        self.assertIn("GENERAL_T1_TOKEN_SOURCE = BASIC_INFANTRY", text)
        self.assertIn("GENERAL_T2_AUTO_PRODUCTION = SELECTED_GENERAL_UNIT", text)
        self.assertIn("GENERAL_T2_TOKEN_SOURCE = SELECTED_GENERAL_UNIT", text)
        for unit in GENERAL_T2:
            self.assertIn(unit, text)

    def test_special_t1_has_random_auto_production_and_no_token_source(self) -> None:
        text = read(CANON)
        self.assertIn("SPECIAL_T1_AUTO_PRODUCTION = RANDOM_SPECIAL_UNIT", text)
        self.assertIn("SPECIAL_T1_TOKEN_SOURCE = NONE", text)
        self.assertIn("SPECIAL_T2_AUTO_PRODUCTION = SELECTED_SPECIAL_UNIT", text)
        self.assertIn("SPECIAL_T2_TOKEN_SOURCE = SELECTED_SPECIAL_UNIT", text)
        self.assertIn("SPECIAL_AUTO_PRODUCTION_INTERVAL = LONGER_THAN_GENERAL_UNIT", text)
        self.assertIn("SPECIAL_UNIT_FUNCTIONAL_POWER = STRONGER_THAN_GENERAL_UNIT", text)
        for unit in SPECIAL_T2:
            self.assertIn(unit, text)

    def test_defense_tower_has_three_distinct_t2_roles(self) -> None:
        text = read(CANON)
        for marker in (
            "T2 포격탑",
            "범위 공격",
            "T2 방어탑(방어 강화형)",
            "방어력·내구",
            "T2 저격탑",
            "긴 사거리",
        ):
            self.assertIn(marker, text)

    def test_vault_farm_command_and_mana_are_linear(self) -> None:
        text = read(CANON)
        self.assertIn("LINEAR_TIER_BUILDINGS = VAULT / FARM / COMMAND_POST / MANA_TOWER", text)
        self.assertIn("LINEAR_T2_BRANCHING = FORBIDDEN", text)
        for building in LINEAR_BUILDINGS:
            self.assertIn(f"{building} T1 → T2 → T3", text)

    def test_stage_one_keeps_six_required_foundation_buildings(self) -> None:
        text = read(ONBOARDING)
        self.assertIn(PARENT_DECISION_ID, text)
        self.assertIn("PARTIAL_APPROVAL_6_OF_10", text)
        self.assertIn("일반병 병영", text)
        self.assertIn("SPECIAL_BARRACKS_STAGE1_REQUIRED = FALSE", text)
        self.assertIn("FIRST_STAGE2_T2_CANDIDATES = PENDING_GRILLME", text)

    def test_old_universal_branch_canon_is_implementation_forbidden(self) -> None:
        text = read(OLD_CANON)
        self.assertIn("SUPERSEDED", text)
        self.assertIn("IMPLEMENTATION_INPUT_FORBIDDEN", text)
        self.assertIn(DECISION_ID, text)
        for rejected in (
            "안정 금고 / 행운 금고",
            "징집 농장 / 예비 농장",
            "전열 병영 / 기동 병영",
            "연사탑 / 포격탑",
            "돌격 지휘소 / 수비 지휘소",
        ):
            self.assertIn(rejected, text)

    def test_central_files_route_checkpoint_six(self) -> None:
        for path in CENTRAL_FILES:
            text = read(path)
            self.assertIn(DECISION_ID, text, str(path.relative_to(ROOT)))
            self.assertIn("PARTIAL_APPROVAL_6_OF_10", text, str(path.relative_to(ROOT)))

    def test_review_covers_known_failure_modes(self) -> None:
        text = read(REVIEW)
        for marker in (
            "SPECIAL_T1_TOKEN_LEAK",
            "SPECIAL_DOUBLE_ADVANTAGE",
            "AUTO_PRODUCTION_TOKEN_SOURCE_CONFLATION",
            "DEFENSE_BRANCH_ROLE_OVERLAP",
            "OLD_CANON_AUTHORITY_LEAK",
            "STAGE1_SEVEN_BUILDING_OVERLOAD",
            "PREMATURE_T3_AND_NUMERIC_FIXATION",
            "PRODUCT_CODE = UNCHANGED",
        ):
            self.assertIn(marker, text)

    def test_product_and_numeric_boundaries_remain_fail_closed(self) -> None:
        text = read(CANON)
        for marker in (
            "PRODUCT_CODE = UNCHANGED",
            "SCENE_RESOURCE_DATA = UNCHANGED",
            "EXACT_NUMERICS = PENDING_SIMULATION",
            "SIMULATION = NOT_RUN",
            "RUNTIME = NOT_RUN",
            "HUMAN_QA = NOT_RUN",
        ):
            self.assertIn(marker, text)


if __name__ == "__main__":
    unittest.main()
