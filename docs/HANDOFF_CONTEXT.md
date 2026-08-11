# [현행] OMENWARD 프로젝트 인수인계 컨텍스트

```yaml
updated_at: 2026-08-12
project: OMENWARD / 오멘워드
work_mode: BUILD_BLOCKED_ROOT_CAUSE_ISOLATION
current_decision: OMW-DEC-20260809-PLANNING-BARRACKS-ROLE-OUTPUT-RUNTIME-IMPLEMENTATION-PACKAGE-V1
runtime_pr: 175
runtime_issue: 176
runtime_status: OPEN_DRAFT_BLOCKED_PROJECT_BOOT_SIGNAL11
current_blocker: CANONICAL_EXACT_HEAD_PROJECT_BOOT_BOUNDARY
next_gate: DISPOSABLE_AUTOLOAD_AB_ISOLATION
product_completion: false
new_product_decision_required: false
base_candidate: DISPOSABLE_EXACT_HEAD_RUNTIME_STARTUP_ISOLATION_BEFORE_ACTIVE_MUTATION
base_proposal_id: RESOLVE_AT_BASE_SUBMISSION_FROM_LATEST_BASE_REGISTRY
```

이 파일은 재개 locator다. GitHub/Sheet/live local state보다 높은 정본이 아니며, 재개 시 최신 상태를 먼저 읽는다.

## 먼저 읽을 문서

1. `PROJECT_CORE.md`
2. `ACTIVE_CONTEXT.md`
3. `CURRENT_IMPLEMENTATION_STATUS.md`
4. `docs/operations/ISSUE176_SIGNAL11_CRASH_ISOLATION_HANDOFF_2026-08-12.md`
5. `PROJECT_CANON_DECISION_LEDGER.md`
6. `ONBOARDING_PLANNING_CURRENT_AUTHORITY.md`
7. PR #175 / Issue #176 fresh GitHub state
8. Google Sheet current project hub row

## Current baseline at this handoff

```text
OMENWARD_MAIN_OBSERVED = 1fef69ccdd7896d70ae2aacdb28ee03f33b6241a
PR175 = OPEN_DRAFT
PR175_HEAD_OBSERVED = 83cf816a11f732e2cd285461865cf9c5ed404802
PR175_CHANGED_FILES_OBSERVED = 19
ISSUE176_APPROVED_RUNTIME_GAPS = 7
PR177 = REFERENCE_ONLY_DO_NOT_MERGE
BASE_MAIN_OBSERVED = 1d6cc79ae95ffb67ba4de618f010a6540fc6e02c
BASE_OPEN_PR_OBSERVED = 0
```

These are observation points only. Fresh-read before use.

## What was completed before pause

```text
C0 repository/toolchain gate = PASS
C0 isolated local HiGodot gate = PASS
PR175 current-main reconciliation = COMPLETE at observed head
PR175 runtime scope = restored to exact 19 changed files
PR175 exact-head CI after reconciliation = previously Green at observed head
Issue176 product completion = FALSE
```

Runtime crash isolation then established:

```text
fresh exact-head archive = CREATED
archive initial .git = absent
archive initial .godot = absent
fresh archive --import = no signal11 crash markers
fresh archive normal headless boot = signal11 crash
active project source mutation by diagnostic = NONE
active local test hashes = preserved at diagnostic snapshot
classification = CANONICAL_EXACT_HEAD_PROJECT_BOOT_BOUNDARY
```

Detailed evidence and exact classification matrix live in:
`docs/operations/ISSUE176_SIGNAL11_CRASH_ISOLATION_HANDOFF_2026-08-12.md`.

## Current approved runtime work remains paused

Issue #176 still owns the same seven approved runtime gaps. Do not request reapproval for the same scope after the boot blocker is resolved.

Do not start production implementation while normal project boot crashes before semantic GUT discovery.

Expected sequence after blocker recovery:

```text
project boot healthy
→ approved single-file GUT semantic RED with >0 discovered tests
→ HiGodot-only seven-gap implementation
→ parse/import
→ same single-file GUT GREEN
→ relevant regressions
→ five registered FV fixtures x2 deterministic
→ Hera live QA/observability
→ tracked-source delta NONE
→ adversarial review
→ commit/push/exact-head CI
→ PR175 merge gate review
```

## Next executable step — no product mutation

