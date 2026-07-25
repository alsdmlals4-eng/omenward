from __future__ import annotations

import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE_COMMIT = "039465c4f135f6de1e524bd147a8005d8a1da28f"
PROJECT_REPOSITORY = "alsdmlals4-eng/omenward"
ROUTE_PATH = ROOT / "skills/BASE_SHARED_SKILL_ROUTES.json"
ADAPTER_PATH = ROOT / "skills/PROJECT_BASE_SKILL_ADAPTER.json"
ARCHIVE_ADAPTER_PATH = ROOT / "docs/archive/ARCHIVE_RETENTION_ADAPTER.json"
ARCHIVE_MANIFEST_PATH = ROOT / "docs/archive/MANIFEST.json"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


class BaseSharedSkillAdapterTests(unittest.TestCase):
    def test_route_and_adapter_use_same_pinned_base(self) -> None:
        route = load(ROUTE_PATH)
        adapter = load(ADAPTER_PATH)
        archive = load(ARCHIVE_ADAPTER_PATH)
        self.assertEqual(route["base"]["repository"], "alsdmlals4-eng/Base")
        self.assertEqual(route["base"]["commit"], BASE_COMMIT)
        self.assertEqual(adapter["base"]["commit"], BASE_COMMIT)
        self.assertEqual(archive["base"]["commit"], BASE_COMMIT)
        self.assertEqual(adapter["project"]["repository"], PROJECT_REPOSITORY)
        self.assertEqual(archive["project"]["repository"], PROJECT_REPOSITORY)

    def test_all_base_skills_route_through_project_adapter(self) -> None:
        route = load(ROUTE_PATH)
        main_route = route["base_registry_route"]
        self.assertEqual(main_route["source_registry"], "skills/SKILL_REGISTRY.json")
        self.assertEqual(main_route["selection"], "automatic-trigger-match")
        self.assertEqual(main_route["adapter"], "skills/PROJECT_BASE_SKILL_ADAPTER.json")
        self.assertFalse(main_route["copy_skill_bodies_to_project"])
        expected = {
            "legacy_retention_and_archives": "governing-legacy-retention-and-archives",
            "godot_assets_before_creation": "evaluating-godot-assets-and-plugins-before-creation",
        }
        self.assertEqual({key: value["skill_id"] for key, value in route["routes"].items()}, expected)
        self.assertEqual(route["routes"]["legacy_retention_and_archives"]["adapter"], "docs/archive/ARCHIVE_RETENTION_ADAPTER.json")
        self.assertEqual(route["routes"]["godot_assets_before_creation"]["adapter"], "skills/PROJECT_BASE_SKILL_ADAPTER.json")
        policy = route["local_skill_policy"]
        self.assertEqual(policy["base_shared_skills"], "adapter-only")
        self.assertEqual(policy["project_specific_skills"], "local-only")
        self.assertFalse(policy["duplicate_base_skill_bodies"])

    def test_adapter_bindings_and_records_exist(self) -> None:
        adapter = load(ADAPTER_PATH)
        required_roles = {
            "project_agents", "documentation_map", "active_context", "skill_registry",
            "archive_root", "archive_readme", "archive_manifest", "archive_retention_adapter",
        }
        self.assertTrue(required_roles <= set(adapter["role_bindings"]))
        for path in adapter["role_bindings"].values():
            self.assertTrue((ROOT / path).exists(), path)
        for path in adapter["canonical_sources"]:
            self.assertTrue((ROOT / path).exists(), path)
        self.assertTrue((ROOT / adapter["third_party_inventory"]).is_file())
        self.assertTrue((ROOT / adapter["license_record"]).is_file())
        self.assertIn("governing-legacy-retention-and-archives", adapter["shared_skill_overrides"])
        self.assertIn("evaluating-godot-assets-and-plugins-before-creation", adapter["shared_skill_overrides"])

    def test_archive_is_non_authoritative_and_manifest_is_valid(self) -> None:
        archive = load(ARCHIVE_ADAPTER_PATH)
        manifest = load(ARCHIVE_MANIFEST_PATH)
        policies = archive["policies"]
        self.assertTrue(policies["preserve_original_content"])
        self.assertFalse(policies["blank_placeholders_allowed"])
        self.assertFalse(policies["secrets_may_be_archived"])
        self.assertFalse(policies["default_active_authority"])
        self.assertEqual(policies["default_implementation_authority"], "NONE")
        self.assertEqual(manifest["manifest_role"], "project-archive-retention-index")
        self.assertIsInstance(manifest["records"], list)
        readme = (ROOT / archive["paths"]["archive_readme"]).read_text(encoding="utf-8")
        self.assertTrue("현재 정본" in readme or "current canon" in readme)


if __name__ == "__main__":
    unittest.main()
