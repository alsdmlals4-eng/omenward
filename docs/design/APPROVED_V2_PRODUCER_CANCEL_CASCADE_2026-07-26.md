# 승인된 Producer 취소 영향 확인·원자 연쇄 취소 계약

- 승인일: 2026-07-26
- 상태: `V2_SPEC_APPROVED / PRODUCT_CODE_NOT_AUTHORIZED`
- 승인 근거: 사용자 권장안 승인
- 상위 책임:
  - `docs/design/APPROVED_V2_PLANNING_DEPENDENCY_DAG_AND_PROVISIONAL_IDS_2026-07-26.md`
  - `docs/design/APPROVED_V2_PLANNING_REVALIDATION_ALL_OR_NOTHING_2026-07-26.md`
  - `docs/design/APPROVED_V2_TRANSACTION_FOUNDATION_SEQUENCE_2026-07-26.md`

이 문서는 일반 `TACTICAL_PLANNING`에서 provisional output을 생산하는 예약을 취소할 때, 직접·간접 dependent의 영향 범위 계산, 사용자 확인, stale 확인 방지, 원자적 큐 mutation과 전체 재검증을 소유한다.

이 문서는 상위 DAG 문서의 다음 미결정 상태를 명시적으로 대체한다.

```text
PRODUCER_CANCEL_DEPENDENT_UX_POLICY: REVIEW_PENDING
```

## 1. 승인된 핵심 결정

```text
PRODUCER_CANCEL_DEPENDENT_UX_POLICY: EXPLICIT_PREVIEW_THEN_ATOMIC_CASCADE
TRANSITIVE_DEPENDENT_CLOSURE: REQUIRED
SILENT_DEPENDENT_AUTO_DELETE: FORBIDDEN
AUTO_REBIND_TO_OTHER_PRODUCER: FORBIDDEN
DANGLING_DEPENDENT_AFTER_CANCEL: FORBIDDEN
CASCADE_CONFIRMATION: REQUIRED_WHEN_DEPENDENTS_EXIST
CASCADE_CONFIRMATION_BASIS_HASH: REQUIRED
STALE_CASCADE_CONFIRMATION: REJECT_WITH_ZERO_MUTATION
CASCADE_QUEUE_MUTATION: ATOMIC
QUEUE_REVISION_INCREMENT_PER_CASCADE: EXACTLY_ONCE
POST_CASCADE_FULL_QUEUE_REVALIDATION: REQUIRED
```

producer 예약에 dependent가 하나라도 있으면 취소 요청은 즉시 큐를 변경하지 않는다.

```text
producer 취소 요청
→ 현재 dependency graph에서 reverse transitive closure 계산
→ 제거될 producer와 모든 dependent를 미리 표시
→ 사용자 [돌아가기] 또는 [모두 취소]
→ [모두 취소] 시 basis 재확인
→ producer + transitive dependent 원자 삭제
→ queue_revision 1회 증가
→ stale plan·report·동의·mapping 폐기
→ 남은 전체 큐 재검증
```

## 2. 영향 집합 정의

취소 영향 집합은 root producer와 해당 producer에 직접 또는 간접으로 의존하는 모든 예약의 합집합이다.

```text
cascade_removal_set = root_producer ∪ reverse_reachable_dependents(root_producer)
```

예:

```text
R1 병영 건설
└─ R2 건설 사이트 집결지 설정
   └─ R3 집결지 후속 명령

R1 취소 영향 집합 = {R1, R2, R3}
```

다이아몬드 예:

```text
R1 producer
├─ R2 consumer
└─ R3 consumer
   └─ R4 consumer of R2 and R3

R1 취소 영향 집합 = {R1, R2, R3, R4}
```

필수 규칙:

- 직접 dependent뿐 아니라 모든 transitive dependent를 포함한다.
- 이미 다른 이유로 `BLOCKED`인 dependent도 graph상 도달 가능하면 포함한다.
- dependent가 여러 producer를 요구하더라도 취소 대상 producer 입력이 필수라면 dependent를 포함한다.
- 제거 집합 계산은 UI 계층 구조가 아니라 승인된 explicit dependency edge만 사용한다.
- 동일 예약은 영향 집합에 한 번만 포함한다.
- 표시 순서는 `reservation_sequence` 오름차순으로 결정한다.

## 3. 취소 영향 Preview

영향 preview는 실제 상태를 변경하지 않는 순수 계산이다.

`ProducerCancelImpactPreview`는 최소 다음을 포함한다.

```text
planning_session_id
queue_revision
root_producer_reservation_id
root_provisional_outputs
ordered_direct_dependent_ids
ordered_transitive_dependent_ids
ordered_cascade_removal_ids
dependency_edges_in_scope
cascade_confirmation_basis_hash
```

