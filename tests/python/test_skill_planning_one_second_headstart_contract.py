from __future__ import annotations

import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[2]
POLICY = ROOT / "docs" / "design" / "APPROVED_V2_PLANNING_ONE_SECOND_HEADSTART_2026-07-26.md"
REVIEW = ROOT / "docs" / "reviews" / "2026-07-26-v2-planning-one-second-headstart-review.md"
FIXED_ORDER_POLICY = ROOT / "docs" / "design" / "APPROVED_V2_FIXED_COMMAND_ORDER_AND_SPIN_SNAPSHOT_2026-07-26.md"
TIME_RESUME_POLICY = ROOT / "docs" / "design" / "APPROVED_V2_SIMULTANEOUS_COMMAND_START_AND_TIME_RESUME_2026-07-26.md"
REVALIDATION_POLICY = ROOT / "docs" / "design" / "APPROVED_V2_PLANNING_REVALIDATION_ALL_OR_NOTHING_2026-07-26.md"
DEPENDENCY_POLICY = ROOT / "docs" / "design" / "APPROVED_V2_PLANNING_DEPENDENCY_DAG_AND_PROVISIONAL_IDS_2026-07-26.md"
MAPRUN_POLICY = ROOT / "docs" / "design" / "APPROVED_MAPRUN_STAGE_WAVE_AND_MIDPOINT_CORE_V1.md"


class PlanningOneSecondHeadstartContractTests(unittest.TestCase):
    def test_contract_is_routed_to_current_parent_policies(self) -> None:
        self.assertTrue(POLICY.is_file())
        self.assertTrue(REVIEW.is_file())
        text = POLICY.read_text(encoding="utf-8")
        for parent in (
            FIXED_ORDER_POLICY.name,
            TIME_RESUME_POLICY.name,
            REVALIDATION_POLICY.name,
            DEPENDENCY_POLICY.name,
            MAPRUN_POLICY.name,
        ):
            self.assertIn(parent, text)

    def test_headstart_contract_markers(self) -> None:
        text = POLICY.read_text(encoding="utf-8")
        for marker in (
            "TACTICAL_PLANNING_STATE_MODEL: TRANSACTIONAL_PLANNING_BRANCH",
            "PLANNING_BRANCH_VISIBLE_STATE: IMMEDIATE",
            "PLANNING_COMMAND_ON_ACCEPT: APPLY_INITIAL_TRANSITION",
            "INSTANT_DEMOLITION_IN_PLANNING_BRANCH: REQUIRED",
            "FREED_NODE_REUSE_IN_SAME_PLANNING_SESSION: ALLOWED",
            "TIMED_WORK_PLANNING_HEADSTART: ONE_SECOND",
            "GLOBAL_SIMULATION_CLOCK_DURING_PLANNING: PAUSED",
            "NON_COMMAND_SYSTEMS_DURING_HEADSTART: FROZEN",
            "PLANNING_EDIT_REBUILD: ENTRY_SNAPSHOT_FULL_REPLAY",
            "AUTHORITATIVE_LEDGER_COMMIT_BEFORE_CONFIRM: FORBIDDEN",
            "CONFIRM_ATOMIC_BRANCH_PROMOTION: REQUIRED",
            "INITIAL_HEADSTART_REAPPLICATION_ON_CONFIRM: FORBIDDEN",
            "POST_PLANNING_PROGRESS_CONTINUATION: FROM_ONE_SECOND",
            "SHORT_DURATION_AT_OR_BELOW_ONE_SECOND_POLICY: REVIEW_PENDING",
            "PlanningEntrySnapshot",
            "PlanningBranchState",
            "PlanningVirtualLedger",
        ):
            self.assertIn(marker, text)

    def test_demolition_construction_and_upgrade_examples_are_explicit(self) -> None:
        text = POLICY.read_text(encoding="utf-8")
        self.assertIn("branch에서 병영 즉시 제거", text)
        self.assertIn("node 즉시 빈 상태", text)
        self.assertIn("새 provisional building 생성", text)
        self.assertIn("건설 진행 1초에서 정지", text)
        self.assertIn("UPGRADING_TO_TIER_2", text)
        self.assertIn("upgrade elapsed = 1.0 second", text)
        self.assertIn("work_elapsed_in_planning = min(1.0 second, total_duration)", text)

    def test_global_time_and_non_command_systems_remain_frozen(self) -> None:
        text = POLICY.read_text(encoding="utf-8")
        self.assertIn("전투 전체 simulation 1초가 아니다", text)
        self.assertIn("명령 10개 입력", text)
        self.assertIn("global simulation 10초 경과", text)
        for frozen_system in (
            "적과 아군 유닛 이동·공격",
            "wave timer와 spawn timer",
            "스킬 cooldown",
            "접전지 진행",
            "simulation clock",
        ):
            self.assertIn(frozen_system, text)

    def test_edit_replay_does_not_accumulate_progress(self) -> None:
        text = POLICY.read_text(encoding="utf-8")
        review = REVIEW.read_text(encoding="utf-8")
        self.assertIn("PlanningEntrySnapshot 복사", text)
        self.assertIn("고정 reservation_sequence 순서로 전체 명령 replay", text)
        self.assertIn("같은 명령 replay가 2초·3초로 증가하지 않음", text)
        self.assertIn("R1 progress는 2초가 아니라 계속 1초", review)
        self.assertIn("철거 취소 시 기존 건물 복원", text)

    def test_confirm_promotes_branch_without_reapplying_first_second(self) -> None:
        text = POLICY.read_text(encoding="utf-8")
        revalidation = REVALIDATION_POLICY.read_text(encoding="utf-8")
        self.assertIn("branch elapsed 1초", text)
        self.assertIn("live elapsed 1초", text)
        self.assertIn("다음 simulation tick부터 1초 이후 진행", text)
        self.assertIn("elapsed를 2초로 만드는 중복 적용", text)
        self.assertIn("receipt 기록 실패도 전체 commit 실패", text)
        self.assertIn("PLANNING_BATCH_COMMIT: ATOMIC_ALL_OR_NOTHING", revalidation)

    def test_review_records_resolution_without_product_authorization(self) -> None:
        policy = POLICY.read_text(encoding="utf-8")
        review = REVIEW.read_text(encoding="utf-8")
        fixed_order = FIXED_ORDER_POLICY.read_text(encoding="utf-8")
        self.assertIn("F-21: RESOLVED", review)
        self.assertIn("TRANSACTIONAL_BRANCH_WITH_COMMAND_LOCAL_ONE_SECOND_HEADSTART", review)
        self.assertIn("AUTHORITATIVE_MUTATION_BEFORE_CONFIRM: FORBIDDEN", fixed_order)
        self.assertIn("confirm 전 transactional planning branch mutation = 필수", review)
        self.assertIn("PRODUCT_CODE_AUTHORIZED: NO", policy)
        self.assertIn("V2_IMPLEMENTATION: NOT_STARTED", policy)


if __name__ == "__main__":
    unittest.main()
