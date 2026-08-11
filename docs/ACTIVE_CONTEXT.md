# [현행] Active Context

```yaml
updated_at: 2026-08-12
current_branch: main
current_main: RESOLVE_FROM_REPOSITORY_DEFAULT_BRANCH
context_baseline_commit: RESOLVE_FROM_REPOSITORY_DEFAULT_BRANCH
current_decision: OMW-DEC-20260809-PLANNING-BARRACKS-ROLE-OUTPUT-RUNTIME-IMPLEMENTATION-PACKAGE-V1
activation_decision: OMW-DEC-20260811-OPS-ACTIVATE-INTEGRATED-CONTRACT-V4-5-R2-V1
contract_version: 4.5
work_phase: PHASE_C_ISSUE176_PROJECT_BOOT_SIGNAL11_ISOLATION
phase_c_gate: OPEN_BLOCKED_RUNTIME_BOOT
```

Current main SHA는 이 문서에 고정하지 않고 repository default branch에서 fresh resolve한다.

## Current phase

```text
MAIN_CANONICAL_APPROVED_10_OF_10
WHOLE_PROJECT_CONTENT_DECISION_GROUPS_OPEN = 0
WHOLE_PROJECT_CONTENT_DECISIONS = CLOSED
USER_EXPLICIT_PLANNING_COMPLETE_DECLARATION = RECEIVED
PHASE_B_FINAL_PLANNING_REVIEW = PASS
OMW-DEC-20260811-OPS-PHASE-B-FINAL-PLANNING-REVIEW-V1
PHASE_C_C0_REPOSITORY_TOOLCHAIN_GATE = PASS
PHASE_C_C0_LOCAL_HIGODOT_GATE = PASS
PHASE_C_C0_OVERALL = PASS
NEW_PRODUCT_DECISION_REQUIRED = FALSE
IMPLEMENTATION_PACKAGE_DEFINITION_OF_READY = CLOSED
PHASE_C_GATE = OPEN
PHASE_C_STATUS = ISSUE176_PROJECT_BOOT_SIGNAL11_BLOCKED
PRODUCT_IMPLEMENTATION_COMPLETION = FALSE
```

Current C0 local closure owner remains:
`docs/reviews/PHASE_C_C0_LOCAL_HIGODOT_CLOSURE_2026-08-11.md`

Historical C0 repository/toolchain owner remains:
`docs/reviews/PHASE_C_C0_PREFLIGHT_2026-08-11.md`

Historical activation evidence remains:

```text
OMW-DEC-20260811-OPS-ACTIVATE-INTEGRATED-CONTRACT-V4-5-R2-V1
V45_R2_ACTIVATION_EVIDENCE_CLOSURE = MERGED
```

## Runtime handoff — current blocker

```text
PR175 = OPEN_DRAFT
PR175_HEAD_OBSERVED = 83cf816a11f732e2cd285461865cf9c5ed404802
PR175_BASE_OBSERVED = 1fef69ccdd7896d70ae2aacdb28ee03f33b6241a
PR175_CHANGED_FILES_OBSERVED = 19
ISSUE176 = OPEN
ISSUE176_APPROVED_RUNTIME_GAPS = 7
ISSUE176_7_GAPS = IMPLEMENTATION_COMPLETENESS
PR175_MERGE = FORBIDDEN_UNTIL_RUNTIME_ACCEPTANCE
PR177 = REFERENCE_ONLY_DO_NOT_MERGE
CURRENT_RUNTIME_BLOCKER = CANONICAL_EXACT_HEAD_PROJECT_BOOT_BOUNDARY
CLEAN_ARCHIVE_INITIAL_GIT = ABSENT
CLEAN_ARCHIVE_INITIAL_GODOT = ABSENT
CLEAN_ARCHIVE_IMPORT = PASS_NO_SIGNAL11_MARKERS
CLEAN_ARCHIVE_NORMAL_HEADLESS_BOOT = CRASH_SIGNAL11_EXIT_NEG1073741819
ACTIVE_PROJECT_FILES_CHANGED_BY_DIAGNOSTIC = NONE
ACTIVE_TEST_HASHES_PRESERVED_AT_DIAGNOSTIC_SNAPSHOT = TRUE
NEXT_EXECUTABLE_STEP = DISPOSABLE_AUTOLOAD_AB_ISOLATION
```

The clean exact-head archive reproduces the earliest crash without the active local `.godot` cache and without the user's uncommitted Issue #176 test deltas. It isolates the blocker to committed project startup state or below, but does not yet identify a specific autoload or main-scene component.

Exact committed autoload boundary at the observed PR head:

```text
HeraGameInspector="*uid://c4ug7a211oav8"
_mcp_game_helper="*res://addons/godot_ai/runtime/game_helper.gd"
```

Next diagnostic is read-only with respect to the active project:

```text
BASELINE = BOTH_AUTOLOADS_ON_CRASH_ALREADY_PROVEN
A = independent fresh exact-head TEMP; HeraGameInspector off only
B = independent fresh exact-head TEMP; _mcp_game_helper off only
C = both off only if A and B both still crash
```

Do not sequentially edit one TEMP project for A/B. Do not apply an active-project startup fix before the one-variable matrix identifies the responsible component or interaction boundary.

