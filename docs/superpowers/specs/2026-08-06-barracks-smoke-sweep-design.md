# Barracks 2,000-Seed Smoke Sweep Design

```yaml
updated_at: 2026-08-06
decision_id: OMW-DEC-20260806-PLANNING-BARRACKS-SMOKE-SWEEP-RESULTS-AND-IDENTIFIABILITY-GATE-V1
parent_decision_id: OMW-DEC-20260806-PLANNING-CURRENT-MAPRUN-ECONOMY-AND-PRESSURE-BASELINE-V1
approval_count: 4_OF_10
status: USER_AUTHORIZED_EXECUTION_DESIGN
scope: ANALYSIS_ARTIFACT_ONLY
product_code_authority: NONE
```

## 1. Goal

Execute the approved 2,000-seed smoke sweep against the 3/10 MapRun economy and pressure baseline, calculate the approved KPI contract, and identify whether the current evidence is sufficient to enter the 10,000-seed decision sweep.

## 2. Selected approach

```text
APPROACH = PROXY_MONTE_CARLO_WITH_IDENTIFIABILITY_ENVELOPE
```

A full battle simulator is rejected because current canon does not provide HP, DPS, range, movement, casualty, tower damage, command aura, tactical skill output, or lane commitment numerics. A static spreadsheet is rejected because it cannot exercise seeded special results, roulette outcomes, build timing, gold policies, and common-random-number comparisons.

The smoke model therefore has two layers:

1. **Canon-backed economy and reel layer**: gold, costs, construction, active-combat clocks, production intervals, physical TokenSource instances, spin price, Stage 1–5 times, and Threat Unit budgets.
2. **Explicit non-canon readiness proxy**: unit functional value, pressure affinity, and non-barracks support are isolated in a model-assumption file and tested under LOW / MID / HIGH support envelopes.

If a KPI threshold changes materially across support envelopes, the result is classified as `MODEL_IDENTIFIABILITY_FAIL` rather than selecting a product balance vector.

## 3. Smoke matrix

```text
SEEDS = 2000
COMMON_RANDOM_NUMBERS = REQUIRED
PARAMETER_VECTORS = 9
STAGE2_PATHS = SHIELD / ARCHER
GOLD_SCENARIOS = LOW / STANDARD / HIGH
SPIN_POLICIES = AGGRESSIVE / RESERVE / MAINTENANCE_ONLY
BUILD_PLANS = GENERAL_ONLY / SPECIAL_ONLY / GENERAL_AND_SPECIAL / MULTI_SPECIAL
FIXED_SPECIAL_OUTCOMES = ASSASSIN / PRIEST / MAGE / FLYING_UNIT / GIANT
```

The nine parameter vectors are the eight contract-range corners plus the current 3/10 baseline:

```text
COST_MULTIPLIER = 1.25 / 2.00
INTERVAL_MULTIPLIER = 1.45 / 2.20
FUNCTIONAL_VALUE_INDEX = 1.35 / 1.65
BASELINE = 1.50 / 1.70 / 1.50
```

Intermediate values remain for the 10,000-seed decision sweep if smoke evidence is sufficient.

## 4. Model boundaries

```text
ROULETTE = NATURAL_CENTERLINE_ONLY
LUCKY_AND_MOVE_OPTIMIZATION = NOT_MODELED
REWARD_GRADE = NORMAL_ONLY
CASUALTY_AND_DEATH = NOT_MODELED
IRREVERSIBLE_LANE_ASSIGNMENT = NOT_MODELED
NON_BARRACKS_SUPPORT = LOW_MID_HIGH_ASSUMPTION_ENVELOPE
FIFTEEN_MINUTE_WINDOW = CENSORED_AT_STAGE5_END_830_SECONDS
```

These omissions make the run a screening model, not a product combat prediction. The output must preserve them as required caveats.

## 5. KPI calculation

The simulator reports the nine approved primary KPIs and supporting diagnostics.

- `SPECIAL_OPTION_DOMINANCE_RATE`: one-special plan materially exceeds the matched general-only plan.
- `GENERAL_PATH_VALIDITY_RATE`: all Stage 1–5 pressure checks pass in the selected support envelope.
- `EACH_SPECIAL_OUTCOME_PATH_VALIDITY_RATE`: fixed-result validity for each of the five special units.
- `WORST_SPECIAL_REGRET_RATE`: worst fixed special result trails the matched median by more than 15%.
- `SPECIAL_TOKEN_SHARE_10_MIN`: physical special TokenSource instances divided by reel length at 10 minutes.
- `SPECIAL_TOKEN_SHARE_BURST_MAX`: maximum physical special token share through the smoke horizon.
- `MULTI_SPECIAL_DOMINANCE_RATE`: multi-special materially exceeds all matched non-multi plans.
- `SECOND_SPECIAL_MARGINAL_VALUE_RATIO`: added 10-minute unit-equivalent value of the second special divided by that of the first.
- `REROLL_EXPECTED_VALUE_GAIN`: fixed to zero because retry and reload preserve the seed and selected result.

## 6. Stop-ship rules

```text
IF_GENERAL_VALIDITY_THRESHOLD_FLIPS_ACROSS_SUPPORT_ENVELOPES = MODEL_IDENTIFIABILITY_FAIL
IF_GENERAL_PATH_VALIDITY_RATE < 0.95 = STOP_SHIP
IF_SPECIAL_TOKEN_SHARE_BURST_MAX > 0.45 = STOP_SHIP
IF_RESULT_DEPENDS_ON_UNAPPROVED_PRODUCT_STATS = DECISION_SWEEP_BLOCKED
IF_STATIC_TEST_PASS_ONLY = BALANCE_PASS_FORBIDDEN
```

A parameter vector cannot advance merely because it passes more countable thresholds. Identifiability and all hard Stop-ship rules take precedence.

## 7. Artifacts

- `docs/analysis/barracks_simulation/smoke_model_assumptions.v1.json`
- `docs/analysis/barracks_simulation/run_barracks_smoke_sweep.py`
- `docs/analysis/barracks_simulation/smoke_sweep_2000.v1.json`
- `docs/analysis/barracks_simulation/smoke_sweep_2000.v1.csv`
- `docs/design/APPROVED_OMENWARD_BARRACKS_SMOKE_SWEEP_RESULTS_2026-08-06.md`
- `docs/reviews/ADVERSARIAL_BARRACKS_SMOKE_SWEEP_REVIEW_2026-08-06.md`
- `tests/python/test_barracks_smoke_sweep.py`

## 8. Product boundary

```text
PRODUCT_CODE = UNCHANGED
GDSCRIPT = UNCHANGED
SCENE_RESOURCE_DATA = UNCHANGED
PROJECT_GODOT = UNCHANGED
LOCAL_GODOT_PROJECT = UNCHANGED
FINAL_PARAMETER_VECTOR = NOT_SELECTED
```
