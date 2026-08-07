from __future__ import annotations

import json
import subprocess
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
STATE = ROOT / "docs/operations/BASE_WHOLE_REPOSITORY_AND_SKILL_MAP.v1.json"
WORKFLOW = ROOT / ".github/workflows/validate-omenward-core.yml"
BASE_CHECKOUT = ROOT / "_base_recovery"

DECISION_ID = "OMW-DEC-20260807-PROCESS-BASE-REPOSITORY-SKILL-MAP-AND-LOCAL-VERIFICATION-PACK-V1"
PUBLIC_DECISION_ID = "OMW-DEC-20260807-PROCESS-PUBLIC-REPOSITORY-STANDARD-HOSTED-ACTIONS-V1"
BASE_SHA = "fa69a77a14f923a756064f6ae151d34cadb374f7"
BASE_TREE_SHA = "913b69460649fe717294a27246e0b833958e70e4"
OMENWARD_SHA = "c3efdba7c288f391f492fd5313d80ad5b824de3b"

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

BINARY_SUFFIXES = {
    ".png", ".jpg", ".jpeg", ".webp", ".gif", ".ico", ".woff", ".woff2",
    ".ttf", ".otf", ".pdf", ".zip", ".gz", ".bin",
}
ALLOWED_CLASSIFICATIONS = {
    "SKILL", "ROUTER", "WORKFLOW", "TEMPLATE", "POLICY", "TEST", "SCRIPT",
    "REGISTRY", "ARCHIVE", "GENERATED", "BINARY",
}


def classify_base_path(path: str) -> str | None:
    p = Path(path)
    suffix = p.suffix.lower()
    name = p.name

    if suffix in BINARY_SUFFIXES:
        return "BINARY"
    if path.startswith("docs/archive/") or path.startswith("[수정제안서]/"):
        return "ARCHIVE"
    if path.startswith("docs/generated/") or name in {"pnpm-lock.yaml"}:
        return "GENERATED"
    if path.startswith(".github/workflows/"):
        return "WORKFLOW"
    if path.startswith("templates/") or path.startswith("examples/"):
        return "TEMPLATE"
    if path.startswith("tests/"):
        return "TEST"
    if path.startswith("tools/"):
        return "SCRIPT"
    if path.startswith("schemas/") or path.startswith(".codex-plugin/"):
        return "REGISTRY"
    if name.endswith("SKILL.md") and path.startswith("skills/"):
        return "SKILL"
    if "router" in name.lower() and path.startswith("skills/"):
        return "ROUTER"
    if path.startswith("skills/"):
        if name.endswith("REGISTRY.json") or name.endswith("SNAPSHOT.json") or name.endswith("ROUTES.json"):
            return "REGISTRY"
        return "POLICY"
    if path.startswith("docs/") or path.startswith(".github/"):
        return "POLICY"
    if name.startswith("base") and name.endswith(".lock.json"):
        return "REGISTRY"
    if name in {"package.json", "pnpm-workspace.yaml", "requirements-publication.txt"}:
        return "REGISTRY"
    if name in {"AGENTS.md", "README.md", "SECURITY.md", "START_HERE.md", "LICENSE", ".gitattributes", ".gitignore"}:
        return "POLICY"
    return None


