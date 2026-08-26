# OMENWARD · Remaining P0 Candidate Batch · 2026-08-26

```yaml
candidate_batch_id: OMW-ASSET-CANDIDATE-20260826-P0-REMAINDER-V1
status: PROPOSED_FOR_USER_REVIEW
generation_authority: USER_REQUEST__"권장안대로 진행"
scope: ROULETTE_UI__HUD_MINIMAP__BATTLEFIELD_WORLD__OMEN_WARDEN
candidate_count: 20
project_local_candidate_storage: COMPLETE
notion_approval_storage: NOT_CREATED__CANDIDATE_NOT_YET_APPROVED
source_units_for_token_crops: EXISTING_APPROVED_UNIT_MASTERS_ONLY
token_crop_export: DEFERRED__CELL_ENVELOPE_NOT_LOCKED
cleanup_export: NOT_RUN
implementation_ready: NO
godot_codex: NOT_RUN
```

## Candidate groups

- Roulette UI: Gold token, X token, token frame, token-state overlay, 3×3 board frame, manipulation arrow, omen device.
- HUD/minimap: MASS, ARMORED, FLYING, INFILTRATION, SIEGE signatures; mana; troop capacity; minimap marker atlas.
- Battlefield/world: terrain plate, Ward stronghold anchor, Veil rift anchor, route-landmark prop atlas.
- Command: Omen Warden source sprite.

The 20 PNG candidates and the local checksum/geometry manifest are in `.asset-vault/candidates/2026-08-26-p0-roulette-ui-batch`, `.asset-vault/candidates/2026-08-26-p0-hud-minimap-batch`, `.asset-vault/candidates/2026-08-26-p0-roulette-world-command-batch`, and `.asset-vault/candidates/2026-08-26-p0-candidate-manifest.json`.

## Review boundary

Candidates keep transparent-background intent and contain no text/UI screenshot. They are not approved images, are not stored as Notion approval records, and cannot be cleaned/exported, marked `IMPLEMENTATION_READY`, imported into Godot, or integrated by Codex until the user approves the candidate batch.

Unit token crops are intentionally not newly generated: they must be deterministic role-anchor crops from the already approved unit masters after a token cell-envelope/pivot contract is approved.
