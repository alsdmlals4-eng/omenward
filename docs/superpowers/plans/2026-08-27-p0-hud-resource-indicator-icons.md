# P0 HUD Resource Indicator Icons · Implementation Plan

**Issue:** #224

## Goal

Use only the already approved Gold and Troop Capacity cleanup masters to add compact visual cues to the existing Stage HUD resource values.

## Scope

- Export local transparent runtime icon derivatives.
- Bind Gold next to the existing Gold number and Troop Capacity next to the existing Food used/cap number.
- Preserve the exact values and existing economy behavior.

## Explicit exclusions

- No inferred pressure-signature mapping: the current wave data has no approved pressure field.
- No building consumer/definition for Command Post, Mana Tower, Special Barracks, or Vault.
- No roulette, battlefield, construction, or balance change.

## Verification

Write a focused Stage HUD resource-icon contract first, observe RED, then export/bind minimally until GREEN. Run the current headless suite, Godot import, and a live HUD capture. Record partial evidence only.