preview 생성 중에는 다음을 변경하지 않는다.

- 예약 큐.
- `queue_revision`.
- 금화·식량.
- 건물·유닛·스킬.
- provisional 또는 actual ID registry.
- `PlanningRevalidationReport`.
- `PlanningCommitPlan`.
- simulation 상태.

## 4. UI와 명시적 동의

영향받는 dependent가 존재하면 UI는 최소 다음을 표시한다.

```text
이 예약을 취소하면 다음 예약도 함께 제거됩니다.

- R2 건설 사이트 집결지 설정
- R3 집결지 후속 명령

[돌아가기] [모두 취소]
```

필수 UX 규칙:

- root producer와 제거될 모든 dependent를 구분 가능하게 표시한다.
- 각 dependent가 어떤 producer 또는 중간 예약을 통해 영향받는지 추적할 수 있어야 한다.
- 제거 수량을 표시한다.
- `[돌아가기]`는 상태 변경 0으로 종료한다.
- `[모두 취소]`만 cascade mutation을 승인한다.
- 단순히 모달을 닫거나 화면을 전환한 것은 동의가 아니다.
- dependent를 유지하려면 취소 전에 별도 큐 mutation으로 다른 producer에 명시적으로 재지정해야 한다.

root producer에 dependent가 없으면 표준 단일 예약 취소를 사용할 수 있다. 이 경우에도 큐 revision 증가와 전체 재검증 규칙은 유지한다.

## 5. 확인 Basis와 Stale 방지

사용자 동의는 preview 당시의 정확한 영향 집합에만 유효하다.

권장 `cascade_confirmation_basis_hash` 입력:

```text
planning_session_id
queue_revision
root_producer_reservation_id
ordered_cascade_removal_ids
dependency_edges_in_scope
root provisional output declarations
```

확인창이 열린 뒤 다음 중 하나라도 바뀌면 기존 동의는 stale이다.

- 예약 추가·삭제·수정·재정렬.
- dependency edge 변경.
- producer output declaration 변경.
- dependent가 다른 producer로 재지정됨.
- `queue_revision` 변경.

stale 확인 처리:

```text
현재 basis hash != preview basis hash
→ STALE_CASCADE_PREVIEW
→ 상태 변경 0
→ 최신 영향 preview 재생성
→ 사용자 재동의 필요
```

과거 동의로 새 dependent를 조용히 삭제해서는 안 된다.

## 6. 공유 Dependency 처리

하나의 dependent가 여러 producer를 요구할 수 있다.

```text
R1 건설 사이트
R2 전술 앵커
R3 requires R1 and R2
```

R1을 취소하면 R3는 R2가 남아 있어도 필수 입력 하나를 잃으므로 cascade removal 대상이다.

R3의 downstream dependent도 모두 제거한다.

금지:

- 남은 producer가 있다는 이유로 R3를 자동 유지.
- R3를 다른 같은 유형 producer에 자동 연결.
- required input을 optional로 임의 변경.
- dangling 상태로 큐에 남겨 전투 재개를 차단.

optional dependency를 지원하려면 command schema가 별도 명시해야 하며, 현재 계약은 모든 선언된 `depends_on_reservation_ids`와 input reference를 필수로 취급한다.

## 7. 원자 Cascade Mutation

사용자가 최신 preview에서 `[모두 취소]`를 선택하면 하나의 `queue_mutation_transaction_id`로 처리한다.

```text
최신 queue_revision 재확인
→ dependency graph invariant 재확인
→ cascade_confirmation_basis_hash 재확인
→ removal set 전체 존재 확인
→ producer + dependent 전체 삭제
→ queue_revision 정확히 1 증가
→ QueueMutationReceipt 기록
→ 전체 큐 재검증
```

허용 결과는 두 가지뿐이다.

```text
전체 제거 성공 + QueueMutationReceipt
또는
전체 상태 변경 0
```

부분 삭제는 금지한다.

예를 들어 R1·R2·R3 중 R2 삭제 처리에서 실패하면 R1만 제거하거나 R3만 남겨서는 안 된다. 큐는 mutation 전 상태로 유지한다.

## 8. Mutation 뒤 Stale 처리

성공한 cascade mutation은 planning queue의 의미를 바꾸므로 다음을 stale로 처리한다.

- 기존 `PlanningRevalidationReport`.
- 기존 `PlanningCommitPlan`.
- 기존 `planning_commit_transaction_id` 후보.
- 과거 mandatory consent basis.
- 과거 legendary conflict consent basis.
- 과거 provisional-to-tentative-actual mapping.
- 제거된 producer의 provisional output reference.

남은 예약은 새 `queue_revision`에서 전체 dependency graph와 authoritative 상태를 다시 검증한다.

