# Barracks Functional-Value Measurement Scenarios Design

## Goal

Pre-register deterministic, same-input role-measurement fixtures for Priest, Mage, Flier, and Giant without inventing runtime outputs that the current product does not generate. The design converts approved role relationships into measurable vectors and explicitly marks unavailable outputs as `BLOCKED_RUNTIME_OUTPUT`.

## Authority inputs

- `APPROVED_OMENWARD_BARRACKS_FUNCTIONAL_VALUE_COMBAT_NUMERICS_DEFINITION_REVIEW_2026-08-09.md`
- `APPROVED_PLAYER_TEN_UNIT_LINEAGES_POC_V1.md`
- current product unit resources under `data/units/`
- current battle/runtime behavior recovered in PR169

The PoC numeric values remain hypothesis/reference inputs rather than final product numerics.

## Comparison form

```text
FUNCTIONAL_VALUE_COMPARISON = ROLE_SPECIFIC_VECTOR_NO_SINGLE_WEIGHTED_SCORE
POST_HOC_WEIGHT_TUNING = FORBIDDEN
FIXTURE_POLICY = DETERMINISTIC_SAME_INPUT
MONTE_CARLO_FOR_ROLE_VALUE = NOT_AUTHORIZED_BEFORE_ROLE_OUTPUT_RUNTIME_EXISTS
```

No scalar functional-value index is produced by this Gate.

## Output availability classes

```text
MEASURABLE_CURRENT_RUNTIME
PARTIAL_RUNTIME_OUTPUT
BLOCKED_RUNTIME_OUTPUT
DIAGNOSTIC_ONLY
```

`BLOCKED_RUNTIME_OUTPUT` means the scenario is approved and the metric definition is frozen, but no value may be synthesized until runtime instrumentation/behavior exists.

## Shared fixture rules

- Same team counts, initial lane positions, objective state, and deterministic tick settings for both sides of a paired comparison.
- Unit resources are referenced by current archetype IDs, not historical smoke labels.
- No randomized special selection.
- No economy multiplier or functional scalar is injected into battle output.
- Common measurements use current runtime only when the required event/output exists.
- Role-specific unavailable outputs remain null/blocked rather than zero.

## Scenario set

### FV-COMMON-01 — Single-target contact

Purpose: establish common direct-combat timing/output for any archetype under the same opposing frontliner.

Fixture:
- attacker: one candidate unit
- defender: one `shield_guard`
- same initial lane distance and objective state

Current-runtime surfaces:
- time to first contact
- damage dealt
- damage received
- survival time
- capture contribution when applicable
- structure damage only if a structure phase is explicitly included

No role-specific success conclusion is drawn from this scenario alone.

### FV-PRIEST-01 — Support attrition

Purpose: measure Priest contribution as self-combat plus support rather than a damage scalar.

Paired fixture:
- common allied frontline: `shield_guard` + `greatsword_warrior`
- enemy pressure package: `greatsword_warrior` + `archer`
- compare allied package with Priest support against the same base package without Priest support while preserving the same opponent and initial geometry

Required role outputs:
- effective healing HP — `BLOCKED_RUNTIME_OUTPUT`
- overheal waste — `BLOCKED_RUNTIME_OUTPUT`
- supported-target seconds — `BLOCKED_RUNTIME_OUTPUT`
- buff uptime — `BLOCKED_RUNTIME_OUTPUT`
- buff-affected-target seconds — `BLOCKED_RUNTIME_OUTPUT`
- ally deaths prevented — `DIAGNOSTIC_ONLY` after runtime output exists

Current base attack/survival outputs may be collected but cannot substitute for support output.

### FV-MAGE-01 — Cluster versus Archer

Purpose: separate sustained single-target value from Mage collateral/control value.

Paired fixture:
- candidate: `mage` or `archer`
- enemy package: one primary `shield_guard` plus two nearby `shield_guard` targets in a fixed cluster
- same start distance/positions for both candidate runs

Pre-registered relationship from approved PoC direction:
- Archer sustained single-target DPS > Mage sustained single-target DPS
- Mage functional value must be supported by collateral/control output, not by overturning that single-target relationship

