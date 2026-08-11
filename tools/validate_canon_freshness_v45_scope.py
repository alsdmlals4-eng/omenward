#!/usr/bin/env python3
"""Validate bounded activation and Phase A planning surfaces for v4.5."""
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
    ".github/workflows/validate-active-integrated-contract-v4-4.yml",
    ".github/workflows/validate-canon-freshness-v4-5.yml",
    "AGENTS.md", "docs/ACTIVE_CONTEXT.md", "docs/CURRENT_IMPLEMENTATION_STATUS.md",
    "docs/DECISIONS_PENDING.md", "docs/DOCUMENTATION_MAP.md", "docs/DOCUMENT_LIFECYCLE_REGISTRY.md",
    "docs/OMENWARD_GDD_CURRENT_CANON.md", "docs/ONBOARDING_PLANNING_CURRENT_AUTHORITY.md",
    "docs/PROJECT_CANON_DECISION_LEDGER.md", "docs/PROJECT_CORE.md", "docs/PROJECT_GOOGLE_SHEET_WORKBOOK.md",
    "docs/design/APPROVED_OMENWARD_BUILDING_TIER_REALIGNMENT_2026-08-06.md",
    "docs/operations/ACTIVE_INTEGRATED_CONTRACT_STATE.v2.json",
    "docs/operations/CANON_FRESHNESS_V45_SHEET_SYNC_EVIDENCE_2026-08-11.json",
    "docs/process/ACTIVE_INTEGRATED_CONTRACT_BINDING_2026-08-11.md",
    "docs/process/APPROVED_OMENWARD_CANON_FRESHNESS_AND_V4_5_THIN_ADAPTER_2026-08-11.md",
    "docs/process/PROJECT_TOTAL_PLANNING_IMPLEMENTATION_AND_DELIVERY_INSTRUCTION_v4.5_r2.md",
    "docs/superpowers/plans/2026-08-11-canon-freshness-v45-routing.md",
    "tests/python/test_canon_freshness_v45_routing.py", "tests/python/test_canon_freshness_v45_scope.py",
    "tools/validate_canon_freshness_v45_scope.py",
}
ACTIVATION_REQUIRED_ANCHORS = {
    "docs/process/ACTIVE_INTEGRATED_CONTRACT_BINDING_2026-08-11.md",
    "docs/operations/ACTIVE_INTEGRATED_CONTRACT_STATE.v2.json",
    "docs/process/PROJECT_TOTAL_PLANNING_IMPLEMENTATION_AND_DELIVERY_INSTRUCTION_v4.5_r2.md",
    "docs/operations/CANON_FRESHNESS_V45_SHEET_SYNC_EVIDENCE_2026-08-11.json",
    "tests/python/test_canon_freshness_v45_routing.py",
    "tests/python/test_canon_freshness_v45_scope.py",
}

POSTMERGE_CI_ALLOWED_FILES = {
    ".github/workflows/validate-omenward-core.yml", "tests/python/test_ci_usage_contract.py",
    "tools/validate_ci_usage_contract.py", "tests/python/test_canon_freshness_v45_scope.py",
    "tools/validate_canon_freshness_v45_scope.py",
}
POSTMERGE_CI_REQUIRED_ANCHORS = set(POSTMERGE_CI_ALLOWED_FILES)

WINDOWS_CANONICAL_EVIDENCE_ALLOWED_FILES = {
    "tests/python/test_barracks_10000_robustness_execution.py",
    "tests/python/test_barracks_conditional_fail_remediation.py", "tests/python/test_base_recovery_map.py",
    "tests/python/test_project_base_adapter_freshness.py", "tests/python/test_git_canonical_evidence.py",
    "tools/git_canonical_evidence.py", "tests/python/test_canon_freshness_v45_scope.py",
    "tools/validate_canon_freshness_v45_scope.py",
}
WINDOWS_CANONICAL_EVIDENCE_REQUIRED_ANCHORS = set(WINDOWS_CANONICAL_EVIDENCE_ALLOWED_FILES)

POSTMERGE_EVIDENCE_ALLOWED_FILES = {
    "docs/operations/ACTIVE_INTEGRATED_CONTRACT_STATE.v2.json",
    "docs/operations/CANON_FRESHNESS_V45_SHEET_SYNC_EVIDENCE_2026-08-11.json",
}
POSTMERGE_EVIDENCE_REQUIRED_ANCHORS = set(POSTMERGE_EVIDENCE_ALLOWED_FILES)

CURRENT_CONSUMER_RECONCILIATION_ALLOWED_FILES = {
    "docs/ACTIVE_CONTEXT.md", "docs/CURRENT_IMPLEMENTATION_STATUS.md", "docs/DECISIONS_PENDING.md",
    "tests/python/test_canon_freshness_v45_routing.py", "tests/python/test_canon_freshness_v45_scope.py",
    "tools/validate_canon_freshness_v45_scope.py",
}
CURRENT_CONSUMER_RECONCILIATION_REQUIRED_ANCHORS = set(CURRENT_CONSUMER_RECONCILIATION_ALLOWED_FILES)

