# OMENWARD · Remaining P0 Autonomous Approval + Dual Storage

```yaml
approval_id: OMW-ASSET-AUTO-APPROVAL-20260826-P0-REMAINDER-V1
policy_id: OMW-VIS-POLICY-20260826-AUTONOMOUS-REQUIRED-IMAGES-V1
status: AUTO_APPROVED_SOURCE_AND_CLEANUP_MASTERS_STORED
scope: 20_P0_ROULETTE_HUD_MINIMAP_WORLD_COMMAND_IMAGES
local_source_storage: COMPLETE__20
notion_source_records: COMPLETE__20
cleanup_masters: COMPLETE__20
partial_alpha_pixels: 0_TOTAL
transparent_corner_alpha: 0_TOTAL
opaque_rgb_regression: 0
implementation_ready: NO
godot_import: NOT_RUN
runtime_readability: NOT_RUN
```

## Included source groups

- Roulette: Gold/X tokens, frame, active-state overlay, 3×3 board frame, manipulation arrow, omen device.
- HUD/minimap: five omen signatures, mana, troop capacity, minimap-marker atlas.
- World: terrain plate, Ward stronghold, Veil rift anchor, route-landmark prop atlas.
- Command: Omen Warden source sprite.

All sources are held in `.asset-vault/library/` and each has an individual Notion approval record beneath the Runtime Consumer Asset Checklist. The local source manifest is `.asset-vault/p0_remainder_approved_sources_2026-08-26.json`; cleanup export and per-pixel verification manifests are in `.asset-vault/p0_remainder_cleanup_masters_2026-08-26.json` and `.asset-vault/p0_remainder_cleanup_master_verification_2026-08-26.json`.

The master process preserves source dimensions and retained-pixel RGB. It removes alpha values `0–63` and hardens retained pixels to alpha `255`; approved sources remain immutable.

## Exclusions

Unit-token role-anchor crops, atlas/cell geometry, pivots, animation timing, Godot import, runtime readability, and Codex implementation remain separate work. No file/Scene/Resource consumer has changed in this approval record.
