# OMENWARD · Shield Guard Idle Texture Consumer · Execution Packet

```yaml
packet_id: OMW-IMPL-20260826-SHIELD-GUARD-IDLE-TEXTURE-CONSUMER-01
github_issue: 33
approval_basis: USER_EXPLICIT_CODEX_REACTIVATION_2026-08-26
scope: LUMERN_AND_VEIL_SHIELD_GUARD_IDLE_PAIR_ONLY
status: COMPLETE__IMPORT_AND_HEADLESS_CONTRACTS_VERIFIED
```

## Goal

Render the approved Shield Guard cleanup masters through the existing shared `Unit` Scene.  Lumern and Veil select different idle textures through `visual_faction_id`; gameplay data and timing stay shared.

## Player-visible result

When a `shield_guard` is present in battle, its flat procedural marker is replaced by the approved faction-specific idle image.  Other archetypes and an unavailable texture keep the existing graybox rendering.

## In scope

- Commit the two approved cleanup-master derivatives to `assets/art/units/` as Godot runtime inputs.
- Add an idle texture and pivot to `FactionVisualProfile`.
- Add a `Sprite2D` receiver to `scenes/units/unit.tscn`.
- Make `UnitView` choose the texture, apply the locked pivot, mirror Veil for lane-facing, and preserve its procedural fallback.
- Cover the resource, scene, and asset contract with a focused headless test.

## Explicit exclusions

- Other unit, building, HUD, roulette, minimap, or commander images.
- New image generation, crop redesign, atlas production, animation timing, gameplay values, or battle rules.
- Runtime/readability or human-play PASS claims.

## Locked inputs

- Lumern master SHA-256: `f3189ba44bb2994760075eed1aa8aed97333948116f7d66f618ff66b3db999bf`
- Veil master SHA-256: `11d6fa548f03b1609afb60344404fac288ba9e5702a15cc57e76ff577eacff0a`
- Common master canvas: `1280×1344`; idle pivot: `(640, 1280)`; source facing: right.
- Source authority: `docs/images/approved/OMENWARD_SHIELD_GUARD_CLEANUP_MASTER_PAIR_V1_APPROVAL_2026-08-26.md`.

## Acceptance criteria

1. Both approved Shield Guard masters are versioned as Godot-readable project assets with the recorded SHA-256.
2. `shield_guard` Lumern and Veil profiles each resolve their own texture and the shared pivot.
3. The one shared `Unit` Scene owns the `Sprite2D`; no enemy-only scene, contract, or gameplay branch is added.
4. Veil mirrors from the shared right-facing source; missing texture and all other units retain procedural fallback.
5. The focused RED→GREEN test, existing scene contract, editor import, and relevant headless suite run without a new task-related error.

## Evidence ceiling

This packet can establish import/receiver contracts only. `CURRENT_SD_UNIT_RUNTIME_READABILITY` and human play evidence remain `NOT_RUN` until an interactive review is recorded.

## Completion evidence

- `assets/art/units/lumern_shield_guard_idle.png` SHA-256 matches the locked Lumern cleanup master.
- `assets/art/units/veil_shield_guard_idle.png` SHA-256 matches the locked Veil cleanup master.
- Godot 4.7.1 headless editor import completed for both PNG files.
- Focused `shield_guard_visual_asset_test.gd`, existing `scene_contract_test.gd`, every current `tests/headless/*_test.gd`, and the one-second headless smoke completed with exit code `0`.
- Notion runtime-copy evidence was created and read back: `Shield Guard Idle Runtime Import V1 · Codex Evidence` (`3c81b237-eb1c-81a1-a637-d4529159a7f3`).
- Editor shutdown emitted pre-existing resource/ObjectDB leak warnings; no task-related parser, importer, or test error was reported.

`CURRENT_SD_UNIT_RUNTIME_READABILITY = NOT_RUN` and `CURRENT_HUMAN_PLAYER_EVIDENCE = NOT_RUN` remain unchanged.
