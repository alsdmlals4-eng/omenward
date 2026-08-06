from __future__ import annotations

import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
STATE = ROOT / "docs/operations/BASE_WHOLE_REPOSITORY_AND_SKILL_MAP.v1.json"

DECISION_ID = "OMW-DEC-20260807-PROCESS-BASE-REPOSITORY-SKILL-MAP-AND-LOCAL-VERIFICATION-PACK-V1"
BASE_SHA = "4f98f968a377f7b6a11aafa4fc94d11bddbebedc"
BASE_TREE_SHA = "4bc8d45d4bb88649eb5041f16478b862801b3901"
OMENWARD_SHA = "93c388ad1c50581671f8ea059357c863d8d8e0f7"

EXPECTED_ROOT_PATHS = {
    ".codex-plugin", ".gitattributes", ".github", ".gitignore", "AGENTS.md",
    "LICENSE", "README.md", "SECURITY.md", "START_HERE.md", "[수정제안서]",
    "base-v9.1.lock.json", "base-v9.2.lock.json", "base-v9.3.lock.json",
    "base-v9.4.1.lock.json", "base-v9.4.2.lock.json",
    "base-v9.4.3.lock.json", "base-v9.4.lock.json", "base.lock.json",
    "docs", "examples", "package.json", "pnpm-lock.yaml",
    "pnpm-workspace.yaml", "requirements-publication.txt", "schemas",
    "skills", "templates", "tests", "tools",
}

EXPECTED_SKILLS = {
    "analyzing-and-refining-game-concepts",
    "auditing-and-refining-ui-art",
    "auditing-canonical-reference-freshness",
    "building-project-visual-dashboards",
    "creating-user-learning-notes",
    "designing-art-prompts-and-technique-cards",
    "designing-vertical-slices",
    "diagnosing-game-engine-runtime-failures",
    "establishing-project-core",
    "evaluating-godot-assets-and-plugins-before-creation",
    "evolving-project-discipline-skills",
    "governing-game-user-research-coverage",
    "governing-legacy-retention-and-archives",
    "identifying-project-core",
    "maintaining-long-running-task-continuity",
    "maintaining-project-context-and-handoff",
    "managing-base-change-proposals",
    "managing-design-documents",
    "managing-game-project-operating-system",
    "managing-project-intake-and-work-contract",
    "optimizing-ai-model-and-prompt-costs",
    "orchestrating-deepseek-worktrees",
    "producing-game-development-youtube-videos",
    "pruning-stale-and-nonfunctional-material",
    "refactoring-with-contract-preservation",
    "reviewing-and-validating-project-changes",
    "running-adversarial-review-and-refinement",
    "simplifying-skill-bodies",
    "synchronizing-local-and-github-state",
}

EXPECTED_WORKFLOWS = {
    "dependency-review.yml",
    "reusable-godot-project-pilot.yml",
    "validate-base-v9-rc.yml",
    "validate-bca-visual-sheet-workflow.yml",
    "validate-evidence-knowledge.yml",
    "validate-game-project-operating-system.yml",
    "validate-game-ux-ui-system.yml",
    "validate-integrated-vertical-slice-prompt.yml",
    "validate-skill-behavior-evidence.yml",
}

REMOVED_LOCAL_PACK_PATHS = (
    ".github/workflows/validate-base-recovery-local-verification-pack.yml",
    "docs/operations/LOCAL_VERIFICATION_MATRIX.v1.json",
    "tests/python/test_base_recovery_and_local_verification_pack.py",
    "tests/python/test_local_verification_powershell_root.py",
    "tests/python/test_local_verification_pack_registration.py",
    "tools/run_local_verification_pack.py",
    "tools/run_local_verification_pack.ps1",
    "tools/run_local_verification_pack_wsl.sh",
    "tools/verify_base_recovery_and_local_verification_pack.py",
)


class BaseRecoveryMapContract(unittest.TestCase):
    def setUp(self) -> None:
        self.state = json.loads(STATE.read_text(encoding="utf-8"))

    def test_authority_and_gate_are_fail_closed(self) -> None:
        self.assertEqual(self.state["decision_id"], DECISION_ID)
        self.assertEqual(self.state["base_repository_commit"], BASE_SHA)
        self.assertEqual(self.state["base_root_tree_sha"], BASE_TREE_SHA)
        self.assertEqual(self.state["omenward_repository_base_commit"], OMENWARD_SHA)
        self.assertEqual(self.state["recovery_status"], "INCOMPLETE")
        self.assertFalse(self.state["base_recovery_blocker_cleared"])
        self.assertEqual(self.state["entry_gate"], "BLOCK")

    def test_root_inventory_is_exact(self) -> None:
        self.assertEqual(set(self.state["root_inventory"]), EXPECTED_ROOT_PATHS)
        self.assertEqual(self.state["root_inventory_count"], len(EXPECTED_ROOT_PATHS))

    def test_skill_and_workflow_inventory_is_exact(self) -> None:
        self.assertEqual(set(self.state["skill_entrypoints"]), EXPECTED_SKILLS)
        self.assertEqual(self.state["skill_entrypoint_count"], len(EXPECTED_SKILLS))
        self.assertEqual(set(self.state["workflow_files"]), EXPECTED_WORKFLOWS)
        self.assertEqual(self.state["workflow_count"], len(EXPECTED_WORKFLOWS))

    def test_unread_surfaces_are_explicit_and_blocking(self) -> None:
        unread = self.state["unread_or_partially_read_surfaces"]
        self.assertGreater(len(unread), 0)
        self.assertTrue(all(row["status"] in {"NOT_READ", "PARTIAL_READ"} for row in unread))
        self.assertTrue(all(row["gate_effect"] == "BLOCKED" for row in unread))

    def test_existing_actions_workflow_is_the_only_validation_path(self) -> None:
        strategy = self.state["validation_strategy"]
        self.assertEqual(strategy["primary_workflow"], ".github/workflows/validate-omenward-core.yml")
        self.assertEqual(strategy["trigger"], "workflow_dispatch")
        self.assertEqual(strategy["runner_policy"], "STANDARD_GITHUB_HOSTED_ONLY")
        self.assertEqual(strategy["operating_systems"], ["ubuntu-latest", "windows-latest"])
        self.assertEqual(strategy["python_versions"], ["3.11", "3.12", "3.13"])
        self.assertEqual(strategy["local_verification_pack"], "REMOVED")

    def test_local_verification_pack_is_absent(self) -> None:
        for relative_path in REMOVED_LOCAL_PACK_PATHS:
            with self.subTest(path=relative_path):
                self.assertFalse((ROOT / relative_path).exists(), relative_path)


if __name__ == "__main__":
    unittest.main()
