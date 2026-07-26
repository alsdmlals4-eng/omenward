from __future__ import annotations

import json
import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[2]
REGISTRY = json.loads((ROOT / "docs" / "base" / "SKILL_REGISTRY.json").read_text(encoding="utf-8"))
TACTICAL_LEGENDARY_POLICY = ROOT / "docs" / "design" / "APPROVED_V2_TACTICAL_LEGENDARY_RESERVATION_ORDER_2026-07-26.md"
DANGER_TICK_LEGENDARY_POLICY = ROOT / "docs" / "design" / "APPROVED_V2_DANGER_TICK_LEGENDARY_DEPLOYMENT_ORDER_2026-07-26.md"
DANGER_MULTI_LEGENDARY_POLICY = ROOT / "docs" / "design" / "APPROVED_V2_DANGER_MULTI_LEGENDARY_COMMAND_ORDER_2026-07-26.md"
SPIN_SESSION_RESUME_GATE_POLICY = ROOT / "docs" / "design" / "APPROVED_V2_SPIN_SESSION_TACTICAL_RESUME_GATE_2026-07-26.md"
PLANNING_REVALIDATION_POLICY = ROOT / "docs" / "design" / "APPROVED_V2_PLANNING_REVALIDATION_ALL_OR_NOTHING_2026-07-26.md"
LEGENDARY_PARENT_POLICY = ROOT / "docs" / "design" / "APPROVED_V2_LEGENDARY_DEPLOYMENT_LIMIT_2026-07-26.md"
MAPRUN_POLICY = ROOT / "docs" / "design" / "APPROVED_MAPRUN_STAGE_WAVE_AND_MIDPOINT_CORE_V1.md"
TRANSACTION_FOUNDATION_POLICY = ROOT / "docs" / "design" / "APPROVED_V2_TRANSACTION_FOUNDATION_SEQUENCE_2026-07-26.md"
INTEGRATED_LEDGER = ROOT / "docs" / "design" / "APPROVED_CORE_V2_INTEGRATED_DECISION_LEDGER_2026-07-25.md"


