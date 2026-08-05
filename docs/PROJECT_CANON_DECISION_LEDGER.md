# [현행] 오멘워드 기획 정본 결정 원장

```yaml
updated_at: 2026-08-05
status: CURRENT_DECISION_LEDGER / ACTIVE_PLANNING_BRANCH
current_planning_decision: OMW-DEC-20260805-PLANNING-TROOP-ROLES-SYNERGIES-AND-COUNTERS-V1
current_process_policy: OMW-PROC-20260805-BENCHMARK-TDD-APPROVAL-BATCH-V1
lifecycle_policy: OMW-PROC-20260804-DYNAMIC-CURRENT-MAIN-AND-DOCUMENT-LIFECYCLE-V1
current_main: RESOLVE_FROM_REPOSITORY_DEFAULT_BRANCH
work_mode: TOTAL_PLANNING
last_merged_planning_pr: 138
last_merged_planning_commit: 797a4c9b1525c1132a26db762bdd06b5f65f3b41
current_working_pr: 139
current_count: 4_OF_10
product_code_authority: NONE
art_asset_production_authority: NONE
image_generation: STOPPED_BY_USER
```

## 1. 운영 원칙

- `PROJECT_CORE.md`가 제품 정체성과 핵심 불변을 소유한다.
- `DOCUMENTATION_MAP.md`와 `DOCUMENT_LIFECYCLE_REGISTRY.md`가 현재 권위와 구형 문서 상태를 소유한다.
- `current_main`과 `context_baseline_commit`은 저장소 기본 브랜치에서 동적으로 해석한다.
- Google Sheet는 같은 Decision ID와 exact PR HEAD로 동기화한다.
- GPT는 핵심 재미·콘텐츠·플레이어 경험·UX·아트 방향을 소유한다.
- Codex는 자료구조·알고리즘·좌표·경로탐색·성능·코드·테스트를 소유한다.
- 관련 벤치마크와 현업 관행을 비교하고 채택·비채택 이유를 기록한다.
- 승인 10건은 최대 정본 배치 크기이며 고위험 충돌·세션 종료·대규모 정본 영향 시 조기 체크포인트를 허용한다.
- 모든 행동 변경은 `RED → GREEN → REFACTOR`로 진행한다.
- GitHub 파일 쓰기는 명시적 비기본 branch에서만 수행하고 main은 검증된 PR 병합으로 변경한다.

## 2. 현재 Planning Batch

| 순서 | 상태 | Decision |
|---|---|---|
| 1/10 | 완료 | `OMW-DEC-20260804-PLANNING-CORE-FUN-AND-CONTENT-GUARDRAILS-V1` |
| 2/10 | 완료 | `OMW-DEC-20260804-PLANNING-STAGE-WAVE-DANGER-BOSS-PRESSURE-MATRIX-V1` |
| 3/10 | 완료 | `OMW-DEC-20260805-PLANNING-SIX-BUILDING-T2-T3-BRANCHES-AND-COUNTERS-V1` |
| 4/10 | 현행 | `OMW-DEC-20260805-PLANNING-TROOP-ROLES-SYNERGIES-AND-COUNTERS-V1` |
| 5/10 | 다음 | `OMW-DEC-20260805-PLANNING-TACTICAL-SKILLS-AND-MANA-V1` |

## 3. Decision 1/10 — 핵심 재미

```text
예고된 압력
→ 제작한 확률
→ 비가역 전선 커밋
→ 설명 가능한 결과·다음 설계
```

압력: `MASS / ARMORED / FLYING / INFILTRATION / SIEGE`.

책임 원본: `design/APPROVED_OMENWARD_CORE_FUN_AND_CONTENT_GUARDRAILS_2026-08-04.md`.

## 4. Decision 2/10 — Stage 압력

```text
MapRun = 20 Stage
Wave Beat = 3
Danger = 4 / 9 / 14 / 19
Boss = 5 / 10 / 15 / 20
```

책임 원본: `design/APPROVED_OMENWARD_STAGE_WAVE_DANGER_BOSS_PRESSURE_MATRIX_2026-08-04.md`.

## 5. Decision 3/10 — 건물 전문화

```text
T1 → T2 A → T3 A
T1 → T2 B → T3 B
CROSS_BRANCH = FORBIDDEN
DUAL_T3 = FORBIDDEN
MAPRUN_PERMANENT_CHOICE
```

책임 원본:

- `design/APPROVED_OMENWARD_SIX_BUILDING_T2_T3_BRANCHES_AND_COUNTERS_2026-08-05.md`
- `reviews/ADVERSARIAL_BUILDING_BRANCH_COUNTER_AND_OPPORTUNITY_COST_REVIEW_2026-08-05.md`

