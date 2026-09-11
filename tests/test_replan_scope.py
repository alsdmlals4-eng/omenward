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

if __name__ == '__main__':
    unittest.main()
