# First 10–15 Minutes Flow — Checkpoint 1 Specification

```yaml
updated_at: 2026-08-05
decision_id: OMW-DEC-20260805-PLANNING-FIRST-10-15-MINUTES-FLOW-V1
status: PARTIAL_APPROVAL_2_OF_10
planning_count: 7_OF_10_IN_PROGRESS
source: USER_APPROVED_RECOMMENDATION_A
```

## Problem

OMENWARD has separately defined construction, roulette control, deployment, mana tower, tactical research, and merchant systems. A detached tutorial could drift from real MapRun rules, while opening every system at Stage 1 would create cognitive overload and obscure the core causal loop. The onboarding therefore needs both an approved form and an approved exposure order.

## Approved design

The first session is the real MapRun. Systems are disclosed progressively inside play when they become relevant to the current objective.

```text
ONBOARDING_FORMAT = IN_RUN_PROGRESSIVE_DISCLOSURE
FIRST_SESSION = REAL_MAPRUN
SYSTEM_EXPOSURE_ORDER = APPROVED_CORE_CAUSAL_CHAIN_FIRST
SEPARATE_TUTORIAL = FORBIDDEN
FULL_SYSTEM_DUMP_AT_STAGE_1 = FORBIDDEN
RULE_PARITY_WITH_MAIN_RUN = REQUIRED
SCRIPTED_VICTORY = FORBIDDEN
```

## Approved exposure order

```text
Stage 1: forecast → first build preview/choice → roulette → troop result → irreversible deployment → real combat → causal review → first merchant
Stage 2: move tickets → row/column preview → multi-front comparison → irreversible deployment
Stage 3: mana tower → research relation → first T1 tactic → manual target/lane/timing → result review
Stage 4: first Danger integration using learned systems
Stage 5: first Boss mastery check without adding a new core system
```

The first merchant appears in Stage 1 maintenance and teaches only optional purchase and gold opportunity cost. It does not teach the full four-slot strategy at once.

## Required player experience

The player must learn OMENWARD through real decisions:

```text
read pressure
→ spend a limited resource
→ shape construction or roulette outcome
→ commit troops to a lane
→ observe the real result
→ understand the cause
→ revise the next decision
```

Belu may explain objectives, available actions, and causal feedback. Belu may not replace player choice.

## Explicit non-decisions

This checkpoint does not decide the exact first building candidates, minimum valid paths, first ruler-choice content, Belu intervention intensity, exact Danger pressure, exact Boss pattern, failure/retry/skip rules, exact timing, or human-QA thresholds. Those remain `PENDING_GRILLME` or `PENDING_SIMULATION_AND_HUMAN_QA`.

## Boundaries

No product code, Scene, Resource, game data, art, animation, or HX production is authorized by this specification.
