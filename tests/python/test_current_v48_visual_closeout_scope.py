from __future__ import annotations

import importlib.util
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[2]
TOOL = ROOT / "tools/validate_canon_freshness_v45_scope.py"

VISUAL_CLOSEOUT = {
    "AGENTS.md",
    "docs/ACTIVE_CONTEXT.md",
    "docs/CURRENT_CONFIRMED_DECISIONS.md",
    "docs/CURRENT_IMPLEMENTATION_STATUS.md",
    "docs/HANDOFF_CONTEXT.md",
    "docs/OMENWARD_GDD_CURRENT_CANON.md",
    "docs/PROJECT_CORE.md",
    "docs/handoffs/2026-08-25-front-state-visual-approved-closeout.md",
    "docs/handoffs/2026-08-25-front-state-visual-receiver-ack.md",
    "docs/images/planning/canonical/OMENWARD_APPROVED_FRONT_STATE_VISUAL_2026-08-25.md",
    "docs/superpowers/specs/2026-08-25-front-state-minimap-sd-fantasy-design.md",
    "tests/python/test_canon_freshness_v45_routing.py",
    "tests/python/test_current_canon_reconciliation_20260821.py",
    "tests/python/test_current_v48_visual_closeout_scope.py",
    "tests/python/test_project_core_docs.py",
    "tools/validate_canon_freshness_v45_scope.py",
    "tools/validate_project_core_docs.py",
}


def load_module():
    spec = importlib.util.spec_from_file_location("canon_v45_scope", TOOL)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class CurrentV48VisualCloseoutScopeTests(unittest.TestCase):
    def test_exact_visual_closeout_surface_passes(self) -> None:
        self.assertEqual([], load_module().validate_canon_freshness_scope(VISUAL_CLOSEOUT))

    def test_partial_visual_closeout_is_rejected(self) -> None:
        errors = load_module().validate_canon_freshness_scope(
            VISUAL_CLOSEOUT - {"docs/handoffs/2026-08-25-front-state-visual-approved-closeout.md"}
        )
        self.assertTrue(any("missing required v4.5 current v4.8 visual closeout anchors" in error for error in errors), errors)

    def test_receiver_ack_is_required_after_transfer_acceptance(self) -> None:
        errors = load_module().validate_canon_freshness_scope(
            VISUAL_CLOSEOUT - {"docs/handoffs/2026-08-25-front-state-visual-receiver-ack.md"}
        )
        self.assertTrue(any("missing required v4.5 current v4.8 visual closeout anchors" in error for error in errors), errors)

    def test_current_canon_consumer_is_required(self) -> None:
        errors = load_module().validate_canon_freshness_scope(
            VISUAL_CLOSEOUT - {"tests/python/test_current_canon_reconciliation_20260821.py"}
        )
        self.assertTrue(any("missing required v4.5 current v4.8 visual closeout anchors" in error for error in errors), errors)

    def test_product_source_remains_forbidden(self) -> None:
        errors = load_module().validate_canon_freshness_scope(VISUAL_CLOSEOUT | {"scripts/core/stage_run.gd"})
        self.assertTrue(any("protected product paths" in error for error in errors), errors)

    def test_unrelated_document_remains_forbidden(self) -> None:
        errors = load_module().validate_canon_freshness_scope(VISUAL_CLOSEOUT | {"docs/UNRELATED.md"})
        self.assertTrue(any("unapproved files" in error for error in errors), errors)


if __name__ == "__main__":
    unittest.main()
