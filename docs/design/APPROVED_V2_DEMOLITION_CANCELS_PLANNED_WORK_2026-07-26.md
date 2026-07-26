# 승인된 철거 시 계획 작업 취소·가상 비용 해제 계약

- 승인일: 2026-07-26
- 상태: `V2_SPEC_APPROVED / PRODUCT_CODE_NOT_AUTHORIZED`
- 승인 근거: 사용자 권장안 승인
- 상위 책임:
  - `docs/design/APPROVED_V2_PLANNING_ONE_SECOND_HEADSTART_2026-07-26.md`
  - `docs/design/APPROVED_V2_PRODUCER_CANCEL_CASCADE_2026-07-26.md`
  - `docs/design/APPROVED_V2_PLANNING_REVALIDATION_ALL_OR_NOTHING_2026-07-26.md`
  - `docs/design/APPROVED_V2_TRANSACTION_FOUNDATION_SEQUENCE_2026-07-26.md`

이 문서는 일반 `TACTICAL_PLANNING`의 transactional planning branch에서 건물 철거 명령이 이미 존재하는 미확정 건설·업그레이드 작업과 충돌할 때, 영향 preview, 사용자 동의, 가상 비용 해제, 종속 예약 정리와 원자적 branch mutation을 소유한다.

## 1. 승인된 핵심 결정

```text
DEMOLITION_WITH_PLANNED_WORK_POLICY: PREVIEW_CONFIRM_CANCEL_THEN_DEMOLISH
PLANNED_WORK_IMPACT_PREVIEW: REQUIRED
PLANNED_WORK_CANCEL_CONFIRMATION: REQUIRED
PLANNED_WORK_VIRTUAL_COST_RELEASE: REQUIRED
DEMOLITION_AND_WORK_CANCEL: ATOMIC_SINGLE_QUEUE_MUTATION
SILENT_PLANNED_WORK_DISCARD: FORBIDDEN
PLANNED_WORK_COST_WASTE: FORBIDDEN
STALE_DEMOLITION_CONFIRMATION: REJECT_WITH_ZERO_MUTATION
QUEUE_REVISION_INCREMENT_PER_DEMOLITION_OVERRIDE: EXACTLY_ONCE
POST_DEMOLITION_FULL_REPLAY: REQUIRED
LIVE_LEDGER_MUTATION_BEFORE_CONFIRM: FORBIDDEN
```

승인된 처리 순서:

```text
철거 요청
→ 현재 planning branch와 queue revision에서 target 작업 탐색
→ 취소될 작업·종속 예약·가상 비용 해제 preview
→ [돌아가기] 또는 [작업 취소 후 철거]
→ 최신 basis 재확인
→ 작업 예약 제거 + 가상 비용 해제 + 철거 transition 원자 적용
→ queue_revision 정확히 1 증가
→ entry snapshot부터 전체 replay
```

## 2. 적용 범위

대상은 일반 `TACTICAL_PLANNING`에서 아직 live world에 commit되지 않은 다음 작업이다.

- 기존 authoritative 건물에 대한 업그레이드 예약.
- 같은 planning session에서 생성된 provisional 건물의 건설 예약.
- 해당 건설 또는 업그레이드 결과를 필수 입력으로 참조하는 downstream 예약.

현재 문서는 일반 수리, 생산 queue, 영구 해금, 위험 전투의 실시간 철거를 새로 정의하지 않는다.

## 3. 기존 건물의 업그레이드 후 철거

예:

```text
R1: 기존 병영 Tier 2 업그레이드
→ planning branch에서 UPGRADING_TO_TIER_2
→ elapsed = 1초

R2: 같은 병영 철거 요청
```

R2는 R1을 조용히 덮어쓰지 않는다. 먼저 다음 preview를 만든다.

```text
이 건물을 철거하면 다음 작업이 취소됩니다.

- 병영 Tier 2 업그레이드
- 해제되는 가상 비용
- 함께 제거되는 종속 예약

[돌아가기] [작업 취소 후 철거]
```

승인 후 결과:

```text
업그레이드 예약 제거
→ 업그레이드 1초 진행 상태 제거
→ 업그레이드 planned gold debit 제거
→ building을 branch에서 REMOVED 처리
→ node 점유 해제
```

확정 전 live 건물과 live 금화 원장은 변경하지 않는다.

## 4. 같은 세션에서 건설 중인 provisional 건물 철거

예:

```text
R1: 빈 node에 병영 건설
→ provisional 병영
→ UNDER_CONSTRUCTION, elapsed = 1초

R2: provisional 병영 철거 요청
```

