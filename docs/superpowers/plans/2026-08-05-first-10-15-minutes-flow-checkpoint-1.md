# First 10–15 Minutes Flow — Checkpoint 1 Plan

```yaml
updated_at: 2026-08-05
decision_id: OMW-DEC-20260805-PLANNING-FIRST-10-15-MINUTES-FLOW-V1
status: PARTIAL_APPROVAL_1_OF_10
planning_count: 7_OF_10_IN_PROGRESS
```

## Goal

Canonize only the approved onboarding form while keeping every unapproved sequence, timing, numeric, UX, and implementation detail blocked.

## TDD sequence

1. Add `test_first_10_15_minutes_flow_canon.py` and wire it into documentation CI.
2. Confirm the new contract fails because authority and routing files are absent.
3. Add the partial canon, adversarial review, and central authority routing.
4. Synchronize Google Sheet with the same Decision ID and exact Draft PR HEAD.
5. Run fresh documentation CI, bounded Sheet read-back, PR diff review, and unresolved-thread check.
6. Keep PR #142 as Draft until the remaining 7/10 decisions are approved or an explicit early merge checkpoint is requested.

## Approved scope

- real MapRun onboarding
- in-run progressive disclosure
- no separate tutorial
- no Stage 1 full-system dump
- no scripted victory
- rule parity with the main run
- Belu does not replace player choice

## Deferred scope

- system exposure order
- first meaningful ruler choice
- minimum valid paths
- Danger and Boss teaching
- first merchant exposure
- failure/retry/skip rules
- exact timings and human-QA thresholds

## Product boundary

No product code, Scene, Resource, data migration, image, animation, or HX change is permitted in this planning checkpoint.
