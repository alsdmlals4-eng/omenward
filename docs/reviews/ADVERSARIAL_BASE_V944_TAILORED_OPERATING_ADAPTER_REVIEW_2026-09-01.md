# Adversarial Review — Base v9.4.4 Tailored Operating Adapter

```yaml
review_id: OMW-REV-20260901-BASE-V944-TAILORED-OPERATING-ADAPTER-01
review_date: 2026-09-01
scope: OPERATING_ROUTER__ADAPTER__GENERATED_VIEWS__CI_VALIDATION
product_mutation: NONE
base_semantic_release:
  version: 9.4.4
  release_commit: 210ec78292fa12ed7563ba743b322dd36103ae4a
  evidence_commit: bb61e68dc3028421b60c11b87ba2abd297ee6f78
  finalization_commit: 5adc196c0185951f50e49ab5e51586eff8d60886
base_validator_reference:
  commit: 19355b7ef065a21d0f2b685c7d9be64a4a3970f8
  role: CURRENT_PROGRAM_ONLY__GIT_CANONICAL_EOL_HANDLING
  unreleased_policy_adoption: NONE
machine_review: PASS_5_OF_5
runtime_review: NOT_RUN__NOT_IN_SCOPE
human_player_review: NOT_RUN__NOT_IN_SCOPE
release_and_rights_review: NOT_RUN__NOT_IN_SCOPE
```

## Review boundary

This change updates how OMENWARD reads and validates Base. It does not change Godot scenes, scripts, resources, game data, save data, approved asset binaries, product rules, or the user-approved protected implementation delta already recorded from `9a67a267a69c80fba6f25d5a37e360a15dcc2419`.

The adapter therefore keeps that approved protected baseline. The CI route validates the exact approved manifest instead of reclassifying historical protected changes as new work. A baseline migration requires a separate approval and is not inferred here.

## Findings corrected before final review

1. **Schema could not express the real repository-only boundary.** The former adapter schema treated the legacy GDD Sheet as a current workspace. Schema v2 adds the explicit `project_id` required by Base's released adapter model and records the Sheet as a no-read/no-write migration compatibility source.
2. **Released validator emitted Windows EOL false mismatches.** The v9.4.4 semantic release remains the complete content authority, while the current Base validator program is used solely to obtain Git-canonical byte handling for generated views. This does not adopt the unreleased v9.5 policy candidate.
3. **Generated views still carried the pre-index Windows hash.** Git stores the `.gitattributes`-locked adapter as LF (`996f19cf…`), while the first local generation recorded the unnormalized working-file hash. Generated source hashes, dashboard provenance, and regression expectations now use the Git-stored LF bytes; the generated-artifact EOL test prevents OS-dependent recurrence.
4. **The user-approved protected baseline looked stale but is semantically required.** Replacing it with `main` or a PR base would invalidate the exact approval receipt. It remains frozen and all protected-change workflows now read the exact approval manifest.
5. **The old root router duplicated volatile product details.** `AGENTS.md` is a thin start router again, with only durable operational constraints and links to live Decision/Context owners. Stable quality constraints required by current consumers remain as routing markers.
6. **Legacy adapter tests asserted v9.4.3.** They now preserve their planning-first and first-prompt coverage while asserting the v9.4.4 release and repository-only behavior.

## Five adversarial passes

### 1. Authority and release-pin drift — PASS

- Re-read fresh Base `origin/main` at `19355b7ef065a21d0f2b685c7d9be64a4a3970f8` and the released v9.4.4 finalization worktree at `5adc196c0185951f50e49ab5e51586eff8d60886`.
- Confirmed the adapter's release/evidence/finalization triple and Base skill-registry SHA against the exact released content.
- Confirmed `UNRELEASED_v9_5_POLICY_ADOPTION = NONE` in the router and adapter.

### 2. Generated-view integrity — PASS

- Regenerated the declared compatibility views from the canonical adapter using the current validator program against the exact v9.4.4 released content.
- Rechecked the canonical adapter byte hash and generated-view checks.
- Ran the focused Base adapter group: **26 tests passed**.
- Ran Base approved operating-contract validation against the exact v9.4.4 content and the existing user-approved protected manifest: **passed**.

### 3. Legacy Sheet and Notion reactivation — PASS

- The canonical adapter records the GDD Sheet as `GOOGLE_SHEETS_LEGACY_MIGRATION_SOURCE`, `HISTORICAL_RECONCILIATION_ONLY`, and `NO_CURRENT_READ_OR_WRITE`.
- Repository-only current authority remains explicit in the router and Active Context.
- No Notion or Google Sheet content was read, written, deleted, synchronized, or restored in this change.

### 4. Stale multi-front / obsolete route leakage — PASS

- Current routes resolve the single active march front from the current Decision and Active Context owners.
- The legacy three-front material remains discoverable only as historical evidence; it was neither deleted nor reactivated.
- Current router reconciliation, content-closure, platform, and recovery routes passed: **55 tests passed**.

### 5. Protected product and evidence-scope leakage — PASS

- The diff is limited to operating contracts, generated adapter views, documentation routes, CI validation, and regression tests; no Godot product path is changed.
- The approved protected-change manifest continues to validate the inherited product delta rather than allowing a broad bypass.
- No machine result was promoted to runtime, human/player, accessibility, release, or asset-rights acceptance. Those gates remain `NOT_RUN` or outside this documentation-only scope.

## Validation receipt

```text
Focused Base adapter regression                         PASS (26 tests)
Current router/platform/recovery regression             PASS (55 tests)
Full root unittest suite                                PASS (24 tests)
Full Python unittest suite                              PASS (570 tests)
Project core documentation validation                   PASS
Project skill-system validation                         PASS (12 active / 28 registered)
Exact approved operating-contract validation            PASS
Workflow YAML syntax / formatting validation            PASS
Frozen v4.5 canon-freshness comparator                  NOT_APPLICABLE
```

The frozen v4.5 comparator is deliberately not used as a pass/fail verdict for this current contract-only update: it compares `origin/main` against an older fixed product scope and flags the already-approved product implementation inherited by this branch. Its allowlist and historical baseline were not altered to manufacture a pass. Current route and protected-contract validations above are the applicable evidence.

## Remaining gates and rollback

- **Human usability and multi-unit combat readability:** `NOT_RUN`; this operating work does not observe a player session.
- **Runtime/device/accessibility:** `NOT_RUN` for this change; existing evidence is not reclassified.
- **Release, rights, and store submission:** `NOT_RUN`; no asset or platform claim changes.
- **Base promotion:** no Base write was made. The Git-canonical EOL improvement is already present in the current validator reference; the project-specific split is not an automatic Base policy promotion.
- **Rollback:** revert the single scoped commit. The previous adapter/CI/router behavior is preserved in Git history; no runtime data migration is required.
