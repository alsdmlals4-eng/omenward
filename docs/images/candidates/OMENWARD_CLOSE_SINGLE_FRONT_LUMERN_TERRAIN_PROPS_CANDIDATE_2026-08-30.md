# [Candidate] OMENWARD Close Single-Front Lumern Terrain Props

```yaml
asset_set_id: OMW-IMG-20260830-CLOSE-FRONT-LUMERN-PROPS-V1
created_at: 2026-08-30 KST
status: USER_APPROVED_EXACT_CANDIDATE_SET__CANON_REGISTERED__IMPLEMENTED__RUNTIME_TECHNICAL_SMOKE_PASS
generator: BUILT_IN_IMAGEGEN
consumer_candidate: BattleFocusView/TerritoryProps/Lumern
runtime_assets: assets/art/battlefield/props/omenward_lumern_low_slab_cluster_v1.png | assets/art/battlefield/props/omenward_lumern_meadow_bank_v1.png | assets/art/battlefield/props/omenward_lumern_blue_flower_bank_v1.png
runtime: BOUND_TO_BATTLEFOCUSVIEW_TERRITORY_PROPS
human_readability: NOT_RUN
rights_status: GENERATION_PROVENANCE_RECORDED__RELEASE_RIGHTS_REVIEW_PENDING
user_asset_lock: USER_APPROVED_EXACT_LUMERN_PROP_SET_V1
approval_source: USER_CHAT__2026-08-31__"좋아 확정할게"
canon_record: docs/images/approved/OMENWARD_CLOSE_SINGLE_FRONT_BATTLEFIELD_MODULAR_V1.md
```

## Exact candidate files

| Candidate | Role | Source | SHA-256 | Size | Transparency |
| --- | --- | --- | --- | --- | --- |
| `OMW-IMG-20260830-LUMERN-LOW-SLABS-V1` | pale low limestone slabs and blue ward-moss | `C:/Users/user/.codex/generated_images/01a04af4-0452-7a13-9b6e-1a6077568d72/exec-681c0f53-acdc-4438-936f-93ff9814e65d.png` | `35937288B8F69AB5AE0AAFE3E3169D134A837C64650F9D208E8634E939AB3964` | 1536x1024 | verified alpha, four corners alpha 0 |
| `OMW-IMG-20260830-LUMERN-MEADOW-BANK-V1` | low meadow edge, blue shrubs, pebbles | `C:/Users/user/.codex/generated_images/01a04af4-0452-7a13-9b6e-1a6077568d72/exec-ec2a55a1-ee06-4585-bf78-68f52dbfc645.png` | `ADF6685CBE54F4E978632BBC1478047F11B06075F5C06F9F79A240FE3B0F59F8` | 1619x971 | verified alpha, four corners alpha 0 |
| `OMW-IMG-20260830-LUMERN-BLUE-FLOWER-BANK-V1` | low limestone chips, blue flowers, short grass | `C:/Users/user/.codex/generated_images/01a04af4-0452-7a13-9b6e-1a6077568d72/exec-65d9082d-120a-4351-8ba7-ff902effa3b0.png` | `0AB2D0C3CACA27EDC542053308503A265A8DE7DEDAABCA922F8A07DAC44B5DEC` | 1672x941 | verified alpha, four corners alpha 0 |

## Placement contract

- These are independently movable transparent props, never baked into the
  foundation or a route texture.
- Standard Lumern placement is only when front pressure is `< 0.36`; it thins
  during the `0.36..0.46` transition.
- The clear central clash band (`0.46..0.54`) receives no Lumern prop.
- Props belong on the outer edge or low foreground and must not cover the
  active units, one defensive tower, or the continuous readable route.
- Every destination rectangle must stay entirely in the upper `0.00..0.30` or
  lower `0.82..1.00` vertical edge band. The unit-travel corridor
  `0.36..0.80` is forbidden to props regardless of rendering order.
- None is a building, capture marker, resource node, construction slot, or
  tower. Gameplay ownership remains runtime state rather than baked art.

## Completed promotion record

The user locked the **exact three files as a set** on 2026-08-31. Repository
copies, hashes, runtime binding, and the edge-band placement guard are recorded
in the approved asset record. Human readability is still `NOT_RUN`.
