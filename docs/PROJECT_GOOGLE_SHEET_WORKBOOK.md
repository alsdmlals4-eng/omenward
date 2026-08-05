# [현행] OMENWARD Google Sheet 정본 동기화 계약

```yaml
updated_at: 2026-08-06
spreadsheet_id: 1VLwRtXGDtyj0JFt98wdIOtG6Zqc3wtdfCzSF9Fo6lpw
status: PROJECT_SHEET_CONFIGURED / USER_FACING_GDD_WORKSPACE / PROPOSED_SHEET_CHANGE
current_decision: OMW-DEC-20260805-PLANNING-FIRST-10-15-MINUTES-FLOW-V1
current_count: 7_OF_10_IN_PROGRESS
approval_checkpoint: PARTIAL_APPROVAL_4_OF_10
current_working_pr: 142
```

Google Sheet는 GitHub 정본을 운영·탐색 목적으로 미러링하는 `USER_FACING_GDD_WORKSPACE`다. Sheet 단독 변경은 정본 변경이 아니며, PR 병합 전 쓰기는 `PROPOSED_SHEET_CHANGE` 상태로 취급한다.

## 1. 7/10 부분 승인 동기화 대상

반드시 기록할 항목:

```text
Decision ID = OMW-DEC-20260805-PLANNING-FIRST-10-15-MINUTES-FLOW-V1
exact Draft PR HEAD
Planning counter = 7_OF_10_IN_PROGRESS
Approval checkpoint = PARTIAL_APPROVAL_4_OF_10
Onboarding format = IN_RUN_PROGRESSIVE_DISCLOSURE
First session = REAL_MAPRUN
SYSTEM_EXPOSURE_ORDER = APPROVED_FOUNDATION_THEN_BRANCH_CHOICE
STAGE_1_T1_BUILDINGS = ONE_EACH_ALL_SIX
STAGE_1_T1_BUILD_BUDGET = GUARANTEED_SUFFICIENT_FOR_REQUIRED_SET
STAGE_1_BUILD_CURRENCY = REAL_GOLD
T1_BUILDING_EXPLANATION = BRIEF_ROLE_LABELS
T1_BUILDING_PLACEMENT = PLAYER_EXECUTED
T1_BUILDING_BRANCH_CHOICE = NONE
FIRST_MEANINGFUL_COMBAT_CHOICE = STAGE_1_IRREVERSIBLE_DEPLOYMENT
FIRST_MEANINGFUL_BUILD_CHOICE = STAGE_2_T2_UPGRADE
STAGE_2_T2_CANDIDATES = TWO_RELEVANT_VALID_OPTIONS
STAGE_2_T2_UPGRADE_BUDGET = GUARANTEED_SUFFICIENT_FOR_ONE_CANDIDATE
T2_UPGRADE_PREVIEW = REQUIRED
MANA_TOWER_T1_INCLUDED_IN_STAGE_1_SET = REQUIRED
MANA_TOWER_STAGE_1_EXPLANATION = BRIEF_RESOURCE_ROLE_ONLY
TACTICAL_RESEARCH_EXPLANATION_BEFORE_STAGE_3 = FORBIDDEN
Stage 1 = build one each of all six T1 buildings, roulette, deployment, combat, first merchant
Stage 2 = two valid T2 candidates, build one, roulette control and multi-front judgment
Stage 3 = mana tower research and manual tactic
Stage 4 = first Danger integration
Stage 5 = first Boss mastery check
Separate tutorial = FORBIDDEN
Stage 1 full-system dump = FORBIDDEN
Rule parity with main run = REQUIRED
Scripted victory = FORBIDDEN
Belu replaces player choice = FORBIDDEN
OMW-AUD-492~523
Remaining decisions = PENDING_GRILLME
Product code / image / animation HX = NOT_AUTHORIZED
```

## 2. 미승인 범위

```text
T1_PLACEMENT_LAYOUT = PENDING_GRILLME
T1_BUILD_ORDER = PENDING_GRILLME
STAGE_1_LEFTOVER_GOLD_POLICY = PENDING_GRILLME
STAGE_1_NON_T1_SPENDING_RULE = PENDING_GRILLME
FIRST_T2_UPGRADE_CANDIDATE_IDENTITIES = PENDING_GRILLME
STAGE_2_LEFTOVER_GOLD_POLICY = PENDING_GRILLME
MINIMUM_VALID_PATHS = PENDING_GRILLME
BELU_INTERVENTION_LEVEL = PENDING_GRILLME
DANGER_EXACT_PRESSURE = PENDING_GRILLME
BOSS_EXACT_PATTERN = PENDING_GRILLME
FAILURE_RETRY_SKIP_RULES = PENDING_GRILLME
HUMAN_VALIDATION_STOP_SHIP = PENDING_GRILLME
EXACT_TIMINGS = PENDING_SIMULATION_AND_HUMAN_QA
```

