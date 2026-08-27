# OMENWARD · Target Screen Surface & Visual Coverage Audit

```yaml
audit_id: OMW-SCREEN-VISUAL-COVERAGE-20260827-01
github_issue: 227
status: SCREEN_INVENTORY_HANDOFF_READY
scope: CURRENT_RUN_COMMAND_VERTICAL_SLICE
screen_inventory_contract: GAME_SCREEN_SURFACE_INVENTORY_AND_VISUAL_ASSET_MATRIX
canonical_visual_coverage_owner: GAME_VISUAL_ASSET_COVERAGE_CHECKLIST
image_generation: FORBIDDEN_BY_THIS_AUDIT
runtime_evidence_ceiling: PARTIAL__TECHNICAL_MACHINE_QA_ONLY
human_player_evidence: NOT_RUN
```

## 1. Purpose and authority boundary

This is a screen-first companion audit, not a second GDD or asset manifest. It traces the current target build from the player-visible surface to the actual Godot consumer, then links existing assets, references, evidence, and bounded gaps.

The current visual decision remains `OMW-PLAN-20260825-FRONT-STATE-MINIMAP-SD-FANTASY-01`; `OM-IMG-023` remains its approved direction reference. Runtime truth remains the current `main` scenes, scripts, asset manifests, and execution evidence.

```text
SCREEN_SURFACE_INVENTORY_FIRST
→ actual consumer check
→ SCREEN_DESIGN_REFERENCE / RUNTIME_COMPONENT_ASSET / GODOT_UI distinction
→ gap = requirement or defer, never automatic image production
```

## 2. Target player flow recovered from actual implementation

```text
Godot bootstrap
→ tutorial stage starts automatically
→ RunCommandScreen / PREPARE
→ STOPPED_3X3 / MANIPULATE / RESULT_CONFIRM
→ COMMIT
→ BATTLE
→ REVIEW
→ retry current stage
```

`scenes/main/main.tscn` instantiates `Battlefield`, `RunCommandScreen`, hidden `StageHud`, and hidden `StageSelect`. `GameSession` starts `tutorial_stage` directly. Therefore Stage Select is not part of the current default player path even though its scene exists.

## 3. Screen inventory and screen-to-asset coverage matrix

