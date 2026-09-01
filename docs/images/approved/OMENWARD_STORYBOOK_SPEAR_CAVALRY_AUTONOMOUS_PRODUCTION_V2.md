# OMENWARD Storybook Spear and Cavalry Autonomous Production V2

```yaml
asset_set_id: OMW-IMG-20260902-STORYBOOK-SPEAR-CAVALRY-AUTONOMOUS-V2
status: GENERATED_CANDIDATE__TECHNICAL_PASS__STANDING_AUTONOMOUS_RUNTIME_PROMOTION_AUTHORIZED__IMPLEMENTED__MACHINE_VERIFIED__RUNTIME_TECHNICAL_SMOKE_PASS
authorization_source: USER_CHAT__2026-09-02__"앞으로 필요하다고 판단되는 이미지는 별도 승인받지말고 제작해"
exact_user_asset_approval: FALSE
scope: FOUR_REPLACEMENT_ROLE_DERIVATIVES_ONLY
style_reference_lock: USER_APPROVED_ARCHER_MAGE_PAIR_SET_V1
source_record: docs/images/candidates/OMENWARD_STORYBOOK_ROLE_PROFILE_TRUE_ALPHA_CANDIDATES_2026-09-01.md
runtime_consumer: scripts/ui/battle_focus_view.gd::BattleFocusView
runtime_cell_px: 512x512
runtime_pivot_px: 256x448
source_facing: RIGHT
veil_runtime_facing: LEFT__MIRROR_REQUIRED
implementation_issue: Issue #256
runtime: TECHNICAL_SMOKE_PASS__2026-09-02
human_readability: NOT_RUN
release_rights: REVIEW_PENDING__NOT_RELEASE_PASS
```

## Autonomous replacement set

| Faction / role | Generated source master | Source SHA-256 | Candidate derivative | Candidate SHA-256 | Runtime derivative / SHA-256 |
| --- | --- | --- | --- | --- | --- |
| Lumern Spear Guard | `C:/Users/user/.codex/generated_images/01a04af4-0452-7a13-9b6e-1a6077568d72/exec-cd05dee8-7692-4dd0-9f8c-758494ccc187.png` | `30554A9D0A37378800F04C7E176ABD2B69118801E4E02E44089B1BDC7210C2D0` | `docs/images/candidates/role_profiles/omenward_lumern_spear_guard_storybook_role_candidate_v3.png` | `E34E87E0BB9E4028239C865BB1CB4546CF6D3B8BC1EEF31C4200A6EBF54CF11F` | `assets/art/units/lumern_spear_guard_storybook_idle_v3.png` / `E34E87E0BB9E4028239C865BB1CB4546CF6D3B8BC1EEF31C4200A6EBF54CF11F` |
| Veil Spear Guard | `C:/Users/user/.codex/generated_images/01a04af4-0452-7a13-9b6e-1a6077568d72/exec-1a063eaa-b31d-43e6-80b1-a598401669bc.png` | `5E6714367BE5C76582CC047DB8C890EA3CA22BF1294A3AB2813CB12C642224F6` | `docs/images/candidates/role_profiles/omenward_veil_spear_guard_storybook_role_candidate_v2.png` | `FE0BBE1D3803AF79DD44D49C64CBD84078C8459FE1E9C446DB9A967744695805` | `assets/art/units/veil_spear_guard_storybook_idle_v2.png` / `FE0BBE1D3803AF79DD44D49C64CBD84078C8459FE1E9C446DB9A967744695805` |
| Lumern Cavalry | `C:/Users/user/.codex/generated_images/01a04af4-0452-7a13-9b6e-1a6077568d72/exec-a5657521-78fe-42f4-b83a-a6425ad70889.png` | `8B677E87540684DED7B92927E5787D13ECC9F0A70FCF1BF9B89EA3655AAA8A86` | `docs/images/candidates/role_profiles/omenward_lumern_cavalry_storybook_role_candidate_v2.png` | `32979D35D29E7ECD887B8A59FD443AA19D5528C3DCADF8EF6944F156A682A6CD` | `assets/art/units/lumern_cavalry_storybook_idle_v2.png` / `32979D35D29E7ECD887B8A59FD443AA19D5528C3DCADF8EF6944F156A682A6CD` |
| Veil Cavalry | `C:/Users/user/.codex/generated_images/01a04af4-0452-7a13-9b6e-1a6077568d72/exec-63052f01-0980-46a7-afb8-a86057b47934.png` | `D1572003F71BFC16414442979FF0376B359EC23087B34A689503F4C682502C10` | `docs/images/candidates/role_profiles/omenward_veil_cavalry_storybook_role_candidate_v2.png` | `5BA94A8ED5021BBF1A9CD1932386F1DCC3646040AD95D34776E1FBC097A356FF` | `assets/art/units/veil_cavalry_storybook_idle_v2.png` / `5BA94A8ED5021BBF1A9CD1932386F1DCC3646040AD95D34776E1FBC097A356FF` |

## Scope, technique, and evidence ceiling

The exact user-approved Archer/Mage set is the visual reference and remains the
only `USER_APPROVED_EXACT` asset selection in this batch. This document records
the separate standing authority to create and technically promote four required
replacement role sprites without pausing for a duplicate image-creation
approval. It does not convert that authority into a claim that the user has
individually approved any of these four bytes.

The image generator produced opaque light backdrops. To meet the existing
runtime true-alpha contract, technical normalization isolated only neutral,
light pixels connected to each source-image border, then applied the approved
512px cell and `(256,448)` ground-pivot normalization. It did not redraw,
inpaint, recolor, merge, or alter the source character. The candidate record
contains each source and derivative hash for exact rollback.

The actual runtime derivative is an exact byte copy of its candidate derivative.
`BattleFocusView` resolves the two Spear Guard textures during the reproducible
live role-profile fixture. Cavalry texture loading and faction/role resolution
are covered by the headless contract; its six-unit readability capture remains
the next optional human review. This is not individual user-byte approval,
rights release, human readability approval, or release approval. Existing V1/V2
candidate files and legacy runtime textures remain preserved and unmodified.
