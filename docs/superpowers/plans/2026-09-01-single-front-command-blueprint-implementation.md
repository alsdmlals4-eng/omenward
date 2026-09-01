# Feature Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Turn the approved single-front command Blueprint into a trustworthy vertical visual slice: eight role-distinct, true-alpha unit candidates; then, after exact user asset selection, bind only the approved profiles to the close battle renderer and capture the current 960×540 presentation.

**Architecture:** Keep domain state and combat rules unchanged. `BattleFocusView` stays a read-only projection of one active front and selects a texture through a narrow, approved `archetype_id → texture` table. The asset record owns provenance, hashes, geometry, pivot, consumer, and approval state; it is deliberately separate from candidates and from gameplay data. `RunCommandScreen` remains the phase/tab router and owns no visual-profile logic.

**Tech Stack:** Godot 4/GDScript, GUT headless tests, project-local contract validators, built-in ImageGen for original raster candidates, Pillow read-only alpha inspection, GitHub PR #257 exact-head CI.

**Spec:** `docs/superpowers/specs/2026-09-01-single-front-command-blueprint-design.md`
**Product authority:** `docs/CURRENT_CONFIRMED_DECISIONS.md` and `docs/ACTIVE_CONTEXT.md`
**Visual source of truth:** `docs/images/approved/OMENWARD_STORYBOOK_SD_SHIELD_GUARD_TRUE_ALPHA_PAIR_V1.md`
**Benchmark input:** `docs/benchmarks/OMENWARD_SINGLE_FRONT_COMMAND_BENCHMARK_REVERSE_ENGINEERING_2026-09-01.md`

## Global Constraints

- Maintain one active front and the five-sector march route: Ward Citadel → Ward Forward → Clash → Veil Forward → Veil Citadel.
- Keep the top minimap a read-only, one-row context strip. It cannot gain unit markers, unit counts, battle input, a second battlefield, or a second tower.
- Keep exactly one fixed tower at the Ward Forward sector. Map buildings, build nodes, placement interactions, barricades, and fences remain forbidden.
- The global building roster remains `6 + stable player-held eligible point`, capped at 9. This visual work does not mutate its save schema or economy.
- Do not change roulette probability, command-phase semantics, player commitment, combat balance, platforms, external add-ons, save paths, or release claims.
- Existing approved Shield Guard textures, title art, terrain assets, historic candidates, user changes, and unrelated PR material are never overwritten, moved, or deleted.
- A generated image is only a `GENERATED_CANDIDATE`; it must not be copied into `assets/art/units/` or loaded by Godot until the user approves that exact cell and a SHA/provenance record exists.
- Machine image checks, headless tests, runtime capture, human readability, rights review, and release readiness are separate evidence states.

## Task 1: Authorize and register the bounded candidate batch

**Files:**
- Modify: `docs/superpowers/specs/2026-09-01-single-front-command-blueprint-design.md`
- Create: `docs/images/candidates/OMENWARD_STORYBOOK_ROLE_PROFILE_TRUE_ALPHA_CANDIDATES_2026-09-01.md`
- Create: `docs/images/candidates/role_profiles/` (only original generated PNG candidates that pass technical inspection)

- [x] Mark the Blueprint as `USER_CONFIRMED__ASSET_CANDIDATE_PRODUCTION_AUTHORIZED`; this authorizes candidate production, not runtime binding or final art promotion.
- [x] Pre-register the exact eight cells: Lumern and Veil each receive Spear Guard, Archer, Mage, and Cavalry. The approved Shield Guard pair is excluded to prevent redundant generation.
- [x] Record for every cell the candidate ID, generation prompt, output path, generator, source type, SHA-256, pixel dimensions, alpha extrema, alpha coverage, pivot `(256,448)`, intended consumer `BattleFocusView`, and status.
- [x] Keep rejected/malformed generations outside runtime asset paths with an explicit rejection reason rather than silently normalizing or replacing them. All eight outputs passed the bounded technical gate; therefore no rejection record was required.

**Verification:** Candidate registry covers exactly eight roles/factions; every retained PNG is `512×512`, has an RGBA channel with meaningful transparency, contains no text/checkerboard/UI, and is visually a single full-body right-facing role silhouette. Record this as machine candidate evidence only.

## Task 2: Produce and inspect original role-profile image candidates

**Files:**
- Create: `docs/images/candidates/role_profiles/omenward_<faction>_<role>_storybook_role_candidate_v1.png` (only after pass)
- Modify: `docs/images/candidates/OMENWARD_STORYBOOK_ROLE_PROFILE_TRUE_ALPHA_CANDIDATES_2026-09-01.md`

