from __future__ import annotations

import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[2]
ADAPTER = ROOT / "skills" / "PROJECT_BASE_ADAPTER.json"
ROUTER = ROOT / ".agents" / "skills" / "omenward-workflow-router" / "SKILL.md"
PROJECT_AGENTS = ROOT / "AGENTS.md"
SHARED = ROOT / "skills" / "SHARED_EXECUTION_CONTRACT.md"
BASE_VERSION = ROOT / "docs" / "BASE_RULES_VERSION.md"
ADAPTER_WORKFLOW = ROOT / ".github" / "workflows" / "validate-project-base-adapter.yml"
CURRENT_BASE_MAIN = "edb3b3376603c9f6b00d64af3126304f8c9946bf"


class R54WorkspaceAuthorityReconciliationTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.adapter = json.loads(ADAPTER.read_text(encoding="utf-8"))
        cls.router = ROUTER.read_text(encoding="utf-8")
        cls.project_agents = PROJECT_AGENTS.read_text(encoding="utf-8")
        cls.shared = SHARED.read_text(encoding="utf-8")
        cls.base_version = BASE_VERSION.read_text(encoding="utf-8")
        cls.adapter_workflow = ADAPTER_WORKFLOW.read_text(encoding="utf-8")

    def test_adapter_uses_v2_identity_and_sheet_is_compatibility_only(self) -> None:
        self.assertEqual(self.adapter["schema_version"], 2)
        self.assertEqual(self.adapter["project"]["project_id"], "omenward")
        sheet = self.adapter["gdd_sheet"]
        self.assertEqual(sheet["role"], "GOOGLE_SHEETS_LEGACY_MIGRATION_SOURCE")
        self.assertEqual(sheet["workspace_status"], "MIGRATION_COMPATIBILITY_SURFACE")
        self.assertFalse(sheet["new_input_allowed"])
        self.assertFalse(sheet["read_for_normal_work"])

    def test_adapter_routes_human_and_runtime_authority_to_notion_and_repository(self) -> None:
        planning = self.adapter["shared_overrides"]["managing-project-intake-and-work-contract"]["planning_first_governance"]
        self.assertEqual(planning["current_human_workspace"], "NOTION_DEFAULT_PROJECT_WORKSPACE")
        self.assertEqual(planning["runtime_structured_authority"], "GITHUB_REPOSITORY_AND_ACTUAL_RUNTIME")

    def test_generated_router_remains_generator_owned_while_project_agents_owns_fresh_read(self) -> None:
        self.assertIn("Resolve this project's Base shared and project-local Skills through its verified v9.1 operating contracts.", self.router)
        self.assertIn("Before selecting any route, run the project operating-contract validator", self.router)
        self.assertIn("fresh Base", self.project_agents)
        self.assertIn("Project Notion Home", self.project_agents)
        self.assertIn("Google Sheet", self.project_agents)
        self.assertIn("current human authority", self.project_agents)

    def test_shared_execution_contract_does_not_treat_project_base_version_file_as_current_base_owner(self) -> None:
        self.assertIn("fresh Base latest completed main", self.shared)
        self.assertNotIn("`docs/BASE_RULES_VERSION.md`가 고정한 Base 원칙", self.shared)

    def test_project_base_version_file_is_explicitly_historical_adoption_evidence(self) -> None:
        self.assertIn("PROJECT_BASE_ADOPTION_HISTORY", self.base_version)
        self.assertIn("CURRENT_BASE_AUTHORITY = FRESH_LATEST_COMPLETED_MAIN", self.base_version)
        self.assertIn("GOOGLE_SHEETS = COMPATIBILITY_ONLY", self.base_version)

    def test_adapter_workflow_uses_current_base_validator_without_changing_release_pin(self) -> None:
        self.assertIn(f"ref: {CURRENT_BASE_MAIN}", self.adapter_workflow)
        self.assertNotIn("ref: bfdc9e44d4a6920dc085eaa3f9d19d31b1acd2a1", self.adapter_workflow)
        self.assertEqual(self.adapter["base_release"]["version"], "9.4.3")
        self.assertEqual(
            self.adapter["base_release"]["release_commit"],
            "7dd1a4f80388bc5faca767ff74a3eb32dc9d0ac8",
        )

    def test_remote_canonical_baseline_uses_recorded_ancestry_not_pr_base_override(self) -> None:
        baseline = self.adapter["protected_baseline"]
        self.assertEqual(baseline["authority_kind"], "REMOTE_TRACKING_REF")
        self.assertEqual(baseline["policy_source_type"], "CANONICAL_ADAPTER_SOURCE")
        self.assertIn("RECORDED_PROTECTED_BASE_SHA", self.adapter_workflow)
        self.assertIn("git merge-base --is-ancestor", self.adapter_workflow)
        self.assertNotIn('PROTECTED_BASE_SHA="$PR_BASE_SHA"', self.adapter_workflow)
        self.assertNotIn('--protected-base "$PROTECTED_BASE_SHA"', self.adapter_workflow)


if __name__ == "__main__":
    unittest.main()
