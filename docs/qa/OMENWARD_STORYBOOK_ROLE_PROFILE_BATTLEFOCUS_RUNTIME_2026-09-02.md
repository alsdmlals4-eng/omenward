# OMENWARD Storybook Role Profile — BattleFocus Runtime QA

```yaml
qa_id: OMW-QA-20260902-STORYBOOK-ROLE-PROFILE-BATTLEFOCUS
status: MACHINE_VERIFIED__RUNTIME_TECHNICAL_SMOKE_PASS__HUMAN_NOT_RUN
scope: ARCHER_MAGE_EXACT_USER_APPROVAL__SPEAR_CAVALRY_STANDING_AUTONOMOUS_PROMOTION
approved_exact_asset_set: OMW-IMG-20260902-STORYBOOK-ARCHER-MAGE-PAIR-SET-V1
autonomous_asset_set: OMW-IMG-20260902-STORYBOOK-SPEAR-CAVALRY-AUTONOMOUS-V2
runtime_consumer: scripts/ui/battle_focus_view.gd::BattleFocusView
runtime_fixture: tests/visual/battle_focus_role_profile_fixture.tscn
runtime_surface: scenes/main/main.tscn::RunCommandScreen__BATTLE__FRONT_TAB
capture: docs/images/reviews/OMENWARD_STORYBOOK_ROLE_PROFILE_BATTLEFOCUS_RUNTIME_2026-09-02.png
capture_sha256: 6EDDC18A00E5FDECD93810C336A6EE2CE5617A6D3C31E5221C1A463E96B28AC6
capture_dimensions_px: 960x540
godot_version: 4.7.1
runtime_errors: 0
runtime_warnings: 0
human_player_evidence: NOT_RUN
rights_release: REVIEW_PENDING__NOT_RELEASE_PASS
```

## What was checked

The fixture starts the real tutorial-stage application composition, enters the
normal `BATTLE` phase and `전선` tab, and binds the same `BattleFocusView` used
by the player-facing Run Command screen. Only its QA roster injection is
fixture-specific: it places Lumern/Veil Spear Guard, Archer, and Mage in the
single active front, then stops the session driver so no preview unit dies
before the capture. The BattleFocus renderer, MarchMinimap, fixed tower,
catalog resources, and faction-facing logic remain the production consumers.

The final capture shows all six injected silhouettes inside the close battle
frame: three Lumern and three Veil. The renderer uses an `88×88` display cell
instead of the former `74×74`, so the bow, staff light, spear, and faction
color language stay distinguishable against the modular field art.

## Evidence and result

| Gate | Result | Evidence |
| --- | --- | --- |
| Exact approved Archer/Mage bytes | PASS | Four canonical runtime siblings are byte-identical to their locked candidate derivatives. |
| Spear/Cavalry source provenance and true alpha | PASS | Candidate records contain source and derivative SHA-256 values; outputs are `512×512` RGBA with normalized `(256,448)` pivot. |
| Faction/role lookup and Veil orientation | PASS | `storybook_role_profile_visual_asset_test.gd`; Veil Archer/Mage/Spear/Cavalry map to their own texture and mirror only where their source facing requires it. |
| No Shield Guard impostor fallback | PASS | Unsupported roles return an empty visual map and render a role marker, rather than a misleading Shield Guard texture. |
| BattleFocus live composition | TECHNICAL PASS | Hera ran the fixture as `tests/visual/battle_focus_role_profile_fixture.tscn`; UI tree confirmed BATTLE, Front tab, BattleFocus, and MarchMinimap all visible. |
| Live error/warning log | PASS | Hera diagnostics: `0` errors and `0` warnings. |
| Full Godot headless contract suite | PASS | `33 / 33` scripts passed. |
| Full Python contract suite | PASS | `570` passed with the workflow-pinned Base checkout recreated locally for the CI-only recovery-map assertion. |

The screenshot analyzer reports `possible_clipping: true` because the overall
screen has legitimate content against its left frame edge. Manual artifact
inspection found the six role silhouettes wholly within the BattleFocus border;
this is an automated capture interpretation note, not a human usability claim.

## Evidence ceiling and next safe work

This is a machine/runtime technical smoke. It does **not** establish player
readability on a physical target device, combat balance, final animation states,
commercial-asset rights, release approval, or individual user approval of the
four autonomous Spear/Cavalry bytes. The most useful next human check is a
short readability pass with an actual combat-produced mixed roster, including
the two Cavalry silhouettes.
