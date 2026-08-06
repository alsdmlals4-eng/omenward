# Actions-Budget Local Exact-HEAD Fallback Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Define and prove a cost-free exact-HEAD verification fallback for non-runtime OMENWARD changes while GitHub Actions cannot start because of account billing or spending-limit restrictions.

**Architecture:** A machine-readable policy classifies which PR surfaces may use connector-backed remote readback plus sandbox reconstruction, and which surfaces remain blocked until real Godot/GUT/platform execution exists. A Python validator and focused tests enforce that the fallback never claims GitHub Actions Green, never bypasses repository policy, and never substitutes for Godot, GUT, Windows, Android, asset, or product-runtime evidence.

**Tech Stack:** GitHub REST readback, Git blob SHA-1, Python 3 standard library, JSON policy/evidence manifests, unittest.

## Global Constraints

- Decision: `OMW-DEC-20260807-PROCESS-ACTIONS-BUDGET-LOCAL-EXACT-HEAD-FALLBACK-V1`.
- Active contract: `PROJECT_TOTAL_PLANNING_IMPLEMENTATION_AND_DELIVERY_INSTRUCTION v4.3`.
- Trigger: `BILLING_OR_SPENDING_LIMIT_PRE_START` with zero workflow steps and runner ID 0.
- The fallback is permitted only for process, documentation, Python validator, and data-contract changes.
- Product implementation, Godot authoring, formal GUT runtime, Windows/Android runtime, export, and asset import remain blocked.
- The fallback may support a normal merge only when GitHub accepts the merge without policy bypass and all scope-specific evidence is present.
- No `project.godot`, `.tscn`, `.tres`, `.res`, production `.gd`, data, image, audio, or `addons/gut/**` mutation is allowed in this PR.

---

### Task 1: Policy Contract

**Files:**
- Test: `tests/python/test_local_exact_head_fallback.py`
- Create: `docs/operations/LOCAL_EXACT_HEAD_FALLBACK_POLICY.v1.json`
- Create: `tools/validate_local_exact_head_fallback.py`

**Interfaces:**
- Consumes: policy JSON at `docs/operations/LOCAL_EXACT_HEAD_FALLBACK_POLICY.v1.json`.
- Produces: `validate_policy(data: dict) -> list[str]` and CLI exit status.

- [ ] **Step 1: Write the failing test**

Require the policy to identify the user-approved Decision, preserve Actions as not Green, restrict eligible PR classes, forbid runtime substitution, require exact remote blob readback, and prohibit repository-policy bypass.

- [ ] **Step 2: Run test to verify it fails**

Run: `python -m unittest tests.python.test_local_exact_head_fallback`
Expected: import or file-not-found failure because validator and policy do not exist.

- [ ] **Step 3: Write minimal implementation**

Create the policy JSON and validator with only the invariants exercised by the tests.

- [ ] **Step 4: Run test to verify it passes**

Run: `python -m unittest tests.python.test_local_exact_head_fallback`
Expected: all focused tests pass.

- [ ] **Step 5: Commit**

Commit the test, policy, and validator after Green.

### Task 2: PR #157 Exact-HEAD Evidence

**Files:**
- Create: `docs/evidence/PR157_LOCAL_EXACT_HEAD_VERIFICATION_2026-08-07.json`
- Create: `docs/process/ACTIONS_BUDGET_LOCAL_EXACT_HEAD_FALLBACK_2026-08-07.md`
- Create: `docs/reviews/ADVERSARIAL_ACTIONS_BUDGET_FALLBACK_REVIEW_2026-08-07.md`

**Interfaces:**
- Consumes: PR #157 exact head `c27715cfb7f161854fd994711a6859ee23a68fac`, seven-file remote inventory, exact Git blob SHAs, and reconstructed command results.
- Produces: auditable evidence that distinguishes `LOCAL_EXACT_HEAD_PASS` from `GITHUB_ACTIONS_GREEN` and from runtime validation.

- [ ] **Step 1: Record exact remote inventory**

Record all seven changed paths and their Git blob SHAs from GitHub readback.

- [ ] **Step 2: Record reconstructed execution**

Record exact executable blob matches and fresh results for `py_compile`, eight focused unittests, and the contract validator.

- [ ] **Step 3: Record limitations**

Keep Godot, GUT CLI/JUnit, Windows, Android, local checkout, and runtime statuses as `NOT_RUN` or `BLOCKED_UNVERIFIED`.

- [ ] **Step 4: Run policy and evidence validation**

Run the validator against the policy and evidence bundle; confirm exit 0 without claiming Actions Green.

- [ ] **Step 5: Commit**

Commit documentation, adversarial review, and evidence after validation.

### Task 3: Exact-HEAD Review and Sheet Sync

**Files:**
- Google Sheet: `02_현재_확정결정`, `04_누락_충돌_감사`, `99_변경이력`.
- PR body and conversation comment.

**Interfaces:**
- Consumes: final PR head, changed-file allowlist, fresh local test results, and remote blob readback.
- Produces: same Decision ID and final exact head in GitHub and Google Sheet.

- [ ] **Step 1: Verify final changed-file scope**

Compare the branch with main and reject unexpected product, Godot, GUT addon, data, image, or audio paths.

- [ ] **Step 2: Reconstruct final executable files**

Fetch the final remote test, validator, policy, and evidence blobs; reconstruct and run the complete focused suite.

- [ ] **Step 3: Update Draft PR**

Open a Draft PR describing the fallback boundary, exact commands, results, and residual blockers.

- [ ] **Step 4: Synchronize Google Sheet**

Write and read back the same Decision ID and exact head in the three contracted ranges.

- [ ] **Step 5: Apply merge policy**

A normal merge may be attempted only if exact-head fallback evidence is complete, review findings contain no P0/P1, GitHub accepts the merge without bypass, and the PR contains only fallback-eligible surfaces.
