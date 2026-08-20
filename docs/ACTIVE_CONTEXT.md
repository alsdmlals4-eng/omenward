# [현행] Active Context

```yaml
updated_at: 2026-08-20
current_branch: main
current_main: RESOLVE_FROM_REPOSITORY_DEFAULT_BRANCH
planning_contract: PROJECT_TOTAL_PLANNING_IMPLEMENTATION_AND_DELIVERY_INSTRUCTION_v4.7
planning_status: REOPENED_REVIEW_IN_PROGRESS
current_decision_index: docs/CURRENT_CONFIRMED_DECISIONS.md
current_gdd: docs/OMENWARD_GDD_CURRENT_CANON.md
current_review: CLEAN_REVIEW_EXIT_FOR_DECISIONS_1_TO_6_AND_ROUTING
current_review_full_loop_count: 6
current_world_story_decision: OMW-PLAN-20260820-WORLD-CONFLICT-STORY-01
current_content_decision: OMW-PLAN-20260820-CONTENT-BOSS-ARC-01
current_content_owner: docs/design/APPROVED_OMENWARD_20_STAGE_CONTENT_AND_BOSS_ARC_2026-08-20.md
current_next_gate: BALANCE_BUDGET
implementation_authorized: false
current_chat_runtime_status: NOT_RUN
human_player_evidence: NOT_RUN
visual_generation: PAUSED_PENDING_USER_REFERENCE_FILES
```

## Current planning state

```text
CURRENT_APPROVED_REPLAN_DECISIONS = 8
WORLD_ROLE = CONFIRMED
MAPRUN_WORLD_MEANING = CONFIRMED
PRESSURE_LANGUAGE = CONFIRMED
MOBILIZATION_REGISTRY_WORLD_MEANING = CONFIRMED
FIRST5_FTUE_MASTERY_LADDER = CONFIRMED
RUN_COMMAND_SCREEN_FOCUS_MODES = CONFIRMED
WORLD_CONFLICT_AND_CORE_STORY = CONFIRMED
20_STAGE_CONTENT_AND_BOSS_STRUCTURE = CONFIRMED
DECISION_1_TO_6_ADVERSARIAL_REVIEW = CLEAN_REVIEW_EXIT
VISUAL_GENERATION = PAUSED_PENDING_USER_REFERENCE_FILES
CURRENT_NEXT = BALANCE_BUDGET
IMPLEMENTATION_START = NOT_AUTHORIZED
```

## Current product promise

```text
징조 관측
→ 건설 / 동원 인장 / 미래 병력 분포 설계
→ 세 징조륜에서 병력 획득
→ 세 전선 중 하나에 비가역 커밋
→ 자동전투 + 결정적 순간의 수동 전술
→ 인과 복기
→ 다음 설계
```

Player role: `징조수호관(Omen Warden)`

Run meaning: `one Ward Citadel + one 20 Stage Omen Cycle`

Run shell: `PREPARE → COMMIT → BATTLE → REVIEW`

World conflict:

```text
VEIL = 현실과 겹쳐지는 적대적 경계현상 / 단일 종족 아님
OMEN = 실제 공세 전에 나타나는 Pre-Echo
STAGE_20 = 해당 수호성의 수렴핵/정박체 파괴 결산
RUN_HISTORY_RESET = FALSE
```

## Current 20 Stage spine

```text
Stage 1~5   = PRESSURE LITERACY
Stage 6~10  = COMBINATION
Stage 11~15 = OPPORTUNITY COST
Stage 16~20 = SYNTHESIS
```

Boss function:

```text
Stage 5  = PRIORITY
Stage 10 = ROUTE
Stage 15 = STANCE
Stage 20 = SEQUENTIAL_SYNTHESIS
```

Global cadence:

```text
BASELINE_WAVE_BEATS = 3
ELITE_ESCALATION = EVERY_STAGE_FINAL_WAVE
BOSS_STAGES = 5 / 10 / 15 / 20
DANGER_STAGE_TYPE = REMOVED
```

Former Danger ideas are only normal-stage authored variations:

```text
Stage 4  = REVEALED_BYPASS_ROUTE
Stage 9  = REVEALED_WAVE_OVERLAP_TIMETABLE
Stage 14 = REVEALED_PRIMARY_LANE_ROTATION
Stage 19 = REVEALED_ROUTE_CONVERGENCE
```

Stage 20 Final Boss:

```text
Pattern I   = MASS + FLYING
Pattern II  = ARMORED + SIEGE
Pattern III = INFILTRATION + prior residual pressure
NEXT_PATTERN_FORECAST = REQUIRED
ALL_PRESSURES_SIMULTANEOUS_SPAM = FORBIDDEN
```

## Bounded variation

Vertical Slice / first validation uses a stable authored spine.

Long-term allowed variation:

