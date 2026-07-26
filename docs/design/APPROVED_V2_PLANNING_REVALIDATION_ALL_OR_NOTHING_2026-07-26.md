# 승인된 전술계획 재검증 전체 차단·원자 커밋 계약

- 승인일: 2026-07-26
- 상태: `V2_SPEC_APPROVED / PRODUCT_CODE_NOT_AUTHORIZED`
- 승인 근거: 사용자 권장안 승인
- 상위 책임:
  - `docs/design/APPROVED_V2_SPIN_SESSION_TACTICAL_RESUME_GATE_2026-07-26.md`
  - `docs/design/APPROVED_MAPRUN_STAGE_WAVE_AND_MIDPOINT_CORE_V1.md`
  - `docs/design/APPROVED_V2_TACTICAL_LEGENDARY_RESERVATION_ORDER_2026-07-26.md`
  - `docs/design/APPROVED_V2_TRANSACTION_FOUNDATION_SEQUENCE_2026-07-26.md`

이 문서는 일반 `TACTICAL_PLANNING`에서 `SpinSession` 종료 뒤 또는 예약 큐 변경 뒤 수행한 재검증 결과에 실패 예약이나 미해결 필수 동의가 있을 때의 재개 게이트와 전체 batch 원자 커밋을 소유한다.

이 문서는 상위 재개 게이트 문서의 다음 미결정 상태를 명시적으로 대체한다.

```text
POST_CLOSE_REVALIDATION_FAILURE_POLICY: REVIEW_PENDING
```

## 1. 승인된 핵심 결정

```text
POST_CLOSE_REVALIDATION_FAILURE_POLICY: BLOCK_ENTIRE_PLANNING_COMMIT
ANY_INVALID_RESERVATION_BLOCKS_RESUME: YES
UNRESOLVED_MANDATORY_CONSENT_BLOCKS_RESUME: YES
VALID_RESERVATION_PARTIAL_APPLY: FORBIDDEN
FAILED_RESERVATION_AUTO_CANCEL: FORBIDDEN
PLANNING_QUEUE_WHILE_BLOCKED: PRESERVED_UNAPPLIED
QUEUE_MUTATION_REVALIDATION: FULL_QUEUE_REQUIRED
PLANNING_BATCH_COMMIT: ATOMIC_ALL_OR_NOTHING
PLANNING_COMMIT_FAILURE_ROLLBACK: REQUIRED
```

재검증 대상 예약 중 하나라도 유효하지 않거나 필수 동의가 해결되지 않았으면 `[전투 재개]`와 전체 계획 커밋을 차단한다.

```text
전체 예약 큐 재검증
→ 실패·동의 필요 예약 1개 이상
→ PlanningRevalidationReport = BLOCKED
→ 예약 전체 보존·미적용
→ 비용·식량·건물·spawn 변경 0
→ 플레이어 수정 또는 취소
→ queue_revision 증가
→ 전체 큐 재검증
→ 전부 유효할 때만 전체 batch 커밋 가능
```

## 2. 차단 사유

다음 상태 중 하나라도 존재하면 전체 계획은 커밋할 수 없다.

- 예약 비용을 지불할 수 없음.
- 식량 또는 보관·배치 공간 부족.
- 대상 건물·유닛·라인·앵커·스킬이 존재하지 않거나 상태가 변경됨.
- 건물 소유권·blocked·Tier·업그레이드 선행 조건 불일치.
- 동일 자원 또는 footprint에 대한 예약 충돌.
- 전설 변환 등 필수 동의가 없거나 `conflict_basis_hash`가 stale임.
- 예약 transaction ID 또는 sequence invariant 위반.
- planning basis revision이 현재 authoritative 상태와 일치하지 않음.
- 순수 계획 단계에서 확정 가능한 `PlanningCommitPlan`을 만들 수 없음.

정보성 경고만 존재하고 모든 필수 조건이 충족된 경우에는 차단 사유가 아니다. 필수 동의와 단순 안내는 명시적으로 구분해야 한다.

## 3. 차단 중 상태 보존

차단 상태에서는 예약 큐를 그대로 유지한다.