Sheet 행은 위 항목을 승인 완료처럼 표시하지 않는다.

## 3. 완료된 6/10 상인 기록

과거 6/10 행은 수정하거나 삭제하지 않는다.

```text
OMW-DEC-20260805-PLANNING-STAGE-END-MERCHANT-V1
6_OF_10
PR = 141
MERGED_MAIN = 6b23ca2bb627827651a42ba6db01829e44ee8a14
POST_MERGE_BOUNDED_READBACK = PASS
```

5/10 전술·마력 정본 계보와 1~6/10 완료 행을 보존한다.

## 4. 수명주기

과거 별도 튜토리얼·Stage 1 전체 시스템 덤프·scripted victory·Stage 1 prebuilt T1 시작·T1 장문 설명은 다음 상태로 기록한다.

```text
SUPERSEDED
IMPLEMENTATION_INPUT_FORBIDDEN
```

과거 1~6/10 행은 덮어쓰지 않는다. 동일 Decision ID의 7/10 부분 승인 행은 최신 checkpoint와 exact HEAD로 갱신하며 변경이력에 별도 증거 행을 추가한다.

## 5. 기록 탭

- `00_프로젝트_허브`: 현재 Decision·counter·approval checkpoint·exact HEAD·상태.
- `01_작업순서`: 7/10 진행 범위·다음 GrillMe·TDD 증거.
- `02_현재_확정결정`: Stage 1 여섯 T1 직접 설치와 Stage 2 두 T2 후보 선택.
- `03_근거_라이브러리`: 사용자 지시·Spec·Review·TDD·Lifecycle 근거.
- `04_누락_충돌_감사`: `OMW-AUD-492~523`.
- `05_GDD_요약`: Stage 1·2 핵심 인과와 미승인 범위.
- `12_핵심루프`: 기초 구축→배치→T2 발전→결과 복기.
- `15_조작_게임규칙`: 짧은 T1 설명·실제 골드·T2 비교 Preview·벨루 비대체.
- `40_핵심시스템_메인콘텐츠`: Stage 1~5 시스템 노출 구조와 제품 경계.
- `50_메인콘텐츠`: 첫 상인 노출은 승인, T1 위치·T2 정체·Danger/Boss 정확 내용은 `PENDING_GRILLME`.
- `60_UX_UI_접근성`: T1 건설 완료 추적·짧은 역할 라벨·T2 같은 기준 비교.
- `99_변경이력`: exact HEAD·PR·read-back·CI 상태.

## 6. 쓰기 규칙

1. GitHub 책임 원본과 Decision ID를 먼저 확정한다.
2. exact PR HEAD를 기록한다.
3. 과거 완료 Decision 행을 덮어쓰지 않는다.
4. 쓰기 직후 같은 bounded range를 다시 읽는다.
5. Decision ID·HEAD·counter·approval checkpoint·감사 범위 불일치는 blocker다.
6. Draft PR 단계에는 `PROPOSED_SHEET_CHANGE`, 병합 뒤에만 `MERGED_CANON`을 사용한다.

## 7. 차단 표식

```text
OPEN_P0
OPEN_P1
MERGE_BLOCKER
READBACK_PENDING
```

fresh preflight에서 열린 차단 표식이 있으면 병합하지 않는다.

## 8. 제품 경계

```text
PRODUCT_CODE = UNCHANGED
DATA_MIGRATION = NOT_AUTHORIZED
EXACT_NUMERICS = PENDING_SIMULATION
IMAGE_GENERATION = NOT_AUTHORIZED
ANIMATION_HX = NOT_AUTHORIZED
```

## 9. 완료 이력

```text
OMW-DEC-20260805-PLANNING-STAGE-END-MERCHANT-V1
6_OF_10
OMW-DEC-20260805-PLANNING-TACTICAL-SKILLS-AND-MANA-V1
5_OF_10
OMW-DEC-20260805-PLANNING-TROOP-ROLES-SYNERGIES-AND-COUNTERS-V1
4_OF_10
OMW-DEC-20260805-PLANNING-SIX-BUILDING-T2-T3-BRANCHES-AND-COUNTERS-V1
3_OF_10
LEGACY_C1_C2_C3_PROVEN
```
