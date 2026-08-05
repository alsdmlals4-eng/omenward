# [현행] OMENWARD 프로젝트 인수인계 컨텍스트

```yaml
updated_at: 2026-08-05
project: OMENWARD / 오멘워드
work_mode: TOTAL_PLANNING
phase: CORE_FUN_AND_CONTENT_DEEPENING
current_decision: OMW-DEC-20260805-PLANNING-TROOP-ROLES-SYNERGIES-AND-COUNTERS-V1
current_process_policy: OMW-PROC-20260805-BENCHMARK-TDD-APPROVAL-BATCH-V1
current_main: RESOLVE_FROM_REPOSITORY_DEFAULT_BRANCH
current_grill_me_count: 4_OF_10
working_pr: 139
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
design/APPROVED_OMENWARD_STAGE_WAVE_DANGER_BOSS_PRESSURE_MATRIX_2026-08-04.md
design/APPROVED_OMENWARD_SIX_BUILDING_T2_T3_BRANCHES_AND_COUNTERS_2026-08-05.md
design/APPROVED_OMENWARD_TROOP_ROLES_SYNERGIES_AND_COUNTERS_2026-08-05.md
reviews/ADVERSARIAL_TROOP_ROLE_SYNERGY_AND_COUNTER_REVIEW_2026-08-05.md
process/APPROVED_BENCHMARK_TDD_AND_APPROVAL_BATCH_POLICY_2026-08-05.md
CURRENT_IMPLEMENTATION_STATUS.md
PROJECT_CANON_DECISION_LEDGER.md
DECISIONS_PENDING.md
```

대상 파일이 lifecycle registry에서 `[현행]`인지 확인한 뒤 사용한다.

## 2. 핵심 재미

> **건물로 룰렛을 만들고, 룰렛으로 전선을 지휘한다.**

```text
예고된 압력
→ 제작한 확률
→ 비가역 전선 커밋
→ 설명 가능한 결과·다음 설계
```

## 3. Stage·건물 기준선

```text
MapRun = 20 Stage
Wave Beat = 3
Danger = 4 / 9 / 14 / 19
Boss = 5 / 10 / 15 / 20
압력 = MASS / ARMORED / FLYING / INFILTRATION / SIEGE
```

```text
건물 인스턴스 T1
├─ T2 A → T3 A
└─ T2 B → T3 B
CROSS_BRANCH = FORBIDDEN
DUAL_T3 = FORBIDDEN
```

## 4. 현재 병종 정본 — 4/10

```text
ROSTER_BASELINE: 10
ROSTER_COUNT_IS_NOT_SACRED
ROSTER_MIN_MAX: NOT_PRESET
```

```text
방패수호병 / 대검병 / 창병 / 궁수 / 마도사
사제 / 암살자 / 기병 / 비행병 / 거인
```

| 압력 | 주 대응 | 보조 |
|---|---|---|
| MASS | 대검병·마도사 | 방패수호병 |
| ARMORED | 마도사·창병 | 거인 |
| FLYING | 궁수·비행병 | 요격탑·후속 전술 |
| INFILTRATION | 암살자·기병 | 후방 방패수호병 |
| SIEGE | 창병·기병/암살자 | 거인 역공 |

- 각 압력에는 최소 두 병종 경로와 건물·전술 대안이 필요하다.
- 시너지는 관찰 가능한 행동 연결이며 단순 세트 보너스는 금지한다.
- 암살자·기병·비행병은 우회 추적·공개 Route 대응·공중 우세로 구분한다.
- 전열/기동 병영은 후보 가중을 바꾸되 반대 계열을 삭제하지 않는다.
- 병종 수 증감은 역할 공백·중복·학습량·아트 비용을 근거로 별도 승인한다.

## 5. Tier·룰렛·이동 경계

```text
T1 병종 토큰 = 실제 T1 인게임 이미지
T2 병종 토큰 = 실제 T2 인게임 이미지
T3 병종 토큰 = FORBIDDEN
FREE_RECALL = FORBIDDEN
FREE_CROSS_LANE_MOVE = FORBIDDEN
```

## 6. 검증 증거

```text
RED = Project Core Documentation run 922 / FAILURE_AS_EXPECTED
GREEN_HEAD = bfaf34dbf7c8dd46a7aa833bb782cb3440db6cfd
PROJECT_CORE = 945 / SUCCESS
GDD_SHEET = 652 / SUCCESS
OMENWARD_CORE = 121 / SUCCESS
BASE_V9 = 635 / SUCCESS
SHEET_BOUNDED_READBACK = PASS
REFACTOR = COMPLETE
```

실행 기록과 중앙 상태 갱신으로 HEAD가 변경됐으므로 최종 exact-head CI·Sheet read-back·PR preflight를 다시 수행한다.

## 7. 문서·제품 경계

```text
[현행] = 사용 허용
[대체됨] = 후속 정본 사용
[보류] = 재검증 전 사용 금지
[폐기] = 사용 금지
[증거] = 과거 사실만 허용
```

`data/units/*.tres`는 `[증거] LEGACY_PROTOTYPE_UNIT_DATA / IMPLEMENTATION_INPUT_FORBIDDEN`이다.

```text
CURRENT_PRODUCT = LEGACY_PROTOTYPE
LATEST_APPROVED = TROOP_ROLE_CANON_NOT_IMPLEMENTED
PRODUCT_CODE = UNCHANGED
DATA_MIGRATION = NOT_AUTHORIZED
ART_ASSET_PRODUCTION = NOT_AUTHORIZED
IMAGE_GENERATION = STOPPED_BY_USER
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
CURRENT_COUNT = 4_OF_10
NEXT_DECISION = OMW-DEC-20260805-PLANNING-TACTICAL-SKILLS-AND-MANA-V1
```

완료 이력:

```text
OMW-DEC-20260805-PLANNING-SIX-BUILDING-T2-T3-BRANCHES-AND-COUNTERS-V1
3_OF_10
```