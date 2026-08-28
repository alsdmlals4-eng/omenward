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
POST_C0_FULL_CURRENT_CONSUMER_CLOSURE = {
    "docs/DOCUMENTATION_MAP.md",
    "docs/PROJECT_GOOGLE_SHEET_WORKBOOK.md",
    "docs/DOCUMENT_LIFECYCLE_REGISTRY.md",
    "docs/ONBOARDING_PLANNING_CURRENT_AUTHORITY.md",
    "docs/OMENWARD_GDD_CURRENT_CANON.md",
    "docs/process/ACTIVE_INTEGRATED_CONTRACT_BINDING_2026-08-11.md",
    "docs/operations/ACTIVE_INTEGRATED_CONTRACT_STATE.v2.json",
    "docs/PROJECT_CANON_DECISION_LEDGER.md",
    "tests/python/test_canon_freshness_v45_routing.py",
    "tests/python/test_canon_freshness_v45_scope.py",
    "tools/validate_canon_freshness_v45_scope.py",
}
POST_C0_TRANSIENT_OPS_STATE_DECOUPLING = {
    "docs/reviews/PHASE_C_C0_LOCAL_HIGODOT_CLOSURE_2026-08-11.md",
    "docs/PROJECT_GOOGLE_SHEET_WORKBOOK.md",
    "docs/operations/ACTIVE_INTEGRATED_CONTRACT_STATE.v2.json",
    "docs/PROJECT_CANON_DECISION_LEDGER.md",
    "tests/python/test_canon_freshness_v45_routing.py",
    "tests/python/test_canon_freshness_v45_scope.py",
    "tools/validate_canon_freshness_v45_scope.py",
}
WINDOWS_CANONICAL_EVIDENCE_PORTABILITY = {"tests/python/test_barracks_10000_robustness_execution.py", "tests/python/test_barracks_conditional_fail_remediation.py", "tests/python/test_base_recovery_map.py", "tests/python/test_project_base_adapter_freshness.py", "tests/python/test_git_canonical_evidence.py", "tools/git_canonical_evidence.py", "tests/python/test_canon_freshness_v45_scope.py", "tools/validate_canon_freshness_v45_scope.py"}
POSTMERGE_EVIDENCE_CLOSURE = {"docs/operations/ACTIVE_INTEGRATED_CONTRACT_STATE.v2.json", "docs/operations/CANON_FRESHNESS_V45_SHEET_SYNC_EVIDENCE_2026-08-11.json"}
CURRENT_CONSUMER_RECONCILIATION = {
    "docs/ACTIVE_CONTEXT.md",
    "docs/CURRENT_IMPLEMENTATION_STATUS.md",
    "docs/DECISIONS_PENDING.md",
    "docs/HANDOFF_CONTEXT.md",
    "tests/python/test_canon_freshness_v45_routing.py",
    "tests/python/test_canon_freshness_v45_scope.py",
    "tools/validate_canon_freshness_v45_scope.py",
}
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


# A narrowly bounded repair surface for current-state metadata only. It must not
# re-open the completed visual-closeout package or permit product paths.
CURRENT_MAIN_ROUTER_HANDOFF_SYNC = {
    "docs/DECISIONS_PENDING.md",
    "docs/HANDOFF_CONTEXT.md",
    "tests/python/test_current_v48_router_sync.py",
    "tests/python/test_quality_guardrails_elite_boss_cadence.py",
    "tests/python/test_phase_b_final_planning_review.py",
    "tests/python/test_canon_freshness_v45_scope.py",
    "tools/validate_canon_freshness_v45_scope.py",
}

SCREEN_SURFACE_COVERAGE_AUDIT = {
    ".github/workflows/validate-active-integrated-contract-v4-4.yml",
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
    "docs/PROJECT_CANON_DECISION_LEDGER.md",
    "docs/PROJECT_CORE.md",
    "docs/design/OMENWARD_TARGET_SCREEN_SURFACE_AND_VISUAL_COVERAGE_AUDIT_2026-08-27.md",
    "tests/python/test_bca_visual_sheet_adoption.py",
    "tests/python/test_c3_core_ux_contract.py",
    "tests/python/test_canon_freshness_v45_routing.py",
    "tests/python/test_canon_freshness_v45_scope.py",
    "tests/python/test_content_closure_benchmark_first.py",
    "tests/python/test_current_canon_reconciliation_20260821.py",
    "tests/python/test_current_v48_router_sync.py",
    "tests/python/test_phase_b_final_planning_review.py",
    "tests/python/test_project_core_docs.py",
    "tests/python/test_run_command_implementation_authority_scope.py",
    "tools/validate_c1_roulette.py",
    "tools/validate_c2_battle_objective.py",
    "tools/validate_c3_core_ux.py",
    "tools/validate_canon_freshness_v45_scope.py",
    "tools/validate_project_core_docs.py",
}

