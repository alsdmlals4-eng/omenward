from __future__ import annotations

import pathlib
import tempfile
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[2]
WORKFLOWS = ROOT / ".github" / "workflows"


class CiUsageContractTests(unittest.TestCase):
    def _read(self, name: str) -> str:
        return (WORKFLOWS / name).read_text(encoding="utf-8")

    @staticmethod
    def _section(text: str, start: str, end: str | None = None) -> str:
        start_index = text.find(start)
        if start_index < 0:
            return ""
        if end is None:
            return text[start_index:]
        end_index = text.find(end, start_index + len(start))
        if end_index < 0:
            return text[start_index:]
        return text[start_index:end_index]

    def test_documentation_pr_uses_one_linux_python_job(self) -> None:
        text = self._read("validate-project-core-docs.yml")
        self.assertIn("runs-on: ubuntu-latest", text)
        self.assertIn('python-version: "3.12"', text)
        self.assertNotIn("matrix:", text)
        self.assertNotIn("unittest discover", text)
        self.assertNotIn("validate_skill_system.py", text)

    def test_documentation_workflow_does_not_duplicate_skill_or_core_workflows(self) -> None:
        text = self._read("validate-project-core-docs.yml")
        self.assertEqual(2, text.count('- "!docs/base/**"'))
        self.assertEqual(2, text.count('- "!docs/BASE_RULES_VERSION.md"'))
        self.assertNotIn('.github/workflows/validate-omenward-core.yml', text)
        self.assertNotIn('.github/workflows/validate-skill-system.yml', text)

    def test_core_pr_runs_full_suite_before_merge_and_main_keeps_full_matrix(self) -> None:
        text = self._read("validate-omenward-core.yml")
        pr_section = self._section(text, "  contracts_pr:", "  contracts_full:")
        full_section = self._section(text, "  contracts_full:", "  godot:")
        project_checkout = self._section(full_section, "    steps:\n", "      - name: Checkout exact Base recovery source")
        self.assertIn("contracts_pr:", text)
        self.assertIn("contracts_full:", text)
        self.assertIn("github.event_name == 'pull_request'", text)
        self.assertIn("github.event_name != 'pull_request'", text)
        self.assertIn("workflow_dispatch:", text)
        self.assertIn("os: [ubuntu-latest, windows-latest]", text)
        self.assertIn('python-version: ["3.11", "3.12", "3.13"]', text)
        self.assertIn("runs-on: ${{ matrix.os }}", full_section)
        self.assertNotIn("self-hosted", full_section)
        self.assertNotIn('- "docs/**"', text)
        self.assertNotIn('- "README.md"', text)
        self.assertIn("python -m unittest discover -s tests/python -v", pr_section)
        self.assertIn("python -m unittest discover -s tests/python -v", full_section)
        self.assertIn("fetch-depth: 0", pr_section)
        self.assertIn("fetch-depth: 0", project_checkout)
        self.assertIn("python -m pip install --disable-pip-version-check numpy", pr_section)
        self.assertIn("python -m pip install --disable-pip-version-check numpy", full_section)
        self.assertIn("::error title=Python repository test failure::", pr_section)
        for test_name in (
            "tests.python.test_c1_roulette_contract",
            "tests.python.test_c2_battle_objective_contract",
            "tests.python.test_c3_core_ux_contract",
            "tests.python.test_ci_usage_contract",
            "tests.python.test_base_recovery_map",
        ):
            self.assertIn(test_name, pr_section)
        self.assertIn("python tools/validate_ci_usage_contract.py", pr_section)

    def test_skill_workflow_self_validates_ci_usage_contract(self) -> None:
        text = self._read("validate-skill-system.yml")
        self.assertIn("python tools/validate_ci_usage_contract.py", text)
        self.assertIn("tests.python.test_ci_usage_contract", text)

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

    def test_documentation_skill_overlap_regression_is_rejected(self) -> None:
        validate = self._load_validator()
        with tempfile.TemporaryDirectory() as directory:
            temp_root = pathlib.Path(directory)
            self._copy_workflows(temp_root)
            workflow = temp_root / ".github" / "workflows" / "validate-project-core-docs.yml"
            workflow.write_text(
                workflow.read_text(encoding="utf-8").replace(
                    '      - "!docs/base/**"\n',
                    "",
                    1,
                ),
                encoding="utf-8",
            )
            errors = validate(temp_root)
            self.assertTrue(any("exclude Skill base docs from PR and push triggers" in error for error in errors))

    def test_core_docs_trigger_regression_is_rejected(self) -> None:
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

    def test_core_pr_full_suite_omission_is_rejected(self) -> None:
        validate = self._load_validator()
        with tempfile.TemporaryDirectory() as directory:
            temp_root = pathlib.Path(directory)
            self._copy_workflows(temp_root)
            workflow = temp_root / ".github" / "workflows" / "validate-omenward-core.yml"
            text = workflow.read_text(encoding="utf-8")
            pr_start = text.index("  contracts_pr:")
            full_start = text.index("  contracts_full:")
            pr_section = text[pr_start:full_start].replace(
                "python -m unittest discover -s tests/python -v",
                "python -m unittest tests.python.test_c1_roulette_contract tests.python.test_c2_battle_objective_contract tests.python.test_c3_core_ux_contract tests.python.test_ci_usage_contract tests.python.test_base_recovery_map -v",
                1,
            )
            workflow.write_text(text[:pr_start] + pr_section + text[full_start:], encoding="utf-8")
            errors = validate(temp_root)
            self.assertTrue(any("core PR job must run the full Python suite" in error for error in errors))

    def test_core_pr_shallow_checkout_regression_is_rejected(self) -> None:
        validate = self._load_validator()
        with tempfile.TemporaryDirectory() as directory:
            temp_root = pathlib.Path(directory)
            self._copy_workflows(temp_root)
            workflow = temp_root / ".github" / "workflows" / "validate-omenward-core.yml"
            text = workflow.read_text(encoding="utf-8")
            pr_start = text.index("  contracts_pr:")
            full_start = text.index("  contracts_full:")
            pr_section = text[pr_start:full_start].replace("fetch-depth: 0", "fetch-depth: 1", 1)
            workflow.write_text(text[:pr_start] + pr_section + text[full_start:], encoding="utf-8")
            errors = validate(temp_root)
            self.assertTrue(any("core PR job must fetch project history" in error for error in errors))

    def test_core_python_311_regression_is_rejected(self) -> None:
        validate = self._load_validator()
        with tempfile.TemporaryDirectory() as directory:
            temp_root = pathlib.Path(directory)
            self._copy_workflows(temp_root)
            workflow = temp_root / ".github" / "workflows" / "validate-omenward-core.yml"
            workflow.write_text(
                workflow.read_text(encoding="utf-8").replace(
                    'python-version: ["3.11", "3.12", "3.13"]',
                    'python-version: ["3.12", "3.13"]',
                    1,
                ),
                encoding="utf-8",
            )
            errors = validate(temp_root)
            self.assertTrue(any("Python 3.11, 3.12, and 3.13" in error for error in errors))

    def test_core_self_hosted_regression_is_rejected(self) -> None:
        validate = self._load_validator()
        with tempfile.TemporaryDirectory() as directory:
            temp_root = pathlib.Path(directory)
            self._copy_workflows(temp_root)
            workflow = temp_root / ".github" / "workflows" / "validate-omenward-core.yml"
            workflow.write_text(
                workflow.read_text(encoding="utf-8").replace(
                    "runs-on: ${{ matrix.os }}",
                    "runs-on: [self-hosted, ${{ matrix.os }}]",
                    1,
                ),
                encoding="utf-8",
            )
            errors = validate(temp_root)
            self.assertTrue(any("standard GitHub-hosted runners" in error for error in errors))

    def test_core_full_history_regression_is_rejected(self) -> None:
        validate = self._load_validator()
        with tempfile.TemporaryDirectory() as directory:
            temp_root = pathlib.Path(directory)
            self._copy_workflows(temp_root)
            workflow = temp_root / ".github" / "workflows" / "validate-omenward-core.yml"
            text = workflow.read_text(encoding="utf-8")
            full_start = text.index("  contracts_full:")
            full_end = text.index("  godot:", full_start)
            full_section = text[full_start:full_end].replace("fetch-depth: 0", "fetch-depth: 1", 1)
            workflow.write_text(text[:full_start] + full_section + text[full_end:], encoding="utf-8")
            errors = validate(temp_root)
            self.assertTrue(any("full matrix must fetch project history" in error for error in errors))

    def test_core_full_numpy_dependency_regression_is_rejected(self) -> None:
        validate = self._load_validator()
        with tempfile.TemporaryDirectory() as directory:
            temp_root = pathlib.Path(directory)
            self._copy_workflows(temp_root)
            workflow = temp_root / ".github" / "workflows" / "validate-omenward-core.yml"
            workflow.write_text(
                workflow.read_text(encoding="utf-8").replace(
                    "      - name: Install full-suite Python dependency\n        run: python -m pip install --disable-pip-version-check numpy\n",
                    "",
                    1,
                ),
                encoding="utf-8",
            )
            errors = validate(temp_root)
            self.assertTrue(any("full matrix must install numpy" in error for error in errors))

    def test_skill_ci_contract_omission_is_rejected(self) -> None:
        validate = self._load_validator()
        with tempfile.TemporaryDirectory() as directory:
            temp_root = pathlib.Path(directory)
            self._copy_workflows(temp_root)
            workflow = temp_root / ".github" / "workflows" / "validate-skill-system.yml"
            workflow.write_text(
                workflow.read_text(encoding="utf-8").replace(
                    "      - name: Validate CI usage contract\n        run: python tools/validate_ci_usage_contract.py\n",
                    "",
                    1,
                ),
                encoding="utf-8",
            )
            errors = validate(temp_root)
            self.assertTrue(any("Skill workflow must validate the CI usage contract" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
