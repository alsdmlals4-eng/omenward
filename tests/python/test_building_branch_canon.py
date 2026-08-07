from __future__ import annotations

import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[2]
LEGACY_DECISION_ID = "OMW-DEC-20260805-PLANNING-SIX-BUILDING-T2-T3-BRANCHES-AND-COUNTERS-V1"
CURRENT_DECISION_ID = "OMW-DEC-20260806-PLANNING-BUILDING-TIER-REALIGNMENT-V1"
SPEC = ROOT / "docs/superpowers/specs/2026-08-05-six-building-t2-t3-branches-design.md"
LEGACY_CANON = ROOT / "docs/design/APPROVED_OMENWARD_SIX_BUILDING_T2_T3_BRANCHES_AND_COUNTERS_2026-08-05.md"
CURRENT_CANON = ROOT / "docs/design/APPROVED_OMENWARD_BUILDING_TIER_REALIGNMENT_2026-08-06.md"
REVIEW = ROOT / "docs/reviews/ADVERSARIAL_BUILDING_BRANCH_COUNTER_AND_OPPORTUNITY_COST_REVIEW_2026-08-05.md"
PROCESS_TOMBSTONE = ROOT / "docs/process/APPROVED_BENCHMARK_TDD_AND_APPROVAL_BATCH_POLICY_2026-08-05.md"
LIFECYCLE = ROOT / "docs/DOCUMENT_LIFECYCLE_REGISTRY.md"
ROADMAP = ROOT / "docs/OMENWARD_ROADMAP.md"

CURRENT_BUILDINGS = ("금고", "농장", "일반병 병영", "특수병 병영", "방어탑", "지휘소", "마력탑")
LOCAL_COMMON_POLICY_MARKERS = (
    "BENCHMARK_REQUIRED",
    "INDUSTRY_COMPARISON_REQUIRED",
    "MAX_APPROVAL_BATCH: 10",
    "TDD_MANDATORY",
    "EXPLICIT_BRANCH_REQUIRED_FOR_GITHUB_MUTATION",
    "DIRECT_MAIN_WRITE: FORBIDDEN",
)
LINEAGE_FILES = (LIFECYCLE, ROADMAP)


def read(path: pathlib.Path) -> str:
    return path.read_text(encoding="utf-8")


class BuildingBranchCanonTests(unittest.TestCase):
    def test_building_authority_and_lineage_files_exist(self) -> None:
        for path in (SPEC, LEGACY_CANON, CURRENT_CANON, REVIEW, PROCESS_TOMBSTONE, LIFECYCLE):
            self.assertTrue(path.is_file(), f"missing authority file: {path.relative_to(ROOT)}")

    def test_legacy_universal_branch_document_is_superseded(self) -> None:
        text = read(LEGACY_CANON)
        for marker in (
            "# [대체됨]",
            LEGACY_DECISION_ID,
            "SUPERSEDED / HISTORICAL_EVIDENCE_ONLY / IMPLEMENTATION_INPUT_FORBIDDEN",
            CURRENT_DECISION_ID,
            "APPROVED_OMENWARD_BUILDING_TIER_REALIGNMENT_2026-08-06.md",
            "모든 6종 건물 공통 A/B 분기 = 사용 금지",
        ):
            self.assertIn(marker, text)

    def test_current_building_tier_structure_is_explicit(self) -> None:
        text = read(CURRENT_CANON)
        self.assertIn("# [현행]", text)
        self.assertIn(CURRENT_DECISION_ID, text)
        for building in CURRENT_BUILDINGS:
            self.assertIn(building, text)
        for marker in (
            "FOUNDATION_REQUIRED_T1_COUNT = 6",
            "SPECIAL_BARRACKS_STAGE1_REQUIRED = FALSE",
            "GENERAL_T2_AUTO_PRODUCTION = SELECTED_GENERAL_UNIT",
            "SPECIAL_T2_AUTO_PRODUCTION = SELECTED_SPECIAL_UNIT",
            "LINEAR_TIER_BUILDINGS = VAULT / FARM / COMMAND_POST / MANA_TOWER",
            "LINEAR_T2_BRANCHING = FORBIDDEN",
        ):
            self.assertIn(marker, text)

    def test_current_building_safety_boundaries_are_explicit(self) -> None:
        text = read(CURRENT_CANON)
        for marker in (
            "UNIVERSAL_AB_BRANCH_GRAMMAR = FORBIDDEN",
            "UNAPPROVED_LINEAR_BUILDING_BRANCH = FORBIDDEN",
            "PREMATURE_T3_FIXATION = FORBIDDEN",
            "PRODUCT_CODE = UNCHANGED",
            "EXACT_NUMERICS = PENDING_SIMULATION",
            "SIMULATION = NOT_RUN",
            "RUNTIME = NOT_RUN",
            "HUMAN_QA = NOT_RUN",
        ):
            self.assertIn(marker, text)

    def test_common_process_authority_is_base_only(self) -> None:
        tombstone = read(PROCESS_TOMBSTONE)
        self.assertIn("SUPERSEDED_BY_BASE_COMMON_AUTHORITY", tombstone)
        self.assertIn("alsdmlals4-eng/Base/AGENTS.md", tombstone)
        self.assertIn("HISTORICAL_PATH_POINTER_ONLY", tombstone)
        self.assertIn("implementation_input: FORBIDDEN", tombstone)
        for marker in LOCAL_COMMON_POLICY_MARKERS:
            self.assertNotIn(marker, tombstone)
            self.assertNotIn(marker, read(ROOT / "README.md"))
            self.assertNotIn(marker, read(ROOT / "AGENTS.md"))

    def test_lineage_routes_decision_three_of_ten_without_reactivating_it(self) -> None:
        for path in LINEAGE_FILES:
            text = read(path)
            self.assertIn(LEGACY_DECISION_ID, text, str(path.relative_to(ROOT)))
            self.assertIn("3_OF_10", text, str(path.relative_to(ROOT)))
        lifecycle = read(LIFECYCLE)
        self.assertIn("LEGACY_UNIVERSAL_BUILDING_BRANCHES", lifecycle)
        self.assertIn("SUPERSEDED_BY_BUILDING_TIER_REALIGNMENT", lifecycle)
        self.assertIn(CURRENT_DECISION_ID, lifecycle)

    def test_review_preserves_historical_risk_evidence_without_authorizing_product(self) -> None:
        text = read(REVIEW)
        for marker in (
            "OMW-AUD-398",
            "OMW-AUD-419",
            "DOMINANT_BRANCH_RISK",
            "FALSE_CHOICE_RISK",
            "COMPLEXITY_BUDGET_RISK",
            "PRESSURE_COVERAGE_GAP",
            "PRODUCT_CODE = UNCHANGED",
            "IMPLEMENTATION_READINESS = BLOCKED_BY_TROOP_AND_TACTICAL_DECISIONS",
        ):
            self.assertIn(marker, text)


if __name__ == "__main__":
    unittest.main()