# The 2026-08-28 audit repairs current router drift after the approved
# battlefield/roulette presentation evidence. It is documentation and contract
# coverage only; no product code, Scene, Resource, or runtime asset path is
# permitted.
CANON_PLAY_VISUAL_AUDIT = {
    "README.md",
    "docs/ACTIVE_CONTEXT.md",
    "docs/CURRENT_IMPLEMENTATION_STATUS.md",
    "docs/DECISIONS_PENDING.md",
    "docs/DOCUMENTATION_MAP.md",
    "docs/DOCUMENT_LIFECYCLE_REGISTRY.md",
    "docs/OMENWARD_GDD_CURRENT_CANON.md",
    "docs/OMENWARD_ROADMAP.md",
    "docs/PROJECT_CANON_DECISION_LEDGER.md",
    "docs/PROJECT_CORE.md",
    "docs/analysis/ui/current_roulette_ddd_feedback.v1.json",
    "docs/audits/OMENWARD_CANON_PLAY_EXPERIENCE_VISUAL_AUDIT_2026-08-28.md",
    "docs/images/planning/OMENWARD_UNIT_ANIMATION_PRODUCTION_CONTRACT_2026-08-26.md",
    "tests/python/test_canon_freshness_v45_routing.py",
    "tests/python/test_canon_freshness_v45_scope.py",
    "tests/python/test_content_closure_benchmark_first.py",
    "tests/python/test_current_canon_reconciliation_20260821.py",
    "tests/python/test_current_v48_router_sync.py",
    "tests/python/test_run_command_implementation_authority_scope.py",
    "tools/validate_canon_freshness_v45_scope.py",
}

STORYBOOK_SD_THREE_FRONT_STRATEGIC_MAP_DIRECTION_LOCK = {
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
    "docs/PROJECT_CANON_DECISION_LEDGER.md",
    "docs/PROJECT_CORE.md",
    "docs/audits/OMENWARD_CANON_PLAY_EXPERIENCE_VISUAL_AUDIT_2026-08-28.md",
    "docs/design/OMENWARD_GAME_SCREEN_AND_IMAGE_COVERAGE_2026-08-28.md",
    "docs/images/approved/OMENWARD_BATTLEFIELD_BACKDROP_V1.md",
    "docs/images/planning/OMENWARD_PROJECT_CORE_SCENE_VISUAL_BOARD_2026-08-28.md",
    "docs/images/planning/generated/OMENWARD_PROJECT_CORE_SCENE_VISUAL_BOARD_2026-08-28_v1.png",
    "docs/superpowers/specs/2026-08-28-battlefield-map-and-roulette-picker-design.md",
    "docs/superpowers/specs/2026-08-28-storybook-sd-three-front-strategic-map-design.md",
    "tests/python/test_canon_freshness_v45_routing.py",
    "tests/python/test_canon_freshness_v45_scope.py",
    "tests/python/test_content_closure_benchmark_first.py",
    "tests/python/test_current_canon_reconciliation_20260821.py",
    "tests/python/test_current_v48_router_sync.py",
    "tests/python/test_project_core_docs.py",
    "tests/python/test_run_command_implementation_authority_scope.py",
    "tools/validate_canon_freshness_v45_scope.py",
    "tools/validate_project_core_docs.py",
}

