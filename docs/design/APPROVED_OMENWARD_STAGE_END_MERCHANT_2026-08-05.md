# [현행] OMENWARD Stage 종료 상인 정본

```yaml
decision_id: OMW-DEC-20260805-PLANNING-STAGE-END-MERCHANT-V1
approved_at: 2026-08-05 KST
approval: USER_APPROVED_RECOMMENDED_DIRECTION
status: MAIN_CANON_TARGET / NOT_IMPLEMENTED
planning_counter: 6_OF_10
product_code_authority: NONE
simulation: NOT_RUN
runtime: NOT_RUN
human_validation: NOT_RUN
```

## 1. 목적

Stage 종료 상인은 상시 상점이 아니라 다음 Stage를 준비하는 제한된 골드 기회비용 장치다.

```text
Stage 결과 정산·checkpoint
→ 정비시간
→ 상인 재고 공개
→ 골드 사용 결정
→ 건설·연구·미션 정리
→ 다음 Stage 시작 확정
```

상인은 룰렛·건물·병종·전술 연구를 우회하지 않고, 이동권·수리·연구·일회성 비용을 제한적으로 보정한다.

## 2. 방문 계약

```text
MERCHANT_VISIT_STAGES = 1_TO_19
STAGE_20_MERCHANT = FORBIDDEN
STAGE_20_NEXT = MAPRUN_FINAL_SETTLEMENT
ALWAYS_AVAILABLE_HUD_SHOP = FORBIDDEN
COMBAT_REENTRY = FORBIDDEN
```

- Stage 1~19 종료 정비시간마다 한 번 방문한다.
- 다음 Stage 시작 확정 뒤 해당 방문 재고는 소멸한다.
- 전투 중 구매·재진입·재고 갱신을 금지한다.
- Stage 20 종료 뒤에는 상인이 아니라 MapRun 최종 정산으로 이동한다.

## 3. 4칸 유한 재고

```text
TOTAL_MERCHANT_SLOTS = 4
SLOT_A = ROULETTE_CONTROL
SLOT_B = RECOVERY_SERVICE
SLOT_C = DEVELOPMENT_SERVICE
SLOT_D = VARIABLE_OPPORTUNITY
VISIT_STOCK = FINITE
INFINITE_PURCHASE = FORBIDDEN
INFINITE_REROLL = FORBIDDEN
```

기본 재고는 슬롯별 1개다. 정확 재고 수는 시뮬레이션 전 확정하지 않는다.

### 3.1 A — 룰렛 제어

```text
STORED_MOVE_TICKETS < 3
→ STORED_MOVE_TICKET +1

STORED_MOVE_TICKETS = 3
→ NEXT_SPIN_ONE_TIME_GOLD_DISCOUNT

DISCOUNT_STACKING = FORBIDDEN
UNUSED_DISCOUNT_EXPIRES_AT_NEXT_STAGE_START
```

- 매 방문 룰렛 제어 상품 하나는 보장한다.
- 이동권 상한 3개를 초과하지 않는다.
- 할인은 다음 룰렛 회전 1회에만 적용한다.
- 재고 생성 뒤 구매 전 상품이 숨겨서 바뀌지 않는다.

### 3.2 B — 복구 서비스

기본 후보는 손상 건물 수리다.

- 손상 건물 하나를 선택해 즉시 수리한다.
- 수리 대상이 없으면 현재 상태에 유효한 다른 복구·정비 상품으로 대체한다.
- 파괴 건물 즉시 부활·완전 무상 복구·영구 방어 증가를 제공하지 않는다.

### 3.3 C — 성장 보조

기본 후보는 전술 연구 가속이다.

- 진행 중 연구의 남은 시간을 줄인다.
- 진행 중 연구가 없으면 마력탑 Tier 조건을 만족하는 연구 후보에 제한된 시작 진행도를 부여하거나 유효 상품으로 대체한다.
- 전술스킬을 직접 해금하지 않는다.
- 마력탑 Tier와 동시 연구 1개 규칙을 우회하지 않는다.

### 3.4 D — 가변 기회

현재 상태에 유효한 후보 하나를 제시한다.

- 추가 이동권 또는 룰렛 1회 할인.
- 추가 수리 서비스.
- 연구 가속.
- 다음 건설·업그레이드 1회 비용 할인.

동일 서비스가 재고 대부분을 차지하지 않도록 중복 상한을 둔다.

## 4. 핵심 시스템 우회 금지