| ID | Priority / surface | Player goal and question | Actual consumer | Existing visual modes and evidence | Coverage and bounded follow-up |
| --- | --- | --- | --- | --- | --- |
| `SCR-BOOT-01` | P0 / boot-to-tutorial transition | Enter the scoped slice without an unexplained stall. | `project.godot` → `scenes/main/main.tscn`; `GameSession._ready()` starts tutorial. | Engine boot/default clear color; no project-owned boot/loading scene or asset. | `NOT_APPLICABLE_FOR_CURRENT_TARGET_BUILD`: no separate boot/loading surface is implemented or required by the approved slice. Do not generate a splash or loading image from this row. |
| `SCR-RUN-PREPARE-01` | P0 / Run Command PREPARE | “다가오는 징조를 보고 무엇을 준비할까?” Build, inspect resources, and begin the stopped board. | `scenes/ui/run_command_screen.tscn` `TopBar`, `Fronts`, `LowerDeck/PreparePanel`; `scripts/ui/run_command_screen.gd`. | Godot panels/text; approved building button thumbnails; approved gold/troop indicators; three front context panels; `OM-IMG-023` is direction reference only. Machine QA captured the surface at 960/1280/1920. | `PARTIAL_TECHNICAL_COVERAGE`: layout/import evidence exists, but a human-readable completed composition comparison is not established. Existing consumer work is complete for this audit; no new bitmap requirement is inferred. |
| `SCR-RUN-ROULETTE-01` | P0 / stopped board, manipulation, result confirmation | “3×3 징조를 조정할까, 지금 결과를 볼까?” | `RunCommandScreen/LowerDeck/RoulettePanel`, `scripts/ui/run_command_screen.gd`; `StageRun` phase owner. | Existing approved local board frame, arrow, omen device, empty/gold/state/token assets recorded by `docs/images/approved/OMENWARD_RUN_COMMAND_VISUAL_ASSET_MANIFEST_2026-08-27.json`; Godot UI/text layers provide state and costs. Machine QA verified the full 3×3 and 12 controls. | `COVERED_EXISTING_FOR_SCOPED_SLICE`: preserve the asset manifest as the runtime asset owner. A focus-screen reference may use a Godot capture; it does not require a generated UI image. |
| `SCR-RUN-COMMIT-01` | P0 / irreversible deployment confirmation | “획득 병력을 어느 전선에 되돌릴 수 없게 보낼까?” | `RunCommandScreen/LowerDeck/CommitPanel`; `StageRun.confirm_pending_deployment()`. | Godot `OptionButton`, labels, existing token/unit identity assets, actual phase and transaction contracts. | `PARTIAL_TECHNICAL_COVERAGE`: component consumer and atomic behavior exist. A complete player-facing composition/reference for assignment, warning, and confirm hierarchy is not yet captured; use a future runtime capture first. |
| `SCR-RUN-BATTLE-01` | P0 / combat observation | Read three fronts and their local context while battle advances. | `scenes/battle/battlefield.tscn`; `scripts/battle/battlefield_view.gd`; `RunCommandScreen/Fronts` and `BattlePanel`. | Approved idle unit cells are actual `UnitView` textures. Battlefield ground, gates, outposts, and front context are current procedural graybox/Godot controls. Three panel/minimap areas were technically visible in machine QA; natural BATTLE→REVIEW runtime is not captured. | `GAP_BLOCKING_VISUAL_RUNTIME_VALIDATION`, not an image-production request: obtain a bounded natural runtime capture and compare actual three-front hierarchy/minimap context against current visual direction. No terrain, minimap, VFX, or new unit image is authorized by this audit. |
| `SCR-RUN-REVIEW-01` | P0 / factual result and retry | “이번 설계와 배치가 만든 결과를 복기한다.” | `RunCommandScreen/LowerDeck/ReviewPanel`; `StageRun` enters REVIEW from actual result. | Godot UI/text and retry control; headless phase contract covers outcome transition. | `GAP_BLOCKING_CORE_LOOP_VISUAL_VALIDATION`: current panel states intent but no captured long-form player-facing causal review. First required deliverable is runtime evidence and a text/UI requirement decision, not a raster image. |
| `SCR-STAGE-SELECT-01` | P1 / stage selection | Choose tutorial or regular stage when this becomes a player entry point. | `scenes/ui/stage_select.tscn`, but node is `visible = false` in main and the tutorial starts automatically. | Godot panel/button text only. | `NOT_APPLICABLE_FOR_CURRENT_DEFAULT_FLOW`: retained development/alternate surface. Do not add map, title, or selection art until a current player entry decision makes it a consumer. |
| `SCR-TITLE-MENU-01` | P2 / main title, continue, safe exit | Start, continue, and reach settings in a full product build. | No scene, route, or controller consumer found. | No project title/menu assets or runtime evidence. | `DEFERRED_BY_NO_ACTUAL_CONSUMER`: explicit non-applicability prevents an invented title-image queue. |
| `SCR-SAVE-LOAD-01` | P1 / profile and save/load | Select or recover a run safely. | No player-facing scene or active route found. Platform save adapter is not a player UI consumer. | No screen reference or runtime evidence. | `DEFERRED_BY_NO_ACTUAL_CONSUMER`. |
| `SCR-PAUSE-SETTINGS-01` | P1 / pause, audio, display, input, accessibility | Pause safely and adjust the application. | No pause/settings scene, input route, or player-facing consumer found. | No screen reference or runtime evidence. | `NOT_APPLICABLE_FOR_CURRENT_TARGET_BUILD`; do not infer a settings icon, menu, or artwork. |
| `SCR-ERROR-RECOVERY-01` | P1 / recoverable loading, bootstrap, or save error | Understand failure and choose a safe recovery action. | Bootstrap reports errors programmatically; no player-facing error surface found. | Engine diagnostics only. | `DEFERRED_BY_NO_ACTUAL_CONSUMER`: future failure UX needs a separate product/implementation decision. |

### Composition and technical reading rules

- `OM-IMG-023` is a single approved battlefield direction reference. It does not promote its embedded copy, exact UI geometry, or a full-screen mockup into a runtime texture.
- `SCR-RUN-ROULETTE-01` is served by actual approved raster derivatives. `SCR-RUN-PREPARE-01`, `SCR-RUN-COMMIT-01`, and `SCR-RUN-REVIEW-01` principally use Godot UI and text layers.
- `SCR-RUN-BATTLE-01` uses actual unit sprites plus procedural battlefield rendering. A graybox is not evidence that final readability, art fit, or a human experience pass exists.
- Hidden or absent scenes are recorded explicitly rather than being converted into speculative asset work.

