#!/usr/bin/env python3
"""Validate the temporary no-budget exact-HEAD verification fallback."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Iterable

ROOT = Path(__file__).resolve().parents[1]
POLICY_PATH = Path("docs/operations/LOCAL_EXACT_HEAD_FALLBACK_POLICY.v1.json")
EVIDENCE_PATH = Path("docs/evidence/PR157_LOCAL_EXACT_HEAD_VERIFICATION_2026-08-07.json")
DECISION_ID = "OMW-DEC-20260807-PROCESS-ACTIONS-BUDGET-LOCAL-EXACT-HEAD-FALLBACK-V1"
EXPECTED_PR = 157
EXPECTED_HEAD = "c27715cfb7f161854fd994711a6859ee23a68fac"
EXPECTED_BASE = "7588317f294d602cfad5f7f15bfebcf849b8a77b"
ELIGIBLE_CLASSES = {
    "PROCESS_ONLY",
    "DOCUMENTATION_ONLY",
    "PYTHON_VALIDATOR_ONLY",
    "DATA_CONTRACT_ONLY",
}
FORBIDDEN_CLASSES = {
    "PRODUCT_IMPLEMENTATION",
    "GODOT_AUTHORING",
    "GODOT_RUNTIME",
    "FORMAL_GUT_RUNTIME",
    "WINDOWS_ANDROID_RUNTIME",
    "ASSET_IMPORT_OR_RUNTIME",
    "EXPORT_OR_PACKAGE",
}
EXPECTED_REMOTE_FILES = {
    ".github/workflows/validate-active-integrated-contract-v4-3.yml": "8ada75fad25c41f0db996decac71eb747dce0b2b",
    "docs/operations/ACTIVE_INTEGRATED_CONTRACT_STATE.v1.json": "34ce302f78646ebc3610bd2e24c1d11b0aff66b4",
    "docs/process/ACTIVE_INTEGRATED_CONTRACT_BINDING_2026-08-06.md": "3e90342367d91b46e9830bd7337b1990ee8c63cf",
    "docs/reviews/ADVERSARIAL_INTEGRATED_CONTRACT_V4_3_ACTIVATION_REVIEW_2026-08-06.md": "6a02e318505796eec298c77f7170363260ac5c49",
    "docs/superpowers/plans/2026-08-06-activate-integrated-contract-v4-3.md": "3fa228386802e3d13d411e5911ca92a23cc32f97",
    "tests/python/test_active_integrated_contract_v4_3.py": "c4ce54be50866b086966c61fc4752abef3cfc7bb",
    "tools/validate_active_integrated_contract_v4_3.py": "6a3bd2d3ae0b294197f38692bbc7ce58c2712f67",
}


def load_json(path: Path) -> dict[str, Any]:
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def validate_policy(data: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    if data.get("decision_id") != DECISION_ID:
        errors.append("Decision ID mismatch")
    if data.get("status") != "ACTIVE_TEMPORARY_FALLBACK":
        errors.append("fallback policy must be active")
    if data.get("authority") != "USER_DIRECT_APPROVAL_IN_CURRENT_CONVERSATION":
        errors.append("fallback authority mismatch")

    trigger = data.get("trigger", {})
    if trigger.get("classification") != "BILLING_OR_SPENDING_LIMIT_PRE_START":
        errors.append("Actions blocker classification mismatch")
    if trigger.get("workflow_steps") != 0 or trigger.get("runner_id") != 0:
        errors.append("Actions pre-start boundary mismatch")
    if trigger.get("github_actions_green") is not False:
        errors.append("GitHub Actions Green must remain false")
    if trigger.get("code_or_test_commands_executed_in_actions") is not False:
        errors.append("Actions command-execution claim must remain false")

    scope = data.get("scope", {})
    eligible = set(scope.get("eligible_pr_classes", []))
    if eligible != ELIGIBLE_CLASSES:
        errors.append("eligible PR classes mismatch")
    if eligible & FORBIDDEN_CLASSES:
        errors.append("runtime or product class cannot be fallback-eligible")
    if not FORBIDDEN_CLASSES.issubset(set(scope.get("ineligible_pr_classes", []))):
        errors.append("ineligible runtime and product classes incomplete")

    requirements = data.get("verification_requirements", {})
    if requirements.get("require_exact_head") is not True:
        errors.append("exact HEAD verification must be required")
    if requirements.get("require_git_blob_sha") is not True:
        errors.append("Git blob SHA readback must be required")
    if requirements.get("require_changed_file_allowlist") is not True:
        errors.append("changed-file allowlist must be required")
    if requirements.get("require_reconstruct_from_remote") is not True:
        errors.append("remote reconstruction must be required")
    if requirements.get("require_fresh_commands") is not True:
        errors.append("fresh commands must be required")
    if requirements.get("can_claim_github_actions_green") is not False:
        errors.append("fallback cannot claim GitHub Actions Green")
    if requirements.get("can_substitute_for_godot_runtime") is not False:
        errors.append("fallback cannot substitute for Godot runtime")
    if requirements.get("can_substitute_for_gut_runtime") is not False:
        errors.append("fallback cannot substitute for GUT runtime")
    if requirements.get("can_substitute_for_windows_android") is not False:
        errors.append("fallback cannot substitute for platform runtime")

    merge = data.get("merge_policy", {})
    if merge.get("normal_merge_only") is not True:
        errors.append("only normal merge may be used")
    if merge.get("repository_policy_bypass") != "FORBIDDEN":
        errors.append("repository policy bypass must be FORBIDDEN")
    if merge.get("branch_protection_bypass") != "FORBIDDEN":
        errors.append("branch protection bypass must be FORBIDDEN")
    if merge.get("runtime_pr_merge_authorized") is not False:
        errors.append("runtime PR merge must remain unauthorized")
    if set(merge.get("eligible_pr_classes", [])) != ELIGIBLE_CLASSES:
        errors.append("merge-eligible classes mismatch")

    subject = data.get("initial_subject", {})
    if subject.get("pull_request") != EXPECTED_PR:
        errors.append("initial fallback subject PR mismatch")
    if subject.get("head_sha") != EXPECTED_HEAD:
        errors.append("initial fallback exact head mismatch")
    if subject.get("base_sha") != EXPECTED_BASE:
        errors.append("initial fallback base mismatch")
    if subject.get("pr_class") not in ELIGIBLE_CLASSES:
        errors.append("initial subject class is not eligible")
    return errors


def validate_evidence(data: dict[str, Any], policy: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    if data.get("decision_id") != DECISION_ID:
        errors.append("evidence Decision ID mismatch")
    if data.get("policy_status") != policy.get("status"):
        errors.append("evidence policy status mismatch")

    subject = data.get("subject", {})
    if subject.get("pull_request") != EXPECTED_PR or subject.get("head_sha") != EXPECTED_HEAD:
        errors.append("PR157 exact head mismatch")
    if subject.get("base_sha") != EXPECTED_BASE:
        errors.append("PR157 base mismatch")
    if subject.get("pr_class") not in ELIGIBLE_CLASSES:
        errors.append("PR157 class is not fallback-eligible")

    remote = data.get("remote_readback", {})
    files = remote.get("changed_files", [])
    observed = {entry.get("path"): entry.get("blob_sha") for entry in files}
    if remote.get("changed_file_count") != len(EXPECTED_REMOTE_FILES):
        errors.append("PR157 changed-file count mismatch")
    if observed != EXPECTED_REMOTE_FILES:
        errors.append("PR157 remote blob inventory mismatch")

    execution = data.get("reconstructed_execution", {})
    matches = execution.get("executable_blob_matches", [])
    if len(matches) != 3 or not all(entry.get("match") is True for entry in matches):
        errors.append("executable blob reconstruction mismatch")
    commands = execution.get("commands", [])
    if len(commands) != 3 or any(command.get("exit_code") != 0 for command in commands):
        errors.append("reconstructed command failed")

    actions = data.get("github_actions_boundary", {})
    if actions.get("classification") != "BILLING_OR_SPENDING_LIMIT_PRE_START":
        errors.append("evidence Actions classification mismatch")
    if actions.get("steps") != 0 or actions.get("runner_id") != 0:
        errors.append("evidence Actions pre-start boundary mismatch")
    if actions.get("github_actions_green") is not False:
        errors.append("evidence cannot claim GitHub Actions Green")
    if actions.get("code_or_test_commands_executed") is not False:
        errors.append("evidence cannot claim Actions commands ran")

    scope = data.get("path_scope", {})
    for key in (
        "product_paths_changed",
        "godot_authoring_paths_changed",
        "addons_gut_paths_changed",
        "audio_asset_paths_changed",
    ):
        if scope.get(key) != 0:
            errors.append("unexpected protected path change")
            break
    if scope.get("unexpected_paths") not in ([], None):
        errors.append("unexpected paths must be empty")

    review = data.get("review", {})
    if review.get("p0_open") != 0 or review.get("p1_open") != 0:
        errors.append("P0/P1 findings must be zero")

    limitations = data.get("limitations", {})
    if limitations.get("godot_runtime") not in {"NOT_RUN", "BLOCKED_UNVERIFIED"}:
        errors.append("Godot runtime must remain NOT_RUN or BLOCKED_UNVERIFIED")
    if limitations.get("gut_cli_junit") not in {"NOT_RUN", "BLOCKED_UNVERIFIED"}:
        errors.append("GUT runtime must remain NOT_RUN or BLOCKED_UNVERIFIED")
    if limitations.get("windows") not in {"NOT_RUN", "BLOCKED_UNVERIFIED"}:
        errors.append("Windows validation must remain NOT_RUN or BLOCKED_UNVERIFIED")
    if limitations.get("android") not in {"NOT_RUN", "BLOCKED_UNVERIFIED"}:
        errors.append("Android validation must remain NOT_RUN or BLOCKED_UNVERIFIED")

    verdict = data.get("verdict", {})
    if verdict.get("local_exact_head") != "PASS_PROCESS_ONLY":
        errors.append("process-only exact-head verdict mismatch")
    if verdict.get("github_actions_green") is not False:
        errors.append("verdict cannot claim GitHub Actions Green")
    if verdict.get("runtime_validation") != "NOT_PROVEN":
        errors.append("runtime validation must remain not proven")
    return errors


def main(argv: Iterable[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--policy", action="store_true")
    parser.add_argument("--evidence", action="store_true")
    args = parser.parse_args(list(argv) if argv is not None else None)
    try:
        policy = load_json(POLICY_PATH)
        evidence = load_json(EVIDENCE_PATH)
    except (OSError, json.JSONDecodeError) as exc:
        print(f"local_exact_head_fallback=FAILED error={exc}")
        return 1

    errors = validate_policy(policy)
    if args.evidence or not args.policy:
        errors.extend(validate_evidence(evidence, policy))
    if errors:
        print("local_exact_head_fallback=FAILED")
        for error in errors:
            print(f"- {error}")
        return 1
    print(
        "local_exact_head_fallback=PASS "
        "scope=PROCESS_ONLY actions_green=FALSE runtime=NOT_PROVEN"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
