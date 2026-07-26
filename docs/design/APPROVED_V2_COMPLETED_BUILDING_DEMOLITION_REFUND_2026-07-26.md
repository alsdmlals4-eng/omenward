# 승인된 완공 건물 철거·고정 환급 계약

- 승인일: 2026-07-26
- 상태: `V2_SPEC_APPROVED / PRODUCT_CODE_NOT_AUTHORIZED`
- 승인 근거: 사용자 확정
- 상위 책임:
  - `docs/design/APPROVED_V2_EXISTING_WORK_CANCEL_REFUND_2026-07-26.md`
  - `docs/design/APPROVED_V2_DEMOLITION_CANCELS_PLANNED_WORK_2026-07-26.md`
  - `docs/design/APPROVED_V2_PRODUCER_CANCEL_CASCADE_2026-07-26.md`
  - `docs/design/APPROVED_V2_PLANNING_REVALIDATION_ALL_OR_NOTHING_2026-07-26.md`
  - `docs/design/APPROVED_V2_TRANSACTION_FOUNDATION_SEQUENCE_2026-07-26.md`
  - `docs/design/APPROVED_STAGE_ECONOMY_AND_BUILDING_COST_BASELINE_V1.md`

이 문서는 일반 `TACTICAL_PLANNING`에서 이미 live world에 완공되어 존재하는 건물을 플레이어가 철거할 때 적용하는 환급률, 환급 basis, payment lineage, planning preview, 가상 원장, node 재사용, active upgrade 결합 처리, dependent 정리와 최종 원자 승격을 소유한다.

## 1. 승인된 핵심 결정

```text
COMPLETED_BUILDING_DEMOLITION_REFUND_RATE: 40_PERCENT_BASE_CONSTRUCTION_ONLY
DEMOLITION_REFUND_BASIS: BASE_CONSTRUCTION_ACTUAL_PAID_GOLD
COMPLETED_UPGRADE_COSTS_IN_DEMOLITION_REFUND: EXCLUDED
DEMOLITION_REFUND_ROUNDING: FLOOR_TO_INTEGER_GOLD
DEMOLITION_IMPACT_PREVIEW: REQUIRED
DEMOLITION_CONFIRMATION: REQUIRED
PLANNING_VIRTUAL_DEMOLITION_REFUND_CREDIT: REQUIRED
LIVE_DEMOLITION_REFUND_BEFORE_CONFIRM: FORBIDDEN
DEMOLITION_BRANCH_NODE_RELEASE: IMMEDIATE
SAME_SESSION_PROVISIONAL_BUILDING_REMOVAL: RELEASE_PLANNED_DEBIT_NOT_REFUND
ACTIVE_UPGRADE_PLUS_DEMOLITION_REFUNDS: SEPARATE_LEDGER_ENTRIES
ACTIVE_UPGRADE_CANCEL_REFUND_RATE: 50_PERCENT
DEMOLITION_DEPENDENT_CASCADE: REQUIRED
DEMOLITION_QUEUE_MUTATION: ATOMIC
QUEUE_REVISION_INCREMENT_PER_DEMOLITION: EXACTLY_ONCE
DEMOLITION_REPLAY_FROM_ENTRY_SNAPSHOT: REQUIRED
STALE_DEMOLITION_PREVIEW: REJECT_WITH_ZERO_MUTATION
DEMOLITION_DUPLICATE_TRANSACTION: SAME_RECEIPT
CONFIRM_DEMOLITION_PROMOTION: ATOMIC
FAILED_CONFIRM_DEMOLITION_LIVE_MUTATION: ZERO
ENEMY_DESTRUCTION_DEMOLITION_REFUND: NONE
PRODUCT_CODE_AUTHORIZED: NO
```

승인된 기본식:

```text
demolition_refund_gold = floor(base_construction_actual_paid_gold * 40 / 100)
```

완료된 Tier 2·Tier 3 업그레이드의 과거 지불액은 위 식에 합산하지 않는다.

## 2. 적용 범위

적용 대상:

- planning 진입 전에 live world에서 완공된 건물.
- `ACTIVE_TIER_1`, `ACTIVE_TIER_2`, `ACTIVE_TIER_3` 등 완공 lifecycle의 건물.
- 완공 건물이 현재 live upgrade를 진행 중인 경우의 철거 요청.
- 해당 건물이나 capability를 참조하는 현재 planning session의 downstream 예약.

적용하지 않는 대상:

- 같은 planning session에서 새로 생성되어 아직 live payment가 발생하지 않은 provisional 건물.
- 아직 live `CONSTRUCTING`인 건설 작업의 취소.
- 적 공격이나 전투 규칙에 의한 파괴.
- 수리·생산 queue 취소.
- 철거가 아닌 upgrade 취소만 요청한 경우.

같은 planning session에서 새로 만든 provisional 건물이 shared horizon 안에서 branch `COMPLETED`가 되었더라도 live payment와 live building lineage가 아직 없으므로 40% 철거 환급을 만들지 않는다. producer 예약과 `planned debit`을 제거한다.

