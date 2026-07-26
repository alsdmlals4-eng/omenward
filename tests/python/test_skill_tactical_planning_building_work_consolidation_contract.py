from __future__ import annotations

import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[2]
POLICY = (
    ROOT
    / "docs"
    / "design"
    / "APPROVED_V2_TACTICAL_PLANNING_BUILDING_WORK_CONSOLIDATED_2026-07-26.md"
)
REVIEW = (
    ROOT
    / "docs"
    / "reviews"
    / "2026-07-26-v2-tactical-planning-building-work-consolidation-review.md"
)

PARENT_POLICIES = (
    "APPROVED_V2_FIXED_COMMAND_ORDER_AND_SPIN_SNAPSHOT_2026-07-26.md",
    "APPROVED_V2_SIMULTANEOUS_COMMAND_START_AND_TIME_RESUME_2026-07-26.md",
    "APPROVED_V2_PLANNING_ONE_SECOND_HEADSTART_2026-07-26.md",
    "APPROVED_V2_DEMOLITION_CANCELS_PLANNED_WORK_2026-07-26.md",
    "APPROVED_V2_PLANNING_SHORT_WORK_COMPLETION_2026-07-26.md",
    "APPROVED_V2_PLANNING_SHARED_ONE_SECOND_HORIZON_2026-07-26.md",
    "APPROVED_V2_EXISTING_LIVE_WORK_FROZEN_IN_PLANNING_2026-07-26.md",
    "APPROVED_V2_EXISTING_WORK_CANCEL_REFUND_2026-07-26.md",
    "APPROVED_V2_COMPLETED_BUILDING_DEMOLITION_REFUND_2026-07-26.md",
    "APPROVED_V2_REPAIR_SETTINGS_DEFERRED_LIVE_SETTLEMENT_2026-07-26.md",
)


