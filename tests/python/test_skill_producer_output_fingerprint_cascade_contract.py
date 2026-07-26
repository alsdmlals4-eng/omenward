from __future__ import annotations

import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[2]
POLICY = ROOT / "docs" / "design" / "APPROVED_V2_PRODUCER_OUTPUT_FINGERPRINT_CASCADE_2026-07-26.md"
REVIEW = ROOT / "docs" / "reviews" / "2026-07-26-v2-producer-output-fingerprint-cascade-review.md"
DEPENDENCY_POLICY = ROOT / "docs" / "design" / "APPROVED_V2_PLANNING_DEPENDENCY_DAG_AND_PROVISIONAL_IDS_2026-07-26.md"
CANCEL_POLICY = ROOT / "docs" / "design" / "APPROVED_V2_PRODUCER_CANCEL_CASCADE_2026-07-26.md"
REVALIDATION_POLICY = ROOT / "docs" / "design" / "APPROVED_V2_PLANNING_REVALIDATION_ALL_OR_NOTHING_2026-07-26.md"
TRANSACTION_POLICY = ROOT / "docs" / "design" / "APPROVED_V2_TRANSACTION_FOUNDATION_SEQUENCE_2026-07-26.md"


class ProducerOutputFingerprintCascadeContractTests(unittest.TestCase):
    def test_contract_is_routed_to_current_parent_policies(self) -> None:
        self.assertTrue(POLICY.is_file())
        self.assertTrue(REVIEW.is_file())
        text = POLICY.read_text(encoding="utf-8")
        for parent in (
            DEPENDENCY_POLICY.name,
            CANCEL_POLICY.name,
            REVALIDATION_POLICY.name,
            TRANSACTION_POLICY.name,
        ):
            self.assertIn(parent, text)

    def test_output_fingerprint_cascade_markers(self) -> None:
        text = POLICY.read_text(encoding="utf-8")
        for marker in (
            "PRODUCER_MODIFICATION_OUTPUT_POLICY: OUTPUT_FINGERPRINT_BRANCH_CASCADE",
            "OUTPUT_CONTRACT_FINGERPRINT: REQUIRED",
            "CONSUMER_COMPATIBILITY_CHECK: REQUIRED",
            "UNCHANGED_OUTPUT_DEPENDENTS: PRESERVED",
            "COMPATIBLE_CHANGED_OUTPUT_DEPENDENTS: PRESERVED_REVALIDATED",
            "INCOMPATIBLE_OUTPUT_BRANCH_CASCADE: PREVIEW_AND_CONFIRM",
            "AUTO_REBIND_ON_OUTPUT_CHANGE: FORBIDDEN",
            "PRODUCER_MODIFICATION_AND_CASCADE: ATOMIC",
            "STALE_MODIFICATION_CONFIRMATION: REJECT_WITH_ZERO_MUTATION",
            "QUEUE_REVISION_INCREMENT_PER_MODIFICATION: EXACTLY_ONCE",
            "POST_MODIFICATION_FULL_QUEUE_REVALIDATION: REQUIRED",
            "output_contract_fingerprint",
            "ProducerModificationImpactPreview",
            "producer_modification_basis_hash",
            "QueueMutationReceipt",
            "queue_mutation_transaction_id",
        ):
            self.assertIn(marker, text)

    def test_only_broken_dependency_branches_are_removed(self) -> None:
        text = POLICY.read_text(encoding="utf-8")
        self.assertIn("broken_direct_consumers", text)
        self.assertIn("reverse_reachable_dependents(broken_direct_consumers)", text)
        self.assertIn("변경된 output과 무관한 dependency branch는 보존", text)
        self.assertIn("호환되는 direct consumer와 그 descendants는 제거하지 않는다", text)
        self.assertIn("output B만 incompatible", text)
        self.assertIn("affected_removal_set = {R3, R5}", text)
        self.assertIn("R2와 R4는 유지", text)

    def test_compatibility_and_identity_rules_are_explicit(self) -> None:
        text = POLICY.read_text(encoding="utf-8")
        self.assertIn("CHANGED_COMPATIBLE", text)
        self.assertIn("CHANGED_INCOMPATIBLE", text)
        self.assertIn("consumer별로 수행", text)
        self.assertIn("Capability 추가처럼 identity를 바꾸지 않는 호환 변경", text)
        self.assertIn("Replacement output은 새 provisional ID", text)
        self.assertIn("기존 consumer reference는 호환되지 않는다", text)
        self.assertIn("자동 연결해서는 안 된다", text)

    def test_stale_confirmation_atomicity_and_revalidation_are_preserved(self) -> None:
        text = POLICY.read_text(encoding="utf-8")
        revalidation = REVALIDATION_POLICY.read_text(encoding="utf-8")
        self.assertIn("STALE_PRODUCER_MODIFICATION_PREVIEW", text)
        self.assertIn("상태 변경 0", text)
        self.assertIn("producer 수정 + 영향 예약 제거를 하나의 원자 mutation", text)
        self.assertIn("queue_revision 정확히 1 증가", text)
        self.assertIn("남은 예약은 새 `queue_revision`에서 전체 DAG", text)
        self.assertIn("동일 `queue_mutation_transaction_id` 재요청", text)
        self.assertIn("PLANNING_BATCH_COMMIT: ATOMIC_ALL_OR_NOTHING", revalidation)

    def test_review_records_resolution_without_product_authorization(self) -> None:
        policy = POLICY.read_text(encoding="utf-8")
        review = REVIEW.read_text(encoding="utf-8")
        self.assertIn("F-18: RESOLVED", review)
        self.assertIn("COMPARE_OUTPUT_CONTRACTS_AND_CASCADE_ONLY_BROKEN_BRANCHES", review)
        self.assertIn("DEPENDENCY_REORDER_POLICY: REVIEW_PENDING", policy)
        self.assertIn("PRODUCT_CODE_AUTHORIZED: NO", policy)
        self.assertIn("V2_IMPLEMENTATION: NOT_STARTED", policy)


if __name__ == "__main__":
    unittest.main()