## 4. Screen design reference queue

| Queue ID | Surface | Deliverable | Status and gate |
| --- | --- | --- | --- |
| `SCREEN-REF-01` | BATTLE → REVIEW | A bounded Godot runtime capture from natural battle outcome through Review, at the approved target resolutions. | `REQUIRED_FOR_VALIDATION`; no bitmap generation. It must preserve `NOT_RUN` human/player evidence. |
| `SCREEN-REF-02` | COMMIT | One runtime capture that shows assignment choices, irreversible warning, and primary confirm hierarchy with an actual pending reward. | `REQUIRED_FOR_SCREEN_COMPOSITION_CHECK`; no asset work until the capture proves a specific need. |
| `SCREEN-REF-03` | PREPARE | Compare a current Godot capture against the protected hierarchy of `OM-IMG-023`: three front contexts primary, compact lower deck secondary. | `REQUIREMENT_LINKED`; existing approved reference is reused. |
| `SCREEN-REF-04` | title / save-load / pause-settings | No reference deliverable. | `DO_NOT_GENERATE` until a player-flow decision creates an actual consumer. |

## 5. Runtime asset family queue

| Family | Current disposition | Consumer boundary |
| --- | --- | --- |
| Roulette workbench and tokens | `COVERED_EXISTING` | Existing manifest-local derivatives only; no duplicate sheet or generation. |
| Unit idle identity cells | `COVERED_EXISTING_FOR_CURRENT_CONSUMER` | `UnitView` uses approved local assets. Animation/state expansion remains governed by the unit production contract, not this audit. |
| Building thumbnails and HUD indicators | `COVERED_EXISTING_FOR_CURRENT_CONSUMER` | Current Prepare buttons and top resource indicators only. |
| Battlefield terrain, gates, outposts, front context, minimap visuals | `REQUIREMENT_LINKED_AFTER_RUNTIME_CAPTURE` | Current consumer is procedural graybox. Decide implementation mode after `SCREEN-REF-01`, not by generating a generic background or minimap sheet. |
| Review causal summary | `GODOT_UI_AND_TEXT_REQUIREMENT` | No new image file required by current evidence. |
| Title, save/load, settings, error UI | `DO_NOT_GENERATE` | No actual current consumer. |

## 6. Correction log and adversarial review

| Pass | Test | Result / correction |
| --- | --- | --- |
| 1 | Asset list could hide missing whole screens. | Corrected by inventorying boot, default route, five Run Command states, stage select, title, save/load, pause/settings, and error recovery. |
| 2 | Hidden or legacy scene might be counted as a player surface. | Corrected: `StageSelect` is explicitly hidden and tutorial auto-starts; it is not P0 flow coverage. |
| 3 | A direction mockup might be treated as runtime art. | Corrected: `OM-IMG-023` remains a screen direction reference; runtime assets, Godot UI, and procedural draw are separately named. |
| 4 | Technical capture might be promoted to human readability. | Corrected: 960/1280/1920 and bounded input checks are retained as technical only; BATTLE→REVIEW and human/player evidence remain unverified. |
| 5 | A coverage gap might become an unauthorized image queue. | Corrected: all gaps route to runtime capture, Godot UI/text requirement, future decision, or defer. This audit authorizes no image generation or asset promotion. |

## 7. Implementation handoff boundary

No code change is required to make this audit true. The next safe implementation-facing package is only `SCREEN-REF-01`: run the existing project long enough to reach a natural result, capture the BATTLE→REVIEW transition, then compare front-state/minimap/review readability against this audit and `OM-IMG-023` without changing product code.

Before any visual implementation beyond the current consumer, the task must state exact files, expected implementation mode (`GODOT_UI`, `PROCEDURAL_DRAW`, `RASTER_IMAGE`, or `SHADER`), acceptance criteria, and runtime validation. A missing reference or asset is not authorization to generate images.

## 8. Readback checklist

- Repository owner: this file, `docs/ACTIVE_CONTEXT.md`, and `docs/DOCUMENT_LIFECYCLE_REGISTRY.md`.
- Human-facing destination: Notion Home receives a concise screen-first audit pointer and the same evidence/generation boundary.
- Current main and Notion must be read back after merge/update; open PRs #205, #209, and #212 remain out of scope and read-only.