class TacticalPlanningBuildingWorkConsolidationContractTests(unittest.TestCase):
    def test_policy_review_and_parent_contracts_exist(self) -> None:
        self.assertTrue(POLICY.is_file())
        self.assertTrue(REVIEW.is_file())
        text = POLICY.read_text(encoding="utf-8")
        for parent_name in PARENT_POLICIES:
            parent = ROOT / "docs" / "design" / parent_name
            self.assertTrue(parent.is_file(), parent_name)
            self.assertIn(parent_name, text)

    def test_pr_lineage_is_summarized(self) -> None:
        text = POLICY.read_text(encoding="utf-8")
        for pr_number in range(82, 92):
            self.assertIn(f"#{pr_number}", text)
        self.assertIn("건설 중 구조물도 현재 허용 최대 HP 범위에서 유료 수리 가능", text)

    def test_current_precedence_markers_are_explicit(self) -> None:
        text = POLICY.read_text(encoding="utf-8")
        for marker in (
            "TACTICAL_PLANNING_BUILDING_WORK_CANON: THIS_DOCUMENT",
            "COMMAND_REORDER_UI: NOT_SUPPORTED",
            "COMMAND_EXECUTION_ORDER: SYSTEM_CREATION_ORDER",
            "ROULETTE_RESULT_RECOMPUTE_FROM_PLANNING_MUTATION: FORBIDDEN",
            "PLANNING_BRANCH_PROJECTION: REQUIRED",
            "LIVE_WORLD_MUTATION_BEFORE_CONFIRM: FORBIDDEN",
            "NEW_WORK_SHARED_PLANNING_HORIZON: ONE_SECOND_PER_SESSION",
            "EXISTING_LIVE_WORK_PASSIVE_PLANNING_PROGRESS: ZERO",
            "EXISTING_CONSTRUCTION_CANCEL_REFUND_RATE: 70_PERCENT",
            "EXISTING_UPGRADE_CANCEL_REFUND_RATE: 50_PERCENT",
            "COMPLETED_BUILDING_DEMOLITION_REFUND_RATE: 40_PERCENT_BASE_CONSTRUCTION_ONLY",
            "COMPLETED_UPGRADE_COST_IN_DEMOLITION_REFUND: EXCLUDED",
            "TACTICAL_PLANNING_DEMOLITION_BRANCH_EFFECT: IMMEDIATE_REMOVE_AND_FREE_NODE",
            "REPAIR_PLANNING_HEAL_AND_DEBIT: ZERO",
            "REPAIR_FIRST_LIVE_SETTLEMENT_AFTER_RESUME: REQUIRED",
            "CONSTRUCTING_STRUCTURE_PAID_REPAIR: ALLOWED",
        ):
            self.assertIn(marker, text)

    def test_legacy_conflicts_are_explicitly_superseded(self) -> None:
        text = POLICY.read_text(encoding="utf-8")
        for legacy_rule in ("GM-42", "GM-44", "GM-46", "GM-47"):
            self.assertIn(legacy_rule, text)
        self.assertIn("기존 진행 건설 취소: 실제 지불액 70%", text)
        self.assertIn("기존 진행 업그레이드 취소: 실제 지불액 50%", text)
        self.assertIn("최초 기본 건설 실제 지불액의 40%만 환급", text)
        self.assertIn("완료된 Tier 업그레이드 지불액은 합산하지 않는다", text)
        self.assertIn("planning branch에서 건물을 즉시 제거하고 node를 비운다", text)

    def test_shared_horizon_and_existing_work_are_separated(self) -> None:
        text = POLICY.read_text(encoding="utf-8")
        for marker in (
            "PLANNING_HORIZON_START: t=0",
            "PLANNING_HORIZON_END: t=1_SECOND",
            "INDEPENDENT_NEW_WORK_START: t=0",
            "DEPENDENT_NEW_WORK_START: MAX_REQUIRED_PRODUCER_COMPLETION_TIME",
            "HORIZON_REPLAY_ACCUMULATION: FORBIDDEN",
            "EXISTING_LIVE_WORK_ENTRY_PROGRESS: IMMUTABLE_DURING_PLANNING",
            "EXISTING_LIVE_WORK_SHARED_HORIZON_ELIGIBILITY: NONE",
            "REPEATED_PLANNING_ENTRY_FREE_PROGRESS: FORBIDDEN",
            "CONFIRM_EXISTING_TIMER_REBASE: FORBIDDEN",
        ):
            self.assertIn(marker, text)

    def test_refund_formulas_and_planned_debit_release_are_locked(self) -> None:
        text = POLICY.read_text(encoding="utf-8")
        self.assertIn(
            "refund = floor(construction_actual_paid_gold * 70 / 100)", text
        )
        self.assertIn("refund = floor(upgrade_actual_paid_gold * 50 / 100)", text)
        self.assertIn(
            "refund = floor(base_construction_actual_paid_gold * 40 / 100)", text
        )
        self.assertIn("completed_upgrade_cost = excluded", text)
        self.assertIn("planned debit release", text)
        self.assertIn("적에 의한 파괴는 환불 없음", text)

    def test_repair_is_deferred_outside_planning_horizon(self) -> None:
        text = POLICY.read_text(encoding="utf-8")
        for marker in (
            "REPAIR_SHARED_ONE_SECOND_HORIZON_ELIGIBILITY: NONE",
            "REPAIR_PLANNING_HP_CHANGE: ZERO",
            "REPAIR_PLANNING_GOLD_DEBIT: ZERO",
            "REPAIR_FUTURE_WAGE_ESCROW: NONE",
            "REPAIR_SETTING_PER_STRUCTURE: LATEST_REQUEST_WINS",
            "REPAIR_SETTING_ZERO_WORKERS: STOP_REQUEST",
        ):
            self.assertIn(marker, text)
        self.assertIn("첫 live 1초 settlement", text)
        self.assertIn("요청 수 적용", text)
        self.assertIn("글로벌 금화 부족 해소", text)
        self.assertIn("금화 차감", text)
        self.assertIn("실제 치유", text)

    def test_constructing_structure_paid_repair_is_safe(self) -> None:
        text = POLICY.read_text(encoding="utf-8")
        for marker in (
            "CONSTRUCTING_STRUCTURE_PAID_REPAIR: ALLOWED",
            "CONSTRUCTING_REPAIR_OWNER_REQUIREMENT: PLAYER_OWNED",
            "CONSTRUCTING_REPAIR_MINIMUM_HP: GREATER_THAN_ZERO",
            "CONSTRUCTING_REPAIR_CHANNEL: PARALLEL_WITH_CONSTRUCTION",
            "CONSTRUCTING_REPAIR_MAX_HP_CAP: CURRENT_CONSTRUCTION_ALLOWED_MAX_HP",
            "CONSTRUCTING_REPAIR_AUTO_FILL_ON_CAP_GROWTH: FORBIDDEN",
            "CONSTRUCTING_REPAIR_ZERO_HP_RESULT: CONSTRUCTION_FAIL_AND_REPAIR_STOP",
            "PROVISIONAL_CONSTRUCTING_REPAIR_TARGET: ALLOWED_WITH_STABLE_PROVISIONAL_ID",
            "PROVISIONAL_REPAIR_HEAL_OR_DEBIT_BEFORE_CONFIRM: ZERO",
            "CONSTRUCTING_REPAIR_FIRST_LIVE_SETTLEMENT: AFTER_CONFIRM_AND_RESUME",
        ):
            self.assertIn(marker, text)
        self.assertIn("construction_allowed_max_hp_at_settlement - current_hp", text)
        self.assertIn(
            "min(requested_repair_hp_after_budget_resolution, repairable_missing_hp)",
            text,
        )
        self.assertIn("과거 수리비로 자동 보충하지 않는다", text)
        self.assertIn("producer cancel cascade로 함께 제거", REVIEW.read_text(encoding="utf-8"))

    def test_stale_atomicity_and_pending_scheduler_order_are_explicit(self) -> None:
        text = POLICY.read_text(encoding="utf-8")
        self.assertIn("STALE_TACTICAL_PLANNING_BUILDING_WORK_PREVIEW", text)
        self.assertIn(
            "CONSTRUCTION_PROGRESS_REPAIR_SETTLEMENT_SAME_TIMESTAMP_ORDER: REVIEW_PENDING",
            text,
        )
        self.assertIn("동일 transaction 재요청은 같은 receipt", text)
        self.assertIn("전체 확정 성공 시 원자 승격", text)

    def test_review_records_approval_without_product_authorization(self) -> None:
        policy = POLICY.read_text(encoding="utf-8")
        review = REVIEW.read_text(encoding="utf-8")
        for marker in (
            "F-29: RESOLVED",
            "F-29_RESULT: APPROVED",
            "TACTICAL_PLANNING_BUILDING_WORK_CONSOLIDATION: APPROVED",
            "CONSTRUCTING_STRUCTURE_PAID_REPAIR_POLICY: APPROVED",
            "F-30",
        ):
            self.assertIn(marker, review)
        self.assertIn("PRODUCT_CODE_AUTHORIZED: NO", policy)
        self.assertIn("V2_IMPLEMENTATION: NOT_STARTED", policy)
        self.assertIn("FINAL_CODEX_HANDOFF: NOT_AUTHORIZED", policy)


if __name__ == "__main__":
    unittest.main()
