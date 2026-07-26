from __future__ import annotations

import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[2]
POLICY = ROOT / "docs" / "design" / "APPROVED_V2_PLANNING_SHARED_ONE_SECOND_HORIZON_2026-07-26.md"
REVIEW = ROOT / "docs" / "reviews" / "2026-07-26-v2-planning-shared-one-second-horizon-review.md"
SHORT_WORK = ROOT / "docs" / "design" / "APPROVED_V2_PLANNING_SHORT_WORK_COMPLETION_2026-07-26.md"
HEADSTART = ROOT / "docs" / "design" / "APPROVED_V2_PLANNING_ONE_SECOND_HEADSTART_2026-07-26.md"
DEPENDENCY = ROOT / "docs" / "design" / "APPROVED_V2_PLANNING_DEPENDENCY_DAG_AND_PROVISIONAL_IDS_2026-07-26.md"
FIXED_ORDER = ROOT / "docs" / "design" / "APPROVED_V2_FIXED_COMMAND_ORDER_AND_SPIN_SNAPSHOT_2026-07-26.md"
REVALIDATION = ROOT / "docs" / "design" / "APPROVED_V2_PLANNING_REVALIDATION_ALL_OR_NOTHING_2026-07-26.md"
TRANSACTION = ROOT / "docs" / "design" / "APPROVED_V2_TRANSACTION_FOUNDATION_SEQUENCE_2026-07-26.md"


class PlanningSharedOneSecondHorizonContractTests(unittest.TestCase):
    def test_contract_is_routed_to_current_parent_policies(self) -> None:
        self.assertTrue(POLICY.is_file())
        self.assertTrue(REVIEW.is_file())
        text = POLICY.read_text(encoding="utf-8")
        for parent in (
            SHORT_WORK.name,
            HEADSTART.name,
            DEPENDENCY.name,
            FIXED_ORDER.name,
            REVALIDATION.name,
            TRANSACTION.name,
        ):
            self.assertIn(parent, text)

    def test_shared_horizon_markers(self) -> None:
        text = POLICY.read_text(encoding="utf-8")
        for marker in (
            "PLANNING_HEADSTART_TIME_MODEL: SHARED_GLOBAL_ONE_SECOND_HORIZON",
            "PLANNING_HORIZON_DURATION: ONE_SECOND",
            "PER_COMMAND_HEADSTART_BUDGET: FORBIDDEN",
            "INDEPENDENT_READY_COMMANDS_START_AT_T0: REQUIRED",
            "INDEPENDENT_COMMANDS_PROGRESS_CONCURRENTLY: REQUIRED",
            "DEPENDENT_COMMAND_EARLIEST_START: REQUIRED_PRODUCER_CAPABILITY_TIME",
            "DEPENDENT_START_TIME: MAX_REQUIRED_PRODUCER_AVAILABLE_TIME",
            "HORIZON_PROGRESS_CLAMP: REQUIRED",
            "MULTI_STAGE_CHAIN_USES_REMAINING_HORIZON_ONLY: REQUIRED",
            "HORIZON_END_ZERO_PROGRESS_START: ALLOWED",
            "GLOBAL_SIMULATION_CLOCK_DURING_HORIZON: PAUSED",
            "PLANNING_REPLAY_HORIZON_ACCUMULATION: FORBIDDEN",
            "CONFIRM_REAPPLIES_HORIZON: FORBIDDEN",
            "POST_CONFIRM_REMAINING_DURATION: TOTAL_MINUS_BRANCH_ELAPSED",
        ):
            self.assertIn(marker, text)

    def test_independent_commands_share_time_without_serialization(self) -> None:
        text = POLICY.read_text(encoding="utf-8")
        self.assertIn("R1, R2, R3 시작", text)
        self.assertIn("R1 elapsed = 1초", text)
        self.assertIn("R2 elapsed = 1초", text)
        self.assertIn("R3 elapsed = 1초", text)
        self.assertIn("독립 명령마다 별도의 1초 budget 부여", text)
        self.assertIn("독립 작업의 시간 예산을 직렬 분할하지 않는다", text)

    def test_dependency_chain_uses_only_remaining_horizon(self) -> None:
        text = POLICY.read_text(encoding="utf-8")
        self.assertIn("R2 시작", text)
        self.assertIn("R2 = IN_PROGRESS, elapsed 0.5초 / 총 0.8초", text)
        self.assertIn("R3 = NOT_STARTED, elapsed 0초", text)
        self.assertIn("R3 elapsed = 0초", text)
        self.assertIn("R4 elapsed 0.1, in progress", text)
        self.assertIn("R1 완료 후 R2 horizon을 새로 시작", text)

    def test_multi_producer_and_fixed_point_scheduling_are_explicit(self) -> None:
        text = POLICY.read_text(encoding="utf-8")
        self.assertIn("required_capability_available_tick_1", text)
        self.assertIn("가장 늦게 준비되는 producer의 available tick", text)
        self.assertIn("CANONICAL_ONE_SECOND_TICKS", text)
        self.assertIn("virtual_available_ticks = max(0, horizon_end_tick - virtual_start_tick)", text)
        self.assertIn("UI 표시 반올림이 scheduling 결과를 바꾸지 않는다", text)

    def test_replay_confirm_and_global_time_are_safe(self) -> None:
        text = POLICY.read_text(encoding="utf-8")
        self.assertIn("PlanningEntrySnapshot 복사", text)
        self.assertIn("단일 [0, 1초] horizon timeline 전체 재생성", text)
        self.assertIn("과거 virtual elapsed를 새 replay에 carry하지 않는다", text)
        self.assertIn("remaining_duration_ticks = total_duration_ticks - branch_virtual_elapsed_ticks", text)
        self.assertIn("confirm 시 horizon이나 완료 event를 재적용하지 않는다", text)
        self.assertIn("live simulation clock", text)
        self.assertIn("planning horizon 1초", text)
        self.assertIn("live world 1초 경과", text)
        self.assertIn("simulation time advance", text)

    def test_review_records_resolution_without_product_authorization(self) -> None:
        policy = POLICY.read_text(encoding="utf-8")
        review = REVIEW.read_text(encoding="utf-8")
        self.assertIn("F-24_RESULT: APPROVED", review)
        self.assertIn("MULTI_STAGE_SHORT_WORK_CHAIN_POLICY: RESOLVED_SHARED_HORIZON", review)
        self.assertIn("기존 live 진행 작업이 planning 진입만으로 1초 headstart를 얻는지 여부", policy)
        self.assertIn("PRODUCT_CODE_AUTHORIZED: NO", policy)
        self.assertIn("V2_IMPLEMENTATION: NOT_STARTED", policy)


if __name__ == "__main__":
    unittest.main()
