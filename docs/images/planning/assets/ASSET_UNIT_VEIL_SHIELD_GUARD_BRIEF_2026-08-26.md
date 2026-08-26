# OMENWARD · Veil Shield Guard Runtime Asset Brief

```yaml
asset_brief_id: OMW-ASSET-BRIEF-20260826-VEIL-SHIELD-GUARD-01
asset_family: ASSET-UNIT-VEIL-SHIELD-GUARD
first_generation_target: ASSET-UNIT-VEIL-SHIELD-GUARD-IDLE-V1
status: BRIEF_READY
created_at: 2026-08-26
parent_policy: OMW-VIS-POLICY-20260826-RUNTIME-CONSUMER-ASSET-FIRST-01
paired_with: ASSET-UNIT-LUMERN-SHIELD-GUARD-IDLE-V1
lumern_pair_approval: OMW-ASSET-APPROVAL-20260826-LUMERN-SHIELD-GUARD-IDLE-V1
image_generation: NOT_STARTED
runtime_import: NOT_RUN
```

## 1. Actual consumer

Primary consumer: Battlefield unit renderer replacing the current procedural graybox representation for `shield_guard` + `visual_faction_id=veil`.

Secondary uses: enemy preview / battle readability surfaces that consume the same unit art. Do not create a separate explanation-sheet character.

## 2. Shared archetype contract

Veil Shield Guard must remain recognizably the **same Shield Guard combat archetype** as the approved Lumern pair while not looking like a recolor.

Shared functional read:
- frontline defender;
- oversized frontal defense mass;
- low, stable center of gravity;
- short-range secondary attack element;
- right-facing 3/4 tactical source orientation;
- compatible future animation arrangement and pivot logic.

## 3. Veil visual language

```text
PALETTE = BLACK_PURPLE + DARK_RED + CARAPACE_GRAY + LIMITED_RIFT_GLOW
SHAPE_LANGUAGE = ASYMMETRIC_RIFT + CARAPACE + SPIKE + VOID_APERTURE
ROLE_ANCHOR = BROAD_FRONTAL_CARAPACE_SHIELD
UNIT_PROPORTION = 2.5_TO_3_HEAD_SD_TACTICAL_MINIATURE
```

The unit should look like a Veil translation of the Shield Guard role, not a human knight painted purple.

Primary silhouette:
- broad body-height frontal carapace plate / shield structure;
- defensive mass is still larger and more important than the attack appendage or face;
- asymmetry is allowed but must not destroy the clear forward-facing defense read.

Secondary silhouette:
- compact armored torso / carapace body;
- folded or braced defensive lower limbs;
- one short carapace blade / claw-like attack structure subordinate to the frontal defense mass.

## 4. Attack-element alternatives

### A · Short carapace blade / forelimb — RECOMMENDED

Keeps the shared short stab/slash animation language while translating the human sword into Veil biology.

### B · Short spear-like horn — REJECTED FOR FIRST PAIR

Risks overlapping the Spear Guard role silhouette.

### C · Heavy claw / mace limb — REJECTED FOR FIRST PAIR

Too blunt and risks drifting from the shared Shield Guard attack motion identity.

The exact anatomy remains changeable until the generated image is approved.

## 5. First output only

Produce exactly one isolated idle candidate first.

```text
BACKGROUND = TRANSPARENT
BAKED_TEXT = NONE
BAKED_UI = NONE
BAKED_GROUND_SHADOW = NONE
SOURCE_FACING = RIGHT
POSE = DEFENSIVE_COMBAT_READY_IDLE
OUTPUT_ROLE = RUNTIME_UNIT_SOURCE_CANDIDATE
```

Do not produce a turnaround, comparison board, animation atlas, or explanation sheet as the production output.

## 6. Pair compatibility

The Veil candidate must be judged next to the approved Lumern Shield Guard by these criteria:

- same combat role readable before faction detail;
- same general tactical scale and SD proportion;
- compatible future canvas/pivot/state arrangement;
- clearly distinct faction shape language without relying only on color;
- Veil unit does not become a giant monster or boss;
- shield mass remains primary despite carapace spikes/rift details.

## 7. Pixel / material guardrails

- crisp hard pixel edges;
- consistent pixel density;
- 2–4-tone body/carapace shading with restrained highlight;
- limited rift glow only in small internal cracks/apertures;
- no constant bloom cloud;
- no painterly soft blur;
- no random spikes that obscure the role silhouette.

## 8. Animation boundary

Current common state names remain:

```text
deploy
idle
move
attack_basic
skill_1
hit_light
death
victory
```

First generation = `idle` only.

Exact frame count, FPS, `skill_1` choreography, and final atlas geometry remain `NOT_LOCKED`.

## 9. First candidate acceptance

- [ ] single isolated Veil Shield Guard;
- [ ] transparent background;
- [ ] reads as Shield Guard without labels;
- [ ] broad frontal carapace defense dominates the silhouette;
- [ ] not a recolored human knight;
- [ ] black-purple / dark red / carapace gray hierarchy with restrained rift glow;
- [ ] regular combat unit, not elite/boss visual weight;
- [ ] same approximate tactical scale and source facing as the approved Lumern pair;
- [ ] short attack element does not read as Spear Guard or Greatsword;
- [ ] future animation/pivot pairing remains plausible.

## 10. Production boundary

```text
BRIEF = READY
IMAGE_GENERATION = NOT_STARTED
USER_APPROVAL = NOT_RUN
PIXEL_CLEANUP = NOT_RUN
RUNTIME_IMPORT = NOT_RUN
GODOT_CODEX = NOT_RUN
```
