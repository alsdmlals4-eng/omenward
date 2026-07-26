from __future__ import annotations

import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[2]
POLICY = ROOT / "docs" / "design" / "APPROVED_V2_EXISTING_WORK_CANCEL_REFUND_2026-07-26.md"
REVIEW = ROOT / "docs" / "reviews" / "2026-07-26-v2-existing-work-cancel-refund-review.md"
FROZEN = ROOT / "docs" / "design" / "APPROVED_V2_EXISTING_LIVE_WORK_FROZEN_IN_PLANNING_2026-07-26.md"
DEMOLITION = ROOT / "docs" / "design" / "APPROVED_V2_DEMOLITION_CANCELS_PLANNED_WORK_2026-07-26.md"
CASCADE = ROOT / "docs" / "design" / "APPROVED_V2_PRODUCER_CANCEL_CASCADE_2026-07-26.md"
REVALIDATION = ROOT / "docs" / "design" / "APPROVED_V2_PLANNING_REVALIDATION_ALL_OR_NOTHING_2026-07-26.md"
TRANSACTION = ROOT / "docs" / "design" / "APPROVED_V2_TRANSACTION_FOUNDATION_SEQUENCE_2026-07-26.md"
ECONOMY = ROOT / "docs" / "design" / "APPROVED_STAGE_ECONOMY_AND_BUILDING_COST_BASELINE_V1.md"


class ExistingWorkCancelRefundContractTests(unittest.TestCase):
    def test_contract_is_routed_to_current_parent_policies(self) -> None:
        self.assertTrue(POLICY.is_file())
        self.assertTrue(REVIEW.is_file())
        text = POLICY.read_text(encoding="utf-8")
        for parent in (
            FROZEN.name,
            DEMOLITION.name,
            CASCADE.name,
            REVALIDATION.name,
            TRANSACTION.name,
            ECONOMY.name,
        ):
            self.assertIn(parent, text)

    def test_fixed_refund_markers_are_explicit(self) -> None:
        text = POLICY.read_text(encoding="utf-8")
        for marker in (
            "EXISTING_CONSTRUCTION_CANCEL_REFUND_RATE: 70_PERCENT",
            "EXISTING_UPGRADE_CANCEL_REFUND_RATE: 50_PERCENT",
            "REFUND_BASIS: ACTUAL_PAID_GOLD_AT_WORK_START",
            "REFUND_ROUNDING: FLOOR_TO_INTEGER_GOLD",
            "PROGRESS_PROPORTIONAL_REFUND: FORBIDDEN",
            "CANCELLATION_IMPACT_PREVIEW: REQUIRED",
            "CANCELLATION_CONFIRMATION: REQUIRED",
            "PLANNING_VIRTUAL_REFUND_CREDIT: REQUIRED",
            "LIVE_REFUND_BEFORE_CONFIRM: FORBIDDEN",
            "CANCELED_WORK_PROGRESS_RECOVERY: FORBIDDEN",
            "ENEMY_DESTRUCTION_REFUND: NONE",
        ):
            self.assertIn(marker, text)

    def test_actual_payment_basis_and_rounding_examples_are_locked(self) -> None:
        text = POLICY.read_text(encoding="utf-8")
        self.assertIn("construction_refund_gold = floor(actual_paid_gold * 70 / 100)", text)
        self.assertIn("upgrade_refund_gold = floor(actual_paid_gold * 50 / 100)", text)
        self.assertIn("actual_paid_gold = 35", text)
        self.assertIn("refund = floor(35 * 70 / 100) = 24", text)
        self.assertIn("actual_paid_gold = 45", text)
        self.assertIn("refund = floor(45 * 50 / 100) = 22", text)
        self.assertIn("현재 건물 가격, 정가, 향후 가격 변경을 사용하지 않는다", text)
        self.assertIn("payment snapshot이 누락되거나 검증 불가능하면", text)

    def test_construction_and_upgrade_cancel_results_are_distinct(self) -> None:
        text = POLICY.read_text(encoding="utf-8")
        self.assertIn("EXISTING_CONSTRUCTION_CANCEL_RESULT: REMOVE_WORK_AND_FREE_NODE", text)
        self.assertIn(
            "EXISTING_UPGRADE_CANCEL_RESULT: RESTORE_PREVIOUS_ACTIVE_TIER_KEEP_NODE_OCCUPIED",
            text,
        )
        self.assertIn("node 점유 해제", text)
        self.assertIn("previous active tier 상태로 복원", text)
        self.assertIn("업그레이드 취소는 건물 철거나 node 해제가 아니다", text)

    def test_planned_debit_release_is_not_live_refund(self) -> None:
        text = POLICY.read_text(encoding="utf-8")
        self.assertIn(
            "PLANNED_SAME_SESSION_WORK_REMOVAL: RELEASE_PLANNED_DEBIT_NOT_REFUND",
            text,
        )
        self.assertIn("planned debit을 삭제할 뿐이며 환불 gold를 새로 만들지 않는다", text)
        self.assertIn("planned debit 해제와 existing live payment 환불", text)
        self.assertIn("live gold는 증가하지 않는다", text)

    def test_cascade_stale_atomicity_and_idempotency_are_safe(self) -> None:
        text = POLICY.read_text(encoding="utf-8")
        for marker in (
            "CANCEL_REFUND_DEPENDENT_CASCADE: REQUIRED",
            "CANCEL_REFUND_QUEUE_MUTATION: ATOMIC",
            "QUEUE_REVISION_INCREMENT_PER_CANCEL: EXACTLY_ONCE",
            "CANCEL_REFUND_REPLAY_FROM_ENTRY_SNAPSHOT: REQUIRED",
            "STALE_CANCEL_REFUND_PREVIEW: REJECT_WITH_ZERO_MUTATION",
            "CANCEL_REFUND_DUPLICATE_TRANSACTION: SAME_RECEIPT",
            "CONFIRM_CANCEL_REFUND_PROMOTION: ATOMIC",
            "FAILED_CONFIRM_CANCEL_REFUND_LIVE_MUTATION: ZERO",
        ):
            self.assertIn(marker, text)
        self.assertIn("STALE_EXISTING_WORK_CANCEL_REFUND_PREVIEW", text)
        self.assertIn("전체 성공", text)
        self.assertIn("전체 상태 변경 0", text)
        self.assertIn("동일 `planning_commit_transaction_id` 재요청", text)

    def test_review_records_resolution_without_product_authorization(self) -> None:
        policy = POLICY.read_text(encoding="utf-8")
        review = REVIEW.read_text(encoding="utf-8")
        self.assertIn("F-26: RESOLVED", review)
        self.assertIn("F-26_RESULT: APPROVED", review)
        self.assertIn(
            "EXISTING_WORK_CANCEL_REFUND_POLICY: FIXED_70_CONSTRUCTION_50_UPGRADE",
            review,
        )
        self.assertIn("PRODUCT_CODE_AUTHORIZED: NO", policy)
        self.assertIn("V2_IMPLEMENTATION: NOT_STARTED", policy)
        self.assertIn("FINAL_CODEX_HANDOFF: NOT_AUTHORIZED", policy)


if __name__ == "__main__":
    unittest.main()