At the observed exact PR head, `project.godot` has two autoloads:

```text
HeraGameInspector="*uid://c4ug7a211oav8"
_mcp_game_helper="*res://addons/godot_ai/runtime/game_helper.gd"
```

Use the already-proven exact-head archive method in disposable TEMP and run a one-variable A/B matrix:

```text
A = separate fresh extraction; disable HeraGameInspector only
B = separate fresh extraction; disable _mcp_game_helper only
C = both off only if A and B both crash
```

Do not edit the active project's `project.godot`, autoloads, plugins, main scene, GDScript, resources, imports, or `.godot` during this diagnostic.

## Local working-tree protection

The latest local reports indicated uncommitted content changes only in:

```text
tests/gut/test_barracks_role_output.gd
tests/headless/barracks_role_output_fv_test.gd
```

This file does not claim those deltas still exist. Fresh-read the local working tree on resume. If they exist, preserve them; do not reset/restore/clean/stage/overwrite them as part of handoff recovery.

## Tool authority

```text
PERSISTENT_GODOT_GDSCRIPT_GUT_AUTHORING = HIGODOT_ONLY
GUT = DETERMINISTIC_TEST_AUTHORITY
HERA = POST_GREEN_LIVE_QA_OBSERVABILITY_ONLY
HERA_PERSISTENT_SOURCE_MUTATION = FORBIDDEN
SESSION_PID_AND_SESSION_ID = FRESH_READ_EACH_EXECUTION_BLOCK
```

Hera is required later; it is not removed from the workflow. It is downstream of GREEN/FV for this runtime package.

## Recent applicable lessons

### OMW-LSN-ISSUE176-001
Past PID/session values are historical evidence, not current mutation selectors. Fresh-list and bind exact project identity before each mutation block.

### OMW-LSN-ISSUE176-002
A Codex sandbox failure to create `git worktree` metadata is an execution-route failure, not a Godot failure. For clean committed-tree diagnostics that do not need Git metadata, `git archive` to disposable TEMP preserved the active repository and unblocked the experiment.

### OMW-LSN-ISSUE176-003
Godot `--import` PASS and normal headless game boot PASS are separate gates. The current evidence is import-no-crash plus game-boot signal11; do not collapse them into one status.

### OMW-LSN-ISSUE176-004
One-variable startup isolation must use independent fresh variants. Sequential edits in one TEMP project can contaminate the classification.

Lesson detail owner:
`docs/operations/ISSUE176_SIGNAL11_CRASH_ISOLATION_HANDOFF_2026-08-12.md`.

## Base learning state

```yaml
learning_id: OMW-LRN-20260812-DISPOSABLE-EXACT-HEAD-STARTUP-ISOLATION
classification: BASE_CANDIDATE
project_application: APPLIED_TO_HANDOFF_AND_RESUME_PROCEDURE
project_verification: PROJECT_CLOSURE_PR_REQUIRED
base_existing_solution_verdict: MATERIAL_BOUNDED_EXTENSION_TO_EXISTING_RUNTIME_DIAGNOSTIC_OWNERS
base_proposal_id: RESOLVE_AT_BASE_SUBMISSION_FROM_LATEST_BASE_SCHEMA
base_active_implementation_authority: NOT_GRANTED_IN_THIS_STAGE
```

The Base proposal stage may write only `[수정제안서]/**`. It must not modify Base active Skill/Registry/Template/Test/Tool/Workflow/Docs in this stage.

## Stop conditions

Stop before product mutation when:

- PR175/main authority moved and is not reconciled;
- exact current HiGodot session cannot be proven;
- project boot is still crashing;
- a proposed A/B comparison changes more than one variable;
- a tool/sandbox/transport failure occurs before the intended Godot probe actually runs;
- GUT discovers zero tests or fails for parser/tooling instead of approved semantic gaps.

## Continuation checkpoint

```yaml
state_observed_at_main: 1fef69ccdd7896d70ae2aacdb28ee03f33b6241a
work_merge_main_sha: null
closure_pr: RESOLVE_FROM_GITHUB_HISTORY
closure_head_sha: RESOLVE_FROM_GITHUB_HISTORY
self_merge_sha_required_in_file: false
resume_rule: FETCH_LATEST_MAIN_BEFORE_USE
```

Do not create a recursive Handoff PR only to write this closure PR's own merge SHA back into the file.
