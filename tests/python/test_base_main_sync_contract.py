"""Regression checks for the Omenward sync to the current Base main."""

from __future__ import annotations

import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
HUB = ROOT / "[기획서]" / "00_프로젝트_허브"
BASE_COMMIT = "ee265576da7f67d3278f8099dd97d4e714ef0651"
LEGACY_COMMIT = "d2457e75a856260d309203e20262f2a2142d2dd6"
BASE_SKILLS = [
  "managing-project-intake-and-work-contract",
  "managing-game-project-operating-system",
  "evolving-project-discipline-skills",
  "managing-design-documents",
  "maintaining-project-context-and-handoff",
  "reviewing-and-validating-project-changes",
  "managing-base-change-proposals",
  "analyzing-and-refining-game-concepts",
  "designing-vertical-slices",
  "orchestrating-deepseek-worktrees",
  "auditing-canonical-reference-freshness",
  "designing-art-prompts-and-technique-cards",
  "auditing-and-refining-ui-art"
]
DISCIPLINE_SKILLS = [
  "omenward-narrative",
  "omenward-game-design",
  "omenward-ux-ui-accessibility",
  "omenward-engineering",
  "omenward-technical-art-pipeline",
  "omenward-art",
  "omenward-audio",
  "omenward-qa",
  "omenward-production-pm",
  "omenward-analytics-user-research",
  "omenward-integration-review"
]
FRONT_MATTER_NAME = re.compile(r"\A---\n.*?^name:\s*([^\n]+)\n.*?^---\n", re.MULTILINE | re.DOTALL)


class BaseMainSyncContractTests(unittest.TestCase):
    def load_registry(self) -> dict:
        return json.loads((HUB / "SKILL_REGISTRY.json").read_text(encoding="utf-8"))

    def test_current_base_main_is_the_canonical_pin(self) -> None:
        paths = [
            ROOT / "README.md",
            ROOT / "AGENTS.md",
            HUB / "START_HERE.md",
            HUB / "ACTIVE_CONTEXT.md",
            HUB / "BASE_RULES_VERSION.md",
            ROOT / "docs" / "base" / "BASE_SYNC_AUDIT_2026-07-21.md",
        ]
        for path in paths:
            text = path.read_text(encoding="utf-8")
            self.assertIn(BASE_COMMIT, text, path)

    def test_pr18_pin_is_preserved_only_as_non_canonical_legacy(self) -> None:
        paths = [
            ROOT / "README.md",
            ROOT / "AGENTS.md",
            HUB / "START_HERE.md",
            HUB / "ACTIVE_CONTEXT.md",
            HUB / "BASE_RULES_VERSION.md",
            ROOT / "docs" / "base" / "BASE_SYNC_AUDIT_2026-07-21.md",
            ROOT / "skills" / "LEGACY_SKILL_ALIASES.md",
        ]
        for path in paths:
            text = path.read_text(encoding="utf-8")
            if LEGACY_COMMIT in text:
                lowered = text.lower()
                self.assertTrue(
                    any(marker in lowered for marker in ("legacy", "비정본", "미병합", "not current")),
                    f"Legacy commit lacks non-canonical classification: {path}",
                )

        registry = self.load_registry()
        legacy = registry["legacy_extensions"]["base_pr18_global_productivity"]
        self.assertEqual(legacy["status"], "PRESERVED_NON_CANONICAL")
        self.assertFalse(legacy["present_in_pinned_base_main"])
        self.assertFalse(legacy["routing_enabled_by_project_registry"])

    def test_automatic_routing_matches_current_base(self) -> None:
        policy = self.load_registry()["routing_policy"]
        self.assertFalse(policy["load_all_skills"])
        self.assertEqual(policy["default_selection"], "automatic-trigger-match")
        self.assertTrue(policy["automatic_selection"])
        self.assertFalse(policy["user_skill_declaration_required"])
        self.assertTrue(policy["require_trigger_match"])
        self.assertTrue(policy["require_execution_report"])
        self.assertEqual(policy["work_modes"], ["PLAN", "BUILD", "REVIEW"])
        self.assertEqual(policy["max_primary_discipline_skills"], 1)
        self.assertEqual(policy["max_foundation_skills"], 3)

    def test_selected_disciplines_and_compatibility_alias_agree(self) -> None:
        registry = self.load_registry()
        selected = registry["selected_disciplines"]
        self.assertEqual(selected, registry["required_disciplines"])
        self.assertEqual(selected, list(registry["discipline_entrypoints"]))
        self.assertTrue(all(registry["discipline_entrypoints"][item] for item in selected))

    def test_all_24_expected_skills_are_registered(self) -> None:
        registry = self.load_registry()
        ids = [item["skill_id"] for item in registry["skills"]]
        self.assertEqual(len(ids), 24)
        self.assertEqual(len(ids), len(set(ids)))
        self.assertEqual(set(BASE_SKILLS + DISCIPLINE_SKILLS), set(ids))

    def test_each_registered_skill_identity_and_contract(self) -> None:
        registry = self.load_registry()
        paths = []
        for item in registry["skills"]:
            path = ROOT / item["path"]
            self.assertTrue(path.is_file(), path)
            paths.append(item["path"])
            text = path.read_text(encoding="utf-8")
            match = FRONT_MATTER_NAME.search(text)
            self.assertIsNotNone(match, path)
            self.assertEqual(match.group(1).strip(), item["skill_id"], path)
            self.assertFalse(item["load_by_default"])
            self.assertTrue(item["trigger_tags"])
            self.assertTrue(item["use_when"])
            self.assertTrue(item["do_not_use_when"])
            self.assertTrue((ROOT / item["learning_log"]).is_file())
            self.assertIn("## Work", text)
            self.assertIn("## Output", text)
        self.assertEqual(len(paths), len(set(paths)))

    def test_schema_uses_selected_disciplines_not_pr18_productivity_requirement(self) -> None:
        schema = json.loads((ROOT / "schemas" / "skill-registry-v3.schema.json").read_text(encoding="utf-8"))
        required = schema["required"]
        self.assertIn("selected_disciplines", required)
        self.assertNotIn("global_productivity", required)
        self.assertIn("required_disciplines", schema["properties"])

    def test_gameplay_files_are_not_part_of_the_base_sync_contract(self) -> None:
        audit = (ROOT / "docs" / "base" / "BASE_SYNC_AUDIT_2026-07-21.md").read_text(encoding="utf-8")
        for phrase in (
            "gameplay code and services",
            "Godot Scenes and Resources",
            "game data and save format",
            "approved battlefield concept image",
        ):
            self.assertIn(phrase, audit)


if __name__ == "__main__":
    unittest.main()
