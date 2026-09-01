# OMENWARD Storybook Role Profile True-Alpha Candidates — 2026-09-01

```yaml
batch_id: OMW-IMG-20260901-STORYBOOK-ROLE-PROFILE-CANDIDATES-V1
status: GENERATED_CANDIDATE__TECHNICAL_CHECK_PASS__USER_REVIEW_PENDING
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
technical_evidence: COMPLETE_PER_CELL__TRUE_ALPHA_512x512_DERIVATIVES
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

The batch continues to contain **eight role cells**. `OMW-IMG-20260901-ROLE-001`
has one preserved V1 and one V2 replacement candidate because a direct
comparison with `BattleFocusView`'s current `74×74` draw target showed that V1
would render its body at only about 26px wide. The V2 does not add a new role,
system, or consumer; it restores the requested small-battlefield visibility.

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

| Candidate ID | Faction / role | Required readable silhouette | Target candidate path | Status | Prompt delta / provenance / technical review |
| --- | --- | --- | --- | --- | --- |
| `OMW-IMG-20260901-ROLE-001` | Lumern Spear Guard — V1 | navy/ivory/gold infantry; long upright spear; light guard silhouette | `docs/images/candidates/role_profiles/omenward_lumern_spear_guard_storybook_role_candidate_v1.png` | `REJECTED__NARROW_AT_CURRENT_74PX_RENDER_TARGET` | Shared brief + “right-facing infantry guard; unmistakably long upright spear; compact buckler; alert advance.” Source `exec-3dad8832-ff2e-47f6-a063-e6c13d5c2712.png`; source SHA `E5B29EC07952BEC0B1E9C7639BF5C58063BBDF63A1616D798ABCF3E3ED621933`; derivative SHA `16312EEE5E583776A85B6163920969F77A30C989B8B1B897400AEE3027BEAFE8`; RGBA `512×512`, alpha `0..255`, non-transparent coverage `11.428%`, alpha bbox `(166,32)-(347,448)`. Rejection reason: its `181px` normalized art width projects to about `26px` at the actual `74×74` BattleFocus draw target; retain only as traceable review provenance. |
| `OMW-IMG-20260901-ROLE-001-R1` | Lumern Spear Guard — V2 replacement | navy/ivory/gold infantry; low diagonal forward spear; broad grounded advance | `docs/images/candidates/role_profiles/omenward_lumern_spear_guard_storybook_role_candidate_v2.png` | `GENERATED_CANDIDATE__TECHNICAL_PASS__USER_REVIEW_PENDING` | Shared brief + “right-facing broad grounded advance; low diagonal forward spear; no banner/vertical pole; sturdy silhouette at 74px.” Source `exec-ce1014b9-ead2-4cec-982a-ae77078cf414.png`; source SHA `7036FB1EF5BD013E9DBF39CFF3145ABAEB3EAE23997B326CDA887180D66F05CA`; derivative SHA `10FE102E74A71BB2BFBA0CE2CC2A41E978B2CCC0C4AF8BF130C4494A3CAFCD04`; RGBA `512×512`, alpha `0..255`, non-transparent coverage `23.120%`, alpha bbox `(26,47)-(486,448)`, normalized art `460×401`, which projects to a 66px-wide in-game silhouette before any later renderer scale change. |
| `OMW-IMG-20260901-ROLE-002` | Veil Spear Guard | black-purple/dark-red infantry; long rift-tipped spear; jagged carapace | `docs/images/candidates/role_profiles/omenward_veil_spear_guard_storybook_role_candidate_v1.png` | `GENERATED_CANDIDATE__TECHNICAL_PASS__USER_REVIEW_PENDING` | Shared brief + “right-facing aggressive Veil infantry; long diagonally-forward jagged spear; compact buckler; angular carapace.” Source `exec-4ec2d4ce-294c-4d22-bdf3-57d8920ad399.png`; source SHA `B3983D61C8A7A6DE8FAF072396E9E654B44A676CC60B9942D5E6C7D41159F4D1`; derivative SHA `650B3EAA74F9AD6153B0066F90544F8F8F19EA699AB00FC68E88C2C1A80AA0F0`; RGBA `512×512`, alpha `0..255`, non-transparent coverage `19.135%`, alpha bbox `(26,93)-(486,448)` |
| `OMW-IMG-20260901-ROLE-003` | Lumern Archer | navy/ivory archer; unmistakably drawn bow and quiver | `docs/images/candidates/role_profiles/omenward_lumern_archer_storybook_role_candidate_v1.png` | `GENERATED_CANDIDATE__TECHNICAL_PASS__USER_REVIEW_PENDING` | Shared brief + “right-facing bow-drawing archer; bent longbow, nocked arrow, small quiver; no shield.” Source `exec-d69f64ae-b963-4a88-befa-4d980165463c.png`; source SHA `A948FE570723B287E0245C9ADC7BAB0D71486C6F67B2A640172B8191DCEBFBA6`; derivative SHA `B074BABB6B4088CA40C868230C0E79AC15E5857876F87E71BA4C9E8F00730B44`; RGBA `512×512`, alpha `0..255`, non-transparent coverage `21.999%`, alpha bbox `(74,32)-(436,448)` |
| `OMW-IMG-20260901-ROLE-004` | Veil Archer | black-purple/dark-red archer; sinister curved bow, restrained rift glow | `docs/images/candidates/role_profiles/omenward_veil_archer_storybook_role_candidate_v1.png` | `GENERATED_CANDIDATE__TECHNICAL_PASS__USER_REVIEW_PENDING` | Shared brief + “right-facing hostile bow-drawing archer; curved bow, nocked arrow, quiver; limited violet rift detail.” Source `exec-ebeb79b6-d437-413b-9660-c9956f585f68.png`; source SHA `3259C92CAFDF7AFFD9DF4382FB796E8D0EB732E425B47877E918B594C0AB9376`; derivative SHA `611F18C424F65C33F4DA3CED8D487DCC44EC28F6EF64268D5D34BDB2AD59AA0E`; RGBA `512×512`, alpha `0..255`, non-transparent coverage `22.784%`, alpha bbox `(65,32)-(447,448)` |
| `OMW-IMG-20260901-ROLE-005` | Lumern Mage | blue/ivory hooded mage; raised staff/focus with restrained ward light | `docs/images/candidates/role_profiles/omenward_lumern_mage_storybook_role_candidate_v1.png` | `GENERATED_CANDIDATE__TECHNICAL_PASS__USER_REVIEW_PENDING` | Shared brief + “right-facing hooded mage; raised staff/crystal focus; compact blue-white ward halo; no wings/mount.” Source `exec-94e187a7-bdec-46a0-a4d3-e85352053790.png`; source SHA `5679AA88E419CCD7D6A1F1BEF5EC6AB3AF3FD4EE665D1885AB80E699D0F3EC6E`; derivative SHA `1C8CA525896B87D024C4BB880D4249B487F9230B122DFAF52DB55373BE67B155`; RGBA `512×512`, alpha `0..255`, non-transparent coverage `25.710%`, alpha bbox `(92,32)-(421,448)` |
| `OMW-IMG-20260901-ROLE-006` | Veil Mage | black-purple cult mage; raised staff/focus with limited violet rift energy | `docs/images/candidates/role_profiles/omenward_veil_mage_storybook_role_candidate_v1.png` | `GENERATED_CANDIDATE__TECHNICAL_PASS__USER_REVIEW_PENDING` | Shared brief + “right-facing hooded cult mage; raised fractured staff; contained violet rift spell; no wings/mount.” Source `exec-27ef32bf-742b-49bf-99cb-eb4d854c32d0.png`; source SHA `52CF7BCEF63848F718E7DFC82400325EE41650B7C1E49227313A2055513DBBF0`; derivative SHA `EB7166341F4A9F9133FD0423188E9561B5BFEFAF5BCCC05DFEF325E2352B18E3`; RGBA `512×512`, alpha `0..255`, non-transparent coverage `25.291%`, alpha bbox `(72,32)-(440,448)` |
| `OMW-IMG-20260901-ROLE-007` | Lumern Cavalry | blue/ivory armored rider and pale horse; horizontal mounted charge mass | `docs/images/candidates/role_profiles/omenward_lumern_cavalry_storybook_role_candidate_v1.png` | `GENERATED_CANDIDATE__TECHNICAL_PASS__USER_REVIEW_PENDING` | Shared brief + “right-facing armored rider on one pale compact warhorse; horizontal charge; short lance; four readable horse legs.” Source `exec-6a7ba381-0a33-4be2-b49d-1486100934e3.png`; source SHA `7646CD19E1D20E9AFE266BD2237EF9B4926AF25CB93BF5E428A1EA37A0E8F612`; derivative SHA `AC8B3794DC0979CB9575ADFD5E3C19E783A4DCB5D67B8034E7021CC2A788BA20`; RGBA `512×512`, alpha `0..255`, non-transparent coverage `27.119%`, alpha bbox `(26,97)-(486,448)` |
| `OMW-IMG-20260901-ROLE-008` | Veil Cavalry | black-purple armored rider and shadow mount; horizontal mounted charge mass | `docs/images/candidates/role_profiles/omenward_veil_cavalry_storybook_role_candidate_v1.png` | `GENERATED_CANDIDATE__TECHNICAL_PASS__USER_REVIEW_PENDING` | Shared brief + “right-facing armored rider on one shadow warhorse; horizontal charge; short jagged lance; four readable horse legs.” Source `exec-ffd9f807-f7c1-494b-a038-3bdf0e0b660b.png`; source SHA `CF3DEC79B8F705BF3BCA55F6F14A3ABDB420D652201B30400444032FD031A844`; derivative SHA `20F0B064DEA4D6ED8DD6041521BF8BD705C912B6C4523EDF4296BBE67F2BA220`; RGBA `512×512`, alpha `0..255`, non-transparent coverage `27.069%`, alpha bbox `(26,104)-(485,448)` |

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

The image model emitted the first Lumern Spear source as `1024×1536` and the
other sources as `1254×1254`. For each retained candidate, the project-bound
derivative was made only through a non-destructive technical normalization:
alpha-threshold (`>8`) bounds crop with 4px source padding, LANCZOS fit inside
a maximum `460×416` art area, then horizontal centering on a transparent
`512×512` canvas grounded at y=`448`. No inpainting, painting, background
removal, redraw, shadow, compositing, or legacy-asset overwrite occurred.

Failure leaves the output unbound and records `REJECTED` plus the reason in
this document. Technical passing is still only `GENERATED_CANDIDATE`: it is
not user approval, canon registration, runtime verification, human readability
approval, rights clearance, or release pass.

## Rollback and preservation

This batch is additive. Its candidate paths are versioned siblings; no approved
or legacy asset is overwritten. Rejected candidates remain traceable records
outside runtime asset paths. Deleting generated source files or candidate bytes
is not part of this task.
