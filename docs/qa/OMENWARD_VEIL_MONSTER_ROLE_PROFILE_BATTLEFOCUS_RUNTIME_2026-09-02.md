# OMENWARD Veil Monster Role Profile — BattleFocus Runtime QA

```yaml
qa_id: OMW-QA-20260902-VEIL-MONSTER-ROLE-PROFILE-BATTLEFOCUS
status: MACHINE_VERIFIED__RUNTIME_TECHNICAL_SMOKE_PASS__HUMAN_NOT_RUN
scope: VEIL_SPEAR_GUARD_V3__ARCHER_V2__CAVALRY_V3__MAGE_V2
runtime_consumer: scripts/ui/battle_focus_view.gd::BattleFocusView
runtime_fixture: tests/visual/battle_focus_role_profile_fixture.tscn
runtime_surface: scenes/main/main.tscn::RunCommandScreen__BATTLE__FRONT_TAB
capture: docs/images/reviews/OMENWARD_VEIL_MONSTER_ROLE_PROFILE_BATTLEFOCUS_RUNTIME_2026-09-02.png
capture_sha256: AAD65051CA03945213645F5DFA0356EDE4BD4DAADCDE4C04D2D6770B38F49BE6
capture_dimensions_px: 960x540
godot_version: 4.7.1
runtime_errors: 0
runtime_warnings: 0
human_player_evidence: NOT_RUN
rights_release: REVIEW_PENDING__NOT_RELEASE_PASS
```

## Technical result

The fixture runs the real `main.tscn` composition, enters the player-facing
`BATTLE` / `전선` surface, and injects the same six-unit display roster used by
the prior role-profile smoke. On the Veil half of the battlefield, the active
Spear Guard, Archer, and Mage render from their new monster variants. The
Cavalry resource is exercised by the faction/role path contract. The fixed
tower, one-row march minimap, close terrain, route state, and BattleFocus
renderer remain the actual production consumers.

| Gate | Result | Evidence |
| --- | --- | --- |
| New Veil role path and faction-facing contract | PASS | `storybook_role_profile_visual_asset_test.gd` asserts all four new paths, `512×512` texture cells, common pivot, and Veil mirroring. |
| Targeted role-asset contract | PASS | RED first failed for the absent V3/V2 paths and stale catalog/preload bindings; GREEN passed after assets and bindings existed. |
| Full Godot headless suite | PASS | `33 / 33` scripts passed. |
| Live BattleFocus technical capture | PASS | Hera ran `battle_focus_role_profile_fixture.tscn`; all six injected silhouettes remain inside the close-battle frame. |
| Live diagnostics | PASS | Hera diagnostics reported `0` errors and `0` warnings. |
| Screenshot structural analysis | PASS WITH NOTE | `960×540`, nonblank, non-low-detail; analyzer reports `possible_clipping` from legitimate overall left-edge frame content, not a unit crop. |

This is a renderer and technical-readiness result. It is not a human/player
readability PASS, art-direction sign-off, device test, rights clearance, or
release gate.
