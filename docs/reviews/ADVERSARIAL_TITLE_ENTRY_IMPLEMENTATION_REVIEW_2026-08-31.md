# Adversarial Review · Omen Warden Title Entry — 2026-08-31

```yaml
review_id: OMW-REV-20260831-TITLE-ENTRY-01
decision_id: OMW-PLAN-20260831-OMEN-WARDEN-TITLE-ENTRY-01
mode: BUILD_REVIEW__POST_CHANGE_MONITOR_LOOP
input_branch: codex/full-godot-implementation-20260830
native_title_route_history_head: 398ba784a220a6ea2b2c992057c9cd62b9f129bb
locked_asset_worktree_baseline: f94731ff543bafce7e30d82a9d88fa10fc122752
full_scope_loop_minimum: 5
full_scope_loops_completed: 5
machine_evidence: 32_GODOT_CONTRACTS_PASS__569_PYTHON_CONTRACTS_PASS
live_technical_smoke: LOCKED_ASSET_TECHNICAL_SMOKE_PASS
human_usability_evidence: NOT_RUN
candidate_asset_lock: USER_APPROVED__CANON_REGISTERED__PHYSICAL_CANDIDATES_DELETED
completion_state: ACCEPT_WITH_FOLLOWUP__HUMAN_RIGHTS_REMOTE_CI_PENDING
```

## Scope and protected intent

The reviewed change replaces automatic tutorial launch with one truthful title
action, `원정 시작`. It must preserve the approved `내정 → 룰렛 → 전선` single-front
run and cannot introduce saves, settings, shops, parallel fronts, building-map
placement, or unapproved runtime art binding. The authority is
`docs/superpowers/specs/2026-08-31-omen-warden-title-entry-design.md`; the
existing protected-change manifest was extended only with the exact scene and
script paths needed for that approved continuation.

## Historical native-title route review

| Loop | Attack and validation across scope | Valid finding and resolution | Regression / output state |
|---|---|---|---|
| 1 | Attacked boot readiness, failure handling, explicit stage selection, UI signal ordering, and the ability to begin a run after bootstrap. | `P2 / OMISSION`: a malformed `GameSession` composition emitted a failure signal but did not retain its message for the title. Added a red SceneTree case, then stored the exact composition error in `_bootstrap_errors`. | The new composition-failure test passed after the minimal change; `begin_tutorial()` remains fail-closed. |
| 2 | Re-attacked the normal player path, double-trigger risk, title/Run Command visibility, bootstrap state readback, and existing tutorial routing. | No new valid finding. The button is disabled before use, bootstrap state is read on TitleScreen readiness to cover signal order, and the UI changes only after the actual `stage_started` signal. | Full headless Godot suite: 31/31, and a live 960×540 click moved TitleScreen `true → false` and RunCommand `false → true`. |
| 3 | Re-attacked candidate governance, accidental runtime art consumption, generated-text risk, title vocabulary, consumer separation, and the visual identity boundary. | No new valid finding. Runtime scene/script search found zero `TITLE-BG-01` / `TITLE-SEAL-01` references; the preview is isolated and labeled as not yet a runtime asset. | Native labels own readable text. Candidate SHA-256, prompt provenance, future consumers, and `LOCK / REVISE / REJECT` gate are recorded. |
| 4 | Re-attacked protected-path authorization, current decision/context references, stale current markers, fake menus, and rollback scope. | `P2 / COMPLEMENT_GAP`: the existing PR manifest initially lacked the title scene/script, isolated preview, and changed `GameSession` path. The exact Base gate rejected that omission; the same approved manifest was extended with only those user-authorized paths and the decision ID. | `tools/validate_project_core_docs.py`, JSON parsing, and `git diff --check` passed. The full Base approved-change gate is rerun against the amended exact commit. |
| 5 | Re-attacked duplicate/open work, temporary-file hygiene, generated import churn, exact test evidence, human-evidence overclaim, release-rights drift, and long-term fit. | No duplicate active PR owns the title-entry implementation; PR #257 is the sole active product PR. No P0/P1 finding. `P3 / DEFER`: Godot editor import exits 0 but prints known add-on font parsing and engine exit-time resource diagnostics; no title-specific failure reproduces in 31 headless checks or the live smoke. | A temporary exact Base checkout was removed after Python validation, and 27 editor-touched import sidecars were hash-proved identical to index then restored. Human usability, art fit, accessibility, performance, release rights, and remote CI for the new commit remain unverified. |

## Locked-asset promotion · five full-scope review loops

