# 승인된 기존 진행 작업 취소·고정 환불 계약

- 승인일: 2026-07-26
- 상태: `V2_SPEC_APPROVED / PRODUCT_CODE_NOT_AUTHORIZED`
- 승인 근거: 사용자 A안 승인
- 상위 책임:
  - `docs/design/APPROVED_V2_EXISTING_LIVE_WORK_FROZEN_IN_PLANNING_2026-07-26.md`
  - `docs/design/APPROVED_V2_DEMOLITION_CANCELS_PLANNED_WORK_2026-07-26.md`
  - `docs/design/APPROVED_V2_PRODUCER_CANCEL_CASCADE_2026-07-26.md`
  - `docs/design/APPROVED_V2_PLANNING_REVALIDATION_ALL_OR_NOTHING_2026-07-26.md`
  - `docs/design/APPROVED_V2_TRANSACTION_FOUNDATION_SEQUENCE_2026-07-26.md`
  - `docs/design/APPROVED_STAGE_ECONOMY_AND_BUILDING_COST_BASELINE_V1.md`

이 문서는 일반 `TACTICAL_PLANNING` 진입 전에 이미 live world에서 진행 중이던 건설·업그레이드를 플레이어가 취소할 때 적용하는 환불률, 환불 기준 금액, planning preview, 가상 원장, branch 상태 전이, dependent 정리와 최종 원자 승격을 소유한다.

## 1. 승인된 핵심 결정

```text
EXISTING_CONSTRUCTION_CANCEL_REFUND_RATE: 70_PERCENT
EXISTING_UPGRADE_CANCEL_REFUND_RATE: 50_PERCENT
REFUND_BASIS: ACTUAL_PAID_GOLD_AT_WORK_START
REFUND_ROUNDING: FLOOR_TO_INTEGER_GOLD
PROGRESS_PROPORTIONAL_REFUND: FORBIDDEN
CANCELLATION_IMPACT_PREVIEW: REQUIRED
CANCELLATION_CONFIRMATION: REQUIRED
PLANNING_VIRTUAL_REFUND_CREDIT: REQUIRED
LIVE_REFUND_BEFORE_CONFIRM: FORBIDDEN
EXISTING_CONSTRUCTION_CANCEL_RESULT: REMOVE_WORK_AND_FREE_NODE
EXISTING_UPGRADE_CANCEL_RESULT: RESTORE_PREVIOUS_ACTIVE_TIER_KEEP_NODE_OCCUPIED
CANCELED_WORK_PROGRESS_RECOVERY: FORBIDDEN
ENEMY_DESTRUCTION_REFUND: NONE
PLANNED_SAME_SESSION_WORK_REMOVAL: RELEASE_PLANNED_DEBIT_NOT_REFUND
CANCEL_REFUND_DEPENDENT_CASCADE: REQUIRED
CANCEL_REFUND_QUEUE_MUTATION: ATOMIC
QUEUE_REVISION_INCREMENT_PER_CANCEL: EXACTLY_ONCE
CANCEL_REFUND_REPLAY_FROM_ENTRY_SNAPSHOT: REQUIRED
STALE_CANCEL_REFUND_PREVIEW: REJECT_WITH_ZERO_MUTATION
CANCEL_REFUND_DUPLICATE_TRANSACTION: SAME_RECEIPT
CONFIRM_CANCEL_REFUND_PROMOTION: ATOMIC
FAILED_CONFIRM_CANCEL_REFUND_LIVE_MUTATION: ZERO
PRODUCT_CODE_AUTHORIZED: NO
```

승인된 기본식:

```text
construction_refund_gold = floor(actual_paid_gold * 70 / 100)
upgrade_refund_gold = floor(actual_paid_gold * 50 / 100)
loss_gold = actual_paid_gold - refund_gold
```

진행률은 환불률에 영향을 주지 않는다.

## 2. 적용 범위

적용 대상:

- planning 진입 전에 live world에서 이미 시작되어 `CONSTRUCTING`인 건설 작업.
- planning 진입 전에 live world에서 이미 시작되어 `UPGRADING`인 업그레이드 작업.
- 해당 작업의 완료 상태나 output을 전제로 하는 현재 planning session의 downstream 예약.

적용하지 않는 대상:

- 같은 planning session에서 새로 생성했지만 아직 live payment가 발생하지 않은 건설·업그레이드.
- 적 공격이나 전투 규칙으로 파괴된 건물·건설물.
- 이미 완료된 작업.
- 완공 건물의 일반 철거 환급률.
- 수리·생산 queue 취소.

같은 planning session에서 새로 만든 작업을 제거하면 `planned debit`을 삭제할 뿐이며 환불 gold를 새로 만들지 않는다.

## 3. 작업 시작 시 지불 Snapshot

live 시간 기반 작업은 시작 시 다음 immutable payment basis를 보존해야 한다.