class BaseRecoveryMapContract(unittest.TestCase):
    def setUp(self) -> None:
        self.state = json.loads(STATE.read_text(encoding="utf-8"))

    def test_current_authority_and_base_recovery_gate_are_complete(self) -> None:
        self.assertEqual(self.state["decision_id"], DECISION_ID)
        self.assertEqual(self.state["base_repository_commit"], BASE_SHA)
        self.assertEqual(self.state["base_root_tree_sha"], BASE_TREE_SHA)
        self.assertEqual(self.state["omenward_repository_base_commit"], OMENWARD_SHA)
        self.assertEqual(self.state["recovery_status"], "COMPLETE")
        self.assertTrue(self.state["base_recovery_blocker_cleared"])
        self.assertEqual(self.state["entry_gate"], "BLOCK")

    def test_v44_recovery_scope_is_inventory_plus_relevant_full_text(self) -> None:
        contract = self.state["recovery_contract"]
        self.assertEqual(contract["authority"], "PROJECT_TOTAL_PLANNING_IMPLEMENTATION_AND_DELIVERY_INSTRUCTION_v4.4#4.1")
        self.assertEqual(contract["tracked_file_requirement"], "WHOLE_TRACKED_FILE_INVENTORY_AND_CLASSIFICATION")
        self.assertEqual(contract["full_text_requirement"], "PROJECT_RELEVANT_TEXT_ONLY")
        self.assertEqual(contract["non_relevant_text_policy"], "INDEX_AND_CLASSIFY_WITHOUT_BLIND_FULL_LOAD")
        self.assertTrue(contract["record_unread_or_unverified"])
        self.assertEqual(self.state["unread_or_partially_read_surfaces"], [])

    def test_root_skill_and_workflow_inventories_are_current(self) -> None:
        self.assertEqual(set(self.state["root_inventory"]), EXPECTED_ROOT_PATHS)
        self.assertEqual(self.state["root_inventory_count"], len(EXPECTED_ROOT_PATHS))
        self.assertEqual(set(self.state["skill_entrypoints"]), EXPECTED_SKILLS)
        self.assertEqual(self.state["skill_entrypoint_count"], len(EXPECTED_SKILLS))
        self.assertEqual(set(self.state["workflow_files"]), EXPECTED_WORKFLOWS)
        self.assertEqual(self.state["workflow_count"], len(EXPECTED_WORKFLOWS))

    def test_public_ci_checks_out_exact_current_base_for_inventory_validation(self) -> None:
        workflow = WORKFLOW.read_text(encoding="utf-8")
        self.assertIn("repository: alsdmlals4-eng/Base", workflow)
        self.assertIn(f"ref: {BASE_SHA}", workflow)
        self.assertIn("path: _base_recovery", workflow)

    def test_every_current_base_tracked_file_has_a_classification(self) -> None:
        self.assertTrue(BASE_CHECKOUT.is_dir(), "CI must check out current Base into _base_recovery")
        head = subprocess.check_output(
            ["git", "-C", str(BASE_CHECKOUT), "rev-parse", "HEAD"], text=True
        ).strip()
        self.assertEqual(head, BASE_SHA)
        tracked = subprocess.check_output(
            ["git", "-C", str(BASE_CHECKOUT), "-c", "core.quotepath=false", "ls-files"], text=True
        ).splitlines()
        self.assertGreater(len(tracked), 0)
        classified = {path: classify_base_path(path) for path in tracked}
        unclassified = [path for path, category in classified.items() if category is None]
        invalid = {
            path: category for path, category in classified.items()
            if category is not None and category not in ALLOWED_CLASSIFICATIONS
        }
        self.assertEqual(unclassified, [])
        self.assertEqual(invalid, {})
        self.assertEqual(self.state["tracked_file_classification"]["unclassified_count"], 0)
        self.assertEqual(self.state["tracked_file_classification"]["validation"], "CI_GIT_LS_FILES_ZERO_UNCLASSIFIED")

    def test_project_relevant_full_text_evidence_is_closed(self) -> None:
        evidence = self.state["project_relevant_full_text_evidence"]
        required = {
            "START_HERE.md",
            "AGENTS.md",
            "docs/OPERATING_MODEL.md",
            "docs/WORK_MODE_AND_SKILL_ROUTING.md",
            "docs/DOCUMENTATION_MAP.md",
            "skills/SKILL_REGISTRY.json",
            "docs/BASE_SHARED_SKILL_ADAPTER_CONTRACT.md",
            "skills/managing-game-project-operating-system/SKILL.md",
            "skills/managing-game-project-operating-system/references/project-adapter-and-routing-contract.md",
            "skills/reviewing-and-validating-project-changes/SKILL.md",
            "skills/running-adversarial-review-and-refinement/SKILL.md",
            "docs/knowledge/godot/HIGODOT_SINGLE_AUTHORITY_AND_SAFE_OPERATION.md",
            "docs/PROJECT_GDD_GOOGLE_SHEETS_POLICY.md",
        }
        by_path = {row["path"]: row for row in evidence}
        self.assertTrue(required.issubset(by_path))
        self.assertTrue(all(by_path[path]["status"] == "FULL_TEXT_READ" for path in required))

    def test_adapter_delta_is_recorded_without_automatic_migration(self) -> None:
        delta = self.state["omenward_base_adapter_delta"]
        self.assertEqual(delta["project_release_pin"], "9.4.3")
        self.assertEqual(delta["current_base_main"], BASE_SHA)
        self.assertEqual(delta["release_pin_verdict"], "VALID_RELEASE_PIN")
        self.assertEqual(delta["current_base_main_delta"], "PRESENT_POST_RELEASE")
        self.assertEqual(delta["migration_action"], "NO_AUTOMATIC_MIGRATION")
        self.assertEqual(delta["adapter_freshness_followup"], "REQUIRED_SEPARATE_FIX")

    def test_existing_actions_remain_the_validation_path(self) -> None:
        strategy = self.state["validation_strategy"]
        self.assertEqual(strategy["primary_workflow"], ".github/workflows/validate-omenward-core.yml")
        self.assertEqual(strategy["runner_policy"], "STANDARD_GITHUB_HOSTED_ONLY")
        self.assertEqual(strategy["operating_systems"], ["ubuntu-latest", "windows-latest"])
        self.assertEqual(strategy["python_versions"], ["3.11", "3.12", "3.13"])
        self.assertEqual(strategy["local_verification_pack"], "REMOVED")
        self.assertEqual(strategy["repository_visibility_observed"], "public")
        self.assertEqual(strategy["visibility_decision_id"], PUBLIC_DECISION_ID)


if __name__ == "__main__":
    unittest.main()