| Loop | Attack and validation across scope | Finding / resolution | Regression / output state |
|---|---|---|---|
| 1 | Attacked exact approval selection, byte identity, source-to-runtime promotion, alpha separation, and a hidden duplicate title label. | No P0/P1 finding. The latest user-supplied background hash and canonical background hash match exactly; the wordmark remains a separate RGBA texture. The former native `Panel/Title` node was deliberately removed so the title appears once. | New locked-asset SceneTree contract loaded both textures, asserted their exact paths, and rejected the removed candidate directory and duplicate label. |
| 2 | Attacked boot order, title visibility, disabled state, semantic button targeting, title-to-command transition, and existing tutorial routing. | No new valid finding. On a fresh run `TitleScreen=true`, `RunCommandScreen=false`, and the sole `원정 시작` action was enabled; the live text-target click changed them to `false` and `true` respectively. | 32 / 32 headless Godot contracts passed with 0 failures; title-route coverage remained in the complete suite. |
| 3 | Attacked candidate cleanup, stale scene/test/capture consumers, historical-reference loss, duplicated current authority, and file-size hygiene. | No active candidate PNG, preview scene, preview contract, or old title capture survived. Candidate identity, prompt provenance, hashes, and disposal decisions are retained in one history-only archive rather than duplicated image files. | Active scene/script/test search finds canonical title paths only; the candidate archive is explicitly classified as non-runtime history. |
| 4 | Attacked document/current-state drift, protected-path approval scope, canonical locator propagation, and release-rights overclaim. | No blocking drift found after updating the decision index, active context, documentation map, lifecycle registry, asset record, QA record, and approval manifest. The asset record continues to mark AI terms/input rights/distribution as `RELEASE_BLOCKED_UNVERIFIED`. | Project core docs, archive governance, skill system, and Base adapter contract checks all passed; no legal or release claim was promoted. |
| 5 | Attacked exact-machine evidence, runtime render bounds, post-start screenshot provenance, editor import noise, temporary checkout cleanup, remote/main divergence, and accidental import churn. | `P3 / FOLLOW_UP`: PR #257 remains `DIRTY` against current `origin/main`, so this change must not be represented as merged or main-verified. Godot import had non-title add-on/engine diagnostics; live diagnostics were clean with 0 errors and 0 warnings. Temporary Base checkout was removed. The generic Base claim-and-intent checker is `UNVERIFIED_DEPENDENCY`: this thin-adapter project intentionally has no local `skills/reviewing-and-validating-project-changes/` schema bundle for that checker to load. | 569 / 569 Python contracts passed against the exact temporary Base revision. Ready render inspector reported `possible_clipping=false`; post-start generic command-screen heuristic remains recorded rather than treated as UX pass. The declared record at `docs/reviews/OMENWARD_TITLE_ENTRY_REVIEW_EVIDENCE_2026-08-31.json` is retained, but its generic checker is not counted as a PASS. |

## Multi-lens outcome

| Lens | Verdict | Evidence boundary |
|---|---|---|
| Simplify | APPLIED | Two approved runtime textures plus native UI replaced ten candidate PNGs, a preview scene, a preview test, and superseded captures without removing title-route behavior. |
| Style Guide | APPLIED | The separate wordmark, storybook watercolor battle scene, and restrained lower action panel match the registered Ward-versus-Veil visual language. Human aesthetic confirmation beyond the exact asset selection is still not measured. |
| Domain Review | APPLIED | The title continues to enter the approved single-front `tutorial_stage` flow and adds no buildings, map placement, tower rule, roulette rule, or combat behavior. |
| Security / Safety / Trust Boundary | APPLIED_WITH_FOLLOW_UP | Candidate provenance is retained, release rights are fail-closed, temporary test materials were removed, and the PR/main conflict is not bypassed. Remote CI, legal/rights review, and human use evidence remain open. |

## Better alternatives and long-term fit

| Alternative | Decision | Reason |
|---|---|---|
| Auto-launch the tutorial as before | REJECT | It gives no first-frame orientation and bypasses the player's only real entry decision. |
| Add Continue, Settings, Store, or Save selectors | REJECT | Those systems have no actual backing state; their labels would make a false product promise. |
| Bind generated title art immediately | REJECT | It would skip the required user visual lock and improperly promote candidate bytes to runtime assets. |
| Native functional entry plus candidate-only art review | ADOPT | It makes the game playable now, preserves truthful UI, and keeps visual/publishing decisions reversible. |

The adopted route is compatible with the single-front product core: it starts the
existing tutorial and does not alter roulette agency, building slots, combat data,
or the battle-primary/minimap surface.

## Post-change monitor result

- **Same-goal PR recheck:** PR #257 remains open; its pre-change remote head was
  `f94731ff543bafce7e30d82a9d88fa10fc122752`. Current `origin/main` was fetched
  and the PR is `DIRTY`, so no rebase, force-push, or direct-main change was used.
- **Untouched consumer check:** `main.tscn` and `GameSession` retain their title
  route relationship; `TitleScreen`, the locked-asset contract, title-route
  contract, current decision/context, documentation map, lifecycle registry,
  approval manifest, asset record, candidate archive, and technical-smoke record
  are connected. Historical plans remain history-only.
- **Omission/conflict/duplicate classification:** stale candidate runtime consumers
  were removed; no duplicate active visual authority was found. The PR/main
  conflict is a separate integration follow-up, not a reason to rewrite the
  current title decision.
- **Evidence ceiling:** this result is machine plus live technical smoke and user
  exact-asset selection, not human usability, accessibility, performance,
  legal/rights, remote CI, merged-main, or release evidence. The repository does
  not define `.github/reference-freshness.json`; therefore the Base automatic
  freshness checker is also not runnable here. A manual impact map and active
  consumer scan were completed instead: the title scene, locked-asset contract,
  decision/context, documentation map, lifecycle registry, approval manifest,
  asset record, QA record, and review are current consumers; historical plan and
  candidate-archive references are retained only as history.

## Decision and remaining gate

The locked title implementation is accepted for the current PR continuation:
the user-approved wordmark and last-attached battle-surge image are canonically
bound, machine-verified, and technically rendered. It is not merged to main or
release-ready. The next gates are remote PR validation after push, a dedicated
PR/main reconciliation without discarding current work, human readability and
accessibility observation, performance profiling on target hardware, and asset
rights review. The generic Base claim-and-intent and reference-freshness helpers
also need a project-local adapter/config route before they can contribute fresh
machine evidence; their unavailable state is not represented as a PASS.
