from __future__ import annotations

import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def load(path: str) -> dict:
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


class OmenwardV91OperatingContractTests(unittest.TestCase):
    def test_only_omenward_specific_skills_are_project_local(self) -> None:
        adapter = load("skills/PROJECT_BASE_ADAPTER.json")
        self.assertEqual(
            {route["route_id"] for route in adapter["routing"]["project_routes"]},
            {"omenward-art-assets", "omenward-core-design", "omenward-core-ux", "omenward-godot"},
        )
        self.assertIn(
            "managing-game-project-operating-system",
            {route["route_id"] for route in adapter["routing"]["base_routes"]},
        )

    def test_router_uses_only_generated_contracts(self) -> None:
        router = (ROOT / ".agents/skills/omenward-workflow-router/SKILL.md").read_text(encoding="utf-8")
        self.assertIn("PROJECT_BASE_ADAPTER.json", router)
        self.assertIn("PROJECT_SKILL_SNAPSHOT.json", router)
        self.assertNotIn("skills/foundation/", router)

    def test_legacy_skill_classes_are_explicit_and_non_destructive(self) -> None:
        manifest = load("docs/archive/OMENWARD_LEGACY_SKILL_MANIFEST.json")
        records = manifest["records"]
        self.assertEqual(len(records), 24)
        self.assertEqual(
            {record["classification"] for record in records},
            {"KEEP", "REPLACED", "ARCHIVE", "DELETE_CANDIDATE"},
        )
        self.assertTrue((ROOT / "docs/base/SKILL_REGISTRY.json").is_file())


if __name__ == "__main__":
    unittest.main()
