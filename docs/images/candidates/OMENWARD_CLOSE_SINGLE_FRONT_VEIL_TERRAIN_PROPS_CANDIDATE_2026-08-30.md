# [Candidate] OMENWARD Close Single-Front Veil Terrain Props

```yaml
asset_set_id: OMW-IMG-20260830-CLOSE-FRONT-VEIL-PROPS-V1
created_at: 2026-08-30 KST
status: USER_APPROVED_EXACT_CANDIDATE_SET__CANON_REGISTERED__IMPLEMENTED__RUNTIME_TECHNICAL_SMOKE_PASS
generator: BUILT_IN_IMAGEGEN
consumer_candidate: BattleFocusView/TerritoryProps/Veil
runtime_assets: assets/art/battlefield/props/omenward_veil_rubble_v1.png | assets/art/battlefield/props/omenward_veil_crystal_cluster_v1.png | assets/art/battlefield/props/omenward_veil_thorn_brush_v1.png
runtime: BOUND_TO_BATTLEFOCUSVIEW_TERRITORY_PROPS
human_readability: NOT_RUN
rights_status: GENERATION_PROVENANCE_RECORDED__RELEASE_RIGHTS_REVIEW_PENDING
user_asset_lock: USER_APPROVED_EXACT_VEIL_PROP_SET_V1
approval_source: USER_CHAT__2026-08-31__"좋아 확정할게"
canon_record: docs/images/approved/OMENWARD_CLOSE_SINGLE_FRONT_BATTLEFIELD_MODULAR_V1.md
```

## Exact candidate files

| Candidate | Role | Source | SHA-256 | Size | Transparency |
| --- | --- | --- | --- | --- | --- |
| `OMW-IMG-20260830-VEIL-FISSURED-RUBBLE-V1` | dark fragmented rubble with restrained violet fissures | `C:/Users/user/.codex/generated_images/01a04af4-0452-7a13-9b6e-1a6077568d72/exec-8d196141-8773-4927-9a7e-6afa4e23a511.png` | `C1E3E2C61C45E79E0CB598D9F063185D9DE3F49BF5B60C006A22D3A04699CCB4` | 1254x1254 | verified alpha, four corners alpha 0 |
| `OMW-IMG-20260830-VEIL-DULL-CRYSTAL-OUTCROP-V1` | dark stone outcrop with non-neon smoky violet crystals | `C:/Users/user/.codex/generated_images/01a04af4-0452-7a13-9b6e-1a6077568d72/exec-4e6ae0b7-deb0-4d24-9594-8620d690d6dc.png` | `7ACB51B36D6B56D7EC2085DDD6D83A2BBB79EA55BC61DA555026827CED979012` | 1536x1024 | verified alpha, four corners alpha 0 |
| `OMW-IMG-20260830-VEIL-THORN-BRUSH-V1` | dark thorn brush with restrained purple edge | `C:/Users/user/.codex/generated_images/01a04af4-0452-7a13-9b6e-1a6077568d72/exec-307bf8c4-cf24-48f3-b7d4-8189cfad1895.png` | `EEABC752E72CACB02A7944CF289CCA8382CEF85918365A34AF757B4EA7A3E1B3` | 1254x1254 | verified alpha, four corners alpha 0 |

## Placement contract

- These are independently movable transparent props, never baked into the
  foundation or a route texture.
- Standard Veil placement begins only beyond front pressure `> 0.64` and
  appears gradually in the `0.54..0.64` transition.
- The clear central clash band (`0.46..0.54`) receives no Veil prop.
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
