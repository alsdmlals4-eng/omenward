from __future__ import annotations

import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[2]
POLICY = ROOT / "docs" / "design" / "APPROVED_V2_COMPLETED_BUILDING_DEMOLITION_REFUND_2026-07-26.md"
REVIEW = ROOT / "docs" / "reviews" / "2026-07-26-v2-completed-building-demolition-refund-review.md"
EXISTING_REFUND = ROOT / "docs" / "design" / "APPROVED_V2_EXISTING_WORK_CANCEL_REFUND_2026-07-26.md"
DEMOLITION = ROOT / "docs" / "design" / "APPROVED_V2_DEMOLITION_CANCELS_PLANNED_WORK_2026-07-26.md"
CASCADE = ROOT / "docs" / "design" / "APPROVED_V2_PRODUCER_CANCEL_CASCADE_2026-07-26.md"
REVALIDATION = ROOT / "docs" / "design" / "APPROVED_V2_PLANNING_REVALIDATION_ALL_OR_NOTHING_2026-07-26.md"
TRANSACTION = ROOT / "docs" / "design" / "APPROVED_V2_TRANSACTION_FOUNDATION_SEQUENCE_2026-07-26.md"
ECONOMY = ROOT / "docs" / "design" / "APPROVED_STAGE_ECONOMY_AND_BUILDING_COST_BASELINE_V1.md"


class CompletedBuildingDemolitionRefundContractTests(unittest.TestCase):
    def test_contract_is_routed_to_current_parent_policies(self) -> None:
        self.assertTrue(POLICY.is_file())
        self.assertTrue(REVIEW.is_file())
        text = POLICY.read_text(encoding="utf-8")
        for parent in (
            EXISTING_REFUND.name,
            DEMOLITION.name,
            CASCADE.name,
            REVALIDATION.name,
            TRANSACTION.name,
            ECONOMY.name,
        ):
            self.assertIn(parent, text)

    def test_completed_building_demolition_markers_are_explicit(self) -> None:
        text = POLICY.read_text(encoding="utf-8")
        for marker in (
            "COMPLETED_BUILDING_DEMOLITION_REFUND_RATE: 40_PERCENT_BASE_CONSTRUCTION_ONLY",
            "DEMOLITION_REFUND_BASIS: BASE_CONSTRUCTION_ACTUAL_PAID_GOLD",
            "COMPLETED_UPGRADE_COSTS_IN_DEMOLITION_REFUND: EXCLUDED",
            "DEMOLITION_REFUND_ROUNDING: FLOOR_TO_INTEGER_GOLD",
            "DEMOLITION_IMPACT_PREVIEW: REQUIRED",
            "DEMOLITION_CONFIRMATION: REQUIRED",
            "PLANNING_VIRTUAL_DEMOLITION_REFUND_CREDIT: REQUIRED",
            "LIVE_DEMOLITION_REFUND_BEFORE_CONFIRM: FORBIDDEN",
            "DEMOLITION_BRANCH_NODE_RELEASE: IMMEDIATE",
            "ENEMY_DESTRUCTION_DEMOLITION_REFUND: NONE",
        ):
            self.assertIn(marker, text)

    def test_base_payment_lineage_and_rounding_examples_are_locked(self) -> None:
        text = POLICY.read_text(encoding="utf-8")
        self.assertIn(
            "demolition_refund_gold = floor(base_construction_actual_paid_gold * 40 / 100)",
            text,
        )
        self.assertIn("BuildingPaymentLineage", text)
        self.assertIn("base_construction_actual_paid_gold", text)
        self.assertIn("Tier 2·Tier 3 업그레이드가 완료되어도 기본 건설 payment lineage를 덮어쓰지 않는다", text)
        self.assertIn("demolition_refund = floor(40 * 40 / 100) = 16", text)
        self.assertIn("demolition_refund = floor(35 * 40 / 100) = 14", text)
        self.assertIn("base_construction_actual_paid_gold = 0", text)
        self.assertIn("현재 건물 가격, 재건축 가격, 업그레이드 누적 투자액", text)

    def test_completed_upgrades_and_active_upgrade_are_distinct(self) -> None:
        text = POLICY.read_text(encoding="utf-8")
        self.assertIn("45와 70은 이미 완료된 과거 upgrade investment", text)
        self.assertIn("ACTIVE_UPGRADE_PLUS_DEMOLITION_REFUNDS: SEPARATE_LEDGER_ENTRIES", text)
        self.assertIn("ACTIVE_UPGRADE_CANCEL_REFUND_RATE: 50_PERCENT", text)
        self.assertIn("upgrade 취소 환불 = floor(45 * 50 / 100) = 22", text)
        self.assertIn("완공 건물 철거 환급 = floor(40 * 40 / 100) = 16", text)
        self.assertIn("총 예상 credit = 38", text)
        self.assertIn("두 금액은 별도 ledger entry type", text)
        self.assertIn("최종 node를 비운다", text)

    def test_provisional_removal_is_not_live_demolition_refund(self) -> None:
        text = POLICY.read_text(encoding="utf-8")
        self.assertIn(
            "SAME_SESSION_PROVISIONAL_BUILDING_REMOVAL: RELEASE_PLANNED_DEBIT_NOT_REFUND",
            text,
        )
        self.assertIn("40% 철거 환급을 만들지 않는다", text)
        self.assertIn("provisional building 제거는 `PLANNED_DEBIT_RELEASE`", text)
        self.assertIn("같은 비용을 debit release와 refund credit 양쪽에 중복 기록하지 않는다", text)

    def test_preview_cascade_atomicity_stale_and_idempotency_are_safe(self) -> None:
        text = POLICY.read_text(encoding="utf-8")
        for marker in (
            "DEMOLITION_DEPENDENT_CASCADE: REQUIRED",
            "DEMOLITION_QUEUE_MUTATION: ATOMIC",
            "QUEUE_REVISION_INCREMENT_PER_DEMOLITION: EXACTLY_ONCE",
            "DEMOLITION_REPLAY_FROM_ENTRY_SNAPSHOT: REQUIRED",
            "STALE_DEMOLITION_PREVIEW: REJECT_WITH_ZERO_MUTATION",
            "DEMOLITION_DUPLICATE_TRANSACTION: SAME_RECEIPT",
            "CONFIRM_DEMOLITION_PROMOTION: ATOMIC",
            "FAILED_CONFIRM_DEMOLITION_LIVE_MUTATION: ZERO",
        ):
            self.assertIn(marker, text)
        self.assertIn("STALE_COMPLETED_BUILDING_DEMOLITION_PREVIEW", text)
        self.assertIn("node 점유 즉시 해제", text)
        self.assertIn("live refund 0", text)
        self.assertIn("동일 transaction 재요청", text)

    def test_review_records_resolution_without_product_authorization(self) -> None:
        policy = POLICY.read_text(encoding="utf-8")
        review = REVIEW.read_text(encoding="utf-8")
        self.assertIn("F-27: RESOLVED", review)
        self.assertIn("F-27_RESULT: APPROVED", review)
        self.assertIn(
            "COMPLETED_BUILDING_DEMOLITION_REFUND_POLICY: BASE_CONSTRUCTION_ACTUAL_PAID_40_PERCENT",
            review,
        )
        self.assertIn("PRODUCT_CODE_AUTHORIZED: NO", policy)
        self.assertIn("V2_IMPLEMENTATION: NOT_STARTED", policy)
        self.assertIn("FINAL_CODEX_HANDOFF: NOT_AUTHORIZED", policy)


if __name__ == "__main__":
    unittest.main()