## 3. 기본 건설 Payment Lineage

완공 건물은 수명 동안 다음 immutable payment lineage를 유지해야 한다.

```text
BuildingPaymentLineage
- building_id
- base_construction_actual_paid_gold
- base_construction_payment_transaction_id
- base_construction_quote_fingerprint
- base_construction_started_simulation_tick
- base_construction_completed_simulation_tick
```

필수 규칙:

- `base_construction_actual_paid_gold`는 최초 기본 건설 시작 시 실제 원장에서 차감된 정수 금화다.
- 할인·무료 효과가 있었다면 할인 적용 후 실제 지불액을 사용한다.
- Tier 2·Tier 3 업그레이드가 완료되어도 기본 건설 payment lineage를 덮어쓰지 않는다.
- 현재 건물 가격, 재건축 가격, 업그레이드 누적 투자액, 향후 데이터 변경을 사용하지 않는다.
- payment lineage가 누락되거나 검증 불가능하면 현재 가격으로 추정하지 않고 철거 commit을 차단한다.
- 실제 지불액이 0이면 철거 환급도 0이다.

## 4. 환급 계산

예시:

```text
base_construction_actual_paid_gold = 40
demolition_refund = floor(40 * 40 / 100) = 16
```

```text
base_construction_actual_paid_gold = 35
demolition_refund = floor(35 * 40 / 100) = 14
```

```text
base_construction_actual_paid_gold = 0
demolition_refund = 0
```

반올림은 양의 정수 금화 기준 내림이다. UI 표시와 ledger 계산은 같은 canonical 정수 결과를 사용한다.

금지:

- 완료된 업그레이드 실제 지불액을 철거 환급 basis에 더함.
- 현재 가격이나 정가로 환급 재계산.
- 건물 체력·경과 시간·Tier에 따라 40% 비율 변경.
- 소수 금화를 별도 잔액으로 누적.
- 동일 건물을 두 번 철거해 환급 중복 지급.

## 5. 완료된 업그레이드 비용 제외

예:

```text
Tier 1 기본 건설 실제 지불액 = 40
Tier 2 완료 업그레이드 실제 지불액 = 45
Tier 3 완료 업그레이드 실제 지불액 = 70
현재 건물 = 완공 Tier 3
```

철거 환급:

```text
floor(40 * 40 / 100) = 16
```

45와 70은 이미 완료된 과거 upgrade investment이므로 철거 환급에 포함하지 않는다.

## 6. 진행 중 업그레이드가 있는 완공 건물 철거

완공 건물이 live upgrade를 진행 중이라면 두 경제 사건을 분리 계산한다.

```text
upgrade_cancel_refund_gold = floor(active_upgrade_actual_paid_gold * 50 / 100)
demolition_refund_gold = floor(base_construction_actual_paid_gold * 40 / 100)
total_virtual_credit = upgrade_cancel_refund_gold + demolition_refund_gold
```

예:

```text
기본 건설 실제 지불액 = 40
진행 중 upgrade 실제 지불액 = 45

upgrade 취소 환불 = floor(45 * 50 / 100) = 22
완공 건물 철거 환급 = floor(40 * 40 / 100) = 16
총 예상 credit = 38
```

필수 규칙:

- 두 금액은 별도 ledger entry type으로 기록한다.
- upgrade 지불액을 기본 건설 basis에 합쳐 40%를 다시 계산하지 않는다.
- upgrade 취소와 건물 철거 중 일부만 적용하지 않는다.
- 철거가 확정되면 previous tier 건물을 유지하지 않고 최종 node를 비운다.
- 진행 중 upgrade progress는 복구하지 않는다.

## 7. 철거 Preview

철거 버튼은 즉시 live 상태를 변경하지 않는다. 먼저 순수 `CompletedBuildingDemolitionPreview`를 계산한다.

최소 필드:

```text
planning_session_id
queue_revision
building_id
node_id
building_lifecycle
current_tier
base_construction_actual_paid_gold
demolition_refund_rate_percent
demolition_refund_gold
completed_upgrade_payment_ids_excluded
active_upgrade_work_id_if_any
active_upgrade_cancel_refund_gold_if_any
ordered_removed_dependent_reservation_ids
released_capacity_and_token_sources
post_demolition_branch_state
building_payment_lineage_fingerprint
demolition_basis_hash
```

UI는 최소 다음을 표시한다.

```text
이 건물을 철거합니다.
- 기본 건설 실제 지불액
- 철거 환급액
- 환급되지 않는 완료 업그레이드 비용
- 진행 중 upgrade 취소 환불액
- 제거되는 기능·토큰·생산·종속 예약

[돌아가기] [철거]
```

preview 생성 중 queue, branch, live world, live ledger, simulation time을 변경하지 않는다.

## 8. Planning branch 적용

사용자가 `[철거]`를 명시적으로 승인하면 하나의 queue mutation으로 demolition command를 추가하고 entry snapshot부터 전체 queue를 replay한다.

