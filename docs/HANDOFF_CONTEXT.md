# [현행] OMENWARD 프로젝트 인수인계 컨텍스트

```yaml
updated_at: 2026-08-12
project: OMENWARD / 오멘워드
work_mode: BUILD_BLOCKED_ROOT_CAUSE_ISOLATION
phase: PHASE_C_ISSUE176_PROJECT_BOOT_SIGNAL11_ISOLATION
current_planning_status: MAIN_CANONICAL_APPROVED_10_OF_10
current_decision: OMW-DEC-20260809-PLANNING-BARRACKS-ROLE-OUTPUT-RUNTIME-IMPLEMENTATION-PACKAGE-V1
current_blocker: CANONICAL_EXACT_HEAD_PROJECT_BOOT_BOUNDARY
next_gate: DISPOSABLE_AUTOLOAD_AB_ISOLATION
product_completion: false
new_product_decision_required: false
resume_rule: FETCH_LATEST_MAIN_AND_PR175_BEFORE_USE
```

이 파일은 재개 locator다. 저장된 SHA/PID/session/PR 상태는 관찰점이며 GitHub·Sheet·현재 local state보다 높은 정본이 아니다.

## 먼저 읽을 문서

1. `PROJECT_CORE.md`
2. `ACTIVE_CONTEXT.md`
3. `CURRENT_IMPLEMENTATION_STATUS.md`
4. `DECISIONS_PENDING.md`
5. `ONBOARDING_PLANNING_CURRENT_AUTHORITY.md`
6. `PROJECT_CANON_DECISION_LEDGER.md`
7. PR #175 / Issue #176 fresh GitHub state
8. Google Sheet current project hub row

## Current runtime continuation

```text
OMENWARD_MAIN_OBSERVED = 1fef69ccdd7896d70ae2aacdb28ee03f33b6241a
PR175 = OPEN_DRAFT
PR175_DRAFT_7_RUNTIME_GAPS_OPEN
PR175_HEAD_OBSERVED = 83cf816a11f732e2cd285461865cf9c5ed404802
PR175_CHANGED_FILES_OBSERVED = 19
ISSUE176 = OPEN
ISSUE176_APPROVED_RUNTIME_GAPS = 7
ISSUE176_7_GAPS = IMPLEMENTATION_COMPLETENESS
PR175_MERGE = FORBIDDEN_UNTIL_RUNTIME_ACCEPTANCE
PR177 = REFERENCE_ONLY_DO_NOT_MERGE
PHASE_C_GATE = OPEN
CURRENT_RUNTIME_BLOCKER = CANONICAL_EXACT_HEAD_PROJECT_BOOT_BOUNDARY
NEXT_EXECUTABLE_STEP = DISPOSABLE_AUTOLOAD_AB_ISOLATION
```

The clean exact-head archive diagnostic established:

```text
TEMP_INITIAL_GIT = ABSENT
TEMP_INITIAL_GODOT = ABSENT
TEMP_IMPORT = PASS_NO_SIGNAL11_MARKERS
TEMP_NORMAL_HEADLESS_BOOT = CRASH_SIGNAL11_EXIT_NEG1073741819
ACTIVE_PROJECT_FILES_CHANGED_BY_DIAGNOSTIC = NONE
ACTIVE_TEST_HASHES_PRESERVED_AT_DIAGNOSTIC_SNAPSHOT = TRUE
```

Therefore the active local `.godot` cache and the user's uncommitted Issue #176 two-test delta are not required for the earliest reproduced crash. This does not yet identify a specific startup component.

Exact committed autoload boundary at the observed PR head:

```text
HeraGameInspector="*uid://c4ug7a211oav8"
_mcp_game_helper="*res://addons/godot_ai/runtime/game_helper.gd"
```

Next root-cause experiment must use independent fresh exact-head TEMP variants:

```text
BASELINE = BOTH_ON_CRASH_ALREADY_PROVEN
A = HeraGameInspector off only
B = _mcp_game_helper off only
C = both off only if A and B both still crash
```

Do not sequentially edit one TEMP project. Do not modify the active `project.godot`, autoloads, plugins, main scene, GDScript, resources, imports, or active `.godot` during this diagnostic.

## Approved runtime continuation after blocker recovery

The seven Issue #176 runtime gaps remain approved; the same scope does not require reapproval.

```text
PROJECT_BOOT_BLOCKER_CLEARED
→ single-file GUT semantic RED with TESTS_DISCOVERED > 0
→ HiGodot-only seven-gap implementation
→ parse/import
→ same single-file GUT GREEN
→ relevant regressions
→ five registered FV fixtures x2 deterministic
→ Hera live QA/observability
→ HERA_TRACKED_SOURCE_DELTA = NONE
→ adversarial review
→ commit/push/exact-head CI
→ PR175 merge gate review
```

Tool authority:

```text
PERSISTENT_GODOT_GDSCRIPT_GUT_AUTHORING = HIGODOT_ONLY
GUT = DETERMINISTIC_TEST_AUTHORITY
HERA = POST_GREEN_LIVE_QA_OBSERVABILITY_ONLY
HERA_PERSISTENT_SOURCE_MUTATION = FORBIDDEN
SESSION_PID_AND_SESSION_ID = FRESH_READ_EACH_EXECUTION_BLOCK
```

Historical PID/session values must never be reused as current mutation selectors.

## Current product grammar retained

> **건물로 룰렛을 만들고, 룰렛으로 전선을 지휘한다.**

