# Roster / building / hero candidate provenance

## Ward/facility alpha-only continuation · 2026-09-13

User-approved local extraction: `tools/veil_cutout.py --ward`, connected exterior paper removal and inward 0.5px alpha feather; RGB byte-for-byte preserved, no source overwrite or redraw. Sources remain the corresponding original files in this directory. Special atlas crops `(0,0,1254,610)` at the reviewed empty gutter. `front_art.gd` consumes Ward portraits and facility portraits; building rows split at y407 to preserve chapel spire. Shield uses its existing motion asset instead. These remain runtime candidate derivatives, not final art approval.

| Output | SHA-256 |
|---|---|
| ward-roster-alpha.png | 9554b87382f742c5429e30bcfeb79569de718b0116e05bf782a3265c5803ec99 |
| ward-special-alpha.png | dfe2bf87d9cb4d8cfd854cb71054878db64c81c0c27ccc255c2541d91811f232 |
| building-tree-alpha.png | 2c33babaca340318d00ec52a84372219ad7193ac58987dc8aff91e58b775d5ce |

Source hashes: ward-roster.png `8b2d56769fa8b123c0158f7b2aac8a3c253060ee6b1373e3e66561781d609e2c`; special-roster-additions.png `a35fcf30c33284f56f98772eb43fbb217257925ddfca9b20bb5f16d53a6cb820`; building-tree.png `c915b277179ed33fe08c20d07f85d931cb9378a98245de99ece4a98f813e6216`.

This operation did not use Aseprite or produce new animation frames. Existing shield/native Veil files are unchanged. RGB/alpha automated checks and sampled pale anatomy plus mixed GPU inspection are not exhaustive segmentation approval. Enclosed paper remnants, narrow cell/weapon margins, generic facility fallback icons and remaining motion families are still partial/unimplemented. No source image may be removed because it binds provenance and regression tests.

## Shield four-pose motion · 2026-09-12

Reuse of `ward-shield-slash-alpha-candidate.png` (SHA-256 `d291307bf45e3ebf910bc1385c80c0aa30f28bb4aaa5411a41b2653dfecd99ce`), not new generated artwork. Four disconnected components can be separated despite crossing the old 2×2 grid. `tools/ward_motion.py` preserves every source pixel with alpha >8 exactly; only disconnected background specks with alpha <=8 are omitted. No scaling, rotation, deformation or RGB repainting. Translation offsets: idle(71,83), windup(-553,79), impact(37,-474), recover(-569,-476). Each 768×768 frame has foot pivot (384,700).

| File | SHA-256 | Role |
|---|---|---|
| ward-shield-motion.png | 9047aab8a8b0ecc4275ddf69ae5bd419c630ee0a64fb99bf6ff50010f026cb4c | 3072×768 RGBA atlas; front_art.gd ally shield frames0–3 |
| ward-shield-motion.aseprite | 2831a69669b2158a90e892f653926f83b392ccbf813238374195feeb2eca1227 | Native editable four frames, shield layer |
| ward-shield-motion.json | Recompute on metadata changes | Frame geometry and 400/180/100/150ms timing; filename labels normalized after export |

Aseprite USED: imported existing raster poses into four initially empty frames and set durations. A failed attempt duplicated populated cels and overlaid poses; the corrected native and export match all four input RGBA frames exactly. Lesson: create blank frames before imports, then compare every export frame to its source. Automated export regression now prevents this failure from silently returning. No new freehand drawing was done in Aseprite. Idle's400ms is preview timing only; actual runtime idle lasts until combat state changes.

Consumer: front_screen.gd selects frame from actual windup/action state. Windup180ms, impact100ms, recovery150ms are simulation-time values; runtime substeps can quantize transitions by up to50ms. Damage occurs at windup completion with target/range revalidation. Existing damage and cooldown values remain; first strike is delayed. Savev1 missing optional fields remains readable. Model55 checks and UI/native timing checks PASS. Actual GPU natural combat captures `output/front-shield-windup.png`, `front-shield-impact.png`, `front-shield-recover.png` show all three action states; these are unedited screen captures, not posed mockups. Quality remains a four-pose candidate, not smooth full animation, walk/hit/death or Human/final art approval. Original source retained because extraction tests consume it. Rollback is the previous idle-only consumer plus pre-windup model, not overwriting other units or saves.

## Veil local alpha follow-up · 2026-09-12

Follow-up edge refinement: ADAPT Pillow GaussianBlur(0.5) on alpha only, clamped by the original alpha (inward feather); REJECT whole-RGB blur and broad erosion because they alter detail or thin silhouettes. Official method reference: https://pillow.readthedocs.io/en/stable/reference/ImageFilter.html#PIL.ImageFilter.GaussianBlur. Source RGB remains byte-identical. Feathering alone preserves occupied pixels; a separately reviewed priest ground ROI (local x>=150, y>=405) clears 1860 old occupied paper/shadow pixels. Left-side magical glow is excluded and regression-tested. Five cutout tests cover head, lower glow, ground, wing top, and bounded feather. This does not remove every enclosed light region or all paper residue: quality remains PARTIAL.