Persistent Issue #176 product authoring remains stopped until:

```text
PROJECT_BOOT_BLOCKER_CLEARED
→ semantic single-file GUT RED with TESTS_DISCOVERED > 0
→ HiGodot-only seven-gap implementation
→ GUT GREEN + regressions
→ registered FV fixtures x2 deterministic
→ Hera live QA
→ HERA_TRACKED_SOURCE_DELTA = NONE
```

## Runtime/evidence dependency

```text
ROLE_OUTPUT_RUNTIME -> DETERMINISTIC_MEASUREMENT -> FUNCTIONAL_VALUE_COMPARISON -> FINAL_TUNING
FINAL_FUNCTIONAL_VALUE = POST_RUNTIME_EVIDENCE_TUNING
FINAL_PARAMETER_VECTOR = NOT_SELECTED
FINAL_PRODUCT_NUMERICS = NOT_APPROVED
SPECIAL_T1_SELECTION_DISTRIBUTION = POST_RUNTIME_EVIDENCE_TUNING
```

## Physical TokenSource current truth

```text
SPECIAL_T1_SELECTION_TRIGGER = SUCCESSFUL_CONSTRUCTION_COMMIT
SPECIAL_T1_AUTO_PRODUCTION = SELECTED_RANDOM_SPECIAL_UNIT
SPECIAL_T1_TOKEN_SOURCE = SELECTED_RANDOM_SPECIAL_UNIT
TOKEN_INSTANCES_PER_REEL_PER_ACTIVE_SOURCE = 1
TOTAL_TOKEN_INSTANCES_PER_ACTIVE_SOURCE = 3
FRACTIONAL_TOKEN_WEIGHT = FORBIDDEN
```

## Work-entry process

```text
BENCHMARK_AND_INDUSTRY_RESEARCH_REQUIRED_BEFORE_WORK = TRUE
BENCHMARK_DISPOSITION = ADOPT / ADAPT / AVOID / TEST / IGNORE
COMPETITOR_BEHAVIOR_AUTOMATIC_AUTHORITY = FORBIDDEN
POST_CHANGE_ADVERSARIAL_MONITORING = REQUIRED
ROOT_CAUSE_BEFORE_FIX = REQUIRED
DISPOSABLE_ONE_VARIABLE_PROBE_BEFORE_ACTIVE_BOOT_FIX = REQUIRED_FOR_CURRENT_BLOCKER
```

## Godot AI execution route

```text
GODOT_VERSION = 4.7.1-stable
GODOT_AI_PLUGIN_VERSION = 3.1.4
GODOT_AI_SERVER_VERSION = 3.1.4
OMENWARD_EDITOR_SETTINGS = SELF_CONTAINED_ISOLATED
OMENWARD_GODOT_AI_HTTP_PORT = 8002
OMENWARD_GODOT_AI_WS_PORT = 9502
CODEX_INSTALLATION = SHARED
OMENWARD_CODEX_HOME = C:/Users/user/.codex-omenward
SESSION_ID_FRESH_RESOLVE_EACH_EXECUTION_BLOCK = REQUIRED
PERSISTENT_GODOT_AUTHORING = HIGODOT_ONLY
GUT_AUTHORITY = DETERMINISTIC_GDSCRIPT_TESTS
HERA_AUTHORITY = POST_GREEN_LIVE_QA_OBSERVABILITY_ONLY
```

Historical session/PID evidence is not a future selector. Every local mutation block must fresh-list and match the exact OMENWARD project/session identity before mutation.

## Product canon retained

```text
OMW-DEC-20260811-PLANNING-WHOLE-PROJECT-CONTENT-CLOSURE-V1
OMW-DEC-20260811-PLANNING-QUALITY-GUARDRAILS-V1
OMW-DEC-20260811-PLANNING-ELITE-WAVE-BOSS-CADENCE-V1
DANGER_STAGE_TYPE = REMOVED
ELITE_ESCALATION = EVERY_STAGE_FINAL_WAVE
BOSS_STAGES = 5 / 10 / 15 / 20
BOSS_STAGE_FINAL_WAVE_ELITE_REQUIRED = TRUE
LEGACY_DANGER_STAGES_4_9_14_19 = SUPERSEDED_FOR_CURRENT_CADENCE
```

## Resume-first handoff locator

This Active Context is the current resume router for the paused runtime diagnostic. `docs/HANDOFF_CONTEXT.md` remains an older planning snapshot and must not override this file or fresh GitHub/Sheet truth for Issue #176 continuation.

Resume read order:

1. fresh OMENWARD main and PR #175/#177 state;
2. fresh Base main/current operating contract;
3. Google Sheet project hub;
4. this `ACTIVE_CONTEXT.md`;
5. `CURRENT_IMPLEMENTATION_STATUS.md`;
6. PR #175 / Issue #176 latest discussion and local diagnostic output;
7. fresh local Git/HiGodot identity only when local execution resumes.

## Release-deferred items

```text
PLATFORM_SAVE_EXPORT_STORE = RELEASE_PHASE_DEFERRED_FOR_PR175
SHARED_SAVE_SCHEMA = NOT_STARTED
EXPORT_PRESETS = ABSENT
```

These are not the current Issue #176 boot blocker.
