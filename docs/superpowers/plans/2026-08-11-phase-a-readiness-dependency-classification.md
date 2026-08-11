# Phase A Readiness Dependency Classification Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Separate true pre-build planning blockers from approved provisional inputs, post-runtime tuning outputs, and platform/release-deferred work, while repairing stale TokenSource pending propagation without choosing new product content.

**Architecture:** Treat current approved GitHub owners as source of truth and add one review-only classification artifact. Current-facing routers may summarize only source-supported dependency status; historical design documents remain untouched. A fail-closed v4.5 scope mode limits this work to planning/test/tool/workflow files and forbids product/Godot mutation.

**Tech Stack:** Markdown canon/review artifacts, Python `unittest` contract tests, GitHub Actions v4.5 routing gate, Google Sheets bounded current-surface sync.

## Global Constraints

- `PHASE_A_GPT_CHAT_PLANNING` remains current.
- `PHASE_C_BLOCKED` remains enforced.
- User has not declared `기획 완료`; do not infer it.
- No GDScript, Scene, Resource, `project.godot`, data migration, final balance value, T3 content identity, or persistent Godot authoring changes.
- Preserve historical evidence; only current-facing consumers may be corrected.
- Same operational activation Decision: `OMW-DEC-20260811-OPS-ACTIVATE-INTEGRATED-CONTRACT-V4-5-R2-V1`.
- Fresh Base at plan creation: `315c66eea9614c284b9c11c4d522141065dfa4b0`, open PRs `0`.
- Fresh OMENWARD main at plan creation: `a57e533c30c47cb3b31766bae27bcf0d7eed5bc6`.
- Runtime PR #175 remains Draft with seven Issue #176 implementation-completeness gaps; PR #177 remains reference-only.

## Execution evidence amendment

Adversarial CI-route review found that creating a new readiness unit test was insufficient because the existing v4.5 workflow did not compile or execute it. The approved planning-only surface therefore expanded by exactly one CI file, `.github/workflows/validate-canon-freshness-v4-5.yml`, while preserving full-SHA action pins and all existing validation steps.

Observed RED lineage:

```text
31446118758 = initial new readiness scope rejected while existing routing stayed Green
31446268878 = workflow-added surface rejected because classifier had not yet admitted the workflow
31446353990 = routing Green + scope Green + readiness content-only RED
```

Final exact readiness surface is 11 files:

```text
.github/workflows/validate-canon-freshness-v4-5.yml
AGENTS.md
docs/DECISIONS_PENDING.md
docs/OMENWARD_GDD_CURRENT_CANON.md
docs/ONBOARDING_PLANNING_CURRENT_AUTHORITY.md
docs/PROJECT_GOOGLE_SHEET_WORKBOOK.md
docs/reviews/PHASE_A_PLANNING_READINESS_DEPENDENCY_CLASSIFICATION_2026-08-11.md
docs/superpowers/plans/2026-08-11-phase-a-readiness-dependency-classification.md
tests/python/test_phase_a_readiness_dependency_classification.py
tests/python/test_canon_freshness_v45_scope.py
tools/validate_canon_freshness_v45_scope.py
```

---

### Task 1: Add fail-closed readiness classification contracts

**Files:**
- Modify: `.github/workflows/validate-canon-freshness-v4-5.yml`
- Create: `tests/python/test_phase_a_readiness_dependency_classification.py`
- Modify: `tests/python/test_canon_freshness_v45_scope.py`
- Modify: `tools/validate_canon_freshness_v45_scope.py`

**Interfaces:**
- Consumes: approved physical-token contract, runtime-package dependency chain, platform/release owners.
- Produces: `PHASE_A_READINESS_CLASSIFICATION` exact-file scope mode and regression checks for current-facing dependency markers.

- [x] **Step 1: Write the failing readiness test**

The test requires current-facing consumers to distinguish resolved physical TokenInstance grammar from final special selection distribution.

- [x] **Step 2: Write the failing scope-mode test**

The test requires exactly the 11-file surface above and rejects partial/extra-file variants.

- [x] **Step 3: Run server CI and verify RED**

Observed: existing routing remained Green while new scope/readiness requirements failed.

- [x] **Step 4: Implement only the new fail-closed scope mode**

`PHASE_A_READINESS_CLASSIFICATION_ALLOWED_FILES` uses identical required anchors. Existing activation/postmerge/Windows/evidence/current-consumer modes remain unchanged.

- [x] **Step 5: Wire CI to the new readiness contract**

The v4.5 workflow now path-triggers, compiles, and runs `tests/python/test_phase_a_readiness_dependency_classification.py` while preserving immutable action SHAs.

- [x] **Step 6: Re-run focused infrastructure contracts**

Observed at run `31446353990`: routing Green, scope Green, readiness content-only RED.

### Task 2: Classify existing dependencies without inventing product decisions

