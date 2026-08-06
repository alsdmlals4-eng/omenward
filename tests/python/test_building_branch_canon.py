from __future__ import annotations

import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[2]
DECISION_ID = "OMW-DEC-20260805-PLANNING-SIX-BUILDING-T2-T3-BRANCHES-AND-COUNTERS-V1"
SPEC = ROOT / "docs/superpowers/specs/2026-08-05-six-building-t2-t3-branches-design.md"
CANON = ROOT / "docs/design/APPROVED_OMENWARD_SIX_BUILDING_T2_T3_BRANCHES_AND_COUNTERS_2026-08-05.md"
REVIEW = ROOT / "docs/reviews/ADVERSARIAL_BUILDING_BRANCH_COUNTER_AND_OPPORTUNITY_COST_REVIEW_2026-08-05.md"
PROCESS_TOMBSTONE = ROOT / "docs/process/APPROVED_BENCHMARK_TDD_AND_APPROVAL_BATCH_POLICY_2026-08-05.md"

BUILDINGS = ("금고", "농장", "병영", "방어탑", "지휘소", "마력탑")
PRESSURES = ("MASS", "ARMORED", "FLYING", "INFILTRATION", "SIEGE")
LOCAL_COMMON_POLICY_MARKERS = (
    "BENCHMARK_REQUIRED",
    "INDUSTRY_COMPARISON_REQUIRED",
    "MAX_APPROVAL_BATCH: 10",
    "TDD_MANDATORY",
    "EXPLICIT_BRANCH_REQUIRED_FOR_GITHUB_MUTATION",
    "DIRECT_MAIN_WRITE: FORBIDDEN",
)
CENTRAL_FILES = (
    ROOT / "README.md",
    ROOT / "AGENTS.md",
    ROOT / "docs/PROJECT_CORE.md",
    ROOT / "docs/ACTIVE_CONTEXT.md",
    ROOT / "docs/DOCUMENTATION_MAP.md",
    ROOT / "docs/DOCUMENT_LIFECYCLE_REGISTRY.md",
    ROOT / "docs/OMENWARD_GDD_CURRENT_CANON.md",
    ROOT / "docs/DECISIONS_PENDING.md",
    ROOT / "docs/OMENWARD_ROADMAP.md",
)


def read(path: pathlib.Path) -> str:
    return path.read_text(encoding="utf-8")


class BuildingBranchCanonTests(unittest.TestCase):
    def test_building_branch_authority_files_exist(self) -> None:
        for path in (SPEC, CANON, REVIEW):
            self.assertTrue(path.is_file(), f"missing authority file: {path.relative_to(ROOT)}")

    def test_common_branch_grammar_and_tradeoffs_are_explicit(self) -> None:
        text = read(CANON)
        self.assertIn(DECISION_ID, text)
        self.assertIn("T1 → T2 A → T3 A", text)
        self.assertIn("T1 → T2 B → T3 B", text)
        self.assertIn("CROSS_BRANCH: FORBIDDEN", text)
        self.assertIn("DUAL_T3: FORBIDDEN", text)
        self.assertIn("MAPRUN_PERMANENT_CHOICE", text)
        self.assertGreaterEqual(text.count("얻는 것"), 12)
        self.assertGreaterEqual(text.count("포기하는 것"), 12)
        self.assertGreaterEqual(text.count("T3 —"), 12)

    def test_all_six_buildings_and_five_pressures_are_covered(self) -> None:
        text = read(CANON)
        for building in BUILDINGS:
            self.assertIn(building, text)
        for pressure in PRESSURES:
            self.assertIn(pressure, text)
        self.assertIn("압력별 최소 두 대응 경로", text)
        self.assertIn("단일 만능 분기 금지", text)

    def test_failure_boundaries_preserve_current_core(self) -> None:
        text = read(CANON)
        for marker in (
            "정확 수치: PENDING_SIMULATION",
            "FREE_RECALL: FORBIDDEN",
            "FREE_CROSS_LANE_MOVE: FORBIDDEN",
            "AUTO_TACTICAL_CAST: FORBIDDEN",
            "INFINITE_GOLD_OR_MANA: FORBIDDEN",
            "T3_ROULETTE_TOKEN: FORBIDDEN",
            "HIDDEN_COUNTER_CHANGE: FORBIDDEN",
        ):
            self.assertIn(marker, text)

    def test_common_process_authority_is_base_only(self) -> None:
        self.assertTrue(PROCESS_TOMBSTONE.is_file())
        tombstone = read(PROCESS_TOMBSTONE)
        self.assertIn("SUPERSEDED_BY_BASE_COMMON_AUTHORITY", tombstone)
        self.assertIn("alsdmlals4-eng/Base/AGENTS.md", tombstone)
        self.assertIn("HISTORICAL_PATH_POINTER_ONLY", tombstone)
        self.assertIn("IMPLEMENTATION_INPUT: FORBIDDEN", tombstone)
        for marker in LOCAL_COMMON_POLICY_MARKERS:
            self.assertNotIn(marker, tombstone)
            self.assertNotIn(marker, read(ROOT / "README.md"))
            self.assertNotIn(marker, read(ROOT / "AGENTS.md"))

    def test_central_authority_routes_decision_three_of_ten(self) -> None:
        for path in CENTRAL_FILES:
            text = read(path)
            self.assertIn(DECISION_ID, text, str(path.relative_to(ROOT)))
            self.assertIn("3_OF_10", text, str(path.relative_to(ROOT)))

    def test_review_closes_known_design_risks_without_authorizing_product(self) -> None:
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