class AdversarialReviewContractTests(unittest.TestCase):
    def test_review_skill_contains_all_three_methods(self) -> None:
        path = ROOT / next(
            skill["path"]
            for skill in REGISTRY["skills"]
            if skill["id"] == "foundation.validation-review"
        )
        text = path.read_text(encoding="utf-8")
        for required in ("Adversarial Review", "Red Teaming", "Critique–Refine"):
            self.assertIn(required, text)

    def test_shared_contract_blocks_false_completion(self) -> None:
        text = (ROOT / "skills" / "SHARED_EXECUTION_CONTRACT.md").read_text(encoding="utf-8")
        self.assertIn("P0·P1이 남으면 완료하지 않는다", text)
        self.assertIn("NOT_RUN", text)
        self.assertIn("문서에 테스트 이름이 존재한다는 사실은 `PROVEN`이 아니다", text)

    def test_review_stack_uses_active_validation_and_freshness_skills(self) -> None:
        stack = REGISTRY["routing"]["review_stack"]
        self.assertEqual(
            stack,
            ["foundation.validation-review", "specialist.canonical-freshness"],
        )
        self.assertNotIn("discipline.integration-review", stack)

    def test_shared_contract_matches_registry_routing_limits(self) -> None:
        text = (ROOT / "skills" / "SHARED_EXECUTION_CONTRACT.md").read_text(encoding="utf-8")
        self.assertIn("`routing.always_on`은 비워", text)
        self.assertIn("지원 Discipline은 최대 1개", text)
        for skill_id in REGISTRY["routing"]["review_stack"]:
            self.assertIn(f"`{skill_id}`", text)

    def test_tactical_legendary_reservation_contract_is_routed(self) -> None:
        self.assertTrue(TACTICAL_LEGENDARY_POLICY.is_file())
        text = TACTICAL_LEGENDARY_POLICY.read_text(encoding="utf-8")
        self.assertIn(LEGENDARY_PARENT_POLICY.name, text)
        self.assertIn(MAPRUN_POLICY.name, text)

    def test_tactical_legendary_reservation_contract_markers(self) -> None:
        text = TACTICAL_LEGENDARY_POLICY.read_text(encoding="utf-8")
        for marker in (
            "TACTICAL_PLANNING_LEGENDARY_RESERVATION: ORDERED_VIRTUAL_SIMULATION",
            "QUEUE_MUTATION_REEVALUATION: REQUIRED",
            "CONSENT_BASIS_HASH: REQUIRED",
            "TACTICAL_RESUME_REVALIDATION: REQUIRED",
            "TACTICAL_BATCH_APPLY: ATOMIC",
            "AUTO_DOWNGRADE_WITH_STALE_CONSENT: FORBIDDEN",
            "reservation_sequence",
            "PlanningCommitPlan",
            "PlanningCommitReceipt",
        ):
            self.assertIn(marker, text)

    def test_tactical_legendary_reservation_preserves_parent_contracts(self) -> None:
        parent = LEGENDARY_PARENT_POLICY.read_text(encoding="utf-8")
        maprun = MAPRUN_POLICY.read_text(encoding="utf-8")
        self.assertIn("PLAYER_ALIVE_LEGENDARY_BATTLEFIELD_CAP: 1", parent)
        self.assertIn("AUTO_DOWNGRADE_WITHOUT_CONSENT: FORBIDDEN", parent)
        self.assertIn("TACTICAL_PLANNING", maprun)
        self.assertIn("[전투 재개]", maprun)
        self.assertIn("비용을 일괄 차감한 뒤 동시에 적용", maprun)

    def test_danger_tick_legendary_contract_is_routed(self) -> None:
        self.assertTrue(DANGER_TICK_LEGENDARY_POLICY.is_file())
        text = DANGER_TICK_LEGENDARY_POLICY.read_text(encoding="utf-8")
        self.assertIn(LEGENDARY_PARENT_POLICY.name, text)
        self.assertIn(MAPRUN_POLICY.name, text)
        self.assertIn(TACTICAL_LEGENDARY_POLICY.name, text)

    def test_danger_tick_legendary_contract_markers(self) -> None:
        text = DANGER_TICK_LEGENDARY_POLICY.read_text(encoding="utf-8")
        for marker in (
            "DANGER_TICK_LEGENDARY_ORDER: COMBAT_SETTLEMENT_BEFORE_DEPLOYMENT_COMMIT",
            "ALIVE_LEGENDARY_INDEX: POST_SETTLEMENT_REVISION",
            "DANGER_DEPLOYMENT_INPUT: QUEUED_NOT_DIRECT_SPAWN",
            "WALL_CLOCK_ORDERING: FORBIDDEN",
            "RENDER_CALLBACK_ORDERING: FORBIDDEN",
            "NEW_SPAWN_COMBAT_ACTIVATION: NEXT_SIMULATION_TICK",
            "command_sequence",
            "command_cutoff_sequence",
            "CombatSettlementReceipt",
            "AliveLegendaryIndexRevision",
            "CONSENT_REQUIRED",
        ):
            self.assertIn(marker, text)

    def test_danger_tick_contract_preserves_revalidation_and_atomicity(self) -> None:
        danger = DANGER_TICK_LEGENDARY_POLICY.read_text(encoding="utf-8")
        parent = LEGENDARY_PARENT_POLICY.read_text(encoding="utf-8")
        maprun = MAPRUN_POLICY.read_text(encoding="utf-8")
        self.assertIn("실제 배치 transaction을 커밋하는 순간 생존 전설 수를 다시 검사", parent)
        self.assertIn("동일 `deployment_transaction_id` 재요청", parent)
        self.assertIn("룰렛 회전·판독·이동·확정·보관·판매·배치 중에도 전투가 진행", maprun)
        self.assertIn("MULTIPLE_NEW_LEGENDARY_COMMANDS_SAME_COMMIT_PHASE: REVIEW_PENDING", danger)
        self.assertIn("제품 코드 승인: `NO`", danger)

    def test_danger_multi_legendary_contract_is_routed(self) -> None:
        self.assertTrue(DANGER_MULTI_LEGENDARY_POLICY.is_file())
        text = DANGER_MULTI_LEGENDARY_POLICY.read_text(encoding="utf-8")
        self.assertIn(LEGENDARY_PARENT_POLICY.name, text)
        self.assertIn(DANGER_TICK_LEGENDARY_POLICY.name, text)
        self.assertIn(MAPRUN_POLICY.name, text)

    def test_danger_multi_legendary_contract_markers(self) -> None:
        text = DANGER_MULTI_LEGENDARY_POLICY.read_text(encoding="utf-8")
        for marker in (
            "DANGER_MULTI_LEGENDARY_COMMAND_ORDER: COMMAND_SEQUENCE_SERIAL_COMMIT",
            "COMMAND_ATOMICITY: PER_COMMAND",
            "ALIVE_LEGENDARY_INDEX_REFRESH_AFTER_SUCCESS: REQUIRED",
            "EARLIER_SUCCESS_ROLLBACK_ON_LATER_FAILURE: FORBIDDEN",
            "FAILED_COMMAND_RESERVES_LEGENDARY_SLOT: NO",
            "STALE_CONSENT_AUTO_DOWNGRADE: FORBIDDEN",
            "DUPLICATE_COMMAND_SEQUENCE: INVARIANT_VIOLATION",
            "NEW_SPAWN_COMBAT_ACTIVATION: NEXT_SIMULATION_TICK",
            "command_sequence",
            "command_cutoff_sequence",
            "AliveLegendaryIndexRevision",
            "conflict_basis_hash",
            "CONSENT_REQUIRED",
        ):
            self.assertIn(marker, text)

    def test_danger_multi_legendary_preserves_parent_safety(self) -> None:
        multi = DANGER_MULTI_LEGENDARY_POLICY.read_text(encoding="utf-8")
        parent = LEGENDARY_PARENT_POLICY.read_text(encoding="utf-8")
        danger = DANGER_TICK_LEGENDARY_POLICY.read_text(encoding="utf-8")
        self.assertIn("PLAYER_ALIVE_LEGENDARY_BATTLEFIELD_CAP: 1", parent)
        self.assertIn("AUTO_DOWNGRADE_WITHOUT_CONSENT: FORBIDDEN", parent)
        self.assertIn("COMBAT_SETTLEMENT_BEFORE_DEPLOYMENT_COMMIT", danger)
        self.assertIn("후속 명령의 `CONSENT_REQUIRED`, 자원 부족 또는 spawn 실패는 앞선 명령의 이미 완료된 receipt를 취소하지 않는다", multi)
        self.assertIn("PRODUCT_CODE_AUTHORIZED: NO", multi)

    def test_spin_session_resume_gate_contract_is_routed(self) -> None:
        self.assertTrue(SPIN_SESSION_RESUME_GATE_POLICY.is_file())
        text = SPIN_SESSION_RESUME_GATE_POLICY.read_text(encoding="utf-8")
        for parent in (
            INTEGRATED_LEDGER.name,
            "APPROVED_ROULETTE_CORE_RULES.md",
            MAPRUN_POLICY.name,
            TRANSACTION_FOUNDATION_POLICY.name,
        ):
            self.assertIn(parent, text)

    def test_spin_session_resume_gate_contract_markers(self) -> None:
        text = SPIN_SESSION_RESUME_GATE_POLICY.read_text(encoding="utf-8")
        for marker in (
            "TACTICAL_RESUME_WITH_OPEN_SPIN_SESSION: BLOCKED",
            "RESUME_COMMAND_REQUIRES_CLOSED_SPIN_SESSION: YES",
            "SPIN_SESSION_AUTO_CONFIRM_ON_RESUME: FORBIDDEN",
            "SPIN_SESSION_AUTO_CANCEL_ON_RESUME: FORBIDDEN",
            "PLANNING_RESERVATIONS_WHILE_BLOCKED: PRESERVED_UNAPPLIED",
            "RESUME_ATTEMPT_STATE_MUTATION: ZERO",
            "POST_SPIN_CLOSE_REVALIDATION: REQUIRED",
            "POST_CLOSE_REVALIDATION_FAILURE_POLICY: REVIEW_PENDING",
            "PlanningRevalidationReport",
            "SPIN_SESSION_OPEN",
            "ConfirmReceipt",
        ):
            self.assertIn(marker, text)

    def test_spin_session_resume_gate_preserves_transaction_boundaries(self) -> None:
        gate = SPIN_SESSION_RESUME_GATE_POLICY.read_text(encoding="utf-8")
        transaction = TRANSACTION_FOUNDATION_POLICY.read_text(encoding="utf-8")
        ledger = INTEGRATED_LEDGER.read_text(encoding="utf-8")
        maprun = MAPRUN_POLICY.read_text(encoding="utf-8")
        self.assertIn("미확정 `SpinSession`은 닫고 재개할 수 있다", ledger)
        self.assertIn("건설·업그레이드·철거·새 회전은 금지", ledger)
        self.assertIn("SpinSession close", transaction)
        self.assertIn("[전투 재개]", maprun)
        self.assertIn("재검증 완료 전 전투 simulation이 재개되지 않음", gate)
        self.assertIn("재검증 실패 예약을 유지·취소할지, 전체 batch를 차단할지는 별도 검수 결정", gate)
        self.assertIn("PRODUCT_CODE_AUTHORIZED: NO", gate)

    def test_planning_revalidation_all_or_nothing_contract_is_routed(self) -> None:
        self.assertTrue(PLANNING_REVALIDATION_POLICY.is_file())
        text = PLANNING_REVALIDATION_POLICY.read_text(encoding="utf-8")
        for parent in (
            SPIN_SESSION_RESUME_GATE_POLICY.name,
            MAPRUN_POLICY.name,
            TACTICAL_LEGENDARY_POLICY.name,
            TRANSACTION_FOUNDATION_POLICY.name,
        ):
            self.assertIn(parent, text)

    def test_planning_revalidation_all_or_nothing_markers(self) -> None:
        text = PLANNING_REVALIDATION_POLICY.read_text(encoding="utf-8")
        for marker in (
            "POST_CLOSE_REVALIDATION_FAILURE_POLICY: BLOCK_ENTIRE_PLANNING_COMMIT",
            "ANY_INVALID_RESERVATION_BLOCKS_RESUME: YES",
            "UNRESOLVED_MANDATORY_CONSENT_BLOCKS_RESUME: YES",
            "VALID_RESERVATION_PARTIAL_APPLY: FORBIDDEN",
            "FAILED_RESERVATION_AUTO_CANCEL: FORBIDDEN",
            "PLANNING_QUEUE_WHILE_BLOCKED: PRESERVED_UNAPPLIED",
            "QUEUE_MUTATION_REVALIDATION: FULL_QUEUE_REQUIRED",
            "PLANNING_BATCH_COMMIT: ATOMIC_ALL_OR_NOTHING",
            "PLANNING_COMMIT_FAILURE_ROLLBACK: REQUIRED",
            "PlanningRevalidationReport",
            "PlanningCommitPlan",
            "PlanningCommitReceipt",
            "planning_commit_transaction_id",
            "queue_revision",
            "basis_revision_hash",
        ):
            self.assertIn(marker, text)

    def test_planning_revalidation_supersedes_pending_without_scope_expansion(self) -> None:
        policy = PLANNING_REVALIDATION_POLICY.read_text(encoding="utf-8")
        gate = SPIN_SESSION_RESUME_GATE_POLICY.read_text(encoding="utf-8")
        maprun = MAPRUN_POLICY.read_text(encoding="utf-8")
        self.assertIn("POST_CLOSE_REVALIDATION_FAILURE_POLICY: REVIEW_PENDING", gate)
        self.assertIn("명시적으로 대체", policy)
        self.assertIn("비용을 일괄 차감한 뒤 동시에 적용", maprun)
        self.assertIn("실패 예약 자동 삭제", policy)
        self.assertIn("전체 예약 성공 + PlanningCommitReceipt", policy)
        self.assertIn("전체 상태 변경 0", policy)
        self.assertIn("PRODUCT_CODE_AUTHORIZED: NO", policy)


if __name__ == "__main__":
    unittest.main()
