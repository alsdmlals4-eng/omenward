# [Approved] OMENWARD Close Single-Front Battlefield Modular V1

```yaml
asset_bundle_id: OMW-IMG-20260831-CLOSE-FRONT-BATTLEFIELD-MODULAR-V1
approved_at: 2026-08-31 KST
status: USER_APPROVED__CANON_REGISTERED__IMPLEMENTED__RUNTIME_TECHNICAL_SMOKE_PASS
user_approval_source: USER_CHAT__2026-08-31__"좋아 확정할게"
placement_approval_source: USER_CHAT__2026-08-31__"지형지물들은 전선에(병사들 이동)에 방해되지않게 좀 벗어난 위치에만 분포시켜줘."
consumer: scripts/ui/battle_focus_view.gd
scene_surface: scenes/ui/run_command_screen.tscn::BattleFocusViewport
legacy_backdrop_consumer: REMOVED_FROM_BATTLEFOCUSVIEW__FILE_RETAINED
legacy_root_battlefield_renderer: HIDDEN_AND_UNBOUND__NOT_AN_ACTIVE_BATTLE_RENDERER
human_readability: NOT_RUN
rights_status: GENERATION_PROVENANCE_RECORDED__RELEASE_RIGHTS_REVIEW_PENDING
```

## Canonical runtime copies

| Asset | Repository path | SHA-256 | Runtime role |
| --- | --- | --- | --- |
| Foundation | `assets/art/battlefield/omenward_close_single_front_foundation_v1.png` | `5568028f5821e0107951e1d8055f9e64616c33654f96c7d117b2979b303bd775` | Connected neutral ground only |
| Lumern low slabs | `assets/art/battlefield/props/omenward_lumern_low_slab_cluster_v1.png` | `35937288b8f69ab5ae0aafe3e3169d134a837c64650f9d208e8634e939ab3964` | Lumern outer-edge prop |
| Lumern meadow bank | `assets/art/battlefield/props/omenward_lumern_meadow_bank_v1.png` | `adf6685cbe54f4e978632bbc1478047f11b06075f5c06f9f79a240fe3b0f59f8` | Lumern lower-edge prop |
| Lumern blue flowers | `assets/art/battlefield/props/omenward_lumern_blue_flower_bank_v1.png` | `0ab2d0c3caca27edc542053308503a265a8de7dedaabca922f8a07dac44b5dec` | Lumern lower-edge prop |
| Veil rubble | `assets/art/battlefield/props/omenward_veil_rubble_v1.png` | `c1e3e2c61c45e79e0cb598d9f063185d9de3f49bf5b60c006a22d3a04699ccb4` | Veil outer-edge prop |
| Veil crystal cluster | `assets/art/battlefield/props/omenward_veil_crystal_cluster_v1.png` | `7acb51b36d6b56d7ec2085ddd6d83a2bbb79ea55bc61da555026827ced979012` | Veil lower-edge prop |
| Veil thorn brush | `assets/art/battlefield/props/omenward_veil_thorn_brush_v1.png` | `eeabc752e72cacb02a7944cf289cca8382cef85918365a34af757b4ea7a3e1b3` | Veil outer-edge prop |

The exact candidate provenance remains in the three source records under
`docs/images/candidates/`. No legacy backdrop or earlier generated candidate
was overwritten or promoted through this record.

## Runtime placement contract

```text
BATTLEFIELD_FOUNDATION = FULL_BATTLE_FOCUS_RECT
UNIT_TRAVEL_Y_RATIO = 0.36..0.80
PROP_RECT_INTERSECTS_UNIT_TRAVEL_CORRIDOR = FORBIDDEN
LUMERN_PROP_X_RATIO = <= 0.36
VEIL_PROP_X_RATIO = >= 0.64
LUMERN_PROP_RECT_END_X_RATIO = <= 0.36
VEIL_PROP_RECT_START_X_RATIO = >= 0.64
TOP_PROP_SAFE_BAND_Y_RATIO = 0.00..0.30
BOTTOM_PROP_SAFE_BAND_Y_RATIO = 0.82..1.00
BUILDING_MAP_PLACEMENT = FORBIDDEN
FIXED_TOWER_COUNT_PER_ACTIVE_FRONT = 1
```

`BattleFocusView.terrain_prop_layout()` owns six independently movable texture
rectangles. `is_terrain_prop_placement_allowed()` rejects both an incorrect
Lumern/Veil anchor and a rectangle that crosses its side-band boundary or
intersects the unit travel corridor, even if a future placement data edit
becomes invalid. The visual props are
atmosphere only: none represents a building, construction node, capture marker,
resource node, or defense tower.

## Implementation and evidence

- Bound as preloaded assets in `scripts/ui/battle_focus_view.gd`; the old
  `ward_veil_three_lane_backdrop_v1.png` preload is no longer a consumer of the
  close battle view, while its original file remains retained. The root legacy
  `Battlefield` node is deliberately hidden and no longer receives `bind_run`,
  so it cannot render a second wide battlefield behind the close battle view.
- `scenes/ui/run_command_screen.tscn` gives `BattleFocusViewport` `686×302`
  logical pixels at `x=16, y=62`; the matching read-only minimap remains at
  `x=712, y=62, 230×302`. The top `HBoxContainer` holds `내정 / 룰렛 / 전선`.
- Focused contract: `tests/headless/close_battlefield_redesign_contract_test.gd`
  verifies exact asset existence, full-rectangle side-band limits, empty unit
  corridor, one tower boundary, removal of the legacy backdrop consumer and
  standalone clash-circle marker, and the inactive root legacy renderer.
- Full headless suite: 30 scripts exited `0` on 2026-08-31. Existing headless
  Godot teardown leak warnings and existing image-as-`Image` test warnings
  remain warnings, not test failures.
- Live technical smoke: `docs/qa/OMENWARD_CLOSE_SINGLE_FRONT_BATTLEFIELD_RUNTIME_SMOKE_2026-08-31.md`.

This record does **not** claim human readability, player usability, release
rights clearance, device coverage, or final art approval beyond the exact user
locked candidate set.
