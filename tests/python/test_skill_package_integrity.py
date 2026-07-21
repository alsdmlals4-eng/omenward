"""Integrity checks for active Omenward Skill packages."""

from __future__ import annotations

import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
REGISTRY = ROOT / "[기획서]" / "00_프로젝트_허브" / "SKILL_REGISTRY.json"
BACKTICK = re.compile(r"`([^`\n]+)`")
MARKDOWN_LINK = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
LOCAL_PREFIXES = ("skills/", "docs/", "[기획서]/", "schemas/", "tests/", "tools/", ".github/")


def load_registry() -> dict:
    return json.loads(REGISTRY.read_text(encoding="utf-8"))


def candidate_path(raw: str, skill_path: Path) -> Path | None:
    value = raw.strip().strip(".,;:")
    value = value.split("#", 1)[0]
    if not value or value.startswith(("http://", "https://", "mailto:")):
        return None
    if any(token in value for token in ("<", ">", "*", "{", "}", "|")):
        return None
    if value.startswith(LOCAL_PREFIXES):
        return ROOT / value
    if value.startswith(("references/", "scripts/")):
        return skill_path.parent / value
    return None


class ProjectSkillPackageIntegrityTests(unittest.TestCase):
    def test_registry_and_local_skill_packages_are_one_to_one(self) -> None:
        expected = {item["path"] for item in load_registry()["skills"]}
        actual = {
            path.relative_to(ROOT).as_posix()
            for path in (ROOT / "skills").rglob("SKILL.md")
        }
        self.assertEqual(actual, expected)

    def test_all_local_artifact_references_from_skills_exist(self) -> None:
        missing: list[str] = []
        for item in load_registry()["skills"]:
            skill_path = ROOT / item["path"]
            text = skill_path.read_text(encoding="utf-8")
            candidates = set(BACKTICK.findall(text))
            candidates.update(MARKDOWN_LINK.findall(text))
            for raw in sorted(candidates):
                path = candidate_path(raw, skill_path)
                if path is not None and not path.exists():
                    missing.append(f"{item['path']} -> {raw}")
        self.assertEqual(missing, [], "Missing local Skill references:\n" + "\n".join(missing))

    def test_all_active_skills_are_discoverable(self) -> None:
        entrypoints = [
            ROOT / "README.md",
            ROOT / "AGENTS.md",
            ROOT / "docs" / "base" / "BASE_SYNC_AUDIT_2026-07-21.md",
            ROOT / "[기획서]" / "00_프로젝트_허브" / "START_HERE.md",
            ROOT / "[기획서]" / "00_프로젝트_허브" / "DOCUMENTATION_MAP.md",
        ]
        combined = "\n".join(path.read_text(encoding="utf-8") for path in entrypoints)
        missing = [
            item["skill_id"]
            for item in load_registry()["skills"]
            if item["skill_id"] not in combined
        ]
        self.assertEqual(missing, [], f"Undiscoverable active skills: {missing}")

    def test_no_active_skill_uses_a_legacy_id_as_its_name(self) -> None:
        legacy = (ROOT / "skills" / "LEGACY_SKILL_ALIASES.md").read_text(encoding="utf-8")
        current_ids = {item["skill_id"] for item in load_registry()["skills"]}
        for line in legacy.splitlines():
            if not line.startswith("| `"):
                continue
            legacy_id = line.split("`", 2)[1]
            if legacy_id.startswith("Base PR"):
                continue
            self.assertNotIn(legacy_id, current_ids)


if __name__ == "__main__":
    unittest.main()