보존 대상:

```text
planning_session_id
queue_revision
reservation_id
reservation_sequence
command_type
target identifiers
quoted cost and food
validation basis revision
mandatory consent basis
user-authored parameters
```

차단은 예약 성공을 보장하지 않지만 다음 동작은 금지한다.

- 실패 예약 자동 삭제.
- 실패 예약 자동 수정.
- 유효 예약만 먼저 적용.
- 비용 또는 식량 선차감.
- 건물·업그레이드·배치·스킬 일부 실행.
- 실패 예약을 숨기고 전투 재개.
- 이전 재검증 보고서를 현재 결과처럼 재사용.

## 4. UI와 사용자 수정

`PlanningRevalidationReport`는 각 예약에 대해 최소 다음을 표시한다.

```text
reservation_id
reservation_sequence
status
blocking_reason_code
current authoritative requirement
quoted value
current value
required user action
```

예:

```text
예약 1: 병영 건설 — VALID
예약 2: 전설 배치 — BLOCKED / FOOD_INSUFFICIENT
예약 3: 전술 스킬 — VALID
```

UI는 전체 계획이 아직 적용되지 않았음을 명확히 표시한다.

플레이어는 차단 상태에서 다음을 할 수 있다.

- 실패 예약 수정.
- 실패 예약 취소.
- 유효 예약 수정 또는 취소.
- 필수 동의 갱신.
- 예약 순서 변경이 허용된 UI라면 명시적으로 재정렬.

큐가 하나라도 변경되면 `queue_revision`을 증가시키고 기존 `PlanningRevalidationReport`와 동의 basis를 stale로 처리한 뒤 전체 큐를 다시 검증한다.

## 5. 부분 적용 금지

다음 예에서 예약 1과 3이 유효해도 먼저 적용하지 않는다.

```text
예약 1: VALID
예약 2: BLOCKED
예약 3: VALID
```

허용 결과:

```text
예약 1 적용 0
예약 2 적용 0
예약 3 적용 0
전투 재개 0
```

예약 간에는 금화, 식량, footprint, TokenSource, 생존 전설 index, 스킬 대상과 같은 공유 상태 의존성이 존재할 수 있다. 유효 예약만 부분 적용하면 이후 예약의 의미와 플레이어가 본 계획 전체가 달라질 수 있으므로 허용하지 않는다.

## 6. 전체 재검증

전체 재검증은 하나의 authoritative basis에서 수행한다.

필수 basis 예:

```text
planning_session_id
queue_revision
gold_ledger_revision
food_revision
building_state_revision
battlefield_revision
pending_reward_revision
skill_state_revision
alive_legendary_index_revision
spin_session_state = CLOSED
```

재검증은 예약 시점 quoted value만 신뢰하지 않는다. 현재 상태로 모든 예약을 검증하고 전체 계획의 비용·식량·대상·동의를 다시 계산한다.

재검증 결과는 다음 중 하나다.

```text
VALID
BLOCKED
INVARIANT_VIOLATION
```

`VALID`인 경우에만 `PlanningCommitPlan`을 생성할 수 있다.

## 7. 전체 batch 원자 커밋

모든 예약이 유효하면 현재 basis와 큐를 묶은 하나의 `PlanningCommitPlan`을 만든다.

계획에는 최소 다음이 포함된다.

```text
planning_commit_transaction_id
planning_session_id
queue_revision
basis_revision_hash
ordered reservation IDs
aggregate gold debit
aggregate food reservation
building and upgrade mutations
unit deployment mutations
skill mutations
mandatory consent proofs
rollback journal
```

커밋 경계:

```text
최종 basis 재확인
→ 전체 금화·식량·footprint·대상 예약
→ 모든 예약의 commit 준비
→ 전체 상태 전이
→ receipt·인과 로그 기록
→ simulation 재개
```

허용 결과는 다음 두 가지뿐이다.

```text
전체 예약 성공 + PlanningCommitReceipt
또는
전체 상태 변경 0
```

## 8. 커밋 실패와 rollback

사전 검증 뒤 실제 커밋 중 다음 실패가 발생할 수 있다.

