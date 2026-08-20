# [현행] Active Context

```yaml
updated_at: 2026-08-20
current_branch: main
current_main: RESOLVE_FROM_REPOSITORY_DEFAULT_BRANCH
planning_contract: PROJECT_TOTAL_PLANNING_IMPLEMENTATION_AND_DELIVERY_INSTRUCTION_v4.7
work_phase: PHASE_A_GPT_CHAT_REPLANNING_VISUAL_DEFERRED_USER_REFERENCE
planning_status: REOPENED_REVIEW_IN_PROGRESS
current_decision_index: docs/CURRENT_CONFIRMED_DECISIONS.md
current_decision: OMW-PLAN-20260820-RUN-COMMAND-SHELL-01
current_visual_inventory: docs/design/OMENWARD_VISUAL_REQUIREMENT_INVENTORY_2026-08-20.md
current_next_gate: USER_REFERENCE_VISUAL_UPLOAD_THEN_REVIEW
implementation_authorized: false
current_chat_runtime_status: NOT_RUN
human_player_evidence: NOT_RUN
```

Current main SHA는 이 문서에 고정하지 않고 repository default branch에서 fresh resolve한다. 이 파일은 2026-08-20 재기획 흐름의 현재 상태를 소유하며 2026-08-11~12의 Phase C/PR175 실행 지시는 역사 상태로만 보존한다.

## Current planning phase

```text
PROJECT_STATE_RECOVERED = TRUE
PLANNING_REOPENED_BY_USER = TRUE
CURRENT_APPROVED_REPLAN_DECISIONS = 6
WORLD_ROLE = CONFIRMED
MAPRUN_WORLD_MEANING = CONFIRMED
PRESSURE_LANGUAGE = CONFIRMED
MOBILIZATION_REGISTRY_WORLD_MEANING = CONFIRMED
FIRST5_FTUE_MASTERY_LADDER = CONFIRMED
RUN_COMMAND_SCREEN_FOCUS_MODES = CONFIRMED
VISUAL_REQUIREMENT_INVENTORY = COMPLETE_PROPOSED
VISUAL_NORTH_STAR_SELECTION = OPTION_A_APPROVED
VISUAL_GENERATION = DEFERRED_PENDING_USER_REFERENCE_FILES
VISUAL_GENERATED_CANDIDATE = REJECTED_NOT_CANON
VISUAL_APPROVED_ASSET = NONE
IMPLEMENTATION_START = NOT_AUTHORIZED
```

Current recovery owner:

`docs/CURRENT_CONFIRMED_DECISIONS.md`

Current Decision owners:

- `docs/design/APPROVED_OMENWARD_WORLD_ROLE_AND_OMEN_WARD_IDENTITY_2026-08-20.md`
- `docs/design/APPROVED_OMENWARD_OMEN_CYCLE_MAPRUN_WORLD_2026-08-20.md`
- `docs/design/APPROVED_OMENWARD_PRESSURE_LANGUAGE_AND_OMEN_SIGNATURES_2026-08-20.md`
- `docs/design/APPROVED_OMENWARD_MOBILIZATION_REGISTRY_AND_TRIPLE_OMEN_WHEELS_2026-08-20.md`
- `docs/design/APPROVED_OMENWARD_FIRST5_FTUE_MASTERY_LADDER_2026-08-20.md`
- `docs/design/APPROVED_OMENWARD_RUN_COMMAND_SCREEN_FOCUS_MODES_2026-08-20.md`
- `docs/ONBOARDING_PLANNING_CURRENT_AUTHORITY.md`

Current Visual planning owner:

- `docs/design/OMENWARD_VISUAL_REQUIREMENT_INVENTORY_2026-08-20.md`

## Current product promise

```text
징조 관측
→ 건설 / 동원 인장 / 미래 병력 분포 설계
→ 세 징조륜에서 병력 획득
→ 세 전선 중 하나에 비가역 커밋
→ 자동전투 + 결정적 순간의 수동 전술
→ 인과 복기
→ 다음 설계
```

Player role:

`징조수호관(Omen Warden)`

Run world meaning:

`one Ward Citadel + one 20 Stage Omen Cycle`

Pressure language:

