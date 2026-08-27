# Battlefield Map + Roulette Picker QA · 2026-08-28

```yaml
issue: 229
decision: OMW-VISUAL-20260828-BATTLEFIELD-MAP-ROULETTE-PICKER-01
scope: RUN_COMMAND_VERTICAL_SLICE_PRESENTATION_ONLY
technical_status: PASS
human_player_evidence: NOT_RUN
```

## Machine evidence

- `tests/headless/roulette_picker_ui_test.gd` passed after its red→green contract cycle.
- Godot headless editor import/parse completed without task-related parse errors.
- Hera ran `res://scenes/main/main.tscn` at 960×540 and captured PREPARE, STOPPED 3×3, and a changed inspected selection (`5 → 2`).
- Hera diagnostics for the live game reported `error_count = 0`, `warning_count = 0`.

## Visual technical check

| Criterion | Evidence | Status |
|---|---|---|
| Enlarged battlefield is primary | 0.66 backdrop scale; translucent front-state panels | PASS |
| Three forward bases / clash zones | Visible in the 960×540 PREPARE capture | PASS |
| Bypass routes | Forest/river/bridge routes visibly separate from the three main lanes | PASS |
| Roulette list visible | 3×3 compact selectable list is shown beside the board | PASS |
| Selection is UI-only | Selecting index 2 changes readout, not roulette rule data | PASS |

## Adversarial review

- Background is context only: no combat rule or lane-assignment state is read from image pixels.
- Board/list selection changes only `_selected_roulette_index`; movement, preview, result lock, reward, deployment, and combat callbacks remain owned by `StageRun`.
- The opaque background contains no UI/text/watermark and is stored with its hash/provenance record.
- Human play/readability and long-form battle evaluation remain `NOT_RUN`.

## Retained capture paths

- `artifacts/qa/battlefield-watercolor-enlarged-prepare.png`
- `artifacts/qa/roulette-picker-visible-list.png`
- `artifacts/qa/roulette-picker-selection-02.png`