ONE_WARD_CITADEL_THREE_BRANCHES_CORRECTION = {
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
    "docs/PROJECT_CANON_DECISION_LEDGER.md",
    "docs/PROJECT_CORE.md",
    "docs/design/OMENWARD_GAME_SCREEN_AND_IMAGE_COVERAGE_2026-08-28.md",
    "docs/images/approved/OMENWARD_BATTLEFIELD_BACKDROP_V1.md",
    "docs/images/planning/OMENWARD_PROJECT_CORE_SCENE_VISUAL_BOARD_2026-08-28.md",
    "docs/images/planning/generated/OMENWARD_PROJECT_CORE_SCENE_VISUAL_BOARD_2026-08-28_v2_BRANCHING.png",
    "docs/superpowers/specs/2026-08-28-battlefield-map-and-roulette-picker-design.md",
    "docs/superpowers/specs/2026-08-28-storybook-sd-three-front-strategic-map-design.md",
    "tests/python/test_canon_freshness_v45_routing.py",
    "tests/python/test_canon_freshness_v45_scope.py",
    "tests/python/test_current_canon_reconciliation_20260821.py",
    "tests/python/test_current_v48_router_sync.py",
    "tools/validate_canon_freshness_v45_scope.py",
    "tools/validate_project_core_docs.py",
}

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

    def test_current_consumer_reconciliation_requires_handoff(self) -> None:
        module = load_module()
        self.assertEqual(module.validate_canon_freshness_scope(CURRENT_CONSUMER_RECONCILIATION), [])
        errors = module.validate_canon_freshness_scope(CURRENT_CONSUMER_RECONCILIATION - {"docs/HANDOFF_CONTEXT.md"})
        self.assertTrue(any("missing required v4.5 current consumer reconciliation anchors" in error for error in errors), errors)

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

    def test_post_c0_full_current_consumer_closure_exact_surface_passes(self) -> None:
        self.assertEqual(load_module().validate_canon_freshness_scope(POST_C0_FULL_CURRENT_CONSUMER_CLOSURE), [])

    def test_partial_post_c0_full_current_consumer_closure_is_rejected(self) -> None:
        errors = load_module().validate_canon_freshness_scope(
            POST_C0_FULL_CURRENT_CONSUMER_CLOSURE - {"docs/PROJECT_CANON_DECISION_LEDGER.md"}
        )
        self.assertTrue(any("missing required v4.5 post-C0 full current-consumer closure anchors" in error for error in errors), errors)

    def test_post_c0_transient_ops_state_decoupling_exact_surface_passes(self) -> None:
        self.assertEqual(load_module().validate_canon_freshness_scope(POST_C0_TRANSIENT_OPS_STATE_DECOUPLING), [])

    def test_partial_post_c0_transient_ops_state_decoupling_is_rejected(self) -> None:
        errors = load_module().validate_canon_freshness_scope(
            POST_C0_TRANSIENT_OPS_STATE_DECOUPLING - {"docs/PROJECT_GOOGLE_SHEET_WORKBOOK.md"}
        )
        self.assertTrue(any("missing required v4.5 post-C0 transient ops-state decoupling anchors" in error for error in errors), errors)

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
        errors = load_module().validate_canon_freshness_scope(POST_C0_TRANSIENT_OPS_STATE_DECOUPLING | {"scripts/battle/lane_state.gd"})
        self.assertTrue(any("protected product" in error for error in errors), errors)

    def test_unrelated_file_is_rejected(self) -> None:
        errors = load_module().validate_canon_freshness_scope(POST_C0_TRANSIENT_OPS_STATE_DECOUPLING | {"docs/UNRELATED.md"})
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


    def test_current_main_router_handoff_sync_exact_surface_passes(self) -> None:
        module = load_module()
        self.assertEqual(module.validate_canon_freshness_scope(CURRENT_MAIN_ROUTER_HANDOFF_SYNC), [])

    def test_screen_surface_coverage_audit_exact_surface_passes(self) -> None:
        self.assertEqual(load_module().validate_canon_freshness_scope(SCREEN_SURFACE_COVERAGE_AUDIT), [])

    def test_canon_play_visual_audit_exact_surface_passes(self) -> None:
        self.assertEqual(load_module().validate_canon_freshness_scope(CANON_PLAY_VISUAL_AUDIT), [])

    def test_canon_play_visual_audit_rejects_missing_audit_record(self) -> None:
        errors = load_module().validate_canon_freshness_scope(
            CANON_PLAY_VISUAL_AUDIT
            - {"docs/audits/OMENWARD_CANON_PLAY_EXPERIENCE_VISUAL_AUDIT_2026-08-28.md"}
        )
        self.assertTrue(
            any("missing required v4.5 canon/play/visual audit anchors" in error for error in errors),
            errors,
        )

    def test_storybook_direction_lock_exact_surface_passes(self) -> None:
        self.assertEqual(
            load_module().validate_canon_freshness_scope(
                STORYBOOK_SD_THREE_FRONT_STRATEGIC_MAP_DIRECTION_LOCK
            ),
            [],
        )

    def test_storybook_direction_lock_rejects_missing_planning_board(self) -> None:
        errors = load_module().validate_canon_freshness_scope(
            STORYBOOK_SD_THREE_FRONT_STRATEGIC_MAP_DIRECTION_LOCK
            - {"docs/images/planning/OMENWARD_PROJECT_CORE_SCENE_VISUAL_BOARD_2026-08-28.md"}
        )
        self.assertTrue(
            any("storybook SD three-front strategic-map direction lock" in error for error in errors),
            errors,
        )

    def test_one_ward_citadel_three_branches_correction_exact_surface_passes(self) -> None:
        self.assertEqual(
            load_module().validate_canon_freshness_scope(
                ONE_WARD_CITADEL_THREE_BRANCHES_CORRECTION
            ),
            [],
        )

    def test_one_ward_citadel_three_branches_correction_rejects_missing_v2_board(self) -> None:
        errors = load_module().validate_canon_freshness_scope(
            ONE_WARD_CITADEL_THREE_BRANCHES_CORRECTION
            - {"docs/images/planning/generated/OMENWARD_PROJECT_CORE_SCENE_VISUAL_BOARD_2026-08-28_v2_BRANCHING.png"}
        )
        self.assertTrue(
            any("one Ward Citadel three-branches visual correction" in error for error in errors),
            errors,
        )

    def test_partial_current_main_router_handoff_sync_is_rejected(self) -> None:
        errors = load_module().validate_canon_freshness_scope(
            CURRENT_MAIN_ROUTER_HANDOFF_SYNC - {"docs/HANDOFF_CONTEXT.md"}
        )
        self.assertTrue(
            any(
                "missing required v4.5 current-main router handoff synchronization anchors" in error
                for error in errors
            ),
            errors,
        )


if __name__ == "__main__":
    unittest.main()
