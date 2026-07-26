from __future__ import annotations

import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[2]
POLICY = ROOT / "docs" / "design" / "APPROVED_V2_SIMULTANEOUS_COMMAND_START_AND_TIME_RESUME_2026-07-26.md"
REVIEW = ROOT / "docs" / "reviews" / "2026-07-26-v2-simultaneous-command-start-and-time-resume-review.md"
FIXED_ORDER_POLICY = ROOT / "docs" / "design" / "APPROVED_V2_FIXED_COMMAND_ORDER_AND_SPIN_SNAPSHOT_2026-07-26.md"
REVALIDATION_POLICY = ROOT / "docs" / "design" / "APPROVED_V2_PLANNING_REVALIDATION_ALL_OR_NOTHING_2026-07-26.md"
DEPENDENCY_POLICY = ROOT / "docs" / "design" / "APPROVED_V2_PLANNING_DEPENDENCY_DAG_AND_PROVISIONAL_IDS_2026-07-26.md"
TRANSACTION_POLICY = ROOT / "docs" / "design" / "APPROVED_V2_TRANSACTION_FOUNDATION_SEQUENCE_2026-07-26.md"
MAPRUN_POLICY = ROOT / "docs" / "design" / "APPROVED_MAPRUN_STAGE_WAVE_AND_MIDPOINT_CORE_V1.md"


class SimultaneousCommandStartAndTimeResumeContractTests(unittest.TestCase):
    def test_contract_is_routed_to_current_parent_policies(self) -> None:
        self.assertTrue(POLICY.is_file())
        self.assertTrue(REVIEW.is_file())
        text = POLICY.read_text(encoding="utf-8")
        for parent in (
            FIXED_ORDER_POLICY.name,
            REVALIDATION_POLICY.name,
            DEPENDENCY_POLICY.name,
            TRANSACTION_POLICY.name,
            MAPRUN_POLICY.name,
        ):
            self.assertIn(parent, text)

    def test_time_policy_markers_are_present(self) -> None:
        text = POLICY.read_text(encoding="utf-8")
        for marker in (
            "TACTICAL_CONFIRM_TIME_POLICY: SIMULTANEOUS_START_THEN_NORMAL_RESUME",
            "COMMAND_START_BOUNDARY: SINGLE_AUTHORITATIVE_SIMULATION_BOUNDARY",
            "TIME_BASED_COMMANDS_SHARE_START_TIME: YES",
            "TIME_BASED_COMMAND_AUTO_COMPLETE_ON_CONFIRM: FORBIDDEN",
            "COMMAND_DURATION_FAST_FORWARD_ON_CONFIRM: FORBIDDEN",
            "SEQUENTIAL_DURATION_ACCUMULATION: FORBIDDEN",
            "PLANNING_COMMIT_PROCESSING_TIME_COUNTS_AS_SIMULATION_TIME: NO",
            "TIME_ADVANCE_BEFORE_SUCCESSFUL_RECEIPT: FORBIDDEN",
            "POST_COMMIT_COMPLETION_BASIS: SIMULATION_ELAPSED_TIME",
            "NEW_DEPLOYMENT_ACTION_START: NEXT_SIMULATION_TICK",
            "PREPARATION_SCOPE: EXCLUDED",
            "DANGER_COMBAT_SCOPE: EXCLUDED",
            "command_start_simulation_time",
            "commit_simulation_tick",
            "PlanningCommitReceipt",
        ):
            self.assertIn(marker, text)

    def test_same_start_and_independent_completion_are_explicit(self) -> None:
        text = POLICY.read_text(encoding="utf-8")
        self.assertIn("batch 안의 모든 시간 기반 명령은 동일 `command_start_simulation_time`", text)
        self.assertIn("건설과 업그레이드처럼 duration을 가진 명령은 확정 성공 직후 완료 상태가 아니다", text)
        self.assertIn("current_simulation_time - started_at_simulation_time >= required_duration", text)
        self.assertIn("같은 batch의 시간 기반 명령은 같은 시점에 시작하지만 각자 duration에 따라 독립적으로 완료", text)
        self.assertIn("총 35초를 즉시 진행", text)
        self.assertIn("가장 긴 20초를 즉시 건너뜀", text)

    def test_atomicity_next_tick_and_no_time_acceleration_are_preserved(self) -> None:
        text = POLICY.read_text(encoding="utf-8")
        revalidation = REVALIDATION_POLICY.read_text(encoding="utf-8")
        dependency = DEPENDENCY_POLICY.read_text(encoding="utf-8")
        self.assertIn("새로 배치된 유닛의 이동·공격·AI 행동은 기존 계약대로 다음 simulation tick부터 시작", text)
        self.assertIn("시간은 성공 receipt보다 먼저 진행하지 않는다", text)
        self.assertIn("전체 명령 시작 + receipt + 정상 시간 재개", text)
        self.assertIn("전체 상태 변경 0 + 시간 진행 0", text)
        self.assertIn("PLANNING_BATCH_COMMIT: ATOMIC_ALL_OR_NOTHING", revalidation)
        self.assertIn("TIME_ACCELERATION_IN_VIRTUAL_STATE: FORBIDDEN", dependency)

    def test_idempotency_scope_and_review_status_are_explicit(self) -> None:
        policy = POLICY.read_text(encoding="utf-8")
        review = REVIEW.read_text(encoding="utf-8")
        self.assertIn("동일 `planning_commit_transaction_id` 재요청", policy)
        self.assertIn("Receipt의 `commit_simulation_tick`과 `command_start_simulation_time`은 재요청에서도 동일", policy)
        self.assertIn("준비 화면은 상위 MapRun 계약의 즉시 적용 규칙을 유지", policy)
        self.assertIn("위험 전투는 실시간 즉시 명령 경로를 유지", policy)
        self.assertIn("F-20: RESOLVED", review)
        self.assertIn("SIMULTANEOUS_START_AT_ONE_COMMIT_BOUNDARY", review)
        self.assertIn("PRODUCT_CODE_AUTHORIZED: NO", policy)
        self.assertIn("V2_IMPLEMENTATION: NOT_STARTED", policy)


if __name__ == "__main__":
    unittest.main()
