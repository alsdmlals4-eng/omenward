# OMENWARD · P0 Unit Idle Runtime Consumer Extension · Execution Packet

```yaml
packet_id: OMW-IMPL-20260826-P0-UNIT-IDLE-RUNTIME-CONSUMER-01
github_issue: 33
approval_basis: USER_CONTINUATION_AND_CODEX_IMPLEMENTATION_AUTHORITY_2026-08-26
scope: NINE_APPROVED_P0_UNIT_PAIRS_EXCLUDING_SHIELD_GUARD_PILOT
status: COMPLETE__IMPORT_AND_HEADLESS_CONTRACTS_VERIFIED
```

## Goal

Extend the verified shared Shield Guard texture path to the remaining approved P0 unit pairs after normalizing their heterogeneous source geometry.

## In scope

- Produce 18 transparent runtime-only idle cells using the geometry contract and committed provenance run record.
- Bind each existing `FactionVisualProfile` to its correct faction-specific texture and pivot.
- Verify the real bootstrap catalog binding through a focused headless RED→GREEN test.

## Exclusions

- Shield Guard pilot changes, new image generation, animation frames, timing, attack effects, buildings, HUD, battle rules, or runtime readability PASS.

## Acceptance criteria

1. All eighteen profiles resolve their own runtime PNG and the declared common pivot.
2. All cells are `512×512`, fully transparent at the corners, binary-alpha, and derived only from listed cleanup masters using nearest-neighbour scaling.
3. Existing `UnitView` remains the one shared receiver with its existing missing-texture fallback.
4. Focused contract, editor import, relevant regression suite, and smoke execute without a new task-related failure.
5. The local run record and a Notion evidence page are both created and read back.

## Evidence ceiling

Headless/import checks cannot establish battlefield readability or human usability. Both remain `NOT_RUN`.

## Completion evidence

- 18 manifest-listed runtime cells were exported to `assets/art/units/` and imported by Godot 4.7.1 headlessly.
- `docs/images/approved/OMENWARD_P0_UNIT_IDLE_RUNTIME_CELL_RUN_RECORD_2026-08-26.json` records every cleanup-master and output SHA-256, bounds, output size, and pivot.
- The focused `p0_unit_idle_geometry_test.gd` was observed RED before binding and GREEN after binding.
- All current 16 `tests/headless/*_test.gd` files and the 60-frame headless project smoke exited `0`.
- Notion evidence was created and read back: `P0 Unit Idle Runtime Cells V1 · Codex Evidence` (`3c81b237-eb1c-8137-9ff6-c03dfbe1bbec`).
- A live `tests/visual/p0_unit_idle_gallery.tscn` instantiated all 18 profiles through the shared `UnitView`; its final capture and Hera diagnostics reported no clipping signal or runtime error.

Known headless shutdown resource/ObjectDB leak messages remain outside this scope and do not indicate an importer, parser, or contract-test failure.
