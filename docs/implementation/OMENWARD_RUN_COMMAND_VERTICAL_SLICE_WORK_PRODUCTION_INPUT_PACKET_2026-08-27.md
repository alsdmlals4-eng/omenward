# OMENWARD Run Command Vertical Slice · Work Production Input Packet

```yaml
slice_id: OMW-SLICE-20260827-RUN-COMMAND-01
issue: 208
baseline: 2169004bab375b7ce54651888afcdfa94b21520b
approval_reference: USER_CONTINUOUS_APPROVAL__RECOMMENDED_PLAN__AUTO_EXECUTE_AND_COMMIT
work_mode: BUILD
readiness: READY_FOR_SINGLE_CODEX_WINDOW
human_qa: DEFERRED_BY_USER
```

## Player outcome

The tutorial becomes one player-facing command flow. The player can inspect three fronts, prepare with the existing construction options, pay for one honest stopped 3×3 roulette result, use limited direct row/column moves, confirm the result, choose fronts for the acquired troops, make one irreversible atomic deployment, observe battle, and read a factual review.

```text
PREPARE → STOPPED_3X3 → MANIPULATE → RESULT_CONFIRM → COMMIT → BATTLE → REVIEW
```

## Exact scope

- Add one `StageRun`-owned Run Command phase state and snapshot. The existing combat, economy, roulette resolution, and deployment services stay their own authorities.
- Add a paid stopped-board roulette session: 3×3 board, 12 direct arrows, preview without spend, limited irreversible executed moves, and separate result confirmation.
- Add editable pending lane assignments and one aggregate preflight/atomic deployment confirmation. A rejected confirmation leaves economy, deployed cards, battle spawns, and input log unchanged.
- Pause wave/combat/economy advancement outside `BATTLE`; transition to `REVIEW` only from an actual stage outcome.
- Add a default player-facing `RunCommandScreen` while preserving `StageHud` as a hidden technical/evidence surface.
- Render all three front contexts concurrently, with one compact progress/stronghold/route minimap per front. Minimap data is contextual only: no unit-by-unit replication or combat-VFX duplicate.
- Export and bind only the approved local roulette visual inputs listed below. Existing approved unit cells remain the troop visual source.

## Explicit exclusions

- No new game economy/balance values, stage content, 20-stage conversion, tactical actions, audio, VFX, save migration, or controller PASS.
- No three-reel-to-three-lane binding, automatic lane deployment, fake near-miss, jackpot/gambling language, or player UI calculation of canonical game rules.
- No change to the debug `StageHud` semantics or existing test contracts beyond necessary phase-aware compatibility.
- No new image generation. This slice uses approved, locally stored sources only.

## Approved visual inputs and local derivatives

| Player consumer | Approved cleanup master | Runtime derivative | Contract |
|---|---|---|---|
| Roulette board | `.asset-vault/library/ui/roulette/masters/OMENWARD_ASSET_ROULETTE_BOARD_FRAME_V1_CLEANUP_MASTER_V1.png` | `assets/art/ui/run_command/roulette_board_frame.png` | nearest-neighbour, transparent RGBA, 180×180 |
| Direction arrows | `.asset-vault/library/ui/roulette/masters/OMENWARD_ASSET_ROULETTE_ARROW_V1_CLEANUP_MASTER_V1.png` | `assets/art/ui/run_command/roulette_arrow.png` | nearest-neighbour, transparent RGBA, 28×28; UI rotates it |
| Omen device anchor | `.asset-vault/library/ui/roulette/masters/OMENWARD_ASSET_OMEN_DEVICE_V1_CLEANUP_MASTER_V1.png` | `assets/art/ui/run_command/omen_device.png` | nearest-neighbour, transparent RGBA, 72×76 |
| Empty / Gold / token frame / state | approved token cleanup masters in `.asset-vault/library/ui/tokens/masters/` | `assets/art/ui/run_command/token_{x,gold,frame,state}.png` | nearest-neighbour, transparent RGBA, 34×34 |

The source masters are already user-approved under `OMW-ASSET-AUTO-APPROVAL-20260826-P0-REMAINDER-V1` and are locally retained. The derivative manifest records each input/output SHA-256 and local path. Notion retains the approval/provenance record; no binary-upload claim is made unless an actual Notion attachment exists.

## Existing code reuse

| Existing owner | Reuse disposition | Slice role |
|---|---|---|
| `StageRun` | ADAPT | sole orchestration owner and phase gate |
| `RouletteService.resolve_board_snapshot()` | REUSE | canonical stopped-board result calculation after confirmation |
| `DeploymentService` | ADAPT | batch preflight and atomic deployment application |
| `BattleSimulator`, `WaveDirector`, `StageEconomy` | REUSE | run only during `BATTLE` |
| `core_ux_snapshot()` | REUSE | forecast and factual review projection |
| `StageHud` | REFERENCE_ONLY | preserved debug/evidence receiver, not player default |
| existing unit runtime cells | REUSE | troop identity in battlefield rendering |

## Before and after

| Concern | Before | After |
|---|---|---|
| Player flow | technical HUD mixes spin, deployment, debug readouts, and live simulation | one visible phase question and one primary progression action |
| Roulette | spin resolves and grants immediately | paid stopped board → move preview/execute → result confirm |
| Deployment | next reward may be individually deployed through three abstract buttons | staged front assignments → aggregate preflight → atomic irreversible confirm |
| Battle timing | simulation runs continuously | only `BATTLE` advances time |
| Front context | one technical battlefield surface | three concurrent front-state summaries with compact minimaps |

## Acceptance criteria

1. Valid tutorial path completes `PREPARE → STOPPED_3X3 → MANIPULATE → RESULT_CONFIRM → COMMIT → BATTLE → REVIEW`; phase skips and invalid actions reject without mutation.
2. The board is always 3×3 and exposes 12 direct arrows. Preview does not consume a move; an executed move does, and cannot be undone/reset in the same session.
3. Paid spin spends exactly once. Confirming a board resolves via the existing central-row judgment and existing reward rules; it never auto-selects a lane.
4. COMMIT supports at least one pending reward; failed aggregate capacity or spawn preflight leaves every relevant mutable state unchanged. Success writes deterministic assignment/deployment input-log entries.
5. The player default screen has three simultaneous front contexts, three readable compact minimaps, the lower control deck as a secondary surface, and the 3×3/12-arrow workbench only in the roulette phase.
6. All listed runtime assets are local, imported by Godot, alpha-safe, and recorded in a deterministic manifest/run record.
7. Focused RED is observed before implementation; focused GREEN, current headless regression suite, Godot import/parse, deterministic replay comparison, and live tutorial smoke are run after implementation.
8. Human/player usability, controller, final resolution accessibility, performance, and release evidence remain `NOT_RUN` unless separately observed.

## Validation and rollback

- Run the focused phase/transaction/UI contract tests first and record RED before adding implementation.
- Validate Godot import and run the deterministic headless suite after each coherent implementation increment.
- Use read-only live Godot/Hera inspection for the tutorial at 960×540, then capture available 1280×720 and 1920×1080 evidence without persistent authoring through the live tool.
- Rollback is limited to the new Run Command screen, phase/session seams, batch deployment seam, runtime derivatives, focused tests, and this slice documentation. No data migration is introduced.

## Known evidence ceiling

The repository currently has partial technical live captures for unit gallery, building buttons, and resource indicators. They are not proof of this new Run Command flow. This slice cannot claim human comprehension, visual readability at every target resolution, controller accessibility, performance, or final product readiness without the corresponding execution evidence.