PHASE_A_READINESS_CLASSIFICATION_ALLOWED_FILES = {
    ".github/workflows/validate-canon-freshness-v4-5.yml", "AGENTS.md", "docs/DECISIONS_PENDING.md",
    "docs/OMENWARD_GDD_CURRENT_CANON.md", "docs/ONBOARDING_PLANNING_CURRENT_AUTHORITY.md",
    "docs/PROJECT_GOOGLE_SHEET_WORKBOOK.md",
    "docs/reviews/PHASE_A_PLANNING_READINESS_DEPENDENCY_CLASSIFICATION_2026-08-11.md",
    "docs/superpowers/plans/2026-08-11-phase-a-readiness-dependency-classification.md",
    "tests/python/test_phase_a_readiness_dependency_classification.py",
    "tests/python/test_canon_freshness_v45_scope.py", "tools/validate_canon_freshness_v45_scope.py",
}
PHASE_A_READINESS_CLASSIFICATION_REQUIRED_ANCHORS = set(PHASE_A_READINESS_CLASSIFICATION_ALLOWED_FILES)

PHASE_A_WHOLE_PROJECT_OPEN_CONTENT_ALLOWED_FILES = {
    ".github/workflows/validate-canon-freshness-v4-5.yml", "AGENTS.md", "docs/ACTIVE_CONTEXT.md",
    "docs/CURRENT_IMPLEMENTATION_STATUS.md", "docs/DECISIONS_PENDING.md", "docs/OMENWARD_GDD_CURRENT_CANON.md",
    "docs/PROJECT_CORE.md", "docs/PROJECT_GOOGLE_SHEET_WORKBOOK.md",
    "docs/reviews/PHASE_A_WHOLE_PROJECT_OPEN_CONTENT_INVENTORY_2026-08-11.md",
    "docs/superpowers/plans/2026-08-11-phase-a-whole-project-open-content-inventory.md",
    "tests/python/test_phase_a_whole_project_open_content_inventory.py",
    "tests/python/test_canon_freshness_v45_scope.py", "tools/validate_canon_freshness_v45_scope.py",
}
PHASE_A_WHOLE_PROJECT_OPEN_CONTENT_REQUIRED_ANCHORS = set(PHASE_A_WHOLE_PROJECT_OPEN_CONTENT_ALLOWED_FILES)

APPROVED_FILES = (
    ACTIVATION_ALLOWED_FILES | POSTMERGE_CI_ALLOWED_FILES | WINDOWS_CANONICAL_EVIDENCE_ALLOWED_FILES
    | POSTMERGE_EVIDENCE_ALLOWED_FILES | CURRENT_CONSUMER_RECONCILIATION_ALLOWED_FILES
    | PHASE_A_READINESS_CLASSIFICATION_ALLOWED_FILES | PHASE_A_WHOLE_PROJECT_OPEN_CONTENT_ALLOWED_FILES
)


def _normalize(paths: Iterable[str]) -> set[str]:
    return {path.strip().replace("\\", "/") for path in paths if path.strip()}


def _is_protected_product(path: str) -> bool:
    return path == "project.godot" or path.startswith(PROTECTED_PREFIXES)


def _validate_required(changed: set[str], required: set[str], label: str) -> list[str]:
    missing = sorted(required - changed)
    return [] if not missing else [f"missing required v4.5 {label} anchors: {missing}"]


def validate_canon_freshness_scope(changed_files: Iterable[str]) -> list[str]:
    changed = _normalize(changed_files)
    errors: list[str] = []
    historical_mutations = sorted(changed & HISTORICAL_V44_AUTHORITY)
    if historical_mutations:
        errors.append(f"historical v4.4 authority mutation is forbidden: {historical_mutations}")
    protected = sorted(path for path in changed if _is_protected_product(path))
    if protected:
        errors.append(f"protected product paths are forbidden in v4.5 canon freshness scope: {protected}")
    unexpected = sorted(changed - APPROVED_FILES)
    if unexpected:
        errors.append(f"v4.5 canon freshness transition contains unapproved files: {unexpected}")
    if errors:
        return errors

    modes = (
        (POSTMERGE_EVIDENCE_ALLOWED_FILES, POSTMERGE_EVIDENCE_REQUIRED_ANCHORS, "postmerge evidence"),
        (POSTMERGE_CI_ALLOWED_FILES, POSTMERGE_CI_REQUIRED_ANCHORS, "postmerge CI remediation"),
        (WINDOWS_CANONICAL_EVIDENCE_ALLOWED_FILES, WINDOWS_CANONICAL_EVIDENCE_REQUIRED_ANCHORS, "Windows canonical evidence portability"),
        (CURRENT_CONSUMER_RECONCILIATION_ALLOWED_FILES, CURRENT_CONSUMER_RECONCILIATION_REQUIRED_ANCHORS, "current consumer reconciliation"),
        (PHASE_A_READINESS_CLASSIFICATION_ALLOWED_FILES, PHASE_A_READINESS_CLASSIFICATION_REQUIRED_ANCHORS, "Phase A readiness classification"),
        (PHASE_A_WHOLE_PROJECT_OPEN_CONTENT_ALLOWED_FILES, PHASE_A_WHOLE_PROJECT_OPEN_CONTENT_REQUIRED_ANCHORS, "Phase A whole-project open-content"),
        (ACTIVATION_ALLOWED_FILES, ACTIVATION_REQUIRED_ANCHORS, "activation"),
    )
    for allowed, required, label in modes:
        if changed <= allowed:
            return _validate_required(changed, required, label)
    return ["v4.5 canon freshness transition did not match a recognized fail-closed scope mode"]


def changed_files_from_git(base: str, head: str) -> list[str]:
    result = subprocess.run(["git", "diff", "--name-only", f"{base}...{head}"], capture_output=True, text=True, encoding="utf-8", errors="replace", check=False)
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