```text
PURCHASE_CURRENCY = GOLD_ONLY
DIRECT_UNIT_SALE = FORBIDDEN
DIRECT_T3_SALE = FORBIDDEN
DIRECT_HERO_SALE = FORBIDDEN
DIRECT_LEGENDARY_SALE = FORBIDDEN
DIRECT_TACTICAL_UNLOCK = FORBIDDEN
DIRECT_MANA_SALE = FORBIDDEN
BUILDING_BRANCH_RESELECT = FORBIDDEN
STAGE_INFORMATION_SALE = FORBIDDEN
PERMANENT_FORCE_CAP_INCREASE = FORBIDDEN
```

상인은 특정 병종 당첨·T3 승급·전술 해금·마력 확보·건물 분기 되돌리기를 판매하지 않는다.

## 5. 골드 기회비용

상인 구매는 다음 골드 사용처와 경쟁한다.

```text
건설
업그레이드
수리
룰렛 회전
전술 연구
상인 구매
```

- 매 방문 모든 상품 구매가 기본 정답이 되어서는 안 된다.
- 초반에 어떤 상품도 살 수 없는 장식 상점이어서도 안 된다.
- 가격은 상품 가치·현재 경제·Act 구간을 함께 고려한다.
- 금고 투자 하나로 매 방문 전체 재고를 독식하는 전략은 Stop-ship이다.

```text
EXACT_PRICES = PENDING_SIMULATION
EXACT_STOCK_COUNTS = PENDING_SIMULATION
EXACT_APPEARANCE_RATES = PENDING_SIMULATION
EXACT_DISCOUNTS = PENDING_SIMULATION
```

## 6. 구매·할인·저장 계약

- 구매 결과는 즉시 적용하거나 명시된 다음 행동 1회에만 적용한다.
- 할인 중첩을 금지한다.
- 다음 Stage 시작 시 미사용 1회성 할인은 소멸한다.
- 구매 확인에는 상품·대상·효과·소멸 조건·구매 후 골드를 표시한다.
- 골드 차감과 상품 적용은 하나의 멱등 거래다.
- 중복 클릭·화면 전환·checkpoint 복구로 같은 재고를 두 번 구매할 수 없다.
- 판매·흥정·대출·외상·상인 전용 통화는 6/10 범위에 포함하지 않는다.

## 7. 정보 공개와 UX

상인 화면은 다음을 동시에 공개한다.

- 현재 골드와 구매 후 잔액.
- 네 슬롯의 상품·가격·남은 재고.
- 즉시 적용/다음 Stage 한정/다음 행동 1회 여부.
- 대상 선택과 사용 불가 이유.
- 현재 이동권·손상 건물·진행 연구.
- 다음 Stage 시작 시 소멸하는 권리.
- 다음 Stage 압력 요약으로 돌아가는 경로.

구매 뒤 다른 슬롯 내용·가격을 숨겨서 변경하지 않는다.

## 8. Stage·Act 규칙

- Act 1은 이동권·수리 등 이해하기 쉬운 정비를 우선할 수 있다.
- Act 2~4는 연구 가속·비용 할인 비중을 늘릴 수 있다.
- Boss 직전 강한 상품이나 필수 카운터를 자동 보장하지 않는다.
- 특정 상인 상품 미구매가 다음 Stage 자동 패배 조건이 되어서는 안 된다.

## 9. 실패·예외

- 골드 부족: 구매 불가와 부족량 표시.
- 이동권 3/3: 이동권 대신 룰렛 1회 할인.
- 수리 대상 없음: 수리 상품 생성 금지 또는 유효 상품 대체.
- 연구 대상 없음: 직접 해금 금지, 유효 성장 상품으로 대체.
- 할인 대상 없음: 할인 상품 생성 금지 또는 대체.
- 구매 직후 종료·크래시: 거래 ID 기준 골드와 효과를 함께 복구.
- Stage 20 종료: 상인 인스턴스 생성 금지.

## 10. 벤치마킹 적용

채택:

- 방문 시점에 한정된 재고로 자원 결정을 집중한다.
- 전투 결과 정산과 다음 구간 소비 결정을 분리한다.
- 단일 경제 루트로 전체 재고를 반복 독식하는 전략을 억제한다.

비채택:

- 타 게임의 가격·상품 수·등장률 직접 복제.
- 상인 전용 통화·무한 reroll·상시 접근.
- 병종·전술·마력 직접 판매.
- 별도 상인 인벤토리·흥정 미니게임.

## 11. 제품 경계

```text
PRODUCT_CODE = UNCHANGED
DATA_MIGRATION = NOT_AUTHORIZED
EXACT_NUMERICS = PENDING_SIMULATION
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
```

이 문서 병합은 상인 제품 구현·가격 확정·런타임 상태머신 승인이 아니다.

## 12. 다음 Gate

```text
OMW-DEC-20260805-PLANNING-FIRST-10-15-MINUTES-FLOW-V1
7_OF_10
```
