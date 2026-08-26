# OMENWARD · P0 Units + Buildings Cleanup Master Export V1

```yaml
approval_scope_id: OMW-ASSET-APPROVAL-20260826-P0-UNITS-BUILDINGS-CLEANUP-EXPORT-V1
status: CLEANUP_MASTER_EXPORT_COMPLETED_UNDER_USER_APPROVED_SCOPE
scope_approval_input: "승인"
source_approval_id: OMW-ASSET-APPROVAL-20260826-P0-UNITS-BUILDINGS-BATCH-V1
scope: 17_NEW_UNIT_SOURCES_PLUS_7_T1_BUILDING_SOURCES
source_originals: IMMUTABLE
cleanup_rule: ALPHA_0_TO_63_REMOVED__ALPHA_64_TO_255_HARDENED_TO_255__OPAQUE_RGB_PRESERVED
canvas_policy: SOURCE_DIMENSIONS_RETAINED__NO_NORMALIZATION_OR_REFRAME
master_export: COMPLETE__24_FILES
partial_alpha_pixels: 0_TOTAL
transparent_corner_alpha: 0_TOTAL
opaque_rgb_regression: NONE
implementation_ready: NO
godot_import: NOT_RUN
runtime_readability: NOT_RUN
```

## Result boundary

The user approved this non-destructive cleanup/export scope after approving the 24 source images. Each master is a separate derivative under a `masters` directory; no approved source was overwritten. The process does not redraw pose, silhouette, palette, direction, crop, scale, or canvas geometry.

The first GDI copy draft changed RGB values on semi-transparent pixels and therefore failed the preservation verifier. Those 24 rejected drafts were quarantined under `.asset-vault/diagnostics/p0-gdi-cleanup-drafts-2026-08-26` and are not production masters. The final exporter edits decoded source bytes in memory before encoding, and its verifier checked every pixel of every final master.

## Final local masters

