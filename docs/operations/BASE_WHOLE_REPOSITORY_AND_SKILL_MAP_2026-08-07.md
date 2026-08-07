# Base whole-repository and Skill recovery map

Decision: `OMW-DEC-20260807-PROCESS-BASE-REPOSITORY-SKILL-MAP-AND-LOCAL-VERIFICATION-PACK-V1`
Base exact commit: `4f98f968a377f7b6a11aafa4fc94d11bddbebedc`
OMENWARD starting main: `93c388ad1c50581671f8ea059357c863d8d8e0f7`
Status: `INCOMPLETE / ENTRY_GATE_BLOCK`

## Confirmed inventory

The Base root tree contains 29 tracked root paths. Exact recursive indexes were recovered for `.codex-plugin`, `.github`, `skills`, and `tools`; the tests index was fetched but the connector response was clamped. The Base Skill subtree exposes 29 `SKILL.md` entrypoints. The GitHub configuration contains nine workflow files.

The authoritative Base cold-start order begins with `START_HERE.md` and `AGENTS.md`, then routes through the operating model, Work Mode/Skill routing, documentation map, and `skills/SKILL_REGISTRY.json`. A top-level inventory is not full-content recovery.

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

Every unread or partially read top-level surface remains `gate_effect=BLOCKED`. Consequently:

- `BASE_WHOLE_REPOSITORY_AND_SKILL_RECOVERY_NOT_COMPLETED` remains unresolved.
- `ENTRY_GATE` remains `BLOCK`.
- This map cannot authorize product, Godot, GUT, audio, Ready, or merge activity.

## Simplified validation path

The separate Windows/WSL2 launcher and JSON-receipt pack has been removed. Validation now reuses `.github/workflows/validate-omenward-core.yml` through `workflow_dispatch`.

The Full validation job uses only standard GitHub-hosted labels:

- operating systems: `ubuntu-latest`, `windows-latest`
- Python: `3.11`, `3.12`, `3.13`
- Godot: `4.7.1` headless import, contract tests, and runtime smoke

The repository was observed as `private` when this recovery decision was first drafted. The later decision `OMW-DEC-20260807-PROCESS-PUBLIC-REPOSITORY-STANDARD-HOSTED-ACTIONS-V1` superseded only that visibility-preservation clause, and the repository is now public. Standard hosted runner execution, Godot 4.7.1 validation, and the repaired C1·C2·C3 authority contracts are proven on public Actions; Base recovery itself remains incomplete and the entry gate remains blocked.
