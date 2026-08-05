# First 10–15 Minutes Flow — Checkpoint 5 Specification

```yaml
updated_at: 2026-08-06
decision_id: OMW-DEC-20260805-PLANNING-FIRST-10-15-MINUTES-FLOW-V1
status: PARTIAL_APPROVAL_5_OF_10
planning_count: 7_OF_10_IN_PROGRESS
source: USER_APPROVED_RECOMMENDATION
```

## Problem

Stage 1 must teach construction through real action and real gold without turning foundation setup into either a fake tutorial economy or a recoverability trap. An unrestricted real wallet can be spent below the remaining required T1 cost, and unrestricted placement can make the first session unwinnable before the player understands the consequences.

## Approved foundation contract

```text
STAGE_1_T1_BUILDINGS = ONE_EACH_ALL_SIX
STAGE_1_T1_BUILD_BUDGET = GUARANTEED_SUFFICIENT_FOR_REQUIRED_SET
STAGE_1_BUILD_CURRENCY = REAL_GOLD
T1_BUILDING_EXPLANATION = BRIEF_ROLE_LABELS
T1_BUILDING_PLACEMENT = PLAYER_EXECUTED
T1_BUILDING_BRANCH_CHOICE = NONE
T1_PLACEMENT_POLICY = CATEGORY_COMPATIBLE_SAFE_NODES
T1_BUILD_ORDER = PLAYER_SELECTED
FOUNDATION_SETUP_RELOCATION = FREE_BEFORE_CONFIRMATION
FOUNDATION_SETUP_CONFIRMATION = REQUIRED
POST_CONFIRMATION_PLACEMENT_RULES = STANDARD_RUN_RULES
FREE_RELOCATION_AFTER_CONFIRMATION = FORBIDDEN
STAGE_1_REQUIRED_COST_RESERVE = SUM_OF_UNBUILT_REQUIRED_T1_COSTS
STAGE_1_NON_T1_SPENDING_BEFORE_REQUIRED_SET_COMPLETE = BLOCKED
STAGE_1_LEFTOVER_GOLD_POLICY = NORMAL_WALLET_AFTER_REQUIRED_SET_COMPLETE
FOUNDATION_GRANT_SURPLUS = FORBIDDEN
T1_INVALID_PLACEMENT_TRANSACTION = ATOMIC_ROLLBACK_FULL_REFUND
FIRST_ROULETTE_UNLOCK = AFTER_ALL_SIX_T1_AND_SETUP_CONFIRMATION
EXACT_T1_COSTS = PENDING_SIMULATION
T1_EXACT_NODE_COORDINATES = PENDING_LEVEL_LAYOUT
```

## Placement policy

- Show only category-compatible nodes that preserve a valid first-combat state.
- The player chooses the build order.
- Exact node coordinates and node counts remain a level-layout decision.
- Before confirmation, already placed T1 buildings may move or swap only among allowed safe nodes.
- Confirmation ends the temporary recovery window; normal Run placement rules apply afterward.

## Gold policy

```text
required_cost_reserve = sum(real cost of each unbuilt required T1)
```

- Foundation gold enters the real wallet.
- A transaction is rejected when it would reduce the wallet below the remaining required-cost reserve.
- Non-T1 spending is blocked until all six required T1 buildings are complete.
- Foundation funding covers the actual required set but must not create intentional surplus.
- After the required set is complete, any legitimate remainder becomes normal wallet gold.

## Atomic transaction policy

Building creation, node occupation, wallet deduction, required-set completion, and reserve recalculation form one atomic transaction. Invalid placement, duplicate occupation, cost mismatch, or persistence failure rolls back the entire transaction and restores the full amount.

## Exposure order

```text
Stage 1: forecast → real-gold grant → build all six T1 → foundation confirmation → roulette → troop result → irreversible deployment → real combat → causal review → first merchant
Stage 2: real-gold T2 grant → compare two valid T2 candidates → construct one T2 → roulette control → multi-front judgment
Stage 3: mana tower research → first T1 tactic → manual use
Stage 4: first Danger integration
Stage 5: first Boss mastery check
```

## Explicit non-decisions

```text
FIRST_T2_UPGRADE_CANDIDATE_IDENTITIES = PENDING_GRILLME
STAGE_2_LEFTOVER_GOLD_POLICY = PENDING_GRILLME
MINIMUM_VALID_PATHS = PENDING_GRILLME
BELU_INTERVENTION_LEVEL = PENDING_GRILLME
DANGER_EXACT_PRESSURE = PENDING_GRILLME
BOSS_EXACT_PATTERN = PENDING_GRILLME
FAILURE_RETRY_SKIP_RULES = PENDING_GRILLME
EXACT_TIMINGS = PENDING_SIMULATION_AND_HUMAN_QA
```

## Platform and product boundaries

The branch preserves `OMW-DEC-20260805-PLATFORM-PC-ANDROID-V1`, `COMMON_PLATFORM_GATE`, `PC_RELEASE_GATE`, and `MOBILE_RELEASE_GATE`.

No product code, Scene, Resource, game data, exact numeric cost, level coordinate, art, animation, or HX production is authorized by this specification.
