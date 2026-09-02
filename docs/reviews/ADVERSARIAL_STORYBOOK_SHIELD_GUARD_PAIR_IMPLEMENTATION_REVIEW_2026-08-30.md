# Adversarial Review — Storybook Shield Guard Pair Implementation

```yaml
review_id: OMW-REV-20260830-STORYBOOK-SHIELD-GUARD-PAIR-IMPLEMENTATION-01
status: MACHINE_SCOPE_REVIEW_COMPLETE__RUNTIME_AND_HUMAN_EVIDENCE_OPEN
scope: USER_APPROVED_EXACT_LUMERN_VEIL_SHIELD_GUARD_PAIR_ONLY
approval_source: USER_CHAT__2026-08-30__"확정해 진행하자"
implementation_issue: Issue #256
input_state: codex/full-godot-implementation-20260830 worktree
full_scope_loops_completed: 5
machine_clean_exit: true
product_runtime_clean_exit: false
runtime: NOT_RUN
human_readability: NOT_RUN
release_rights: REVIEW_PENDING__NOT_RELEASE_PASS
```

## Scope, protected strengths, and non-goals

The reviewed change binds only the exact user-approved Lumern and Veil
Storybook SD Shield Guard pair as new sibling `512×512` runtime textures. It
preserves the existing simulation, roster rules, save data, other archetype
profiles, legacy textures, and source masters. It does not approve or bind the
remaining 16 source-sheet cells, create an animation atlas, or claim live
runtime/readability/release evidence.

## Full-scope review loops

Each loop re-attacked the user intent, project core, approval/provenance,
runtime consumers, data/schema compatibility, code path, tests, documentation,
rollback, unrelated workstreams, cost, and evidence ceiling. The rows list the
distinct evidence delta rather than treating a single review lens as a loop.

| Loop | Attack and validated result | Approved minimal refinement | Verification / re-attack | Better alternative and long-term result |
|---:|---|---|---|---|
| 1 | **MUST_FIX found:** the approved Veil source already faces left while `UnitView` unconditionally mirrored every Veil texture, causing a double flip in the actual consumer. | Added default-preserving `FactionVisualProfile.idle_mirror_for_veil`; set it to `false` only for `VisualShieldVeil`; amended `UnitView`. | The Shield Guard contract was deliberately RED first, then GREEN; existing Veil profiles keep the default `true` behavior. | A faction-wide reverse rule would regress every existing Veil texture; the per-profile opt-out is the smallest durable change. |
| 2 | **MUST_FIX found:** the current documentation validator still required the prior “all source sheets pending” gate although the approved pair was now bound. | Registered the approved pair, hashes, consumers, direction exception, and the remaining-cell boundary; advanced the current gate only to the remaining cells. | `tools/validate_project_core_docs.py` and its 38 tests passed after a deliberate RED update. | Leaving the old marker would conceal implementation truth; claiming all roles complete would exceed approval. The split status is retained. |
| 3 | **MUST_FIX found:** current summaries still said the open battlefield layout was planning-only/unimplemented despite the global roster and fixed-tower implementation. | Reconciled current routing summaries to `GLOBAL_ROSTER_AND_FIXED_TOWERS__IMPLEMENTED__RUNTIME_NOT_RUN`. | Current-doc validator, routing tests, and protected approval validator passed; historical records remain historical rather than being deleted. | Rewriting dated history would destroy provenance; updating only current owners gives correct routing without erasing history. |
| 4 | No new P0/P1 issue in asset geometry, source binding, battle scene, strategic-map consumer, or command-token consumer. Existing warning output was classified as pre-existing headless dummy-renderer/image-test environment output, not a pass condition. | No code change justified. | All 25 headless Godot contracts passed, including `shield_guard_visual_asset_test.gd`, scene, roster, map, and visual-asset contracts. | Broad renderer replacement or art rework would add risk without evidence; the existing shared `UnitView` path remains the long-term reusable boundary. |
| 5 | No new omission/conflict/duplicate work found across the exact approval record, two repository PNGs, profiles, consumers, current canon, protected manifest, or unrelated open workstreams. | No code change justified. | Asset readback confirmed both PNGs are RGBA `512×512`, alpha extrema `0..255`, and their recorded SHA-256 values. Protected-contract validation, documentation validation, and 556 non-CI Python tests passed. | The only remaining verification gap is actual Omenward live rendering and human readability; using another project's live editor would be invalid, so it remains explicitly open. |

## Decision report

```text
RESOLVED_MUST_FIX = VEIL_LEFT_FACING_SOURCE_DOUBLE_FLIP
RESOLVED_MUST_FIX = CURRENT_CANON_GATE_AND_STATUS_DRIFT
RESOLVED_MUST_FIX = CURRENT_LAYOUT_IMPLEMENTATION_STATUS_DRIFT
NO_MATERIAL_FOLLOWUP = TRUE_FOR_MACHINE_SCOPE
UNRELATED_OPEN_WORKSTREAM_MUTATION = NONE
REMAINING_APPROVED_SCOPE_WORK = LIVE_OMENWARD_RUNTIME_CAPTURE_AND_HUMAN_READABILITY_REVIEW
REMAINING_UNAPPROVED_WORK = 16_STORYBOOK_SOURCE_SHEET_CELLS_REQUIRE_OWN_EXACT_REVIEW
```

The retained live-evidence blocker is precise: the active Godot editor session
belongs to another project, so it was read only and not repurposed. Open the
Omenward project with its live-editor addon to capture the actual Battlefield
and Run Command presentation; only then can `RUNTIME_NOT_RUN` or
`HUMAN_NOT_RUN` be reconsidered.

## Rollback

Rollback is localized and non-destructive: restore the previous Shield Guard
texture paths/pivots in `data/bootstrap_catalog.tres`, restore the prior Run
Command token preload, and remove the two new sibling derivative files. The
legacy runtime textures and external source masters remain intact.
