# [현행] 오멘워드 로드맵

```yaml
updated_at: 2026-08-20
planning_contract: PROJECT_TOTAL_PLANNING_IMPLEMENTATION_AND_DELIVERY_INSTRUCTION_v4.7
planning_status: REOPENED_REVIEW_IN_PROGRESS
current_next_gate: TOKEN_COMPONENT_SPEC
implementation_authorized: false
visual_style: ANIME_PIXEL_ART_UNITS_PLUS_CLEAN_PIXEL_BATTLEFIELD
visual_generation: USER_REQUEST_ONLY
```

## Current milestone

```text
PROJECT_STATE_RECOVERED
→ DECISION_1_TO_6_CONFIRMED
→ 6_FULL_ADVERSARIAL_LOOPS_AND_CANON_RECONCILIATION
→ WORLD_CONFLICT_AND_CORE_STORY_CONFIRMED
→ 20_STAGE_CONTENT_AND_BOSS_STRUCTURE_CONFIRMED
→ NORMALIZED_BALANCE_BUDGET_CONFIRMED
→ TEXT_UX_AND_STATE_TRANSITION_CONFIRMED
→ VISUAL_STYLE_AND_COMPONENT_DIRECTION_CONFIRMED
→ BATTLEFIELD_SCALE_AND_COMBAT_READABILITY_CONFIRMED
→ 3X3_ROULETTE_COMPONENT_SPEC_CONFIRMED
→ TOKEN_COMPONENT_SPEC = CURRENT_NEXT
```

## Current planning order

### P0 — Token component spec — CURRENT NEXT

Define the common 3×3 tile and actual unit-art crop rules so each unit type is readable at small size.

```text
common token tile frame
T1/T2 unit-art reuse
role silhouette priority
face / weapon / body crop hierarchy
faction/Tier/rarity overlay priority
Gold Token using actual game gold art
X token readability
small-size validation
```

### P0 — Lower Control Deck — NEXT

Fit the approved 3×3 board, 12 direct arrows, move resources, Spin/Confirm and focus tabs inside the `25~32%` lower-deck envelope without duplicating top-HUD resources.

### P0 — Roulette DDD feedback — NEXT

Design the anticipation/payoff chain:

```text
probability setup
→ spin buildup
→ row/column manipulation
→ center-line lock
→ completed-line reveal
→ result snap
→ storage/commit transfer
→ battlefield reinforcement link
```

Casino/jackpot/paid-spin fantasy remains forbidden.

### Visual North Star — AFTER COMPONENT CONTRACTS

Create exactly one rebuilt North Star only after Token + Lower Deck + DDD contracts are coherent.

Required visual contract:

```text
ANIME_PIXEL_ART_UNITS
CLEAN_PIXEL_BATTLEFIELD
FULL_THREE_LANES
WIDE_COMBAT_ROADS
BATTLEFIELD_PRIMARY / LOWER_DECK_SECONDARY
3×3 ROULETTE
PROMINENT ROW/COLUMN ARROWS
ROLE-READABLE UNIT TOKENS
GOLD TOKEN
NO DUPLICATE LOWER RESOURCES
```

### Final planning review

After component contracts and rebuilt North Star result approval:

```text
minimum 5 full adversarial loops / until clean
Decision 1~13 + visual/component regression review
Notion/GitHub drift check
implementation Definition of Ready
explicit user implementation authority
```

Only then open implementation handoff.

## Current 3×3 Roulette authority

Owners:

- `docs/design/APPROVED_OMENWARD_3X3_ROULETTE_COMPONENT_SPEC_2026-08-20.md`
- `docs/analysis/ui/current_3x3_roulette_component.v1.json`

```text
3×3 exposure window
12 direct arrows
hover/focus preview without spend
execute = move resource spend + immediate committed move
undo/reset after move = forbidden
center horizontal row = primary judging line
Lucky free move first / stored tickets cap 3
```

## Current Battlefield authority

Owners:

- `docs/design/APPROVED_OMENWARD_BATTLEFIELD_SCALE_AND_COMBAT_READABILITY_2026-08-20.md`
- `docs/analysis/visual/current_battlefield_scale_readability.v1.json`

Planning envelope:

```text
reference = 960×540
battlefield height = 68~75%
lower deck = 25~32%
common unit = 30~36 px visual height
common footprint = 18~22 px
usable road = 60~72 px / 2.75~3.25× footprint
lateral ranks = 2~3
lane center spacing = 105~125 px
clash node = 78~96 px
default camera = full three lanes
```

These are validation ranges, not final runtime geometry.

## Current Visual authority

Owner:
`docs/design/APPROVED_OMENWARD_VISUAL_STYLE_AND_COMPONENT_CONTRACT_2026-08-20.md`

```text
CHARACTER_AND_UNIT_STYLE = ANIME_PIXEL_ART
BATTLEFIELD_AND_BACKGROUND_STYLE = CLEAN_PIXEL_ART
PRIMARY_VISUAL_MASS = BATTLEFIELD
SECONDARY_VISUAL_MASS = LOWER_CONTROL_DECK
ROULETTE_EXPOSURE = 3×3
ROW_COLUMN_ARROWS = PROMINENT
GOLD_TOKEN = SUPPORTED
DUPLICATE_RESOURCE_DISPLAY_IN_LOWER_DECK = FORBIDDEN
```

## Current GitHub work-item routing

```text
PR175 = CLOSED_UNMERGED_HISTORICAL
PR177 = CLOSED_UNMERGED_REFERENCE_HISTORY
ISSUE176 = OPEN_HISTORICAL_FOLLOWUP_REQUIRES_RECONCILIATION
PR197 = OPEN_DRAFT_OTHER_WORKSTREAM_READ_ONLY
```

PR197 is protected from this planning workstream.

## Current runtime/evidence gate

```text
CURRENT_GODOT_RUNTIME = NOT_RUN
CURRENT_WINDOWS_RUNTIME = NOT_RUN
CURRENT_HUMAN_USABILITY_EVIDENCE = NOT_RUN
CURRENT_PLAYER_EXPERIENCE_EVIDENCE = NOT_RUN
FINAL_PARAMETER_VECTOR = NOT_SELECTED
FINAL_PRODUCT_NUMERICS = NOT_APPROVED
```

## Platform / release deferred

```text
PC / Steam = PRIMARY_PLANNING_AND_VALIDATION_TARGET
Android / Google Play = COMMITTED_RELEASE_TARGET_EXECUTION_DEFERRED_RELEASE_NEAR
SHARED_SAVE_SCHEMA = NOT_STARTED
EXPORT_PRESETS = ABSENT
```
