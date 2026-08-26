# P0 Unit Idle Runtime Geometry Plan

**Goal:** Bind the remaining approved P0 units to the existing shared idle-texture receiver without moving their preserved masters or creating new art.

**Architecture:** A manifest-driven export produces fixed 512×512 transparent cells. `FactionVisualProfile` remains the presentation owner; `UnitView` remains unchanged and consumes the profiles exactly as it did for Shield Guard.

## Steps

1. Add and run a failing headless contract for the nine currently unbound P0 pairs.
2. Export manifest-listed cleanup masters with nearest-neighbour scaling and write the local provenance report.
3. Bind the resulting textures and shared pivot in the bootstrap catalog.
4. Import through Godot, run focused and regression validation, then record evidence in Notion and current-context documentation.
