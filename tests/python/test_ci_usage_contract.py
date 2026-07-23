from __future__ import annotations

import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[2]
WORKFLOWS = ROOT / ".github" / "workflows"


class CiUsageContractTests(unittest.TestCase):
    def _read(self, name: str) -> str:
        return (WORKFLOWS / name).read_text(encoding="utf-8")

    def test_documentation_pr_uses_one_linux_python_job(self) -> None:
        text = self._read("validate-project-core-docs.yml")
        self.assertIn("runs-on: ubuntu-latest", text)
        self.assertIn('python-version: "3.12"', text)
        self.assertNotIn("matrix:", text)
        self.assertNotIn("unittest discover", text)
        self.assertNotIn("validate_skill_system.py", text)

    def test_core_pr_uses_fast_jobs_but_main_keeps_full_matrix(self) -> None:
        text = self._read("validate-omenward-core.yml")
        self.assertIn("contracts_pr:", text)
        self.assertIn("contracts_full:", text)
        self.assertIn("github.event_name == 'pull_request'", text)
        self.assertIn("github.event_name != 'pull_request'", text)
        self.assertIn("os: [ubuntu-latest, windows-latest]", text)
        self.assertIn('python-version: ["3.12", "3.13"]', text)
        self.assertNotIn('- "docs/**"', text)
        self.assertNotIn('- "README.md"', text)

    def test_all_active_workflows_cancel_stale_pr_runs(self) -> None:
        for name in (
            "validate-project-core-docs.yml",
            "validate-omenward-core.yml",
            "validate-skill-system.yml",
        ):
            with self.subTest(name=name):
                text = self._read(name)
                self.assertIn("concurrency:", text)
                self.assertIn("cancel-in-progress: true", text)


class CiUsageValidatorMutationTests(unittest.TestCase):
    def _load_validator(self):
        import runpy

        validator = ROOT / "tools" / "validate_ci_usage_contract.py"
        if not validator.exists():
            self.fail("CI usage validator is missing")
        return runpy.run_path(str(validator))["validate"]

    def _copy_workflows(self, destination: pathlib.Path) -> None:
        import shutil

        target = destination / ".github" / "workflows"
        target.mkdir(parents=True, exist_ok=True)
        for name in (
            "validate-project-core-docs.yml",
            "validate-omenward-core.yml",
            "validate-skill-system.yml",
        ):
            shutil.copy2(WORKFLOWS / name, target / name)

    def test_current_repository_passes_validator(self) -> None:
        validate = self._load_validator()
        self.assertEqual([], validate(ROOT))

    def test_documentation_matrix_regression_is_rejected(self) -> None:
        import tempfile

        validate = self._load_validator()
        with tempfile.TemporaryDirectory() as directory:
            temp_root = pathlib.Path(directory)
            self._copy_workflows(temp_root)
            workflow = temp_root / ".github" / "workflows" / "validate-project-core-docs.yml"
            workflow.write_text(
                workflow.read_text(encoding="utf-8")
                + '\n# matrix:\n#   os: [ubuntu-latest, windows-latest]\n',
                encoding="utf-8",
            )
            errors = validate(temp_root)
            self.assertTrue(any("documentation workflow must not use a matrix" in error for error in errors))

    def test_core_docs_trigger_regression_is_rejected(self) -> None:
        import tempfile

        validate = self._load_validator()
        with tempfile.TemporaryDirectory() as directory:
            temp_root = pathlib.Path(directory)
            self._copy_workflows(temp_root)
            workflow = temp_root / ".github" / "workflows" / "validate-omenward-core.yml"
            workflow.write_text(
                workflow.read_text(encoding="utf-8").replace(
                    '      - "scripts/**"',
                    '      - "scripts/**"\n      - "docs/**"',
                    1,
                ),
                encoding="utf-8",
            )
            errors = validate(temp_root)
            self.assertTrue(any("core workflow must not trigger on docs/**" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
