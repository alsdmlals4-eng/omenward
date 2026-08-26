# OMENWARD · HUD Resource Indicator Vertical Slice · Work Production Input Packet

```yaml
slice_id: OMW-SLICE-20260827-HUD-RESOURCE-INDICATORS-01
baseline: 60d25bf8f8abf9e3e52075bf8e369d5390d6a62e
github_issue: 224
readiness: READY_FOR_SINGLE_CODEX_WINDOW
human_qa: DEFERRED_BY_CURRENT_USER
```

## Player outcome

The player can read current Gold and troop-capacity usage at a glance in the existing tutorial HUD, without changing the economy or construction decision. The icons support the current numeric text; they never replace it.

## Scope

- Add project-local runtime derivatives of the approved Gold Token and Troop Capacity cleanup masters.
- Bind them beside the existing `Gold` and `Food used/cap` values in `StageHud`.
- Preserve the numeric text, game rules, input flow, compact lower deck, and all resource semantics.

## Explicit non-scope / protected scope

- No resource, food, construction, roulette, combat, lane, or balance change.
- No inferred Omen-pressure icon mapping: runtime wave data has no approved pressure field.
- No new consumer for Command Post, Mana Tower, Special Barracks, or Vault.
- No audio/VFX requirement: this static readability slice has no new trigger or feedback event.

## Approved visual inputs

| Requirement | Actual consumer | Approved cleanup master | Runtime output |
|---|---|---|---|
| Gold indicator | `StageHud` Gold value | `.asset-vault/library/ui/tokens/masters/OMENWARD_ASSET_TOKEN_GOLD_V1_CLEANUP_MASTER_V1.png` | compact transparent icon under `assets/art/ui/` |
| Capacity indicator | `StageHud` Food used/cap value | `.asset-vault/library/ui/hud/masters/OMENWARD_ASSET_ICON_TROOP_CAPACITY_V1_CLEANUP_MASTER_V1.png` | compact transparent icon under `assets/art/ui/` |

Both source masters are covered by `OMW-ASSET-AUTO-APPROVAL-20260826-P0-REMAINDER-V1`; provenance, source storage, and Notion approval records already exist. Derivatives must record source/output hashes, preserve binary alpha and transparent corners, and use nearest-neighbour resampling.

## Implementation acceptance

1. Both current numeric resource values remain visible with unchanged meaning.
2. Both icon receivers load local textures; no remote runtime dependency exists.
3. A focused scene contract is written and observed RED before implementation, then passes GREEN.
4. Current deterministic suite, Godot import/parse, headless smoke, and a live HUD capture pass.
5. Runtime evidence stays `PARTIAL`; human/player usability remains `NOT_RUN`.

## Runtime QA scenario

Launch the current tutorial, capture the initial HUD, construct Farm and/or spend Gold through the existing button flow, then verify that both icons persist while the existing numbers and disabled-state behavior update normally. Inspect Hera diagnostics and screenshot clipping only; Hera must not author persistent source.

## Rollback

Remove only the two new runtime derivatives and their HUD receiver nodes/bindings. No data migration or save compatibility action is needed.
