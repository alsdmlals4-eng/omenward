# OMENWARD Storybook Archer and Mage Pair Set V1

```yaml
asset_set_id: OMW-IMG-20260902-STORYBOOK-ARCHER-MAGE-PAIR-SET-V1
status: USER_APPROVED__CANON_REGISTERED__IMPLEMENTED__MACHINE_VERIFIED__RUNTIME_TECHNICAL_SMOKE_PASS
approval_source: USER_CHAT__2026-09-02__"궁병,마법사만 이미지 승인"
user_asset_lock: FOUR_EXACT_DERIVATIVES
creation_route: AI_GENERATED__TECHNICAL_RGBA_NORMALIZATION
generator: BUILT_IN_IMAGEGEN
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

## Exact approved derivatives

| Faction / role | Approved candidate | Candidate SHA-256 | Runtime derivative / SHA-256 |
| --- | --- | --- | --- |
| Lumern Archer | `docs/images/candidates/role_profiles/omenward_lumern_archer_storybook_role_candidate_v1.png` | `B074BABB6B4088CA40C868230C0E79AC15E5857876F87E71BA4C9E8F00730B44` | `assets/art/units/lumern_archer_storybook_idle_v1.png` / `B074BABB6B4088CA40C868230C0E79AC15E5857876F87E71BA4C9E8F00730B44` |
| Veil Archer | `docs/images/candidates/role_profiles/omenward_veil_archer_storybook_role_candidate_v1.png` | `611F18C424F65C33F4DA3CED8D487DCC44EC28F6EF64268D5D34BDB2AD59AA0E` | `assets/art/units/veil_archer_storybook_idle_v1.png` / `611F18C424F65C33F4DA3CED8D487DCC44EC28F6EF64268D5D34BDB2AD59AA0E` |
| Lumern Mage | `docs/images/candidates/role_profiles/omenward_lumern_mage_storybook_role_candidate_v1.png` | `1C8CA525896B87D024C4BB880D4249B487F9230B122DFAF52DB55373BE67B155` | `assets/art/units/lumern_mage_storybook_idle_v1.png` / `1C8CA525896B87D024C4BB880D4249B487F9230B122DFAF52DB55373BE67B155` |
| Veil Mage | `docs/images/candidates/role_profiles/omenward_veil_mage_storybook_role_candidate_v1.png` | `EB7166341F4A9F9133FD0423188E9561B5BFEFAF5BCCC05DFEF325E2352B18E3` | `assets/art/units/veil_mage_storybook_idle_v1.png` / `EB7166341F4A9F9133FD0423188E9561B5BFEFAF5BCCC05DFEF325E2352B18E3` |

## Runtime evidence

`BattleFocusView` resolves the exact role/faction texture rather than using a
Shield Guard stand-in. The reproducible Godot fixture draws both approved Archer
and Mage pairs in the actual `RunCommandScreen` BATTLE/전선 surface with the
single-row march minimap and fixed tower. The capture and its machine/runtime
evidence are owned by
`docs/qa/OMENWARD_STORYBOOK_ROLE_PROFILE_BATTLEFOCUS_RUNTIME_2026-09-02.md`.

## Scope and rollback

This record locks only the four listed bytes. It authorizes their copy into
new sibling runtime paths and role-specific BattleFocus binding. Existing
legacy idle textures remain untouched. The archived Spear Guard and Cavalry
candidates are not approved and cannot be selected as a fallback.

Rollback is a targeted binding reversal: remove only these four sibling
runtime derivatives and restore the prior profile references. Candidate bytes,
their source-master records, and all unrelated unit assets remain preserved.
