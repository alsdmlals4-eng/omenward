from __future__ import annotations

import pathlib
import sys
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools"))

from validate_canon_freshness_v45_scope import validate_canon_freshness_scope  # noqa: E402

CURRENT_V48_ORCHESTRATION_PLAN_SURFACE = {
    "docs/ACTIVE_CONTEXT.md",
    "docs/CURRENT_CONFIRMED_DECISIONS.md",
    "docs/CURRENT_IMPLEMENTATION_STATUS.md",
    "docs/design/APPROVED_OMENWARD_ORCHESTRATION_FIRST_VERTICAL_SLICE_IMPLEMENTATION_ARCHITECTURE_2026-08-24.md",
    "docs/reviews/ORCHESTRATION_FIRST_VSLICE_PLANNING_ADVERSARIAL_REVIEW_2026-08-24.md",
    "docs/superpowers/plans/2026-08-24-omenward-orchestration-first-vertical-slice.md",
    "tests/python/test_current_canon_reconciliation_20260821.py",
    "tests/python/test_current_v48_orchestration_plan_scope.py",
    "tests/python/test_project_core_docs.py",
    "tools/validate_canon_freshness_v45_scope.py",
    "tools/validate_project_core_docs.py",
}


class CurrentV48OrchestrationPlanScopeTests(unittest.TestCase):
    def test_exact_orchestration_planning_surface_passes(self) -> None:
        self.assertEqual([], validate_canon_freshness_scope(CURRENT_V48_ORCHESTRATION_PLAN_SURFACE))

    def test_missing_architecture_owner_is_rejected(self) -> None:
        changed = set(CURRENT_V48_ORCHESTRATION_PLAN_SURFACE)
        changed.remove(
            "docs/design/APPROVED_OMENWARD_ORCHESTRATION_FIRST_VERTICAL_SLICE_IMPLEMENTATION_ARCHITECTURE_2026-08-24.md"
        )
        errors = validate_canon_freshness_scope(changed)
        self.assertTrue(any("missing required" in error for error in errors), errors)

    def test_missing_implementation_plan_is_rejected(self) -> None:
        changed = set(CURRENT_V48_ORCHESTRATION_PLAN_SURFACE)
        changed.remove("docs/superpowers/plans/2026-08-24-omenward-orchestration-first-vertical-slice.md")
        errors = validate_canon_freshness_scope(changed)
        self.assertTrue(any("missing required" in error for error in errors), errors)

    def test_missing_current_decision_index_is_rejected(self) -> None:
        changed = set(CURRENT_V48_ORCHESTRATION_PLAN_SURFACE)
        changed.remove("docs/CURRENT_CONFIRMED_DECISIONS.md")
        errors = validate_canon_freshness_scope(changed)
        self.assertTrue(any("missing required" in error for error in errors), errors)

    def test_missing_current_implementation_status_is_rejected(self) -> None:
        changed = set(CURRENT_V48_ORCHESTRATION_PLAN_SURFACE)
        changed.remove("docs/CURRENT_IMPLEMENTATION_STATUS.md")
        errors = validate_canon_freshness_scope(changed)
        self.assertTrue(any("missing required" in error for error in errors), errors)

    def test_product_runtime_path_remains_forbidden(self) -> None:
        changed = set(CURRENT_V48_ORCHESTRATION_PLAN_SURFACE)
        changed.add("scripts/core/stage_run.gd")
        errors = validate_canon_freshness_scope(changed)
        self.assertTrue(any("protected product paths" in error for error in errors), errors)

    def test_unrelated_file_remains_forbidden(self) -> None:
        changed = set(CURRENT_V48_ORCHESTRATION_PLAN_SURFACE)
        changed.add("docs/random-unrelated.md")
        errors = validate_canon_freshness_scope(changed)
        self.assertTrue(any("unapproved files" in error for error in errors), errors)


if __name__ == "__main__":
    unittest.main()
