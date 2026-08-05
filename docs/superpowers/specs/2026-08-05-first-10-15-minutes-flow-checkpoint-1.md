# First 10–15 Minutes Flow — Checkpoint 1 Specification

```yaml
updated_at: 2026-08-05
decision_id: OMW-DEC-20260805-PLANNING-FIRST-10-15-MINUTES-FLOW-V1
status: PARTIAL_APPROVAL_1_OF_10
planning_count: 7_OF_10_IN_PROGRESS
source: USER_APPROVED_RECOMMENDATION_A
```

## Problem

OMENWARD has separately defined construction, roulette control, deployment, mana tower, tactical research, and merchant systems, but the first-session teaching form was not canonized. A detached tutorial could drift from real MapRun rules, while opening every system at Stage 1 would create cognitive overload and obscure the core causal loop.

## Approved design

The first session is the real MapRun. Systems are disclosed progressively inside play when they become relevant to the current objective.

```text
ONBOARDING_FORMAT = IN_RUN_PROGRESSIVE_DISCLOSURE
FIRST_SESSION = REAL_MAPRUN
SEPARATE_TUTORIAL = FORBIDDEN
FULL_SYSTEM_DUMP_AT_STAGE_1 = FORBIDDEN
RULE_PARITY_WITH_MAIN_RUN = REQUIRED
SCRIPTED_VICTORY = FORBIDDEN
```

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

This checkpoint does not decide system exposure order, the number of valid paths, exact timing, Danger/Boss teaching, merchant teaching, failure/retry rules, or human-QA thresholds. Those remain `PENDING_GRILLME`.

## Boundaries

No product code, scene, resource, game data, art, animation, or HX production is authorized by this specification.
