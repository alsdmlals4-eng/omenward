from __future__ import annotations

import pathlib
import runpy
import sys
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools"))

from validate_canon_freshness_v45_scope import validate_canon_freshness_scope  # noqa: E402

MODULE = runpy.run_path(str(ROOT / "tools" / "validate_project_core_docs.py"))
validate_project_core = MODULE["validate"]

# Exact retained surface of PR #207. Volatile implementation authority is owned by
# AGENTS routing + Current Decisions + Active Context; durable current consumers do
# not need to be rewritten just to repeat the same live gate. The two validators and
# their mutation tests are included so the transition remains fail-closed.
RUN_COMMAND_AUTHORITY_SYNC_SURFACE = {
    "AGENTS.md",
    "docs/ACTIVE_CONTEXT.md",
    "docs/CURRENT_CONFIRMED_DECISIONS.md",
    "tests/python/test_project_core_docs.py",
    "tests/python/test_run_command_implementation_authority_scope.py",
    "tools/validate_canon_freshness_v45_scope.py",
    "tools/validate_project_core_docs.py",
}


class RunCommandImplementationAuthorityScopeTests(unittest.TestCase):
    def test_exact_authority_sync_surface_is_recognized(self) -> None:
        self.assertEqual([], validate_canon_freshness_scope(RUN_COMMAND_AUTHORITY_SYNC_SURFACE))

    def test_missing_current_decision_index_is_rejected(self) -> None:
        changed = set(RUN_COMMAND_AUTHORITY_SYNC_SURFACE)
        changed.remove("docs/CURRENT_CONFIRMED_DECISIONS.md")
        errors = validate_canon_freshness_scope(changed)
        self.assertTrue(any("missing required" in error for error in errors), errors)

    def test_product_source_is_not_authorized_by_docs_sync(self) -> None:
        changed = set(RUN_COMMAND_AUTHORITY_SYNC_SURFACE)
        changed.add("scripts/core/stage_run.gd")
        errors = validate_canon_freshness_scope(changed)
        self.assertTrue(any("protected product paths" in error for error in errors), errors)

    def test_current_repository_has_scoped_authority_without_runtime_promotion(self) -> None:
        self.assertEqual([], validate_project_core(ROOT))
        decisions = (ROOT / "docs/CURRENT_CONFIRMED_DECISIONS.md").read_text(encoding="utf-8")
        active = (ROOT / "docs/ACTIVE_CONTEXT.md").read_text(encoding="utf-8")
        self.assertIn("IMPLEMENTATION_AUTHORITY = SCOPED_APPROVED", decisions)
        self.assertIn("CURRENT_NEXT = REVIEW_TERRAIN_CANDIDATE_AND_RUN_HUMAN_USABILITY_CHECK", decisions)
        self.assertIn("implementation_scope: SINGLE_MARCH_FRONT_AND_THREE_TAB_COMMAND", active)
        self.assertIn("current_chat_runtime_status: PARTIAL__SINGLE_FRONT_PREPARE_TO_BATTLE_LIVE_CAPTURED__HEADLESS_NATURAL_TUTORIAL_TO_REVIEW_PASS__HUMAN_NOT_RUN", active)
        self.assertNotIn("CURRENT_GODOT_RUNTIME = PASS", active)


if __name__ == "__main__":
    unittest.main()