## 6. Decision 4/10 — 병종 역할·시너지·카운터

`OMW-DEC-20260805-PLANNING-TROOP-ROLES-SYNERGIES-AND-COUNTERS-V1`

책임 원본:

- `design/APPROVED_OMENWARD_TROOP_ROLES_SYNERGIES_AND_COUNTERS_2026-08-05.md`
- `reviews/ADVERSARIAL_TROOP_ROLE_SYNERGY_AND_COUNTER_REVIEW_2026-08-05.md`
- `superpowers/specs/2026-08-05-troop-roles-synergies-counters-design.md`
- `superpowers/plans/2026-08-05-troop-roles-synergies-counters.md`

```text
ROSTER_BASELINE: 10
ROSTER_COUNT_IS_NOT_SACRED
ROSTER_MIN_MAX: NOT_PRESET
```

기준선:

```text
방패수호병 / 대검병 / 창병 / 궁수 / 마도사
사제 / 암살자 / 기병 / 비행병 / 거인
```

결정:

- 압력별 최소 두 병종 대응 경로와 건물·전술 대안을 둔다.
- 시너지는 관찰 가능한 전장 행동이며 단순 세트 보너스는 금지한다.
- 암살자·기병·비행병은 우회 추적·공개 Route 대응·공중 우세로 분리한다.
- 병영은 전열/기동 후보 가중을 바꾸되 반대 계열을 영구 삭제하지 않는다.
- 병종 수 증감은 역할 공백·중복·학습량·아트 비용을 근거로 별도 승인한다.
- T1/T2 실제 인게임 이미지를 룰렛에 재사용하고 T3 토큰은 금지한다.
- 제품 수치·AI·데이터는 `PENDING_SIMULATION / NOT_AUTHORIZED`다.

## 7. TDD 증거

```text
RED_RUN = Project Core Documentation 922
RED_RESULT = FAILURE_AS_EXPECTED
RED_CAUSE = TROOP_AUTHORITY / REVIEW / 4_OF_10_ROUTING / LEGACY_UNIT_LIFECYCLE_MISSING
GREEN_CANDIDATE = PR_139_EXACT_HEAD
PRODUCT_CODE = UNCHANGED
```

최종 Green·REFACTOR·Sheet·preflight 증거는 exact PR HEAD에서 갱신한다.

## 8. 적대적 감사 계보

```text
OMW-AUD-208~289 = 전투 결정·유지보수
OMW-AUD-290~299 = 전투 공간·기획 경계
OMW-AUD-300~313 = 전장 시각 계층
OMW-AUD-314~343 = HUD·룰렛·자원·건물·자산 재사용
OMW-AUD-344~359 = 픽셀·일러스트 하이브리드 아트
OMW-AUD-360~375 = 핵심 재미·정본·구형 문서 충돌
OMW-AUD-376~397 = Stage 압력·공정성·리플레이성
OMW-AUD-398~419 = 건물 분기·카운터·포기 비용·운영 정책
OMW-AUD-420~443 = 병종 역할·시너지·카운터·로스터 수·Legacy 데이터 경계
```

## 9. 수명주기

- `[대체됨]`: 구형 master GDD, 15 Wave Stage, 과거 상태 Sync.
- `[보류]`: 첫 10분·첫 4공세·Hero·Legendary·Meta·Hub·구형 구현 계획.
- `[폐기]`: 식량 핵심 자원, 건물 5종, 주변 지휘소, 별도 룰렛 아이콘, T3 룰렛 토큰, 단순 세트 보너스, 병영 반대 계열 삭제, 하드키 병종.
- `[증거]`: PR·CI·벤치마크·archive·`data/units/*.tres` Legacy Prototype.

## 10. 현재 경계와 다음 Gate

```text
CURRENT_PRODUCT = LEGACY_PROTOTYPE
LATEST_PLANNING = TROOP_ROLE_CANON_NOT_IMPLEMENTED
PRODUCT_CODE = UNCHANGED
DATA_MIGRATION = NOT_AUTHORIZED
SIMULATION_TOOL_CODE = NOT_AUTHORIZED
ART_ASSET_PRODUCTION = NOT_AUTHORIZED
IMAGE_GENERATION = STOPPED_BY_USER
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
CURRENT_COUNT = 4_OF_10
NEXT_DECISION = OMW-DEC-20260805-PLANNING-TACTICAL-SKILLS-AND-MANA-V1
```