# Adversarial Review — Close Single-Front Battlefield Implementation

```yaml
reviewed_at: 2026-08-31 KST
scope: APPROVED_MODULAR_FOUNDATION_AND_TERRITORY_PROPS__BATTLEFOCUSVIEW__TOP_TAB_RAIL
review_status: PASS_5_OF_5__MACHINE_AND_TECHNICAL_RUNTIME_SCOPE_ONLY
human_player_evidence: NOT_RUN
```

## Review loop 1 — route and legacy-consumer regression

**Attack.** Could the close view silently keep sampling the old three-front
backdrop, reintroducing an unsuitable route or baked content?

**Evidence.** `rg` found no `ward_veil_three_lane_backdrop_v1.png` consumer in
`scripts/ui/battle_focus_view.gd`; the focused contract also asserts its
absence. Independent review then found that the retained root `Battlefield`
scene could still draw its legacy backdrop behind the UI. The final boundary
hides that root node in `scenes/main/main.tscn` and removes its `bind_run` call
from `scripts/presentation/scene_binder.gd`. Live runtime readback confirmed
`Battlefield.visible = false` while `BattleFocusViewport.visible = true`.

**Result.** PASS. Only the close view is an active battle renderer; it draws
the approved neutral foundation, then dynamic tower/units, then independent
props.

## Review loop 2 — moving-unit obstruction and wrong-faction placement

**Attack.** Could a future prop-data edit put Lumern in the central/Veil area,
Veil in the central/Lumern area, or place either prop over the soldiers?

**Evidence.** The contract test was intentionally strengthened first and
failed while `is_terrain_prop_placement_allowed()` was absent. The added guard
rejects a Lumern prop at `x_ratio=0.50`, any Veil prop before `0.64`, either
faction's full prop rectangle crossing its side-band boundary, and any prop
rect touching the `y_ratio=0.36..0.80` travel corridor. The test then passed
with valid edge placements and all invalid mutations.

**Result.** PASS. The renderer rejects invalid placement before drawing;
correct draw order alone is not relied upon.

## Review loop 3 — battlefield content and UI-width regression

**Attack.** Could the wider battle panel hide a vertical rail, add a building
or construction node, or multiply the fixed defense tower?

**Evidence.** `close_battlefield_redesign_contract_test.gd`,
`battle_primary_march_minimap_contract_test.gd`, and
`run_command_tab_contract_test.gd` pass. The scene has one `TopTabRail`
`HBoxContainer`, `BattleFocusViewport` at `x16..702`, retains the right-side
minimap, and deletes the old `TabRail` `VBoxContainer`. Source scanning found
no map-level building/node/pad/barricade/river/bridge identifiers in the battle
focus renderer. Existing global-roster and fixed-one-tower tests remain green.

**Result.** PASS. The field’s visual inventory remains terrain, one live tower,
and units only; building interaction stays in its roster surface.

## Review loop 4 — exact asset/provenance mismatch

**Attack.** Could a correct-looking local asset be a different candidate, a
partial set, or a stale imported file?

**Evidence.** All seven repository runtime files hash-match their locked
candidate records. The foundation SHA is
`5568028f5821e0107951e1d8055f9e64616c33654f96c7d117b2979b303bd775`;
each of the six prop SHA values is recorded in
`docs/images/approved/OMENWARD_CLOSE_SINGLE_FRONT_BATTLEFIELD_MODULAR_V1.md`.
Godot reimported the new image files before the focused tests ran.

**Result.** PASS. The exact user-approved foundation and all six props are the
only new runtime copies bound by this change.

## Review loop 5 — integrated runtime and regression sweep

**Attack.** Could static contracts pass while BATTLE never exposes the close
view/minimap, while a reward cannot reach a unit, or while the final guard
breaks unrelated systems?

**Evidence.** In a live Godot 4.7.2 runtime, deterministic roulette seed `4`
reported `중앙 판정: unit · 완성선 1`; its Shield Guard was committed,
after which `BATTLE`, `병력 1/12`, visible battle focus, and visible minimap
were observed. The post-review 960×540 capture also confirmed the root legacy
renderer was hidden. After the renderer and full-rectangle side-band guards,
all 30 headless tests exited `0`.

**Result.** PASS for machine coverage and the stated live technical smoke.

## Ceiling and remaining risk

```text
HUMAN_READABILITY = NOT_RUN
MULTI_UNIT_COMBAT_READABILITY = NOT_RUN
PLAYER_USABILITY = NOT_RUN
DEVICE_RESOLUTION_COVERAGE = NOT_RUN
RELEASE_RIGHTS_REVIEW = PENDING
```

The captured tutorial fixture contains one friendly Shield Guard and no Veil
unit yet. It proves runtime binding and the safety boundary, not a human
judgement that multi-unit combat reads well.
