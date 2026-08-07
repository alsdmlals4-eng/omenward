# Adversarial review — Base recovery map and Actions simplification

Decision: `OMW-DEC-20260807-PROCESS-BASE-REPOSITORY-SKILL-MAP-AND-LOCAL-VERIFICATION-PACK-V1`

## Findings

### P0 — False completion from a top-level map

**Risk:** A root inventory and Skill index could be presented as full-content recovery.

**Control:** `recovery_status=INCOMPLETE`, `base_recovery_blocker_cleared=false`, explicit unread rows, and `ENTRY_GATE=BLOCK`.

### P0 — Public billing policy applied before visibility changed

**Risk:** Standard hosted runners could be described as free and unlimited while the repository was still private.

**Control:** Preserve the original private observation as historical evidence, then supersede only the visibility clause through `OMW-DEC-20260807-PROCESS-PUBLIC-REPOSITORY-STANDARD-HOSTED-ACTIONS-V1`. Require repository API `public` readback and assigned-runner execution before accepting the public hosted path.

### P1 — Local verification machinery becomes the work

**Risk:** Shell boundaries, launchers, receipts, and exact-head collection create more operational complexity than the validation they protect.

**Control:** Remove the dedicated local pack and reuse the existing `Validate Omenward Core` workflow through `workflow_dispatch`.

### P1 — Runtime coverage silently narrows

**Risk:** Removing the local pack could drop Python 3.11 or platform coverage.

**Control:** The Full matrix is contractually fixed to `ubuntu-latest` and `windows-latest` with Python 3.11, 3.12, and 3.13. The historical C2 3.12/3.13 proof marker remains documented without narrowing the actual matrix. Godot 4.7.1 headless validation remains in the same workflow.

### P1 — Workflow presence confused with Green

**Risk:** A valid workflow definition could be reported as successful without a completed exact-head run.

**Control:** Require public standard runner allocation and exact-head success for Project Core Documentation, GDD Sheet Adoption, Base v9 adoption, Omenward Core contracts, Godot import/headless tests, and runtime smoke. Record exact SHAs and run IDs outside this self-referential document.

### P1 — Green Actions confused with Base recovery completion

**Risk:** Successful CI could be used to clear the broader Base recovery or product entry gate.

**Control:** Keep `RECOVERY_STATUS=INCOMPLETE`, `BASE_RECOVERY_BLOCKER_CLEARED=FALSE`, and `ENTRY_GATE=BLOCK` even after exact-head Actions Green. Product, GUT, audio, Ready, and merge authorization remain separate decisions.

## Verdict

`ACCEPTABLE_AS_VALIDATED_DRAFT_PROCESS_EVIDENCE`

The public standard-hosted validation path is proven, the local pack is removed, and exact-head automated contracts are Green. The Base recovery blocker and global entry gate remain open, so PR #159 stays Draft and unmerged.
