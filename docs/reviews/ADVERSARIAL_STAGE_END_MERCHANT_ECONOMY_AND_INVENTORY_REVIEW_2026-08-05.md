# [현행] OMENWARD Stage 종료 상인 적대적 검토

```yaml
review_id: OMW-REV-20260805-STAGE-END-MERCHANT-ECONOMY-INVENTORY-V1
decision_id: OMW-DEC-20260805-PLANNING-STAGE-END-MERCHANT-V1
reviewed_at: 2026-08-05 KST
status: REVIEW_PASS_WITH_NUMERIC_AND_RUNTIME_DEPENDENCIES
product_code: UNCHANGED
exact_numerics: PENDING_SIMULATION
```

## 결론

```text
CORE_FIT = STRONG
MERCHANT_ROLE = LIMITED_MAINTENANCE_AND_GOLD_OPPORTUNITY_COST
INVENTORY_READABILITY = COHERENT
ECONOMY_SAFETY = STRUCTURALLY_VIABLE
DOCUMENT_PR_MERGE_READINESS = PASS
PRODUCT_CODE = UNCHANGED
EXACT_NUMERICS = PENDING_SIMULATION
IMPLEMENTATION_READINESS = BLOCKED_BY_NUMERIC_AND_RUNTIME_PLAN
```

상인은 핵심 시스템을 우회하지 않는 한 유효하다. 정확 가격·수량·등장률·할인율과 거래 상태머신은 후속 시뮬레이션·Codex 계획이 필요하다.

## 감사 `OMW-AUD-468~491`

