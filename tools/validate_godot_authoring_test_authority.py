#!/usr/bin/env python3
"""Validate HiGodot/GUT authority separation and the fail-closed work-entry gate."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Iterable, NamedTuple, Sequence

ROOT = Path(__file__).resolve().parents[1]
DECISION_ID = "OMW-DEC-20260806-TOOLS-HIGODOT-GUT-AUTHORITY-AND-WORK-ENTRY-GATE-V1"
ADOPTION_PATH = Path("docs/operations/GUT_ADOPTION_RECORD.v1.json")
ENTRY_PATH = Path("docs/operations/WORK_ENTRY_GATE_STATE.v1.json")
SPEC_PATH = Path("docs/design/PROPOSED_OMENWARD_HIGODOT_GUT_AUTHORITY_AND_GUT_9_7_1_ADOPTION_2026-08-06.md")
GATE_PATH = Path("docs/operations/OMENWARD_WORK_ENTRY_GATE_2026-08-06.md")
REVIEW_PATH = Path("docs/reviews/ADVERSARIAL_GUT_ADOPTION_AND_WORK_ENTRY_GATE_REVIEW_2026-08-06.md")
PLAN_PATH = Path("docs/superpowers/plans/2026-08-06-gut-adoption-and-work-entry-gate.md")
TEST_PATH = Path("tests/python/test_godot_authoring_test_authority.py")
WORKFLOW_PATH = Path(".github/workflows/validate-godot-authoring-test-authority.yml")
AGENTS_PATH = Path("AGENTS.md")

BOOTSTRAP_ALLOWLIST = frozenset(
    {
        str(ADOPTION_PATH),
        str(ENTRY_PATH),
        str(SPEC_PATH),
        str(GATE_PATH),
        str(REVIEW_PATH),
        str(PLAN_PATH),
        str(TEST_PATH),
        str(WORKFLOW_PATH),
        "tools/validate_godot_authoring_test_authority.py",
        str(AGENTS_PATH),
    }
)

REMEDIATION_EXACT_PATHS = frozenset(
    {
        "docs/PROJECT_CANON_DECISION_LEDGER.md",
        "docs/DECISIONS_PENDING.md",
        "docs/ACTIVE_CONTEXT.md",
        "docs/CURRENT_IMPLEMENTATION_STATUS.md",
        "docs/DOCUMENTATION_MAP.md",
        "docs/DOCUMENT_LIFECYCLE_REGISTRY.md",
        "README.md",
        "AGENTS.md",
        *BOOTSTRAP_ALLOWLIST,
    }
)
REMEDIATION_PREFIXES = ("addons/gut/", "tests/gut/", "scripts/tests/")
FORBIDDEN_REJECTED_IMAGE_STATES = {"READY", "AWAITING", "APPROVED"}


class EntryDecision(NamedTuple):
    allowed: bool
    status: str
    blockers: tuple[str, ...]
    errors: tuple[str, ...] = ()


def load_json(root: Path, relative: Path) -> dict[str, Any]:
    return json.loads((root / relative).read_text(encoding="utf-8"))


def _is_remediation_path(path: str) -> bool:
    return path in REMEDIATION_EXACT_PATHS or path.startswith(REMEDIATION_PREFIXES)


def validate_adoption(data: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    if data.get("decision_id") != DECISION_ID:
        errors.append("GUT adoption Decision ID mismatch")
    if data.get("framework", {}).get("name") != "GUT":
        errors.append("test framework must be GUT")
    if data.get("framework", {}).get("version") != "9.7.1":
        errors.append("GUT version must be pinned to 9.7.1")
    if data.get("framework", {}).get("source_commit") != "aeb5d4f3f7f0a6c9b5e178876d6c99b791fda605":
        errors.append("GUT source commit must match the reviewed 9.7.1 godot_4_7 commit")
    if data.get("compatibility", {}).get("godot_declared") != "4.7.x":
        errors.append("GUT compatibility must declare Godot 4.7.x")

    authorities = data.get("authorities", {})
    higodot = authorities.get("higodot", {})
    gut = authorities.get("gut", {})
    if higodot.get("role") != "HIGODOT_AUTHORING_AUTHORITY":
        errors.append("HiGodot must be the sole authoring authority")
    if not higodot.get("may_mutate_project_files", False):
        errors.append("HiGodot authoring authority must permit scoped project mutation")
    if gut.get("role") != "GUT_TEST_AUTHORITY":
        errors.append("GUT must be the test authority")
    if gut.get("may_mutate_project_files", False):
        errors.append("GUT must not mutate project authoring files")
    if not gut.get("may_write_test_artifacts_only", False):
        errors.append("GUT must be limited to test artifacts and reports")
    if set(higodot.get("owned_surfaces", [])) & set(gut.get("owned_surfaces", [])):
        errors.append("HiGodot and GUT owned surfaces must not overlap")

    provenance = data.get("provenance", {})
    if provenance.get("upstream_addons_tree_sha") == provenance.get("project_addons_tree_sha"):
        if not provenance.get("vendor_tree_exact_match", False):
            errors.append("matching vendor trees must be recorded as exact match")
    elif provenance.get("vendor_tree_exact_match", False):
        errors.append("different vendor trees cannot be recorded as exact match")

    licenses = data.get("licenses", {})
    if licenses.get("gut") != "MIT" or licenses.get("fonts") != "SIL-OFL-1.1":
        errors.append("GUT MIT and bundled font SIL-OFL-1.1 licenses must be recorded")
    if not data.get("consumption_path", {}).get("planned_gut_test_root"):
        errors.append("GUT consumption path is missing")
    if not data.get("removal_and_rollback", {}).get("steps"):
        errors.append("GUT removal and rollback procedure is missing")

    if data.get("adoption_status") == "ACTIVATION_READY":
        if not provenance.get("vendor_tree_exact_match", False):
            errors.append("ACTIVATION_READY requires exact upstream vendor tree match")
        verification = data.get("verification", {})
        if verification.get("godot_import") != "PASS" or verification.get("gut_cli_smoke") != "PASS":
            errors.append("ACTIVATION_READY requires Godot import and GUT CLI smoke PASS")
        if verification.get("project_regression") != "PASS":
            errors.append("ACTIVATION_READY requires project regression PASS")
    return errors


def validate_entry_state(data: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    if data.get("decision_id") != DECISION_ID:
        errors.append("work-entry Decision ID mismatch")
    blockers = tuple(data.get("blockers", []))
    gate_status = data.get("gate_status")
    if gate_status == "READY" and blockers:
        errors.append("gate cannot claim READY while blockers remain")
    if gate_status == "BLOCKED" and not blockers:
        errors.append("blocked gate must name at least one blocker")

    decision_readback = data.get("decision_readback", {})
    if decision_readback.get("sheet_latest_decision") != "OMW-DEC-20260806-PLANNING-BARRACKS-SMOKE-SWEEP-RESULTS-AND-IDENTIFIABILITY-GATE-V1":
        errors.append("Sheet latest approved Decision readback is not the current 4/10 smoke gate")
    if decision_readback.get("decision_ledger_status") != "STALE_CANON_CONFLICT":
        errors.append("Decision Ledger must remain classified as STALE_CANON_CONFLICT until reconciled")
    if decision_readback.get("pending_decisions_status") != "STALE_RELATIVE_TO_PR154_4_OF_10":
        errors.append("DECISIONS_PENDING must remain classified as stale relative to PR154 4/10")

    image = data.get("image_review_readback", {})
    if image.get("ready_count") != 0:
        errors.append("image review READY count must be zero")
    if image.get("awaiting_count") != 0:
        errors.append("image review AWAITING count must be zero")
    if image.get("in_review_not_generated_count") != 1:
        errors.append("image review must preserve one not-generated IN_REVIEW item")
    rejected = image.get("rejected_image_ids", [])
    expected_rejected = {f"OM-IMG-{number:03d}" for number in range(5, 11)}
    actual_rejected = {row.get("image_id") for row in rejected}
    if actual_rejected != expected_rejected:
        errors.append("image rejected/reset set must be OM-IMG-005 through OM-IMG-010")
    for row in rejected:
        if row.get("status") in FORBIDDEN_REJECTED_IMAGE_STATES:
            errors.append("rejected image cannot be READY/AWAITING/APPROVED")
    return errors


def validate_contract(root: Path = ROOT) -> list[str]:
    errors: list[str] = []
    required = (
        ADOPTION_PATH,
        ENTRY_PATH,
        SPEC_PATH,
        GATE_PATH,
        REVIEW_PATH,
        PLAN_PATH,
        TEST_PATH,
        WORKFLOW_PATH,
        AGENTS_PATH,
    )
    for relative in required:
        if not (root / relative).is_file():
            errors.append(f"missing required authority/gate file: {relative.as_posix()}")
    if errors:
        return errors

    adoption = load_json(root, ADOPTION_PATH)
    entry = load_json(root, ENTRY_PATH)
    errors.extend(validate_adoption(adoption))
    errors.extend(validate_entry_state(entry))

    spec = (root / SPEC_PATH).read_text(encoding="utf-8")
    gate = (root / GATE_PATH).read_text(encoding="utf-8")
    agents = (root / AGENTS_PATH).read_text(encoding="utf-8")
    for marker in (
        "HIGODOT_AUTHORING_AUTHORITY",
        "GUT_TEST_AUTHORITY",
        "MUTATION_AUTHORITY_OVERLAP = FORBIDDEN",
        "VENDOR_TREE_MISMATCH",
        "REMOVAL_AND_ROLLBACK_PROCEDURE",
        "WORK_ENTRY_GATE = FAIL_CLOSED",
    ):
        if marker not in spec:
            errors.append(f"adoption spec missing marker: {marker}")
    for marker in ("WORK_ENTRY_GATE = FAIL_CLOSED", "BOOTSTRAP_ONLY_EXCEPTION", "GATE_REMEDIATION_ONLY_EXCEPTION"):
        if marker not in gate:
            errors.append(f"work-entry gate document missing marker: {marker}")
    if "python tools/validate_godot_authoring_test_authority.py --entry" not in agents:
        errors.append("AGENTS.md does not route the mandatory work-entry command")
    return errors


def evaluate_entry(data: dict[str, Any], changed_files: Sequence[str] = ()) -> EntryDecision:
    errors = tuple(validate_entry_state(data))
    blockers = tuple(data.get("blockers", []))
    if errors:
        return EntryDecision(False, "WORK_ENTRY_CONTRACT_INVALID", blockers, errors)
    if data.get("gate_status") == "READY" and not blockers:
        return EntryDecision(True, "WORK_ENTRY_READY", ())

    changed = tuple(path for path in changed_files if path)
    if changed and set(changed).issubset(BOOTSTRAP_ALLOWLIST):
        return EntryDecision(True, "BOOTSTRAP_ONLY_ALLOWED_WHILE_ENTRY_BLOCKED", blockers)
    if changed and all(_is_remediation_path(path) for path in changed):
        return EntryDecision(True, "GATE_REMEDIATION_ONLY_ALLOWED", blockers)
    return EntryDecision(False, "WORK_ENTRY_BLOCKED", blockers)


def main(argv: Iterable[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--contract", action="store_true", help="validate contract truthfulness without opening normal work entry")
    parser.add_argument("--entry", action="store_true", help="evaluate whether the provided changed files may enter work")
    parser.add_argument("--changed-file", action="append", default=[], help="repository-relative changed path; repeatable")
    args = parser.parse_args(list(argv) if argv is not None else None)

    errors = validate_contract(ROOT)
    if errors:
        print("OMENWARD Godot authority/work-entry contract FAILED")
        for error in errors:
            print(f"- {error}")
        return 1

    entry = load_json(ROOT, ENTRY_PATH)
    decision = evaluate_entry(entry, changed_files=tuple(args.changed_file))
    print(f"contract=PASS entry_status={decision.status}")
    for blocker in decision.blockers:
        print(f"blocker={blocker}")
    if args.entry and not decision.allowed:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
