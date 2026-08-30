# OMENWARD Close Single-Front Battlefield Runtime Technical Smoke

```yaml
executed_at: 2026-08-31 KST
status: RUNTIME_TECHNICAL_SMOKE_PASS__HUMAN_NOT_RUN
project_revision: codex/full-godot-implementation-20260830__working_tree
editor: Godot_4.7.2_stable
runtime_surface: scenes/main/main.tscn::RunCommandScreen
renderer_boundary_capture: docs/qa/captures/close_battlefield/omenward_close_battlefield_single_renderer_runtime_960x540.png
renderer_boundary_capture_sha256: 174e36e02de371200d19259a99c740ecb123d1ddad865839c9cc94713904d0c7
renderer_boundary_capture_status: HISTORICAL__PRE_STANDALONE_CLASH_MARKER_REMOVAL
latest_runtime_probe: GODOT_4_7_2_GAME_HELPER__BATTLE_STATE__2026-08-31_KST
latest_runtime_probe_persistent_capture: NOT_RETAINED
```

## Executed player-flow fixture

1. Started the existing tutorial stage.
2. Used deterministic roulette spin seed `4`; the live UI reported
   `중앙 판정: unit · 완성선 1`.
3. Confirmed the result, committed the produced Shield Guard, and selected the
   `전선` tab.
4. Observed `BATTLE`, `병력 1/12`, `BattleFocusViewport.visible = true`,
   `MarchMinimap.visible = true`, and root legacy `Battlefield.visible = false`
   in the running game tree.

## Captured technical observations

| Check | Observation | Result |
| --- | --- | --- |
| Battle surface | `BattleFocusViewport = x16, y62, 686×302` | PASS |
| Context surface | `MarchMinimap = x712, y62, 230×302` | PASS |
| Live field contents | Foundation + six edge props + one fixed tower + one live Lumern unit; no map building, construction node, or pad | PASS |
| Active renderer boundary | Root legacy `Battlefield` is hidden and no longer bound; only `BattleFocusViewport` renders the close battlefield | PASS |
| Unit corridor | The central grass corridor remains free of the prop rectangles; source contract independently rejects a central-band faction violation, either faction rectangle crossing the full side boundary, and a `y=0.36..0.80` travel-corridor violation before drawing | PASS (technical) |
| Standalone marker | The post-cleanup live `BATTLE` probe contains no standalone central clash-circle marker; a focused headless contract forbids `_draw_clash_focus` | PASS (technical) |
| Historical capture quality | 960×540, nonblank, no possible clipping, low-detail false | PASS |

The capture contains one friendly unit and no Veil unit because the early-stage
runtime fixture had not yet spawned an opposing wave. It proves the approved
asset binding and single-front field composition in a real `BATTLE` state; it
does not prove multi-unit battle readability or player usability.

## Evidence boundary

```text
GODOT_RUNTIME_TECHNICAL_SMOKE = PASS
MACHINE_CONTRACTS = PASS
HUMAN_READABILITY = NOT_RUN
PLAYER_USABILITY = NOT_RUN
MULTI_UNIT_COMBAT_READABILITY = NOT_RUN
DEVICE_RESOLUTION_COVERAGE = NOT_RUN
RELEASE_RIGHTS_REVIEW = PENDING
```

The stored renderer-boundary capture remains historical technical evidence;
it predates removal of the standalone clash-circle marker. The latest marker
removal probe was executed against an actual `BATTLE` state but is not retained
as a repository capture. It proves technical execution only and does not add
human-readability evidence.