`MASS / ARMORED / FLYING / INFILTRATION / SIEGE = Omen Signature, not enemy race/faction`

Player-facing Run shell:

`PREPARE → COMMIT → BATTLE → REVIEW`

## First-session current truth

```text
FIRST_SESSION = REAL_MAPRUN
STAGE_1_REQUIRED_T1 = VAULT / FARM / GENERAL_BARRACKS / DEFENSE_TOWER / COMMAND_POST / MANA_TOWER
SPECIAL_BARRACKS_STAGE1_REQUIRED = FALSE
FIRST_ROULETTE_UNLOCK = AFTER_ALL_SIX_T1_AND_SETUP_CONFIRMATION
STAGE_1 = CAUSAL_UNDERSTANDING
STAGE_2 = FUTURE_DISTRIBUTION_MODIFICATION
STAGE_3 = TACTICAL_INTERVENTION
STAGE_4 = APPLICATION_WITH_NO_NEW_CORE_SYSTEM
STAGE_5 = FIRST_BOSS_AND_BUILD_REVIEW
```

Stage 1의 6개 필수 T1은 현재 유지하지만, `생존 기반 → 군사 기반 → 지휘 기반` 세 묶음으로 순차 학습한다. release-near Vertical Slice 사람 플레이에서 과부하가 실제 관측되면 필수 건물 축소안을 최우선 재검토한다.

## Current GitHub work-item truth

Fresh 2026-08-20 readback:

```text
PR175 = CLOSED_UNMERGED
PR177 = CLOSED_UNMERGED_REFERENCE_HISTORY
ISSUE176 = OPEN_HISTORICAL_FOLLOWUP_PACKET_REQUIRES_RECONCILIATION_BEFORE_ANY_NEW_IMPLEMENTATION
PR197 = OPEN_DRAFT_OTHER_WORKSTREAM_READ_ONLY
```

### PR #175

`[Runtime] Implement barracks role-output behaviors and FV evidence`

- closed on 2026-08-18
- merged = false
- historical implementation/evidence only
- none of its unmerged runtime changes are current main product truth

### PR #177

`[Handoff] Persist PR175/Issue176 pause and resume state`

- closed on 2026-08-18
- merged = false
- reference/historical handoff only

### Issue #176

Issue remains open and still describes seven historical role-output/FV gaps under the old PR175 package. Because its parent implementation PR is now closed/unmerged and the project has reopened planning, **do not execute it blindly**. Before any future implementation work, reconcile it against then-current main, current planning Decisions, and current implementation scope.

### PR #197

`feat: pilot reusable candidate draft engine`

- OPEN / DRAFT
- head: `feat/p0-draft-ui-symbol-pilot-20260820`
- current workstream is read-only from this planning chat
- do not modify, retarget, merge, or use its unmerged changes as current product truth

## Runtime and evidence boundary

The 2026-08-11~12 signal11/HiGodot isolation records remain historical evidence. This 2026-08-20 replanning chat has **not executed current Godot runtime**.

```text
CURRENT_GODOT_RUNTIME = NOT_RUN
CURRENT_WINDOWS_RUNTIME = NOT_RUN
CURRENT_UI_EVIDENCE = NOT_RUN
CURRENT_HUMAN_USABILITY_EVIDENCE = NOT_RUN
CURRENT_PLAYER_EXPERIENCE_EVIDENCE = NOT_RUN
FINAL_PARAMETER_VECTOR = NOT_SELECTED
FINAL_PRODUCT_NUMERICS = NOT_APPROVED
```

Do not state that the old signal11 crash is currently reproduced. If implementation/runtime work resumes later, fresh current-main execution determines the new runtime truth.

## Protected mechanics

