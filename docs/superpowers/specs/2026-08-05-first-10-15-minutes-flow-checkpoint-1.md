# First 10–15 Minutes Flow — Checkpoint Specification

```yaml
updated_at: 2026-08-05
decision_id: OMW-DEC-20260805-PLANNING-FIRST-10-15-MINUTES-FLOW-V1
status: PARTIAL_APPROVAL_3_OF_10
planning_count: 7_OF_10_IN_PROGRESS
source: USER_DIRECTED_T1_PRIORITY_CORRECTION
```

## Problem

OMENWARD has separately defined construction, roulette control, deployment, mana tower, tactical research, and merchant systems. A detached tutorial could drift from real MapRun rules, while opening every system at Stage 1 would create cognitive overload. The earlier assumption that Stage 1 should begin with a T1 construction choice also overemphasized a basic setup action and delayed the meaningful T2 and deployment decisions.

## Approved design

The first session is the real MapRun. Systems are disclosed progressively inside play when they become relevant to the current objective.

```text
ONBOARDING_FORMAT = IN_RUN_PROGRESSIVE_DISCLOSURE
FIRST_SESSION = REAL_MAPRUN
SYSTEM_EXPOSURE_ORDER = APPROVED_CORE_CAUSAL_CHAIN_FIRST
INITIAL_T1_BUILDINGS = PREBUILT
T1_BUILDING_EXPLANATION = BRIEF_ROLE_LABELS
T1_BUILDING_CONSTRUCTION_TUTORIAL = FORBIDDEN
LONG_T1_BUILDING_EXPLANATION = FORBIDDEN
FIRST_MEANINGFUL_RULER_CHOICE = T2_UPGRADE_AND_IRREVERSIBLE_DEPLOYMENT
T2_UPGRADE_PREVIEW = REQUIRED
SEPARATE_TUTORIAL = FORBIDDEN
FULL_SYSTEM_DUMP_AT_STAGE_1 = FORBIDDEN
RULE_PARITY_WITH_MAIN_RUN = REQUIRED
SCRIPTED_VICTORY = FORBIDDEN
```

## Approved exposure order

```text
Stage 1: forecast → prebuilt T1 quick read → T2 upgrade preview/choice → roulette → troop result → irreversible deployment → real combat → causal review → first merchant
Stage 2: move tickets → row/column preview → multi-front comparison → irreversible deployment
Stage 3: mana tower → research relation → first T1 tactic → manual target/lane/timing → result review
Stage 4: first Danger integration using learned systems
Stage 5: first Boss mastery check without adding a new core system
```

The first merchant appears in Stage 1 maintenance and teaches only optional purchase and gold opportunity cost. It does not teach the full four-slot strategy at once.

## Required player experience

```text
read pressure
→ recognize the prebuilt T1 roles quickly
→ choose a meaningful T2 development direction
→ observe the shaped roulette result
→ commit troops to a lane
→ observe the real result
→ understand the cause
→ revise the next decision
```

Belu may summarize T1 roles, objectives, available actions, and causal feedback. Belu may not replace the T2 upgrade or deployment choice.

## Explicit non-decisions

This checkpoint does not decide the exact number or placement of prebuilt T1 instances, exact first T2 candidates, minimum valid paths, Belu intervention intensity, exact Danger pressure, exact Boss pattern, failure/retry/skip rules, exact timing, or human-QA thresholds. Those remain `PENDING_GRILLME` or `PENDING_SIMULATION_AND_HUMAN_QA`.

## Boundaries

No product code, Scene, Resource, game data, art, animation, or HX production is authorized by this specification.
