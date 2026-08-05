# [현행] OMENWARD 프로젝트 인수인계 컨텍스트

```yaml
updated_at: 2026-08-05
project: OMENWARD / 오멘워드
work_mode: TOTAL_PLANNING
phase: CORE_FUN_AND_CONTENT_DEEPENING
current_decision: OMW-DEC-20260805-PLANNING-STAGE-END-MERCHANT-V1
current_process_policy: OMW-PROC-20260805-BENCHMARK-TDD-APPROVAL-BATCH-V1
current_main: RESOLVE_FROM_REPOSITORY_DEFAULT_BRANCH
current_grill_me_count: 6_OF_10
working_pr: 141
product_code_authority: NONE
art_asset_production_authority: NONE
image_generation: STOPPED_BY_USER
simulation: NOT_RUN
runtime: NOT_RUN
human_qa: NOT_RUN
```

## 1. 먼저 읽을 문서

```text
PROJECT_CORE.md
ACTIVE_CONTEXT.md
DOCUMENTATION_MAP.md
DOCUMENT_LIFECYCLE_REGISTRY.md
OMENWARD_GDD_CURRENT_CANON.md
design/APPROVED_VERTICAL_SLICE_SYSTEM_CONTRACT_2026-07-27.md
design/APPROVED_OMENWARD_TACTICAL_SKILLS_AND_MANA_2026-08-05.md
design/APPROVED_OMENWARD_STAGE_END_MERCHANT_2026-08-05.md
reviews/ADVERSARIAL_STAGE_END_MERCHANT_ECONOMY_AND_INVENTORY_REVIEW_2026-08-05.md
CURRENT_IMPLEMENTATION_STATUS.md
PROJECT_CANON_DECISION_LEDGER.md
DECISIONS_PENDING.md
```

대상 파일이 lifecycle registry에서 `[현행]`인지 확인한 뒤 사용한다.

## 2. 핵심 재미

> **건물로 룰렛을 만들고, 룰렛으로 전선을 지휘한다.**

```text
예고된 압력
→ 제작한 확률·연구 선택
→ 비가역 전선 커밋
→ 마력 기반 수동 전술
→ Stage 종료 제한 상인 선택
→ 설명 가능한 결과·다음 설계
```

## 3. Stage·건물·병종 기준선

```text
MapRun = 20 Stage
Wave Beat = 3
Danger = 4 / 9 / 14 / 19
Boss = 5 / 10 / 15 / 20
압력 = MASS / ARMORED / FLYING / INFILTRATION / SIEGE
```

병종 기준선은 방패수호병·대검병·창병·궁수·마도사·사제·암살자·기병·비행병·거인 10종이다. 수량은 역할 근거와 별도 승인에 따라 증감할 수 있다.

다섯 분기 건물은 3/10 계보를 유지한다. 마력탑만 5/10의 선형 예외를 사용한다.

## 4. 전술스킬·마력 — 완료 5/10

```text
마력탑 최대 활성 수 = 1
마력탑 T1 → T2 → T3
분기 = FORBIDDEN
동시 연구 = 1
연구 = 골드 + 시간
시전 = 마력
Stage 전 편성 = 없음
자동 시전 = 금지
```

```text
T1 4종 = 속박진 / 수호장 / 집중 명령 / 충격파
T2 3종 = 폭풍 억제 / 파쇄 명령 / 봉쇄 결계
T3 3종 = 결전의 깃발 / 성역 / 시간 왜곡
```

## 5. Stage 종료 상인 — 현행 6/10

```text
MERCHANT_VISIT_STAGES = 1_TO_19
STAGE_20_MERCHANT = FORBIDDEN
TOTAL_MERCHANT_SLOTS = 4
VISIT_STOCK = FINITE
PURCHASE_CURRENCY = GOLD_ONLY
```

```text
A = 룰렛 제어
B = 복구 서비스
C = 성장 보조
D = 가변 기회
```

- 이동권 3개 미만에는 이동권, 3/3에는 다음 룰렛 1회 할인을 제시한다.
- 수리 대상·연구 대상·할인 대상이 없으면 유효 상품으로 대체한다.
- 병종·T3·Hero·Legendary·전술스킬·마력·건물 분기·Stage 정보 직접 판매는 금지한다.
- 상시 상점·전투 중 재진입·무한 구매·무한 reroll·할인 중첩은 금지한다.
- 가격·재고·등장률·할인율은 `PENDING_SIMULATION`이다.

## 6. 문서·제품 경계

```text
[현행] = 사용 허용
[대체됨] = 후속 정본 사용
[보류] = 재검증 전 사용 금지
[폐기] = 사용 금지
[증거] = 과거 사실만 허용
```

과거 마력탑 분기·구형 자원명·상시 상점·무한 재고·직접 핵심 보상 판매는 `[대체됨] / IMPLEMENTATION_INPUT_FORBIDDEN`이다.

```text
CURRENT_PRODUCT = LEGACY_PROTOTYPE
LATEST_APPROVED = STAGE_END_MERCHANT_CANON_NOT_IMPLEMENTED
PRODUCT_CODE = UNCHANGED
DATA_MIGRATION = NOT_AUTHORIZED
ART_ASSET_PRODUCTION = NOT_AUTHORIZED
IMAGE_GENERATION = STOPPED_BY_USER
EXACT_NUMERICS = PENDING_SIMULATION
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
CURRENT_COUNT = 6_OF_10
NEXT_DECISION = OMW-DEC-20260805-PLANNING-FIRST-10-15-MINUTES-FLOW-V1
```

## 7. TDD·Sheet 증거

```text
RED = Project Core Documentation run 986 / FAILURE_AS_EXPECTED
RED_EXISTING_CONTRACTS = 55 PASS
GREEN = PENDING_FINAL_CENTRAL_AND_SHEET_SYNC
```

최종 exact-head 검증과 merge 증거는 PR #141 및 Sheet 현재 상태 셀에서 확인한다. 문서에 최종 SHA를 반복 고정하지 않는다.

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
