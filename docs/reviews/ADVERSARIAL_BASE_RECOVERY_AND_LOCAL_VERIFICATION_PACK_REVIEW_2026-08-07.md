# Adversarial review — Base recovery map and local verification pack

Decision: `OMW-DEC-20260807-PROCESS-BASE-REPOSITORY-SKILL-MAP-AND-LOCAL-VERIFICATION-PACK-V1`

## Findings

### P0 — False completion from a top-level map

**Risk:** A root inventory and Skill index could be presented as full-content recovery.

**Control:** `recovery_status=INCOMPLETE`, `base_recovery_blocker_cleared=false`, explicit unread rows, and `ENTRY_GATE=BLOCK`.

### P0 — Claiming user-local execution from generated scripts

**Risk:** The existence of PowerShell/WSL launchers could be reported as Windows/WSL PASS.

**Control:** Every canonical environment begins at `NOT_RUN_USER_LOCAL`. Only exact-head receipts produced on the user's machine can change evidence state.

### P1 — Platform drift between four environments

**Risk:** Different launchers could run different commands.

**Control:** All launchers delegate to one Python runner. The runner verifies runtime version, exact Git HEAD, command list, exit codes, and receipt.

### P1 — GitHub Actions billing pre-start confused with code failure or Green

**Risk:** A steps-zero billing failure could be described as test failure or success.

**Control:** Classify it separately after exact-head inspection; never call it Actions Green.

## Verdict

`CONDITIONALLY_ACCEPTABLE_AS_DRAFT_PROCESS_EVIDENCE`

P0/P1 controls are encoded, but the Base recovery blocker remains open and user-local Windows/WSL results remain unexecuted.
