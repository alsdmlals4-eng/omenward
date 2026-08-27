# OMENWARD Run Command Machine QA · 2026-08-27

## Scope and evidence boundary

- **Baseline:** `origin/main` at `d0f1742e8b65781ba6513c2cfe0e3f1f55da447e` (`feat: add Run Command vertical slice (#225)`).
- **Engine:** Godot 4.7.1 on Windows, executed from an isolated QA worktree.
- **Purpose:** record machine-observed technical layout and interaction evidence for the approved Run Command vertical slice.
- **Not established by this record:** human/player readability, player experience, balance, or a natural full BATTLE → REVIEW run.

## Machine-observed results

| Check | Result | Evidence |
| --- | --- | --- |
| Approved interaction path | PASS (bounded) | Hera executed `PREPARE → STOPPED_3X3 → MANIPULATE → RESULT_CONFIRM → COMMIT → BATTLE` with mouse interaction. |
| Focused keyboard action | PASS (technical) | After `RowRight0.grab_focus()`, Godot action `ui_accept` changed `STOPPED_3X3` / 3 moves to `MANIPULATE` / 2 moves. |
| Three fronts and minimap presence | PASS (technical) | All three front panels and their minimap areas were visible in the live scene. |
| 960 × 540 standalone capture | PASS (technical) | The fixed logical surface and lower control deck were fully present without clipping. |
| 1280 × 720 standalone capture | PASS (technical) | The 960 × 540 integer-scaled surface was fully present; expected side letterboxing preserved its layout. |
| 1920 × 1080 fullscreen capture | PASS (technical) | The full roulette board and all 12 manipulation controls were visible without bottom clipping. |
| Runtime diagnostics | PASS (bounded) | Hera diagnostics reported no task-related errors or warnings during this flow. |

## Keyboard incident correction

Initial raw Space/Enter injection was received by the runtime but did not translate through Godot's action map, which created a false keyboard-defect signal. The focus-targeted `ui_accept` action test above demonstrated the product-side state transition. The incident record on GitHub Issue #208 was corrected accordingly.

## Remaining boundaries

- `CURRENT_HUMAN_USABILITY_EVIDENCE = NOT_RUN`
- `CURRENT_PLAYER_EXPERIENCE_EVIDENCE = NOT_RUN`
- Long natural BATTLE → REVIEW runtime is not established by this bounded live capture. The existing headless phase contract separately covers its debug outcome transition.

No product code, scene, asset, or balance data changed for this QA record.
