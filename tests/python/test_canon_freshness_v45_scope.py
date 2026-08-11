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
    ".github/workflows/validate-active-integrated-contract-v4-4.yml", CANON_V45_WORKFLOW, "AGENTS.md",
    "docs/ACTIVE_CONTEXT.md", "docs/CURRENT_IMPLEMENTATION_STATUS.md", "docs/DECISIONS_PENDING.md",
    "docs/DOCUMENTATION_MAP.md", "docs/DOCUMENT_LIFECYCLE_REGISTRY.md", "docs/OMENWARD_GDD_CURRENT_CANON.md",
    "docs/ONBOARDING_PLANNING_CURRENT_AUTHORITY.md", "docs/PROJECT_CANON_DECISION_LEDGER.md", "docs/PROJECT_CORE.md",
    "docs/PROJECT_GOOGLE_SHEET_WORKBOOK.md", "docs/design/APPROVED_OMENWARD_BUILDING_TIER_REALIGNMENT_2026-08-06.md",
    "docs/operations/ACTIVE_INTEGRATED_CONTRACT_STATE.v2.json", "docs/operations/CANON_FRESHNESS_V45_SHEET_SYNC_EVIDENCE_2026-08-11.json",
    "docs/process/ACTIVE_INTEGRATED_CONTRACT_BINDING_2026-08-11.md", "docs/process/APPROVED_OMENWARD_CANON_FRESHNESS_AND_V4_5_THIN_ADAPTER_2026-08-11.md",
    CANONICAL_V45_R2, "docs/superpowers/plans/2026-08-11-canon-freshness-v45-routing.md",
    "tests/python/test_canon_freshness_v45_routing.py", "tests/python/test_canon_freshness_v45_scope.py",
    "tools/validate_canon_freshness_v45_scope.py",
}
PHASE_B_POSTMERGE_FULL_SUITE_REMEDIATION = {
    CORE_WORKFLOW,
    "AGENTS.md",
    "docs/CURRENT_IMPLEMENTATION_STATUS.md",
    "tests/python/test_ci_usage_contract.py",
    "tools/validate_ci_usage_contract.py",
    "tests/python/test_canon_freshness_v45_scope.py",
    "tools/validate_canon_freshness_v45_scope.py",
}
PHASE_C_C0_TOOLCHAIN_GATE = {
    CORE_WORKFLOW,
    "docs/reviews/PHASE_C_C0_PREFLIGHT_2026-08-11.md",
    "docs/superpowers/plans/2026-08-11-phase-c-c0-toolchain-ci-gate.md",
    "tests/python/test_phase_c_c0_toolchain_ci_gate.py",
    "tests/python/test_tool_state_user_approval_remote_sync.py",
    "tools/validate_ci_usage_contract.py",
    "tests/python/test_canon_freshness_v45_scope.py",
    "tools/validate_canon_freshness_v45_scope.py",
}
PHASE_C_C0_LOCAL_HIGODOT_CLOSURE = {
    "docs/ACTIVE_CONTEXT.md",
    "docs/CURRENT_IMPLEMENTATION_STATUS.md",
    "docs/reviews/PHASE_C_C0_LOCAL_HIGODOT_CLOSURE_2026-08-11.md",
    "tests/python/test_canon_freshness_v45_scope.py",
    "tools/validate_canon_freshness_v45_scope.py",
}
POST_C0_CURRENT_ROUTER_RECONCILIATION = {
    "AGENTS.md",
    "README.md",
    "docs/PROJECT_CORE.md",
    "docs/DECISIONS_PENDING.md",
    "docs/OMENWARD_ROADMAP.md",
    "docs/reviews/PHASE_C_C0_LOCAL_HIGODOT_CLOSURE_2026-08-11.md",
    "tests/python/test_canon_freshness_v45_routing.py",
    "tests/python/test_canon_freshness_v45_scope.py",
    "tools/validate_canon_freshness_v45_scope.py",
}
WINDOWS_CANONICAL_EVIDENCE_PORTABILITY = {"tests/python/test_barracks_10000_robustness_execution.py", "tests/python/test_barracks_conditional_fail_remediation.py", "tests/python/test_base_recovery_map.py", "tests/python/test_project_base_adapter_freshness.py", "tests/python/test_git_canonical_evidence.py", "tools/git_canonical_evidence.py", "tests/python/test_canon_freshness_v45_scope.py", "tools/validate_canon_freshness_v45_scope.py"}
POSTMERGE_EVIDENCE_CLOSURE = {"docs/operations/ACTIVE_INTEGRATED_CONTRACT_STATE.v2.json", "docs/operations/CANON_FRESHNESS_V45_SHEET_SYNC_EVIDENCE_2026-08-11.json"}
CURRENT_CONSUMER_RECONCILIATION = {"docs/ACTIVE_CONTEXT.md", "docs/CURRENT_IMPLEMENTATION_STATUS.md", "docs/DECISIONS_PENDING.md", "tests/python/test_canon_freshness_v45_routing.py", "tests/python/test_canon_freshness_v45_scope.py", "tools/validate_canon_freshness_v45_scope.py"}
PHASE_A_READINESS_CLASSIFICATION = {CANON_V45_WORKFLOW, "AGENTS.md", "docs/DECISIONS_PENDING.md", "docs/OMENWARD_GDD_CURRENT_CANON.md", "docs/ONBOARDING_PLANNING_CURRENT_AUTHORITY.md", "docs/PROJECT_GOOGLE_SHEET_WORKBOOK.md", "docs/reviews/PHASE_A_PLANNING_READINESS_DEPENDENCY_CLASSIFICATION_2026-08-11.md", "docs/superpowers/plans/2026-08-11-phase-a-readiness-dependency-classification.md", "tests/python/test_phase_a_readiness_dependency_classification.py", "tests/python/test_canon_freshness_v45_scope.py", "tools/validate_canon_freshness_v45_scope.py"}
CONTENT_CLOSURE_BENCHMARK_FIRST = {
    CANON_V45_WORKFLOW, "AGENTS.md", "docs/ACTIVE_CONTEXT.md", "docs/DECISIONS_PENDING.md",
    "docs/design/APPROVED_OMENWARD_WHOLE_PROJECT_CONTENT_CLOSURE_2026-08-11.md",
    "docs/process/APPROVED_OMENWARD_BENCHMARK_INDUSTRY_RESEARCH_FIRST_2026-08-11.md",
    "docs/superpowers/plans/2026-08-11-content-closure-benchmark-first.md",
    "tests/python/test_content_closure_benchmark_first.py", "tests/python/test_phase_a_readiness_dependency_classification.py",
    "tests/python/test_canon_freshness_v45_scope.py", "tools/validate_canon_freshness_v45_scope.py",
}
QUALITY_GUARDRAILS_ELITE_BOSS_CADENCE = {
    CANON_V45_WORKFLOW, "AGENTS.md", "docs/ACTIVE_CONTEXT.md", "docs/DECISIONS_PENDING.md",
    "docs/design/APPROVED_OMENWARD_QUALITY_GUARDRAILS_2026-08-11.md",
    "docs/design/APPROVED_OMENWARD_ELITE_WAVE_AND_BOSS_CADENCE_2026-08-11.md",
    "docs/superpowers/specs/2026-08-11-quality-guardrails-elite-boss-cadence-design.md",
    "docs/superpowers/plans/2026-08-11-quality-guardrails-elite-boss-cadence.md",
    "tests/python/test_quality_guardrails_elite_boss_cadence.py", "tests/python/test_canon_freshness_v45_scope.py",
    "tools/validate_canon_freshness_v45_scope.py",
}
PHASE_B_FINAL_PLANNING_REVIEW = {
    CANON_V45_WORKFLOW,
    "README.md",
    "AGENTS.md",
    "docs/ACTIVE_CONTEXT.md",
    "docs/CURRENT_IMPLEMENTATION_STATUS.md",
    "docs/DECISIONS_PENDING.md",
    "docs/DOCUMENTATION_MAP.md",
    "docs/DOCUMENT_LIFECYCLE_REGISTRY.md",
    "docs/OMENWARD_GDD_CURRENT_CANON.md",
    "docs/OMENWARD_ROADMAP.md",
    "docs/ONBOARDING_PLANNING_CURRENT_AUTHORITY.md",
    "docs/PROJECT_CORE.md",
    "docs/PROJECT_GOOGLE_SHEET_WORKBOOK.md",
    "docs/operations/ACTIVE_INTEGRATED_CONTRACT_STATE.v2.json",
    "docs/reviews/PHASE_B_FINAL_PLANNING_REVIEW_2026-08-11.md",
    "tests/python/test_canon_freshness_v45_routing.py",
    "tests/python/test_canon_freshness_v45_scope.py",
    "tests/python/test_phase_a_readiness_dependency_classification.py",
    "tests/python/test_content_closure_benchmark_first.py",
    "tests/python/test_quality_guardrails_elite_boss_cadence.py",
    "tests/python/test_phase_b_final_planning_review.py",
    "tools/validate_canon_freshness_v45_scope.py",
}