이 경우 건물은 아직 live world에 존재하지 않으므로, 승인된 의미는 `건설 예약 취소`이다.

```text
provisional 건설 예약 제거
→ 건설 가상 비용 제거
→ provisional output 제거
→ 해당 node를 planning branch에서 다시 빈 상태로 복원
→ 필수 dependent는 승인된 cascade 정책으로 제거
```

별도의 live 철거 이벤트나 철거 비용을 만들지 않는다.

## 5. 영향 집합

철거 override의 직접 영향 집합은 최소 다음을 포함한다.

```text
target_building_id or provisional_id
active planned construction command
active planned upgrade command
planned work progress state
planned virtual resource entries
required downstream consumers
transitive descendants of removed consumers
```

필수 규칙:

- 동일 target의 취소될 작업은 한 번만 표시한다.
- 종속 예약은 explicit dependency edge로만 계산한다.
- 필수 작업 또는 output을 잃는 consumer는 영향 집합에 포함한다.
- 직접 영향과 transitive 영향을 구분해 표시한다.
- 표시 순서는 `reservation_sequence` 오름차순이다.
- 영향받지 않는 다른 건물의 작업은 제거하지 않는다.

## 6. Preview 데이터

`DemolitionPlannedWorkImpactPreview`는 실제 상태를 변경하지 않는 순수 계산이다.

최소 필드:

```text
planning_session_id
queue_revision
target_building_id
root_demolition_request_id
ordered_canceled_work_reservation_ids
ordered_removed_dependent_reservation_ids
released_virtual_gold
released_virtual_food_or_capacity
released_node_or_output_reservations
dependency_edges_in_scope
demolition_override_basis_hash
```

preview 생성 중 다음은 변경하지 않는다.

- planning queue.
- `queue_revision`.
- planning branch.
- live building과 node.
- live gold와 food.
- simulation clock.
- 기존 receipt.

## 7. 사용자 동의

취소될 작업이 하나라도 있으면 명시적 확인이 필수다.

허용 동작:

```text
[돌아가기]
→ 상태 변경 0

[작업 취소 후 철거]
→ 최신 basis 검증 뒤 원자 mutation 시도
```

금지:

- 철거 버튼을 누른 사실만으로 자동 승인.
- 모달 닫기를 승인으로 처리.
- 업그레이드 비용을 유지한 채 철거.
- 작업을 조용히 삭제.
- 일부 종속 예약만 남김.

취소될 작업이 없다면 기존 표준 철거 transition을 즉시 planning branch에 적용할 수 있다.

## 8. Confirmation basis와 stale 방지

`demolition_override_basis_hash`는 최소 다음을 포함한다.

```text
planning_session_id
queue_revision
target identity
current building lifecycle
canceled work reservation IDs and fingerprints
ordered dependent removal IDs
virtual cost release entries
dependency edges in scope
```

확인창이 열린 뒤 다음 중 하나라도 바뀌면 기존 동의는 stale이다.

- target 작업 추가·수정·취소.
- dependency edge 변경.
- 가상 비용 변경.
- target building identity 또는 lifecycle 변경.
- `queue_revision` 변경.

처리:

```text
current basis != preview basis
→ STALE_DEMOLITION_PLANNED_WORK_PREVIEW
→ 상태 변경 0
→ 최신 preview 재생성
→ 사용자 재동의 필요
```

## 9. 원자 Queue Mutation

승인된 철거 override는 하나의 `queue_mutation_transaction_id`로 처리한다.

```text
최신 queue revision 재확인
→ graph invariant 재확인
→ demolition basis 재확인
→ 취소 대상 작업 예약 제거
→ dependent cascade 제거
→ virtual ledger entries 해제
→ demolition transition 적용
→ queue_revision 정확히 1 증가
→ QueueMutationReceipt 기록
→ entry snapshot부터 전체 queue replay
```

허용 결과는 두 가지뿐이다.

```text
전체 성공
또는
전체 상태 변경 0
```

부분 적용 금지 예:

- 업그레이드 예약만 삭제되고 건물은 남음.
- 건물만 철거되고 업그레이드 비용은 남음.
- 건설 예약은 제거됐지만 provisional output reference가 남음.
- dependent 일부만 삭제됨.

## 10. 가상 비용 해제

취소되는 미확정 작업의 비용은 live 환불이 아니다.

```text
planned debit 제거
→ planning virtual available gold 증가
→ 후속 명령 전체 재검증
```

필수 규칙:

