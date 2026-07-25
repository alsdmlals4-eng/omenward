import importlib.util
import json
import pathlib
import sys
import tempfile
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[2]


def load(name: str, path: pathlib.Path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


route = load("route_skills_v4", ROOT / "tools" / "route_skills.py")
validator = load("validate_skill_system_v4", ROOT / "tools" / "validate_skill_system.py")


class RouterTests(unittest.TestCase):
    def registry(self):
        return {
            "routing": {"work_modes": ["PLAN", "BUILD", "REVIEW"], "max_support_disciplines": 1, "review_stack": ["foundation.review"], "always_on": []},
            "aliases": {"discipline.engineering": "discipline.godot"},
            "skills": [
                {"id": "foundation.review", "category": "foundation", "path": "skills/foundation/review/SKILL.md", "triggers": ["검토"], "not_use_when": [], "depends_on": [], "priority": 90, "status": "active", "modes": ["REVIEW"]},
                {"id": "discipline.godot", "category": "disciplines", "path": "skills/disciplines/godot/SKILL.md", "triggers": ["Godot"], "not_use_when": ["문서만"], "depends_on": [], "priority": 80, "status": "active", "modes": ["PLAN", "BUILD", "REVIEW"]},
                {"id": "discipline.old", "category": "disciplines", "path": "skills/disciplines/old/SKILL.md", "triggers": ["Godot"], "not_use_when": [], "depends_on": [], "priority": 100, "status": "inactive", "modes": []},
            ],
        }

    def test_inactive_skill_never_routes(self):
        self.assertEqual([item["id"] for item in route.route("Godot 구현", self.registry())["skills"]], ["discipline.godot"])

    def test_legacy_alias_resolves(self):
        self.assertEqual([item["id"] for item in route.route("작업", self.registry(), forced_skills=["discipline.engineering"])["skills"]], ["discipline.godot"])

    def test_review_stack_is_stage_scoped(self):
        self.assertEqual(route.route("일반 계획", self.registry())["skills"], [])
        self.assertEqual([item["id"] for item in route.route("검토", self.registry())["skills"]], ["foundation.review"])


class ValidatorTests(unittest.TestCase):
    def test_dynamic_count_and_aliases(self):
        with tempfile.TemporaryDirectory() as directory:
            root = pathlib.Path(directory)
            package = root / "skills" / "foundation" / "review" / "SKILL.md"
            package.parent.mkdir(parents=True)
            package.write_text("`foundation.review`\n" + "\n".join(validator.REQ), encoding="utf-8")
            registry = {"schema_version": 4, "routing": {"always_on": [], "review_stack": ["foundation.review"]}, "aliases": {"foundation.old": "foundation.review"}, "skills": [{"id": "foundation.review", "path": "skills/foundation/review/SKILL.md", "status": "active", "depends_on": []}]}
            path = root / "docs" / "base" / "SKILL_REGISTRY.json"
            path.parent.mkdir(parents=True)
            path.write_text(json.dumps(registry), encoding="utf-8")
            self.assertEqual(validator.validate(path, root), [])


class CoreUxPlaytestContractTests(unittest.TestCase):
    def test_human_core_loop_protocol_is_preserved(self):
        skill = (
            ROOT
            / "skills"
            / "disciplines"
            / "evaluating-omenward-core-ux-and-playtests"
            / "SKILL.md"
        ).read_text(encoding="utf-8")
        required = (
            "첫 10분",
            "Session contract",
            "Build and seed",
            "LOOP_PROVEN",
            "UX_GAP",
            "RULE_GAP",
            "CONTENT_GAP",
            "TECHNICAL_BLOCKED",
            "NOT_RUN",
            "자동화 통과를 인간 이해 증거로 대체",
        )
        for value in required:
            with self.subTest(value=value):
                self.assertIn(value, skill)


if __name__ == "__main__":
    unittest.main()
