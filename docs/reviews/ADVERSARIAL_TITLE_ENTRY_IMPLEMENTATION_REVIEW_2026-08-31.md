# Adversarial Review · Omen Warden Title Entry — 2026-08-31

```yaml
review_id: OMW-REV-20260831-TITLE-ENTRY-01
decision_id: OMW-PLAN-20260831-OMEN-WARDEN-TITLE-ENTRY-01
mode: BUILD_REVIEW__POST_CHANGE_MONITOR_LOOP
input_branch: codex/full-godot-implementation-20260830
input_head_before_title_entry: 398ba784a220a6ea2b2c992057c9cd62b9f129bb
full_scope_loop_minimum: 5
full_scope_loops_completed: 5
machine_evidence: PASS
live_technical_smoke: PASS
human_usability_evidence: NOT_RUN
candidate_asset_lock: USER_DECISION_REQUIRED
completion_state: ACCEPT_WITH_FOLLOWUP__TITLE_CANDIDATE_LOCK_PENDING
```

## Scope and protected intent

The reviewed change replaces automatic tutorial launch with one truthful title
action, `원정 시작`. It must preserve the approved `내정 → 룰렛 → 전선` single-front
run and cannot introduce saves, settings, shops, parallel fronts, building-map
placement, or unapproved runtime art binding. The authority is
`docs/superpowers/specs/2026-08-31-omen-warden-title-entry-design.md`; the
existing protected-change manifest was extended only with the exact scene and
script paths needed for that approved continuation.

## Five full-scope review loops

| Loop | Attack and validation across scope | Valid finding and resolution | Regression / output state |
|---|---|---|---|
| 1 | Attacked boot readiness, failure handling, explicit stage selection, UI signal ordering, and the ability to begin a run after bootstrap. | `P2 / OMISSION`: a malformed `GameSession` composition emitted a failure signal but did not retain its message for the title. Added a red SceneTree case, then stored the exact composition error in `_bootstrap_errors`. | The new composition-failure test passed after the minimal change; `begin_tutorial()` remains fail-closed. |
| 2 | Re-attacked the normal player path, double-trigger risk, title/Run Command visibility, bootstrap state readback, and existing tutorial routing. | No new valid finding. The button is disabled before use, bootstrap state is read on TitleScreen readiness to cover signal order, and the UI changes only after the actual `stage_started` signal. | Full headless Godot suite: 31/31, and a live 960×540 click moved TitleScreen `true → false` and RunCommand `false → true`. |
| 3 | Re-attacked candidate governance, accidental runtime art consumption, generated-text risk, title vocabulary, consumer separation, and the visual identity boundary. | No new valid finding. Runtime scene/script search found zero `TITLE-BG-01` / `TITLE-SEAL-01` references; the preview is isolated and labeled as not yet a runtime asset. | Native labels own readable text. Candidate SHA-256, prompt provenance, future consumers, and `LOCK / REVISE / REJECT` gate are recorded. |
| 4 | Re-attacked protected-path authorization, current decision/context references, stale current markers, fake menus, and rollback scope. | `P2 / COMPLEMENT_GAP`: the existing PR manifest initially lacked the title scene/script, isolated preview, and changed `GameSession` path. The exact Base gate rejected that omission; the same approved manifest was extended with only those user-authorized paths and the decision ID. | `tools/validate_project_core_docs.py`, JSON parsing, and `git diff --check` passed. The full Base approved-change gate is rerun against the amended exact commit. |
| 5 | Re-attacked duplicate/open work, temporary-file hygiene, generated import churn, exact test evidence, human-evidence overclaim, release-rights drift, and long-term fit. | No duplicate active PR owns the title-entry implementation; PR #257 is the sole active product PR. No P0/P1 finding. `P3 / DEFER`: Godot editor import exits 0 but prints known add-on font parsing and engine exit-time resource diagnostics; no title-specific failure reproduces in 31 headless checks or the live smoke. | A temporary exact Base checkout was removed after Python validation, and 27 editor-touched import sidecars were hash-proved identical to index then restored. Human usability, art fit, accessibility, performance, release rights, and remote CI for the new commit remain unverified. |

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

- **Same-goal PR recheck:** PR #257 is open against `main`; its remote head is
  `398ba784a220a6ea2b2c992057c9cd62b9f129bb` before this local commit. Other open
  PRs #212, #209, and #205 are draft/documentation tracks and do not own this UI.
- **Untouched consumer check:** `main.tscn`, `GameSession`, the new title scene,
  focused headless contracts, full headless suite, active context, current decision
  index, approval manifest, candidate record, and technical-smoke record are all
  connected. Candidate preview remains unreferenced by runtime entrypoints.
- **Omission/conflict/duplicate classification:** the composition-message and
  manifest omissions were fixed; no remaining title-entry conflict or duplicate
  work was found.
- **Evidence ceiling:** the current result is machine plus live technical smoke,
  not human usability, accessibility, performance, legal/rights, release, or
  merged-main evidence.

## Decision and remaining gate

The implemented title route is accepted for the current PR continuation. A full
visual runtime promotion is intentionally not closed: the user must choose
`LOCK`, `REVISE`, or `REJECT` for `TITLE-BG-01` and `TITLE-SEAL-01`. On `LOCK`,
only those locked bytes may move to `assets/art/ui/title/`, acquire a canonical
asset record, bind to `TitleScreen`, and receive a new full exact-head validation
and technical capture.
