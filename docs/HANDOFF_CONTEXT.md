# [현행] OMENWARD 프로젝트 인수인계 컨텍스트

```yaml
updated_at: 2026-08-05
project: OMENWARD / 오멘워드
work_mode: TOTAL_PLANNING
phase: CORE_FUN_AND_CONTENT_DEEPENING
current_decision: OMW-DEC-20260805-PLANNING-TACTICAL-SKILLS-AND-MANA-V1
current_process_policy: OMW-PROC-20260805-BENCHMARK-TDD-APPROVAL-BATCH-V1
current_main: RESOLVE_FROM_REPOSITORY_DEFAULT_BRANCH
current_grill_me_count: 5_OF_10
working_pr: 140
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
design/APPROVED_OMENWARD_STAGE_WAVE_DANGER_BOSS_PRESSURE_MATRIX_2026-08-04.md
design/APPROVED_OMENWARD_SIX_BUILDING_T2_T3_BRANCHES_AND_COUNTERS_2026-08-05.md
design/APPROVED_OMENWARD_TROOP_ROLES_SYNERGIES_AND_COUNTERS_2026-08-05.md
design/APPROVED_OMENWARD_TACTICAL_SKILLS_AND_MANA_2026-08-05.md
reviews/ADVERSARIAL_TACTICAL_SKILLS_MANA_AND_RESEARCH_REVIEW_2026-08-05.md
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

## 4. 전술스킬·마력 — 5/10

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

- Tier 상승 시 초당 마력 수급량과 연구 가능한 전술 Tier가 증가한다.
- 해금된 모든 전술은 현재 MapRun 동안 사용 가능하다.
- 새 MapRun에서 마력탑 Tier·연구·해금·보유 마력을 초기화한다.
- 대상 무효·취소·Layer 불일치에는 마력을 소비하지 않는다.
- 전술은 병종·건물의 지속 역할을 대체하지 않는다.

## 5. 문서·제품 경계

```text
[현행] = 사용 허용
[대체됨] = 후속 정본 사용
[보류] = 재검증 전 사용 금지
[폐기] = 사용 금지
[증거] = 과거 사실만 허용
```

과거 마력탑 분기와 구형 자원명은 `[대체됨] / IMPLEMENTATION_INPUT_FORBIDDEN`이다.

```text
CURRENT_PRODUCT = LEGACY_PROTOTYPE
LATEST_APPROVED = TACTICAL_MANA_CANON_NOT_IMPLEMENTED
PRODUCT_CODE = UNCHANGED
DATA_MIGRATION = NOT_AUTHORIZED
ART_ASSET_PRODUCTION = NOT_AUTHORIZED
IMAGE_GENERATION = STOPPED_BY_USER
EXACT_NUMERICS = PENDING_SIMULATION
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
CURRENT_COUNT = 5_OF_10
NEXT_DECISION = OMW-DEC-20260805-PLANNING-STAGE-END-MERCHANT-V1
```

## 6. TDD·Sheet 증거

```text
RED = Project Core Documentation run 954 / FAILURE_AS_EXPECTED
RED_EXISTING_CONTRACTS = 45 PASS
GREEN_CANDIDATE_HEAD = 917445ba9b09260da1f2b7bafb0bbf2f809a834b
PROJECT_CORE = 976 / SUCCESS
GDD_SHEET = 682 / SUCCESS
OMENWARD_CORE = 150 / SUCCESS
BASE_V9 = 665 / SUCCESS
SHEET_CANDIDATE_READBACK = PASS
REFACTOR = COMPLETE
```

최종 exact-head 검증과 merge 증거는 PR #140 및 Sheet 현재 상태 셀에서 확인한다. 문서에 최종 SHA를 반복 고정하지 않는다.

## 7. 완료 이력

```text
OMW-DEC-20260805-PLANNING-SIX-BUILDING-T2-T3-BRANCHES-AND-COUNTERS-V1
3_OF_10
OMW-DEC-20260805-PLANNING-TROOP-ROLES-SYNERGIES-AND-COUNTERS-V1
4_OF_10
LEGACY_C1_C2_C3_PROVEN
```
