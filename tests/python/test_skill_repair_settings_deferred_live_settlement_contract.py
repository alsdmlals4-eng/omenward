from __future__ import annotations

import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[2]
POLICY = ROOT / "docs" / "design" / "APPROVED_V2_REPAIR_SETTINGS_DEFERRED_LIVE_SETTLEMENT_2026-07-26.md"
REVIEW = ROOT / "docs" / "reviews" / "2026-07-26-v2-repair-settings-deferred-live-settlement-review.md"
LEDGER = ROOT / "docs" / "design" / "APPROVED_CORE_V2_INTEGRATED_DECISION_LEDGER_2026-07-25.md"
HORIZON = ROOT / "docs" / "design" / "APPROVED_V2_PLANNING_SHARED_ONE_SECOND_HORIZON_2026-07-26.md"
FROZEN = ROOT / "docs" / "design" / "APPROVED_V2_EXISTING_LIVE_WORK_FROZEN_IN_PLANNING_2026-07-26.md"
REVALIDATION = ROOT / "docs" / "design" / "APPROVED_V2_PLANNING_REVALIDATION_ALL_OR_NOTHING_2026-07-26.md"
TRANSACTION = ROOT / "docs" / "design" / "APPROVED_V2_TRANSACTION_FOUNDATION_SEQUENCE_2026-07-26.md"


class RepairSettingsDeferredLiveSettlementContractTests(unittest.TestCase):
    def test_contract_is_routed_to_parent_policies(self) -> None:
        self.assertTrue(POLICY.is_file())
        self.assertTrue(REVIEW.is_file())
        text = POLICY.read_text(encoding="utf-8")
        for parent in (
            LEDGER.name,
            HORIZON.name,
            FROZEN.name,
            REVALIDATION.name,
            TRANSACTION.name,
        ):
            self.assertIn(parent, text)

    def test_planning_is_settings_only_without_repair_progress(self) -> None:
        text = POLICY.read_text(encoding="utf-8")
        for marker in (
            "REPAIR_PLANNING_POLICY: SETTINGS_ONLY_NO_PROGRESS",
            "REPAIR_PLANNING_HORIZON_ELIGIBILITY: EXCLUDED",
            "PLANNED_REPAIR_WORKER_COUNT: PREVIEW_ONLY",
            "REPAIR_HP_GAIN_DURING_PLANNING: ZERO",
            "REPAIR_GOLD_DEBIT_DURING_PLANNING: ZERO",
            "REPAIR_GOLD_HOLD_DURING_PLANNING: NONE",
        ):
            self.assertIn(marker, text)
        self.assertIn("planning 화면 반복 진입에 따른 무료 치유", text)
        self.assertIn("현실 시간은 repair settlement clock에 포함하지 않는다", text)

    def test_latest_setting_and_replay_are_deterministic(self) -> None:
        text = POLICY.read_text(encoding="utf-8")
        for marker in (
            "REPAIR_SETTING_LATEST_PER_STRUCTURE: WINS",
            "REPAIR_PLANNING_REPLAY: FROM_ENTRY_SNAPSHOT",
            "REPAIR_QUEUE_REVISION_INCREMENT: EXACTLY_ONCE_PER_SETTING_MUTATION",
        ):
            self.assertIn(marker, text)
        self.assertIn("최신 requested worker count", text)
        self.assertIn("HP, 금화, 정산 횟수 또는 worker count가 누적되지 않음", text)
        self.assertIn("`0`은 수리 중지 요청", text)

    def test_confirm_promotes_request_without_early_settlement(self) -> None:
        text = POLICY.read_text(encoding="utf-8")
        for marker in (
            "REPAIR_SETTING_PROMOTION: ATOMIC_WITH_PLANNING_COMMIT",
            "REPAIR_SETTLEMENT_START: FIRST_LIVE_ONE_SECOND_BOUNDARY_AFTER_RESUME",
            "REPAIR_SETTLEMENT_ORDER: APPLY_REQUESTS_THEN_GLOBAL_AFFORDABILITY_THEN_DEBIT_THEN_HEAL",
            "REPAIR_GLOBAL_BUDGET_POLICY: PRESERVED",
        ):
            self.assertIn(marker, text)
        self.assertIn("1초분 금화 즉시 차감", text)
        self.assertIn("1초분 HP 즉시 치유", text)
        self.assertIn("요청 수 적용", text)
        self.assertIn("글로벌 금화 부족 해소", text)
        self.assertIn("금화 차감", text)
        self.assertIn("실제 치유", text)

    def test_preview_does_not_guarantee_affordability(self) -> None:
        text = POLICY.read_text(encoding="utf-8")
        self.assertIn("preview는 정보 제공용", text)
        self.assertIn("다음 정산 결과를 보장하지 않는다", text)
        self.assertIn("별도 escrow로 예약하지 않는다", text)
        self.assertIn("미래 수리 임금을 planned debit으로 차감하지 않는다", text)
        self.assertIn("실제 한계 임금 높은 작업자 우선 제거", text)
        self.assertIn("StableStructureId", text)
        self.assertIn("자동 재고용은 하지 않는다", text)

    def test_invalid_targets_failure_and_duplicates_are_safe(self) -> None:
        text = POLICY.read_text(encoding="utf-8")
        for marker in (
            "FAILED_REPAIR_SETTING_CONFIRM_LIVE_MUTATION: ZERO",
            "REPAIR_SETTING_DUPLICATE_TRANSACTION: SAME_RECEIPT",
            "DANGER_COMBAT_SCOPE: EXCLUDED",
        ):
            self.assertIn(marker, text)
        self.assertIn("전체 확정은 기존 all-or-nothing revalidation 정책에 따라 차단", text)
        self.assertIn("자동으로 다른 구조물에 재지정하지 않는다", text)
        self.assertIn("동일 `planning_commit_transaction_id` 재요청", text)

    def test_review_records_resolution_without_product_authorization(self) -> None:
        policy = POLICY.read_text(encoding="utf-8")
        review = REVIEW.read_text(encoding="utf-8")
        self.assertIn("F-28: RESOLVED", review)
        self.assertIn("F-28_RESULT: APPROVED", review)
        self.assertIn(
            "REPAIR_SETTINGS_POLICY: SETTINGS_ONLY_DEFERRED_TO_FIRST_LIVE_SETTLEMENT",
            review,
        )
        self.assertIn("PRODUCT_CODE_AUTHORIZED: NO", policy)
        self.assertIn("V2_IMPLEMENTATION: NOT_STARTED", policy)
        self.assertIn("FINAL_CODEX_HANDOFF: NOT_AUTHORIZED", policy)


if __name__ == "__main__":
    unittest.main()
