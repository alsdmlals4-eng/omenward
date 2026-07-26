from __future__ import annotations

import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[2]
POLICY = ROOT / "docs" / "design" / "APPROVED_V2_PLANNING_SHORT_WORK_COMPLETION_2026-07-26.md"
REVIEW = ROOT / "docs" / "reviews" / "2026-07-26-v2-planning-short-work-completion-review.md"
HEADSTART = ROOT / "docs" / "design" / "APPROVED_V2_PLANNING_ONE_SECOND_HEADSTART_2026-07-26.md"
TIME_RESUME = ROOT / "docs" / "design" / "APPROVED_V2_SIMULTANEOUS_COMMAND_START_AND_TIME_RESUME_2026-07-26.md"
REVALIDATION = ROOT / "docs" / "design" / "APPROVED_V2_PLANNING_REVALIDATION_ALL_OR_NOTHING_2026-07-26.md"
DEPENDENCY = ROOT / "docs" / "design" / "APPROVED_V2_PLANNING_DEPENDENCY_DAG_AND_PROVISIONAL_IDS_2026-07-26.md"
TRANSACTION = ROOT / "docs" / "design" / "APPROVED_V2_TRANSACTION_FOUNDATION_SEQUENCE_2026-07-26.md"


class PlanningShortWorkCompletionContractTests(unittest.TestCase):
    def test_contract_is_routed_to_current_parent_policies(self) -> None:
        self.assertTrue(POLICY.is_file())
        self.assertTrue(REVIEW.is_file())
        text = POLICY.read_text(encoding="utf-8")
        for parent in (
            HEADSTART.name,
            TIME_RESUME.name,
            REVALIDATION.name,
            DEPENDENCY.name,
            TRANSACTION.name,
        ):
            self.assertIn(parent, text)

    def test_short_work_completion_markers(self) -> None:
        text = POLICY.read_text(encoding="utf-8")
        for marker in (
            "PLANNING_HEADSTART_COMPLETION_THRESHOLD: DURATION_LE_ONE_SECOND",
            "ONE_SECOND_COMPLETION_BOUNDARY: INCLUSIVE",
            "SHORT_TIMED_WORK_BRANCH_RESULT: COMPLETED",
            "SHORT_TIMED_WORK_LIVE_PROMOTION: CONFIRM_ONLY",
            "BRANCH_COMPLETION_CAPABILITIES: AVAILABLE_TO_LATER_COMMANDS",
            "BRANCH_COMPLETION_EXTERNAL_SIDE_EFFECTS: DEFERRED_TO_COMMIT",
            "FIXED_POINT_DURATION_COMPARISON: REQUIRED",
            "PLANNING_REPLAY_COMPLETION_ACCUMULATION: FORBIDDEN",
            "CONFIRM_REAPPLIES_HEADSTART: FORBIDDEN",
            "CONFIRM_DUPLICATES_COMPLETION_EVENT: FORBIDDEN",
            "FAILED_CONFIRM_LIVE_COMPLETION: ZERO",
        ):
            self.assertIn(marker, text)

    def test_inclusive_fixed_point_boundary_is_explicit(self) -> None:
        text = POLICY.read_text(encoding="utf-8")
        self.assertIn("work_elapsed_in_planning >= total_duration", text)
        self.assertIn("`total_duration == 1초`는 완료에 포함", text)
        self.assertIn("total_duration_ticks", text)
        self.assertIn("planning_headstart_ticks", text)
        self.assertIn("부동소수점 근사나 렌더 프레임에 의존하지 않는다", text)
        self.assertIn("duration 0.5초 → branch `COMPLETED`", text)
        self.assertIn("duration 정확히 1초 → inclusive branch `COMPLETED`", text)
        self.assertIn("duration 1초 초과 → branch `IN_PROGRESS`, elapsed 1초", text)

    def test_branch_capability_and_external_side_effect_split(self) -> None:
        text = POLICY.read_text(encoding="utf-8")
        self.assertIn("완료된 short work는 planning branch의 후속 명령 판정에 완료 상태로 사용", text)
        self.assertIn("explicit provisional ID와 output slot", text)
        self.assertIn("branch structural completion", text)
        self.assertIn("live external side-effect execution", text)
        self.assertIn("live TokenSource 등록", text)
        self.assertIn("실제 생산 tick 시작", text)
        self.assertIn("global simulation이 정지", text)

    def test_replay_cancel_confirm_and_idempotency_are_safe(self) -> None:
        text = POLICY.read_text(encoding="utf-8")
        self.assertIn("entry snapshot 복사", text)
        self.assertIn("각 short work에 canonical headstart 한 번 적용", text)
        self.assertIn("기존 branch elapsed에 다시 1초를 더함", text)
        self.assertIn("완료된 short work 명령을 취소하면 완료 상태도 가역적으로 사라진다", text)
        self.assertIn("confirm에서 headstart 재적용 0", text)
        self.assertIn("completion event 중복", text)
        self.assertIn("live completion·registry·resource·time mutation 0", text)
        self.assertIn("동일 `planning_commit_transaction_id` 재요청", text)

    def test_review_records_resolution_without_product_authorization(self) -> None:
        policy = POLICY.read_text(encoding="utf-8")
        review = REVIEW.read_text(encoding="utf-8")
        self.assertIn("F-23: RESOLVED", review)
        self.assertIn("COMPLETE_DURATION_LE_ONE_SECOND_IN_PLANNING_BRANCH", review)
        self.assertIn("MULTI_STAGE_SHORT_WORK_CHAIN_POLICY: REVIEW_PENDING", policy)
        self.assertIn("PRODUCT_CODE_AUTHORIZED: NO", policy)
        self.assertIn("V2_IMPLEMENTATION: NOT_STARTED", policy)


if __name__ == "__main__":
    unittest.main()
