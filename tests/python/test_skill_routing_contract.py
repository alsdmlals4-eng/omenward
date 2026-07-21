from __future__ import annotations

import pathlib
import sys
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools"))

from route_skills import load_registry, route  # noqa: E402

REGISTRY = load_registry(ROOT / "docs" / "base" / "SKILL_REGISTRY.json")


def ids(result: dict) -> list[str]:
    return [item["id"] for item in result["skills"]]


class SkillRoutingTests(unittest.TestCase):
    def test_review_forces_adversarial_stack(self) -> None:
        result = route("PR의 누락과 중복을 적대적으로 검토하고 레드팀 검증해줘", REGISTRY)
        selected = ids(result)
        self.assertEqual(result["mode"], "REVIEW")
        self.assertIn("foundation.project-intake", selected)
        self.assertIn("foundation.validation-review", selected)
        self.assertIn("discipline.integration-review", selected)
        self.assertEqual(len(selected), len(set(selected)))

    def test_game_design_plan(self) -> None:
        result = route("룰렛 확률과 보상 규칙을 기획해줘", REGISTRY)
        self.assertEqual(result["mode"], "PLAN")
        self.assertIn("discipline.game-design", ids(result))

    def test_engineering_build(self) -> None:
        result = route("Godot GDScript 성능 버그를 수정해줘", REGISTRY)
        self.assertEqual(result["mode"], "BUILD")
        self.assertIn("discipline.engineering", ids(result))

    def test_ui_art_audit_selects_specialist(self) -> None:
        result = route("HUD UI 아트의 화면 가독성을 시각 감사해줘", REGISTRY)
        selected = ids(result)
        self.assertEqual(result["mode"], "REVIEW")
        self.assertIn("specialist.ui-art-audit", selected)
        self.assertTrue({"discipline.ux-ui-accessibility", "discipline.art"} & set(selected))

    def test_dependencies_precede_dependents(self) -> None:
        result = route("수직 슬라이스 MVP를 설계해줘", REGISTRY)
        selected = ids(result)
        specialist_index = selected.index("specialist.vertical-slice")
        for dependency in ("discipline.game-design", "discipline.engineering", "discipline.production-pm"):
            self.assertLess(selected.index(dependency), specialist_index)

    def test_generic_request_does_not_enable_specialists(self) -> None:
        result = route("프로젝트 작업을 정리해줘", REGISTRY)
        self.assertFalse(any(skill_id.startswith("specialist.") for skill_id in ids(result)))

    def test_unknown_manual_override_is_rejected(self) -> None:
        with self.assertRaises(ValueError):
            route("검토", REGISTRY, forced_skills=["specialist.does-not-exist"])


if __name__ == "__main__":
    unittest.main()
