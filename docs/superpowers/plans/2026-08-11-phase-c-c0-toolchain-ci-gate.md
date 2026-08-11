# Phase C C0 Toolchain CI Gate Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Re-establish a fail-closed Phase C C0 validation path after the direct main Godot AI 3.1.4 update by making every `addons/**` change trigger the full Omenward Core PR/main validation and recording the current toolchain/race state without changing gameplay product code.

**Architecture:** Extend the existing `Validate Omenward Core` path filter instead of creating a new workflow. Enforce that trigger through the existing CI usage validator and mutation tests, then add a distinct v4.5 fail-closed C0 scope that contains only the workflow, its tests/validators, this plan, and the C0 review owner. The PR itself becomes the current-main validation vehicle because it is based directly on `14b0d942e071dc6e823f48c29ac79f0978477d85`.

**Tech Stack:** GitHub Actions YAML, Python `unittest`, Godot 4.7.1 headless CI, GUT 9.7.1 vendored plugin, Godot AI 3.1.4 vendored plugin, v4.5 Thin Adapter scope validator.

## Global Constraints

- Decision: `OMW-DEC-20260811-OPS-PHASE-C-C0-PREFLIGHT-V1`.
- Base observed at C0 entry: `8e7d85b1b1272002a8086c502a41073888cb3318`.
- OMENWARD main observed at C0 entry: `14b0d942e071dc6e823f48c29ac79f0978477d85`.
- Parent validated Phase B main: `91f4aa98c0dea5307c2482aa0f403ce7dd115e40`.
- `14b0d942...` is a direct main commit with no push workflow runs/status checks; preserve this as audit evidence rather than rewriting history.
- Current repo source truth: Godot AI `3.1.4`, GUT `9.7.1`, Godot project feature line `4.7`; live local Godot-AI session/WS9500 state remains unverified in this environment.
- PR175 remains Draft and diverged from current main; do not treat historical PR175 Green as current evidence.
- No gameplay `scripts/`, `scenes/`, `data/`, `resources/`, or `project.godot` mutation in this C0 gate change.
- Do not select final FV, parameter vector, or product numerics.

---

### Task 1: Add a failing regression for addon-trigger coverage

**Files:**
- Modify: `tests/python/test_ci_usage_contract.py`

**Interfaces:**
- Consumes: `.github/workflows/validate-omenward-core.yml` trigger text.
- Produces: a regression that requires `- "addons/**"` in both pull-request and main-push path filters.

- [ ] **Step 1: Write the failing test**

Add `test_core_workflow_triggers_for_active_addons_on_pr_and_push`, asserting `text.count('- "addons/**"') == 2`.

Add a mutation test `test_core_addons_trigger_regression_is_rejected` that removes one `addons/**` trigger from a temporary workflow copy and expects the validator error `core workflow must trigger for addons/** on PR and push`.

- [ ] **Step 2: Verify RED**

Open a Draft PR with only the plan plus test change. Expected: Omenward Core/CI usage test fails because the current workflow has zero `addons/**` path entries.

### Task 2: Enforce addon-trigger coverage in the validator and workflow

**Files:**
- Modify: `.github/workflows/validate-omenward-core.yml`
- Modify: `tools/validate_ci_usage_contract.py`

**Interfaces:**
- Consumes: regression contract from Task 1.
- Produces: both PR and main push validation whenever any `addons/**` file changes.

- [ ] **Step 1: Implement minimal validator rule**

In `validate()`, require exactly two occurrences of `- "addons/**"` with the error `core workflow must trigger for addons/** on PR and push`.

- [ ] **Step 2: Implement minimal workflow change**

Add `- "addons/**"` once under `pull_request.paths` and once under `push.paths` in `validate-omenward-core.yml`.

- [ ] **Step 3: Verify focused GREEN**

Require `tests.python.test_ci_usage_contract` and `python tools/validate_ci_usage_contract.py` to pass on the PR exact head.

- [ ] **Step 4: Verify full current-main baseline**

