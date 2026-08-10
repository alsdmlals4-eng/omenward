from __future__ import annotations

import importlib.util
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[2]
TOOL = ROOT / "tools/validate_canon_freshness_v45_scope.py"

APPROVED = {
    ".github/workflows/validate-active-integrated-contract-v4-4.yml",
    ".github/workflows/validate-canon-freshness-v4-5.yml",
    "AGENTS.md",
    "docs/ACTIVE_CONTEXT.md",
    "docs/CURRENT_IMPLEMENTATION_STATUS.md",
    "docs/DECISIONS_PENDING.md",
    "docs/DOCUMENTATION_MAP.md",
    "docs/DOCUMENT_LIFECYCLE_REGISTRY.md",
    "docs/OMENWARD_GDD_CURRENT_CANON.md",
    "docs/PROJECT_CANON_DECISION_LEDGER.md",
    "docs/PROJECT_CORE.md",
    "docs/PROJECT_GOOGLE_SHEET_WORKBOOK.md",
    "docs/operations/ACTIVE_INTEGRATED_CONTRACT_STATE.v2.json",
    "docs/operations/CANON_FRESHNESS_V45_SHEET_SYNC_EVIDENCE_2026-08-11.json",
    "docs/process/ACTIVE_INTEGRATED_CONTRACT_BINDING_2026-08-11.md",
    "docs/process/APPROVED_OMENWARD_CANON_FRESHNESS_AND_V4_5_THIN_ADAPTER_2026-08-11.md",
    "docs/superpowers/plans/2026-08-11-canon-freshness-v45-routing.md",
    "tests/python/test_canon_freshness_v45_routing.py",
    "tests/python/test_canon_freshness_v45_scope.py",
    "tools/validate_canon_freshness_v45_scope.py",
}


def load_module():
    if not TOOL.is_file():
        return None
    spec = importlib.util.spec_from_file_location("canon_v45_scope", TOOL)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class CanonFreshnessV45ScopeTest(unittest.TestCase):
    def test_approved_planning_surface_passes(self) -> None:
        self.assertTrue(TOOL.is_file(), "v4.5 scope classifier must exist")
        module = load_module()
        self.assertEqual(module.validate_canon_freshness_scope(APPROVED), [])

    def test_product_path_is_rejected(self) -> None:
        self.assertTrue(TOOL.is_file(), "v4.5 scope classifier must exist")
        module = load_module()
        errors = module.validate_canon_freshness_scope(APPROVED | {"scripts/battle/lane_state.gd"})
        self.assertTrue(any("protected product" in error for error in errors), errors)

    def test_unrelated_file_is_rejected(self) -> None:
        self.assertTrue(TOOL.is_file(), "v4.5 scope classifier must exist")
        module = load_module()
        errors = module.validate_canon_freshness_scope(APPROVED | {"README.md"})
        self.assertTrue(any("unapproved files" in error for error in errors), errors)

    def test_historical_v44_authority_mutation_is_rejected(self) -> None:
        self.assertTrue(TOOL.is_file(), "v4.5 scope classifier must exist")
        module = load_module()
        errors = module.validate_canon_freshness_scope(
            APPROVED | {
                "docs/process/ACTIVE_INTEGRATED_CONTRACT_BINDING_2026-08-06.md",
                "docs/operations/ACTIVE_INTEGRATED_CONTRACT_STATE.v1.json",
            }
        )
        self.assertTrue(any("historical v4.4" in error for error in errors), errors)

    def test_missing_v45_anchor_is_rejected(self) -> None:
        self.assertTrue(TOOL.is_file(), "v4.5 scope classifier must exist")
        module = load_module()
        without_binding = APPROVED - {"docs/process/ACTIVE_INTEGRATED_CONTRACT_BINDING_2026-08-11.md"}
        errors = module.validate_canon_freshness_scope(without_binding)
        self.assertTrue(any("missing required v4.5 anchors" in error for error in errors), errors)


if __name__ == "__main__":
    unittest.main()
