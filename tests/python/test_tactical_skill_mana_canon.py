from __future__ import annotations

import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[2]
DECISION_ID = "OMW-DEC-20260805-PLANNING-TACTICAL-SKILLS-AND-MANA-V1"
SPEC = ROOT / "docs/superpowers/specs/2026-08-05-tactical-skills-and-mana-design.md"
PLAN = ROOT / "docs/superpowers/plans/2026-08-05-tactical-skills-and-mana.md"
CANON = ROOT / "docs/design/APPROVED_OMENWARD_TACTICAL_SKILLS_AND_MANA_2026-08-05.md"
REVIEW = ROOT / "docs/reviews/ADVERSARIAL_TACTICAL_SKILLS_MANA_AND_RESEARCH_REVIEW_2026-08-05.md"
LIFECYCLE = ROOT / "docs/DOCUMENT_LIFECYCLE_REGISTRY.md"
ROADMAP = ROOT / "docs/OMENWARD_ROADMAP.md"
CURRENT_GDD = ROOT / "docs/OMENWARD_GDD_CURRENT_CANON.md"

TACTICAL_SKILLS = (
    "속박진",
    "수호장",
    "집중 명령",
    "충격파",
    "폭풍 억제",
    "파쇄 명령",
    "봉쇄 결계",
    "결전의 깃발",
    "성역",
    "시간 왜곡",
)

CENTRAL_FILES = (
    ROOT / "README.md",
    ROOT / "AGENTS.md",
    ROOT / "docs/PROJECT_CORE.md",
    ROOT / "docs/ACTIVE_CONTEXT.md",
    ROOT / "docs/DOCUMENTATION_MAP.md",
    LIFECYCLE,
    CURRENT_GDD,
    ROOT / "docs/DECISIONS_PENDING.md",
    ROADMAP,
    ROOT / "docs/CURRENT_IMPLEMENTATION_STATUS.md",
    ROOT / "docs/HANDOFF_CONTEXT.md",
    ROOT / "docs/PROJECT_CANON_DECISION_LEDGER.md",
    ROOT / "docs/PROJECT_GOOGLE_SHEET_WORKBOOK.md",
)
MANA_AUTHORITY_FILES = (CANON, LIFECYCLE, CURRENT_GDD)
LINEAGE_FILES = (LIFECYCLE, ROADMAP)


def read(path: pathlib.Path) -> str:
    return path.read_text(encoding="utf-8")


class TacticalSkillManaCanonTests(unittest.TestCase):
    def test_authority_files_exist(self) -> None:
        for path in (SPEC, PLAN, CANON, REVIEW, LIFECYCLE, CURRENT_GDD):
            self.assertTrue(path.is_file(), f"missing authority file: {path.relative_to(ROOT)}")

    def test_mana_tower_is_single_linear_research_authority(self) -> None:
        text = read(CANON)
        for marker in (
            DECISION_ID,
            "MANA_TOWER_MAX_ACTIVE_INSTANCES = 1",
            "BRANCHING = FORBIDDEN",
            "마력탑 T1 → T2 → T3",
            "ONE_CONCURRENT_RESEARCH",
            "연구 비용 = 골드 + 연구 시간",
            "시전 비용 = 마력",
        ):
            self.assertIn(marker, text)

    def test_tactical_roster_is_exactly_four_three_three(self) -> None:
        text = read(CANON)
        for marker in (
            "TOTAL_TACTICAL_SKILLS = 10",
            "T1 = 4",
            "T2 = 3",
            "T3 = 3",
        ):
            self.assertIn(marker, text)
        for skill in TACTICAL_SKILLS:
            self.assertIn(skill, text)

    def test_unlock_cast_and_reset_rules_are_explicit(self) -> None:
        text = read(CANON)
        for marker in (
            "STAGE_LOADOUT = NONE",
            "AUTO_CAST = FORBIDDEN",
            "RESEARCH_USES_MANA = FORBIDDEN",
            "INVALID_CAST_SPENDS_MANA = FALSE",
            "UNLOCK_SCOPE = CURRENT_MAPRUN",
            "RESET_SCOPE = NEW_MAPRUN",
            "STAGE_TRANSITION_RESET = FALSE",
        ):
            self.assertIn(marker, text)

    def test_five_pressures_keep_multiple_layers_of_answers(self) -> None:
        text = read(CANON)
        for pressure in ("MASS", "ARMORED", "FLYING", "INFILTRATION", "SIEGE"):
            self.assertIn(pressure, text)
        self.assertIn("각 압력은 병종·건물·전술 중 최소 두 계층의 대응 경로", text)
        self.assertIn("전술스킬은 병종·건물의 지속 역할을 대체하지 않는다", text)

    def test_current_authority_rejects_legacy_masok_and_routes_mana(self) -> None:
        for path in CENTRAL_FILES:
            self.assertNotIn("마석", read(path), str(path.relative_to(ROOT)))
        for path in MANA_AUTHORITY_FILES:
            self.assertIn("마력", read(path), str(path.relative_to(ROOT)))

    def test_legacy_building_branch_and_term_are_superseded_by_precedence(self) -> None:
        canon = read(CANON)
        lifecycle = read(LIFECYCLE)
        for marker in (
            "[대체됨] 유량 마력탑 → 맥동 도관",
            "[대체됨] 저장 마력탑 → 징조 저장고",
            DECISION_ID,
        ):
            self.assertIn(marker, canon)
        for marker in (
            "LEGACY_MANA_TOWER_BRANCHES",
            "LEGACY_TERM_MASOK",
            "IMPLEMENTATION_INPUT_FORBIDDEN",
            DECISION_ID,
        ):
            self.assertIn(marker, lifecycle)

    def test_lineage_routes_decision_five_of_ten(self) -> None:
        for path in LINEAGE_FILES:
            text = read(path)
            self.assertIn(DECISION_ID, text, str(path.relative_to(ROOT)))
            self.assertIn("5_OF_10", text, str(path.relative_to(ROOT)))

    def test_adversarial_review_closes_known_risks_without_authorizing_product(self) -> None:
        text = read(REVIEW)
        for marker in (
            "OMW-AUD-444",
            "OMW-AUD-467",
            "RESOURCE_HOARDING_DOMINANCE",
            "RESEARCH_SNOWBALL",
            "SINGLE_TOWER_LOCKOUT",
            "T3_PANIC_BUTTON_DOMINANCE",
            "LEGACY_MASOK_TERM_LEAK",
            "PRODUCT_CODE = UNCHANGED",
            "EXACT_NUMERICS = PENDING_SIMULATION",
        ):
            self.assertIn(marker, text)

    def test_product_and_numeric_boundaries_remain_closed(self) -> None:
        text = read(CANON)
        for marker in (
            "PRODUCT_CODE = UNCHANGED",
            "DATA_MIGRATION = NOT_AUTHORIZED",
            "EXACT_NUMERICS = PENDING_SIMULATION",
            "SIMULATION = NOT_RUN",
            "RUNTIME = NOT_RUN",
            "HUMAN_QA = NOT_RUN",
        ):
            self.assertIn(marker, text)


if __name__ == "__main__":
    unittest.main()
