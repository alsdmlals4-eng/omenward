# First 10–15 Minutes Flow — Checkpoint 1 Specification

```yaml
updated_at: 2026-08-06
decision_id: OMW-DEC-20260805-PLANNING-FIRST-10-15-MINUTES-FLOW-V1
status: PARTIAL_APPROVAL_4_OF_10
planning_count: 7_OF_10_IN_PROGRESS
source: USER_APPROVED_RECOMMENDATION_WITH_STAGE_SPLIT_CORRECTION
```

## Problem

OMENWARD must teach construction through real action without turning basic T1 setup into a false strategic branch or a long systems lecture. The player should build the full foundation in Stage 1, make a real irreversible deployment decision, then make the first strategic building choice from two valid T2 candidates in Stage 2.

## Approved design

The first session is the real MapRun and uses real gold, real building costs, and real combat rules.

```text
ONBOARDING_FORMAT = IN_RUN_PROGRESSIVE_DISCLOSURE
FIRST_SESSION = REAL_MAPRUN
SYSTEM_EXPOSURE_ORDER = APPROVED_FOUNDATION_THEN_BRANCH_CHOICE
SEPARATE_TUTORIAL = FORBIDDEN
FULL_SYSTEM_DUMP_AT_STAGE_1 = FORBIDDEN
RULE_PARITY_WITH_MAIN_RUN = REQUIRED
SCRIPTED_VICTORY = FORBIDDEN
```

## Stage 1 foundation setup

The player receives enough real gold to build exactly one T1 instance of each current building family:

```text
금고 / 농장 / 병영 / 방어탑 / 지휘소 / 마력탑
```

```text
STAGE_1_T1_BUILDINGS = ONE_EACH_ALL_SIX
STAGE_1_T1_BUILD_BUDGET = GUARANTEED_SUFFICIENT_FOR_REQUIRED_SET
STAGE_1_BUILD_CURRENCY = REAL_GOLD
T1_BUILDING_EXPLANATION = BRIEF_ROLE_LABELS
T1_BUILDING_PLACEMENT = PLAYER_EXECUTED
T1_BUILDING_BRANCH_CHOICE = NONE
LONG_T1_BUILDING_EXPLANATION = FORBIDDEN
```

Each T1 explanation is limited to its name, one-sentence role, and a core icon. Detailed information remains recheckable through HUD or tooltips.

The first meaningful combat choice is the irreversible placement of roulette troops into a lane.

```text
FIRST_MEANINGFUL_COMBAT_CHOICE = STAGE_1_IRREVERSIBLE_DEPLOYMENT
IRREVERSIBLE_DEPLOYMENT = REQUIRED
```

## Stage 2 strategic building choice

Stage 2 grants enough real gold to construct one of two relevant and valid T2 candidates.

```text
FIRST_MEANINGFUL_BUILD_CHOICE = STAGE_2_T2_UPGRADE
STAGE_2_T2_CANDIDATES = TWO_RELEVANT_VALID_OPTIONS
STAGE_2_T2_UPGRADE_BUDGET = GUARANTEED_SUFFICIENT_FOR_ONE_CANDIDATE
T2_UPGRADE_PREVIEW = REQUIRED
```

Before selection, the player must be able to compare what each option gains, sacrifices, how it relates to the current pressure, and how it changes roulette or combat outcomes. Neither candidate is a disguised wrong answer.

## Approved exposure order

```text
Stage 1: forecast → real-gold grant → build one each of all six T1 buildings → roulette → troop result → irreversible deployment → real combat → causal review → first merchant
Stage 2: real-gold T2 grant → compare two valid T2 candidates → construct one T2 → roulette control → multi-front judgment → irreversible deployment
Stage 3: expose the previously built mana tower's research function → first T1 tactic → manual target/lane/timing → result review
Stage 4: first Danger integration using learned systems
Stage 5: first Boss mastery check without a new core system
```

The mana tower is built in Stage 1, but Stage 1 teaches only its brief resource role. Tactical research instruction remains closed until Stage 3.

```text
MANA_TOWER_T1_INCLUDED_IN_STAGE_1_SET = REQUIRED
MANA_TOWER_STAGE_1_EXPLANATION = BRIEF_RESOURCE_ROLE_ONLY
TACTICAL_RESEARCH_EXPLANATION_BEFORE_STAGE_3 = FORBIDDEN
```

## Explicit non-decisions

This checkpoint does not decide the exact T1 placement layout or build order, leftover-gold handling, non-T1 spending restrictions, exact identities of the first two T2 candidates, exact costs, minimum valid paths beyond this two-option choice, Belu intervention intensity, Danger/Boss details, failure/retry/skip rules, timing, or human-QA thresholds.

## Boundaries

No product code, Scene, Resource, game data, art, animation, or HX production is authorized by this specification.
