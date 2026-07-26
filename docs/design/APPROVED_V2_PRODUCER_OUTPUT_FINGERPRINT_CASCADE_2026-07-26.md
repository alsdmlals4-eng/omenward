# 승인된 Producer Output Fingerprint·영향 가지 Cascade 계약

- 승인일: 2026-07-26
- 상태: `V2_SPEC_APPROVED / PRODUCT_CODE_NOT_AUTHORIZED`
- 승인 근거: 사용자 권장안 승인
- 상위 책임:
  - `docs/design/APPROVED_V2_PLANNING_DEPENDENCY_DAG_AND_PROVISIONAL_IDS_2026-07-26.md`
  - `docs/design/APPROVED_V2_PRODUCER_CANCEL_CASCADE_2026-07-26.md`
  - `docs/design/APPROVED_V2_PLANNING_REVALIDATION_ALL_OR_NOTHING_2026-07-26.md`
  - `docs/design/APPROVED_V2_TRANSACTION_FOUNDATION_SEQUENCE_2026-07-26.md`

이 문서는 일반 `TACTICAL_PLANNING`에서 provisional output producer 예약의 내용이 수정될 때, output별 consumer-visible 계약 비교, 호환성 판정, 영향 dependency 가지 계산, 사용자 확인, 원자 큐 mutation과 전체 재검증을 소유한다.

이 문서는 producer 전체 취소가 아니라 producer 예약을 유지한 채 일부 output declaration, lifecycle, capability 또는 target semantics가 변경되는 경우에 적용한다.

## 1. 승인된 핵심 결정

```text
PRODUCER_MODIFICATION_OUTPUT_POLICY: OUTPUT_FINGERPRINT_BRANCH_CASCADE
OUTPUT_CONTRACT_FINGERPRINT: REQUIRED
CONSUMER_COMPATIBILITY_CHECK: REQUIRED
UNCHANGED_OUTPUT_DEPENDENTS: PRESERVED
COMPATIBLE_CHANGED_OUTPUT_DEPENDENTS: PRESERVED_REVALIDATED
INCOMPATIBLE_OUTPUT_BRANCH_CASCADE: PREVIEW_AND_CONFIRM
AUTO_REBIND_ON_OUTPUT_CHANGE: FORBIDDEN
PRODUCER_MODIFICATION_AND_CASCADE: ATOMIC
STALE_MODIFICATION_CONFIRMATION: REJECT_WITH_ZERO_MUTATION
QUEUE_REVISION_INCREMENT_PER_MODIFICATION: EXACTLY_ONCE
POST_MODIFICATION_FULL_QUEUE_REVALIDATION: REQUIRED
```

Producer 수정은 다음 순서로 처리한다.

```text
현재 producer output 계약 캡처
→ 제안된 producer output 계약 계산
→ output별 fingerprint와 consumer compatibility 비교
→ 호환되지 않는 direct consumer 식별
→ 해당 consumer의 transitive descendants만 영향 집합 계산
→ 영향 집합 preview와 사용자 확인
→ producer 수정 + 영향 예약 제거를 하나의 원자 mutation으로 적용
→ queue_revision 정확히 1회 증가
→ stale artifact 폐기
→ 남은 전체 큐 재검증
```

## 2. Output Contract Fingerprint

각 producer output은 consumer가 관찰하거나 요구할 수 있는 계약을 정규화한 `output_contract_fingerprint`를 가진다.

Fingerprint 입력은 최소 다음을 포함한다.

```text
producer_reservation_id
output_slot
provisional_id_basis
object_kind
lifecycle_state
sorted provided_capabilities
consumer_visible_target_semantics
output_schema_version
```

필수 규칙:

- 필드 직렬화 순서와 capability 정렬은 결정론적이어야 한다.
- UI 표시명, 렌더 순서, wall-clock timestamp는 fingerprint 입력이 아니다.
- 같은 계약은 같은 fingerprint를 생성해야 한다.
- 다른 `object_kind`, provisional identity 또는 target semantics를 같은 fingerprint로 축약해서는 안 된다.
- fingerprint는 호환성 판정을 위한 증거이며 실제 객체 ID가 아니다.

## 3. Output 분류

수정 전후 output은 다음 중 하나로 분류한다.

```text
UNCHANGED
ADDED
REMOVED
CHANGED_COMPATIBLE
CHANGED_INCOMPATIBLE
```

### UNCHANGED

Fingerprint가 동일하다. 기존 dependent reference와 provisional ID를 유지한다.

### ADDED

기존 consumer가 없으므로 cascade 대상이 아니다. 새 output은 결정론적 provisional ID를 발급한다.

### REMOVED

해당 output을 참조하는 모든 direct consumer는 호환되지 않는다.

### CHANGED_COMPATIBLE

Fingerprint는 달라졌지만 현재 모든 direct consumer의 명시적 요구를 계속 만족한다.

예:

- 기존 capability를 유지하면서 새 capability를 추가.
- consumer가 요구하지 않는 부가 메타데이터 변경.
- 동일 provisional identity와 target semantics를 유지하면서 consumer requirement를 약화시키지 않는 변경.

