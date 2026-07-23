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
    def test_review_forces_validation_and_freshness_stack(self) -> None:
        result = route("PR의 누락과 중복을 적대적으로 검토하고 레드팀 검증해줘", REGISTRY)
        selected = ids(result)
        self.assertEqual(result["mode"], "REVIEW")
        self.assertIn("foundation.project-intake", selected)
        self.assertIn("foundation.validation-review", selected)
        self.assertIn("specialist.canonical-freshness", selected)
        self.assertNotIn("discipline.integration-review", selected)
        self.assertEqual(len(selected), len(set(selected)))

    def test_game_design_plan_routes_to_omenward_core_design(self) -> None:
        result = route("룰렛 확률과 보상 규칙을 기획해줘", REGISTRY)
        self.assertEqual(result["mode"], "PLAN")
        self.assertIn("discipline.omenward-core-design", ids(result))
        self.assertNotIn("discipline.game-design", ids(result))

    def test_engineering_build_routes_to_omenward_godot(self) -> None:
        result = route("Godot GDScript 성능 버그를 수정해줘", REGISTRY)
        self.assertEqual(result["mode"], "BUILD")
        self.assertIn("discipline.omenward-godot", ids(result))
        self.assertNotIn("discipline.engineering", ids(result))

    def test_ui_art_audit_uses_one_primary_and_one_support_discipline(self) -> None:
        result = route("HUD UI 아트의 화면 가독성을 시각 감사해줘", REGISTRY)
        selected = ids(result)
        self.assertEqual(result["mode"], "REVIEW")
        self.assertIn("discipline.omenward-core-ux", selected)
        self.assertIn("discipline.omenward-art-assets", selected)
        self.assertNotIn("specialist.ui-art-audit", selected)
        active_disciplines = [skill_id for skill_id in selected if skill_id.startswith("discipline.omenward-")]
        self.assertLessEqual(len(active_disciplines), 2)

    def test_dependencies_precede_dependents(self) -> None:
        result = route("HUD 플레이테스트와 실패 원인을 검토해줘", REGISTRY)
        selected = ids(result)
        core_ux_index = selected.index("discipline.omenward-core-ux")
        for dependency in ("foundation.project-intake", "foundation.validation-review"):
            self.assertLess(selected.index(dependency), core_ux_index)

    def test_legacy_manual_alias_resolves_to_active_skill(self) -> None:
        result = route(
            "Godot 변경",
            REGISTRY,
            forced_mode="BUILD",
            forced_skills=["discipline.engineering"],
        )
        selected = ids(result)
        self.assertIn("discipline.omenward-godot", selected)
        self.assertNotIn("discipline.engineering", selected)

    def test_generic_request_does_not_enable_specialists(self) -> None:
        result = route("프로젝트 작업을 정리해줘", REGISTRY)
        self.assertFalse(any(skill_id.startswith("specialist.") for skill_id in ids(result)))

    def test_unknown_manual_override_is_rejected(self) -> None:
        with self.assertRaises(ValueError):
            route("검토", REGISTRY, forced_skills=["specialist.does-not-exist"])


if __name__ == "__main__":
    unittest.main()
