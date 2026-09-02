# OMENWARD Five Sequential Front Map Candidates — 2026-09-02

```yaml
batch_id: OMW-IMG-20260902-FIVE-SEQUENTIAL-FRONT-MAPS-V1
status: GENERATED_CANDIDATES__AWAITING_USER_VISUAL_CONFIRMATION
authorization: USER_CHAT__2026-09-02__"전선맵을_5단계로_나누면...하나의_전선을_이기면_다음_전선_맵으로_넘어가는_식" + STANDING_AUTONOMOUS_REQUIRED_IMAGE_PRODUCTION
generator: BUILT_IN_IMAGEGEN
source_type: ORIGINAL_GENERATION__PROJECT_VISUAL_DIRECTION_ONLY
consumer_after_exact_user_confirmation: scripts/ui/battle_focus_view.gd::BattleFocusView
runtime_binding: NOT_BOUND__USER_LOCK_PENDING
current_locked_runtime_foundation: assets/art/battlefield/omenward_close_single_front_foundation_v1.png
replacement_policy: ADDITIVE_VERSIONED_MAP_FOUNDATIONS_ONLY__NO_OVERWRITE_OR_DELETION
canvas_px: 1672x941
aspect_ratio: 16:9
central_travel_corridor: REQUIRED__UNOBSTRUCTED
forbidden: UI / text / logo / unit / character / construction_node / building / wall_across_route / fence / barricade / bridge / river
human_visual_review: AWAITING_USER_CONFIRMATION
runtime_technical_review: NOT_RUN__NO_CANDIDATE_BOUND
rights_release_review: PROVENANCE_RECORDED__RELEASE_RIGHTS_REVIEW_PENDING
```

## Purpose and boundary

`OMW-PLAN-20260902-FIVE-SEQUENTIAL-FRONT-MAPS-01` requires a genuinely distinct
foundation for each sequential battle map rather than one image recolored five
times. These five generated originals are candidate foundations for the one
active `BattleFocusView` only. They do **not** create a second battlefield,
place map buildings, replace the single fixed tower rule, or move the global
building roster onto terrain.

All subjects, props, and strong silhouettes are held out of the central troop
travel corridor. Dynamic Lumern/Veil units and the single fixed tower remain
runtime overlays. The currently user-locked shared foundation remains the
active runtime image until the user selects an exact candidate set and the
separate canon/provenance/runtime gates complete.

## Shared art brief used for generation

```text
STYLE = original storybook watercolor fantasy tactical illustration;
        delicate ink linework on ivory paper; soft SD miniature scale
FORMAT = one opaque 16:9 terrain foundation; no UI, title, text, logo,
         characters, units, creatures, tower, building, construction node,
         map marker, road marker, or baked gameplay state
READABILITY = a broad, unmistakably open horizontal travel corridor occupies
              the central combat band; terrain interest stays at outer bands
CONTINUITY = Ward warmth -> forward meadow -> neutral clash -> Veil dusk ->
             Veil Citadel approach, without changing the one-front rules
```

## Exact candidate record