```text
GENERAL_T1 = BASIC_INFANTRY_AUTO_PRODUCTION + BASIC_INFANTRY_TOKEN_SOURCE
GENERAL_T2 = SELECTED_GENERAL_UNIT_AUTO_PRODUCTION + SELECTED_GENERAL_UNIT_TOKEN_SOURCE
GENERAL_T2_BRANCHES = SHIELD / GREATSWORD / SPEAR / ARCHER / CAVALRY
SPECIAL_T1_SELECTION = ONE_RANDOM_RESULT_ON_SUCCESSFUL_CONSTRUCTION_COMMIT
SPECIAL_T1_REVEAL = IMMEDIATE
SPECIAL_T1_PERSISTENCE = FIXED_WHILE_BUILDING_REMAINS_T1
SPECIAL_T1_AUTO_PRODUCTION = SELECTED_RANDOM_SPECIAL_UNIT
SPECIAL_T1_TOKEN_SOURCE = SELECTED_RANDOM_SPECIAL_UNIT
SPECIAL_T1_PATHS = SAME_SELECTED_UNIT_SEPARATE_ACQUISITION_PATHS
SPECIAL_T1_SAVE_RELOAD_RESELECT = FORBIDDEN
SPECIAL_T1_FREE_REROLL = FORBIDDEN
SPECIAL_T2 = SELECTED_SPECIAL_UNIT_AUTO_PRODUCTION + SELECTED_SPECIAL_UNIT_TOKEN_SOURCE
SPECIAL_T2_BRANCHES = MAGE / PRIEST / ASSASSIN / FLYING_UNIT / GIANT
```

기존 `SPECIAL_T1_TOKEN_SOURCE = NONE` 문구는 역사 증거이며 구현 입력 금지다.

## First-run historical planning context retained

```text
STATUS = MAIN_CANONICAL_APPROVED_10_OF_10
FORMAT = IN_RUN_PROGRESSIVE_DISCLOSURE
STAGE_1 = SIX_REQUIRED_T1_AND_FIRST_IRREVERSIBLE_DEPLOYMENT
STAGE_2 = SHIELD_OR_ARCHER_T2_AND_ROULETTE_CONTROL
STAGE_3 = MANA_TOWER_RESEARCH_AND_MANUAL_TACTIC
STAGE_4 = FIRST_DANGER_INTEGRATION
STAGE_5 = FIRST_BOSS_MASTERY_CHECK
MINIMUM_VALID_PATHS = SHIELD_NO_SPECIAL / ARCHER_NO_SPECIAL
INTERNAL_QA_MATRIX = 12_SCENARIOS
FIRST_TIME_HUMAN_SAMPLE = MINIMUM_20
```

The historical August-6 planning state is retained as lineage only. It does not override the current Issue #176 blocker or current runtime continuation above.

## Local working-tree protection

The latest local reports had uncommitted content changes only in:

```text
tests/gut/test_barracks_role_output.gd
tests/headless/barracks_role_output_fv_test.gd
```

This handoff does not assert they still exist. Fresh-read local Git state on resume. If they exist, preserve them; do not reset/restore/clean/stage/overwrite them merely because this file mentions them.

## Base learning candidate

```yaml
learning_id: OMW-LRN-20260812-DISPOSABLE-EXACT-HEAD-STARTUP-ISOLATION
classification: BASE_CANDIDATE
project_application: CURRENT_HANDOFF_CONSUMER_ROUTING_AND_FAIL_CLOSED_SCOPE
base_proposal_id: RESOLVE_AT_BASE_SUBMISSION_FROM_LATEST_BASE_SCHEMA
base_active_implementation_authority: NOT_GRANTED_IN_THIS_STAGE
```

Generic candidate principle:

```text
trusted exact source identity
→ disposable committed-tree materialization
→ fresh derived/cache state
→ earliest reproducible runtime boundary
→ independent one-variable variants
→ active fix only after isolation
```

Base proposal work may write only `[수정제안서]/**` and must fresh-read Base main, Registry, and open proposal PRs before write/merge.

## Recent applicable lessons

- Past PID/session values are historical evidence, not current mutation selectors.
- A sandbox failure to create `git worktree` metadata is an execution-route failure, not a Godot failure; exact `git archive` TEMP materialization is suitable when Git metadata is unnecessary.
- Godot `--import` success and normal game-boot success are separate gates.
- One-variable startup isolation must use independent clean variants; do not reuse one mutated TEMP tree for A/B.
- A handoff/current-state edit is not complete until its machine consumers and scope validator are updated and Green on the same exact head.

## Stop conditions

Stop before product mutation when:

- PR175/main authority moved and is not reconciled;
- exact current HiGodot session cannot be proven;
- normal project boot still crashes;
- a proposed A/B comparison changes more than one variable;
- tooling/sandbox/transport fails before the intended Godot probe actually runs;
- GUT discovers zero tests or fails for parser/tooling instead of approved semantic gaps.

## Continuation checkpoint

```yaml
state_observed_at_main: 1fef69ccdd7896d70ae2aacdb28ee03f33b6241a
work_merge_main_sha: null
closure_pr: 196
closure_head_sha: RESOLVE_FROM_GITHUB_BEFORE_MERGE
self_merge_sha_required_in_file: false
resume_rule: FETCH_LATEST_MAIN_BEFORE_USE
```

Do not create another Handoff PR only to write PR #196's own merge SHA into this file.