Motion follow-up attempt: built-in imagegen `exec-013a8336-f4b7-40e8-9a34-7493fc909f6c.png`, 1254 square RGB, not RGBA. Brief: same ivory/gold/navy knight, 2x2 idle/windup/downward slash/recovery, constant scale and baseline, 18% clear margins, no painted checkerboard. Output violated true-alpha and margin expectations; REJECTED_FOR_RUNTIME and parked in manual-deletion review. No new motion was connected. Next preparation should separate individual poses and validate extraction/pivot before atlas assembly, not keep retrying full-sheet transparency prompts.

User explicitly authorized local background/mask processing after opaque checkerboard attempts failed. Source artwork is unchanged: `veil-roster.png` and lower Veil row of `special-roster-additions.png`. `tools/veil_cutout.py` changes alpha only; all cropped RGB bytes match their source. This is not new image-model artwork or production-art approval.

| Candidate | Dimensions | SHA-256 | Consumer |
|---|---|---|---|
| veil-roster-alpha.png | 1774 × 887 | d3120d16fdcedf9c4fb5761d9b6b23709fac0c48e1c1be0f6ba677413bff9101 | front_art.gd side=1, eight existing roles |
| veil-special-alpha.png | 1254 × 644 | c3f33f82bdad820cc1b775376bbf6fb07ae306cf8a9e271b84fa55bf38e50f26 | front_art.gd side=1 assassin/flying |

Aseprite USED_STATIC_ONLY: each PNG imported into its same-basename `.aseprite`, frame 1 exported, complete RGBA bytes matched. No motion tags/new attack frames. Original opaque atlas sources used imagegen and did not use Aseprite. Alpha zero pixels: 895234 / 507919 respectively. Special crop y=610 uses the empty gutter above the wing at y=618, not the destructive nominal y=627 split.

Independent review found pale priest anatomy erased by the first generic mask. Corrected priest cell uses a conservative threshold; actual head pixels (1450,100)/(1480,100) are regression-tested opaque. Earlier cutout tests 3 PASS; Godot model 39 checks and UI/save/10-role alpha checks PASS. Edge quality remains PARTIAL: pale paper fringe/residue can remain, especially priest; enclosed pale areas require visual refinement. Approval PENDING. Static candidate runtime wiring is not complete animated-character delivery.

User cleanup policy: failed alpha generations, identical generated copies with repository originals retained, and superseded/staging outputs are moved to `C:/Users/user/Downloads/OMENWARD_DELETE_REVIEW_20260912`, not deleted. `ALL_FILES.csv` owns exact paths/hashes/reasons. Unclassified historical sources remain untouched. Previous original-location statements below do not imply duplicate generated copies still occupy that location.

## UI/alpha follow-up · 2026-09-11

- `ward-shield-slash-alpha-candidate.png`: built-in image model, candidate only; source `exec-ea64ba8f-ecf7-4c90-aa9c-382f13513f1b.png`; SHA-256 `d291307bf45e3ebf910bc1385c80c0aa30f28bb4aaa5411a41b2653dfecd99ce`.
- Actual PIL readback: RGBA, 1254×1254, alpha range 0–255, 805895 completely transparent pixels. Godot checks transparent corner, alpha detection and exact 627×627 idle region. No code-based background removal.
- Consumer: `front_art.gd::unit(shield_guard, 0)` → `front_screen.gd`, **top-left idle cell only**, no rectangular card border in battlefield. Other classes remain opaque candidate cards. Final approval PENDING; Aseprite NOT_USED for this file.
- Four generated poses exist, but bottom-left sword crosses its cell; not a valid four-frame animation. Spacing repair outputs again had painted checkerboard and are not copied into the project. No slash playback/impact synchronization claim.
- Origin: style/identity reference `ward-roster.png` top-left soldier → four distinct 2×2 slash poses (`exec-5385a573-3a70-4811-805a-7e6c354272a5.png`, RGB checkerboard rejected) → image-model alpha extraction. Source unchanged; only selected output copied to repository.
- Exact successful extraction prompt: "Use case: background-extraction. Edit target: the provided four-frame knight sheet. Remove ONLY all the visible gray/white checkerboard pixels in the background. Preserve the four knights, their poses, colors and pixels as closely as possible. Return a PNG image with a TRUE alpha channel, completely transparent outside the characters and in holes around arms, weapons, and cloaks. The checkerboard currently in the input is incorrectly painted into RGB. It must be removed, not redrawn. No solid white background, no black background, no gray background, no checkerboard rendering. Actual RGBA transparent cutout. Do not add anything. Keep canvas and character positions identical."
- Learning: transparency can regress on a later spacing edit. Re-test alpha after **every** image edit, not only initial extraction. Project regression checks now reject opaque replacements. Base promotion remains a proposal, not a change to shared policy.

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
