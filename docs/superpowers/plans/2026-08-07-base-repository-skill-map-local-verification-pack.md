# Base repository/Skill recovery map and Windows + WSL2 local verification pack

> **Decision:** `OMW-DEC-20260807-PROCESS-BASE-REPOSITORY-SKILL-MAP-AND-LOCAL-VERIFICATION-PACK-V1` (`NON_COUNTER`)
> **Status:** `RECOVERY_MAP_CREATED_INCOMPLETE / LOCAL_EXECUTION_NOT_RUN / ENTRY_GATE_BLOCK`

**Goal:** Record an exact-commit, fail-closed map of the Base repository surfaces already read, explicitly mark unread material, and add a repeatable local verification pack for Windows Python 3.11/3.12/3.13 plus WSL2 Ubuntu Python 3.12.

**Base commit:** `4f98f968a377f7b6a11aafa4fc94d11bddbebedc`  
**OMENWARD base commit:** `93c388ad1c50581671f8ea059357c863d8d8e0f7`

## Non-goals

- Do not clear `BASE_WHOLE_REPOSITORY_AND_SKILL_RECOVERY_NOT_COMPLETED`.
- Do not claim any user-local Windows or WSL2 command ran.
- Do not authorize product implementation, Godot authoring, GUT activation/execution, asset import, Ready, or merge.
- Do not mutate `addons/gut`, product, Scene, Resource, `project.godot`, or audio paths.

## TDD sequence

1. Commit this plan.
2. Add a focused bootstrap/contract test that requires:
   - exact Base and OMENWARD SHAs,
   - all 29 Base root paths,
   - 29 discovered Base `SKILL.md` entrypoints,
   - nine Base workflows,
   - explicit `NOT_READ/BLOCKED` entries,
   - exact Windows/WSL2 matrix,
   - all user-local results initialized to `NOT_RUN_USER_LOCAL`,
   - `ENTRY_GATE=BLOCK`,
   - PowerShell and WSL2 launchers.
3. Reproduce RED while validator/state/launchers are absent.
4. Add the machine state, validator, common runner, PowerShell launcher, WSL2 launcher, and intended GitHub Actions matrix.
5. Run fresh compile, focused unittest, state validator, launcher dry checks, and `git diff --check` in a reconstructed exact-file workspace.
6. Open a Draft PR, record exact head, changed-file allowlist, verification evidence, and GitHub Actions classification.
7. Sync the same Decision ID to bounded Sheet rows and read them back.

## Local matrix

| Environment ID | Host | Runtime | Required command |
|---|---|---|---|
| `windows-py311` | Windows | CPython 3.11 | `py -3.11` |
| `windows-py312` | Windows | CPython 3.12 | `py -3.12` |
| `windows-py313` | Windows | CPython 3.13 | `py -3.13` |
| `wsl2-ubuntu-py312` | WSL2 Ubuntu | CPython 3.12 | `python3.12` |

Each run writes one JSON receipt. Until the user executes the pack, every environment remains `NOT_RUN_USER_LOCAL`.

## Acceptance

- The map is honest about coverage and does not clear the Base recovery blocker while unread surfaces remain.
- The local pack is deterministic, checks the exact Git HEAD, records runtime identity and every command exit code, and fails on the first non-zero command.
- No completion claim is made without fresh evidence.