Outputs:
- primary-target damage — current direct attack is measurable, but not equivalent to final sustained-DPS acceptance until role-specific attack timing is implemented
- collateral AoE damage — `BLOCKED_RUNTIME_OUTPUT`
- targets hit per cast — `BLOCKED_RUNTIME_OUTPUT`
- control target seconds — `BLOCKED_RUNTIME_OUTPUT`
- debuff target seconds — `BLOCKED_RUNTIME_OUTPUT`

### FV-FLIER-01 — Backline pressure versus Assassin

Purpose: distinguish Assassin burst from Flier sustained backline access.

Paired fixture:
- candidate: `flier` or `assassin`
- enemy frontline: `shield_guard`
- enemy backline: `archer`
- same initial positions and objective state

Pre-registered relationships:
- Assassin single-target burst > Flier single-target burst
- Flier backline-pressure duration > Assassin backline-pressure duration

Outputs:
- time to backline contact — `BLOCKED_RUNTIME_OUTPUT` for decision use until movement-layer/backline targeting exists
- frontline bypass distance/time — Assassin `PARTIAL_RUNTIME_OUTPUT`, Flier `BLOCKED_RUNTIME_OUTPUT`
- dive damage — `BLOCKED_RUNTIME_OUTPUT`
- backline pressure seconds — `BLOCKED_RUNTIME_OUTPUT`
- air targetability exposure — `BLOCKED_RUNTIME_OUTPUT`
- ground obstacle bypass — `BLOCKED_RUNTIME_OUTPUT`

### FV-GIANT-01 — Siege/frontline versus Greatsword

Purpose: separate Greatsword speed/cost advantages from Giant survival/AoE/siege value.

Paired fixture:
- candidate: `giant` or `greatsword_warrior`
- enemy frontline: one `shield_guard`
- fixed enemy objective/structure phase
- same geometry and deterministic tick policy

Pre-registered relationships:
- Greatsword retains speed/cost advantage
- Giant functional value must come from survival/AoE/siege advantage rather than a single damage scalar

Outputs:
- frontline survival time — `MEASURABLE_CURRENT_RUNTIME`
- structure damage — generic siege path `MEASURABLE_CURRENT_RUNTIME`
- slam targets hit — `BLOCKED_RUNTIME_OUTPUT`
- slam total damage — `BLOCKED_RUNTIME_OUTPUT`
- barricade damage — `PARTIAL_RUNTIME_OUTPUT` only where the generic structure path represents the target; role-specific PoC multiplier remains blocked
- stagger/knockback target seconds — `BLOCKED_RUNTIME_OUTPUT`

## Decision rules

1. A role cannot receive a final functional-value index while any role-defining primary output remains `BLOCKED_RUNTIME_OUTPUT`.
2. Base attack/HP/resource values may describe current product inputs but cannot substitute for missing role output.
3. PoC hypothesis numbers may seed later implementation tests, but do not become final targets without a later numeric approval Gate.
4. Comparisons remain vector/Pareto or hard role relationships; no weighted utility score.
5. Missing instrumentation or behavior is a blocker, not a zero observation.

## Gate result and next boundary

When this definition is merged:
- `BARRACKS_FUNCTIONAL_VALUE_MEASUREMENT_SCENARIOS_REQUIRED` is closed.
- `BARRACKS_ROLE_OUTPUT_RUNTIME_IMPLEMENTATION_REQUIRED` remains.
- next planning action becomes `BARRACKS_ROLE_OUTPUT_RUNTIME_IMPLEMENTATION_PACKAGE`.
- actual product/Godot mutation is still unauthorized until the authoring/tool Entry Gate allows it.
- final functional value, final vector, parameter-selection 10k, 50k, and final product numerics remain blocked.

## Self-review

- No placeholder/TBD fields.
- Product archetype IDs use current resources (`shield_guard`, `greatsword_warrior`, `archer`, `assassin`, `priest`, `mage`, `flier`, `giant`).
- Historical smoke taxonomy is not used as product membership.
- Unavailable role metrics are blocked rather than synthesized.
- Scope is one planning/measurement contract; no product implementation is included.
