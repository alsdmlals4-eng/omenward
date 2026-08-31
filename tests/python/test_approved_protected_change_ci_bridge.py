from __future__ import annotations

import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
BRIDGE = ROOT / "tools" / "validate_approved_protected_change_ci.py"


class ApprovedProtectedChangeCiBridgeTests(unittest.TestCase):
    def run_command(
        self,
        command: list[str],
        *,
        cwd: Path,
        env: dict[str, str] | None = None,
    ) -> subprocess.CompletedProcess[str]:
        merged_env = os.environ | (env or {})
        return subprocess.run(
            command,
            cwd=cwd,
            env=merged_env,
            text=True,
            capture_output=True,
            check=False,
        )

    def write_file(self, root: Path, relative: str, content: str) -> None:
        target = root / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(content, encoding="utf-8")

    def commit(self, project: Path, message: str) -> None:
        completed = self.run_command(["git", "add", "."], cwd=project)
        self.assertEqual(0, completed.returncode, completed.stderr)
        completed = self.run_command(["git", "commit", "-qm", message], cwd=project)
        self.assertEqual(0, completed.returncode, completed.stderr)

    def create_project(self, temporary: Path, changes: dict[str, str]) -> tuple[Path, str]:
        project = temporary / "project"
        project.mkdir()
        for command in (
            ["git", "init", "-q"],
            ["git", "config", "user.email", "ci-bridge@example.test"],
            ["git", "config", "user.name", "CI Bridge Test"],
        ):
            completed = self.run_command(command, cwd=project)
            self.assertEqual(0, completed.returncode, completed.stderr)
        self.write_file(project, "README.md", "base\n")
        self.commit(project, "base")
        base = self.run_command(["git", "rev-parse", "HEAD"], cwd=project)
        self.assertEqual(0, base.returncode, base.stderr)
        for path, content in changes.items():
            self.write_file(project, path, content)
        self.commit(project, "change")
        return project, base.stdout.strip()

    def create_fake_base(self, temporary: Path) -> Path:
        base = temporary / "base"
        tool = base / "tools" / "check_approved_project_operating_contract.py"
        tool.parent.mkdir(parents=True)
        tool.write_text(
            "from __future__ import annotations\n"
            "import json\n"
            "import os\n"
            "import sys\n"
            "from pathlib import Path\n"
            "Path(os.environ['BRIDGE_FAKE_LOG']).write_text(json.dumps(sys.argv[1:]), encoding='utf-8')\n"
            "raise SystemExit(int(os.environ.get('BRIDGE_FAKE_EXIT', '0')))\n",
            encoding="utf-8",
        )
        return base

    def run_bridge(
        self,
        project: Path,
        base: Path,
        protected_base: str,
        log: Path,
    ) -> subprocess.CompletedProcess[str]:
        return self.run_command(
            [
                sys.executable,
                str(BRIDGE),
                "--project-root",
                str(project),
                "--base-repository",
                str(base),
                "--pr-base",
                protected_base,
                "--protected-base",
                protected_base,
                "--external-approval",
                "true",
            ],
            cwd=project,
            env={"BRIDGE_FAKE_LOG": str(log)},
        )

    def test_approved_product_change_delegates_exact_manifest_to_base_gate(self) -> None:
        """A product mutation must reach the Base gate with its sole PR manifest."""
        with tempfile.TemporaryDirectory() as temporary_string:
            temporary = Path(temporary_string)
            approval = "docs/approvals/PROJECT_PROTECTED_CHANGE_APPROVAL_TEST.json"
            project, pr_base = self.create_project(
                temporary,
                {
                    "scripts/battle.gd": "extends Node\n",
                    approval: "{\"status\": \"APPROVED\"}\n",
                },
            )
            base = self.create_fake_base(temporary)
            log = temporary / "validator-arguments.json"

            completed = self.run_bridge(project, base, pr_base, log)

            self.assertEqual(0, completed.returncode, completed.stderr)
            self.assertTrue(log.is_file(), "the Base gate must be invoked for a protected mutation")
            arguments = json.loads(log.read_text(encoding="utf-8"))
            self.assertEqual(
                [
                    "--project-root",
                    str(project.resolve()),
                    "--base-repository",
                    str(base.resolve()),
                    "--protected-base",
                    pr_base,
                    "--approval",
                    approval,
                    "--external-approval",
                    "true",
                    "--check",
                ],
                arguments,
            )

    def test_product_change_without_new_approval_manifest_fails_before_base_gate(self) -> None:
        """Removing the manifest cannot turn the historical CI rejection into a bypass."""
        with tempfile.TemporaryDirectory() as temporary_string:
            temporary = Path(temporary_string)
            project, pr_base = self.create_project(temporary, {"scripts/battle.gd": "extends Node\n"})
            base = self.create_fake_base(temporary)
            log = temporary / "validator-arguments.json"

            completed = self.run_bridge(project, base, pr_base, log)

            self.assertNotEqual(0, completed.returncode)
            self.assertIn("exactly one changed approval manifest", completed.stderr)
            self.assertFalse(log.exists(), "the Base gate must not receive an unapproved protected change")

    def test_document_only_change_skips_the_protected_change_gate(self) -> None:
        """A documentation-only PR retains its own historical scope checks without a fake approval."""
        with tempfile.TemporaryDirectory() as temporary_string:
            temporary = Path(temporary_string)
            project, pr_base = self.create_project(temporary, {"docs/notes.md": "updated\n"})
            base = self.create_fake_base(temporary)
            log = temporary / "validator-arguments.json"

            completed = self.run_bridge(project, base, pr_base, log)

            self.assertEqual(0, completed.returncode, completed.stderr)
            self.assertIn("NO_PROTECTED_PATHS", completed.stdout)
            self.assertFalse(log.exists(), "the Base gate is not a substitute for document-only scope validation")

    def test_multiple_changed_approval_manifests_fail_closed(self) -> None:
        """Ambiguous PR approval selection must be rejected instead of choosing an arbitrary manifest."""
        with tempfile.TemporaryDirectory() as temporary_string:
            temporary = Path(temporary_string)
            project, pr_base = self.create_project(
                temporary,
                {
                    "scripts/battle.gd": "extends Node\n",
                    "docs/approvals/PROJECT_PROTECTED_CHANGE_APPROVAL_A.json": "{}\n",
                    "docs/approvals/PROJECT_PROTECTED_CHANGE_APPROVAL_B.json": "{}\n",
                },
            )
            base = self.create_fake_base(temporary)
            log = temporary / "validator-arguments.json"

            completed = self.run_bridge(project, base, pr_base, log)

            self.assertNotEqual(0, completed.returncode)
            self.assertIn("exactly one changed approval manifest", completed.stderr)
            self.assertFalse(log.exists())


if __name__ == "__main__":
    unittest.main()
