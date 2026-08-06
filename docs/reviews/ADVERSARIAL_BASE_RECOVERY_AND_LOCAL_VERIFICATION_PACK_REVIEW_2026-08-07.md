# Adversarial review — Base recovery map and Actions simplification

Decision: `OMW-DEC-20260807-PROCESS-BASE-REPOSITORY-SKILL-MAP-AND-LOCAL-VERIFICATION-PACK-V1`

## Findings

### P0 — False completion from a top-level map

**Risk:** A root inventory and Skill index could be presented as full-content recovery.

**Control:** `recovery_status=INCOMPLETE`, `base_recovery_blocker_cleared=false`, explicit unread rows, and `ENTRY_GATE=BLOCK`.

### P0 — Public billing policy applied to a private repository

**Risk:** Standard hosted runners could be described as free and unlimited merely because no larger-runner label is present.

**Control:** Record the observed repository visibility as `private`, do not change visibility in this PR, and do not assert public unlimited billing applicability.

### P1 — Local verification machinery becomes the work

**Risk:** Shell boundaries, launchers, receipts, and exact-head collection create more operational complexity than the validation they protect.

**Control:** Remove the dedicated local pack and reuse the existing `Validate Omenward Core` workflow through `workflow_dispatch`.

### P1 — Runtime coverage silently narrows

**Risk:** Removing the local pack could drop Python 3.11 or platform coverage.

**Control:** The Full matrix is contractually fixed to `ubuntu-latest` and `windows-latest` with Python 3.11, 3.12, and 3.13. Godot 4.7.1 headless validation remains in the same workflow.

### P1 — Workflow presence confused with Green

**Risk:** A valid workflow definition could be reported as successful without a completed exact-head run.

**Control:** Keep `ACTIONS_GREEN=FALSE` until GitHub records a successful run for the exact PR head.

## Verdict

`CONDITIONALLY_ACCEPTABLE_AS_DRAFT_PROCESS_EVIDENCE`

The validation path is simpler and the local pack is removed. The Base recovery blocker and entry gate remain open, and Actions Green still requires an exact-head run.
