# Issue #176 Signal-11 Crash Isolation Handoff — 2026-08-12

## Status

```yaml
source_project: alsdmlals4-eng/omenward
source_main: 1fef69ccdd7896d70ae2aacdb28ee03f33b6241a
runtime_pr: 175
runtime_pr_head: 83cf816a11f732e2cd285461865cf9c5ed404802
runtime_pr_state: OPEN_DRAFT
runtime_issue: 176
decision: OMW-DEC-20260809-PLANNING-BARRACKS-ROLE-OUTPUT-RUNTIME-IMPLEMENTATION-PACKAGE-V1
product_completion: false
product_mutation_during_crash_isolation: none
current_blocker: CANONICAL_EXACT_HEAD_PROJECT_BOOT_BOUNDARY
next_executable_step: DISPOSABLE_AUTOLOAD_AB_ISOLATION
```

This file is historical/runtime-diagnostic evidence. Live repository, PR, Base, local process, session, PID, port, and working-tree state must be fresh-read before reuse.

## What is currently proven

A fresh exact-head project archive was created from PR #175 head `83cf816a11f732e2cd285461865cf9c5ed404802` in disposable TEMP state.

The clean archive had no `.git` and no `.godot` before Godot execution.

Using the dedicated self-contained Godot 4.7.1 executable:

1. `--headless --path <TEMP_PROJECT> --import` completed with no signal-11 crash markers and created fresh `.godot` state.
2. The subsequent normal headless game boot, `--headless --path <TEMP_PROJECT> --quit-after 2`, crashed with Windows exit `-1073741819` and the signal-11 crash markers.
3. The active project's local `.godot` cache is therefore not required for the earliest reproduced crash.
4. The active user's uncommitted Issue #176 test deltas are not required for the earliest reproduced crash because the clean archive used the exact committed PR head before those local test deltas were copied.
5. Active project tracked source was not changed by this diagnostic run.

Current classification:

```text
CANONICAL_EXACT_HEAD_PROJECT_BOOT_BOUNDARY
```

This does **not** prove which startup component is responsible.

## Exact committed autoload boundary

At exact PR head `83cf816a11f732e2cd285461865cf9c5ed404802`, `project.godot` registers exactly these two autoloads:

```text
HeraGameInspector="*uid://c4ug7a211oav8"
_mcp_game_helper="*res://addons/godot_ai/runtime/game_helper.gd"
```

The next experiment is a disposable one-variable matrix only:

```text
baseline: both on = CRASH (already proven)
A: HeraGameInspector off only
B: _mcp_game_helper off only
C: both off only if A and B both still crash
```

Every variant must start from a separate fresh extraction of the same exact-head archive. Do not reuse one TEMP project and sequentially edit it for A/B.

## Next classification matrix

```text
A PASS + B CRASH
= HERA_GAME_INSPECTOR_AUTOLOAD_BOUNDARY

A CRASH + B PASS
= MCP_GAME_HELPER_AUTOLOAD_BOUNDARY

A PASS + B PASS
= AUTOLOAD_INTERACTION_BOUNDARY

A CRASH + B CRASH + C PASS
= BOTH_AUTOLOADS_INDEPENDENT_TRIGGER_BOUNDARY

A CRASH + B CRASH + C CRASH
= NON_AUTOLOAD_PROJECT_BOOT_BOUNDARY
```

No active-project fix is authorized by this evidence alone. Root cause must be isolated before any fix.

## Runtime-authoring and QA boundaries

- Persistent Godot/GDScript/GUT authoring: HiGodot/Godot AI only.
- GUT remains the deterministic GDScript test authority.
- Hera remains live QA/observability authority after GREEN; it is not a persistent source authoring authority.
- Hera tracked-source delta must be `NONE` when the runtime package eventually reaches the live-QA stage.
- Issue #176 production implementation must not resume until the project boot blocker is cleared and a genuine semantic GUT RED with `>0` discovered tests is obtained.
- `-gdir=res://tests/gut` remains forbidden for the approved Issue #176 GUT entrypoint; use the approved single-file `-gtest=res://tests/gut/test_barracks_role_output.gd` form once project boot is healthy.
- Blocked observables remain literal `BLOCKED_RUNTIME_OUTPUT`; do not synthesize numeric zero.
- No final weighted FV scalar/vector/product numerics are approved.

## Local-state caveat

The last local working-tree reports contained uncommitted changes only in:

```text
tests/gut/test_barracks_role_output.gd
tests/headless/barracks_role_output_fv_test.gd
```

Those are local evidence, not repository-main content. A future executor must fresh-read local `git status`, staged/untracked state, and file hashes before any mutation. Do not discard, restore, reset, clean, stage, commit, or overwrite those local deltas merely because this handoff records them.

## Recent applicable troubleshooting lessons

### OMW-LSN-ISSUE176-001 — Session/PID evidence is ephemeral

- Symptom: a previous PID/session can remain in handoff while the actual editor/session has changed.
- Rule: every mutation block fresh-lists the exact OMENWARD session and binds project path, version, readiness, active state, and current editor PID in one current receipt.
- Do not reuse historical session IDs or PIDs as selectors.

### OMW-LSN-ISSUE176-002 — Sandbox `git worktree` failure is not a Godot failure

- Symptom: diagnostic preparation stopped because Codex sandbox could not write `.git/worktrees` metadata.
- Resolution: use `git archive` of an exact commit into disposable TEMP when the experiment only needs a clean committed project tree and no Git metadata.
- Do not weaken sandbox or active-repository safety just to make `git worktree` succeed.

### OMW-LSN-ISSUE176-003 — Import success and game-boot success are separate gates

- Observation: clean archive `--import` produced no signal-11 markers, while normal headless boot crashed.
- Consequence: classify the earliest failing boundary precisely; do not relabel import Green as project runtime Green.

### OMW-LSN-ISSUE176-004 — Root-cause A/B must use independent clean variants

- Baseline has two startup autoloads.
- A/B variants must be independent fresh archive extractions with exactly one autoload removed per variant.
- Do not attempt an active-project fix before the one-variable matrix identifies the failing component/interaction boundary.

## Resume read order

1. Fresh OMENWARD `main`, open PRs, PR #175 exact current head and changed files.
2. Fresh Base `main` and current project operating contract.
3. Google Sheet current project hub row.
4. `docs/ACTIVE_CONTEXT.md`.
5. `docs/CURRENT_IMPLEMENTATION_STATUS.md`.
6. This file.
7. PR #175 / Issue #176 current discussion and latest local Codex output.
8. Fresh local Git/HiGodot identity only when returning to local execution.

## Stop conditions

Stop before active product mutation if any of these are true:

- PR #175 head/main authority has changed and has not been reconciled.
- exact current OMENWARD HiGodot session cannot be proven.
- disposable A/B experiment is not single-variable.
- a probe fails due to tooling/sandbox/transport before Godot actually runs; classify that failure separately.
- project boot still crashes before semantic GUT discovery.

## Continuation checkpoint

```yaml
state_observed_at_main: 1fef69ccdd7896d70ae2aacdb28ee03f33b6241a
work_merge_main_sha: null
closure_pr: TO_BE_RESOLVED_FROM_GITHUB_HISTORY
closure_head_sha: TO_BE_RESOLVED_FROM_GITHUB_HISTORY
self_merge_sha_required_in_file: false
resume_rule: FETCH_LATEST_MAIN_BEFORE_USE
```

The closure PR's own merge SHA is intentionally not required in this file. GitHub history is the authoritative merge record; do not create a recursive handoff PR only to write back this document's own merge SHA.