- [x] Use the built-in image model once per cell. Prompt each image as a 512×512, true transparent-alpha, full-body, right-facing, 2.5–3-head storybook-watercolor tactical miniature, grounded at pivot y=448.
- [x] Enforce faction palette and role-first silhouette: Lumern uses navy/ivory/cool-grey/restrained gold; Veil uses black-purple/dark red/carapace grey/limited rift glow. Spear has an unmistakably long spear, Archer a drawn bow, Mage a clear casting staff/focus, and Cavalry a mounted horizontal charge mass.
- [x] Reject outputs with a background, checkerboard, text/logo, baked UI, extra limbs, duplicate subject, cropped weapon/feet, wrong direction, or a visually ambiguous role. Do not repair a poor source by painting/converting it into a different illustration. All eight inspected outputs met this candidate-only screen; human readability and exact-cell approval remain pending.
- [x] Copy only technically valid candidate bytes to the versioned `docs/images/candidates/role_profiles/` paths; preserve generated source path and SHA in the registry.
- [x] Inspect the retained transparent images at native scale and update the registry with outcome evidence and `GENERATED_CANDIDATE` status.

**Verification:** For all retained candidates, hash readback and alpha/image inspection match the registry. No `res://` path, scene, script, data file, or save data references a candidate.

## Task 3: Hold exact-cell promotion as a user decision

**Files:**
- Modify after user action: `docs/images/candidates/OMENWARD_STORYBOOK_ROLE_PROFILE_TRUE_ALPHA_CANDIDATES_2026-09-01.md`
- Create after user action: `docs/images/approved/OMENWARD_STORYBOOK_ROLE_VISUAL_PROFILE_BATCH_V1.md`

- [ ] Present the eight retained candidates in a labeled contact sheet/individual previews together with their faction, role, path, and consumer.
- [ ] Ask for selection, revision, or rejection per exact candidate. User-approved selections are not inferred from technical validity.
- [ ] On approval, create the canonical batch record with approval source, asset lock, source/output hashes, original-generator provenance, rights ceiling, `512×512`, pivot `(256,448)`, facing requirement, runtime target path, and `BattleFocusView` consumer.
- [ ] Promote approved bytes by copy to new versioned `assets/art/units/` paths; never overwrite old art. Keep unselected candidates in the candidate catalog.

**Verification:** The approved record includes only user-selected files and every canonical runtime byte has a matching hash/source row. If no user selection exists, this task is intentionally blocked and code work must not begin.

## Task 4: Add the RED role-profile rendering contract before code changes

**Files:**
- Create: `tests/headless/storybook_role_visual_profile_contract_test.gd`
- Read/modify later: `scripts/ui/battle_focus_view.gd`
- Read: `tests/headless/close_battlefield_layout_contract_test.gd`
- Read: `tests/headless/single_march_front_contract_test.gd`

- [ ] After Task 3 approval, write a focused GUT test that establishes the exact approved `archetype_id → texture` paths and verifies that unapproved roles never impersonate a Shield Guard.
- [ ] Include invariants for one active front, read-only five-sector top minimap, one fixed tower, no map buildings/construction nodes, and an unobstructed center battle corridor through the existing focused layout tests.
- [ ] Run the new focused test before implementing the mapping and retain the expected RED failure as evidence.

**Verification:** RED failure must identify the missing/incorrect role-profile mapping, not an unrelated parser/import/environment error. Existing single-front layout tests must stay green before the next task.

## Task 5: Implement approved mapping, capture, and verify exact HEAD

**Files:**
- Modify: `scripts/ui/battle_focus_view.gd`
- Modify if required: `scenes/ui/run_command_screen.tscn`
- Modify: `tests/headless/storybook_role_visual_profile_contract_test.gd`
- Modify: `docs/images/approved/OMENWARD_STORYBOOK_ROLE_VISUAL_PROFILE_BATCH_V1.md`
- Create: `docs/qa/captures/single_front_role_profiles/<exact-head>/...`
- Update only if evidence changes: `docs/ACTIVE_CONTEXT.md`

- [ ] Add preloads only for exact approved runtime PNGs and centralize the `archetype_id → approved texture` lookup in `BattleFocusView`.
- [ ] Preserve the procedural/silhouette fallback only for unknown, intentionally non-approved data. It must not disguise a requested role as a Shield Guard.
- [ ] Preserve BattleFocus’s full-width close combat framing, faction facing, one tower, no map buildings, and edge-only terrain bands. Do not change simulation state or combat numbers.
- [ ] Run RED→GREEN focused contract, affected headless layout suite, project-local validator, and the full appropriate test batch.
- [ ] Capture the title and active single-front battle at the exact Git head in a 960×540 viewport. Inspect the capture for correct top one-row minimap, one tower, readable mixed unit roles, and clear central corridor.
- [ ] Commit each coherent change, push the current PR branch, verify CI only at the reported `headRefOid`, and preserve `NOT_RUN` where runtime/human/rights evidence was not actually obtained.

**Verification:** Focused contract and full affected tests are GREEN; image paths/hash record/imports match; a current exact-head technical capture exists. Human readability and asset-rights release review remain explicitly `NOT_RUN`/`REVIEW_PENDING` unless separately performed.

## Review Checklist

- [ ] Every candidate has a real consumer and provenance; no decorative orphan image was created.
- [ ] No user or approved asset was overwritten, and no temporary generated image remains as the only project reference.
- [ ] Candidate approval, canonical registration, Godot binding, runtime capture, and human readability are not conflated.
- [ ] The implementation contains no three-front revival, building map placement, secondary minimap battlefield, extra tower, fake role art, or roulette/gambling drift.
- [ ] The exact-head test/CI result is fresh, with unrun evidence retained accurately.
