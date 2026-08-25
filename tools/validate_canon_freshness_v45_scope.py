#!/usr/bin/env python3
"""Validate historical v4.5 transitions plus explicit current-canon reconciliation surfaces."""
from __future__ import annotations

import argparse
import subprocess
from typing import Iterable

PROTECTED_PREFIXES = ("data/", "scripts/", "scenes/", "assets/", "addons/")
HISTORICAL_V44_AUTHORITY = {
    "docs/process/ACTIVE_INTEGRATED_CONTRACT_BINDING_2026-08-06.md",
    "docs/operations/ACTIVE_INTEGRATED_CONTRACT_STATE.v1.json",
}
ACTIVATION_ALLOWED_FILES = {
    ".github/workflows/validate-active-integrated-contract-v4-4.yml", ".github/workflows/validate-canon-freshness-v4-5.yml", "AGENTS.md", "docs/ACTIVE_CONTEXT.md", "docs/CURRENT_IMPLEMENTATION_STATUS.md", "docs/DECISIONS_PENDING.md", "docs/DOCUMENTATION_MAP.md", "docs/DOCUMENT_LIFECYCLE_REGISTRY.md", "docs/OMENWARD_GDD_CURRENT_CANON.md", "docs/ONBOARDING_PLANNING_CURRENT_AUTHORITY.md", "docs/PROJECT_CANON_DECISION_LEDGER.md", "docs/PROJECT_CORE.md", "docs/PROJECT_GOOGLE_SHEET_WORKBOOK.md", "docs/design/APPROVED_OMENWARD_BUILDING_TIER_REALIGNMENT_2026-08-06.md", "docs/operations/ACTIVE_INTEGRATED_CONTRACT_STATE.v2.json", "docs/operations/CANON_FRESHNESS_V45_SHEET_SYNC_EVIDENCE_2026-08-11.json", "docs/process/ACTIVE_INTEGRATED_CONTRACT_BINDING_2026-08-11.md", "docs/process/APPROVED_OMENWARD_CANON_FRESHNESS_AND_V4_5_THIN_ADAPTER_2026-08-11.md", "docs/process/PROJECT_TOTAL_PLANNING_IMPLEMENTATION_AND_DELIVERY_INSTRUCTION_v4.5_r2.md", "docs/superpowers/plans/2026-08-11-canon-freshness-v45-routing.md", "tests/python/test_canon_freshness_v45_routing.py", "tests/python/test_canon_freshness_v45_scope.py", "tools/validate_canon_freshness_v45_scope.py",
}
ACTIVATION_REQUIRED_ANCHORS = {"docs/process/ACTIVE_INTEGRATED_CONTRACT_BINDING_2026-08-11.md", "docs/operations/ACTIVE_INTEGRATED_CONTRACT_STATE.v2.json", "docs/process/PROJECT_TOTAL_PLANNING_IMPLEMENTATION_AND_DELIVERY_INSTRUCTION_v4.5_r2.md", "docs/operations/CANON_FRESHNESS_V45_SHEET_SYNC_EVIDENCE_2026-08-11.json", "tests/python/test_canon_freshness_v45_routing.py", "tests/python/test_canon_freshness_v45_scope.py"}
PHASE_B_POSTMERGE_FULL_SUITE_ALLOWED_FILES = {
    ".github/workflows/validate-omenward-core.yml",
    "AGENTS.md",
    "docs/CURRENT_IMPLEMENTATION_STATUS.md",
    "tests/python/test_ci_usage_contract.py",
    "tools/validate_ci_usage_contract.py",
    "tests/python/test_canon_freshness_v45_scope.py",
    "tools/validate_canon_freshness_v45_scope.py",
}
PHASE_B_POSTMERGE_FULL_SUITE_REQUIRED_ANCHORS = set(PHASE_B_POSTMERGE_FULL_SUITE_ALLOWED_FILES)
PHASE_C_C0_TOOLCHAIN_GATE_ALLOWED_FILES = {
    ".github/workflows/validate-omenward-core.yml",
    "docs/reviews/PHASE_C_C0_PREFLIGHT_2026-08-11.md",
    "docs/superpowers/plans/2026-08-11-phase-c-c0-toolchain-ci-gate.md",
    "tests/python/test_phase_c_c0_toolchain_ci_gate.py",
    "tests/python/test_tool_state_user_approval_remote_sync.py",
    "tools/validate_ci_usage_contract.py",
    "tests/python/test_canon_freshness_v45_scope.py",
    "tools/validate_canon_freshness_v45_scope.py",
}
PHASE_C_C0_TOOLCHAIN_GATE_REQUIRED_ANCHORS = set(PHASE_C_C0_TOOLCHAIN_GATE_ALLOWED_FILES)
PHASE_C_C0_LOCAL_HIGODOT_CLOSURE_ALLOWED_FILES = {
    "docs/ACTIVE_CONTEXT.md",
    "docs/CURRENT_IMPLEMENTATION_STATUS.md",
    "docs/reviews/PHASE_C_C0_LOCAL_HIGODOT_CLOSURE_2026-08-11.md",
    "tests/python/test_canon_freshness_v45_scope.py",
    "tools/validate_canon_freshness_v45_scope.py",
}
PHASE_C_C0_LOCAL_HIGODOT_CLOSURE_REQUIRED_ANCHORS = set(PHASE_C_C0_LOCAL_HIGODOT_CLOSURE_ALLOWED_FILES)
POST_C0_CURRENT_ROUTER_RECONCILIATION_ALLOWED_FILES = {
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
POST_C0_CURRENT_ROUTER_RECONCILIATION_REQUIRED_ANCHORS = set(POST_C0_CURRENT_ROUTER_RECONCILIATION_ALLOWED_FILES)
POST_C0_FULL_CURRENT_CONSUMER_CLOSURE_ALLOWED_FILES = {
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
POST_C0_FULL_CURRENT_CONSUMER_CLOSURE_REQUIRED_ANCHORS = set(POST_C0_FULL_CURRENT_CONSUMER_CLOSURE_ALLOWED_FILES)
POST_C0_TRANSIENT_OPS_STATE_DECOUPLING_ALLOWED_FILES = {
    "docs/reviews/PHASE_C_C0_LOCAL_HIGODOT_CLOSURE_2026-08-11.md",
    "docs/PROJECT_GOOGLE_SHEET_WORKBOOK.md",
    "docs/operations/ACTIVE_INTEGRATED_CONTRACT_STATE.v2.json",
    "docs/PROJECT_CANON_DECISION_LEDGER.md",
    "tests/python/test_canon_freshness_v45_routing.py",
    "tests/python/test_canon_freshness_v45_scope.py",
    "tools/validate_canon_freshness_v45_scope.py",
}
POST_C0_TRANSIENT_OPS_STATE_DECOUPLING_REQUIRED_ANCHORS = set(POST_C0_TRANSIENT_OPS_STATE_DECOUPLING_ALLOWED_FILES)
WINDOWS_CANONICAL_EVIDENCE_ALLOWED_FILES = {"tests/python/test_barracks_10000_robustness_execution.py", "tests/python/test_barracks_conditional_fail_remediation.py", "tests/python/test_base_recovery_map.py", "tests/python/test_project_base_adapter_freshness.py", "tests/python/test_git_canonical_evidence.py", "tools/git_canonical_evidence.py", "tests/python/test_canon_freshness_v45_scope.py", "tools/validate_canon_freshness_v45_scope.py"}
WINDOWS_CANONICAL_EVIDENCE_REQUIRED_ANCHORS = set(WINDOWS_CANONICAL_EVIDENCE_ALLOWED_FILES)
POSTMERGE_EVIDENCE_ALLOWED_FILES = {"docs/operations/ACTIVE_INTEGRATED_CONTRACT_STATE.v2.json", "docs/operations/CANON_FRESHNESS_V45_SHEET_SYNC_EVIDENCE_2026-08-11.json"}
POSTMERGE_EVIDENCE_REQUIRED_ANCHORS = set(POSTMERGE_EVIDENCE_ALLOWED_FILES)
CURRENT_CONSUMER_RECONCILIATION_ALLOWED_FILES = {
    "docs/ACTIVE_CONTEXT.md",
    "docs/CURRENT_IMPLEMENTATION_STATUS.md",
    "docs/DECISIONS_PENDING.md",
    "docs/HANDOFF_CONTEXT.md",
    "tests/python/test_canon_freshness_v45_routing.py",
    "tests/python/test_canon_freshness_v45_scope.py",
    "tools/validate_canon_freshness_v45_scope.py",
}
CURRENT_CONSUMER_RECONCILIATION_REQUIRED_ANCHORS = set(CURRENT_CONSUMER_RECONCILIATION_ALLOWED_FILES)
PHASE_A_READINESS_CLASSIFICATION_ALLOWED_FILES = {".github/workflows/validate-canon-freshness-v4-5.yml", "AGENTS.md", "docs/DECISIONS_PENDING.md", "docs/OMENWARD_GDD_CURRENT_CANON.md", "docs/ONBOARDING_PLANNING_CURRENT_AUTHORITY.md", "docs/PROJECT_GOOGLE_SHEET_WORKBOOK.md", "docs/reviews/PHASE_A_PLANNING_READINESS_DEPENDENCY_CLASSIFICATION_2026-08-11.md", "docs/superpowers/plans/2026-08-11-phase-a-readiness-dependency-classification.md", "tests/python/test_phase_a_readiness_dependency_classification.py", "tests/python/test_canon_freshness_v45_scope.py", "tools/validate_canon_freshness_v45_scope.py"}
PHASE_A_READINESS_CLASSIFICATION_REQUIRED_ANCHORS = set(PHASE_A_READINESS_CLASSIFICATION_ALLOWED_FILES)
CONTENT_CLOSURE_BENCHMARK_FIRST_ALLOWED_FILES = {
    ".github/workflows/validate-canon-freshness-v4-5.yml", "AGENTS.md", "docs/ACTIVE_CONTEXT.md", "docs/DECISIONS_PENDING.md", "docs/design/APPROVED_OMENWARD_WHOLE_PROJECT_CONTENT_CLOSURE_2026-08-11.md", "docs/process/APPROVED_OMENWARD_BENCHMARK_INDUSTRY_RESEARCH_FIRST_2026-08-11.md", "docs/superpowers/plans/2026-08-11-content-closure-benchmark-first.md", "tests/python/test_content_closure_benchmark_first.py", "tests/python/test_phase_a_readiness_dependency_classification.py", "tests/python/test_canon_freshness_v45_scope.py", "tools/validate_canon_freshness_v45_scope.py",
}
CONTENT_CLOSURE_BENCHMARK_FIRST_REQUIRED_ANCHORS = set(CONTENT_CLOSURE_BENCHMARK_FIRST_ALLOWED_FILES)
QUALITY_GUARDRAILS_ELITE_BOSS_CADENCE_ALLOWED_FILES = {
    ".github/workflows/validate-canon-freshness-v4-5.yml",
    "AGENTS.md",
    "docs/ACTIVE_CONTEXT.md",
    "docs/DECISIONS_PENDING.md",
    "docs/design/APPROVED_OMENWARD_QUALITY_GUARDRAILS_2026-08-11.md",
    "docs/design/APPROVED_OMENWARD_ELITE_WAVE_AND_BOSS_CADENCE_2026-08-11.md",
    "docs/superpowers/specs/2026-08-11-quality-guardrails-elite-boss-cadence-design.md",
    "docs/superpowers/plans/2026-08-11-quality-guardrails-elite-boss-cadence.md",
    "tests/python/test_quality_guardrails_elite_boss_cadence.py",
    "tests/python/test_canon_freshness_v45_scope.py",
    "tools/validate_canon_freshness_v45_scope.py",
}
QUALITY_GUARDRAILS_ELITE_BOSS_CADENCE_REQUIRED_ANCHORS = set(QUALITY_GUARDRAILS_ELITE_BOSS_CADENCE_ALLOWED_FILES)
PHASE_B_FINAL_PLANNING_REVIEW_ALLOWED_FILES = {
    ".github/workflows/validate-canon-freshness-v4-5.yml",
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
PHASE_B_FINAL_PLANNING_REVIEW_REQUIRED_ANCHORS = set(PHASE_B_FINAL_PLANNING_REVIEW_ALLOWED_FILES)

# Retained to reproduce the 2026-08-21 reconciliation exactly.
CURRENT_V47_CANON_VALIDATOR_RECONCILIATION_ALLOWED_FILES = {
    ".github/workflows/validate-omenward-core.yml",
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
    "docs/design/APPROVED_OMENWARD_TOPDOWN_UNIT_SILHOUETTE_RULES_2026-08-20.md",
    "tests/python/test_bca_visual_sheet_adoption.py",
    "tests/python/test_c1_roulette_contract.py",
    "tests/python/test_c2_battle_objective_contract.py",
    "tests/python/test_c3_core_ux_contract.py",
    "tests/python/test_canon_freshness_v45_routing.py",
    "tests/python/test_content_closure_benchmark_first.py",
    "tests/python/test_current_canon_reconciliation_20260821.py",
    "tests/python/test_current_v47_canon_validator_scope.py",
    "tests/python/test_pc_android_core_adapter_architecture_contract.py",
    "tests/python/test_phase_b_final_planning_review.py",
    "tests/python/test_project_core_docs.py",
    "tests/python/test_quality_guardrails_elite_boss_cadence.py",
    "tools/validate_c1_roulette.py",
    "tools/validate_c2_battle_objective.py",
    "tools/validate_c3_core_ux.py",
    "tools/validate_canon_freshness_v45_scope.py",
    "tools/validate_project_core_docs.py",
}
CURRENT_V47_CANON_VALIDATOR_RECONCILIATION_REQUIRED_ANCHORS = {
    "AGENTS.md",
    "README.md",
    "docs/CURRENT_CONFIRMED_DECISIONS.md",
    "docs/CURRENT_IMPLEMENTATION_STATUS.md",
    "docs/DOCUMENTATION_MAP.md",
    "docs/DOCUMENT_LIFECYCLE_REGISTRY.md",
    "docs/OMENWARD_GDD_CURRENT_CANON.md",
    "docs/PROJECT_CORE.md",
    "tests/python/test_current_canon_reconciliation_20260821.py",
    "tests/python/test_current_v47_canon_validator_scope.py",
    "tools/validate_c1_roulette.py",
    "tools/validate_c2_battle_objective.py",
    "tools/validate_c3_core_ux.py",
    "tools/validate_canon_freshness_v45_scope.py",
    "tools/validate_project_core_docs.py",
}

CURRENT_V48_NORTH_STAR_AUDIT_ALLOWED_FILES = {
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
    "docs/reviews/FINAL_PLANNING_ADVERSARIAL_REVIEW_AND_DRIFT_CHECK_2026-08-24.md",
    "tests/python/test_canon_freshness_v45_routing.py",
    "tests/python/test_content_closure_benchmark_first.py",
    "tests/python/test_current_canon_reconciliation_20260821.py",
    "tests/python/test_current_v48_north_star_audit_scope.py",
    "tests/python/test_pc_android_core_adapter_architecture_contract.py",
    "tests/python/test_phase_b_final_planning_review.py",
    "tests/python/test_project_core_docs.py",
    "tools/validate_canon_freshness_v45_scope.py",
    "tools/validate_project_core_docs.py",
}
CURRENT_V48_NORTH_STAR_AUDIT_REQUIRED_ANCHORS = set(CURRENT_V48_NORTH_STAR_AUDIT_ALLOWED_FILES)

# Current live-state owners transitioned from planning-complete/awaiting-authority to a
# user-approved, *scoped* Run Command implementation packet. Keep this bounded so the
# authority sync itself cannot mutate product source or unrelated current consumers.
RUN_COMMAND_IMPLEMENTATION_AUTHORITY_SYNC_ALLOWED_FILES = {
    "AGENTS.md",
    "docs/ACTIVE_CONTEXT.md",
    "docs/CURRENT_CONFIRMED_DECISIONS.md",
    "tests/python/test_project_core_docs.py",
    "tests/python/test_run_command_implementation_authority_scope.py",
    "tools/validate_canon_freshness_v45_scope.py",
    "tools/validate_project_core_docs.py",
}
RUN_COMMAND_IMPLEMENTATION_AUTHORITY_SYNC_REQUIRED_ANCHORS = set(RUN_COMMAND_IMPLEMENTATION_AUTHORITY_SYNC_ALLOWED_FILES)

# User-approved 2026-08-25 visual closeout. This scope is documentation/validator-only:
# it records the current visual Decision/asset/handoff while keeping all product paths
# and runtime evidence fail-closed. The current-canon consumer is part of this exact
# reconciliation because the approved Decision count and visual owner changed.
CURRENT_V48_VISUAL_CLOSEOUT_ALLOWED_FILES = {
    "AGENTS.md",
    "docs/ACTIVE_CONTEXT.md",
    "docs/CURRENT_CONFIRMED_DECISIONS.md",
    "docs/HANDOFF_CONTEXT.md",
    "docs/handoffs/2026-08-25-front-state-visual-approved-closeout.md",
    "docs/images/planning/canonical/OMENWARD_APPROVED_FRONT_STATE_VISUAL_2026-08-25.md",
    "docs/superpowers/specs/2026-08-25-front-state-minimap-sd-fantasy-design.md",
    "tests/python/test_canon_freshness_v45_routing.py",
    "tests/python/test_current_canon_reconciliation_20260821.py",
    "tests/python/test_current_v48_visual_closeout_scope.py",
    "tests/python/test_project_core_docs.py",
    "tools/validate_canon_freshness_v45_scope.py",
    "tools/validate_project_core_docs.py",
}
CURRENT_V48_VISUAL_CLOSEOUT_REQUIRED_ANCHORS = set(CURRENT_V48_VISUAL_CLOSEOUT_ALLOWED_FILES)

APPROVED_FILES = (
    ACTIVATION_ALLOWED_FILES
    | PHASE_B_POSTMERGE_FULL_SUITE_ALLOWED_FILES
    | PHASE_C_C0_TOOLCHAIN_GATE_ALLOWED_FILES
    | PHASE_C_C0_LOCAL_HIGODOT_CLOSURE_ALLOWED_FILES
    | POST_C0_CURRENT_ROUTER_RECONCILIATION_ALLOWED_FILES
    | POST_C0_FULL_CURRENT_CONSUMER_CLOSURE_ALLOWED_FILES
    | POST_C0_TRANSIENT_OPS_STATE_DECOUPLING_ALLOWED_FILES
    | WINDOWS_CANONICAL_EVIDENCE_ALLOWED_FILES
    | POSTMERGE_EVIDENCE_ALLOWED_FILES
    | CURRENT_CONSUMER_RECONCILIATION_ALLOWED_FILES
    | PHASE_A_READINESS_CLASSIFICATION_ALLOWED_FILES
    | CONTENT_CLOSURE_BENCHMARK_FIRST_ALLOWED_FILES
    | QUALITY_GUARDRAILS_ELITE_BOSS_CADENCE_ALLOWED_FILES
    | PHASE_B_FINAL_PLANNING_REVIEW_ALLOWED_FILES
    | CURRENT_V47_CANON_VALIDATOR_RECONCILIATION_ALLOWED_FILES
    | CURRENT_V48_NORTH_STAR_AUDIT_ALLOWED_FILES
    | RUN_COMMAND_IMPLEMENTATION_AUTHORITY_SYNC_ALLOWED_FILES
    | CURRENT_V48_VISUAL_CLOSEOUT_ALLOWED_FILES
)


def _normalize(paths: Iterable[str]) -> set[str]:
    return {p.strip().replace("\\", "/") for p in paths if p.strip()}


def _is_protected_product(path: str) -> bool:
    return path == "project.godot" or path.startswith(PROTECTED_PREFIXES)


def _validate_required(changed: set[str], required: set[str], label: str) -> list[str]:
    missing = sorted(required - changed)
    return [] if not missing else [f"missing required v4.5 {label} anchors: {missing}"]


def validate_canon_freshness_scope(changed_files: Iterable[str]) -> list[str]:
    changed = _normalize(changed_files)
    errors: list[str] = []
    historical = sorted(changed & HISTORICAL_V44_AUTHORITY)
    if historical:
        errors.append(f"historical v4.4 authority mutation is forbidden: {historical}")
    protected = sorted(p for p in changed if _is_protected_product(p))
    if protected:
        errors.append(f"protected product paths are forbidden in v4.5 canon freshness scope: {protected}")
    unexpected = sorted(changed - APPROVED_FILES)
    if unexpected:
        errors.append(f"v4.5 canon freshness transition contains unapproved files: {unexpected}")
    if errors:
        return errors
    modes = (
        (CURRENT_V48_VISUAL_CLOSEOUT_ALLOWED_FILES, CURRENT_V48_VISUAL_CLOSEOUT_REQUIRED_ANCHORS, "current v4.8 visual closeout"),
        (RUN_COMMAND_IMPLEMENTATION_AUTHORITY_SYNC_ALLOWED_FILES, RUN_COMMAND_IMPLEMENTATION_AUTHORITY_SYNC_REQUIRED_ANCHORS, "Run Command implementation-authority sync"),
        (CURRENT_V48_NORTH_STAR_AUDIT_ALLOWED_FILES, CURRENT_V48_NORTH_STAR_AUDIT_REQUIRED_ANCHORS, "current v4.8 North Star audit reconciliation"),
        (CURRENT_V47_CANON_VALIDATOR_RECONCILIATION_ALLOWED_FILES, CURRENT_V47_CANON_VALIDATOR_RECONCILIATION_REQUIRED_ANCHORS, "current v4.7 canon-validator reconciliation"),
        (POSTMERGE_EVIDENCE_ALLOWED_FILES, POSTMERGE_EVIDENCE_REQUIRED_ANCHORS, "postmerge evidence"),
        (POST_C0_TRANSIENT_OPS_STATE_DECOUPLING_ALLOWED_FILES, POST_C0_TRANSIENT_OPS_STATE_DECOUPLING_REQUIRED_ANCHORS, "post-C0 transient ops-state decoupling"),
        (POST_C0_FULL_CURRENT_CONSUMER_CLOSURE_ALLOWED_FILES, POST_C0_FULL_CURRENT_CONSUMER_CLOSURE_REQUIRED_ANCHORS, "post-C0 full current-consumer closure"),
        (POST_C0_CURRENT_ROUTER_RECONCILIATION_ALLOWED_FILES, POST_C0_CURRENT_ROUTER_RECONCILIATION_REQUIRED_ANCHORS, "post-C0 current-router reconciliation"),
        (PHASE_C_C0_LOCAL_HIGODOT_CLOSURE_ALLOWED_FILES, PHASE_C_C0_LOCAL_HIGODOT_CLOSURE_REQUIRED_ANCHORS, "Phase C C0 local HiGodot closure"),
        (PHASE_C_C0_TOOLCHAIN_GATE_ALLOWED_FILES, PHASE_C_C0_TOOLCHAIN_GATE_REQUIRED_ANCHORS, "Phase C C0 toolchain gate"),
        (PHASE_B_POSTMERGE_FULL_SUITE_ALLOWED_FILES, PHASE_B_POSTMERGE_FULL_SUITE_REQUIRED_ANCHORS, "Phase B postmerge full-suite remediation"),
        (WINDOWS_CANONICAL_EVIDENCE_ALLOWED_FILES, WINDOWS_CANONICAL_EVIDENCE_REQUIRED_ANCHORS, "Windows canonical evidence portability"),
        (CURRENT_CONSUMER_RECONCILIATION_ALLOWED_FILES, CURRENT_CONSUMER_RECONCILIATION_REQUIRED_ANCHORS, "current consumer reconciliation"),
        (PHASE_A_READINESS_CLASSIFICATION_ALLOWED_FILES, PHASE_A_READINESS_CLASSIFICATION_REQUIRED_ANCHORS, "Phase A readiness classification"),
        (CONTENT_CLOSURE_BENCHMARK_FIRST_ALLOWED_FILES, CONTENT_CLOSURE_BENCHMARK_FIRST_REQUIRED_ANCHORS, "content closure benchmark-first"),
        (QUALITY_GUARDRAILS_ELITE_BOSS_CADENCE_ALLOWED_FILES, QUALITY_GUARDRAILS_ELITE_BOSS_CADENCE_REQUIRED_ANCHORS, "quality guardrails elite boss cadence"),
        (PHASE_B_FINAL_PLANNING_REVIEW_ALLOWED_FILES, PHASE_B_FINAL_PLANNING_REVIEW_REQUIRED_ANCHORS, "Phase B final planning review"),
        (ACTIVATION_ALLOWED_FILES, ACTIVATION_REQUIRED_ANCHORS, "activation"),
    )
    for allowed, required, label in modes:
        if changed <= allowed:
            return _validate_required(changed, required, label)
    return ["v4.5 canon freshness transition did not match a recognized fail-closed scope mode"]


def changed_files_from_git(base: str, head: str) -> list[str]:
    result = subprocess.run(
        ["git", "diff", "--name-only", f"{base}...{head}"],
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        check=False,
    )
    if result.returncode:
        raise RuntimeError(result.stderr.strip() or "git diff failed")
    return result.stdout.splitlines()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base", required=True)
    parser.add_argument("--head", default="HEAD")
    args = parser.parse_args()
    changed = changed_files_from_git(args.base, args.head)
    errors = validate_canon_freshness_scope(changed)
    if errors:
        print("canon_freshness_v45_scope=FAIL")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"canon_freshness_v45_scope=PASS changed_files={len(_normalize(changed))}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())