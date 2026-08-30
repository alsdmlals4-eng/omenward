# [Candidate] OMENWARD Close Single-Front Battle UI Reference

```yaml
asset_id: OMW-IMG-20260830-CLOSE-FRONT-UI-REFERENCE-V1
created_at: 2026-08-30 KST
status: GENERATED_CANDIDATE__USER_REVIEW_PENDING
generator: BUILT_IN_IMAGEGEN
source_path: C:/Users/user/.codex/generated_images/01a04af4-0452-7a13-9b6e-1a6077568d72/exec-4fbd8f2d-4248-4dd4-8e12-bd746263216b.png
source_sha256: 2C3F6C61254A8D4F00D9DAA90463354AFC61C7F3210A77559BEE2D246E69801B
source_dimensions_px: 1672x941
pixel_format: Format24bppRgb
transparency: NOT_APPLICABLE__COMPOSITION_REFERENCE
consumer_candidate: RunCommandScreen/BattlePrimaryCompositionReference
runtime_asset: NONE
runtime: NOT_IMPLEMENTED
human_readability: NOT_RUN
rights_status: GENERATION_PROVENANCE_RECORDED__RELEASE_RIGHTS_REVIEW_PENDING
user_asset_lock: NONE
approval_source: NONE
```

## What this previews

This is a **direction-only composition preview**, generated from the new
foundation and territory-prop candidates plus the existing Lumern/Veil unit
language. It demonstrates the intended hierarchy:

```text
thin top command rail
wide single connected battle field
  Lumern props -> clear clash ground <- Veil props
one live defensive tower near Lumern
narrow route-progress minimap at right
shallow compact action deck at bottom
```

The left and right terrain shapes are illustrative of independent runtime
props, not a new baked battlefield image. It contains no authoritative UI
text, source unit sprite, runtime position, gameplay number, or live state.
Godot-native controls, actual shield-guard sprites, the single tower, and the
five-sector minimap continue to be implemented separately after the exact
foundation-and-prop lock.

## Promotion boundary

- The file stays external as a planning preview; it must never be used as a
  texture atlas, UI screenshot, or embedded game screen.
- The user must separately lock the foundation and both three-prop sets before
  runtime art binding begins.
- Image generation, alpha inspection of props, and static documentation do not
  prove runtime readability, UX quality, platform behavior, or release-rights
  clearance.

