"""Approved planning package admission is not runtime or final-art approval."""
import subprocess
import unittest
from pathlib import Path
from tools.validate_canon_freshness_v45_scope import validate_canon_freshness_scope

ROOT = Path(__file__).resolve().parents[2]
ANCHORS = ['docs/design/OMENWARD_REPLAN_AND_MOTION_INTAKE_2026-09-10.md',
           'docs/CURRENT_CONFIRMED_DECISIONS.md', 'docs/ACTIVE_CONTEXT.md']


class ReplanIntegrationScopeTests(unittest.TestCase):
    def test_existing_lean_subset_keeps_its_original_contract(self):
        self.assertEqual(validate_canon_freshness_scope({"AGENTS.md", "docs/BASE_RULES_VERSION.md"}), [])

    def test_exact_candidate_can_be_reviewed_with_authority_anchors(self):
        self.assertEqual([], validate_canon_freshness_scope(ANCHORS + [
            'docs/images/candidates/blueprint-20260911/ward-roster.png']))

    def test_candidate_without_intake_is_not_approved(self):
        self.assertTrue(validate_canon_freshness_scope(ANCHORS[1:] + [
            'docs/images/candidates/blueprint-20260911/ward-roster.png']))

    def test_runtime_siblings_and_unlisted_candidates_remain_closed(self):
        for path in ['scripts/replan/front_run.gd', 'project.godot', 'addons/test.gd',
                     'docs/images/candidates/blueprint-20260911/new.png',
                     'docs/design/../secret.md', 'output/pdf/unknown.pdf']:
            self.assertTrue(validate_canon_freshness_scope(ANCHORS + [path]), path)

    def test_pdf_is_binary_but_markdown_whitespace_stays_checked(self):
        paths = ['output/pdf/OMENWARD_HUMAN_BLUEPRINT_REVIEW_20260911_v3.pdf',
                 'docs/ACTIVE_CONTEXT.md']
        values = subprocess.check_output(['git', 'check-attr', 'diff', 'text', '--', *paths],
                                         cwd=ROOT, text=True).splitlines()
        self.assertEqual(values[:2], [paths[0] + ': diff: unset', paths[0] + ': text: unset'])
        self.assertEqual(values[2:], [paths[1] + ': diff: unspecified', paths[1] + ': text: unspecified'])


if __name__ == '__main__':
    unittest.main()
