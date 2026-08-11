# [현행] OMENWARD Google Sheet 정본 동기화 계약

```yaml
updated_at: 2026-08-11
spreadsheet_id: 1VLwRtXGDtyj0JFt98wdIOtG6Zqc3wtdfCzSF9Fo6lpw
current_phase_decision: OMW-DEC-20260811-OPS-HIGODOT-PROJECT-ISOLATED-EDITOR-PORT-V1
canon_freshness_decision: OMW-DEC-20260811-OPS-CANON-FRESHNESS-V45-ROUTING-V1
sheet_sync_status: SAME_DECISION_REREAD_REQUIRED_BEFORE_RUNTIME_MUTATION
current_phase_focus: PR175_CURRENT_MAIN_REVALIDATION_NEXT
```

Compatibility/workspace identity:

```text
PROJECT_SHEET_CONFIGURED
USER_FACING_GDD_WORKSPACE
PROPOSED_SHEET_CHANGE
TRANSIENT_OPS_PR_STATE = FRESH_READ_ONLY_NOT_DURABLE_CANON
```

These markers identify the connected Sheet as the user-facing GDD workspace and preserve the existing change-proposal contract; approved truth still requires same-Decision-ID synchronization and readback.

## Rule

GitHub authority owner와 Google Sheet mirror는 승인된 결정에 대해 같은 Decision ID를 사용한다. 충돌하면 GitHub current lifecycle/Decision owner를 우선 확인하고 Sheet에 correction/audit/history를 남긴다. 과거 행을 현재 사실처럼 덮어쓰지 않는다.

Transient operations PR numbers/status are not durable current canon. They are fresh-read from GitHub when needed and may be recorded only as historical evidence after the fact.

## Current phase target

```text
USER_EXPLICIT_PLANNING_COMPLETE_DECLARATION = RECEIVED
PHASE_B_FINAL_PLANNING_REVIEW = PASS
IMPLEMENTATION_PACKAGE_DEFINITION_OF_READY = CLOSED
PHASE_C_GATE = OPEN
PHASE_C_C0_OVERALL = PASS
PR175_CURRENT_MAIN_REVALIDATION_NEXT
TRANSIENT_OPS_PR_STATE = FRESH_READ_ONLY_NOT_DURABLE_CANON
```

Current execution Decision:
`OMW-DEC-20260811-OPS-HIGODOT-PROJECT-ISOLATED-EDITOR-PORT-V1`

Current C0 owner:
`docs/reviews/PHASE_C_C0_LOCAL_HIGODOT_CLOSURE_2026-08-11.md`

Historical/preceding Phase B GitHub owner:
`docs/reviews/PHASE_B_FINAL_PLANNING_REVIEW_2026-08-11.md`

## Current product mirror

```text
OMW-DEC-20260811-PLANNING-WHOLE-PROJECT-CONTENT-CLOSURE-V1
OMW-DEC-20260811-PLANNING-QUALITY-GUARDRAILS-V1
OMW-DEC-20260811-PLANNING-ELITE-WAVE-BOSS-CADENCE-V1
DANGER_STAGE_TYPE = REMOVED
ELITE_ESCALATION = EVERY_STAGE_FINAL_WAVE
BOSS_STAGES = 5 / 10 / 15 / 20
BOSS_STAGE_FINAL_WAVE_ELITE_REQUIRED = TRUE
WHOLE_PROJECT_CONTENT_DECISION_GROUPS_OPEN = 0
```

## Barracks / physical token mirror

```text
GENERAL_T1_AUTO_PRODUCTION = BASIC_INFANTRY
GENERAL_T1_TOKEN_SOURCE = BASIC_INFANTRY
GENERAL_T2_AUTO_PRODUCTION = SELECTED_GENERAL_UNIT
GENERAL_T2_TOKEN_SOURCE = SELECTED_GENERAL_UNIT
SPECIAL_T1_SELECTION_TRIGGER = SUCCESSFUL_CONSTRUCTION_COMMIT
SPECIAL_T1_AUTO_PRODUCTION = SELECTED_RANDOM_SPECIAL_UNIT
SPECIAL_T1_TOKEN_SOURCE = SELECTED_RANDOM_SPECIAL_UNIT
SPECIAL_T2_AUTO_PRODUCTION = SELECTED_SPECIAL_UNIT
SPECIAL_T2_TOKEN_SOURCE = SELECTED_SPECIAL_UNIT
TOKEN_INSTANCES_PER_REEL_PER_ACTIVE_SOURCE = 1
TOTAL_TOKEN_INSTANCES_PER_ACTIVE_SOURCE = 3
FRACTIONAL_TOKEN_WEIGHT = FORBIDDEN
SPECIAL_T1_SELECTION_DISTRIBUTION = POST_RUNTIME_EVIDENCE_TUNING
```

