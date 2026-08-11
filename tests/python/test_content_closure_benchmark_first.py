from __future__ import annotations

from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[2]
PRODUCT = ROOT / "docs/design/APPROVED_OMENWARD_WHOLE_PROJECT_CONTENT_CLOSURE_2026-08-11.md"
PROCESS = ROOT / "docs/process/APPROVED_OMENWARD_BENCHMARK_INDUSTRY_RESEARCH_FIRST_2026-08-11.md"
AGENTS = ROOT / "AGENTS.md"
ACTIVE = ROOT / "docs/ACTIVE_CONTEXT.md"
PENDING = ROOT / "docs/DECISIONS_PENDING.md"
WORKFLOW = ROOT / ".github/workflows/validate-canon-freshness-v4-5.yml"

PRODUCT_DECISION = "OMW-DEC-20260811-PLANNING-WHOLE-PROJECT-CONTENT-CLOSURE-V1"
PROCESS_DECISION = "OMW-DEC-20260811-OPS-BENCHMARK-INDUSTRY-RESEARCH-FIRST-V1"


class ContentClosureBenchmarkFirstTest(unittest.TestCase):
    def test_product_closure_decision_exists_and_has_approved_semantics(self) -> None:
        text = PRODUCT.read_text(encoding="utf-8")
        for marker in (
            PRODUCT_DECISION,
            "BUILDING_T3_GRAMMAR = SINGLE_CAPSTONE_DEEPENS_SELECTED_T2_IDENTITY",
            "BUILDING_T3_REBRANCH = FORBIDDEN",
            "GENERAL_BARRACKS_T3_NEW_TROOP_BRANCH = FORBIDDEN",
            "GENERAL_BARRACKS_T3_NEW_TOKEN_SOURCE_GRAMMAR = FORBIDDEN",
            "ARCHER_T3 = CROSSBOW_ARCHER / RAPID_FIRE_ARCHER",
            "DEFENSE_T2_DISPLAY_NAMES = 포격탑 / 요새탑 / 저격탑",
            "HERO_STRATEGIC_ROLE = CONTEXTUAL_AMPLIFIER",
            "HERO_SELECTION_PER_MAPRUN = 1",
            "HERO_STAGE_BY_STAGE_FREE_SWAP = FORBIDDEN",
            "LEGENDARY_GRAMMAR = RARE_CONSTRAINED_SIDEGRADE",
            "LEGENDARY_PLAIN_RAW_STAT_SUPERIOR_TIER = FORBIDDEN",
            "META_HUB_PROGRESSION = HORIZONTAL_CONTEXTUAL",
            "PERMANENT_PURE_COMBAT_STAT_ACCUMULATION = FORBIDDEN",
            "MANDATORY_GRIND_CURRENCY = FORBIDDEN",
            "HELD_REFERENCE_LINEAGE_NOT_CURRENT_EXACT_IMPLEMENTATION_AUTHORITY",
        ):
            self.assertIn(marker, text)

    def test_genre_classification_is_canonical_and_not_slot_only(self) -> None:
        text = PRODUCT.read_text(encoding="utf-8")
        for marker in (
            "PRIMARY_GENRE = ROGUELITE_STRATEGY_AUTO_BATTLER",
            "MECHANICAL_SUBGENRE = ROULETTE_PROBABILITY_BUILDER",
            "MARKETING_SHORT = 룰렛을 설계해 군대를 만드는 로그라이트 전략 오토배틀러",
            "PURE_SLOT_GAME = AVOID_POSITIONING",
            "PURE_TOWER_DEFENSE = AVOID_POSITIONING",
        ):
            self.assertIn(marker, text)

    def test_benchmark_first_process_is_mandatory(self) -> None:
        text = PROCESS.read_text(encoding="utf-8")
        for marker in (
            PROCESS_DECISION,
            "BENCHMARK_AND_INDUSTRY_RESEARCH_REQUIRED_BEFORE_WORK = TRUE",
            "BENCHMARK_DISPOSITION = ADOPT / ADAPT / AVOID / TEST / IGNORE",
            "FRESH_BASE_PROJECT_SHEET_READ",
            "TARGETED_BENCHMARK_AND_INDUSTRY_RESEARCH",
            "PROJECT_CANON_CONFLICT_CHECK",
            "COMPETITOR_BEHAVIOR_AUTOMATIC_AUTHORITY = FORBIDDEN",
        ):
            self.assertIn(marker, text)

    def test_current_routers_close_semantic_groups_but_keep_phase_c_blocked(self) -> None:
        combined = "\n".join(path.read_text(encoding="utf-8") for path in (AGENTS, ACTIVE, PENDING))
        for marker in (
            "WHOLE_PROJECT_CONTENT_DECISION_GROUPS_OPEN = 0",
            "WHOLE_PROJECT_CONTENT_DECISIONS = CLOSED_PENDING_USER_PLANNING_COMPLETE_DECLARATION",
            "USER_EXPLICIT_PLANNING_COMPLETE_DECLARATION = NOT_RECEIVED",
            "PHASE_B_FINAL_PLANNING_REVIEW = NOT_RUN",
            "PHASE_C_BLOCKED",
            "BENCHMARK_AND_INDUSTRY_RESEARCH_REQUIRED_BEFORE_WORK = TRUE",
            PRODUCT_DECISION,
            PROCESS_DECISION,
        ):
            self.assertIn(marker, combined)

    def test_v45_workflow_executes_focused_contract(self) -> None:
        workflow = WORKFLOW.read_text(encoding="utf-8")
        self.assertIn("tests/python/test_content_closure_benchmark_first.py", workflow)
        self.assertIn("tests.python.test_content_closure_benchmark_first", workflow)


if __name__ == "__main__":
    unittest.main()
