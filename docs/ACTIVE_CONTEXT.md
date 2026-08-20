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
current_text_ux_decision: OMW-PLAN-20260820-TEXT-UX-STATE-01
current_visual_style_decision: OMW-PLAN-20260820-VISUAL-STYLE-COMPONENTS-01
current_battlefield_scale_decision: OMW-PLAN-20260820-BATTLEFIELD-SCALE-READABILITY-01
current_roulette_component_decision: OMW-PLAN-20260820-ROULETTE-3X3-COMPONENT-01
current_token_component_decision: OMW-PLAN-20260820-TOKEN-COMPONENT-01
current_lower_control_deck_decision: OMW-PLAN-20260820-LOWER-CONTROL-DECK-01
current_lower_control_deck_owner: docs/design/APPROVED_OMENWARD_LOWER_CONTROL_DECK_SPEC_2026-08-20.md
current_lower_control_deck_machine_owner: docs/analysis/ui/current_lower_control_deck.v1.json
current_next_gate: ROULETTE_DDD_FEEDBACK_SPEC
implementation_authorized: false
current_chat_runtime_status: NOT_RUN
human_player_evidence: NOT_RUN
visual_generation: USER_REQUEST_ONLY
```

## Current planning state

```text
CURRENT_APPROVED_REPLAN_DECISIONS = 15
WORLD_ROLE = CONFIRMED
MAPRUN_WORLD_MEANING = CONFIRMED
PRESSURE_LANGUAGE = CONFIRMED
MOBILIZATION_REGISTRY_WORLD_MEANING = CONFIRMED
FIRST5_FTUE_MASTERY_LADDER = CONFIRMED
RUN_COMMAND_SCREEN_FOCUS_MODES = CONFIRMED
WORLD_CONFLICT_AND_CORE_STORY = CONFIRMED
20_STAGE_CONTENT_AND_BOSS_STRUCTURE = CONFIRMED
BALANCE_BUDGET = CONFIRMED
TEXT_UX_AND_STATE_TRANSITION = CONFIRMED
VISUAL_STYLE_AND_COMPONENT_DIRECTION = CONFIRMED
BATTLEFIELD_SCALE_AND_COMBAT_READABILITY = CONFIRMED
ROULETTE_3X3_COMPONENT = CONFIRMED
TOKEN_COMPONENT = CONFIRMED
LOWER_CONTROL_DECK = CONFIRMED
DECISION_1_TO_6_ADVERSARIAL_REVIEW = CLEAN_REVIEW_EXIT
CURRENT_NEXT = ROULETTE_DDD_FEEDBACK_SPEC
IMPLEMENTATION_START = NOT_AUTHORIZED
```

## Current product promise

```text
징조 관측
→ 건설 / 동원 인장 / 미래 병력 분포 설계
→ 3×3 룰렛/징조륜 조작과 병력 획득
→ 세 전선 중 하나에 비가역 커밋
→ 자동전투 + 결정적 순간의 수동 전술
→ 인과 복기
→ 다음 설계
```

Player role: `징조수호관(Omen Warden)`
Run shell: `PREPARE → COMMIT → BATTLE → REVIEW`

## Current Visual / component contract

```text
CHARACTERS_UNITS = ANIME_PIXEL_ART
BATTLEFIELD_BACKGROUND = CLEAN_PIXEL_ART
UI = DARK_NAVY_CHARCOAL + RESTRAINED_GOLD
PRIMARY_VISUAL_MASS = BATTLEFIELD
SECONDARY_VISUAL_MASS = LOWER_CONTROL_DECK
GOLD_TOKEN = SUPPORTED
DUPLICATE_RESOURCE_DISPLAY_IN_LOWER_DECK = FORBIDDEN
```

Battlefield planning envelope:

```text
REFERENCE_RESOLUTION = 960×540
BATTLEFIELD_HEIGHT = 68~75%
LOWER_DECK_HEIGHT = 25~32%
REFERENCE_BASELINE = 72/28
COMMON_UNIT_VISUAL_HEIGHT = 30~36 px exploration
COMMON_FOOTPRINT_WIDTH = 18~22 px exploration
ROAD_USABLE_WIDTH = 60~72 px exploration
ROAD_TO_FOOTPRINT = 2.75~3.25×
LATERAL_RANK_TARGET = 2~3
LOCAL_ENGAGEMENT_READABILITY = 8~12 combatants per immediate cluster, not a gameplay cap
LANE_CENTER_SPACING = 105~125 px exploration
CLASH_NODE = 78~96 px exploration
DEFAULT_CAMERA = FULL_THREE_LANES_VISIBLE
AUTO_ZOOM_HIDING_OTHER_LANES = FORBIDDEN
```

3×3 roulette component:

```text
ROULETTE_EXPOSURE = 3×3
ROULETTE_FOCUS_LOWER_DECK = 28~32%
TOKEN_TILE = 32~34 px exploration
BOARD_PLUS_ARROWS_HEIGHT = 146~154 px exploration
ARROW_CONTROLS = 12 direct row/column controls
HOVER_OR_FOCUS = preview without spend
EXECUTE = spend + immediate committed move
UNDO_AFTER_MOVE = FORBIDDEN
PRIMARY_JUDGING_LINE = CENTER_HORIZONTAL_ROW
```

Token component:

```text
SOURCE_ART = ACTUAL_GAME_UNIT_ART
INNER_SAFE_ART = 26~29 px exploration
ROLE_ANCHOR_FIRST = TRUE
T1_T2_TOKEN_ART = ALLOWED
T3_TOKEN_ART = FORBIDDEN
TOKEN_RARITY_FRAME = FORBIDDEN
GOLD_TOKEN_USES_GAME_GOLD_ART = TRUE
X_TOKEN = CLEAR_EMPTY_NON_REWARD
```

Lower Control Deck:

```text
ONE_ACTIVE_WORK_SURFACE_AT_A_TIME = TRUE
GLOBAL_LOWER_DECK = 25~32% exploration
ROULETTE_FOCUS = 28~32%
OTHER_FOCUS = 25~28%
TOP_HUD_OWNS_RESOURCE_TOTALS = TRUE
LOCAL_ACTION_COST_IN_LOWER_DECK = ALLOWED
TABS = ROULETTE / STORAGE / BUILD / TACTICAL
BELLU = CONTEXT_GUIDE_NOT_FIFTH_MANAGEMENT_MENU
```

These are North Star / Vertical Slice planning ranges, not final runtime numerics.

## Current Text UX contract

```text
PREPARE = 다가오는 문제를 보고 무엇을 바꿀 것인가?
COMMIT = 얻은 병력을 어느 전선에 확정할 것인가?
BATTLE = 지금 직접 개입해야 하는가?
REVIEW = 왜 이런 결과가 나왔는가?
```

COMMIT uses pending staged assignment followed by one atomic irreversible confirm. REVIEW explains facts/causes and does not prescribe one correct build.

## Current world / content spine

```text
VEIL = hostile boundary phenomenon, not one enemy race
ONE_MAPRUN = ONE_WARD_CITADEL + ONE_20_STAGE_OMEN_CYCLE
RUN_HISTORY_RESET = FALSE

