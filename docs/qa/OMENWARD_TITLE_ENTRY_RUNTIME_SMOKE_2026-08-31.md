# OMENWARD Title Entry · Machine and Live Technical Smoke

```yaml
record_id: OMW-QA-20260831-TITLE-ENTRY-01
decision_id: OMW-PLAN-20260831-OMEN-WARDEN-TITLE-ENTRY-01
checked_at: 2026-08-31 KST
scope: TITLE_ENTRY__BOOT_TO_TUTORIAL_ROUTE
code_state: IMPLEMENTED
machine_evidence: PASS
live_technical_smoke: PASS
human_usability_evidence: NOT_RUN
candidate_asset_state: GENERATED_CANDIDATE__NOT_BOUND
release_rights_review: NOT_RUN
```

## Scope and expected behavior

The title entry owns one real action: `원정 시작`. The game must finish bootstrap
without auto-starting a stage, then start exactly `tutorial_stage` only after that
action. The existing Run Command surface must remain hidden before the action and
appear only after the stage-start signal.

This record covers the native functional title surface. `TITLE-BG-01` and
`TITLE-SEAL-01` are deliberately excluded from runtime binding and remain subject
to the user visual `LOCK / REVISE / REJECT` gate in
`docs/images/candidates/OMENWARD_TITLE_ENTRY_CANDIDATES_2026-08-31.md`.

## Machine evidence

| Check | Result | Evidence |
|---|---|---|
| Focused title-entry contract | PASS | `tests/headless/title_entry_contract_test.gd` loads the title scene, asserts the boot-hidden Run Command surface, the sole real `원정 시작` action, and absence of fake Continue/Settings surfaces. |
| Full Godot headless contracts | PASS | 31 / 31 `tests/headless/*_test.gd` scripts completed with 0 failures. |
| Full Python contract suite | PASS | 569 / 569 tests completed successfully after a temporary exact `Base` checkout at `fa69a77a14f923a756064f6ae151d34cadb374f7`; the checkout was removed immediately after the test. |
| Godot editor load/import | PASS | Godot 4.7.1 loaded and quit with exit code 0. It emitted its pre-existing exit-time resource/ObjectDB diagnostics; these are not promoted to a title-entry failure or human-quality pass. |
| Runtime diagnostics | PASS | The live HERA log reported 0 errors and 0 warnings during the title smoke run. |

## Live technical smoke

Godot 4.7.1 ran `res://scenes/main/main.tscn` in the PR worktree at 960×540.

| Step | Assertion / observation | Result |
|---|---|---|
| Initial state | `/root/Main/UI/TitleScreen.visible == true` | PASS |
| Initial state | `/root/Main/UI/RunCommandScreen.visible == false` | PASS |
| Initial state | `/root/Main/UI/TitleScreen/Panel/StartExpeditionButton.disabled == false` after successful bootstrap | PASS |
| Initial render | 960×540 capture was nonblank and the automated render inspector reported `possible_clipping: false`. | PASS |
| Interaction | A live click on `StartExpeditionButton` was delivered at (480, 348). | PASS |
| Transition | `TitleScreen.visible == false` after the click. | PASS |
| Transition | `RunCommandScreen.visible == true` after the click. | PASS |
| Post-start capture | Existing Run Command surface was visible. The generic render heuristic reported `possible_clipping: true`, while the captured title is no longer present and image inspection found no task-specific title control clipping. This diagnostic remains recorded and is not a human-UX pass. | RECORDED_NONBLOCKING |

## Captures

| State | File | SHA-256 |
|---|---|---|
| Bootstrap ready | `docs/qa/captures/title_entry/omenward_title_entry_ready_960x540.png` | `c49b0963d65c4686286abdd88cabf1545abb57c8366223fe006fffdbc62dddb2` |
| After `원정 시작` | `docs/qa/captures/title_entry/omenward_title_entry_post_start_960x540.png` | `8d02f27aa5f18fb5b213324543459b9f119af2882674d21d1c5cbb02dedc5dfa` |

## Evidence ceiling and next gate

This is a technical execution check, not a human player evaluation. It does not
prove copy comprehension, accessibility, art fit, release-rights clearance, or
release readiness. The immediate remaining decision is the visible title-candidate
pair: `LOCK`, `REVISE`, or `REJECT`.