```text
ROULETTE_IDENTITY = PLAYER_CONSTRUCTED_PROBABILITY_ENGINE
GAMBLING_FANTASY_POSITIONING = FORBIDDEN
PAID_SPIN = FORBIDDEN
FORECASTED_PRESSURE_MULTIPLE_RESPONSE_AXES_REQUIRED = TRUE
RNG_CAN_REMOVE_ALL_VALID_RESPONSES = FORBIDDEN
AUTO_PRODUCTION_AND_TOKEN_SOURCE = SEPARATE_ACQUISITION_PATHS
TOKEN_INSTANCES_PER_REEL_PER_ACTIVE_SOURCE = 1
TOTAL_TOKEN_INSTANCES_PER_ACTIVE_SOURCE = 3
THREE_REELS_TO_THREE_LANES_FIXED_MAPPING = FORBIDDEN
IRREVERSIBLE_LANE_COMMITMENT = REQUIRED
BOSS_STAGES = 5 / 10 / 15 / 20
ELITE_ESCALATION = EVERY_STAGE_FINAL_WAVE
PRESCRIPTIVE_NEXT_BUILD_COMMAND = FORBIDDEN
```

## Current visual planning gate

Visual Requirement Inventory is complete and first North Star candidate selection A was approved, but **all image work is now deferred at the user's request until user-owned local mockup/reference files are provided**.

```text
APPROVED_FIRST_VISUAL_DIRECTION = OMW-VIS-001 / Stage 2 PREPARE · Omen Wheels Focus
GENERATED_CANDIDATE_2026_08_20 = REJECTED_NOT_CANON
REJECTION_REASON = requested stronger dot/pixel feeling was not materially reflected
PROMOTE_GENERATED_CANDIDATE_TO_NOTION_ASSET_LIBRARY = FORBIDDEN
NEXT_VISUAL_ACTION = WAIT_FOR_USER_REFERENCE_FILES
IMAGE_GENERATION_OR_EDIT_BEFORE_REFERENCE_UPLOAD = FORBIDDEN
```

When the user uploads the local files:

```text
user reference files
→ source-grounded review first
→ compare against current Visual Bible + Inventory
→ identify reusable layout / pixel-density / palette / UI language
→ propose exact revision target
→ resume image generation/edit only when the user explicitly requests it
→ approved result only to Visual Bible / Asset Library / Flow
```

Non-visual planning work may continue while this visual gate is deferred.

Inventory coverage retained:

```text
1. Run Command Screen North Star
2. PREPARE / Forecast + Build + Omen Wheel focus
3. COMMIT / spatial three-lane deployment
4. BATTLE / lane readability + tactical intervention
5. REVIEW / causal result explanation
6. Ward Citadel / three-lane battlefield visual identity
7. buildings / mobilization-seal visual language
8. troop silhouettes and pressure readability
9. Omen Signature icon system
10. first-five-stage teaching visual cues
```

## Work-entry process

```text
BENCHMARK_AND_INDUSTRY_RESEARCH_REQUIRED_BEFORE_IMPORTANT_DECISION = TRUE
MINIMUM_VIABLE_ALTERNATIVES = 3
ADVERSARIAL_REVIEW = REQUIRED_BEFORE_LONG_TERM_LOCK
NOTION_HUMAN_FACING_CANON = REQUIRED_FOR_HUMAN_VISUAL_FLOW_MEANING
REPOSITORY_STRUCTURED_CANON = REQUIRED_FOR_RULES_AND_IMPLEMENTATION_CONTRACTS
OPEN_DRAFT_OTHER_WORKSTREAM = READ_ONLY
HUMAN_EVIDENCE_NEVER_SYNTHESIZED = TRUE
```

## Resume-first handoff locator

Resume order:

1. fresh OMENWARD main;
2. `docs/CURRENT_CONFIRMED_DECISIONS.md`;
3. this `docs/ACTIVE_CONTEXT.md`;
4. `docs/design/OMENWARD_VISUAL_REQUIREMENT_INVENTORY_2026-08-20.md`;
5. Project Notion Home + `02 · 비주얼 바이블` + `03 · UI · 게임플레이 Flow Map` + `08 · 핵심 시스템 · 상세`;
6. user-provided visual reference files when available;
7. related open/draft PR inventory, with PR #197 protected/read-only unless its own workstream explicitly resumes;
8. actual code/data/scene/test truth only when implementation scope opens;
9. fresh current runtime evidence only when execution is explicitly resumed.

## Release-deferred items

PC/Steam remains the primary planning/validation target. Android/export/save/store integration remains deferred to the release-near stage unless a later user Decision reopens it.
