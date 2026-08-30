# [Candidate] OMENWARD Single March Front Terrain

```yaml
asset_id: OMW-IMG-20260830-SINGLE-MARCH-FRONT-TERRAIN-V1
created_at: 2026-08-30 KST
status: GENERATED_CANDIDATE__USER_REVIEW_PENDING
generator: BUILT_IN_IMAGEGEN
source_path: C:/Users/user/.codex/generated_images/01a04af4-0452-7a13-9b6e-1a6077568d72/exec-df06f687-762f-43c5-a558-de88db60dae0.png
source_sha256: F0528A0B02E355BD2ACBD8D9AA704A1333026C6A94C59947DE27B6814D6D24F0
source_dimensions_px: 1672x941
consumer_candidate: scenes/battle/battlefield.tscn/Backdrop
runtime_asset: NONE
runtime: NOT_IMPLEMENTED
human_readability: NOT_RUN
rights_status: GENERATION_PROVENANCE_RECORDED__RELEASE_RIGHTS_REVIEW_PENDING
user_asset_lock: NONE
approval_source: NONE
```

## Purpose and visual fit

This is an original terrain-only candidate for the approved single marching
front. It is intended to replace only the *visual ground plate* after an
exact-user asset lock; route ownership, the one tower, unit placement, and all
interaction state remain Godot runtime presentation.

The candidate emphasizes a single wide, uninterrupted left-to-right route
with a cool Ward treatment on the left, neutral central Clash treatment, and a
restrained Veil treatment on the right. It deliberately has no river, chasm,
bridge, branch, parallel road, UI, unit, written label, or baked tower.

```text
WARD_CITADEL -> WARD_FORWARD -> CLASH -> VEIL_FORWARD -> VEIL_CITADEL
ONE_CONTINUOUS_ROUTE = REQUIRED
BATTLEFIELD_RUNTIME_CONTENT = TERRAIN + ONE_DYNAMIC_TOWER + DYNAMIC_UNITS
BUILDINGS_OR_CONSTRUCTION_NODES = FORBIDDEN
```

## Exact generation brief

The source was generated as a 16:9 original storybook-watercolor tactical
terrain plate. It requests a smooth, traversable center road; rich but
non-blocking edge terrain; blue/ivory Ward atmosphere at left; violet Veil
atmosphere at right; and three terrain-lighting clearings that correspond to
Ward Forward, Clash, and Veil Forward. It expressly forbids castles, towers,
forts, buildings, walls, gates, bridges, water, split/parallel routes,
characters, UI, text, logos, and watermarks.

## Promotion boundary

- This file is a **preview provenance record**, not an approved asset catalog
  entry and not a runtime reference.
- The original remains at the recorded generated-image source path. No runtime
  asset has been copied into `assets/`, and no scene texture has changed.
- Existing approved backdrop and unit assets remain untouched.
- Machine tests do not establish source style fit, player readability,
  platform compatibility, release rights, or human UX.

## Required next gate

```text
GENERATED_CANDIDATE__USER_REVIEW_PENDING
-> USER_APPROVED_EXACT_CANDIDATE
-> CANON_REGISTERED_WITH_REPOSITORY_COPY_AND_SHA256
-> BOUND_TO_BATTLEFIELD_BACKDROP
-> RUNTIME_RENDERED_AT_960_1280_1920
-> HUMAN_READABILITY_REVIEW
```
