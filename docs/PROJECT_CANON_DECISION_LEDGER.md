# [현행] 오멘워드 기획 정본 결정 원장

```yaml
updated_at: 2026-08-05
status: CURRENT_DECISION_LEDGER / ACTIVE_PLANNING_BRANCH
current_planning_decision: OMW-DEC-20260805-PLANNING-SIX-BUILDING-T2-T3-BRANCHES-AND-COUNTERS-V1
current_process_policy: OMW-PROC-20260805-BENCHMARK-TDD-APPROVAL-BATCH-V1
lifecycle_policy: OMW-PROC-20260804-DYNAMIC-CURRENT-MAIN-AND-DOCUMENT-LIFECYCLE-V1
current_main: RESOLVE_FROM_REPOSITORY_DEFAULT_BRANCH
work_mode: TOTAL_PLANNING
last_merged_planning_pr: 136
last_merged_planning_commit: b1b1f5ff4af9b7e53df12f282415daf7fde30a9b
last_recovery_pr: 137
last_recovery_commit: a426aef7738a2d9aa8c40cf1eddbe97601e22f80
current_count: 3_OF_10
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
- 승인 10건은 최대 정본 배치 크기다. P0/P1 충돌·세션 종료·대규모 정본 영향 시 조기 체크포인트를 허용한다.
- 모든 행동 변경은 `RED → GREEN → REFACTOR`로 진행한다.
- GitHub 파일 쓰기는 명시적 비기본 branch에서만 수행하고 main은 검증된 PR 병합으로 변경한다.

## 2. 이전 10개 결정과 새 Batch

| 구간 | 핵심 |
|---|---|
| 이전 1~6 | 전투 공정성·Damage·Status·Modifier 의미 |
| 이전 7 | 세 전선·Route·Targeting 경험 |
| 이전 8 | 전장 시각 계층·카메라 |
| 이전 9 | HUD·룰렛·자원·상인·건물 6종 |
| 이전 10 | 픽셀·일러스트 하이브리드 아트 |
| 새 1 | 핵심 재미·콘텐츠 가드레일·문서 lifecycle |
| 새 2 | Stage·Wave·Danger·Boss 압력 매트릭스 |
| 새 3 | 건물 6종 T2/T3 분기·카운터 |

## 3. Decision 1/10 — 핵심 재미

`OMW-DEC-20260804-PLANNING-CORE-FUN-AND-CONTENT-GUARDRAILS-V1`

책임 원본:

`design/APPROVED_OMENWARD_CORE_FUN_AND_CONTENT_GUARDRAILS_2026-08-04.md`

```text
예고된 압력
→ 제작한 확률
→ 비가역 전선 커밋
→ 설명 가능한 결과·다음 설계
```

압력: `MASS / ARMORED / FLYING / INFILTRATION / SIEGE`.

## 4. Decision 2/10 — Stage 압력

`OMW-DEC-20260804-PLANNING-STAGE-WAVE-DANGER-BOSS-PRESSURE-MATRIX-V1`

책임 원본:

`design/APPROVED_OMENWARD_STAGE_WAVE_DANGER_BOSS_PRESSURE_MATRIX_2026-08-04.md`

```text
MapRun = 20 Stage
Wave Beat = 3
Danger = 4 / 9 / 14 / 19
Boss = 5 / 10 / 15 / 20
```

- 1~5 압력 문해력, 6~10 조합, 11~15 기회비용, 16~20 종합 숙련.
- Stage 시작 전 압력·전선·Route·목표·치명 행동 공개.
- Danger는 한 공개 규칙 변형.
- Boss는 Route·태세·목표·호위·집중 공격 기회를 변경.
- 정확한 시간·Threat Budget·적 수치는 시뮬레이션 전 미확정.

## 5. Decision 3/10 — 건물 전문화

`OMW-DEC-20260805-PLANNING-SIX-BUILDING-T2-T3-BRANCHES-AND-COUNTERS-V1`

책임 원본:

- `design/APPROVED_OMENWARD_SIX_BUILDING_T2_T3_BRANCHES_AND_COUNTERS_2026-08-05.md`
- `reviews/ADVERSARIAL_BUILDING_BRANCH_COUNTER_AND_OPPORTUNITY_COST_REVIEW_2026-08-05.md`
- `superpowers/specs/2026-08-05-six-building-t2-t3-branches-design.md`
- `superpowers/plans/2026-08-05-six-building-t2-t3-branches-implementation.md`

공통 문법:

```text
T1 → T2 A → T3 A
T1 → T2 B → T3 B
CROSS_BRANCH = FORBIDDEN
DUAL_T3 = FORBIDDEN
MAPRUN_PERMANENT_CHOICE
```

| 건물 | A 경로 | B 경로 |
|---|---|---|
| 금고 | 안정→비축 | 행운→징조 대박 |
| 농장 | 징집→대규모 동원 | 예비→최후 예비대 |
| 병영 | 전열→정예 전열 | 기동→징조 대응대 |
| 방어탑 | 연사→요격 | 포격→파성 |
| 지휘소 | 돌격→결전 전선 | 수비→종심 방어 |
| 마력탑 | 유량→맥동 | 저장→징조 저장고 |

결정:

- 선택은 건물 인스턴스별.
- 다른 인스턴스는 다른 분기 선택 가능.
- 모든 분기에 얻는 것·포기하는 것·압력 적합성·핵심 루프 영향 명시.
- T3는 순수 수치가 아니라 결과 곡선·표적·전선 교리·Route·자원 타이밍을 변경.
- 철거는 인스턴스와 효과를 제거하고 재건은 새 선택. 정확한 환불·비용은 경제 결정으로 이관.
- 건물만으로 다섯 압력을 모두 해결하지 않음.
- 정확한 비용·배율·범위·쿨다운은 `PENDING_SIMULATION`.
- 제품 구현은 병종·전술 결정과 압력 대응 재검증 전 차단.

## 6. 운영 정책 — 비카운터

`OMW-PROC-20260805-BENCHMARK-TDD-APPROVAL-BATCH-V1`

```text
BENCHMARK_REQUIRED
INDUSTRY_COMPARISON_REQUIRED
MAX_APPROVAL_BATCH = 10
EARLY_CHECKPOINT = HIGH_RISK_CONFLICT / SESSION_END / LARGE_CANON_IMPACT
TDD = RED → GREEN → REFACTOR
EXPLICIT_BRANCH_REQUIRED_FOR_GITHUB_MUTATION
DIRECT_MAIN_WRITE = FORBIDDEN
```

직접 main 쓰기 사고는 PR #137에서 원상복구했다. 해당 파일은 승인 정본으로 취급하지 않았고 새 작업은 PR #138의 명시적 branch에서 RED부터 재시작했다.

## 7. TDD 증거

```text
RED_RUN = Project Core Documentation 888
RED_RESULT = FAILURE_AS_EXPECTED
RED_CAUSE = BUILDING_AUTHORITY / PROCESS_POLICY / 3_OF_10_ROUTING_MISSING
GREEN_CANDIDATE = PR_138_DOCUMENTATION_BRANCH
PRODUCT_CODE = UNCHANGED
```

최종 Green·Refactor·Sheet·preflight 증거는 exact PR HEAD에서 갱신한다.

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
```

