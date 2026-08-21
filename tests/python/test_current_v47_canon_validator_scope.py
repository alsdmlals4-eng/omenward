from __future__ import annotations

import pathlib
import sys
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools"))

from validate_canon_freshness_v45_scope import (  # noqa: E402
    CURRENT_V47_CANON_VALIDATOR_RECONCILIATION_ALLOWED_FILES,
    CURRENT_V47_CANON_VALIDATOR_RECONCILIATION_REQUIRED_ANCHORS,
    validate_canon_freshness_scope,
)


class CurrentV47CanonValidatorScopeTests(unittest.TestCase):
    def test_exact_current_v47_reconciliation_scope_passes(self) -> None:
        changed = set(CURRENT_V47_CANON_VALIDATOR_RECONCILIATION_REQUIRED_ANCHORS)
        changed.update({
            "docs/ACTIVE_CONTEXT.md",
            "docs/DECISIONS_PENDING.md",
            "docs/HANDOFF_CONTEXT.md",
            "docs/OMENWARD_ROADMAP.md",
            "docs/PROJECT_CANON_DECISION_LEDGER.md",
            "tests/python/test_canon_freshness_v45_routing.py",
        })
        self.assertEqual([], validate_canon_freshness_scope(changed))

    def test_missing_current_decision_index_anchor_fails(self) -> None:
        changed = set(CURRENT_V47_CANON_VALIDATOR_RECONCILIATION_REQUIRED_ANCHORS)
        changed.remove("docs/CURRENT_CONFIRMED_DECISIONS.md")
        errors = validate_canon_freshness_scope(changed)
        self.assertTrue(any("missing required" in error for error in errors))

    def test_product_path_is_still_forbidden(self) -> None:
        changed = set(CURRENT_V47_CANON_VALIDATOR_RECONCILIATION_REQUIRED_ANCHORS)
        changed.add("scripts/core/stage_run.gd")
        errors = validate_canon_freshness_scope(changed)
        self.assertTrue(any("protected product paths" in error for error in errors))

    def test_unrelated_file_is_still_forbidden(self) -> None:
        changed = set(CURRENT_V47_CANON_VALIDATOR_RECONCILIATION_REQUIRED_ANCHORS)
        changed.add("docs/random-unrelated.md")
        errors = validate_canon_freshness_scope(changed)
        self.assertTrue(any("unapproved files" in error for error in errors))

    def test_new_mode_is_bounded_to_known_surface(self) -> None:
        self.assertNotIn("scripts/", CURRENT_V47_CANON_VALIDATOR_RECONCILIATION_ALLOWED_FILES)
        self.assertNotIn("scenes/", CURRENT_V47_CANON_VALIDATOR_RECONCILIATION_ALLOWED_FILES)
        self.assertIn("tools/validate_canon_freshness_v45_scope.py", CURRENT_V47_CANON_VALIDATOR_RECONCILIATION_ALLOWED_FILES)
        self.assertIn("tests/python/test_current_canon_reconciliation_20260821.py", CURRENT_V47_CANON_VALIDATOR_RECONCILIATION_ALLOWED_FILES)


if __name__ == "__main__":
    unittest.main()
