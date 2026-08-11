# Phase A Readiness Dependency Classification Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Separate true pre-build planning blockers from approved provisional inputs, post-runtime tuning outputs, and platform/release-deferred work, while repairing stale TokenSource pending propagation without choosing new product content.

**Architecture:** Treat current approved GitHub owners as source of truth and add one review-only classification artifact. Current-facing routers may summarize only source-supported dependency status; historical design documents remain untouched. A fail-closed v4.5 scope mode limits this work to planning/test/tool files and forbids product/Godot mutation.

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

---

### Task 1: Add fail-closed readiness classification contracts

**Files:**
- Create: `tests/python/test_phase_a_readiness_dependency_classification.py`
- Modify: `tests/python/test_canon_freshness_v45_scope.py`
- Modify: `tools/validate_canon_freshness_v45_scope.py`

**Interfaces:**
- Consumes: approved physical-token contract, runtime-package dependency chain, platform/release owners.
- Produces: `PHASE_A_READINESS_CLASSIFICATION` exact-file scope mode and regression checks for current-facing dependency markers.

- [ ] **Step 1: Write the failing readiness test**

```python
def test_physical_token_count_is_not_republished_as_pending():
    for path in CURRENT_CONSUMERS:
        text = path.read_text(encoding="utf-8")
        assert "TOKEN_SOURCE_WEIGHT_AND_COUNT = PENDING_SIMULATION" not in text
        assert "TOKEN_INSTANCES_PER_REEL_PER_ACTIVE_SOURCE = 1" in text
        assert "FRACTIONAL_TOKEN_WEIGHT = FORBIDDEN" in text
```

Also require the review artifact to classify:

```text
ISSUE176_7_GAPS = IMPLEMENTATION_COMPLETENESS / NO_NEW_PRODUCT_DECISION
FINAL_FUNCTIONAL_VALUE = POST_RUNTIME_EVIDENCE_TUNING
SPECIAL_SELECTION_DISTRIBUTION = POST_RUNTIME_EVIDENCE_TUNING
PLATFORM_SAVE_EXPORT_STORE = RELEASE_PHASE_DEFERRED_FOR_PR175
T3_CONTENT_AND_FINAL_NAMES = FULL_PRODUCT_PLANNING_OPEN_NOT_PR175_BLOCKER
PHASE_C = BLOCKED
```

- [ ] **Step 2: Write the failing scope-mode test**

Require exactly this proposed surface to pass while partial or extra-file variants fail:

```text
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

- [ ] **Step 3: Run server CI and verify RED**

Expected: existing routing tests remain Green; new readiness/scope assertions fail because the review artifact and new scope mode do not exist and current consumers still republish ambiguous pending state.

- [ ] **Step 4: Implement only the new fail-closed scope mode**

Add `PHASE_A_READINESS_CLASSIFICATION_ALLOWED_FILES` and identical required anchors. Preserve all existing activation/postmerge/Windows/evidence/current-consumer modes unchanged.

- [ ] **Step 5: Re-run focused scope tests**

Expected: scope mode passes; readiness content test still fails until Task 2.

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

- [ ] **Step 1: Record the source-derived taxonomy**

Use exactly these categories:

```text
IMPLEMENTATION_COMPLETENESS
PROVISIONAL_IMPLEMENTATION_INPUT_APPROVED
POST_RUNTIME_EVIDENCE_TUNING
FULL_PRODUCT_PLANNING_OPEN_NOT_CURRENT_BUILD_BLOCKER
LEVEL_OR_IMPLEMENTATION_DETAIL_DEFERRED
RELEASE_PHASE_DEFERRED
HISTORICAL_OR_SUPERSEDED
```

- [ ] **Step 2: Resolve the ambiguous TokenSource pending phrase**

Current physical reel mechanics must say:

```text
TOKEN_INSTANCES_PER_REEL_PER_ACTIVE_SOURCE = 1
TOTAL_TOKEN_INSTANCES_PER_ACTIVE_SOURCE = 3
FRACTIONAL_TOKEN_WEIGHT = FORBIDDEN
```

Do **not** claim final special-unit selection probabilities are fixed. Classify those separately as `POST_RUNTIME_EVIDENCE_TUNING` because functional-value evidence is required before final distribution tuning.

- [ ] **Step 3: Preserve runtime-before-final-FV dependency direction**

Record:

```text
ROLE_OUTPUT_RUNTIME -> DETERMINISTIC_MEASUREMENT -> FUNCTIONAL_VALUE_COMPARISON -> FINAL_TUNING
```

Therefore `FINAL_FUNCTIONAL_VALUE_INDEX`, final weighted/vector selection, final cost/interval vector, and final product numerics are not pre-PR175 inputs. They remain unselected and must not be synthesized.

- [ ] **Step 4: Separate platform/release work from PR175 DoR**

Record save schema, PC/Android adapters, export presets, store SDKs, and release gates as later architecture/release phases. Do not mark them complete.

- [ ] **Step 5: Preserve genuinely open full-product content**

Do not resolve T3 content identities/effects or final display naming here. Mark them `FULL_PRODUCT_PLANNING_OPEN_NOT_CURRENT_BUILD_BLOCKER` where later owners have not closed them. Preserve later approved unit-lineage corrections where they exist.

- [ ] **Step 6: Correct stale workbook routing metadata**

Replace PR178-era `current_working_pr` with a fresh-state resolver/current Phase-A focus so the workbook does not hard-code a closed planning PR.

- [ ] **Step 7: Run readiness and routing tests**

Expected: new readiness test Green; all existing canon freshness routing tests Green.

### Task 3: Validate, synchronize Sheet, and close the planning-only PR

**Files:**
- Google Sheet current-facing ranges only; append new audit/history rows rather than rewriting history.
- No additional repository product files.

**Interfaces:**
- Consumes: exact GitHub PR head and same activation Decision.
- Produces: bounded GitHub/Sheet evidence for the readiness classification.

- [ ] **Step 1: Open Draft PR from the isolated branch**

Record RED run IDs, source-derived classifications, exact changed-file surface, and `PHASE_C_BLOCKED`.

- [ ] **Step 2: Verify exact-head CI**

Require all triggered workflows Green, no unresolved review threads, exact scope pass, and no protected product paths.

- [ ] **Step 3: Sync Google Sheet with the same Decision ID**

Update current hub/decision text and the current `43_건물_Tier_효과` TokenSource wording; append a new work-order row, audit row, and history row. Preserve historical rows and do not claim final special selection weights are selected.

- [ ] **Step 4: Bounded reread Sheet**

Verify every modified range and the new audit/history IDs before merge.

- [ ] **Step 5: Adversarial review**

Reject any change that accidentally selects final balance numerics, resolves T3 content, claims save/platform completion, weakens a prior scope mode, or opens Phase C.

- [ ] **Step 6: Race check and expected-head squash merge**

Fresh-read Base main/open PRs, OMENWARD main/open PRs, exact head, review threads, and CI immediately before merge.

- [ ] **Step 7: Merged-main readback and push CI**

Require merged main to contain the review taxonomy and current physical-token contract; verify all main-push workflows triggered by the merge.

- [ ] **Step 8: Final Sheet merge-state update and reread**

Record merge SHA and push results, then continue Phase A inventory. Do not infer `기획 완료`.

## Self-review

- Spec coverage: dependency classification, stale current propagation, Sheet conflict, external benchmark boundary, TDD, fail-closed scope, merge/readback all covered.
- Placeholder scan: no implementation placeholders are used as instructions; intentionally open product values are explicitly protected rather than assigned.
- Type/name consistency: taxonomy labels and exact physical-token markers are identical across tests and planned docs.