- confirm 전 live 금화를 차감하거나 환불하지 않는다.
- 동일 비용을 두 번 해제하지 않는다.
- 취소된 작업의 planned food·capacity·node hold가 있다면 함께 해제한다.
- 철거 자체의 비용 또는 환급 규칙이 별도 존재하면 해당 command schema를 따른다.
- 업그레이드 비용을 소비한 뒤 철거하는 표현을 금지한다.

## 11. 철거 후 같은 node 재사용

철거 override 성공 후 planning branch에서 target node는 즉시 비어 있다.

```text
업그레이드 취소 + 기존 건물 철거
→ node FREE
→ 후속 새 건물 건설 허용
→ 새 건물 UNDER_CONSTRUCTION, elapsed = 1초
```

후속 건설은 최신 virtual ledger, node 상태와 dependency graph를 기준으로 검증한다.

## 12. Edit·Cancel과 전체 Replay

철거 override 이후 명령을 다시 수정하거나 취소하면 역연산을 누적하지 않는다.

```text
PlanningEntrySnapshot
→ 현재 queue를 고정 sequence로 전체 replay
→ 작업 취소·철거·재건설 transition 재계산
→ 각 시간 기반 작업은 다시 정확히 1초 상태
```

보장:

- 과거 업그레이드 1초가 누적되지 않음.
- 가상 비용 해제가 중복되지 않음.
- 철거 취소 시 entry snapshot의 기존 건물 복원.
- 철거에 의존한 새 건설은 cascade 정책 적용.

## 13. Confirm과 live 승격

`[확정/전투 재개]` 시 최신 planning branch를 다시 생성하고 원자적으로 승격한다.

성공 결과 예:

```text
기존 병영 제거
새 병영 UNDER_CONSTRUCTION, elapsed = 1초
취소된 업그레이드 live debit = 0
새 건설 비용만 receipt 기준으로 정확히 1회 차감
```

confirm 실패 시:

```text
live 건물 변경 0
live node 변경 0
live resource mutation 0
simulation time advance 0
planning queue 유지
```

## 14. Idempotency

동일 `queue_mutation_transaction_id` 재요청은 기존 `QueueMutationReceipt`를 반환한다.

중복 요청은 다음을 만들지 않는다.

- 작업 재취소.
- 가상 비용 재해제.
- target 재철거.
- dependent 재삭제.
- `queue_revision` 추가 증가.
- provisional ID 추가 폐기.

Receipt 최소 필드:

```text
queue_mutation_transaction_id
planning_session_id
old_queue_revision
new_queue_revision
target_building_id
ordered_canceled_work_reservation_ids
ordered_removed_dependent_reservation_ids
released_virtual_ledger_entries
demolition_override_basis_hash
remaining_queue_hash
```

## 15. 자동 검증 계약

최소 다음 사례를 검증한다.

1. 기존 병영 업그레이드 1초 상태에서 철거 요청 → 영향 preview 필수.
2. `[돌아가기]` → queue·branch·virtual ledger 변경 0.
3. 승인 → 업그레이드 예약·progress·가상 비용 제거 후 건물 철거.
4. 철거 뒤 같은 node에 새 건설 허용, 새 작업 elapsed 1초.
5. provisional 건설 중 철거 → 건설 예약 취소로 처리, 별도 live 철거 이벤트 0.
6. 취소 작업의 필수 dependent와 descendants 전체 표시·제거.
7. 무관한 다른 건물 branch 보존.
8. preview 뒤 queue 변경 → stale 동의 거부·mutation 0.
9. 작업 취소·비용 해제·철거 중 하나 실패 → 전체 rollback.
10. confirm 전 live 금화 차감·환불 0.
11. 동일 queue mutation 재요청 → revision·비용 해제·철거 중복 0.
12. confirm 실패 → live building·node·resource·time 변경 0.

## 16. 현재 상태

```text
DEMOLITION_WITH_PLANNED_WORK_POLICY: PREVIEW_CONFIRM_CANCEL_THEN_DEMOLISH
PLANNED_WORK_VIRTUAL_COST_RELEASE: REQUIRED
DEMOLITION_AND_WORK_CANCEL: ATOMIC_SINGLE_QUEUE_MUTATION
STALE_DEMOLITION_CONFIRMATION: REJECT_WITH_ZERO_MUTATION
POST_DEMOLITION_FULL_REPLAY: REQUIRED
SHORT_DURATION_COMPLETION_BOUNDARY: REVIEW_PENDING
PRODUCT_CODE_AUTHORIZED: NO
V2_IMPLEMENTATION: NOT_STARTED
HUMAN_QA: NOT_RUN
CORE_LOCK_V2: PENDING
```
