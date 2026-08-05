from __future__ import annotations

import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[2]
DECISION_ID = "OMW-DEC-20260805-PLANNING-TROOP-ROLES-SYNERGIES-AND-COUNTERS-V1"
SPEC = ROOT / "docs/superpowers/specs/2026-08-05-troop-roles-synergies-counters-design.md"
CANON = ROOT / "docs/design/APPROVED_OMENWARD_TROOP_ROLES_SYNERGIES_AND_COUNTERS_2026-08-05.md"
REVIEW = ROOT / "docs/reviews/ADVERSARIAL_TROOP_ROLE_SYNERGY_AND_COUNTER_REVIEW_2026-08-05.md"

TROOPS = (
    "방패수호병",
    "대검병",
    "창병",
    "궁수",
    "마도사",
    "사제",
    "암살자",
    "기병",
    "비행병",
    "거인",
)
PRESSURES = ("MASS", "ARMORED", "FLYING", "INFILTRATION", "SIEGE")
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


class TroopRoleCanonTests(unittest.TestCase):
    def test_authority_files_exist(self) -> None:
        for path in (SPEC, CANON, REVIEW):
            self.assertTrue(path.is_file(), f"missing authority file: {path.relative_to(ROOT)}")

    def test_roster_baseline_and_resize_gate_are_explicit(self) -> None:
        text = read(CANON)
        self.assertIn(DECISION_ID, text)
        self.assertIn("ROSTER_BASELINE: 10", text)
        self.assertIn("ROSTER_COUNT_IS_NOT_SACRED", text)
        self.assertIn("ROSTER_MIN_MAX: NOT_PRESET", text)
        self.assertIn("ADD_UNIT_ONLY_IF", text)
        self.assertIn("REMOVE_OR_REPLACE_IF", text)
        for troop in TROOPS:
            self.assertIn(troop, text)

    def test_five_pressures_have_multiple_troop_paths(self) -> None:
        text = read(CANON)
        for pressure in PRESSURES:
            self.assertIn(pressure, text)
        self.assertIn("압력별 최소 두 병종 대응 경로", text)
        self.assertIn("단일 하드키 병종 금지", text)

    def test_synergy_and_barracks_rules_preserve_flexible_composition(self) -> None:
        text = read(CANON)
        for marker in (
            "행동 기반 시너지",
            "단순 세트 보너스: FORBIDDEN",
            "전열 병영 가중 계열",
            "기동 병영 가중 계열",
            "공통 지원 계열",
            "반대 계열 영구 삭제: FORBIDDEN",
        ):
            self.assertIn(marker, text)

    def test_tier_route_layer_and_asset_boundaries_are_explicit(self) -> None:
        text = read(CANON)
        for marker in (
            "T1 병종 토큰 = 실제 T1 인게임 이미지",
            "T2 병종 토큰 = 실제 T2 인게임 이미지",
            "T3 병종 토큰 = FORBIDDEN",
            "FREE_RECALL: FORBIDDEN",
            "FREE_CROSS_LANE_MOVE: FORBIDDEN",
            "EXACT_NUMERICS: PENDING_SIMULATION",
            "PRODUCT_CODE = UNCHANGED",
        ):
            self.assertIn(marker, text)

    def test_central_authority_routes_decision_four_of_ten(self) -> None:
        for path in CENTRAL_FILES:
            text = read(path)
            self.assertIn(DECISION_ID, text, str(path.relative_to(ROOT)))
            self.assertIn("4_OF_10", text, str(path.relative_to(ROOT)))

    def test_legacy_prototype_unit_data_is_not_current_product_authority(self) -> None:
        text = read(ROOT / "docs/DOCUMENT_LIFECYCLE_REGISTRY.md")
        self.assertIn("data/units/*.tres", text)
        self.assertIn("[증거]", text)
        self.assertIn("LEGACY_PROTOTYPE_UNIT_DATA", text)
        self.assertIn("IMPLEMENTATION_INPUT_FORBIDDEN", text)

    def test_adversarial_review_closes_known_risks_without_authorizing_product(self) -> None:
        text = read(REVIEW)
        for marker in (
            "OMW-AUD-420",
            "OMW-AUD-443",
            "ROLE_OVERLAP_RISK",
            "HARD_COUNTER_LOCK_RISK",
            "FORCED_COMPOSITION_RISK",
            "ROSTER_BLOAT_RISK",
            "PRODUCT_CODE = UNCHANGED",
            "IMPLEMENTATION_READINESS = BLOCKED_BY_TACTICAL_AND_NUMERIC_DECISIONS",
        ):
            self.assertIn(marker, text)


if __name__ == "__main__":
    unittest.main()
