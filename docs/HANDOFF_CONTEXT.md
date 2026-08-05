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

세 원형 릴은 3×3 노출창의 세 열이다.

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

- Stage 시작 전에 압력·전선·Route·목표·치명 행동을 공개한다.
- 건물 분기는 얻는 것과 포기하는 것을 함께 표시한다.
- 정확한 적 수·시간·Threat Budget·건물 수치는 시뮬레이션 전 미확정이다.

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
- 시너지는 전장에서 관찰 가능한 행동 연결이며 단순 세트 보너스는 금지한다.
- 암살자·기병·비행병은 우회 추적·공개 Route 대응·공중 우세로 구분한다.
- 전열/기동 병영은 후보 가중을 바꾸되 반대 계열을 영구 삭제하지 않는다.
- 병종 수 증감은 역할 공백·중복·학습량·아트 비용을 근거로 별도 승인한다.

## 5. Tier·룰렛·이동 경계

```text
T1 병종 토큰 = 실제 T1 인게임 이미지
T2 병종 토큰 = 실제 T2 인게임 이미지
T3 병종 토큰 = FORBIDDEN
FREE_RECALL = FORBIDDEN
FREE_CROSS_LANE_MOVE = FORBIDDEN
```

T3는 결과 Preview·보관함·배치 카드·전장 병종으로만 표현한다.

## 6. 자원·HUD·아트

```text
자원 = 골드 / 마석 / 배치 병력·병력 한도 / 이동권
건물 = 금고 / 농장 / 병영 / 방어탑 / 지휘소 / 마력탑
하단 = [룰렛] [보관함] [건설] [전술스킬] [벨루]
상인 = Stage 종료 정비시간
STYLE = PIXEL_ILLUSTRATION_HYBRID
```

실제 이미지·아트 제작은 중단 상태다.

## 7. TDD·검증 상태

```text
RED = Validate Project Core Documentation run 922
RED_CAUSE = TROOP_CANON / REVIEW / 4_OF_10_ROUTING / LEGACY_UNIT_LIFECYCLE_MISSING
GREEN_CANDIDATE = PR_139_EXACT_HEAD
```

최종 Green·REFACTOR·Sheet·preflight 증거는 PR #139 exact HEAD에서 갱신한다.

## 8. 문서 수명주기

- `[현행]`: 사용 허용.
- `[대체됨]`: 후속 정본 사용.
- `[보류]`: 재검증 전 사용 금지.
- `[폐기]`: 사용 금지.
- `[증거]`: 과거 사실만 허용.

`data/units/*.tres`는 `[증거] LEGACY_PROTOTYPE_UNIT_DATA / IMPLEMENTATION_INPUT_FORBIDDEN`이다.

## 9. GPT·Codex 경계

```text
GPT / Work = 핵심 재미·콘텐츠·병종 역할·시너지·카운터·UX·아트·검수 기준
Codex = 자료구조·알고리즘·좌표·경로탐색·Spawn·Targeting·AI·성능·코드·테스트
```

정확한 체력·공격력·관통·회복·속도·확률·비용을 기획 추정치로 구현하지 않는다.

## 10. 현재 금지선과 다음 Gate

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