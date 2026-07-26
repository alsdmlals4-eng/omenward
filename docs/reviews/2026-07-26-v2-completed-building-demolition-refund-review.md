# V2 완공 건물 철거·고정 환급 적대적 검수 F-27

- 검수일: 2026-07-26
- 대상: `APPROVED_V2_COMPLETED_BUILDING_DEMOLITION_REFUND_2026-07-26.md`
- 상태: `F-27: RESOLVED`
- 결과: `F-27_RESULT: APPROVED`
- 제품 코드 승인: `NO`

## 1. 검수 질문

완공 건물을 플레이어가 철거할 때 다음 충돌을 닫아야 한다.

1. 기본 건설비만 환급할지 완료된 업그레이드 투자까지 포함할지.
2. 현재 가격과 최초 실제 지불액 중 무엇을 basis로 사용할지.
3. 진행 중 업그레이드 취소 환불과 완공 건물 철거 환급을 어떻게 결합할지.
4. 같은 planning session에서 생성된 provisional 완공 건물을 철거할 때 환급을 만들지.
5. planning preview·dependent cascade·최종 confirm을 어떻게 원자화할지.

## 2. 승인 결과

```text
COMPLETED_BUILDING_DEMOLITION_REFUND_POLICY: BASE_CONSTRUCTION_ACTUAL_PAID_40_PERCENT
COMPLETED_UPGRADE_INVESTMENT_REFUND: EXCLUDED
ACTIVE_UPGRADE_CANCEL_AND_DEMOLITION: SEPARATE_CREDITS_ATOMIC_COMMIT
PROVISIONAL_BUILDING_REMOVAL: RELEASE_PLANNED_DEBIT_ONLY
```

환급식:

```text
demolition_refund_gold = floor(base_construction_actual_paid_gold * 40 / 100)
```

## 3. 대안 검수

### 대안 A — 기본 건설 실제 지불액의 40%

승인.

- 기존 경제 기준의 40% 철거 환급과 일치한다.
- 완료된 업그레이드 투자까지 반복 회수하는 교체 악용을 차단한다.
- payment snapshot으로 할인·무료 건설을 정확히 처리한다.
- 고정률과 정수 내림으로 preview와 commit 결과가 결정론적이다.

### 대안 B — 누적 투자금 전체의 40%

기각.

- Tier 2·Tier 3 교체 비용을 과도하게 낮춘다.
- upgrade 취소 환불과 철거 환급의 basis가 중첩될 수 있다.
- 건물 lineage와 upgrade history 전체를 환급 basis로 결합해야 한다.

### 대안 C — 환급 없음

기각.

- node 재구성 비용이 과도하다.
- 승인된 경제 기준의 완공 건물 철거 40% 방향과 충돌한다.

## 4. Adversarial Case Matrix

### F-27.1 — 완료 Tier 3 건물

입력:

```text
base construction actual paid = 40
completed Tier 2 upgrade paid = 45
completed Tier 3 upgrade paid = 70
```

기대:

```text
demolition refund = 16
completed upgrade refund = 0
```

판정: PASS.

### F-27.2 — 할인 건설

입력:

```text
current catalog price = 50
base construction actual paid = 35
```

기대:

```text
refund = floor(35 * 40 / 100) = 14
```

현재 가격 50을 사용하지 않는다.

판정: PASS.

### F-27.3 — 무료 건설

입력:

```text
base construction actual paid = 0
```

기대:

```text
refund = 0
```

판정: PASS.

### F-27.4 — active upgrade가 있는 건물

입력:

```text
base construction actual paid = 40
active upgrade actual paid = 45
```

기대:

```text
upgrade cancel refund = 22
demolition refund = 16
total virtual credit = 38
```

두 credit은 별도 ledger entry이며 하나의 atomic demolition commit에 포함된다.

판정: PASS.

### F-27.5 — upgrade 지불액을 base basis에 합산

잘못된 계산:

```text
floor((40 + 45) * 40 / 100) = 34
```

기대: 금지. base 40의 40%와 active upgrade 45의 50%를 분리한다.

판정: PASS.

### F-27.6 — same-session provisional building

입력:

```text
planning session에서 새 건설
shared horizon에서 branch COMPLETED
live payment 없음
```

기대:

```text
planned debit release
refund credit 0
```

판정: PASS.

### F-27.7 — payment lineage 누락

입력:

```text
base_construction_actual_paid_gold unavailable
```

기대:

```text
현재 가격 추정 금지
commit 차단
live mutation 0
```

판정: PASS.

### F-27.8 — node 즉시 재사용

철거 planning mutation 승인 후 branch에서 node가 즉시 비어야 하며 후속 건설이 해당 node를 사용할 수 있다. live node는 confirm 전 변경하지 않는다.

판정: PASS.

### F-27.9 — dependent cascade

철거 건물 capability와 TokenSource를 참조하는 downstream 예약은 explicit dependency closure로 preview·제거한다. 독립 예약은 유지하며 자동 재연결하지 않는다.

판정: PASS.

### F-27.10 — stale preview

preview 이후 building lifecycle, active upgrade, queue revision, payment lineage 또는 dependent 집합이 바뀌면 기존 동의를 거부한다.

기대:

```text
STALE_COMPLETED_BUILDING_DEMOLITION_PREVIEW
state mutation 0
```

판정: PASS.

### F-27.11 — confirm 중 일부 실패

building removal, registry unregister, node release, refund credit 중 하나라도 실패하면 전체 live mutation과 simulation resume가 0이어야 한다.

판정: PASS.

### F-27.12 — duplicate transaction

동일 demolition 또는 planning commit transaction을 재요청해도 refund·removal·node release·revision·resume가 중복되지 않는다.

판정: PASS.

### F-27.13 — enemy destruction

적에 의한 파괴는 node를 비울 수 있지만 player demolition refund를 지급하지 않는다.

판정: PASS.

## 5. 원자성 검수

Queue mutation:

```text
demolition command
+ active upgrade cancellation
+ dependent closure
+ virtual refund entries
+ node release
+ queue revision once
+ full replay
+ receipt
```

Confirm promotion:

```text
building removal
+ upgrade cancellation
+ registry unregister
+ node release
+ refund payment
+ receipt
+ simulation resume
```

각 묶음은 부분 성공을 허용하지 않는다.

## 6. 최종 판정

```text
F-27: RESOLVED
F-27_RESULT: APPROVED
COMPLETED_BUILDING_DEMOLITION_REFUND_POLICY: BASE_CONSTRUCTION_ACTUAL_PAID_40_PERCENT
PRODUCT_CODE_AUTHORIZED: NO
V2_IMPLEMENTATION: NOT_STARTED
FINAL_CODEX_HANDOFF: NOT_AUTHORIZED
```
