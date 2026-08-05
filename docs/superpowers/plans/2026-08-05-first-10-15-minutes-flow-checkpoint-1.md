# First 10–15 Minutes Flow — Checkpoint 1 Plan

```yaml
updated_at: 2026-08-06
decision_id: OMW-DEC-20260805-PLANNING-FIRST-10-15-MINUTES-FLOW-V1
status: PARTIAL_APPROVAL_4_OF_10
planning_count: 7_OF_10_IN_PROGRESS
```

## Goal

Canonize the corrected onboarding split: Stage 1 builds one each of all six T1 buildings with brief explanations and real gold, while Stage 2 presents two valid T2 candidates and enough real gold to construct one. Keep exact layout, costs, leftover-gold rules, candidate identities, timing, and implementation blocked.

## TDD sequence

1. Extend `test_first_10_15_minutes_flow_canon.py` with the Stage 1 T1 set, real-gold budget, Stage 2 two-candidate T2 choice, and mana-tower disclosure boundary.
2. Record RED because checkpoint 3 still required a prebuilt T1 start.
3. Update the partial canon, adversarial review, specification, and central routing to checkpoint 4/10.
4. Mark the prebuilt-T1 start as superseded and implementation-forbidden.
5. Synchronize Google Sheet with the same Decision ID and exact Draft PR HEAD.
6. Run fresh documentation CI when GitHub Actions can start; otherwise preserve `CI_BLOCKED_BILLING / AUTOMATED_GREEN_NOT_PROVEN` and perform bounded connector read-back.
7. Keep PR #142 as Draft until the remaining 7/10 decisions are approved or an explicit early merge checkpoint is requested.

## Approved scope

- real MapRun onboarding
- Stage 1 builds one each of all six current T1 buildings
- Stage 1 uses real gold sufficient for the required T1 set
- brief role labels instead of long T1 explanations
- T1 placement performed by the player
- T1 setup is not a branch choice
- first meaningful combat choice is Stage 1 irreversible deployment
- Stage 2 presents two relevant valid T2 candidates
- Stage 2 uses real gold sufficient for one candidate
- first meaningful building choice is the Stage 2 T2 upgrade
- T2 tradeoff preview is required
- mana tower is built in Stage 1 but research explanation waits until Stage 3
- first merchant remains Stage 1 maintenance and teaches optionality/opportunity cost only

## Deferred scope

- exact T1 placement layout and build order
- leftover-gold and non-T1 spending rules
- exact identities and numeric costs of the first two T2 candidates
- broader minimum valid path count
- Belu intervention level
- exact Danger pressure and Boss pattern
- failure/retry/skip rules
- exact timings and human-QA thresholds

## Product boundary

No product code, Scene, Resource, data migration, image, animation, or HX change is permitted in this planning checkpoint.