이 경우 dependent를 제거하지 않고 전체 재검증한다.

### CHANGED_INCOMPATIBLE

하나 이상의 direct consumer 요구를 더 이상 만족하지 않는다. 해당 consumer에서 시작하는 dependency 가지에 cascade preview가 필요하다.

## 4. Consumer Compatibility 판정

Direct consumer input reference는 최소 다음 조건으로 제안된 output과 비교한다.

```text
expected_producer_reservation_id matches
expected output_slot matches
expected provisional identity remains stable
expected_object_kind matches
required_lifecycle_state is satisfied
required_capabilities are all provided
required target semantics are preserved
```

호환성 판정은 output 전체가 아니라 consumer별로 수행한다.

같은 changed output을 참조하는 consumer 중 일부만 새 계약을 만족할 수 있다. 이 경우 만족하는 consumer 가지는 유지하고, 만족하지 않는 consumer 가지에만 cascade를 적용한다.

다음은 호환되지 않는다.

- output 삭제.
- output slot 변경으로 기존 참조가 사라짐.
- provisional ID basis 또는 object identity 변경.
- `object_kind` 변경.
- required lifecycle보다 약한 lifecycle로 변경.
- consumer가 요구하는 capability 제거.
- 위치·라인·앵커처럼 consumer가 요구한 target semantics 변경.

암묵적으로 비슷한 다른 output이나 같은 유형 producer를 찾아 자동 연결해서는 안 된다.

## 5. 영향 가지 계산

호환되지 않는 direct consumer 집합을 `broken_direct_consumers`라고 한다.

```text
affected_removal_set =
  broken_direct_consumers
  ∪ reverse_reachable_dependents(broken_direct_consumers)
```

필수 규칙:

- 변경된 output과 무관한 dependency branch는 보존한다.
- 호환되는 direct consumer와 그 descendants는 제거하지 않는다.
- 하나의 descendant가 여러 broken branch에서 도달되어도 한 번만 포함한다.
- 필수 dependency 하나를 잃는 shared consumer는 영향 집합에 포함한다.
- 영향 표시 순서는 `reservation_sequence` 오름차순이다.
- explicit dependency edge만 사용하며 UI 계층이나 이름 유사성으로 범위를 확장하지 않는다.

예:

```text
R1 producer
├─ output A → R2 → R4
└─ output B → R3 → R5

output B만 incompatible
→ affected_removal_set = {R3, R5}
→ R2와 R4는 유지
```

## 6. 수정 영향 Preview와 사용자 동의

`ProducerModificationImpactPreview`는 실제 상태를 변경하지 않는 순수 계산이다.

최소 필드:

```text
planning_session_id
queue_revision
producer_reservation_id
old_output_fingerprints
proposed_output_fingerprints
output_classifications
broken_direct_consumer_ids
ordered_affected_removal_ids
dependency_edges_in_scope
producer_modification_basis_hash
```

영향 예약이 존재하면 UI는 최소 다음 선택을 제공한다.

```text
이 수정으로 다음 예약이 더 이상 유효하지 않아 제거됩니다.

- R3 전술 앵커 후속 명령
- R5 앵커 연계 스킬

[수정 취소] [수정하고 영향 예약 제거]
```

- `[수정 취소]`는 상태 변경 0으로 종료한다.
- `[수정하고 영향 예약 제거]`만 producer 수정과 cascade를 승인한다.
- 모달 닫기, 화면 이동, 과거 확인은 동의가 아니다.
- 영향받지 않는 예약도 제거될 것처럼 표시해서는 안 된다.

영향 예약이 없으면 별도 destructive cascade 확인 없이 producer 수정 mutation을 진행할 수 있다. 단, 전체 큐 재검증은 생략하지 않는다.

## 7. 호환 변경과 Provisional ID

호환되는 output의 identity가 유지되는 경우 기존 provisional ID를 유지한다.

```text
same producer_reservation_id
AND same output_slot
AND same provisional_id_basis
AND same object_kind identity
```

다음 변경은 output replacement로 취급한다.

- output slot 교체.
- provisional ID basis 변경.
- `object_kind` 변경.
- consumer-visible target identity 변경.

Replacement output은 새 provisional ID를 사용하며 기존 consumer reference는 호환되지 않는다.

Capability 추가처럼 identity를 바꾸지 않는 호환 변경은 기존 provisional ID를 유지할 수 있다.

## 8. 확인 Basis와 Stale 방지

사용자 동의는 preview 당시의 producer 수정안과 영향 집합에만 유효하다.

`producer_modification_basis_hash` 입력은 최소 다음을 포함한다.

```text
planning_session_id
queue_revision
producer_reservation_id
old output fingerprints
proposed output fingerprints
ordered affected removal IDs
dependency edges in scope
```

확인창이 열린 뒤 다음 중 하나라도 바뀌면 과거 동의는 stale이다.

- producer 수정 내용 변경.
- 예약 추가·삭제·수정·재정렬.
- dependency edge 변경.
- output declaration 또는 consumer requirement 변경.
- `queue_revision` 변경.

처리:

