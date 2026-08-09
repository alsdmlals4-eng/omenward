# Godot CSV import artifact hygiene implementation plan

Decision: `OMW-DEC-20260809-TOOLING-GODOT-CSV-IMPORT-ARTIFACT-HYGIENE-V1`

1. RED: dedicated Python contract must fail while `.csv.import` / `.translation` artifacts are tracked and ignore rules are absent.
2. Preserve canonical simulation sources: `robustness_sweep_10000.v1.csv`, `smoke_sweep_2000.v2.csv`, JSON, runners.
3. Remove only Godot-generated `docs/analysis/barracks_simulation/*.csv.import` and `*.translation` files introduced after `41c48182...`.
4. Add path-scoped `.gitignore` rules so future local Godot imports cannot re-stage these generated files.
5. GREEN: dedicated contract + affected repository CI must pass on exact head.
6. Verify protected product paths (`scripts/`, `data/`, `scenes/`, `assets/`, `project.godot`, `addons/`) changed count remains zero.
7. Record same Decision ID in Sheet and perform role-separated review before squash merge.
8. After merge, continue `BARRACKS_ROLE_OUTPUT_RUNTIME_IMPLEMENTATION_REQUIRED`; this hygiene Gate does not claim GUT/HiGodot/Hera implementation completion.