## 9. 수명주기

- `[대체됨]`: 구형 master GDD, 15 Wave Stage, 과거 상태 Sync.
- `[보류]`: 첫 10분·첫 4공세·Hero·Legendary·Meta·Hub·구형 구현 계획.
- `[폐기]`: 식량 핵심 자원, 건물 5종, 주변 지휘소, 별도 룰렛 아이콘, T3 룰렛 토큰, 동일 인스턴스 교차 분기·양쪽 T3.
- `[증거]`: PR·CI·벤치마크·archive.

## 10. 현재 경계와 다음 Gate

```text
CURRENT_PRODUCT = LEGACY_PROTOTYPE
LATEST_PLANNING = BUILDING_BRANCH_CANON_NOT_IMPLEMENTED
PRODUCT_CODE = UNCHANGED
SIMULATION_TOOL_CODE = NOT_AUTHORIZED
ART_ASSET_PRODUCTION = NOT_AUTHORIZED
IMAGE_GENERATION = STOPPED_BY_USER
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
CURRENT_COUNT = 3_OF_10
NEXT_DECISION = OMW-DEC-20260805-PLANNING-TROOP-ROLES-SYNERGIES-AND-COUNTERS-V1
NEXT_AFTER = OMW-DEC-20260805-PLANNING-TACTICAL-SKILLS-AND-MANA-STONE-V1
```