변경되지 않은 producer가 결정론적으로 같은 provisional ID 문자열을 다시 산출할 수는 있지만, 과거 report·plan·mapping을 현재 권위로 재사용할 수는 없다.

## 9. 자원과 제품 상태

planning 예약 취소는 아직 미적용인 큐 mutation이다. 따라서 cascade 성공 자체는 다음 authoritative 제품 상태를 변경하지 않는다.

- 글로벌 금화.
- 식량 사용량·상한.
- 건물·업그레이드·철거 상태.
- TokenSource와 live 릴.
- PendingReward.
- 전장 유닛.
- 스킬 비용·쿨다운·효과.
- simulation clock.

예약 단계에서 별도 hold 또는 quote가 존재한다면 해당 planning-only reservation bookkeeping은 전체 제거 집합에 맞춰 원자 해제해야 한다. 실제 자원 debit을 환불하는 흐름으로 표현해서는 안 된다.

## 10. Graph Invariant 실패

preview 또는 confirm 시 graph에 다음 문제가 있으면 cascade를 임의 수행하지 않는다.

- dependency cycle.
- self-dependency.
- 중복 `reservation_sequence`.
- 중복 provisional ID.
- 존재하지 않는 예약을 가리키는 edge.
- producer와 consumer 정체성 불일치.

결과:

```text
INVARIANT_VIOLATION
→ 큐 mutation 0
→ 임의 repair 0
→ 전투 재개 차단
```

손상된 graph에서 임의 DFS 결과로 예약을 삭제해서는 안 된다.

## 11. Idempotency

동일 `queue_mutation_transaction_id` 재요청은 기존 `QueueMutationReceipt`를 반환한다.

중복 요청은 다음을 만들지 않는다.

- `queue_revision` 추가 증가.
- 동일 예약 재삭제 로그.
- report·plan 중복 invalidation 이벤트.
- dependent 재탐색에 따른 다른 결과.
- 사용자 확인 없이 추가 예약 삭제.

성공 receipt는 최소 다음을 보존한다.

```text
queue_mutation_transaction_id
planning_session_id
old_queue_revision
new_queue_revision
root_producer_reservation_id
ordered_removed_reservation_ids
cascade_confirmation_basis_hash
invalidated_artifact_ids
```

## 12. 재지정 후 취소

플레이어가 dependent를 유지하려면 다음 순서를 사용한다.

```text
1. dependent의 input reference를 다른 명시적 producer로 수정
2. queue_revision 증가
3. 전체 DAG 재검증
4. 기존 producer 취소 preview 재생성
5. 최신 영향 집합 확인 뒤 취소
```

producer 취소 confirm 단계에서 자동 재지정하거나 대체 producer를 추론하지 않는다.

## 13. 자동 검증 계약

최소 다음 사례를 검증한다.

1. dependent 없는 producer 취소 → 단일 원자 제거, revision 1 증가.
2. 직접 dependent 2개 → 모두 preview에 표시.
3. 3단계 chain → 모든 transitive dependent 포함.
4. diamond graph → 중복 없이 전체 closure 계산.
5. 여러 producer를 요구하는 consumer → 하나의 필수 producer 취소 시 consumer 포함.
6. `[돌아가기]` → 상태 변경 0.
7. 최신 preview에서 `[모두 취소]` → root와 closure 전체 원자 삭제.
8. confirm 전 큐 변경 → `STALE_CASCADE_PREVIEW`, 상태 변경 0.
9. 과거 확인으로 새 dependent 자동 삭제 0.
10. cascade 중 한 삭제 실패 → 전체 큐 rollback.
11. 성공 뒤 `queue_revision` 정확히 1 증가.
12. 성공 뒤 report·plan·동의·mapping stale 처리와 전체 재검증.
13. dependent 자동 rebind 0.
14. cycle 또는 dangling graph에서 cascade 시도 → invariant violation, mutation 0.
15. 동일 mutation transaction 재요청 → revision·삭제 중복 0.
16. 서로 다른 렌더 프레임률에서도 같은 queue log가 같은 removal set과 receipt 생성.

## 14. 현재 상태

```text
PRODUCER_CANCEL_DEPENDENT_UX_POLICY: APPROVED_EXPLICIT_CASCADE
TRANSITIVE_DEPENDENT_CLOSURE: REQUIRED
CASCADE_CONFIRMATION_BASIS_HASH: REQUIRED
CASCADE_QUEUE_MUTATION: ATOMIC
POST_CASCADE_FULL_QUEUE_REVALIDATION: REQUIRED
PRODUCT_CODE_AUTHORIZED: NO
V2_IMPLEMENTATION: NOT_STARTED
HUMAN_QA: NOT_RUN
CORE_LOCK_V2: PENDING
```
