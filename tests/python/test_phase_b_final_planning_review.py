from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def test_phase_b_review_owner_closes_planning_without_new_product_decision() -> None:
    review = read("docs/reviews/PHASE_B_FINAL_PLANNING_REVIEW_2026-08-11.md")
    assert "OMW-DEC-20260811-OPS-PHASE-B-FINAL-PLANNING-REVIEW-V1" in review
    assert "review_result: PASS" in review
    assert "USER_EXPLICIT_PLANNING_COMPLETE_DECLARATION = RECEIVED" in review
    assert "NEW_PRODUCT_DECISION_REQUIRED = FALSE" in review
    assert "IMPLEMENTATION_PACKAGE_DEFINITION_OF_READY = CLOSED" in review
    assert "PHASE_C_GATE = OPEN" in review
    assert "ISSUE176_7_GAPS = IMPLEMENTATION_COMPLETENESS" in review
    assert "FINAL_PRODUCT_NUMERICS = POST_RUNTIME_EVIDENCE_TUNING" in review


def test_current_stage_consumers_use_elite_boss_cadence_not_legacy_danger() -> None:
    current_paths = [
        "README.md",
        "docs/PROJECT_CORE.md",
        "docs/OMENWARD_GDD_CURRENT_CANON.md",
    ]
    for path in current_paths:
        text = read(path)
        assert "DANGER_STAGE_TYPE = REMOVED" in text, path
        assert "ELITE_ESCALATION = EVERY_STAGE_FINAL_WAVE" in text, path
        assert "BOSS_STAGES = 5 / 10 / 15 / 20" in text, path
        assert "Danger = 4 / 9 / 14 / 19" not in text, path
        assert "FIRST_DANGER_INTEGRATION" not in text, path


def test_lifecycle_and_documentation_map_route_latest_product_owners() -> None:
    lifecycle = read("docs/DOCUMENT_LIFECYCLE_REGISTRY.md")
    docmap = read("docs/DOCUMENTATION_MAP.md")
    for text in (lifecycle, docmap):
        assert "APPROVED_OMENWARD_WHOLE_PROJECT_CONTENT_CLOSURE_2026-08-11.md" in text
        assert "APPROVED_OMENWARD_QUALITY_GUARDRAILS_2026-08-11.md" in text
        assert "APPROVED_OMENWARD_ELITE_WAVE_AND_BOSS_CADENCE_2026-08-11.md" in text
        assert "PHASE_B_FINAL_PLANNING_REVIEW_2026-08-11.md" in text
    assert "LEGACY_DANGER_CADENCE_AUTHORITY = NONE" in lifecycle


def test_current_phase_consumers_record_received_gate_and_phase_b_pass() -> None:
    current_paths = [
        "AGENTS.md",
        "docs/ACTIVE_CONTEXT.md",
        "docs/CURRENT_IMPLEMENTATION_STATUS.md",
        "docs/DECISIONS_PENDING.md",
        "docs/DOCUMENTATION_MAP.md",
        "docs/DOCUMENT_LIFECYCLE_REGISTRY.md",
        "docs/ONBOARDING_PLANNING_CURRENT_AUTHORITY.md",
        "docs/PROJECT_GOOGLE_SHEET_WORKBOOK.md",
    ]
    for path in current_paths:
        text = read(path)
        assert "USER_EXPLICIT_PLANNING_COMPLETE_DECLARATION = RECEIVED" in text, path
        assert "PHASE_B_FINAL_PLANNING_REVIEW = PASS" in text, path
        assert "PHASE_C_GATE = OPEN" in text, path


def test_machine_state_opens_phase_c_only_after_phase_b_pass() -> None:
    state = json.loads(read("docs/operations/ACTIVE_INTEGRATED_CONTRACT_STATE.v2.json"))
    phase = state["planning_phase"]
    assert phase["completion_declared"] is True
    assert phase["phase_b_status"] == "PASS"
    assert phase["phase_c_status"] == "READY_TO_ENTER"
    assert state["phase_c_gate"] == "OPEN"
    assert "USER_EXPLICIT_PLANNING_COMPLETE_DECLARATION_REQUIRED" not in state["blocking_reasons"]
    assert "PHASE_B_FINAL_PLANNING_REVIEW_NOT_RUN" not in state["blocking_reasons"]
    assert "ISSUE176_7_RUNTIME_GAPS_OPEN" in state["blocking_reasons"]


def test_phase_b_does_not_fake_runtime_or_numeric_completion() -> None:
    status = read("docs/CURRENT_IMPLEMENTATION_STATUS.md")
    pending = read("docs/DECISIONS_PENDING.md")
    for text in (status, pending):
        assert "PR175 = OPEN_DRAFT" in text
        assert "ISSUE176_APPROVED_RUNTIME_GAPS = 7" in text
        assert "FINAL_PARAMETER_VECTOR = NOT_SELECTED" in text
        assert "FINAL_PRODUCT_NUMERICS = NOT_APPROVED" in text
        assert "USER_REPORTED_GODOT_AI_CURRENT_VERSION = 3.1.4" in text
        assert "GODOT_AI_3_1_4" in text
