# OMENWARD Storybook Role Profile True-Alpha Candidates — 2026-09-01

```yaml
batch_id: OMW-IMG-20260901-STORYBOOK-ROLE-PROFILE-CANDIDATES-V1
status: LUMERN_ARCHER_MAGE_EXACT_USER_APPROVED__VEIL_MONSTER_ROLE_VARIANTS_STANDING_AUTONOMOUS_RUNTIME_PROMOTION_AUTHORIZED
authorization: USER_CHAT__2026-09-02__"궁병,마법사만 이미지 승인" + "앞으로 필요하다고 판단되는 이미지는 별도 승인받지말고 제작해" + "베일쪽이 너무 인간스러워졌다 좀 더 몬스터 느낌나게"
authorization_scope: LUMERN_ARCHER_MAGE_EXACT_USER_APPROVAL__SPEAR_CAVALRY_AUTONOMOUS_REGENERATION__VEIL_MONSTER_VARIANTS__NO_LEGACY_CANDIDATE_RUNTIME_BINDING
generator: BUILT_IN_IMAGEGEN
source_type: ORIGINAL_GENERATION__PROJECT_VISUAL_DIRECTION_ONLY
consumer_after_exact_user_approval: scripts/ui/battle_focus_view.gd::BattleFocusView
candidate_storage: docs/images/candidates/role_profiles/
runtime_storage: USER_APPROVED_EXACT_OR_STANDING_AUTONOMOUS_AUTHORIZATION__CANON_RECORD_REQUIRED
canvas_px: 512x512
runtime_pivot_px: 256x448
facing: RIGHT
background: TRUE_TRANSPARENT_ALPHA_ONLY
technical_evidence: COMPLETE_PER_CELL__TRUE_ALPHA_512x512_DERIVATIVES
human_asset_review: LUMERN_ARCHER_MAGE_EXACT_APPROVED__VEIL_MONSTER_VARIANTS_STANDING_AUTONOMOUS_PROMOTION__READABILITY_NOT_RUN
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
user selects the exact output or grants standing autonomous image authority,
and its canonical record is created.

The batch continues to contain **eight role cells**. `OMW-IMG-20260901-ROLE-001`
has one preserved V1 and one V2 replacement candidate because a direct
comparison with `BattleFocusView`'s former `74×74` draw target showed that V1
would render its body at only about 26px wide. The V2 does not add a new role,
system, or consumer; it restores the requested small-battlefield visibility.

## 2026-09-02 user selection and standing image-production authority

The user selected the exact Lumern/Veil Archer and Lumern/Veil Mage V1
derivatives as the only approved outputs from this first batch. Their canonical
registration and BattleFocus binding are authorized. The user also explicitly
authorized autonomous creation of future required images, but did **not**
approve either existing Spear Guard or Cavalry output. Those four retained
legacy candidates remain outside runtime paths and are superseded for visual
style alignment only; their bytes and provenance remain intact.

The replacement scope is deliberately narrow: four new full-body role sprites
(Lumern/Veil Spear Guard and Lumern/Veil Cavalry) that use the approved
Archer/Mage pair as local style references only. It cannot alter combat stats,
the one-front route, tower count, building system, roulette, save data, or
other unit roles. Each replacement still requires the technical gate below,
canonical provenance record, Godot binding, and separate runtime evidence.

### 2026-09-02 Veil monster-direction correction

The user identified that the active Veil Spear Guard, Archer, Cavalry, and Mage
still read as human soldiers. The latest direction supersedes only their
**active runtime selection**: each replacement retains its role weapon,
small-scale readability, transparent `512×512` cell, `(256,448)` ground pivot,
and right-facing source convention, while removing human skin, hair, and face
readability in favor of a black void aperture, horned asymmetrical carapace,
claws or digitigrade legs, and restrained violet rift cracks.

The original selected Veil Archer/Mage V1 bytes and standing-authority Veil
Spear/Cavalry V2 bytes remain immutable historical provenance. They are not
deleted and are no longer active BattleFocus runtime bindings. The user has
already granted standing image-production authority, so the four new candidates
do not claim a second per-byte user selection; their actual consumer, hashes,
and technical/runtime evidence are recorded separately.

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
| `OMW-IMG-20260901-ROLE-001` | Lumern Spear Guard — V1 | navy/ivory/gold infantry; long upright spear; light guard silhouette | `docs/images/candidates/role_profiles/omenward_lumern_spear_guard_storybook_role_candidate_v1.png` | `REJECTED__NARROW_AT_FORMER_74PX_RENDER_TARGET` | Shared brief + “right-facing infantry guard; unmistakably long upright spear; compact buckler; alert advance.” Source `exec-3dad8832-ff2e-47f6-a063-e6c13d5c2712.png`; source SHA `E5B29EC07952BEC0B1E9C7639BF5C58063BBDF63A1616D798ABCF3E3ED621933`; derivative SHA `16312EEE5E583776A85B6163920969F77A30C989B8B1B897400AEE3027BEAFE8`; RGBA `512×512`, alpha `0..255`, non-transparent coverage `11.428%`, alpha bbox `(166,32)-(347,448)`. Rejection reason: its `181px` normalized art width projected to about `26px` at the former `74×74` BattleFocus draw target; retain only as traceable review provenance. |
| `OMW-IMG-20260901-ROLE-001-R1` | Lumern Spear Guard — V2 replacement | navy/ivory/gold infantry; low diagonal forward spear; broad grounded advance | `docs/images/candidates/role_profiles/omenward_lumern_spear_guard_storybook_role_candidate_v2.png` | `REJECTED_FOR_STYLE_ALIGNMENT__REGENERATION_AUTHORIZED` | Preserved V2 trace record. It passed its original geometry check but does not match the exact user-approved Archer/Mage line weight and watercolor treatment closely enough. It must never bind at runtime. |
| `OMW-IMG-20260901-ROLE-002` | Veil Spear Guard | black-purple/dark-red infantry; long rift-tipped spear; jagged carapace | `docs/images/candidates/role_profiles/omenward_veil_spear_guard_storybook_role_candidate_v1.png` | `REJECTED_FOR_STYLE_ALIGNMENT__REGENERATION_AUTHORIZED` | Preserved V1 trace record. It must never bind at runtime. |
| `OMW-IMG-20260901-ROLE-003` | Lumern Archer | navy/ivory archer; unmistakably drawn bow and quiver | `docs/images/candidates/role_profiles/omenward_lumern_archer_storybook_role_candidate_v1.png` | `USER_APPROVED__CANON_PROMOTION_AUTHORIZED` | Exact user-approved candidate. Source `exec-d69f64ae-b963-4a88-befa-4d980165463c.png`; derivative SHA `B074BABB6B4088CA40C868230C0E79AC15E5857876F87E71BA4C9E8F00730B44`; RGBA `512×512`, alpha bbox `(74,32)-(436,448)`. |
| `OMW-IMG-20260901-ROLE-004` | Veil Archer | black-purple/dark-red archer; sinister curved bow, restrained rift glow | `docs/images/candidates/role_profiles/omenward_veil_archer_storybook_role_candidate_v1.png` | `USER_APPROVED__CANON_PROMOTION_AUTHORIZED` | Exact user-approved candidate. Source `exec-ebeb79b6-d437-413b-9660-c9956f585f68.png`; derivative SHA `611F18C424F65C33F4DA3CED8D487DCC44EC28F6EF64268D5D34BDB2AD59AA0E`; RGBA `512×512`, alpha bbox `(65,32)-(447,448)`. |
| `OMW-IMG-20260901-ROLE-005` | Lumern Mage | blue/ivory hooded mage; raised staff/focus with restrained ward light | `docs/images/candidates/role_profiles/omenward_lumern_mage_storybook_role_candidate_v1.png` | `USER_APPROVED__CANON_PROMOTION_AUTHORIZED` | Exact user-approved candidate. Source `exec-94e187a7-bdec-46a0-a4d3-e85352053790.png`; derivative SHA `1C8CA525896B87D024C4BB880D4249B487F9230B122DFAF52DB55373BE67B155`; RGBA `512×512`, alpha bbox `(92,32)-(421,448)`. |
| `OMW-IMG-20260901-ROLE-006` | Veil Mage | black-purple cult mage; raised staff/focus with limited violet rift energy | `docs/images/candidates/role_profiles/omenward_veil_mage_storybook_role_candidate_v1.png` | `USER_APPROVED__CANON_PROMOTION_AUTHORIZED` | Exact user-approved candidate. Source `exec-27ef32bf-742b-49bf-99cb-eb4d854c32d0.png`; derivative SHA `EB7166341F4A9F9133FD0423188E9561B5BFEFAF5BCCC05DFEF325E2352B18E3`; RGBA `512×512`, alpha bbox `(72,32)-(440,448)`. |
| `OMW-IMG-20260901-ROLE-007` | Lumern Cavalry | blue/ivory armored rider and pale horse; horizontal mounted charge mass | `docs/images/candidates/role_profiles/omenward_lumern_cavalry_storybook_role_candidate_v1.png` | `REJECTED_FOR_STYLE_ALIGNMENT__REGENERATION_AUTHORIZED` | Preserved V1 trace record. It must never bind at runtime. |
| `OMW-IMG-20260901-ROLE-008` | Veil Cavalry | black-purple armored rider and shadow mount; horizontal mounted charge mass | `docs/images/candidates/role_profiles/omenward_veil_cavalry_storybook_role_candidate_v1.png` | `REJECTED_FOR_STYLE_ALIGNMENT__REGENERATION_AUTHORIZED` | Preserved V1 trace record. It must never bind at runtime. |
| `OMW-IMG-20260902-ROLE-001` | Lumern Spear Guard — V3 | navy/ivory/gold infantry; low diagonal forward spear; broad grounded advance | `docs/images/candidates/role_profiles/omenward_lumern_spear_guard_storybook_role_candidate_v3.png` | `GENERATED_CANDIDATE__TECHNICAL_PASS__STANDING_AUTONOMOUS_RUNTIME_PROMOTION_AUTHORIZED` | New style-aligned source `exec-cd05dee8-7692-4dd0-9f8c-758494ccc187.png`; source SHA `30554A9D0A37378800F04C7E176ABD2B69118801E4E02E44089B1BDC7210C2D0`; derivative SHA `E34E87E0BB9E4028239C865BB1CB4546CF6D3B8BC1EEF31C4200A6EBF54CF11F`; RGBA `512×512`, alpha `0..255`, coverage `23.448%`, alpha bbox `(27,94)-(485,447)`, normalized art `460×355`. |
| `OMW-IMG-20260902-ROLE-002` | Veil Spear Guard — V2 | black-purple/dark-red infantry; low diagonal rift spear; broad grounded advance | `docs/images/candidates/role_profiles/omenward_veil_spear_guard_storybook_role_candidate_v2.png` | `GENERATED_CANDIDATE__TECHNICAL_PASS__STANDING_AUTONOMOUS_RUNTIME_PROMOTION_AUTHORIZED` | New style-aligned source `exec-1a063eaa-b31d-43e6-80b1-a598401669bc.png`; source SHA `5E6714367BE5C76582CC047DB8C890EA3CA22BF1294A3AB2813CB12C642224F6`; derivative SHA `FE0BBE1D3803AF79DD44D49C64CBD84078C8459FE1E9C446DB9A967744695805`; RGBA `512×512`, alpha `0..255`, coverage `22.923%`, alpha bbox `(27,107)-(485,447)`, normalized art `460×342`. |
| `OMW-IMG-20260902-ROLE-003` | Lumern Cavalry — V2 | blue/ivory rider and pale horse; compact horizontal charge | `docs/images/candidates/role_profiles/omenward_lumern_cavalry_storybook_role_candidate_v2.png` | `GENERATED_CANDIDATE__TECHNICAL_PASS__STANDING_AUTONOMOUS_RUNTIME_PROMOTION_AUTHORIZED` | New style-aligned source `exec-a5657521-78fe-42f4-b83a-a6425ad70889.png`; source SHA `8B677E87540684DED7B92927E5787D13ECC9F0A70FCF1BF9B89EA3655AAA8A86`; derivative SHA `32979D35D29E7ECD887B8A59FD443AA19D5528C3DCADF8EF6944F156A682A6CD`; RGBA `512×512`, alpha `0..255`, coverage `30.097%`, alpha bbox `(27,69)-(485,447)`, normalized art `460×380`. |
| `OMW-IMG-20260902-ROLE-004` | Veil Cavalry — V2 | black-purple rider and shadow horse; compact horizontal charge | `docs/images/candidates/role_profiles/omenward_veil_cavalry_storybook_role_candidate_v2.png` | `GENERATED_CANDIDATE__TECHNICAL_PASS__STANDING_AUTONOMOUS_RUNTIME_PROMOTION_AUTHORIZED` | New style-aligned source `exec-63052f01-0980-46a7-afb8-a86057b47934.png`; source SHA `D1572003F71BFC16414442979FF0376B359EC23087B34A689503F4C682502C10`; derivative SHA `5BA94A8ED5021BBF1A9CD1932386F1DCC3646040AD95D34776E1FBC097A356FF`; RGBA `512×512`, alpha `0..255`, coverage `26.284%`, alpha bbox `(27,94)-(485,447)`, normalized art `460×355`. |
| `OMW-IMG-20260902-VEIL-001` | Veil Spear Guard — V3 monster variant | faceless horned carapace infantry; clawed feet; low rift spear and compact shield | `docs/images/candidates/role_profiles/omenward_veil_spear_guard_storybook_role_candidate_v3.png` | `GENERATED_CANDIDATE__TECHNICAL_PASS__STANDING_AUTONOMOUS_RUNTIME_PROMOTION_AUTHORIZED` | User-directed non-human replacement source `exec-3595a016-30c3-47eb-ad15-3b93dc309143.png`; source SHA `B564789A57C2AFEB14A31CCACE979465FB7740FCA4B21355994E57918A4B4FA7`; derivative SHA `9121E98F28D4D93E9443A2D8EA72B745FDDC234AEABDC49AF6C68C7886C5A5E3`; RGBA `512×512`, alpha bbox `(26,33)-(486,448)`, normalized art `460×415`. |
| `OMW-IMG-20260902-VEIL-002` | Veil Archer — V2 monster variant | void-aperture horned predator; chitin bow and drawn rift arrow | `docs/images/candidates/role_profiles/omenward_veil_archer_storybook_role_candidate_v2.png` | `GENERATED_CANDIDATE__TECHNICAL_PASS__STANDING_AUTONOMOUS_RUNTIME_PROMOTION_AUTHORIZED` | User-directed non-human replacement source `exec-5834346c-8b65-4155-b69b-01f00f054443.png`; source SHA `3996FAF41E340BDA078DB40227AFB654294AD45638F2C347D8F8331FF76E43D3`; derivative SHA `36F6BEC8FDD3B8122FA95635D38B9D7D3951EAE5B335934B66F05E3B8320B74A`; RGBA `512×512`, alpha bbox `(90,32)-(457,443)`, normalized art `405×416`. |
| `OMW-IMG-20260902-VEIL-003` | Veil Cavalry — V3 monster variant | horned void rider on a clawed rift beast; low charging rift lance | `docs/images/candidates/role_profiles/omenward_veil_cavalry_storybook_role_candidate_v3.png` | `GENERATED_CANDIDATE__TECHNICAL_PASS__STANDING_AUTONOMOUS_RUNTIME_PROMOTION_AUTHORIZED` | User-directed non-human replacement source `exec-bd28a6d1-7a4c-4d37-9c0d-d58442ba3cf5.png`; source SHA `7EF82220EC41BC7DDC6DE00D76D02BE96A9C03E9B448FB5852F054C33C9046C1`; derivative SHA `D6063AC0C6E16C5BBED7FC838D99556BFA6560A29519A7D84A3191E7D89B0D35`; RGBA `512×512`, alpha bbox `(26,142)-(486,448)`, normalized art `460×306`. |
| `OMW-IMG-20260902-VEIL-004` | Veil Mage — V2 monster variant | horned void aperture; clawed spellcaster with a fractured rift staff | `docs/images/candidates/role_profiles/omenward_veil_mage_storybook_role_candidate_v2.png` | `GENERATED_CANDIDATE__TECHNICAL_PASS__STANDING_AUTONOMOUS_RUNTIME_PROMOTION_AUTHORIZED` | User-directed non-human replacement source `exec-7f566476-da2e-43a1-a083-2eda3c8b41a0.png`; source SHA `47E5177FD13C5097292304D4FE9CAD692CA3AC5BBB941A92569CEF3189689D50`; derivative SHA `A2E1071B0A81FA6D3ED1AC36C88816F8B5B7E36F165D27F944F5EE0FBBAAD475`; RGBA `512×512`, alpha bbox `(85,32)-(426,448)`, normalized art `341×416`. |

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

The initial 2026-09-01 sources used their existing true alpha. The 2026-09-02
replacement sources were returned by the image model as opaque, light
checkerboard-like backdrops despite the transparent-background request. For
those four sources only, the technical normalization first removed pixels that
were connected to the source image border and met the neutral-light-background
test (`min RGB ≥ 205`, channel spread `≤ 24`); it preserved the source subject
pixels without inpainting, redrawing, recoloring, or compositing. It then used
the same 4px bounds padding, LANCZOS fit inside a maximum `460×416` art area,
and horizontal centering on a transparent `512×512` canvas grounded at
y=`448`. The resulting outputs have independently verified `0..255` alpha.

Failure leaves the output unbound and records `REJECTED` plus the reason in
this document. Technical passing is still only `GENERATED_CANDIDATE`: it is
not user approval, canon registration, runtime verification, human readability
approval, rights clearance, or release pass.

## Rollback and preservation

This batch is additive. Its candidate paths are versioned siblings; no approved
or legacy asset is overwritten. Rejected candidates remain traceable records
outside runtime asset paths. Deleting generated source files or candidate bytes
is not part of this task.