```text
완공 building 제거
→ active upgrade가 있으면 취소
→ capability·TokenSource·생산 output을 branch에서 제거
→ dependent cascade
→ node 점유 즉시 해제
→ demolition virtual refund credit 추가
→ active upgrade virtual refund credit 별도 추가
```

결과 node는 planning branch에서 즉시 비어 있으므로 같은 세션의 후속 건설 명령이 사용할 수 있다.

철거 명령을 취소하면 replay에서 건물, node 점유, capability와 virtual credits가 모두 entry snapshot 기준으로 복원된다.

## 9. 가상 원장

planning branch는 다음 항목을 구분한다.

```text
PlanningVirtualLedger
+ COMPLETED_BUILDING_DEMOLITION_REFUND_CREDIT
+ EXISTING_UPGRADE_CANCEL_REFUND_CREDIT
- PLANNED_BUILD_OR_UPGRADE_DEBIT
```

필수 규칙:

- 후속 planning 명령은 예상 refund credit을 사용할 수 있다.
- confirm 전 live gold는 증가하지 않는다.
- provisional building 제거는 `PLANNED_DEBIT_RELEASE`이며 demolition refund credit이 아니다.
- 같은 비용을 debit release와 refund credit 양쪽에 중복 기록하지 않는다.
- demolition command를 제거하면 모든 관련 virtual credit도 replay에서 제거된다.

## 10. Dependent cascade

철거되는 건물의 object, capability, TokenSource, 생산 output 또는 node 점유 상태를 필수 입력으로 참조하는 예약은 승인된 producer cancel cascade 정책을 따른다.

```text
root demolished building
→ incompatible direct consumers
→ transitive descendants
```

필수 규칙:

- 영향 집합을 preview에 표시한다.
- explicit dependency edge와 output contract로 계산한다.
- 영향받지 않는 독립 예약은 유지한다.
- dependent를 다른 건물이나 node에 자동 재연결하지 않는다.
- 일부 dependent만 남기는 dangling 상태를 허용하지 않는다.

## 11. Stale 방지

`demolition_basis_hash`는 최소 다음을 포함한다.

```text
planning_session_id
queue_revision
building_id and lifecycle
node_id
current tier
BuildingPaymentLineage fingerprint
active upgrade payment and progress basis
canonical refund calculations
ordered dependent impact set
post-demolition target state
```

preview 이후 basis가 바뀌면:

```text
STALE_COMPLETED_BUILDING_DEMOLITION_PREVIEW
→ 상태 변경 0
→ 최신 preview 재생성
→ 사용자 재동의
```

현재 가격 변화만으로 immutable base construction payment lineage는 바뀌지 않는다.

## 12. Queue mutation 원자성

승인된 철거 명령 추가는 다음을 하나의 원자 mutation으로 처리한다.

```text
demolition command 추가
+ active upgrade cancellation 연결
+ dependent closure 제거
+ virtual refund entries 추가
+ node release
+ queue_revision 정확히 1회 증가
+ entry snapshot부터 full replay
+ mutation receipt 기록
```

일부 mutation만 적용하는 것은 금지한다.

## 13. Confirm 원자 승격

`[확정/전투 재개]` 성공 시 다음을 하나의 commit plan으로 승격한다.

```text
live completed building 제거
+ active upgrade 제거
+ live capability·TokenSource·production unregister
+ node 해제
+ demolition refund gold 지급
+ active upgrade cancel refund gold 지급
+ dependent 결과 정리
+ receipt 기록
+ simulation resume
```

하나라도 실패하면:

```text
live building removal 0
live upgrade cancellation 0
live refund 0
live registry mutation 0
node mutation 0
simulation time advance 0
```

전투 재개는 commit receipt가 기록된 뒤에만 허용한다.

## 14. Idempotency

철거 queue mutation과 최종 planning commit은 안정적인 transaction ID를 사용한다.

```text
demolition_queue_transaction_id
planning_commit_transaction_id
```

동일 transaction 재요청 시 기존 receipt를 반환하며 다음이 중복되어서는 안 된다.

- demolition refund.
- active upgrade cancel refund.
- building removal.
- node release.
- registry unregister.
- dependent cascade.
- queue revision 증가.
- simulation resume.

## 15. 적 파괴와 구분

적 공격 또는 전투 규칙으로 건물이 파괴되면 철거 환급을 지급하지 않는다.

```text
PLAYER_CONFIRMED_DEMOLITION → 40% base construction refund
ENEMY_DESTRUCTION → refund 0
```

파괴와 철거는 같은 node 결과를 만들 수 있어도 경제 transaction kind와 receipt를 공유하지 않는다.

## 16. 범위 보호

이번 승인으로 변경하지 않는 항목:

- 진행 중 건설 취소 70% 환불.
- 진행 중 업그레이드 취소 50% 환불.
- 수리·생산 queue 취소 정책.
- 준비 화면·위험 전투·룰렛 이동 규칙.
- R1+R2 범위.

```text
V2_IMPLEMENTATION: NOT_STARTED
PRODUCT_CODE_AUTHORIZED: NO
FINAL_CODEX_HANDOFF: NOT_AUTHORIZED
```