```text
WorkPaymentSnapshot
- work_id
- work_kind: CONSTRUCTION | UPGRADE
- target_building_id or construction_instance_id
- actual_paid_gold
- payment_transaction_id
- work_started_simulation_tick
- applied_discount_or_quote_fingerprint
- previous_active_tier_if_upgrade
```

필수 규칙:

- `actual_paid_gold`는 작업 시작 시 실제 원장에서 차감된 정수 금화다.
- 할인, 준비 할인, 무료 효과가 있었다면 할인 적용 후 실제 지불액을 사용한다.
- 현재 건물 가격, 정가, 향후 가격 변경을 사용하지 않는다.
- payment snapshot이 누락되거나 검증 불가능하면 현재 가격으로 추정하지 않고 취소 commit을 차단한다.
- 환불액은 실제 지불액을 초과할 수 없다.
- 실제 지불액이 0이면 환불액도 0이다.

## 4. 환불 계산

### 4.1 진행 중 건설

```text
actual_paid_gold = 40
refund = floor(40 * 70 / 100) = 28
loss = 12
```

```text
actual_paid_gold = 35
refund = floor(35 * 70 / 100) = 24
loss = 11
```

### 4.2 진행 중 업그레이드

```text
actual_paid_gold = 45
refund = floor(45 * 50 / 100) = 22
loss = 23
```

```text
actual_paid_gold = 65
refund = floor(65 * 50 / 100) = 32
loss = 33
```

반올림은 양의 정수 금화 기준 내림이다. UI 표시와 ledger 계산은 같은 canonical 정수 결과를 사용한다.

금지:

- 진행률 10%와 90%에 서로 다른 환불률 적용.
- 현재 가격으로 환불 재계산.
- 소수 금화를 별도 잔액으로 누적.
- 동일 작업을 두 번 취소해 환불 중복 지급.

## 5. 취소 Preview

취소 버튼은 즉시 live 상태를 변경하지 않는다. 먼저 순수 `ExistingWorkCancellationPreview`를 계산한다.

최소 필드:

```text
planning_session_id
queue_revision
work_id
work_kind
target_identity
entry_progress_ticks
total_duration_ticks
actual_paid_gold
refund_rate_percent
refund_gold
loss_gold
post_cancel_branch_state
ordered_removed_dependent_reservation_ids
released_capacity_or_node_holds
payment_snapshot_fingerprint
cancel_refund_basis_hash
```

UI는 최소 다음을 표시한다.

```text
진행 중인 작업을 취소합니다.
- 사라지는 진행도
- 실제 지불액
- 환불액
- 손실액
- 함께 제거되는 종속 예약

[돌아가기] [작업 취소]
```

preview 생성 중 queue, branch, live world, live ledger, simulation time을 변경하지 않는다.

## 6. Planning branch 적용

사용자가 `[작업 취소]`를 명시적으로 승인하면 하나의 queue mutation으로 cancellation command를 추가하고 entry snapshot부터 전체 queue를 replay한다.

### 6.1 기존 건설 취소

```text
기존 CONSTRUCTING 작업 제거
→ 건설 중 object를 planning branch에서 제거
→ node 점유 해제
→ construction output을 참조하는 dependent cascade
→ virtual refund credit 추가
```

결과 node는 planning branch에서 비어 있으므로 같은 세션의 후속 건설 명령이 사용할 수 있다.

### 6.2 기존 업그레이드 취소

```text
기존 UPGRADING 작업 제거
→ 업그레이드 진행도 폐기
→ previous active tier 상태로 복원
→ node는 기존 건물이 계속 점유
→ 업그레이드 완료 output을 참조하는 dependent cascade
→ virtual refund credit 추가
```

업그레이드 취소는 건물 철거나 node 해제가 아니다. 이전 Tier의 기존 기능과 생산 진행 basis는 entry snapshot 계약을 유지한다.

## 7. 가상 환불 원장

planning branch의 예상 환불은 다음처럼 처리한다.

```text
PlanningVirtualLedger
+ refund_credit_gold
```

- 후속 planning 명령은 이 가상 credit을 사용할 수 있다.
- confirm 전 live gold는 증가하지 않는다.
- cancellation command를 취소하면 replay에서 virtual refund credit도 제거된다.
- planned debit 해제와 existing live payment 환불을 서로 다른 ledger entry type으로 기록한다.
- 같은 금액을 `planned debit release`와 `refund credit` 양쪽에 중복 기록하지 않는다.

## 8. Dependent cascade

취소되는 작업의 완료 capability 또는 output을 필수 입력으로 참조하는 예약은 승인된 producer cancel cascade 정책을 따른다.

```text
root canceled work
→ incompatible direct consumers
→ transitive descendants
```

필수 규칙:

- 영향 집합을 preview에 표시한다.
- explicit dependency edge로만 계산한다.
- 영향받지 않는 독립 예약은 유지한다.
- dependent를 다른 건물에 자동 재연결하지 않는다.
- 일부 dependent만 남기는 dangling 상태를 허용하지 않는다.

