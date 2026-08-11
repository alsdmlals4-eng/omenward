from __future__ import annotations

import importlib.util
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[2]
TOOL = ROOT / "tools/validate_canon_freshness_v45_scope.py"
CANONICAL_V45_R2 = "docs/process/PROJECT_TOTAL_PLANNING_IMPLEMENTATION_AND_DELIVERY_INSTRUCTION_v4.5_r2.md"
CORE_WORKFLOW = ".github/workflows/validate-omenward-core.yml"
CANON_V45_WORKFLOW = ".github/workflows/validate-canon-freshness-v4-5.yml"

ACTIVATION = {
    ".github/workflows/validate-active-integrated-contract-v4-4.yml", CANON_V45_WORKFLOW,
    "AGENTS.md", "docs/ACTIVE_CONTEXT.md", "docs/CURRENT_IMPLEMENTATION_STATUS.md", "docs/DECISIONS_PENDING.md",
    "docs/DOCUMENTATION_MAP.md", "docs/DOCUMENT_LIFECYCLE_REGISTRY.md", "docs/OMENWARD_GDD_CURRENT_CANON.md",
    "docs/ONBOARDING_PLANNING_CURRENT_AUTHORITY.md", "docs/PROJECT_CANON_DECISION_LEDGER.md", "docs/PROJECT_CORE.md",
    "docs/PROJECT_GOOGLE_SHEET_WORKBOOK.md", "docs/design/APPROVED_OMENWARD_BUILDING_TIER_REALIGNMENT_2026-08-06.md",
    "docs/operations/ACTIVE_INTEGRATED_CONTRACT_STATE.v2.json",
    "docs/operations/CANON_FRESHNESS_V45_SHEET_SYNC_EVIDENCE_2026-08-11.json",
    "docs/process/ACTIVE_INTEGRATED_CONTRACT_BINDING_2026-08-11.md",
    "docs/process/APPROVED_OMENWARD_CANON_FRESHNESS_AND_V4_5_THIN_ADAPTER_2026-08-11.md",
    CANONICAL_V45_R2, "docs/superpowers/plans/2026-08-11-canon-freshness-v45-routing.md",
    "tests/python/test_canon_freshness_v45_routing.py", "tests/python/test_canon_freshness_v45_scope.py",
    "tools/validate_canon_freshness_v45_scope.py",
}
POSTMERGE_CI_REMEDIATION = {CORE_WORKFLOW, "tests/python/test_ci_usage_contract.py", "tools/validate_ci_usage_contract.py", "tests/python/test_canon_freshness_v45_scope.py", "tools/validate_canon_freshness_v45_scope.py"}
WINDOWS_CANONICAL_EVIDENCE_PORTABILITY = {"tests/python/test_barracks_10000_robustness_execution.py", "tests/python/test_barracks_conditional_fail_remediation.py", "tests/python/test_base_recovery_map.py", "tests/python/test_project_base_adapter_freshness.py", "tests/python/test_git_canonical_evidence.py", "tools/git_canonical_evidence.py", "tests/python/test_canon_freshness_v45_scope.py", "tools/validate_canon_freshness_v45_scope.py"}
POSTMERGE_EVIDENCE_CLOSURE = {"docs/operations/ACTIVE_INTEGRATED_CONTRACT_STATE.v2.json", "docs/operations/CANON_FRESHNESS_V45_SHEET_SYNC_EVIDENCE_2026-08-11.json"}
CURRENT_CONSUMER_RECONCILIATION = {"docs/ACTIVE_CONTEXT.md", "docs/CURRENT_IMPLEMENTATION_STATUS.md", "docs/DECISIONS_PENDING.md", "tests/python/test_canon_freshness_v45_routing.py", "tests/python/test_canon_freshness_v45_scope.py", "tools/validate_canon_freshness_v45_scope.py"}
PHASE_A_READINESS_CLASSIFICATION = {CANON_V45_WORKFLOW, "AGENTS.md", "docs/DECISIONS_PENDING.md", "docs/OMENWARD_GDD_CURRENT_CANON.md", "docs/ONBOARDING_PLANNING_CURRENT_AUTHORITY.md", "docs/PROJECT_GOOGLE_SHEET_WORKBOOK.md", "docs/reviews/PHASE_A_PLANNING_READINESS_DEPENDENCY_CLASSIFICATION_2026-08-11.md", "docs/superpowers/plans/2026-08-11-phase-a-readiness-dependency-classification.md", "tests/python/test_phase_a_readiness_dependency_classification.py", "tests/python/test_canon_freshness_v45_scope.py", "tools/validate_canon_freshness_v45_scope.py"}
PHASE_A_WHOLE_PROJECT_OPEN_CONTENT = {
    CANON_V45_WORKFLOW, "AGENTS.md", "docs/ACTIVE_CONTEXT.md", "docs/CURRENT_IMPLEMENTATION_STATUS.md",
    "docs/DECISIONS_PENDING.md", "docs/PROJECT_CORE.md",
    "docs/reviews/PHASE_A_WHOLE_PROJECT_OPEN_CONTENT_INVENTORY_2026-08-11.md",
    "docs/superpowers/plans/2026-08-11-phase-a-whole-project-open-content-inventory.md",
    "tests/python/test_phase_a_whole_project_open_content_inventory.py", "tests/python/test_canon_freshness_v45_scope.py",
    "tools/validate_canon_freshness_v45_scope.py",
}


