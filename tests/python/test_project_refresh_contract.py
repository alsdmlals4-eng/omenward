"""Regression checks for the Base PR #18 refresh contract."""

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

    def test_publication_workflow_uses_the_build_commit(self):
        workflow = (
            PROJECT_ROOT / ".github" / "workflows" / "validate-document-publications.yml"
        ).read_text(encoding="utf-8")

        self.assertNotIn("--source-commit 4cb0ae4", workflow)
        self.assertIn('"$GITHUB_SHA"', workflow)
        self.assertIn("$env:GITHUB_SHA", workflow)

    def test_migration_verifier_records_the_project_metadata_exception(self):
        verifier = (PROJECT_ROOT / "tools" / "verify_migration_inventory.py").read_text(
            encoding="utf-8"
        )

        self.assertIn('"project.godot"', verifier)
        self.assertIn('".gitignore"', verifier)
        self.assertIn('"docs/VERTICAL_SLICE_VALIDATION.md"', verifier)
        self.assertIn('"tests/README.md"', verifier)


if __name__ == "__main__":
    unittest.main()
