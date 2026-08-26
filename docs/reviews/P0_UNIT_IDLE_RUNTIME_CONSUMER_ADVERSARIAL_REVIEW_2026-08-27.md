# P0 Unit Idle Runtime Consumer · Adversarial Review

```yaml
review_id: OMW-REVIEW-20260827-P0-UNIT-IDLE-RUNTIME-01
scope: 18_P0_UNIT_RUNTIME_CELLS_PLUS_SHARED_RENDERER_BINDING
status: PARTIAL_RUNTIME_EVIDENCE__NO_P0_OR_P1_FINDING
```

## Review boundary

This review covers the committed 18-cell P0 runtime import, its bootstrap bindings, and the shared renderer path. It does not turn an automated or agent-observed scene into human-player usability evidence.

## Five review passes

1. **Provenance and mutation attack:** compared the manifest-run record against the immutable cleanup-master inputs. Each cell has a recorded source and output SHA-256, binary alpha, and transparent corners. No vault master was overwritten.
2. **Missing/incorrect binding attack:** ran the new focused contract before binding (RED: all 18 profiles lacked a texture/pivot) and after binding (GREEN). It resolves every listed Lumern/Veil profile to its own `512×512` texture and `(256,448)` pivot.
3. **Shared-renderer and fallback attack:** re-ran the existing Shield Guard consumer contract and the entire current 16-test headless suite. The common `UnitView` route and missing-texture graybox fallback remain intact.
4. **Importer and runtime attack:** Godot 4.7.1 headlessly imported all 18 PNGs. A live tutorial run created two `Unit`/`IdleSprite` nodes; the runtime screenshot showed Veil Shield Guard and newly imported Veil Archer on their lanes without a screenshot-analysis clipping signal. Hera diagnostics reported no errors or warnings.
5. **Authority and drift attack:** checked staged data/asset behavior against the approved scope, ran the 60-frame smoke, and passed the Base project operating-contract and generated-artifact checks after the protected-baseline update.

## Critique–refine

- Removed a Pillow deprecation warning in the export verifier after the first export; the production output algorithm and recorded output hashes are otherwise unchanged.
- Kept Shield Guard on its separately locked pilot geometry instead of silently resampling it into the new cell format.
- Kept runtime evidence at `PARTIAL`: the live scene demonstrated the common renderer with a newly imported Archer, but did not constitute a player study or all-archetype combat readability pass.

## Result

`P0 = none`, `P1 = none`, `P2 = broad interactive readability remains unverified`, `P3 = none`.

The next safe action is a deliberately scoped multi-archetype live readability capture or a user hands-on Godot review. `CURRENT_HUMAN_PLAYER_EVIDENCE` remains `NOT_RUN`.
