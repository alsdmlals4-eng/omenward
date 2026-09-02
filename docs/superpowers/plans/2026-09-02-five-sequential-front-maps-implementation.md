# Five Sequential Front Maps · Implementation Plan

> **Execution note:** follow the project-local approved-change validator, red-first contracts, full Godot/Python suite, live runtime smoke when the Omenward editor is available, exact PR-head CI readback, and safe temporary-worktree cleanup. Do not merge or modify protected main.

**Goal:** Convert the current five-sector context ribbon into a single sequential five-map campaign with a real per-map battle package, explicit next-map review action, and preserved single-front/global-roster boundaries.

**Architecture:** `FrontMapDefinition` resources own map identity, Korean label, terrain consumer key, and wave range. `StageDefinition` owns ordered front maps. `StageRun` owns sequential progression and constructs fresh `BattleSimulator`/`WaveDirector` state only at a map entry. The existing economy, building service, roulette service, deployment state, and one `front` ID endure through a map handoff. `MarchMinimapView` renders the `StageRun.front_map_snapshot()` rather than reverse-inferring progress from capture objectives.

## Task 1: Define actual map packages and red contracts

**Files:**
- Create: `scripts/data/front_map_definition.gd`
- Modify: `scripts/data/stage_definition.gd`
- Modify: `data/stages/regular_stage.tres`
- Modify: `scripts/core/bootstrap_validator.gd`
- Create: `tests/headless/five_sequential_front_maps_contract_test.gd`
- Modify: `tests/headless/stage_data_contract_test.gd`

- [x] Write the red test for five ordered regular map resources, W1–W4 through W17–W20 ownership, and a `front_map_snapshot()` with one current map only.
- [x] Add typed map data and make the bootstrap validator reject missing, duplicate, gapped, or non-five regular map packages.
- [x] Preserve the existing four-wave tutorial as an onboarding exception; it is explicit in data, not accidental array division.

## Task 2: Make StageRun progress map-by-map

**Files:**
- Modify: `scripts/core/stage_run.gd`
- Modify: `scripts/waves/wave_director.gd`
- Modify: `tests/headless/stage_run_test.gd`
- Modify: `tests/headless/c2_battle_objective_test.gd`
- Test: `tests/headless/five_sequential_front_maps_contract_test.gd`

- [x] Add `front_map_index`, `front_map_result`, `current_front_map()`, `front_map_snapshot()`, `can_enter_next_front_map()`, and `enter_next_front_map()`.
- [x] Bind only the current map's declared wave package. A cleared non-final map enters REVIEW, retains `RUNNING`, and does not call `progression.record_victory()`.
- [x] Recreate local battle/wave state at an explicit next-map handoff while preserving global economy/buildings/roulette/deployment ownership.
- [x] Make map 5 the only final victory path and keep defeat from opening future maps.

## Task 3: Render sequential state and transition CTA

**Files:**
- Modify: `scripts/ui/march_minimap_view.gd`
- Modify: `scripts/ui/battle_focus_view.gd`
- Modify: `scripts/ui/run_command_screen.gd`
- Modify: `scenes/ui/run_command_screen.tscn`
- Modify: `tests/headless/strategic_map_ui_contract_test.gd`
- Modify: `tests/headless/battle_primary_march_minimap_contract_test.gd`

- [x] Render cleared/current/locked cells from `StageRun`, retaining top-row, read-only, no-unit-replication behavior.
- [x] Give Review a distinct `다음 전선 진입` CTA for map 1–4 and keep retry for defeat/final review.
- [x] Have BattleFocus resolve a terrain key from the active map. Until separate map candidates are visually locked, show the existing approved foundation and label the requirement as pending; do not silently canonicalize candidate art.

## Task 4: Produce and review map terrain candidates

**Files:**
- Create: `docs/images/candidates/OMENWARD_FIVE_SEQUENTIAL_FRONT_MAP_CANDIDATES_2026-09-02.md`
- Create: five image-model output candidates in the documented candidate path
- Modify: `docs/design/APPROVED_OMENWARD_FIVE_SEQUENTIAL_FRONT_MAPS_2026-09-02.md`

- [x] Generate five independent candidate foundations from the blueprint’s exact visual requirement.
- [x] Record prompt/provenance, SHA-256, intended consumer, and status `GENERATED_CANDIDATE__AWAITING_USER_VISUAL_CONFIRMATION`.
- [x] Show the complete candidate set to the user. Do not replace the user-locked current modular foundation or bind a candidate as a canonical runtime asset before confirmation.

## Task 5: Reconcile canon and verify

**Files:**
- Modify: `docs/CURRENT_CONFIRMED_DECISIONS.md`
- Modify: `docs/ACTIVE_CONTEXT.md`
- Modify: `docs/OMENWARD_GDD_CURRENT_CANON.md`
- Modify: `docs/DOCUMENTATION_MAP.md`
- Modify: `docs/benchmarks/OMENWARD_SINGLE_FRONT_COMMAND_BENCHMARK_REVERSE_ENGINEERING_2026-09-01.md`
- Create: `docs/qa/OMENWARD_FIVE_SEQUENTIAL_FRONT_MAPS_RUNTIME_SMOKE_2026-09-02.md`

- [x] Run focused RED/GREEN scripts, then full Godot and Python suites and the Base validator against the exact adapter pin.
- [ ] Use live Omenward only to enter map 1, force/complete a map transition through real surface controls, and capture a technical smoke. Live entry capture passed; the regular-map handoff remains pending behind the intentionally retained tutorial unlock.
- [x] Perform five full-scope adversarial passes and update current owners. Commit/push and exact PR-head CI readback remain after the final clean verification.
