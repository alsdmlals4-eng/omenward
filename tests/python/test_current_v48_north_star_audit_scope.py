from __future__ import annotations

import pathlib
import sys
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools"))

from validate_canon_freshness_v45_scope import validate_canon_freshness_scope  # noqa: E402

CURRENT_V48_NORTH_STAR_AUDIT_SURFACE = {
    "AGENTS.md",
    "README.md",
    "docs/ACTIVE_CONTEXT.md",
    "docs/CURRENT_CONFIRMED_DECISIONS.md",
    "docs/CURRENT_IMPLEMENTATION_STATUS.md",
    "docs/DECISIONS_PENDING.md",
    "docs/DOCUMENTATION_MAP.md",
    "docs/DOCUMENT_LIFECYCLE_REGISTRY.md",
    "docs/HANDOFF_CONTEXT.md",
    "docs/OMENWARD_GDD_CURRENT_CANON.md",
    "docs/OMENWARD_ROADMAP.md",
    "docs/ONBOARDING_PLANNING_CURRENT_AUTHORITY.md",
    "docs/PROJECT_CANON_DECISION_LEDGER.md",
    "docs/PROJECT_CORE.md",
    "docs/design/APPROVED_OMENWARD_NORTH_STAR_V2_1_AUDIT_AND_CORRECTION_BRIEF_2026-08-24.md",
    "docs/design/APPROVED_OMENWARD_VISUAL_STYLE_AND_COMPONENT_CONTRACT_2026-08-20.md",
    "tests/python/test_canon_freshness_v45_routing.py",
    "tests/python/test_content_closure_benchmark_first.py",
    "tests/python/test_current_canon_reconciliation_20260821.py",
    "tests/python/test_current_v48_north_star_audit_scope.py",
    "tests/python/test_phase_b_final_planning_review.py",
    "tests/python/test_project_core_docs.py",
    "tools/validate_canon_freshness_v45_scope.py",
    "tools/validate_project_core_docs.py",
}


class CurrentV48NorthStarAuditScopeTests(unittest.TestCase):
    def test_exact_v48_north_star_audit_reconciliation_surface_passes(self) -> None:
        self.assertEqual([], validate_canon_freshness_scope(CURRENT_V48_NORTH_STAR_AUDIT_SURFACE))

    def test_missing_current_decision_index_is_rejected(self) -> None:
        changed = set(CURRENT_V48_NORTH_STAR_AUDIT_SURFACE)
        changed.remove("docs/CURRENT_CONFIRMED_DECISIONS.md")
        errors = validate_canon_freshness_scope(changed)
        self.assertTrue(any("missing required" in error for error in errors), errors)

    def test_missing_north_star_audit_owner_is_rejected(self) -> None:
        changed = set(CURRENT_V48_NORTH_STAR_AUDIT_SURFACE)
        changed.remove("docs/design/APPROVED_OMENWARD_NORTH_STAR_V2_1_AUDIT_AND_CORRECTION_BRIEF_2026-08-24.md")
        errors = validate_canon_freshness_scope(changed)
        self.assertTrue(any("missing required" in error for error in errors), errors)

    def test_missing_onboarding_current_consumer_is_rejected(self) -> None:
        changed = set(CURRENT_V48_NORTH_STAR_AUDIT_SURFACE)
        changed.remove("docs/ONBOARDING_PLANNING_CURRENT_AUTHORITY.md")
        errors = validate_canon_freshness_scope(changed)
        self.assertTrue(any("missing required" in error for error in errors), errors)

    def test_product_runtime_path_remains_forbidden(self) -> None:
        changed = set(CURRENT_V48_NORTH_STAR_AUDIT_SURFACE)
        changed.add("scripts/core/stage_run.gd")
        errors = validate_canon_freshness_scope(changed)
        self.assertTrue(any("protected product paths" in error for error in errors), errors)

    def test_unrelated_file_remains_forbidden(self) -> None:
        changed = set(CURRENT_V48_NORTH_STAR_AUDIT_SURFACE)
        changed.add("docs/random-unrelated.md")
        errors = validate_canon_freshness_scope(changed)
        self.assertTrue(any("unapproved files" in error for error in errors), errors)


if __name__ == "__main__":
    unittest.main()
