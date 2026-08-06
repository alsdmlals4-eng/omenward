from __future__ import annotations

import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
STATE = ROOT / "docs/operations/BASE_WHOLE_REPOSITORY_AND_SKILL_MAP.v1.json"
MATRIX = ROOT / "docs/operations/LOCAL_VERIFICATION_MATRIX.v1.json"
VALIDATOR = ROOT / "tools/verify_base_recovery_and_local_verification_pack.py"
RUNNER = ROOT / "tools/run_local_verification_pack.py"
POWERSHELL = ROOT / "tools/run_local_verification_pack.ps1"
WSL = ROOT / "tools/run_local_verification_pack_wsl.sh"

DECISION_ID = "OMW-DEC-20260807-PROCESS-BASE-REPOSITORY-SKILL-MAP-AND-LOCAL-VERIFICATION-PACK-V1"
BASE_SHA = "4f98f968a377f7b6a11aafa4fc94d11bddbebedc"
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

EXPECTED_ENVIRONMENTS = {
    ("windows-py311", "windows", "3.11", "py -3.11"),
    ("windows-py312", "windows", "3.12", "py -3.12"),
    ("windows-py313", "windows", "3.13", "py -3.13"),
    ("wsl2-ubuntu-py312", "wsl2-ubuntu", "3.12", "python3.12"),
}


class BaseRecoveryAndLocalPackContract(unittest.TestCase):
    def setUp(self) -> None:
        self.state = json.loads(STATE.read_text(encoding="utf-8"))
        self.matrix = json.loads(MATRIX.read_text(encoding="utf-8"))

    def test_authority_and_gate_are_fail_closed(self) -> None:
        self.assertEqual(self.state["decision_id"], DECISION_ID)
        self.assertEqual(self.state["base_repository_commit"], BASE_SHA)
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

    def test_local_matrix_is_exact_and_unexecuted(self) -> None:
        actual = {
            (row["environment_id"], row["host"], row["python"], row["launcher"])
            for row in self.matrix["environments"]
        }
        self.assertEqual(actual, EXPECTED_ENVIRONMENTS)
        self.assertTrue(
            all(row["execution_status"] == "NOT_RUN_USER_LOCAL"
                for row in self.matrix["environments"])
        )
        self.assertEqual(self.matrix["entry_gate"], "BLOCK")

    def test_scripts_exist_and_bind_all_environments(self) -> None:
        for path in (VALIDATOR, RUNNER, POWERSHELL, WSL):
            self.assertTrue(path.is_file(), path)
        ps = POWERSHELL.read_text(encoding="utf-8")
        self.assertIn('py -3.11', ps)
        self.assertIn('py -3.12', ps)
        self.assertIn('py -3.13', ps)
        sh = WSL.read_text(encoding="utf-8")
        self.assertIn('python3.12', sh)

    def test_common_runner_records_exact_head_and_receipt(self) -> None:
        source = RUNNER.read_text(encoding="utf-8")
        self.assertIn("git rev-parse HEAD", source)
        self.assertIn("expected_head", source)
        self.assertIn("receipt", source)
        self.assertIn("NOT_RUN_USER_LOCAL", MATRIX.read_text(encoding="utf-8"))

    def test_validator_is_import_safe(self) -> None:
        source = VALIDATOR.read_text(encoding="utf-8")
        self.assertIn("def validate", source)
        self.assertIn('if __name__ == "__main__":', source)


if __name__ == "__main__":
    unittest.main()
