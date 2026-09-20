import importlib.util
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class ScopeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        path = ROOT / 'tools/replan_scope.py'
        cls.module = None
        if path.exists():
            spec = importlib.util.spec_from_file_location('replan_scope', path)
            cls.module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(cls.module)

    def test_approved_front_is_allowed(self):
        self.assertIsNotNone(self.module, 'Missing scoped implementation contract evaluator')
        self.assertEqual([], self.module.unapproved(['scripts/replan/front_screen.gd']))

    def test_legacy_code_stays_protected(self):
        self.assertIsNotNone(self.module)
        self.assertEqual(['scripts/core/stage_run.gd'], self.module.unapproved(['scripts/core/stage_run.gd']))

    def test_p00_p01_exact_continuation_paths(self):
        self.assertEqual([], self.module.unapproved([
            'docs/DOCUMENT_LIFECYCLE_REGISTRY.md', 'docs/DOCUMENTATION_MAP.md',
            'docs/OMENWARD_GDD_CURRENT_CANON.md', 'docs/PROJECT_CORE.md',
            'scripts/replan/front_save.gd', 'scripts/replan/front_save.gd.uid',
            'tests/replan_save_test.gd', 'tests/replan_save_test.gd.uid']))
        self.assertEqual(['scripts/replan/front_save_other.gd'],
                         self.module.unapproved(['scripts/replan/front_save_other.gd']))

    def test_current_blueprint_consumers_are_explicit(self):
        self.assertEqual([], self.module.unapproved([
            'docs/design/OMENWARD_BLUEPRINT_BUILD_INPUT_20260911.json',
            'docs/design/OMENWARD_HUMAN_BLUEPRINT_REVIEW_20260911.md']))

    def test_sibling_and_traversal_rejected(self):
        self.assertIsNotNone(self.module)
        for path in ['scripts/replan/other.gd', 'scripts/replan/../core/stage_run.gd', '/scripts/replan/front_run.gd', 'addons/gut/plugin.gd']:
            self.assertEqual([path], self.module.unapproved([path]))

    def test_only_exact_protected_changes_are_classified(self):
        self.assertIsNotNone(self.module)
        errors = ['Protected-path changes detected: scripts/replan/front_run.gd']
        self.assertEqual([], self.module.unresolved(errors))
        self.assertEqual(['hash mismatch'], self.module.unresolved(errors + ['hash mismatch']))

    def test_unapproved_cannot_hide_among_approved(self):
        self.assertIsNotNone(self.module)
        errors = ['Protected-path changes detected: scripts/replan/front_run.gd, addons/gut/plugin.gd']
        self.assertEqual(errors, self.module.unresolved(errors))

    def test_governance_ci_consumer_only_is_allowed(self):
        self.assertEqual([], self.module.unapproved(['.github/workflows/validate-project-base-adapter.yml']))
        for path in ['skills/unrelated.json', '.github/workflows/other.yml', 'assets/new.png']:
            self.assertEqual([path], self.module.unapproved([path]))

    def test_project_projection_retains_unrelated_errors_and_baseline(self):
        from unittest.mock import Mock, patch
        contract = Mock()
        contract.validation_errors.return_value = ['hash mismatch', 'Generated artifact mismatch: other']
        with patch.object(self.module, 'selected_source_errors', return_value=[]):
            errors = self.module.project_validation_errors(contract, ROOT, 'trusted-base')
        self.assertEqual(errors, contract.validation_errors.return_value)
        contract.validation_errors.assert_called_once_with(ROOT, ROOT, check_generated=True,
                                                          protected_base='trusted-base')
        self.assertEqual(contract._project_router.__name__, 'project_router')

if __name__ == '__main__':
    unittest.main()
