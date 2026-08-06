# Base whole-repository and Skill recovery map

Decision: `OMW-DEC-20260807-PROCESS-BASE-REPOSITORY-SKILL-MAP-AND-LOCAL-VERIFICATION-PACK-V1`  
Base exact commit: `4f98f968a377f7b6a11aafa4fc94d11bddbebedc`  
OMENWARD starting main: `93c388ad1c50581671f8ea059357c863d8d8e0f7`  
Status: `INCOMPLETE / ENTRY_GATE_BLOCK`

## Confirmed inventory

The Base root tree contains 29 tracked root paths. Exact recursive indexes were recovered for `.codex-plugin`, `.github`, `skills`, and `tools`; the tests index was fetched but the connector response was clamped. The Base Skill subtree exposes 29 `SKILL.md` entrypoints. The GitHub configuration contains nine workflow files.

The authoritative Base cold-start order begins with `START_HERE.md` and `AGENTS.md`, then routes through the operating model, Work Mode/Skill routing, documentation map, and `skills/SKILL_REGISTRY.json`. Base explicitly says that “look through the whole repository” does not mean blindly loading every file; it means selecting the responsibility originals and minimum Skills required by the request, without claiming completion when repository access is incomplete.

## Read coverage

Fully read:
- `START_HERE.md`
- `base-v9.4.3.lock.json`
- `tools/run_local_validation.py`

Indexed:
- root tree
- `.codex-plugin/**`
- `.github/**`
- `skills/**`
- `tools/**`
- `tests/**` (response clamped)

Partially read:
- `skills/SKILL_REGISTRY.json`

## Blocking unread coverage

The machine state lists every unread or partially read top-level surface and gives each `gate_effect=BLOCKED`. Consequently:

- `BASE_WHOLE_REPOSITORY_AND_SKILL_RECOVERY_NOT_COMPLETED` remains unresolved.
- `ENTRY_GATE` remains `BLOCK`.
- This map cannot authorize product, Godot, GUT, audio, Ready, or merge activity.

## Local verification pack

The canonical local matrix is:
- Windows: `py -3.11`, `py -3.12`, `py -3.13`
- WSL2 Ubuntu: `python3.12`

`tools/run_local_verification_pack.ps1` runs the three Windows environments. `tools/run_local_verification_pack_wsl.sh` runs Ubuntu 3.12. Each delegates to the same Python runner, verifies exact Git HEAD and Python version, executes the focused contract commands, and writes a JSON receipt.

Shell boundaries are explicit:

- Run `tools/run_local_verification_pack.ps1` from Windows PowerShell.
- Run `tools/run_local_verification_pack_wsl.sh` inside a WSL2 Ubuntu shell.
- Do not use `/mnt/c/...` with PowerShell `Set-Location`, and do not execute the `.sh` file directly as a PowerShell command.
- To launch the WSL verifier while remaining in PowerShell, use `wsl.exe --cd /mnt/c/Users/<USER>/Documents/GitHub/Ninza/omenward bash -lc "./tools/run_local_verification_pack_wsl.sh"`.

Canonical statuses stay `NOT_RUN_USER_LOCAL` until receipts produced on the user's machine are reviewed and bound to an exact commit.
