# Adversarial Review — Close Single-Front Battlefield Implementation

```yaml
reviewed_at: 2026-08-31 KST
scope: APPROVED_MODULAR_FOUNDATION_AND_TERRITORY_PROPS__BATTLEFOCUSVIEW__TOP_TAB_RAIL__TOP_SINGLE_ROW_MARCH_MINIMAP__NINE_SLOT_CAPTURE_BONUS
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
`HBoxContainer`, `BattleFocusViewport` at `x16..942`, places `MarchMinimap`
as a `926×36` full-width strip at `y62..98`, and deletes the old `TabRail`
`VBoxContainer`. Source scanning found
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

**Evidence.** In the current live Godot 4.7.1 runtime, a deterministic roulette
path was stopped, confirmed, committed, and started through the player-facing
controls. The technical readback then recorded `BATTLE`, `BattleFocusViewport`
visible at `x16,y108,926×256`, and `MarchMinimap` visible at
`x16,y62,926×36`; the current 960×540 capture is nonblank and runtime
diagnostics report zero errors and warnings. After the renderer and
full-rectangle side-band guards, all 30 headless tests exited `0`.

**Result.** PASS for machine coverage and the stated live technical smoke.

## 2026-08-31 continuation — top-strip and capacity correction

### Loop 1 — obsolete right-side layout regression

**Attack.** Could a legacy test or current owner silently retain the compact
right-side minimap after the user fixed the minimap to one top row?

**Evidence.** The former compact-width assertion failed against the revised
scene. It was replaced with a runtime scene contract requiring a `>=900`-wide,
`<=48`-high route strip positioned above a `>=900`-wide battle focus. The
focused contract and the complete 30-test Godot headless sweep pass.

**Result.** PASS. The old geometry cannot regress without a focused failure.

### Loop 2 — incomplete capture-point capacity

**Attack.** Could a player-owned Veil Forward Base be omitted, leaving a
visually documented nine-slot cap but an eight-slot runtime cap?

**Evidence.** A RED `StageRun` contract stabilized Ward Forward, Clash, and
Veil Forward for Lumern; the former implementation returned eight. The current
runtime returns nine, and immediately returns eight after only Veil Forward is
lost. The Front tab copy is contract-checked as `기본 6칸 + 점령지 3곳 (최대 9칸)`.

**Result.** PASS. Calculation, screen copy, and owner documents share the
same three eligible points.

### Loop 3 — minimap becoming a second battle renderer

**Attack.** Could expanding the minimap cause it to duplicate units, strength
totals, or combat effects instead of presenting route context?

**Evidence.** `MarchMinimapView` draws only the five route states, ownership,
the one tower marker, and the current sector. The strength-summary drawing
path was removed; its read-only contract remains green.

**Result.** PASS. The top strip stays a route context, not a second battlefield.

### Loop 4 — player-facing battle transition

**Attack.** Could the revised geometry exist in a scene file but never become
visible during the actual command flow?

**Evidence.** Live Hera control clicked the real `내정 → 룰렛 → 전선` path,
confirmed a result, and started battle. Runtime node readback observed both
the top strip and battle focus visible in `BATTLE`; the legacy root
`Battlefield` remains hidden.

**Result.** PASS for this technical player-path smoke.

### Loop 5 — cross-suite/document and temporary-artifact hygiene

**Attack.** Could a code-green change leave stale current owners, silently
depend on the default Python environment, or leave a Base test checkout?

**Evidence.** Project-owner documents and superseded layout-reference metadata
were reconciled. The provided workspace Python, with an isolated exact-Base
temporary checkout, completed all 569 Python tests; the checkout was verified
clean and removed. No generated project asset or temporary Base directory was
retained.

**Result.** PASS. This is machine/document/runtime technical evidence only;
the ceiling below is unchanged.

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