Require the PR Omenward Core job to run the full Python repository suite and Godot 4.7.1 import/headless/runtime smoke against this branch based on `14b0d942...`.

### Task 3: Fail-close the Phase C C0 scope and record findings

**Files:**
- Create: `docs/reviews/PHASE_C_C0_PREFLIGHT_2026-08-11.md`
- Modify: `tests/python/test_canon_freshness_v45_scope.py`
- Modify: `tools/validate_canon_freshness_v45_scope.py`

**Interfaces:**
- Consumes: Decision `OMW-DEC-20260811-OPS-PHASE-C-C0-PREFLIGHT-V1` and verified C0 evidence.
- Produces: a distinct exact C0 non-product surface and durable review owner.

- [ ] **Step 1: Add scope RED**

Define the exact C0 surface as these seven files:
`docs/superpowers/plans/2026-08-11-phase-c-c0-toolchain-ci-gate.md`,
`docs/reviews/PHASE_C_C0_PREFLIGHT_2026-08-11.md`,
`.github/workflows/validate-omenward-core.yml`,
`tests/python/test_ci_usage_contract.py`,
`tools/validate_ci_usage_contract.py`,
`tests/python/test_canon_freshness_v45_scope.py`,
`tools/validate_canon_freshness_v45_scope.py`.

Test exact-surface PASS and missing-anchor rejection with message `missing required v4.5 Phase C C0 toolchain gate anchors`.

- [ ] **Step 2: Add minimal scope implementation**

Register `PHASE_C_C0_TOOLCHAIN_GATE_ALLOWED_FILES` and matching required anchors; preserve all historical modes and protected-path rejection.

- [ ] **Step 3: Write C0 review owner**

Record:
- Base `8e7d85b1...`, OMENWARD `14b0d942...`, Sheet drift from older SHAs;
- direct main Godot AI update has no workflow/status evidence;
- repo source versions Godot AI 3.1.4, GUT 9.7.1, Godot 4.7;
- upstream public 3.1.4 release not verified, so vendored source is project-local source truth only;
- PR175 diverged: merge-base `87339f87...`, PR175 ahead 43 / behind 14;
- local live PID/WS9500/session registry is unverified in this ChatGPT environment;
- C0 cannot authorize PR175 merge; after this CI gate is Green, next step is current-main PR175 rebase/revalidation plus local same-snapshot HiGodot diagnostic.

### Task 4: Adversarial review, Sheet sync, and merge gate

**Files:**
- No additional GitHub files unless a discovered compatibility regression requires an explicitly bounded amendment.
- Google Sheet: current hub, work order, current decision, audit, history under the same C0 Decision ID.

**Interfaces:**
- Consumes: exact-head GitHub CI and review state.
- Produces: authoritative C0 status and next executor boundary.

- [ ] **Step 1: Adversarial review**

Verify exact seven-file surface, product-path mutation = 0, unresolved review threads = 0, current main has not moved, and Base changes do not conflict with OMENWARD.

- [ ] **Step 2: Sync Sheet**

Write Base `8e7d85b1...`, OMENWARD `14b0d942...`, Godot AI 3.1.4 repo source truth, GUT 9.7.1, C0 CI status, PR175 divergence, and live-session unverified state using Decision `OMW-DEC-20260811-OPS-PHASE-C-C0-PREFLIGHT-V1`.

- [ ] **Step 3: Bounded reread**

Require Sheet readback to match GitHub/current C0 evidence.

- [ ] **Step 4: Merge only if exact-head gates are Green**

Use expected-head protection. After merge, require main-push Omenward Core full matrix plus Godot success because the workflow itself changed.

- [ ] **Step 5: Final C0 classification**

If CI is Green but no live HiGodot session evidence exists, classify `C0_PARTIAL_PASS_REPOSITORY_TOOLCHAIN_VERIFIED_LOCAL_LIVE_SESSION_UNVERIFIED`. Do not claim PR175 runtime execution has resumed until the same-snapshot local process/WS9500/session diagnostic is actually available.