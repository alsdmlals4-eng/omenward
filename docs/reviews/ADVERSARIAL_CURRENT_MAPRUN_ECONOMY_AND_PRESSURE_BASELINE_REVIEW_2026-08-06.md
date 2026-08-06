# Adversarial Review — Current MapRun Economy and Pressure Baseline

```yaml
decision_id: OMW-DEC-20260806-PLANNING-CURRENT-MAPRUN-ECONOMY-AND-PRESSURE-BASELINE-V1
scope: SIMULATION_BASELINE_ADVERSARIAL_REVIEW
status: REVIEWED_WITH_SMOKE_ONLY_GATE
```

## Risks and mitigations

### MANDATORY_VAULT_INCOME_DOUBLE_COUNT_RISK
A mandatory Vault plus global passive income can silently recreate the old optional-market income on top of a new baseline. Mitigation: split the baseline into 3 gold global + 3 gold Vault per 20 active-combat seconds and require separate reporting for each source.

### FOUNDATION_GRANT_SURPLUS_LEAK_RISK
A single oversized starting wallet can become free merchant or roulette capital. Mitigation: six required costs sum to exactly 250, the foundation grant is exactly 250, and the 20-gold first-spin grant occurs only after foundation completion.

### MAINTENANCE_AFK_FARM_RISK
Unbounded maintenance with income or production enabled creates optimal waiting. Mitigation: passive income and production are off, the active decision baseline is 30 seconds, and accessibility pause suspends every maintenance clock.

### SPECIAL_BARRACKS_DOUBLE_VALUE_DOMINANCE_RISK
Special T1 supplies both a stronger automatic unit and a physical TokenSource. Mitigation: cost 60, optional-node use, food costs, slower 75~110 second production, uniform result distribution, and existing dominance KPIs remain mandatory.

### FIRST_FIVE_STAGE_FORCED_OVERLAP_RISK
Fixed wave offsets could introduce Stage 9's overlap lesson too early. Mitigation: `MAX_TARGET_OFFSET_OR_PREVIOUS_CLEAR_PLUS_8_SECONDS`; no forced overlap before Stage 9.

### THREAT_UNIT_FALSE_PRECISION_RISK
Threat Unit budgets can look like final enemy counts or stats. Mitigation: TU is explicitly a normalized composition unit; exact HP, DPS, spawn counts, and route speeds remain product-data decisions.

### OPTIONAL_NODE_LAYOUT_AUTHORITY_RISK
A baseline of two optional nodes could be mistaken for final map layout. Mitigation: use 1/2/3 node-budget scenarios and forbid coordinate authority in this decision.

### STAGE2_GRANT_DOUBLE_SPEND_RISK
The reserved 50-gold T2 grant could be spent elsewhere. Mitigation: retain the approved reserve transaction and block non-candidate spending until Shield or Archer is confirmed.

### ECONOMY_TIMER_RESET_EXPLOIT_RISK
Resetting 20/60-second income timers at Stage boundaries can reward transition timing. Mitigation: timers persist across the MapRun and pause outside active combat.

## Stop-ship

```text
FOUNDATION_GRANT_SURPLUS > 0 = STOP_SHIP
STAGE2_RESERVED_GRANT_SPENDABLE_ELSEWHERE = STOP_SHIP
MAINTENANCE_PASSIVE_GOLD_OR_AUTO_PRODUCTION = STOP_SHIP
FORCED_OVERLAP_BEFORE_STAGE9 = STOP_SHIP
SPECIAL_OPTION_DOMINANCE_RATE > 0.60 = STOP_SHIP
GENERAL_PATH_VALIDITY_RATE < 0.95 = STOP_SHIP
FIRST_FIVE_EXPECTED_TOTAL_SECONDS OUTSIDE 600..900 = STOP_SHIP
SMOKE_PASS_ESCALATION_WITHOUT_REVIEW = FORBIDDEN
```

## Validation boundary

```text
PRODUCT_CODE = UNCHANGED
LOCAL_GODOT_PROJECT = UNCHANGED
SIMULATION = READY_NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
FINAL_PRODUCT_NUMERICS = NOT_APPROVED
```
