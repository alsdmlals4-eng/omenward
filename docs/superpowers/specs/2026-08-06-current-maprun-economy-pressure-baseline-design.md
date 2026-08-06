# Current MapRun Economy and Pressure Baseline Design

```yaml
decision_id: OMW-DEC-20260806-PLANNING-CURRENT-MAPRUN-ECONOMY-AND-PRESSURE-BASELINE-V1
approval_count: 3_OF_10
approach: HYBRID_ABSOLUTE_ONBOARDING_AND_NORMALIZED_THREAT_BASELINE
scope: SIMULATION_BASELINE_ONLY
```

## Goal

Resolve the six blockers identified by the approved provenance manifest without pretending that provisional simulation values are final product balance.

## Considered approaches

1. **Restore the July absolute baseline unchanged.** Rejected because it assumes one 15-minute Stage, optional market income, four special classes, and legacy clock rules.
2. **Use only dimensionless indexes.** Rejected because wallet timing, construction completion, production arrival, and Wave scheduling cannot be simulated without gold and seconds.
3. **Hybrid absolute onboarding and normalized threat baseline.** Selected. Gold and seconds are fixed for Stage 1~5 smoke simulation, while enemy pressure and opportunity cost use normalized units and vectors.

## Architecture

- `APPROVED_OMENWARD_CURRENT_MAPRUN_ECONOMY_AND_PRESSURE_BASELINE_2026-08-06.md` owns the human-readable contract.
- `current_maprun_economy_pressure_baseline.v1.json` is the machine-readable input.
- `test_current_maprun_economy_pressure_baseline.py` prevents drift between authority, input, review, routers, and run gates.
- Stage 6~20 is explicitly outside this gate. Later work scales from this baseline after smoke validation.

## Economy

The six required Stage 1 T1 buildings cost exactly 250 gold. The foundation wallet receives exactly 250 and cannot leak surplus. After all six buildings complete, a separate real 20-gold operational grant funds the first normal-price spin. Base income and mandatory Vault income each pay 3 gold per 20 active-combat seconds. Control pays 4 gold per held midpoint every 60 active-combat seconds. Timers persist across Stage boundaries and pause outside active combat.

Stage 2 Shield and Archer share a 50-gold cost and 25-second upgrade time. The Stage 2 reserved grant is exactly 50. Special Barracks T1 costs 60 gold for smoke simulation.

## Clock model

Maintenance has a 30-active-decision-second baseline. Gold, control income, automatic production, cooldowns, mana recovery, damage, healing, and status ticks stop. Construction, upgrades, and repairs progress while the maintenance decision clock is actively running. Accessibility pause suspends every maintenance clock, preventing economic advantage from pausing.

## Production

Basic Infantry produces every 50 active-combat seconds. The first Shield and Archer branches both produce every 65 seconds. Special T1 intervals are Assassin 75, Priest 80, Mage 90, Flying 100, and Giant 110 seconds. Selection remains uniform at 20% each for the smoke baseline.

## Pressure and timeline

One Threat Unit is one Stage 1 baseline light-ground enemy equivalent. It is a simulation composition unit, not a product stat. Stage 1~5 active-combat budgets are 110, 120, 130, 140, and 160 seconds. With a 50-second expected foundation setup and four 30-second maintenance phases, the expected first-five-Stage window is 830 seconds, or 13 minutes 50 seconds.

Wave starts use `MAX_TARGET_OFFSET_OR_PREVIOUS_CLEAR_PLUS_8_SECONDS`. This prevents forced overlap before the separately approved Stage 9 overlap lesson.

## Opportunity cost

Do not collapse investment into one arbitrary score. Compare a four-dimensional vector:

```text
gold = investment_gold / 40
time = first_unit_wait_seconds / 50
food = unit_food_cost / 6
node = occupied_optional_nodes / 2
```

The post-foundation optional-node budget is a simulation baseline of 2, with 1 and 3 as scarcity/leniency stress values. It does not authorize final level coordinates.

## Run gate

The baseline unlocks only the 2,000-seed smoke sweep. Decision and confirmation sweeps remain blocked until the preceding sweep passes and receives an explicit review. Product implementation and final product numerics remain unauthorized.
