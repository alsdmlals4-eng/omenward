# OMENWARD Storybook Role Profile True-Alpha Candidates — 2026-09-01

```yaml
batch_id: OMW-IMG-20260901-STORYBOOK-ROLE-PROFILE-CANDIDATES-V1
status: BRIEF_READY__GENERATION_IN_PROGRESS
authorization: USER_CHAT__2026-09-01__"권장안대로 진행해"
authorization_scope: ORIGINAL_GENERATED_CANDIDATES_ONLY__NO_RUNTIME_BINDING
generator: BUILT_IN_IMAGEGEN
source_type: ORIGINAL_GENERATION__PROJECT_VISUAL_DIRECTION_ONLY
consumer_after_exact_user_approval: scripts/ui/battle_focus_view.gd::BattleFocusView
candidate_storage: docs/images/candidates/role_profiles/
runtime_storage: FORBIDDEN_UNTIL_EXACT_USER_APPROVAL_AND_CANON_REGISTRATION
canvas_px: 512x512
runtime_pivot_px: 256x448
facing: RIGHT
background: TRUE_TRANSPARENT_ALPHA_ONLY
technical_evidence: PENDING_PER_CELL
human_asset_review: PENDING
rights_release_review: REVIEW_PENDING__NOT_RELEASE_PASS
```

## Purpose and boundary

This is the bounded, role-first visual candidate batch specified by
`docs/superpowers/specs/2026-09-01-single-front-command-blueprint-design.md`.
It supplies a truthful future visual profile for `BattleFocusView`; it does not
change archetype data, combat rules, the one-front map, tower count, roulette,
save state, or existing approved runtime assets.

The approved Lumern/Veil Shield Guard pair is explicitly **not** in this batch.
No candidate becomes an `assets/art/units/` file or a Godot preload until the
user selects the exact output and its canonical record is created.

## Shared generation brief

```text
USE CASE = Godot close-battle role-profile sprite candidate
STYLE = storybook watercolor SD tactical illustration; delicate ink contour;
        soft painted shading; restrained pixel-tactical crispness; never a
        photorealistic render or a copied game asset
PROPORTION = one full-body 2.5–3-head tactical miniature
CANVAS = 512×512 PNG with true transparent alpha only
COMPOSITION = centered, entire silhouette and weapon visible, feet grounded at
              the intended pivot y=448, no cast shadow, facing right
READ ORDER = role → weapon → scale → faction color → tier → decoration
FORBIDDEN = scenery/background, paper texture, checkerboard, text, logo,
            UI, frame, duplicate character, extra limb, cropped feet/weapon
```

## Exact candidate cells

| Candidate ID | Faction / role | Required readable silhouette | Target candidate path | Status | Generator result / SHA / technical review |
| --- | --- | --- | --- | --- | --- |
| `OMW-IMG-20260901-ROLE-001` | Lumern Spear Guard | navy/ivory/gold infantry; long upright spear; light guard silhouette | `docs/images/candidates/role_profiles/omenward_lumern_spear_guard_storybook_role_candidate_v1.png` | `BRIEF_READY` | Pending |
| `OMW-IMG-20260901-ROLE-002` | Veil Spear Guard | black-purple/dark-red infantry; long rift-tipped spear; jagged carapace | `docs/images/candidates/role_profiles/omenward_veil_spear_guard_storybook_role_candidate_v1.png` | `BRIEF_READY` | Pending |
| `OMW-IMG-20260901-ROLE-003` | Lumern Archer | navy/ivory archer; unmistakably drawn bow and quiver | `docs/images/candidates/role_profiles/omenward_lumern_archer_storybook_role_candidate_v1.png` | `BRIEF_READY` | Pending |
| `OMW-IMG-20260901-ROLE-004` | Veil Archer | black-purple/dark-red archer; sinister curved bow, restrained rift glow | `docs/images/candidates/role_profiles/omenward_veil_archer_storybook_role_candidate_v1.png` | `BRIEF_READY` | Pending |
| `OMW-IMG-20260901-ROLE-005` | Lumern Mage | blue/ivory hooded mage; raised staff/focus with restrained ward light | `docs/images/candidates/role_profiles/omenward_lumern_mage_storybook_role_candidate_v1.png` | `BRIEF_READY` | Pending |
| `OMW-IMG-20260901-ROLE-006` | Veil Mage | black-purple cult mage; raised staff/focus with limited violet rift energy | `docs/images/candidates/role_profiles/omenward_veil_mage_storybook_role_candidate_v1.png` | `BRIEF_READY` | Pending |
| `OMW-IMG-20260901-ROLE-007` | Lumern Cavalry | blue/ivory armored rider and pale horse; horizontal mounted charge mass | `docs/images/candidates/role_profiles/omenward_lumern_cavalry_storybook_role_candidate_v1.png` | `BRIEF_READY` | Pending |
| `OMW-IMG-20260901-ROLE-008` | Veil Cavalry | black-purple armored rider and shadow mount; horizontal mounted charge mass | `docs/images/candidates/role_profiles/omenward_veil_cavalry_storybook_role_candidate_v1.png` | `BRIEF_READY` | Pending |

## Per-cell technical gate

An output can be copied to its target candidate path only when all checks pass:

1. byte readback and SHA-256 are recorded;
2. width and height are exactly `512×512`;
3. it contains a meaningful alpha channel (not a flat opaque square and not a
   checkerboard that pretends to be transparency);
4. one intact full-body subject, role equipment, and feet remain inside the
   image; and
5. native-scale inspection finds no forbidden text, UI, background, duplicate
   subject, cropped extremities, or anatomical defect.

Failure leaves the output unbound and records `REJECTED` plus the reason in
this document. Technical passing is still only `GENERATED_CANDIDATE`: it is
not user approval, canon registration, runtime verification, human readability
approval, rights clearance, or release pass.

## Rollback and preservation

This batch is additive. Its candidate paths are versioned siblings; no approved
or legacy asset is overwritten. Rejected candidates remain traceable records
outside runtime asset paths. Deleting generated source files or candidate bytes
is not part of this task.