| ID | 공격 항목 | 분류 | 조치 | 상태 |
|---|---|---|---|---|
| OMW-AUD-468 | 매 방문 이동권 구매가 강제되는 루프 | MERCHANT_MANDATORY_PURCHASE_LOOP | A 슬롯 가격·가치와 미구매 성공률을 시뮬레이션 | PENDING_NUMERIC_SIMULATION |
| OMW-AUD-469 | 금고 투자로 매 방문 전체 재고 독식 | TREASURY_BUYOUT_SNOWBALL | 전체 매입률·다른 골드 지출 포기 비용 Stop-ship | PENDING_NUMERIC_SIMULATION |
| OMW-AUD-470 | 이동권 3/3에서 보장 슬롯이 무효 | DEAD_GUARANTEED_SLOT | 룰렛 1회 할인으로 상태 기반 대체 | MITIGATED_STATE_SUBSTITUTION |
| OMW-AUD-471 | 직접 병종 판매가 룰렛을 우회 | DIRECT_UNIT_SALE_BYPASS | 병종·T3·Hero·Legendary 직접 판매 금지 | MITIGATED_FORBIDDEN |
| OMW-AUD-472 | 연구 가속이 전술 직접 해금으로 변질 | DIRECT_UNLOCK_BYPASS | Tier·동시 연구 규칙 유지, 직접 해금 금지 | MITIGATED_GUARDRAIL |
| OMW-AUD-473 | 마력 판매로 마력탑 성장 무효화 | DIRECT_MANA_SALE_BYPASS | 마력 직접 판매 금지 | MITIGATED_FORBIDDEN |
| OMW-AUD-474 | 수리 서비스가 파괴 건물 무료 부활 | FREE_REBUILD_BYPASS | 손상 건물만, 부활·완전 무상 복구 금지 | MITIGATED_TARGET_LIMIT |
| OMW-AUD-475 | 건물 분기 재선택권이 비가역 결정 파괴 | BUILDING_BRANCH_RESELECT_BYPASS | 분기 재선택 상품 금지 | MITIGATED_FORBIDDEN |
| OMW-AUD-476 | Boss 전 필수 카운터를 상점에 숨김 | MERCHANT_HARD_COUNTER_DEPENDENCY | 필수 카운터 보장·단일 구매 의존 금지 | MITIGATED_MULTI_PATH |
| OMW-AUD-477 | 무료·유료 reroll 반복으로 최적 재고 탐색 | INFINITE_REROLL_EXPLOIT | 기본 reroll 없음, 무한 reroll 금지 | MITIGATED_NO_REROLL |
| OMW-AUD-478 | 할인 중첩으로 비용 0 또는 음수 | DISCOUNT_STACKING_EXPLOIT | 한 행동 1회, 중첩 금지 | MITIGATED_SINGLE_USE |
| OMW-AUD-479 | 다음 Stage 이후 할인 권리 무한 보관 | DISCOUNT_LIFETIME_LEAK | 다음 Stage 시작 시 소멸 | MITIGATED_EXPLICIT_EXPIRY |
| OMW-AUD-480 | 같은 서비스가 네 칸 대부분을 점유 | INVENTORY_DUPLICATION_OVERLOAD | 중복 상한과 상태 유효성 필터 | MITIGATED_DIVERSITY_GUARD |
| OMW-AUD-481 | 상품 구매가 다른 가격을 숨겨 변경 | HIDDEN_PRICE_MUTATION | 구매 전 전체 공개, 구매 후 비구매 슬롯 불변 | MITIGATED_TRANSPARENCY |
| OMW-AUD-482 | 중복 클릭으로 같은 재고 두 번 구매 | DUPLICATE_PURCHASE_TRANSACTION | 거래 ID·재고 소비·골드 차감 멱등 처리 | PENDING_RUNTIME_PLAN |
| OMW-AUD-483 | 구매 직후 크래시로 골드만 차감 | PURCHASE_CRASH_PARTIAL_COMMIT | 골드와 효과 원자적 복구 | PENDING_RUNTIME_PLAN |
| OMW-AUD-484 | checkpoint 재로드로 구매 전 상태 복제 | CHECKPOINT_PURCHASE_DUPLICATION | 방문·재고·거래 ID 저장 계약 | PENDING_RUNTIME_PLAN |
| OMW-AUD-485 | 상인 전용 통화 추가로 경제 과밀 | MERCHANT_CURRENCY_BLOAT | 골드 단일 통화 유지 | MITIGATED_GOLD_ONLY |
| OMW-AUD-486 | 상시 HUD 상점 회귀 | ALWAYS_AVAILABLE_SHOP_REGRESSION | Stage 종료 정비시간 전용 | MITIGATED_VISIT_WINDOW |
| OMW-AUD-487 | 전투 중 상인 재진입·구매 | COMBAT_MERCHANT_REENTRY | 전투 중 접근 금지 | MITIGATED_FORBIDDEN |
| OMW-AUD-488 | Stage 20 뒤 상인 등장 | STAGE_20_MERCHANT_REGRESSION | 최종 정산 우선, 상인 생성 금지 | MITIGATED_FINAL_EXCEPTION |
| OMW-AUD-489 | Act 진행에 따라 가격만 자동 인플레이션 | STAGE_NUMBER_PRICE_INFLATION | 상품 가치·경제·Act를 함께 검증 | PENDING_NUMERIC_SIMULATION |
| OMW-AUD-490 | 초반 상인이 비싸서 아무 선택도 없음 | DECORATIVE_EARLY_MERCHANT | 최소 구매 가능성·미구매 선택 모두 검증 | PENDING_NUMERIC_SIMULATION |
| OMW-AUD-491 | 문서 정본을 제품 구현 승인으로 오해 | PREMATURE_PRODUCT_AUTHORITY | 제품·데이터·수치·런타임 승인 차단 | MITIGATED_BOUNDARY |

## 필수 수치 검증

- Stage별 상인 구매율과 전체 재고 매입률.
- 이동권·수리·연구 가속·할인의 평균 골드 대비 가치.
- 금고 투자별 상인 매입 능력과 건설·룰렛·연구 포기 비용.
- 상인 미구매 Run의 생존 가능성.
- 이동권 3/3 대체 할인의 실제 선택률.
- Act별 무효 상품 생성률과 재고 중복률.

## 런타임 Stop-ship

- 같은 재고 두 번 구매 가능.
- 골드 차감과 상품 적용이 분리 저장됨.
- Stage 20 뒤 상인 생성.
- 전투 중 재진입 가능.
- 할인 중첩 또는 다음 Stage 이후 잔존.
- 수리·연구 대상이 무효인데 구매 가능.

## 제품 경계

```text
PRODUCT_CODE = UNCHANGED
DATA_MIGRATION = NOT_AUTHORIZED
EXACT_NUMERICS = PENDING_SIMULATION
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
```