- 자원 reservation 충돌.
- 건물 mutation 실패.
- unit spawn 준비 또는 spawn 실패.
- 스킬 대상 invalidation.
- receipt 기록 실패.
- 예상하지 못한 revision 변경.

이 경우 전체 계획을 rollback한다.

rollback 대상:

- 금화 debit.
- 식량 reservation.
- 건물 생성·철거·업그레이드 상태.
- TokenSource와 live 릴 변경.
- PendingReward 소비.
- unit spawn.
- 스킬 비용·쿨다운·효과.
- planning 완료 플래그.
- 전투 재개 상태.

부분 rollback이나 실패 예약만 제외한 재시도는 허용하지 않는다. 플레이어에게 실패 원인을 표시하고 planning 상태를 유지한 뒤 전체 재검증을 요구한다.

## 9. 동시 적용과 결정론

사용자 관점의 계약은 전체 예약의 동시 적용이다. 내부 구현이 결정론적 순서를 사용하더라도 그 순서가 부분 성공을 노출해서는 안 된다.

```text
reservation_sequence 기반 순수 plan 계산
→ 전체 precondition 검증
→ 원자 commit
```

내부 순서, provisional ID와 같은 예약 간 의존성 규칙은 별도 후속 검수에서 확정할 수 있다. 이 문서는 실패 시 전체 rollback과 외부 원자성만 고정한다.

## 10. idempotency

동일 `planning_commit_transaction_id` 재요청은 새 적용을 만들지 않고 기존 `PlanningCommitReceipt`를 반환한다.

중복 요청으로 다음이 발생해서는 안 된다.

- 금화 재차감.
- 건물 중복 생성.
- 업그레이드 중복 적용.
- PendingReward 중복 소비.
- 유닛 중복 spawn.
- 스킬 중복 사용.
- simulation resume 중복 처리.

실패 receipt의 재요청도 자동으로 부분 커밋하지 않는다. 큐 또는 basis가 수정된 경우 새 transaction ID와 새 plan이 필요하다.

## 11. 빈 큐

예약 큐가 비어 있고 다음 조건을 만족하면 재개할 수 있다.

```text
SpinSession CLOSED
AND revalidation completed
AND unresolved mandatory consent = 0
AND invariant violation = 0
```

빈 큐 커밋은 자원·건물·전장 변경 없이 planning 종료와 simulation 재개만 기록한다.

## 12. 자동 검증 계약

최소 다음 사례를 검증한다.

1. 예약 3개 중 1개 비용 부족 → 전체 미적용, 재개 차단.
2. 유효 예약 2개 + 실패 예약 1개 → 유효 예약도 적용 0.
3. 실패 예약 자동 취소 0.
4. 실패 예약 수정 뒤 전체 큐 재검증.
5. 실패 예약 취소 뒤 남은 전체 큐 재검증.
6. stale 전설 변환 동의 → 전체 차단.
7. 모든 예약 유효 → aggregate 비용 1회 차감과 전체 성공 receipt.
8. commit 중 두 번째 mutation 실패 → 첫 mutation과 모든 자원 rollback.
9. spawn 일부 실패 → 모든 spawn·PendingReward·식량 rollback.
10. 동일 commit transaction 재요청 → 중복 적용 0.
11. queue revision 변경 뒤 과거 report로 재개 시도 → 차단.
12. basis revision 변경 뒤 과거 plan 커밋 → 차단·재검증.
13. 빈 큐 → 상태 변경 없이 정상 재개 receipt.
14. 재검증 실패 상태에서 반복 재개 클릭 → 상태 변경 0.

## 13. 현재 상태

```text
PLANNING_REVALIDATION_FAILURE_POLICY: APPROVED_ALL_OR_NOTHING
PLANNING_BATCH_COMMIT: ATOMIC
PARTIAL_APPLY: FORBIDDEN
AUTO_CANCEL_FAILED_RESERVATION: FORBIDDEN
PRODUCT_CODE_AUTHORIZED: NO
V2_IMPLEMENTATION: NOT_STARTED
HUMAN_QA: NOT_RUN
CORE_LOCK_V2: PENDING
```
