# Barracks Economy, Production, and TokenSource Simulation Contract Design

```yaml
updated_at: 2026-08-06
decision_id: OMW-DEC-20260806-PLANNING-BARRACKS-ECONOMY-PRODUCTION-TOKEN-SOURCE-SIMULATION-CONTRACT-V1
status: PROPOSED
artifact_scope: SIMULATION_ARTIFACT_ONLY
approval: USER_REVIEW_PENDING
```

## Goal

Define a reproducible, source-backed simulation contract for jointly tuning barracks construction cost, automatic-production cadence, and TokenSource contribution without changing current unit identity rules.

## Architecture

The contract separates four layers:

1. immutable planning canon: which unit each barracks produces and supplies;
2. tunable economic inputs: cost, cadence, token count, and weight;
3. deterministic scenario matrix: build plans, Stage 2 paths, special outcomes, pressure types, gold states, and token-pool states;
4. decision outputs: KPI distributions, guardrail failures, confidence intervals, and a proposed parameter vector.

```text
SIMULATION_ARTIFACT_ONLY
PRODUCT_IMPLEMENTATION = OUT_OF_SCOPE
ABSOLUTE_VALUES_REQUIRE_SOURCE_DATA
STATIC_MARKER_TESTS_VALIDATE_STRUCTURE_ONLY
```

## Data model

Each run consumes an immutable input manifest and emits one row per parameter-vector × scenario × seed-set combination. The manifest must contain source path, source SHA, unit, version, and missing-value status for every required input.

Primary key:

```text
run_id + scenario_key + parameter_vector_hash + seed_set
```

Required output columns:

```text
decision_id
git_sha
input_manifest_hash
scenario_key
parameter_vector
seed_count
special_option_dominance_rate
general_path_validity_rate
each_special_outcome_path_validity_rate
worst_special_regret_rate
special_token_share_10_min
special_token_share_burst_max
multi_special_dominance_rate
second_special_marginal_value_ratio
reroll_expected_value_gain
confidence_interval
failed_thresholds
```

## Validation strategy

The repository contract test asserts that the proposal, review, routing documents, and plan contain the mandatory markers and never claim balance approval. A future simulation implementation must have separate unit tests for formulas, deterministic seeds, manifest rejection, scenario coverage, and aggregation. Product tests are not part of this proposal.

## Non-goals

- No GDScript, Scene, Resource, `project.godot`, or gameplay data changes.
- No final gold costs, seconds, token counts, or weights.
- No free reroll, result reselection, or unit-identity redesign.
- No claim that static contract tests prove gameplay balance.
