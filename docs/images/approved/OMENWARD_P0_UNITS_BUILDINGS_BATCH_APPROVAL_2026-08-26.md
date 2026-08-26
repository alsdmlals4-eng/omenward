# OMENWARD · P0 Units + Buildings Source Batch · 승인 기록

```yaml
approval_id: OMW-ASSET-APPROVAL-20260826-P0-UNITS-BUILDINGS-BATCH-V1
status: USER_APPROVED_SOURCE_BATCH
approved_at: 2026-08-26
user_approval_input: 후보 묶음 승인
scope: 17_NEW_UNIT_SOURCES_PLUS_7_T1_BUILDING_SOURCES
project_local_storage: COMPLETE
notion_approval_records: COMPLETE__24_CHILD_PAGES
pixel_cleanup: COMPLETE__24_FINAL_MASTERS
master_export: COMPLETE__24_FINAL_MASTERS
implementation_ready: NO
runtime_import: NOT_RUN
runtime_readability: NOT_RUN
godot_codex: NOT_RUN
```

## Approved batch scope

- Units: Veil Greatsword; Lumern/Veil Spear, Assassin, Archer, Cavalry, Priest, Mage, Flier, and Giant.
- Buildings: Vault, Farm, General Barracks, Special Barracks, Defense Tower, Command Post, and Mana Tower T1.
- Existing approved Shield Guard pair and Lumern Greatsword are not duplicated by this record.

## Durable storage rule satisfied

All 24 approved PNG sources are stored in `.asset-vault/library/characters/{allies,enemies}` or `.asset-vault/library/buildings`. Each source has a corresponding child approval record under Notion's Runtime Consumer Asset Checklist. Notion records provenance, hash, local path, consumer, and lifecycle state; they do not claim a binary upload.

## Important remaining gate

The user separately approved deterministic cleanup/master export. The 24 final masters are documented in `docs/images/approved/OMENWARD_P0_UNITS_BUILDINGS_CLEANUP_MASTER_EXPORT_V1_2026-08-26.md`; they retain source dimensions and do not normalize canvas/pivot. No Godot import or Codex implementation is authorized by this source-batch approval.
