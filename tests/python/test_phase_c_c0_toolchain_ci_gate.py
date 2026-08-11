from __future__ import annotations

import pathlib
import runpy
import shutil
import tempfile
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[2]
WORKFLOW = ROOT / ".github" / "workflows" / "validate-omenward-core.yml"
VALIDATOR = ROOT / "tools" / "validate_ci_usage_contract.py"


class PhaseCC0ToolchainCiGateTests(unittest.TestCase):
    def test_core_workflow_triggers_for_addons_on_pr_and_push(self) -> None:
        text = WORKFLOW.read_text(encoding="utf-8")
        self.assertEqual(
            2,
            text.count('- "addons/**"'),
            "Validate Omenward Core must trigger for addons/** on both pull_request and push",
        )

    def test_validator_rejects_missing_addon_trigger(self) -> None:
        validate = runpy.run_path(str(VALIDATOR))["validate"]
        with tempfile.TemporaryDirectory() as directory:
            temp_root = pathlib.Path(directory)
            target = temp_root / ".github" / "workflows"
            target.mkdir(parents=True, exist_ok=True)
            for name in (
                "validate-project-core-docs.yml",
                "validate-omenward-core.yml",
                "validate-skill-system.yml",
            ):
                shutil.copy2(ROOT / ".github" / "workflows" / name, target / name)

            workflow = target / "validate-omenward-core.yml"
            text = workflow.read_text(encoding="utf-8")
            if text.count('- "addons/**"') == 2:
                text = text.replace('      - "addons/**"\n', "", 1)
            workflow.write_text(text, encoding="utf-8")

            errors = validate(temp_root)
            self.assertTrue(
                any("core workflow must trigger for addons/** on PR and push" in error for error in errors),
                errors,
            )


if __name__ == "__main__":
    unittest.main()