**Files:**
- Create: `docs/reviews/PHASE_A_PLANNING_READINESS_DEPENDENCY_CLASSIFICATION_2026-08-11.md`
- Modify: `AGENTS.md`
- Modify: `docs/DECISIONS_PENDING.md`
- Modify: `docs/OMENWARD_GDD_CURRENT_CANON.md`
- Modify: `docs/ONBOARDING_PLANNING_CURRENT_AUTHORITY.md`
- Modify: `docs/PROJECT_GOOGLE_SHEET_WORKBOOK.md`

**Interfaces:**
- Consumes: approved source hierarchy and later child Decisions.
- Produces: one explicit taxonomy used by Phase A and current-facing routers.

- [x] **Step 1: Record the source-derived taxonomy**

```text
IMPLEMENTATION_COMPLETENESS
PROVISIONAL_IMPLEMENTATION_INPUT_APPROVED
POST_RUNTIME_EVIDENCE_TUNING
FULL_PRODUCT_PLANNING_OPEN_NOT_CURRENT_BUILD_BLOCKER
LEVEL_OR_IMPLEMENTATION_DETAIL_DEFERRED
RELEASE_PHASE_DEFERRED
HISTORICAL_OR_SUPERSEDED
```

- [x] **Step 2: Resolve the ambiguous TokenSource pending phrase**

Current-facing normalized physical reel mechanics:

```text
TOKEN_INSTANCES_PER_REEL_PER_ACTIVE_SOURCE = 1
TOTAL_TOKEN_INSTANCES_PER_ACTIVE_SOURCE = 3
FRACTIONAL_TOKEN_WEIGHT = FORBIDDEN
SPECIAL_T1_SELECTION_DISTRIBUTION = POST_RUNTIME_EVIDENCE_TUNING
```

These markers summarize the later approved physical TokenInstance grammar; they do not select final special-unit probabilities.

- [x] **Step 3: Preserve runtime-before-final-FV dependency direction**

```text
ROLE_OUTPUT_RUNTIME -> DETERMINISTIC_MEASUREMENT -> FUNCTIONAL_VALUE_COMPARISON -> FINAL_TUNING
```

`FINAL_FUNCTIONAL_VALUE_INDEX`, weighted/vector selection, final cost/interval vector, and final product numerics remain unselected and must not be synthesized.

- [x] **Step 4: Separate platform/release work from PR175 DoR**

Save schema, PC/Android adapters, export presets, store SDKs, and release gates remain incomplete but are classified as later architecture/release work for PR175 dependency purposes.

- [x] **Step 5: Preserve genuinely open full-product content**

No new T3 identity/effect or display name is selected. Later-approved Archer T3 correction remains current; unclosed tower/T3/name detail remains full-product planning work outside PR175's role-output blocker set.

- [x] **Step 6: Correct stale workbook routing metadata**

Closed PR178 routing is removed; workbook current focus is `PR175_PHASE_A_READINESS_REVIEW` with merged Sheet readback status.

- [ ] **Step 7: Run readiness and routing tests**

Expected: readiness, scope, routing, exact surface, and whitespace Green at one exact head.

### Task 3: Validate, synchronize Sheet, and close the planning-only PR

**Files:**
- Google Sheet current-facing ranges only; append new audit/history rows rather than rewriting history.
- No additional repository product files.

**Interfaces:**
- Consumes: exact GitHub PR head and same activation Decision.
- Produces: bounded GitHub/Sheet evidence for the readiness classification.

- [x] **Step 1: Open Draft PR from the isolated branch**

PR #184 records Phase C block and the source-derived scope.

- [ ] **Step 2: Verify exact-head CI**

Require all triggered workflows Green, no unresolved review threads, exact scope pass, and no protected product paths.

- [ ] **Step 3: Sync Google Sheet with the same Decision ID**

Update current hub/decision text and current `43_건물_Tier_효과` TokenSource wording; append work-order/audit/history rows. Preserve historical rows and do not claim final special selection weights are selected.

- [ ] **Step 4: Bounded reread Sheet**

Verify every modified range and new audit/history IDs before merge.

- [ ] **Step 5: Adversarial review**

Reject any change that accidentally selects final balance numerics, resolves T3 content, claims save/platform completion, weakens a prior scope mode, or opens Phase C.

- [ ] **Step 6: Race check and expected-head squash merge**

Fresh-read Base main/open PRs, OMENWARD main/open PRs, exact head, review threads, and CI immediately before merge.

- [ ] **Step 7: Merged-main readback and push CI**

Require merged main to contain the review taxonomy and current physical-token contract; verify all main-push workflows triggered by the merge.

- [ ] **Step 8: Final Sheet merge-state update and reread**

Record merge SHA and push results, then continue Phase A inventory. Do not infer `기획 완료`.

## Self-review

- Spec coverage: dependency classification, stale current propagation, Sheet conflict, TDD, fail-closed scope, CI execution route, merge/readback all covered.
- Placeholder scan: no implementation placeholders are used as instructions; intentionally open product values are explicitly protected rather than assigned.
- Type/name consistency: taxonomy labels and exact physical-token markers are identical across tests and current-facing docs.
