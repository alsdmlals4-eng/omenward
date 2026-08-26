# OMENWARD · P0 Unit Idle Runtime Consumer Extension · Execution Packet

```yaml
packet_id: OMW-IMPL-20260826-P0-UNIT-IDLE-RUNTIME-CONSUMER-01
github_issue: 33
approval_basis: USER_CONTINUATION_AND_CODEX_IMPLEMENTATION_AUTHORITY_2026-08-26
scope: NINE_APPROVED_P0_UNIT_PAIRS_EXCLUDING_SHIELD_GUARD_PILOT
status: IN_PROGRESS
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