| Source | Cleanup master | Dimensions | SHA-256 |
|---|---|---:|---|
| Veil Greatsword Warrior | `characters/enemies/masters/OMENWARD_ASSET_UNIT_VEIL_GREATSWORD_WARRIOR_IDLE_V1_CLEANUP_MASTER_V1.png` | 1536×1024 | `9374c71388756e38b2524d5aaf59e12feef410e39d0f3276d0b703273b6068d7` |
| Lumern Spear Guard | `characters/allies/masters/OMENWARD_ASSET_UNIT_LUMERN_SPEAR_GUARD_IDLE_V1_CLEANUP_MASTER_V1.png` | 1536×1024 | `0ecfe4c63cc3e96522e9e516329114db396edb5dd34106c469314a8884770037` |
| Veil Spear Guard | `characters/enemies/masters/OMENWARD_ASSET_UNIT_VEIL_SPEAR_GUARD_IDLE_V1_CLEANUP_MASTER_V1.png` | 1536×1024 | `e6633022ce9921951f2efc7dc5c19f03b063d59fa8ba5a60af00cc426c0ac8f0` |
| Lumern Assassin | `characters/allies/masters/OMENWARD_ASSET_UNIT_LUMERN_ASSASSIN_IDLE_V1_CLEANUP_MASTER_V1.png` | 1233×1275 | `9a87344203c3d5437f786f9e13c465e09c96e674a98bc4c166680e54942b294a` |
| Veil Assassin | `characters/enemies/masters/OMENWARD_ASSET_UNIT_VEIL_ASSASSIN_IDLE_V1_CLEANUP_MASTER_V1.png` | 1214×1295 | `54150e47941b52b69f9d071b234720bd253e47e10d9ef15e356d8f51b2a709c8` |
| Lumern Archer | `characters/allies/masters/OMENWARD_ASSET_UNIT_LUMERN_ARCHER_IDLE_V1_CLEANUP_MASTER_V1.png` | 1214×1295 | `35bd6fe313a76267039dee00fd15dc38ee6ccc06866dbd749c3ed72b7d0efc3a` |
| Veil Archer | `characters/enemies/masters/OMENWARD_ASSET_UNIT_VEIL_ARCHER_IDLE_V1_CLEANUP_MASTER_V1.png` | 1218×1292 | `32cf1da9afbf9b122ce147d19f773731bf4021b5fc74b978460748c49c3bcaca` |
| Lumern Cavalry | `characters/allies/masters/OMENWARD_ASSET_UNIT_LUMERN_CAVALRY_IDLE_V1_CLEANUP_MASTER_V1.png` | 1254×1254 | `78613118fe5a38ecebdc1a586bcf3df7c578a53ddfa432e230a7a17c5bac75ae` |
| Veil Cavalry | `characters/enemies/masters/OMENWARD_ASSET_UNIT_VEIL_CAVALRY_IDLE_V1_CLEANUP_MASTER_V1.png` | 1383×1137 | `4f89c59586ffffae9dfcbf357bac0a7253949314118b4e5637ce0e1f36281959` |
| Lumern Priest | `characters/allies/masters/OMENWARD_ASSET_UNIT_LUMERN_PRIEST_IDLE_V1_CLEANUP_MASTER_V1.png` | 1214×1295 | `4f68188cbbd00c8a71384efe372c423206b92f1712d9119c4f1454920ae5e598` |
| Veil Priest | `characters/enemies/masters/OMENWARD_ASSET_UNIT_VEIL_PRIEST_IDLE_V1_CLEANUP_MASTER_V1.png` | 1214×1295 | `3aa843b6865c0cba971ad20567b28f278bfea73cbf77fba65edfe7659c5ce488` |
| Lumern Mage | `characters/allies/masters/OMENWARD_ASSET_UNIT_LUMERN_MAGE_IDLE_V1_CLEANUP_MASTER_V1.png` | 1214×1295 | `87582b7bb8430cade53dde3c71bcde4e228445ca336a1dc67caccf7260a2f70a` |
| Veil Mage | `characters/enemies/masters/OMENWARD_ASSET_UNIT_VEIL_MAGE_IDLE_V1_CLEANUP_MASTER_V1.png` | 1243×1265 | `48c6cb8e3a1ec3dcc8a85448d30a6157ca796c52a245d1b353a38cd852a4d321` |
| Lumern Flier | `characters/allies/masters/OMENWARD_ASSET_UNIT_LUMERN_FLIER_IDLE_V1_CLEANUP_MASTER_V1.png` | 1237×1272 | `ee8c870921448d2aeaacf01d82e47d08a65eacee66ff8fbe8e4a1da307bd4bbc` |
| Veil Flier | `characters/enemies/masters/OMENWARD_ASSET_UNIT_VEIL_FLIER_IDLE_V1_CLEANUP_MASTER_V1.png` | 1254×1254 | `52678a54b45cf4ecef859f7b1b0f58d95552aa77af026dbb50ff79230a6d41f8` |
| Lumern Giant | `characters/allies/masters/OMENWARD_ASSET_UNIT_LUMERN_GIANT_IDLE_V1_CLEANUP_MASTER_V1.png` | 1254×1254 | `4885656ef657afd7b19b3498b3b3e311c6077372fb6a9e88b64b0fb72e805192` |
| Veil Giant | `characters/enemies/masters/OMENWARD_ASSET_UNIT_VEIL_GIANT_IDLE_V1_CLEANUP_MASTER_V1.png` | 1254×1254 | `d2666b97ef8e7942626a3201932a6ad49a68e0e1f37569fd5757c79f198faafa` |
| Vault T1 | `buildings/masters/OMENWARD_ASSET_BUILDING_VAULT_T1_CLEANUP_MASTER_V1.png` | 1536×1024 | `44d75a3a9046d3544cacbe9d0eac869ac504f0c29cbf27284c9468144726bfbb` |
| Farm T1 | `buildings/masters/OMENWARD_ASSET_BUILDING_FARM_T1_CLEANUP_MASTER_V1.png` | 1536×1024 | `b302bb827e987ca19fadecd060486e2bc63b5ec283b621e7e16e937e80df64f2` |
| General Barracks T1 | `buildings/masters/OMENWARD_ASSET_BUILDING_GENERAL_BARRACKS_T1_CLEANUP_MASTER_V1.png` | 1214×1295 | `919040f0d9f429b6323169996b1782f816543baf25b2c034765940e616b2fadd` |
| Special Barracks T1 | `buildings/masters/OMENWARD_ASSET_BUILDING_SPECIAL_BARRACKS_T1_CLEANUP_MASTER_V1.png` | 1536×1024 | `8fbc41e374941df3b6b489e5a0f0b141e3b451ad0bbdb90f3ef807f277a0be82` |
| Defense Tower T1 | `buildings/masters/OMENWARD_ASSET_BUILDING_DEFENSE_TOWER_T1_CLEANUP_MASTER_V1.png` | 1208×1302 | `42246b9ce947bad4891260eef895cee4ffbcfe9ec757cf5b528249fa9cfb8bae` |
| Command Post T1 | `buildings/masters/OMENWARD_ASSET_BUILDING_COMMAND_POST_T1_CLEANUP_MASTER_V1.png` | 1312×1199 | `e32ff12f30d00d50a4d3b74d74daa375b25f506e9e57d0a99971ddaef78aaab2` |
| Mana Tower T1 | `buildings/masters/OMENWARD_ASSET_BUILDING_MANA_TOWER_T1_CLEANUP_MASTER_V1.png` | 1214×1295 | `0ae7334d58ffd0c3d7a1aaf620e76c9ea05d7e244a1e75056f1f244f07e4dbd8` |

All paths above are under `.asset-vault/library/`. The final export and per-pixel verification manifests remain in the local vault alongside the masters.

## Validation

- [x] Exactly 24 approved sources were processed; sources remain immutable.
- [x] Each final master retains its source dimensions; no common canvas or pivot was invented.
- [x] All final masters have zero partial-alpha pixels and fully transparent corners.
- [x] Every source pixel with alpha greater than 63 retains exactly the same RGB in its master.
- [x] Each final master SHA-256 is recorded above.
- [ ] `IMPLEMENTATION_READY` review, common idle geometry/pivot policy, Godot import, runtime readability, and human play evidence.

## Next Gate

`NEXT_IMAGE_OR_EDIT_ACTION = REQUIRES_ITS_OWN_EXPLICIT_USER_APPROVAL`

This batch does not authorize Godot import, Codex implementation, atlas creation, canvas normalization, or a runtime PASS claim.
