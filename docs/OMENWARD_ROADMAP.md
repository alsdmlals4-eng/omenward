# [현행] 오멘워드 로드맵

```yaml
updated_at: 2026-08-20
planning_contract: PROJECT_TOTAL_PLANNING_IMPLEMENTATION_AND_DELIVERY_INSTRUCTION_v4.7
planning_status: REOPENED_REVIEW_IN_PROGRESS
current_next_gate: ROULETTE_DDD_FEEDBACK_SPEC
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
→ TOKEN_COMPONENT_SPEC_CONFIRMED
→ LOWER_CONTROL_DECK_SPEC_CONFIRMED
→ ROULETTE_DDD_FEEDBACK_SPEC = CURRENT_NEXT
```

## Current planning order

### P0 — Roulette DDD feedback — CURRENT NEXT

Define the anticipation/payoff chain so the strongest reward feeling comes from **the player's built probability + direct row/column manipulation producing a useful mobilization result**, not from casino fantasy.

```text
probability setup
→ spin buildup
→ natural stop
→ near-hit / readable state
→ row/column manipulation snap
→ center judging-line lock
→ completed-line cascade
→ result reveal
→ storage/commit transfer
→ short battlefield reinforcement link
```

Constraints:

```text
battlefield remains visible
casino/jackpot/paid-spin language forbidden
feedback must be short and interruptible
result grade follows line count, not hidden rarity draw
player manipulation must receive stronger feedback than passive random sparkle
```

### Visual North Star — AFTER DDD CONTRACT

Create exactly one rebuilt North Star only when the user explicitly requests image generation after the DDD contract is coherent.

Required visual contract:

```text
ANIME_PIXEL_ART_UNITS
CLEAN_PIXEL_BATTLEFIELD
FULL_THREE_LANES
WIDE_COMBAT_ROADS
BATTLEFIELD_PRIMARY / LOWER_DECK_SECONDARY
3×3 ROULETTE
PROMINENT ROW/COLUMN ARROWS
ACTUAL-UNIT-ART ROLE-ANCHOR TOKENS
GOLD TOKEN
FOCUS-ADAPTIVE LOWER DECK
NO DUPLICATE LOWER RESOURCES
```

### Component Sheet — AFTER NORTH STAR

Break the approved screen into reusable assets/components:

```text
battlefield road / clash node / lane markers
unit token tile / Gold / X
row/column arrows
focus tabs
CTA states
forecast badges
line-lock / result VFX layers
Bellu context panel if retained
```

### Final planning review

After component contracts and rebuilt North Star result approval:

```text
minimum 5 full adversarial loops / until clean
Decision 1~15 + visual/component regression review
Notion/GitHub drift check
implementation Definition of Ready
explicit user implementation authority
```

Only then open implementation handoff.

## Current Lower Control Deck authority

Owners:
- `docs/design/APPROVED_OMENWARD_LOWER_CONTROL_DECK_SPEC_2026-08-20.md`
- `docs/analysis/ui/current_lower_control_deck.v1.json`

```text
ONE_ACTIVE_WORK_SURFACE_AT_A_TIME
TOP HUD OWNS RESOURCE TOTALS
lower local action cost allowed
ROULETTE / STORAGE / BUILD / TACTICAL tabs
Bellu = contextual guide, not fifth management menu
Roulette focus = left moves / center 3×3 / right action-result
```

## Current Token authority

Owners:
- `docs/design/APPROVED_OMENWARD_TOKEN_COMPONENT_SPEC_2026-08-20.md`
- `docs/analysis/ui/current_token_component.v1.json`

```text
actual game Anime Pixel unit art reused
Role-Anchor Crop
T1/T2 tokens only
T3 token art forbidden
reward rarity != token rarity
Gold uses actual game Gold art
X = clear empty non-reward
```

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
