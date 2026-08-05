# [현행] 오멘워드 기획 정본 결정 원장

```yaml
updated_at: 2026-08-05
status: CURRENT_DECISION_LEDGER / ACTIVE_PLANNING_BRANCH
current_planning_decision: OMW-DEC-20260805-PLANNING-STAGE-END-MERCHANT-V1
current_process_policy: OMW-PROC-20260805-BENCHMARK-TDD-APPROVAL-BATCH-V1
lifecycle_policy: OMW-PROC-20260804-DYNAMIC-CURRENT-MAIN-AND-DOCUMENT-LIFECYCLE-V1
current_main: RESOLVE_FROM_REPOSITORY_DEFAULT_BRANCH
work_mode: TOTAL_PLANNING
last_merged_planning_pr: 140
last_merged_planning_commit: 3b212e61b4b6cfcf51282ba44e0e24cfd20ed61e
current_working_pr: 141
current_count: 6_OF_10
product_code_authority: NONE
image_generation: STOPPED_BY_USER
```

## 1. 운영 원칙

- `PROJECT_CORE.md`가 제품 정체성과 핵심 불변을 소유한다.
- `DOCUMENTATION_MAP.md`와 `DOCUMENT_LIFECYCLE_REGISTRY.md`가 현재 권위를 소유한다.
- `current_main`은 저장소 기본 브랜치에서 동적으로 해석한다.
- Google Sheet는 같은 Decision ID와 exact PR HEAD로 동기화한다.
- 벤치마크·현업 비교·채택·비채택 이유를 기록한다.
- 승인 10건은 최대 배치 크기이며 고위험 충돌·세션 종료·대규모 영향 시 조기 체크포인트를 허용한다.
- 모든 행동 변경은 `RED → GREEN → REFACTOR`로 진행한다.
- main은 검증된 PR 병합으로만 변경한다.

## 2. Planning Batch

| 순서 | 상태 | Decision |
|---|---|---|
| 1/10 | 완료 | `OMW-DEC-20260804-PLANNING-CORE-FUN-AND-CONTENT-GUARDRAILS-V1` |
| 2/10 | 완료 | `OMW-DEC-20260804-PLANNING-STAGE-WAVE-DANGER-BOSS-PRESSURE-MATRIX-V1` |
| 3/10 | 완료 | `OMW-DEC-20260805-PLANNING-SIX-BUILDING-T2-T3-BRANCHES-AND-COUNTERS-V1` |
| 4/10 | 완료 | `OMW-DEC-20260805-PLANNING-TROOP-ROLES-SYNERGIES-AND-COUNTERS-V1` |
| 5/10 | 완료 | `OMW-DEC-20260805-PLANNING-TACTICAL-SKILLS-AND-MANA-V1` |
| 6/10 | 현행 | `OMW-DEC-20260805-PLANNING-STAGE-END-MERCHANT-V1` |
| 7/10 | 다음 | `OMW-DEC-20260805-PLANNING-FIRST-10-15-MINUTES-FLOW-V1` |

## 3. Decision 6/10 — Stage 종료 상인

책임 원본:

- `design/APPROVED_OMENWARD_STAGE_END_MERCHANT_2026-08-05.md`
- `reviews/ADVERSARIAL_STAGE_END_MERCHANT_ECONOMY_AND_INVENTORY_REVIEW_2026-08-05.md`
- `superpowers/specs/2026-08-05-stage-end-merchant-design.md`
- `superpowers/specs/2026-08-05-stage-end-merchant-design-amendment.md`
- `superpowers/plans/2026-08-05-stage-end-merchant.md`

```text
MERCHANT_VISIT_STAGES = 1_TO_19
STAGE_20_MERCHANT = FORBIDDEN
TOTAL_MERCHANT_SLOTS = 4
VISIT_STOCK = FINITE
PURCHASE_CURRENCY = GOLD_ONLY
```

재고:

```text
A = 룰렛 제어
B = 복구 서비스
C = 성장 보조
D = 가변 기회
```

결정:

- 이동권이 3개 미만이면 이동권, 3/3이면 다음 룰렛 1회 할인을 제시한다.
- 상인은 손상 건물 수리·전술 연구 가속·다음 행동 1회 비용 할인을 제공할 수 있다.
- 병종·T3·Hero·Legendary·전술스킬·마력·건물 분기·Stage 정보 직접 판매는 금지한다.
- 상시 상점·전투 중 재진입·무한 구매·무한 reroll·할인 중첩은 금지한다.
- 정확 가격·재고 수·등장률·할인율은 `PENDING_SIMULATION`이다.

## 4. TDD·적대적 감사

```text
RED_RUN = Project Core Documentation 986
RED_RESULT = FAILURE_AS_EXPECTED
RED_EXISTING_CONTRACTS = 55 PASS
OMW-AUD-468~491 = REQUIRED_FIXES_APPLIED
GREEN = PENDING_FINAL_CENTRAL_AND_SHEET_SYNC
PRODUCT_CODE = UNCHANGED
```

final exact-head·merge 증거는 PR #141과 Sheet 현재 상태 셀이 소유한다.

## 5. 감사 계보

```text
OMW-AUD-360~375 = 핵심 재미·정본 충돌
OMW-AUD-376~397 = Stage 압력
OMW-AUD-398~419 = 건물 분기
OMW-AUD-420~443 = 병종 역할
OMW-AUD-444~467 = 전술스킬·마력·연구
OMW-AUD-468~491 = Stage 종료 상인·골드 경제·재고·거래
```

## 6. 수명주기

- `[현행]`: 6/10 책임 원본·Spec·Amendment·Plan·Review.
- `[대체됨]`: 상시 HUD 상점·무한 재고·직접 핵심 보상 판매·과거 마력탑 분기·구형 자원명.
- `[보류]`: 첫 10~15분·Hero·Legendary·Meta·Hub.
- `[폐기]`: 자동 시전·Stage 전 편성·복수 마력탑·병렬 연구·상인 무한 reroll·할인 중첩.
- `[증거]`: 과거 PR·CI·Sheet·Legacy Prototype.

## 7. 제품 경계

```text
CURRENT_PRODUCT = LEGACY_PROTOTYPE
LATEST_PLANNING = STAGE_END_MERCHANT_CANON_NOT_IMPLEMENTED
PRODUCT_CODE = UNCHANGED
DATA_MIGRATION = NOT_AUTHORIZED
EXACT_NUMERICS = PENDING_SIMULATION
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
```

## 8. 완료 이력

```text
OMW-DEC-20260805-PLANNING-SIX-BUILDING-T2-T3-BRANCHES-AND-COUNTERS-V1
3_OF_10
OMW-DEC-20260805-PLANNING-TROOP-ROLES-SYNERGIES-AND-COUNTERS-V1
4_OF_10
OMW-DEC-20260805-PLANNING-TACTICAL-SKILLS-AND-MANA-V1
5_OF_10
LEGACY_C1_C2_C3_PROVEN
```