| Order | Candidate ID / map | Exact generated source | SHA-256 | Intended battle identity | Proposed runtime path after exact confirmation | Status |
|---:|---|---|---|---|---|---|
| 1 | `OMW-IMG-20260902-FRONTMAP-001` / `ward_citadel` (수호 성채) | `C:/Users/user/.codex/generated_images/01a04af4-0452-7a13-9b6e-1a6077568d72/exec-8a374b85-9893-4deb-9985-bceb6e1a0c65.png` | `334A9E969592D2FB7640813EE0C9149BF44556314476A1EA5A02C901C1AB532D` | Warm outer meadow; distant left-side ward watchtower and blue banners; center clear. | `assets/art/battlefield/maps/omenward_ward_citadel_foundation_v1.png` | `GENERATED_CANDIDATE__AWAITING_USER_VISUAL_CONFIRMATION` |
| 2 | `OMW-IMG-20260902-FRONTMAP-002` / `ward_forward` (수호 전진) | `C:/Users/user/.codex/generated_images/01a04af4-0452-7a13-9b6e-1a6077568d72/exec-12ce1180-bbe2-4583-8df1-898ca17d99b1.png` | `FE93BFF602DB31564845669C1ED428E0D0A8C19D8A8559D8B32AD058FC0AFB54` | Open forward meadow; blue-flower/lantern side banks; center clear. | `assets/art/battlefield/maps/omenward_ward_forward_foundation_v1.png` | `GENERATED_CANDIDATE__AWAITING_USER_VISUAL_CONFIRMATION` |
| 3 | `OMW-IMG-20260902-FRONTMAP-003` / `clash` (접전) | `C:/Users/user/.codex/generated_images/01a04af4-0452-7a13-9b6e-1a6077568d72/exec-1a6d608d-ec55-4f98-9bda-dd0aa412f97c.png` | `EE989E9D5E052D3997E285AC73F6A609D249E3B07BA1168313CF48546116D6A2` | Neutral ochre meeting field; faded Ward/Veil border traces and outer-edge abandoned banners; center clear. | `assets/art/battlefield/maps/omenward_clash_foundation_v1.png` | `GENERATED_CANDIDATE__AWAITING_USER_VISUAL_CONFIRMATION` |
| 4 | `OMW-IMG-20260902-FRONTMAP-004` / `veil_forward` (장막 전진) | `C:/Users/user/.codex/generated_images/01a04af4-0452-7a13-9b6e-1a6077568d72/exec-dffec424-ffd7-430c-b269-7dde5754c001.png` | `965A16AEB4B6954A8501E536FAF0914C9D4A43340175D09885D28095D1CAB8AD` | Blue-violet dusk; sparse right/outer Veil crystals and distant rift glow; center clear. | `assets/art/battlefield/maps/omenward_veil_forward_foundation_v1.png` | `GENERATED_CANDIDATE__AWAITING_USER_VISUAL_CONFIRMATION` |
| 5 | `OMW-IMG-20260902-FRONTMAP-005` / `veil_citadel` (베일 성채) | `C:/Users/user/.codex/generated_images/01a04af4-0452-7a13-9b6e-1a6077568d72/exec-2814b217-ca95-4534-9683-174d0122d013.png` | `A69DD76AD3BF956AEE68AF5C355F76E9117E2B598C4CB365544DAFF53565DFDC` | Violet twilight approach; extreme right-horizon citadel silhouette; basalt/crystals only in outer bands; center clear. | `assets/art/battlefield/maps/omenward_veil_citadel_foundation_v1.png` | `GENERATED_CANDIDATE__AWAITING_USER_VISUAL_CONFIRMATION` |

Each source is `1672×941` pixels. Its source path and SHA-256 are the
immutable review identity; no generated file has been copied into the
repository or runtime asset directory in this batch.

## Candidate-by-candidate prompt delta

| Map | Direction added to shared brief |
|---|---|
| 수호 성채 | Bright Ward-Citadel outer meadow, a distant watchtower only on the far left, restrained navy banners, and no wall crossing the field. |
| 수호 전진 | Friendly open forward meadow with low flower and lantern interest at outer bands only; no props in the center. |
| 접전 | Golden trampled meeting field, with faded blue/ivory left traces and muted violet right haze; broken remnants only at far edges. |
| 장막 전진 | Blue-violet dusk progression with sparse dark crystals/twisted brush and a distant rift at right/outer bands only. |
| 베일 성채 | Dramatic violet final approach, with the citadel restricted to the extreme right horizon and no wall across the playable corridor. |

## Required promotion gate

```text
GENERATED_CANDIDATE
  -> USER_VISUAL_CONFIRMATION_OF_EXACT_OUTPUTS
  -> CANON_REGISTERED_WITH_REPOSITORY_COPY_AND_SHA256
  -> BOUND_BY_TERRAIN_ID_IN_BATTLEFOCUSVIEW
  -> MACHINE_VERIFIED
  -> RUNTIME_TECHNICAL_SMOKE
  -> HUMAN_READABILITY_REVIEW
```

Until that sequence occurs, `BattleFocusView.current_terrain_id()` may resolve
the relevant map identity, but the visual binding intentionally remains the
existing approved shared foundation. That separation prevents a generated
candidate from silently overwriting a user-locked visual asset.

## Rollback and preservation

This candidate batch is additive. It preserves the five generated originals,
their hashes, and the existing locked runtime foundation. A rejection or
replacement changes only the future canonical map path/binding; it never
deletes a source image or reintroduces a long continuous map, parallel fronts,
or map-building controls.