## 9. Stale 방지

`cancel_refund_basis_hash`는 최소 다음을 포함한다.

```text
planning_session_id
queue_revision
work_id and lifecycle
entry progress and total duration
WorkPaymentSnapshot fingerprint
refund calculation result
ordered dependent impact set
post-cancel target state
```

preview 이후 basis가 바뀌면:

```text
STALE_EXISTING_WORK_CANCEL_REFUND_PREVIEW
→ 상태 변경 0
→ 최신 preview 재생성
→ 사용자 재동의
```

현재 가격 변화만으로 과거 actual payment basis는 바뀌지 않는다.

## 10. Queue mutation 원자성

승인된 취소 명령 추가는 stable `queue_mutation_transaction_id`로 처리한다.

```text
latest queue revision 확인
→ preview basis 재확인
→ cancellation reservation 추가
→ dependent cascade 반영
→ queue_revision 정확히 1 증가
→ entry snapshot부터 full replay
→ QueueMutationReceipt 기록
```

허용 결과:

```text
전체 성공
또는
전체 상태 변경 0
```

동일 transaction 재요청은 같은 receipt를 반환하고 revision, refund credit, dependent 제거를 중복 적용하지 않는다.

## 11. 명령 수정·취소

cancellation reservation 자체를 제거하면:

```text
entry snapshot부터 replay
→ 기존 live work를 entry progress 상태로 branch에 복원
→ virtual refund credit 제거
→ node 또는 previous tier 상태 복원
→ dependent 전체 재검증
```

사라진 작업 진행도를 새로운 작업으로 이전하거나 저장하지 않는다.

## 12. 최종 Confirm

`[확정/전투 재개]` 성공 시 다음을 하나의 `PlanningCommitPlan`으로 원자 적용한다.

```text
기존 작업 취소
+ 실제 환불 gold credit
+ construction node 해제 또는 previous tier 복원
+ dependent 제거
+ 후속 planning 명령 비용 반영
+ PlanningCommitReceipt 기록
+ 전투 시간 재개
```

- live 환불은 receipt 기준 정확히 한 번 지급한다.
- 기존 construction 취소는 live object와 timer를 제거하고 node를 비운다.
- 기존 upgrade 취소는 upgrade timer만 제거하고 이전 Tier 건물을 유지한다.
- 취소와 환불 중 일부만 성공할 수 없다.
- 환불 gold를 사용한 후속 명령도 같은 commit에서 함께 성공하거나 전체 실패한다.

confirm 실패 시:

```text
work cancellation 0
refund 0
node or tier mutation 0
dependent removal 0
resource mutation 0
simulation time advance 0
```

동일 `planning_commit_transaction_id` 재요청은 같은 receipt를 반환하며 환불·취소·시간 재개를 중복 적용하지 않는다.

## 13. 적 파괴와 완료 경계

- 적 또는 전투 규칙에 의한 파괴는 환불 0이다.
- 이미 완료된 작업은 작업 취소 환불 대상이 아니다.
- planning 중 기존 live 작업은 frozen이므로 진입만으로 완료 경계를 넘지 않는다.
- confirm 재검증에서 target lifecycle 또는 payment snapshot이 달라졌다면 zero mutation으로 차단한다.

## 14. 예시

```text
기존 병영 건설
실제 지불 40금화
진행 6초 / 총 20초

취소 preview
- 환불 28금화
- 손실 12금화
- 건설 진행도 폐기
- node 해제

사용자 확인
→ branch에서 병영 건설 제거
→ virtual gold +28
→ 같은 node에 농장 건설 예약 가능
→ 최종 confirm 성공 시 실제 gold +28과 농장 비용을 원자 반영
```

```text
기존 병영 Tier 2 업그레이드
실제 지불 45금화
진행 10초 / 총 25초

취소 preview
- 환불 22금화
- 손실 23금화

사용자 확인
→ branch에서 업그레이드 제거
→ 병영은 이전 Tier 1 상태 유지
→ node는 계속 점유
→ 최종 confirm 성공 시 실제 gold +22
```

## 15. 범위 보호

- 완공 건물 일반 철거 환급률은 이 문서가 변경하지 않는다.
- 수리·생산 queue 취소 환불은 후속 검수 대상이다.
- 준비 화면과 위험 전투의 기존 실시간 규칙을 변경하지 않는다.
- R1+R2 범위를 변경하지 않는다.
- 제품 코드, Scene, Resource, 게임 데이터 변경을 승인하지 않는다.
- 최종 Codex 구현 인계를 승인하지 않는다.

```text
V2_IMPLEMENTATION: NOT_STARTED
PRODUCT_CODE_AUTHORIZED: NO
FINAL_CODEX_HANDOFF: NOT_AUTHORIZED
```
