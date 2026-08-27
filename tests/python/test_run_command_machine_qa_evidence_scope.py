from __future__ import annotations

import pathlib
import sys
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools"))

from validate_canon_freshness_v45_scope import (  # noqa: E402
    RUN_COMMAND_MACHINE_QA_EVIDENCE_SYNC_ALLOWED_FILES,
    RUN_COMMAND_MACHINE_QA_EVIDENCE_SYNC_REQUIRED_ANCHORS,
    validate_canon_freshness_scope,
)


class RunCommandMachineQaEvidenceScopeTests(unittest.TestCase):
    def test_exact_machine_qa_evidence_surface_passes(self) -> None:
        self.assertEqual([], validate_canon_freshness_scope(RUN_COMMAND_MACHINE_QA_EVIDENCE_SYNC_ALLOWED_FILES))

    def test_missing_active_context_is_rejected(self) -> None:
        changed = set(RUN_COMMAND_MACHINE_QA_EVIDENCE_SYNC_REQUIRED_ANCHORS)
        changed.remove("docs/ACTIVE_CONTEXT.md")
        errors = validate_canon_freshness_scope(changed)
        self.assertTrue(any("missing required" in error for error in errors), errors)

    def test_product_source_is_not_authorized(self) -> None:
        errors = validate_canon_freshness_scope(
            RUN_COMMAND_MACHINE_QA_EVIDENCE_SYNC_ALLOWED_FILES | {"scripts/core/stage_run.gd"}
        )
        self.assertTrue(any("protected product paths" in error for error in errors), errors)

    def test_unrelated_document_is_rejected(self) -> None:
        errors = validate_canon_freshness_scope(
            RUN_COMMAND_MACHINE_QA_EVIDENCE_SYNC_ALLOWED_FILES | {"docs/unrelated.md"}
        )
        self.assertTrue(any("unapproved files" in error for error in errors), errors)


if __name__ == "__main__":
    unittest.main()
