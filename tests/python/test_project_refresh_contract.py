"""Regression checks for Omenward's current Base-main refresh contract."""

import unittest
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[2]


class ProjectRefreshContractTests(unittest.TestCase):
    def test_project_metadata_preserves_the_approved_display_contract(self):
        project = (PROJECT_ROOT / "project.godot").read_text(encoding="utf-8")
        self.assertIn('config/features=PackedStringArray("4.7")', project)
        self.assertIn('window/stretch/mode="viewport"', project)
        self.assertIn('window/stretch/aspect="keep"', project)
        self.assertIn('window/stretch/scale_mode="integer"', project)
        self.assertIn('textures/default_filters/use_nearest_mipmap_filter=false', project)

    def test_publication_workflow_runs_contract_tests_and_clean_generation(self):
        workflow = (
            PROJECT_ROOT / ".github" / "workflows" / "validate-document-publications.yml"
        ).read_text(encoding="utf-8")
        self.assertIn("actions/checkout@v7", workflow)
        self.assertIn("actions/setup-python@v6", workflow)
        self.assertIn("actions/setup-node@v7", workflow)
        self.assertIn("python -m unittest discover -s tests/python -v", workflow)
        self.assertIn("python tools/check_active_markdown_links.py", workflow)
        self.assertIn("git diff --exit-code", workflow)
        self.assertIn('"$GITHUB_SHA"', workflow)
        self.assertIn("$env:GITHUB_OUTPUT", workflow)
        self.assertIn("steps.skill-source.outputs.commit", workflow)

    def test_migration_verifier_keeps_existing_project_exceptions(self):
        verifier = (PROJECT_ROOT / "tools" / "verify_migration_inventory.py").read_text(
            encoding="utf-8"
        )
        for path in (
            '"project.godot"',
            '".gitignore"',
            '"docs/VERTICAL_SLICE_VALIDATION.md"',
            '"tests/README.md"',
        ):
            self.assertIn(path, verifier)


if __name__ == "__main__":
    unittest.main()