```text
primary lane
secondary lane
allowed secondary Signature
Route variant
Elite identity
Escort package
limited Wave overlap timing
faction/cosmetic presentation
```

Not allowed:

```text
random replacement of Stage learning role
moving Boss landmarks
removing final-wave Elite cadence
unforecast lethal Route/Pressure swap
a seed that removes all valid responses
```

## Current Balance gap

Balance Budget must define **targets and ranges**, not final production numerics.

```text
STAGE_THREAT_BUDGET
WAVE_THREAT_BUDGET
PRESSURE_COST
ELITE_BUDGET
BOSS_BUDGET
GOLD_INCOME_CURVE
MANA_INCOME_CURVE
TROOP_LIMIT_CURVE
BUILD_AND_UPGRADE_SPEND_TARGETS
ROULETTE_SPEND_TARGETS
MERCHANT_SPEND_TARGETS
```

Final values remain evidence-dependent.

## Runtime / work-item boundary

```text
PR175 = CLOSED_UNMERGED_HISTORICAL
PR177 = CLOSED_UNMERGED_REFERENCE_HISTORY
ISSUE176 = OPEN_HISTORICAL_FOLLOWUP_REQUIRES_RECONCILIATION
PR197 = OPEN_DRAFT_OTHER_WORKSTREAM_READ_ONLY
CURRENT_GODOT_RUNTIME = NOT_RUN
CURRENT_WINDOWS_RUNTIME = NOT_RUN
CURRENT_HUMAN_USABILITY_EVIDENCE = NOT_RUN
CURRENT_PLAYER_EXPERIENCE_EVIDENCE = NOT_RUN
FINAL_PARAMETER_VECTOR = NOT_SELECTED
FINAL_PRODUCT_NUMERICS = NOT_APPROVED
```

PR197은 이 채팅에서 수정·retarget·merge하지 않는다.

## Visual boundary

```text
STYLE = 클린 전술 픽셀 + 미니어처 치비 픽셀 + 제한된 고급 조명
VISUAL_NORTH_STAR_DIRECTION_A = APPROVED_DIRECTION_ONLY
FIRST_GENERATED_CANDIDATE = REJECTED_NOT_CANON
VISUAL_GENERATION = PAUSED_PENDING_USER_REFERENCE_FILES
```

사용자 보유 시안/레퍼런스 파일 수신 전에는 이미지 생성·수정을 재개하지 않는다.

## Current non-image planning order

```text
1. Balance Budget
2. PREPARE / COMMIT / BATTLE / REVIEW text UX + state-transition spec
3. resume visual work only after user reference files arrive
4. final planning review
5. implementation handoff only after user authority
```

## Protected mechanics

```text
ROULETTE_IDENTITY = PLAYER_CONSTRUCTED_PROBABILITY_ENGINE
GAMBLING_FANTASY_POSITIONING = FORBIDDEN
PAID_SPIN = FORBIDDEN
FORECASTED_PRESSURE_MULTIPLE_RESPONSE_AXES_REQUIRED = TRUE
RNG_CAN_REMOVE_ALL_VALID_RESPONSES = FORBIDDEN
AUTO_PRODUCTION_AND_TOKEN_SOURCE = SEPARATE_ACQUISITION_PATHS
TOKEN_INSTANCES_PER_REEL_PER_ACTIVE_SOURCE = 1
TOTAL_TOKEN_INSTANCES_PER_ACTIVE_SOURCE = 3
THREE_REELS_TO_THREE_LANES_FIXED_MAPPING = FORBIDDEN
IRREVERSIBLE_LANE_COMMITMENT = REQUIRED
BOSS_STAGES = 5 / 10 / 15 / 20
ELITE_ESCALATION = EVERY_STAGE_FINAL_WAVE
DANGER_STAGE_TYPE = REMOVED
PRESCRIPTIVE_NEXT_BUILD_COMMAND = FORBIDDEN
VEIL_IS_SINGLE_ENEMY_RACE = FALSE
TIME_LOOP_DEFAULT = FALSE
```

## Resume order

1. fresh OMENWARD main.
2. `docs/CURRENT_CONFIRMED_DECISIONS.md`.
3. this `docs/ACTIVE_CONTEXT.md`.
4. `docs/design/APPROVED_OMENWARD_20_STAGE_CONTENT_AND_BOSS_ARC_2026-08-20.md`.
5. `docs/design/APPROVED_OMENWARD_VEIL_CONVERGENCE_FRONT_AND_CORE_STORY_2026-08-20.md`.
6. current GDD/Project Core.
7. Project Notion Home + `09 · 세계관 · 핵심 스토리` + `10 · 20 Stage · Boss 구조` + relevant `08/03/02`.
8. open/draft PR inventory; PR197 read-only unless its own workstream resumes.
9. fresh runtime only when execution is explicitly resumed.