## Runtime / evidence mirror

```text
PR175 = OPEN_DRAFT
ISSUE176_APPROVED_RUNTIME_GAPS = 7
ISSUE176_7_GAPS = IMPLEMENTATION_COMPLETENESS
PR175_CURRENT_MAIN_REVALIDATION_NEXT
PR175_MERGE = FORBIDDEN_UNTIL_RUNTIME_ACCEPTANCE
FINAL_PARAMETER_VECTOR = NOT_SELECTED
FINAL_PRODUCT_NUMERICS = NOT_APPROVED
PLATFORM_SAVE_EXPORT_STORE = RELEASE_PHASE_DEFERRED_FOR_PR175
SHARED_SAVE_SCHEMA = NOT_STARTED
EXPORT_PRESETS = ABSENT
```

## Godot AI mirror

```text
USER_REPORTED_GODOT_AI_CURRENT_VERSION = 3.1.4
GODOT_AI_3_1_4_C0_STATUS = VERIFIED_PLUGIN_SERVER_SESSION
GODOT_AI_HTTP_PORT = 8002
GODOT_AI_WS_PORT = 9502
GODOT_AI_SESSION_RESOLUTION = FRESH_EXACT_PROJECT_EACH_EXECUTION_BLOCK
```

Exact session IDs and editor PIDs are evidence only. They must not be reused as durable selectors.

## Historical Phase B pre-merge Sheet evidence

The same operational Decision ID was written and bounded-read back from:

- `00_프로젝트_허브!E2:L2`
- `01_작업순서!A73:N73`
- `02_현재_확정결정!A110:M110`
- `04_누락_충돌_감사!A642:H642`
- `50_메인콘텐츠!G302` and `J303`
- `99_변경이력!A191:H191`

```text
PHASE_B_PREMERGE_SHEET_SYNC = PASS
PHASE_B_PREMERGE_SHEET_REREAD = PASS
SHEET_AUDIT_ID = OMW-AUD-642
SHEET_CURRENT_DECISION_ID_AT_THAT_CHECKPOINT = OMW-DEC-20260811-OPS-PHASE-B-FINAL-PLANNING-REVIEW-V1
PRE_SHEET_SYNC_EXACT_HEAD = b468de04065bc181ec4300f1bfe52bc63c4b0ffd
PRE_SHEET_SYNC_EXACT_HEAD_ACTIONS = 13_OF_13_SUCCESS
```

This block is historical evidence, not current execution routing.

## C0 / post-change Sheet evidence lineage

Current Sheet truth preserves historical rows and supersedes them with the same current execution Decision:

```text
CURRENT_EXECUTION_DECISION = OMW-DEC-20260811-OPS-HIGODOT-PROJECT-ISOLATED-EDITOR-PORT-V1
PHASE_C_C0_OVERALL = PASS
HTTP_PORT = 8002
WS_PORT = 9502
SHEET_AUDIT_LINEAGE = OMW-AUD-645 / OMW-AUD-646 / OMW-AUD-647 / OMW-AUD-648
CURRENT_HISTORY_LINEAGE = 99 row194 / row195 / row196 / row197
PR193_MERGE_EVIDENCE = 7d421372c33c2d6a32ee3ef8bdb94ead333bc0c0
TRANSIENT_OPS_PR_STATE = FRESH_READ_ONLY_NOT_DURABLE_CANON
```

`PR193_MERGE_EVIDENCE` is historical closure lineage only. The current Sheet state must be bounded-reread immediately before runtime mutation; this document does not persist a transient operations PR as the current gate.

## Current sync rule

For current and later routing closures:

- keep historical rows unchanged,
- use the same approved Decision ID for current Sheet synchronization,
- resolve transient operations PR state from fresh GitHub rather than durable canon,
- bounded reread before every durable runtime transition,
- record merge/post-merge evidence in audit/history instead of turning temporary PR state into current routing.