def load_module():
    spec = importlib.util.spec_from_file_location("canon_v45_scope", TOOL)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class CanonFreshnessV45ScopeTest(unittest.TestCase):
    def test_known_historical_modes_still_pass(self) -> None:
        module = load_module()
        for surface in (
            ACTIVATION,
            PHASE_B_POSTMERGE_FULL_SUITE_REMEDIATION,
            WINDOWS_CANONICAL_EVIDENCE_PORTABILITY,
            POSTMERGE_EVIDENCE_CLOSURE,
            CURRENT_CONSUMER_RECONCILIATION,
            PHASE_A_READINESS_CLASSIFICATION,
            CONTENT_CLOSURE_BENCHMARK_FIRST,
            QUALITY_GUARDRAILS_ELITE_BOSS_CADENCE,
        ):
            self.assertEqual(module.validate_canon_freshness_scope(surface), [])

    def test_phase_c_c0_toolchain_gate_exact_surface_passes(self) -> None:
        self.assertEqual(load_module().validate_canon_freshness_scope(PHASE_C_C0_TOOLCHAIN_GATE), [])

    def test_partial_phase_c_c0_toolchain_gate_surface_is_rejected(self) -> None:
        errors = load_module().validate_canon_freshness_scope(
            PHASE_C_C0_TOOLCHAIN_GATE - {"docs/reviews/PHASE_C_C0_PREFLIGHT_2026-08-11.md"}
        )
        self.assertTrue(any("missing required v4.5 Phase C C0 toolchain gate anchors" in error for error in errors), errors)

    def test_phase_c_c0_local_higodot_closure_exact_surface_passes(self) -> None:
        self.assertEqual(load_module().validate_canon_freshness_scope(PHASE_C_C0_LOCAL_HIGODOT_CLOSURE), [])

    def test_partial_phase_c_c0_local_higodot_closure_is_rejected(self) -> None:
        errors = load_module().validate_canon_freshness_scope(
            PHASE_C_C0_LOCAL_HIGODOT_CLOSURE - {"docs/reviews/PHASE_C_C0_LOCAL_HIGODOT_CLOSURE_2026-08-11.md"}
        )
        self.assertTrue(any("missing required v4.5 Phase C C0 local HiGodot closure anchors" in error for error in errors), errors)

    def test_post_c0_current_router_reconciliation_exact_surface_passes(self) -> None:
        self.assertEqual(load_module().validate_canon_freshness_scope(POST_C0_CURRENT_ROUTER_RECONCILIATION), [])

    def test_partial_post_c0_current_router_reconciliation_is_rejected(self) -> None:
        errors = load_module().validate_canon_freshness_scope(
            POST_C0_CURRENT_ROUTER_RECONCILIATION - {"docs/OMENWARD_ROADMAP.md"}
        )
        self.assertTrue(any("missing required v4.5 post-C0 current-router reconciliation anchors" in error for error in errors), errors)

    def test_phase_b_postmerge_full_suite_exact_surface_passes(self) -> None:
        self.assertEqual(load_module().validate_canon_freshness_scope(PHASE_B_POSTMERGE_FULL_SUITE_REMEDIATION), [])

    def test_partial_phase_b_postmerge_full_suite_surface_is_rejected(self) -> None:
        errors = load_module().validate_canon_freshness_scope(
            PHASE_B_POSTMERGE_FULL_SUITE_REMEDIATION - {"tools/validate_ci_usage_contract.py"}
        )
        self.assertTrue(any("missing required v4.5 Phase B postmerge full-suite remediation anchors" in error for error in errors), errors)

    def test_phase_b_final_review_exact_surface_passes(self) -> None:
        self.assertEqual(load_module().validate_canon_freshness_scope(PHASE_B_FINAL_PLANNING_REVIEW), [])

    def test_partial_phase_b_surface_is_rejected(self) -> None:
        errors = load_module().validate_canon_freshness_scope(PHASE_B_FINAL_PLANNING_REVIEW - {"docs/reviews/PHASE_B_FINAL_PLANNING_REVIEW_2026-08-11.md"})
        self.assertTrue(any("missing required v4.5 Phase B final planning review anchors" in error for error in errors), errors)

    def test_partial_quality_surface_is_rejected(self) -> None:
        errors = load_module().validate_canon_freshness_scope(QUALITY_GUARDRAILS_ELITE_BOSS_CADENCE - {"AGENTS.md"})
        self.assertTrue(any("missing required v4.5 quality guardrails elite boss cadence anchors" in error for error in errors), errors)

    def test_partial_content_closure_surface_is_rejected(self) -> None:
        errors = load_module().validate_canon_freshness_scope(CONTENT_CLOSURE_BENCHMARK_FIRST - {"AGENTS.md"})
        self.assertTrue(any("missing required v4.5 content closure benchmark-first anchors" in error for error in errors), errors)

    def test_product_path_is_rejected(self) -> None:
        errors = load_module().validate_canon_freshness_scope(POST_C0_CURRENT_ROUTER_RECONCILIATION | {"scripts/battle/lane_state.gd"})
        self.assertTrue(any("protected product" in error for error in errors), errors)

    def test_unrelated_file_is_rejected(self) -> None:
        errors = load_module().validate_canon_freshness_scope(POST_C0_CURRENT_ROUTER_RECONCILIATION | {"docs/UNRELATED.md"})
        self.assertTrue(any("unapproved files" in error for error in errors), errors)

    def test_historical_v44_authority_mutation_is_rejected(self) -> None:
        errors = load_module().validate_canon_freshness_scope(PHASE_B_FINAL_PLANNING_REVIEW | {"docs/process/ACTIVE_INTEGRATED_CONTRACT_BINDING_2026-08-06.md"})
        self.assertTrue(any("historical v4.4" in error for error in errors), errors)

    def test_missing_activation_anchor_is_rejected(self) -> None:
        errors = load_module().validate_canon_freshness_scope(ACTIVATION - {CANONICAL_V45_R2})
        self.assertTrue(any("missing required v4.5 activation anchors" in error for error in errors), errors)

    def test_partial_windows_portability_scope_is_rejected(self) -> None:
        errors = load_module().validate_canon_freshness_scope(WINDOWS_CANONICAL_EVIDENCE_PORTABILITY - {"tests/python/test_base_recovery_map.py"})
        self.assertTrue(any("missing required v4.5 Windows canonical evidence portability anchors" in error for error in errors), errors)

    def test_partial_postmerge_closure_is_rejected(self) -> None:
        errors = load_module().validate_canon_freshness_scope({"docs/operations/ACTIVE_INTEGRATED_CONTRACT_STATE.v2.json"})
        self.assertTrue(any("missing required v4.5 postmerge evidence anchors" in error for error in errors), errors)


if __name__ == "__main__":
    unittest.main()
