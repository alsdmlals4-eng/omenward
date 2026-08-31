# OMENWARD Title Entry · Locked Asset Machine and Live Technical Smoke

```yaml
record_id: OMW-QA-20260831-TITLE-ENTRY-01
decision_id: OMW-PLAN-20260831-OMEN-WARDEN-TITLE-ENTRY-01
checked_at: 2026-08-31 KST
scope: TITLE_ENTRY__LOCKED_WORDMARK_AND_LAST_ATTACHED_BATTLE_SURGE_BACKGROUND
code_state: USER_APPROVED__CANON_REGISTERED__IMPLEMENTED
machine_evidence: FULL_EXACT_WORKTREE_SUITE_PASS
live_technical_smoke: TITLE_READY_AND_POST_START_TECHNICAL_SMOKE_PASS
human_visual_approval: USER_APPROVED_EXACT_ASSET_SELECTION
human_usability_evidence: NOT_RUN
release_rights_review: RELEASE_BLOCKED_UNVERIFIED
```

## Scope and expected behavior

The title entry owns one real action: `원정 시작`. The game must finish bootstrap
without auto-starting a stage, then start exactly `tutorial_stage` only after that
action. The existing Run Command surface must remain hidden before the action and
appear only after the stage-start signal.

The only runtime title artwork is the user's selected `TITLE-BG-06` battle-surge
background and `TITLE-WORDMARK-01` wordmark. Their canonical paths, byte hashes,
provenance, consumer and rights ceiling are owned by
`docs/images/approved/OMENWARD_TITLE_ENTRY_ASSETS_V1.md`. The former candidate
PNG files, preview scene, preview contract, and superseded captures are deleted;
the non-runtime decision history remains in
`docs/images/candidates/OMENWARD_TITLE_ENTRY_CANDIDATES_2026-08-31.md`.

## Machine evidence

| Check | Result | Evidence |
|---|---|---|
| Locked-asset focused contract | PASS | `tests/headless/title_entry_locked_asset_contract_test.gd` loaded both canonical `Texture2D` resources, instantiated `TitleScreen`, asserted the exact resource paths, and rejected the removed native `Panel/Title` and candidate directory. |
| Focused title-route contract | PASS | `tests/headless/title_entry_contract_test.gd` ran inside the exact working-tree Godot contract suite. |
| Full Godot headless contracts | PASS | 32 / 32 `tests/headless/*_test.gd` scripts completed with 0 failures after the locked-asset binding. |
| Full Python contract suite | PASS | 569 / 569 tests completed successfully against a temporary exact `Base` checkout at `fa69a77a14f923a756064f6ae151d34cadb374f7`; the checkout was removed immediately after the test. |
| Godot editor load/import | PASS_WITH_NON_TITLE_DIAGNOSTICS | Godot 4.7.1 completed editor import with exit code 0. It emitted existing add-on font parsing and exit-time resource/ObjectDB diagnostics; those do not prove visual quality and are retained as non-title diagnostics. |

## Live technical smoke

Godot 4.7.1 ran `res://scenes/main/main.tscn` in this PR worktree at 960×540.

| Step | Assertion / observation | Result |
|---|---|---|
| Initial render | The locked battle-surge background and separate transparent wordmark are visible together in the real `TitleScreen`; the action panel remains lower-center and does not replace the illustration with a full-screen card. | PASS |
| Initial capture | The ready capture is nonblank at 960×540; the automated render inspector reported `possible_clipping: false`. | PASS |
| Post-start capture | A separate capture was retained after the real title action to document the route boundary. It is technical evidence only; the old generic Run Command clipping heuristic is not reclassified as a human-UX result. | RECORDED_NONBLOCKING |
| Transition / diagnostics | Fresh pre-click state was `TitleScreen=true`, `RunCommandScreen=false`, and `StartExpeditionButton.disabled=false`; the real text-target click changed it to `TitleScreen=false` and `RunCommandScreen=true`. Runtime diagnostics reported 0 errors and 0 warnings. | PASS |

## Captures

| State | File | SHA-256 |
|---|---|---|
| Locked title ready | `docs/qa/captures/title_entry/omenward_title_entry_locked_assets_ready_960x540.png` | `0ba8f7503940a5d4e0bd1a48adeaafe343b2d78f296846a8d1b6d9f6d3f89ff3` |
| After `원정 시작` | `docs/qa/captures/title_entry/omenward_title_entry_locked_assets_post_start_960x540.png` | `8d02f27aa5f18fb5b213324543459b9f119af2882674d21d1c5cbb02dedc5dfa` |

## Evidence ceiling and next gate

This is technical execution evidence, not a human player evaluation. It does
not prove copy comprehension, accessibility, art fit at player distance,
performance, commercial terms, legal similarity clearance, platform submission,
or release readiness. Full machine and technical runtime gates are complete for
this working-tree state; human usability, accessibility/performance observation,
remote CI for the next pushed commit, and asset-rights review remain open.