def load_module():
    spec = importlib.util.spec_from_file_location("canon_v45_scope", TOOL)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class CanonFreshnessV45ScopeTest(unittest.TestCase):
    def test_activation_surface_passes(self): self.assertEqual(load_module().validate_canon_freshness_scope(ACTIVATION), [])
    def test_postmerge_ci_remediation_surface_passes(self): self.assertEqual(load_module().validate_canon_freshness_scope(POSTMERGE_CI_REMEDIATION), [])
    def test_windows_canonical_evidence_portability_surface_passes(self): self.assertEqual(load_module().validate_canon_freshness_scope(WINDOWS_CANONICAL_EVIDENCE_PORTABILITY), [])
    def test_postmerge_evidence_closure_surface_passes(self): self.assertEqual(load_module().validate_canon_freshness_scope(POSTMERGE_EVIDENCE_CLOSURE), [])
    def test_current_consumer_reconciliation_surface_passes(self): self.assertEqual(load_module().validate_canon_freshness_scope(CURRENT_CONSUMER_RECONCILIATION), [])
    def test_phase_a_readiness_classification_surface_passes(self): self.assertEqual(load_module().validate_canon_freshness_scope(PHASE_A_READINESS_CLASSIFICATION), [])
    def test_phase_a_whole_project_open_content_surface_passes(self): self.assertEqual(load_module().validate_canon_freshness_scope(PHASE_A_WHOLE_PROJECT_OPEN_CONTENT), [])
    def test_product_path_is_rejected(self): self.assertTrue(any("protected product" in e for e in load_module().validate_canon_freshness_scope(ACTIVATION | {"scripts/battle/lane_state.gd"})))
    def test_unrelated_file_is_rejected(self): self.assertTrue(any("unapproved files" in e for e in load_module().validate_canon_freshness_scope(ACTIVATION | {"README.md"})))
    def test_historical_v44_authority_mutation_is_rejected(self): self.assertTrue(any("historical v4.4" in e for e in load_module().validate_canon_freshness_scope(ACTIVATION | {"docs/process/ACTIVE_INTEGRATED_CONTRACT_BINDING_2026-08-06.md", "docs/operations/ACTIVE_INTEGRATED_CONTRACT_STATE.v1.json"})))
    def test_missing_v45_anchor_is_rejected(self): self.assertTrue(any("missing required v4.5 activation anchors" in e for e in load_module().validate_canon_freshness_scope(ACTIVATION - {"docs/process/ACTIVE_INTEGRATED_CONTRACT_BINDING_2026-08-11.md"})))
    def test_repo_canonical_v45_r2_is_required_activation_anchor(self): self.assertTrue(any("missing required v4.5 activation anchors" in e for e in load_module().validate_canon_freshness_scope(ACTIVATION - {CANONICAL_V45_R2})))
    def test_partial_windows_portability_scope_is_rejected(self): self.assertTrue(any("missing required v4.5 Windows canonical evidence portability anchors" in e for e in load_module().validate_canon_freshness_scope(WINDOWS_CANONICAL_EVIDENCE_PORTABILITY - {"tests/python/test_base_recovery_map.py"})))
    def test_partial_postmerge_closure_is_rejected(self): self.assertTrue(any("missing required v4.5 postmerge evidence anchors" in e for e in load_module().validate_canon_freshness_scope({"docs/operations/ACTIVE_INTEGRATED_CONTRACT_STATE.v2.json"})))
    def test_partial_current_consumer_reconciliation_scope_is_rejected(self): self.assertTrue(any("missing required v4.5 current consumer reconciliation anchors" in e for e in load_module().validate_canon_freshness_scope(CURRENT_CONSUMER_RECONCILIATION - {"tests/python/test_canon_freshness_v45_routing.py"})))
    def test_partial_phase_a_readiness_classification_scope_is_rejected(self): self.assertTrue(any("missing required v4.5 Phase A readiness classification anchors" in e for e in load_module().validate_canon_freshness_scope(PHASE_A_READINESS_CLASSIFICATION - {"tests/python/test_phase_a_readiness_dependency_classification.py"})))
    def test_partial_phase_a_whole_project_open_content_scope_is_rejected(self): self.assertTrue(any("missing required v4.5 Phase A whole-project open-content anchors" in e for e in load_module().validate_canon_freshness_scope(PHASE_A_WHOLE_PROJECT_OPEN_CONTENT - {"tests/python/test_phase_a_whole_project_open_content_inventory.py"})))


if __name__ == "__main__": unittest.main()
