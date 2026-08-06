# GUT 9.7.1 Vendor Manifest Reconciliation Plan

**Decision:** `OMW-DEC-20260806-TOOLS-GUT-9-7-1-VENDOR-MANIFEST-RECONCILIATION-V1` (`NON_COUNTER`)

**Goal:** Record the exact file-level delta between upstream GUT 9.7.1 and OMENWARD's vendored `addons/gut` tree without modifying or activating the addon.

**Base:** OMENWARD `main` `7588317f294d602cfad5f7f15bfebcf849b8a77b`

**Architecture:** A static JSON manifest pins upstream/project tree SHAs and all 18 changed blobs. A focused validator rejects hidden path drift, code/config/license changes, premature normalization claims, and activation while evidence is incomplete.

## Constraints

- Separate Draft PR based on exact `main`.
- Do not modify `addons/gut`, `project.godot`, Scene, Resource, gameplay code, data, or assets.
- HiGodot remains the only Godot authoring authority.
- GUT activation remains blocked.
- The binary `.fnt` delta must not be normalized without decoding evidence.

## TDD sequence

1. Add RED tests that require a missing validator and manifest.
2. Record the exact 18-path manifest.
3. Implement the minimal static validator.
4. Add adoption note, adversarial review, and CI workflow.
5. Reconstruct exact files and run `py_compile`, focused unittest, contract validation, and blocked-activation proof.
6. Open a Draft PR and synchronize the same Decision ID to Sheet.
