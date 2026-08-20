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
current_balance_decision: OMW-PLAN-20260820-BALANCE-BUDGET-01
current_balance_owner: docs/design/APPROVED_OMENWARD_NORMALIZED_BALANCE_BUDGET_2026-08-20.md
current_balance_machine_owner: docs/analysis/balance/current_normalized_balance_budget.v1.json
current_next_gate: TEXT_UX_AND_STATE_TRANSITION_SPEC
implementation_authorized: false
current_chat_runtime_status: NOT_RUN
human_player_evidence: NOT_RUN
visual_generation: PAUSED_PENDING_USER_REFERENCE_FILES
```

## Current planning state

```text
CURRENT_APPROVED_REPLAN_DECISIONS = 9
WORLD_ROLE = CONFIRMED
MAPRUN_WORLD_MEANING = CONFIRMED
PRESSURE_LANGUAGE = CONFIRMED
MOBILIZATION_REGISTRY_WORLD_MEANING = CONFIRMED
FIRST5_FTUE_MASTERY_LADDER = CONFIRMED
RUN_COMMAND_SCREEN_FOCUS_MODES = CONFIRMED
WORLD_CONFLICT_AND_CORE_STORY = CONFIRMED
20_STAGE_CONTENT_AND_BOSS_STRUCTURE = CONFIRMED
BALANCE_BUDGET = CONFIRMED
DECISION_1_TO_6_ADVERSARIAL_REVIEW = CLEAN_REVIEW_EXIT
VISUAL_GENERATION = PAUSED_PENDING_USER_REFERENCE_FILES
CURRENT_NEXT = TEXT_UX_AND_STATE_TRANSITION_SPEC
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

## Current normalized Balance envelope

Calibration anchor:

```text
SE = 20 Gold current Spin anchor
ME = 50 Gold current first-T2-class anchor = 2.5 SE
TU = simulation-only relative threat unit
```

Threat is a vector rather than one power score:

```text
RAW_TU
ACTIVE_LANES
SIGNATURE_COUNT
ROUTE_COMPLEXITY
WAVE_OVERLAP
ELITE/BOSS_COMPLEXITY
```

Search envelope:

```text
Act I   = 1.00 reference
Act II  = 1.15~1.35
Act III = 1.40~1.65
Act IV  = 1.70~2.05

Wave 1 = 20~30%
Wave 2 = 25~35%
Final Wave = 40~50% including Elite
Boss raw TU = same-Act normal median × 1.25~1.45 exploration range
```

Mana / capacity target:

```text
Normal Stage T1 tactical opportunities = 1~2
Mana cap exploration = 2~3 T1-cast equivalents
Normal pre-commit troop headroom = 15~30%
Late/Boss prep occupancy = 80~95%
```

## Open Balance reconciliation

Do not treat either side as final without fresh comparison.

```text
analysis baseline:
  base income = 3 / 20s
  Vault = 3 / 20s
  foundation Gold = 250

current main observation:
  StageEconomy base = 5 / 20s
  control = 4 / 60s
  outpost = 2 / 30s
  StageDefinition default starting_gold = 160

ECONOMY_BASELINE_DRIFT = OPEN_RECONCILIATION
FINAL_PRODUCT_NUMERICS = NOT_APPROVED
```

Existing 10k robustness remains scoped evidence only:

```text
SPECIAL_TOKEN_SHARE_10_MIN = 0.296265
SPECIAL_TOKEN_SHARE_BURST_MAX = 0.333333
ROBUSTNESS_10000 = PASS_FOR_APPROVED_NONCOMBAT_GATES
FUNCTIONAL_VALUE = NOT_IDENTIFIED
FINAL_PARAMETER_VECTOR = NOT_SELECTED
```

## Current Text UX gap

Next Decision must turn the approved Run shell into explicit player-facing information and transitions.

```text
PREPARE_COPY_AND_INFORMATION_HIERARCHY
COMMIT_CONFIRMATION_AND_IRREVERSIBILITY_COPY
BATTLE_TACTICAL_STATE_AND_BLOCK_REASONS
REVIEW_CAUSAL_SUMMARY
FTUE_STAGE1_TO_5_PROMPTS
MODE_TRANSITION_RULES
ERROR_AND_DISABLED_REASON_LANGUAGE
DEBUG_VS_PLAYER_SURFACE_BOUNDARY
```

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
1. PREPARE / COMMIT / BATTLE / REVIEW text UX + state-transition spec
2. resume visual work only after user reference files arrive
3. final planning review
4. implementation handoff only after user authority
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
FINAL_NUMERICS_BEFORE_EVIDENCE = FORBIDDEN
```

## Resume order

1. fresh OMENWARD main.
2. `docs/CURRENT_CONFIRMED_DECISIONS.md`.
3. this `docs/ACTIVE_CONTEXT.md`.
4. `docs/design/APPROVED_OMENWARD_NORMALIZED_BALANCE_BUDGET_2026-08-20.md` + machine envelope.
5. current content/story owners.
6. Project Notion Home + `09` + `10` + `11 · Balance Budget` + relevant `08/03/02`.
7. open/draft PR inventory; PR197 read-only unless its own workstream resumes.
8. fresh runtime only when execution is explicitly resumed.
