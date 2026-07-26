# V2 기존 진행 작업 취소·고정 환불 적대적 검수 F-26

- 검수일: 2026-07-26
- 대상: `APPROVED_V2_EXISTING_WORK_CANCEL_REFUND_2026-07-26.md`
- 결과: `F-26: RESOLVED`
- 승인 근거: 사용자 `A` 선택
- 제품 코드 승인: 없음

```text
F-26_RESULT: APPROVED
EXISTING_WORK_CANCEL_REFUND_POLICY: FIXED_70_CONSTRUCTION_50_UPGRADE
```

## 1. 검수 질문

기존 live 건설·업그레이드가 진행 중일 때 planning branch에서 취소 명령을 내리면 다음을 결정해야 했다.

1. 환불률을 진행률에 따라 바꿀지.
2. 정가, 현재가, 실제 지불액 중 무엇을 기준으로 할지.
3. 건설 취소와 업그레이드 취소의 target state를 어떻게 구분할지.
4. 예상 환불을 후속 planning 명령에 사용할 수 있는지.
5. same-session planned work 제거와 live payment 환불을 어떻게 구분할지.
6. dependent, stale preview, confirm failure, duplicate transaction을 어떻게 안전하게 처리할지.

## 2. 승인 결과

```text
진행 중 건설 취소 환불 = actual paid gold의 70%
진행 중 업그레이드 취소 환불 = actual paid gold의 50%
정수 금화 내림
진행률 비례 없음
```

- 실제 지불액은 작업 시작 시 immutable payment snapshot에서 가져온다.
- 건설 취소는 작업·건설 object를 제거하고 node를 비운다.
- 업그레이드 취소는 upgrade 작업만 제거하고 이전 active tier 건물을 유지한다.
- 예상 환불은 planning virtual ledger credit으로 후속 검증에 사용한다.
- live gold 환불은 최종 confirm 성공 시에만 발생한다.

## 3. 대안 기각

### B. 남은 진행률 비례 환불

기각 사유:

- 진행률, tick rounding, 할인 결제액과 환불률 조합이 복잡하다.
- 취소 시점 경계에서 플레이어가 최적화·악용할 여지가 커진다.
- UI 설명과 재현성이 약해진다.

### C. 환불 없음

기각 사유:

- planning에서 실수 수정 비용이 과도하다.
- 이미 승인된 초기 경제 방향과 맞지 않는다.

## 4. 적대적 시나리오

### F-26.1 현재 가격이 상승한 뒤 취소

```text
작업 시작 실제 지불 40
현재 가격 60
```

예상:

```text
refund = floor(40 * 70%) = 28
```

현재 가격 60을 사용하지 않는다.

### F-26.2 할인 업그레이드 취소

```text
정가 60
실제 지불 30
```

예상:

```text
refund = floor(30 * 50%) = 15
```

정가 기준 과다 환불을 금지한다.

### F-26.3 소수점 경계

```text
건설 actual paid 35
35 * 70% = 24.5
```

예상:

```text
refund = 24
```

정수 금화 내림을 사용한다.

### F-26.4 진행률 차이

```text
건설 A 진행 1%
건설 B 진행 99%
actual paid 동일
```

예상: 두 작업의 환불액은 동일하다.

### F-26.5 업그레이드 취소 후 node 상태

예상:

- 이전 Tier 건물 유지.
- node 점유 유지.
- upgrade 진행도 폐기.
- 건물 철거나 node 해제로 해석하지 않음.

### F-26.6 건설 취소 후 node 상태

예상:

- 건설 중 object 제거.
- node 해제.
- 후속 planning 건설이 같은 node를 사용할 수 있음.

### F-26.7 same-session planned work 제거

아직 live payment가 없는 새 planning 건설을 제거한다.

예상:

- planned debit만 제거.
- refund credit 생성 0.
- live gold mutation 0.

### F-26.8 dependent 존재

취소 작업의 완료 output을 후속 예약이 참조한다.

예상:

- 영향 집합 preview.
- 명시적 동의.
- 승인된 cascade로 dependent 정리.
- dangling reference 0.

### F-26.9 preview 후 queue 변경

예상:

```text
STALE_EXISTING_WORK_CANCEL_REFUND_PREVIEW
→ mutation 0
→ 최신 preview와 재동의
```

### F-26.10 confirm 실패

예상:

- live 작업 유지.
- 환불 0.
- node·tier 변경 0.
- dependent 제거 0.
- 후속 비용 차감 0.
- 시간 재개 0.

### F-26.11 duplicate transaction

동일 `queue_mutation_transaction_id` 또는 `planning_commit_transaction_id`를 재요청한다.

예상:

- 같은 receipt 반환.
- 환불·revision·작업 취소·시간 재개 중복 0.

### F-26.12 적 파괴

예상: 환불 0. 플레이어 취소와 적 파괴를 혼합하지 않는다.

## 5. 불변 조건

```text
refund_gold <= actual_paid_gold
actual_paid_gold >= 0
refund_gold >= 0
construction_cancel_frees_node = true
upgrade_cancel_frees_node = false
live_refund_before_confirm = 0
same_session_planned_debit_release_is_refund = false
```

## 6. 검증 항목

- 상위 승인 문서 연결.
- 70%/50% 고정 환불률.
- actual paid basis.
- integer floor.
- 건설·업그레이드 post-cancel state 분리.
- preview·explicit confirmation.
- virtual credit와 live credit 분리.
- same-session planned debit release 구분.
- dependent cascade.
- stale zero mutation.
- queue revision exactly once.
- entry snapshot full replay.
- confirm atomicity·rollback·idempotency.
- enemy destruction no refund.
- 제품 코드 미승인.

## 7. 잔여 범위

다음은 이 검수에서 승인하지 않는다.

- 완공 건물 일반 철거 환급률 최종화.
- 수리·생산 queue 취소 환불.
- 위험 전투 중 실시간 취소 UX.
- 제품 코드 구현.

```text
V2_IMPLEMENTATION: NOT_STARTED
PRODUCT_CODE_AUTHORIZED: NO
FINAL_CODEX_HANDOFF: NOT_AUTHORIZED
```
