# P0 Building Button Thumbnail Consumer Plan

**Goal:** Replace only the three current build-action button grayboxes with compact, approved-building thumbnails while leaving the three-lane battlefield and unconsumed building masters unchanged.

**Consumer mapping:** `GENERAL_BARRACKS_T1 → BarracksButton`, `FARM_T1 → FarmButton`, `DEFENSE_TOWER_T1 → TowerButton`.

**Out of scope:** Vault, Command Post, Mana Tower, and Special Barracks remain source-only because no current UI/data consumer resolves them. No building rule, cost, construction state, or battlefield layout changes.

## Steps

1. Add a failing Stage HUD contract requiring the three current buttons to own a compact icon.
2. Export only the three approved cleanup masters as transparent nearest-neighbour thumbnail cells under `assets/art/buildings/` with source/output provenance.
3. Bind the existing `Button` nodes to those textures with a constrained icon size; leave labels and behavior unchanged.
4. Run focused and full headless checks, then inspect the live tutorial UI and record Notion/repository evidence.
