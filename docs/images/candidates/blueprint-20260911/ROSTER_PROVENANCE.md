# Roster / building / hero candidate provenance

2026-09-11 scoped execution preview: `scripts/replan/front_art.gd` now consumes battlefield-layer, ward-roster, veil-roster, building-tree, special-roster-additions and ui-icons in `scenes/replan/front_slice.tscn`. State remains GENERATED_CANDIDATE; this is a visible review consumer, not final asset registration. UI portraits and battlefield card tokens are opaque static images, Aseprite NOT_USED. Missing special facility art uses an explicitly generic icon. Heroes and historical Aseprite slash are not wired. Source images are unchanged; no duplicated source pixels. Godot GPU captures are implementation evidence, not image approval.

## v3 additions and correction

`special-roster-additions.png`: source `exec-3a276565-c6c5-4642-8f77-94f3cb47644f.png`, image_gen generated, Aseprite NOT_USED. 2x2 opaque codex layout: allied assassin/flying, Veil assassin/flying. Static candidate, user approval pending, not a battle animation. Wing/weapon margin remains a review concern. All new image hashes are in the v3 receipt.

Exact generation prompt:

Use case: stylized-concept. Create one four-cell square portrait atlas for OMENWARD in-game unit codex. Reference image establishes polished dimensional storybook watercolor SD quality, ivory gold navy cloth. Two equal columns and two rows with generous 12% inset margins in EVERY cell. Top left allied hooded assassin with two short daggers, top right allied angelic flying lancer with white feather wings and a short spear, both 2.5-head SD miniature full body facing right. Bottom left a Veil assassin monster: low purple-black chitin stalker with hooked forelimbs, no human armor or face. Bottom right a Veil flying monster: bat-moth hybrid with violet membranes and chitin, facing left. Opaque plain ivory background, no text or frames, no checkerboard, every weapon/wing stays entirely within its cell. This is static codex/card artwork, not animation sprites. Do not reproduce existing characters; only match material finish and paint style.

v3 five-pass review: (1) separated general/special authority; (2) restored missing assassin/flying and same-role T3; (3) 12 schema/graph/cost checks passed; (4) no Aseprite/alpha/runtime overclaim; (5) PDF generation and selected render review only. Full runtime, economy simulation and final user approval remain unrun. Earlier 8-role and single-root review statements below are historical v2, not current structure.

State: GENERATED_CANDIDATE, user approval PENDING, runtime NOT_RUN. Produced with built-in image_gen, not an API fallback. SHA-256 and actual dimensions are recorded in the derived PDF receipt. Originals remain at the image tool's returned location. The repository copies are candidate sources, not registered production assets.

| File | Generated source basename | Intended consumer | Grid |
|---|---|---|---|
| ward-roster.png | exec-2a4a8ede-e0b2-4d85-a3dc-2b509b032063.png | Unit codex / unit cards | 4 x 2 |
| veil-roster.png | exec-d18f9ace-a207-4ba2-8c2b-30080f44dff4.png | Enemy codex / forecast inspection | 4 x 2 |
| building-tree.png | exec-7ab313a3-cb41-4f09-9d1d-b55d78a2a462.png | Building list / specialization selection | 4 x 2 |
| heroes.png | exec-9592efc9-5eac-40a7-a0b5-057fb47b106d.png | Hero selection / codex | 3 x 1 |

## Prompt set (normalized production briefs)

- Ward: polished dimensional storybook watercolor SD; ivory/gold/navy; full-body shield, archer, mage, priest, spear, greatsword, cavalry, siege; opaque ivory equal tiles; no text. Style reference: ../replan-20260910/ward-shield-quality-v3.png, not an approved sprite identity.
- Veil: monster anatomy, not recolored human knights; purple-black chitin and violet glow; shield beetle, quill beast, spore creature, stitching grub, horn beast, scythe mantis, charger, siege behemoth; same full-body opaque tile composition.
- Buildings: navy roofs, ivory stone, golden accents, self-contained three-quarter buildings; barracks, spear hall, archery range, academy, chapel, blade hall, stable, siege forge; list-card artwork, no battlefield construction nodes.
- Heroes: flag commander, silver-haired ranger, dawn priest; polished storybook palette; 3 full-body opaque card tiles; no text. Same Ward style reference.

## Review findings

- All four sources are opaque RGB. This is intentional for UI portrait consumers, not evidence of transparent battle sprites.
- Ward spear/weapon tips approach or cross ideal tile boundaries. Before individual AtlasTexture delivery, repair spacing rather than silently clipping a weapon.
- Hero anatomy is longer than the requested 2.5-3-head battle-unit proportion. Card use remains candidate; battle silhouette needs a separate SD pass.
- Building chapel includes a cross-like roof detail despite sun-emblem brief; world-symbol consistency needs review.
- No spritesheet motion, alpha extraction, engine import, rights clearance, or user approval is claimed.

## Five review passes over the changed scope

1. Authority: corrected T1 shield / specialization and kept final implementation approval closed.
2. Rule consistency: removed free troop switching, initial archers and baseline archer tokens; removed speed-only building upgrade rule.
3. Data: verified parent tier edges and all 8 roles; prices and production are linked to the same IDs.
4. Art: recorded RGB, spacing, hero proportions and chapel symbol issues; no false sprite-ready labels.
5. Delivery: PDF checks page bounds, text presence, 53/159 fixtures and source hashes. Visual review is partial; Git CI and runtime are not promoted to PASS.
