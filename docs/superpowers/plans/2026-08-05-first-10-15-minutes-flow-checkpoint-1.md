# First 10–15 Minutes Flow — Checkpoint 5 Plan

```yaml
updated_at: 2026-08-06
decision_id: OMW-DEC-20260805-PLANNING-FIRST-10-15-MINUTES-FLOW-V1
status: PARTIAL_APPROVAL_5_OF_10
planning_count: 7_OF_10_IN_PROGRESS
```

## Goal

Canonize Stage 1 T1 placement and gold-safety rules while preserving real economy rules, player-selected build order, the Stage 2 T2 strategic choice, and the merged PC·Android platform authority.

## TDD sequence

1. Merge current main `f5e4bcee7f8459fcfeb492f1ebc19ff932a352f0` into PR #142 without force-push.
2. Resolve the `AGENTS.md` conflict by preserving checkpoint 4 onboarding and adding the merged platform authority.
3. Add RED requirements for checkpoint 5 to `test_first_10_15_minutes_flow_canon.py`.
4. Record RED commit `09c7b7766a1a20be41960f80e4b58bd40f57bef0` before canon implementation.
5. Update canon, adversarial review, specification, and all 13 central routing documents to `PARTIAL_APPROVAL_5_OF_10`.
6. Preserve exact T1 costs and node coordinates as simulation/layout decisions.
7. Synchronize Google Sheet using the same Decision ID and exact final Draft PR HEAD without overwriting the platform Decision.
8. Perform bounded connector read-back, diff-scope review, and review-thread checks.
9. Keep `AUTOMATED_GREEN_NOT_PROVEN` because GitHub Actions cannot start under the billing block.
10. Keep PR #142 Draft until all 10 onboarding checkpoints are approved or the user explicitly authorizes an early merge checkpoint.

## Approved scope

```text
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

## Deferred scope

- exact identities and numeric costs of the first two T2 candidates
- Stage 2 grant and leftover-gold rules
- broader minimum valid path count
- Belu intervention level
- exact Danger pressure and Boss pattern
- failure/retry/skip rules
- exact timings and human-QA thresholds

## Verification boundary

```text
MAIN_REBASE_COMMIT = 8e0c10f312929b5bb69f3ae8850eaf7afa48ee91
CHECKPOINT_5_RED_COMMIT = 09c7b7766a1a20be41960f80e4b58bd40f57bef0
GITHUB_ACTIONS = BLOCKED_BY_BILLING
AUTOMATED_GREEN = NOT_PROVEN
CONNECTOR_BOUNDED_READBACK = REQUIRED
```

## Product boundary

No product code, Scene, Resource, data migration, exact numeric data, level coordinates, image, animation, or HX change is permitted in this planning checkpoint.