Stage 1~5   = PRESSURE LITERACY
Stage 6~10  = COMBINATION
Stage 11~15 = OPPORTUNITY COST
Stage 16~20 = SYNTHESIS

Boss 5  = PRIORITY
Boss 10 = ROUTE
Boss 15 = STANCE
Boss 20 = SEQUENTIAL_SYNTHESIS

DANGER_STAGE_TYPE = REMOVED
ELITE_ESCALATION = EVERY_STAGE_FINAL_WAVE
```

## Current normalized Balance envelope

```text
SE = current 20 Gold Spin anchor
ME = current 50 Gold first-T2-class anchor = 2.5 SE
TU = simulation-only relative threat unit
THREAT_VECTOR = Raw TU + Active Lanes + Signature Count + Route Complexity + Wave Overlap + Elite/Boss Complexity
```

Economy drift remains open and final product numerics remain unapproved.

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

## Current work order

```text
1. COMPLETE — battlefield scale / road width / unit readability
2. COMPLETE — compact direct-arrow 3×3 Roulette
3. COMPLETE — Token component
4. COMPLETE — Focus-adaptive Lower Control Deck
5. CURRENT — Roulette DDD feedback / anticipation-payoff spec
6. NEXT — one rebuilt North Star image after component contracts
7. NEXT — component sheet / reusable asset breakup
8. NEXT — final full planning adversarial review
9. NEXT — GitHub/Notion final sync
10. NEXT — implementation handoff only after explicit user authority
```

## Resume order

1. fresh OMENWARD main.
2. `docs/CURRENT_CONFIRMED_DECISIONS.md`.
3. this `docs/ACTIVE_CONTEXT.md`.
4. visual style + battlefield + 3×3 + Token + Lower Deck owners/machine envelopes.
5. Text UX + Balance + Content/Story owner docs.
6. Project Notion Home + `02/03/08/09/10/11/12/13/14/15/16/17` relevant pages.
7. open/draft PR inventory; PR197 read-only.
8. actual runtime only when execution is explicitly resumed.
