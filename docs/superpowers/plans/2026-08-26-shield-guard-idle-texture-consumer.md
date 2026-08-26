# Shield Guard Idle Texture Consumer Plan

> **Goal:** Deliver the smallest approved visual vertical slice: faction-selected Shield Guard idle textures in the shared battle unit renderer, with graybox fallback.

**Architecture:** `FactionVisualProfile` remains the faction-only presentation owner. `UnitView` remains the single shared renderer and decides between its `Sprite2D` receiver and existing procedural draw fallback. Gameplay and animation contracts remain untouched.

**Verification:** focused RED→GREEN asset test, scene contract, Godot editor import, and all headless tests.

## Steps

1. Add the failing focused contract test for both runtime files, profile fields, and shared sprite receiver.
2. Copy the locked cleanup-master pair to versioned `res://assets/art/units/` runtime paths and verify exact SHA-256.
3. Add `idle_texture` and `idle_pivot` only to `FactionVisualProfile`; bind the two Shield Guard resources in the bootstrap catalog.
4. Add `IdleSprite` to the common unit scene and select it in `UnitView`, preserving fallback rendering when no texture resolves.
5. Run focused and regression validation; record import-only evidence and synchronize GitHub/Notion before committing.
