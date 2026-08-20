# [현행] 오멘워드 로드맵

```yaml
updated_at: 2026-08-20
planning_contract: PROJECT_TOTAL_PLANNING_IMPLEMENTATION_AND_DELIVERY_INSTRUCTION_v4.7
planning_status: REOPENED_REVIEW_IN_PROGRESS
current_next_gate: TEXT_UX_AND_STATE_TRANSITION_SPEC
implementation_authorized: false
visual_generation: PAUSED_PENDING_USER_REFERENCE_FILES
```

## Current milestone

```text
PROJECT_STATE_RECOVERED
→ DECISION_1_TO_6_CONFIRMED
→ 6_FULL_ADVERSARIAL_LOOPS_AND_CANON_RECONCILIATION
→ WORLD_CONFLICT_AND_CORE_STORY_CONFIRMED
→ 20_STAGE_CONTENT_AND_BOSS_STRUCTURE_CONFIRMED
→ NORMALIZED_BALANCE_BUDGET_CONFIRMED
→ TEXT_UX_AND_STATE_TRANSITION_SPEC = CURRENT_NEXT
```

Visual work is paused independently and does not block non-image planning.

## Current planning order

### P1 — Text UX / state transitions — CURRENT NEXT

Specify player-facing information, copy, block reasons and transitions for:

```text
PREPARE
COMMIT
BATTLE
REVIEW
FTUE Stage 1~5
Forecast hierarchy
irreversible confirmation
block reasons / errors
Debug vs player surfaces
```

Goal: the player should always understand `what changed / what is required / what becomes irreversible / why an action is blocked / what caused the result` without exposing raw debug state or prescribing one correct build.

### Visual — PAUSED

```text
A_DIRECTION = Stage 2 PREPARE · Omen Wheels Focus
FIRST_GENERATED_CANDIDATE = REJECTED_NOT_CANON
VISUAL_GENERATION = PAUSED_PENDING_USER_REFERENCE_FILES
```

Resume only after the user supplies existing local mockup/reference files.

### Final planning review

After Text UX and later visual-reference reconciliation:

```text
minimum 5 full adversarial loops / until clean
Notion/GitHub sync
implementation Definition of Ready
explicit user implementation authority
```

Only then open implementation handoff.

## Current normalized Balance authority

Owner:

`docs/design/APPROVED_OMENWARD_NORMALIZED_BALANCE_BUDGET_2026-08-20.md`

Machine planning envelope:

`docs/analysis/balance/current_normalized_balance_budget.v1.json`

```text
SE = current 20 Gold Spin anchor
ME = current 50 Gold first-T2-class anchor = 2.5 SE
TU = simulation-only relative threat unit
```

Threat vector:

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
Final = 40~50%
Boss raw TU = same-Act normal median × 1.25~1.45 exploration target
```

Current economy drift is intentionally unresolved until implementation reconciliation:

```text
analysis = base 3/20s + Vault 3/20s + foundation 250
current main observed = base 5/20s + control 4/60s + outpost 2/30s + default start 160
FINAL_PRODUCT_NUMERICS = NOT_APPROVED
```

## Current world / content authority

```text
PLAYER_ROLE = Omen Warden
VEIL = hostile boundary phenomenon, not one enemy race
ONE_MAPRUN = ONE_WARD_CITADEL + ONE_20_STAGE_OMEN_CYCLE
RUN_HISTORY_RESET = FALSE
```

20 Stage learning spine:

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

Cadence:

```text
MAPRUN_STAGE_COUNT = 20
BASELINE_WAVE_BEATS = 3
DANGER_STAGE_TYPE = REMOVED
ELITE_ESCALATION = EVERY_STAGE_FINAL_WAVE
BOSS_STAGES = 5 / 10 / 15 / 20
BOSS_STAGE_FINAL_WAVE_ELITE_REQUIRED = TRUE
```

## Bounded variation roadmap

Vertical Slice uses stable authored stages for reproducible evaluation.

Long-term repeat runs may vary:

```text
lane assignment
allowed secondary Signature
Route variant
Elite identity
Escort package
limited overlap timing
faction/cosmetic presentation
```

Do not randomize the Stage learning role, Boss landmarks, forecasted lethal threat, or existence of a valid response.

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
CURRENT_RUNTIME_BLOCKER = UNVERIFIED_UNTIL_FRESH_EXECUTION
CURRENT_HUMAN_USABILITY_EVIDENCE = NOT_RUN
CURRENT_PLAYER_EXPERIENCE_EVIDENCE = NOT_RUN
FINAL_PARAMETER_VECTOR = NOT_SELECTED
FINAL_PRODUCT_NUMERICS = NOT_APPROVED
```

No historical crash diagnosis is promoted as current without fresh execution.

## Platform / release deferred

```text
PC / Steam = PRIMARY_PLANNING_AND_VALIDATION_TARGET
Android / Google Play = COMMITTED_RELEASE_TARGET_EXECUTION_DEFERRED_RELEASE_NEAR
SHARED_SAVE_SCHEMA = NOT_STARTED
EXPORT_PRESETS = ABSENT
```

## Historical Phase C roadmap

2026-08-11 Phase B/C0 → PR175 path remains historical execution lineage only and does not override the reopened 2026-08-20 planning roadmap.
