from __future__ import annotations

import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[2]
POLICY = ROOT / "docs" / "design" / "APPROVED_V2_EXISTING_LIVE_WORK_FROZEN_IN_PLANNING_2026-07-26.md"
REVIEW = ROOT / "docs" / "reviews" / "2026-07-26-v2-existing-live-work-frozen-in-planning-review.md"
SHARED_HORIZON = ROOT / "docs" / "design" / "APPROVED_V2_PLANNING_SHARED_ONE_SECOND_HORIZON_2026-07-26.md"
HEADSTART = ROOT / "docs" / "design" / "APPROVED_V2_PLANNING_ONE_SECOND_HEADSTART_2026-07-26.md"
SHORT_WORK = ROOT / "docs" / "design" / "APPROVED_V2_PLANNING_SHORT_WORK_COMPLETION_2026-07-26.md"
TIME_RESUME = ROOT / "docs" / "design" / "APPROVED_V2_SIMULTANEOUS_COMMAND_START_AND_TIME_RESUME_2026-07-26.md"
REVALIDATION = ROOT / "docs" / "design" / "APPROVED_V2_PLANNING_REVALIDATION_ALL_OR_NOTHING_2026-07-26.md"
TRANSACTION = ROOT / "docs" / "design" / "APPROVED_V2_TRANSACTION_FOUNDATION_SEQUENCE_2026-07-26.md"


class ExistingLiveWorkFrozenInPlanningContractTests(unittest.TestCase):
    def test_contract_is_routed_to_parent_policies(self) -> None:
        self.assertTrue(POLICY.is_file())
        self.assertTrue(REVIEW.is_file())
        text = POLICY.read_text(encoding="utf-8")
        for parent in (
            SHARED_HORIZON.name,
            HEADSTART.name,
            SHORT_WORK.name,
            TIME_RESUME.name,
            REVALIDATION.name,
            TRANSACTION.name,
        ):
            self.assertIn(parent, text)

    def test_existing_live_work_freeze_markers(self) -> None:
        text = POLICY.read_text(encoding="utf-8")
        for marker in (
            "EXISTING_LIVE_WORK_HEADSTART_ELIGIBILITY: NOT_ELIGIBLE",
            "PLANNING_SESSION_CREATED_WORK_HEADSTART: ELIGIBLE",
            "PLANNING_ENTRY_LIVE_WORK_PROGRESS_SNAPSHOT: PRESERVED",
            "EXISTING_LIVE_WORK_PROGRESS_DURING_PLANNING: FROZEN",
            "EXISTING_LIVE_WORK_COMPLETION_DURING_PLANNING_HORIZON: FORBIDDEN",
            "PLANNING_REENTRY_FREE_PROGRESS: FORBIDDEN",
            "EXISTING_LIVE_WORK_TIMER_REBASE_ON_CONFIRM: FORBIDDEN",
            "POST_CONFIRM_EXISTING_LIVE_WORK_RESUME: FROM_ENTRY_PROGRESS",
            "EXPLICIT_COMMAND_TRANSITION_ON_EXISTING_WORK: ALLOWED_BY_COMMAND_CONTRACT",
            "PASSIVE_HORIZON_PROGRESS_ON_EXISTING_WORK: FORBIDDEN",
            "FAILED_CONFIRM_EXISTING_LIVE_WORK_MUTATION: ZERO",
        ):
            self.assertIn(marker, text)

    def test_entry_progress_and_reentry_exploit_are_explicit(self) -> None:
        text = POLICY.read_text(encoding="utf-8")
        self.assertIn("elapsed_ticks_in_planning = elapsed_ticks_at_entry", text)
        self.assertIn("remaining_ticks_in_planning = remaining_ticks_at_entry", text)
        self.assertIn("진입마다 기존 작업에 1초 추가", text)
        self.assertIn("session을 반복 진입해 작업을 무료 가속", text)
        self.assertIn("병영 6초", text)
        self.assertIn("다시 planning 진입", text)

    def test_new_and_existing_work_use_distinct_progress_rules(self) -> None:
        text = POLICY.read_text(encoding="utf-8")
        self.assertIn("기존 live 작업 A: entry progress에서 정지", text)
        self.assertIn("신규 planning 작업 B: 공유 [0, 1초] horizon에서 진행", text)
        self.assertIn("A elapsed = 6초", text)
        self.assertIn("B elapsed = 1초", text)
        self.assertIn("남은 시간이 0.2초여도 동일", text)
        self.assertIn("planning 중 completion capability 없음", text)

    def test_replay_confirm_failure_and_idempotency_are_safe(self) -> None:
        text = POLICY.read_text(encoding="utf-8")
        self.assertIn("기존 live 작업 progress를 entry 값으로 복원", text)
        self.assertIn("신규 시간 기반 작업에만 공유 horizon 계산", text)
        self.assertIn("existing_elapsed_after_commit = elapsed_ticks_at_entry", text)
        self.assertIn("existing_remaining_after_commit = remaining_ticks_at_entry", text)
        self.assertIn("confirm 처리 wall-clock 시간은 progress에 포함하지 않는다", text)
        self.assertIn("기존 live 작업 progress 변경", text)
        self.assertIn("동일 `planning_commit_transaction_id` 재요청", text)

    def test_review_records_resolution_without_product_authorization(self) -> None:
        policy = POLICY.read_text(encoding="utf-8")
        review = REVIEW.read_text(encoding="utf-8")
        self.assertIn("F-25: RESOLVED", review)
        self.assertIn("FREEZE_EXISTING_LIVE_WORK_AT_ENTRY_PROGRESS", review)
        self.assertIn("EXISTING_LIVE_WORK_HEADSTART_POLICY: RESOLVED_FROZEN_AT_ENTRY_PROGRESS", policy)
        self.assertIn("EXISTING_LIVE_WORK_CANCELLATION_ECONOMICS: REVIEW_PENDING", policy)
        self.assertIn("PRODUCT_CODE_AUTHORIZED: NO", policy)
        self.assertIn("V2_IMPLEMENTATION: NOT_STARTED", policy)


if __name__ == "__main__":
    unittest.main()