```text
current basis hash != preview basis hash
→ STALE_PRODUCER_MODIFICATION_PREVIEW
→ 상태 변경 0
→ 최신 preview 재생성
→ 사용자 재동의 필요
```

과거 동의로 새로 영향받은 예약을 삭제해서는 안 된다.

## 9. 원자 Producer Modification Mutation

승인된 수정은 하나의 `queue_mutation_transaction_id`로 처리한다.

```text
최신 queue_revision 재확인
→ dependency graph invariant 재확인
→ producer_modification_basis_hash 재확인
→ producer output declarations 수정
→ affected_removal_set 전체 삭제
→ queue_revision 정확히 1 증가
→ QueueMutationReceipt 기록
→ stale artifact 폐기
→ 전체 큐 재검증
```

허용 결과는 다음 두 가지뿐이다.

```text
producer 수정과 영향 예약 제거 전체 성공 + QueueMutationReceipt
또는
전체 상태 변경 0
```

금지:

- producer만 수정하고 broken dependent를 남김.
- dependent 일부만 삭제.
- producer 수정 실패 뒤 dependent만 삭제.
- 호환 branch까지 삭제.
- 다른 producer로 자동 rebind.

## 10. Mutation 뒤 Stale 처리

성공한 mutation은 다음을 stale로 처리한다.

- 기존 `PlanningRevalidationReport`.
- 기존 `PlanningCommitPlan`.
- 기존 planning commit transaction 후보.
- 과거 mandatory consent basis.
- 과거 legendary conflict consent basis.
- 변경·삭제된 output의 provisional mapping.
- 변경된 producer를 포함한 과거 dependency fingerprint cache.

남은 예약은 새 `queue_revision`에서 전체 DAG, 자원, lifecycle, capability와 authoritative 상태를 다시 검증한다.

호환 branch가 보존되어도 재검증 결과 비용·위치·공간·식량 등의 다른 조건에서 실패할 수 있다. 이 경우 기존 전체 계획 차단 정책을 적용한다.

## 11. Graph Invariant 실패

다음 상태에서는 producer 수정을 임의 적용하지 않는다.

- dependency cycle 또는 self-dependency.
- 중복 `reservation_sequence`.
- 중복 provisional ID.
- 존재하지 않는 producer·consumer reference.
- output slot 또는 object identity 충돌.
- fingerprint 정규화 실패.

결과:

```text
INVARIANT_VIOLATION
→ queue mutation 0
→ 자동 repair 0
→ 전투 재개 차단
```

## 12. Idempotency

동일 `queue_mutation_transaction_id` 재요청은 기존 `QueueMutationReceipt`를 반환한다.

중복 요청은 다음을 만들지 않는다.

- producer 재수정.
- dependent 재삭제.
- `queue_revision` 추가 증가.
- provisional ID 재발급.
- stale artifact 중복 invalidation.

Receipt는 최소 다음을 보존한다.

```text
queue_mutation_transaction_id
planning_session_id
old_queue_revision
new_queue_revision
producer_reservation_id
old_output_fingerprints
committed_output_fingerprints
ordered_removed_reservation_ids
producer_modification_basis_hash
invalidated_artifact_ids
```

## 13. 자동 검증 계약

최소 다음 사례를 검증한다.

1. output fingerprint 동일 → dependent 유지, 전체 재검증.
2. capability 추가로 기존 consumer 모두 호환 → cascade 없음.
3. 사용 중인 capability 제거 → 해당 direct consumer와 descendants만 preview.
4. output A 유지, output B 삭제 → B branch만 제거.
5. changed output의 consumer 일부만 호환 → broken consumer branch만 제거.
6. unrelated dependency branch 보존.
7. provisional identity 변경 → 기존 consumer incompatible.
8. preview 뒤 producer 수정안 변경 → stale 동의, mutation 0.
9. preview 뒤 새 dependent 추가 → stale 동의, 최신 영향 집합 재표시.
10. producer 수정과 dependent 삭제 중 실패 → 전체 rollback.
11. 성공 mutation → `queue_revision` 정확히 1회 증가.
12. 동일 mutation transaction 재요청 → 수정·삭제·revision 중복 0.
13. 성공 뒤 남은 전체 큐 재검증.
14. 자동 rebind 0.
15. 제품 authoritative 금화·식량·건물·전장 상태 변경 0.

## 14. 범위 보호

이 문서는 다음을 확정하지 않는다.

- optional dependency의 의미와 fallback 규칙.
- 하나의 consumer가 복수 대체 output 중 하나를 선택하는 schema.
- 사용자가 dependency 예약을 재정렬할 때의 UX.
- 각 command type의 구체적인 capability 목록.
- 제품 UI의 색상·레이아웃.

## 15. 현재 상태

```text
PRODUCER_OUTPUT_FINGERPRINT_POLICY: APPROVED
OUTPUT_BRANCH_CASCADE_POLICY: APPROVED
DEPENDENCY_REORDER_POLICY: REVIEW_PENDING
PRODUCT_CODE_AUTHORIZED: NO
V2_IMPLEMENTATION: NOT_STARTED
HUMAN_QA: NOT_RUN
CORE_LOCK_V2: PENDING
```
