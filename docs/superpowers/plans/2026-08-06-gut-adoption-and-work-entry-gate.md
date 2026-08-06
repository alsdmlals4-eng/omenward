# GUT Adoption and Work Entry Gate Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Formally adopt GUT 9.7.1 as OMENWARD's test authority while preserving HiGodot as the sole Godot authoring authority and enforcing a fail-closed current-state work-entry gate.

**Architecture:** A versioned adoption record owns provenance, compatibility, authority boundaries, consumption, CI, and rollback. A separate work-entry state records fresh GitHub/Sheet readback and blocks normal changes while allowing only exact bootstrap and explicitly authorized remediation paths.

**Tech Stack:** Python 3.12, unittest, JSON, Markdown, GitHub Actions, Godot 4.7, GUT 9.7.1.

## Global Constraints

- HiGodot is the sole Scene/Node/Resource/project-setting mutation authority.
- GUT owns test discovery, execution, assertions, doubles, and reports only.
- Do not modify `project.godot`, Scene, Resource, gameplay code, or data in this Draft adoption PR.
- GUT activation requires exact vendor reconciliation, Godot import, CLI smoke, and project regression.
- The work-entry gate is fail-closed; bootstrap is PR #155 only and remediation requires a separate exact-path authorization.

---

### Task 1: Authority and entry-gate RED tests

**Files:**
- Create: `tests/python/test_godot_authoring_test_authority.py`

- [x] Write failing tests for role overlap, premature activation, image READY/AWAITING promotion, and non-remediation entry.
- [x] Run `python -m unittest tests.python.test_godot_authoring_test_authority -v` and confirm failure because the validator is missing.
- [x] Commit the RED test.

### Task 2: Minimal validator and versioned records

**Files:**
- Create: `tools/validate_godot_authoring_test_authority.py`
- Create: `docs/operations/GUT_ADOPTION_RECORD.v1.json`
- Create: `docs/operations/WORK_ENTRY_GATE_STATE.v1.json`

- [x] Implement exact schema and fail-closed entry evaluation.
- [x] Record upstream and project vendor tree SHAs without claiming equality.
- [x] Run the focused unittest and confirm seven tests pass in reconstructed scope.
- [x] Run `python tools/validate_godot_authoring_test_authority.py --contract` and confirm contract PASS with blocked entry status.

### Task 3: Adoption specification, gate routing, and adversarial review

**Files:**
- Create: `docs/design/PROPOSED_OMENWARD_HIGODOT_GUT_AUTHORITY_AND_GUT_9_7_1_ADOPTION_2026-08-06.md`
- Create: `docs/operations/OMENWARD_WORK_ENTRY_GATE_2026-08-06.md`
- Create: `docs/reviews/ADVERSARIAL_GUT_ADOPTION_AND_WORK_ENTRY_GATE_REVIEW_2026-08-06.md`
- Modify: `AGENTS.md`

- [x] Route all work through the validator command.
- [x] Preserve current blockers and forbid READY/AWAITING promotion.
- [x] Re-run tests and contract validation in reconstructed scope.

### Task 4: CI bootstrap gate and Draft PR

**Files:**
- Create: `.github/workflows/validate-godot-authoring-test-authority.yml`

- [x] Compile validator/tests in reconstructed scope.
- [x] Run focused tests and contract validation in reconstructed scope.
- [x] Pass exact changed files to `--entry`; allow only PR #155 bootstrap paths while blocked.
- [x] Open Draft PR #155 from exact main `7588317f294d602cfad5f7f15bfebcf849b8a77b`.
- [x] Re-read PR exact HEAD and Sheet Decision row.
- [ ] Obtain exact-head Actions Green; currently billing/spending pre-start with zero steps.

### Task 5: Close self-modifying gate bypasses

- [x] Add RED tests for PR/branch/base-scoped bootstrap, authoring/GUT overlap, exact HiGodot manifest, counted-vs-NON_COUNTER Sheet readback, and broad GUT prefix denial.
- [x] Bind bootstrap to PR #155 only.
- [x] Replace remediation prefixes with a separate exact-path authorization record.
- [x] Reject mixed HiGodot authoring and GUT test change sets.
- [x] Re-run 12 focused tests, py_compile, contract, bootstrap entry, and unauthorized GUT path denial in reconstructed scope.
- [ ] Re-run these commands in GitHub Actions when account billing/runner execution is restored.

### Task 6: Activation follow-up — separate authorization required

- [ ] Create an exact-path vendor reconciliation Decision and Draft PR without Godot authoring files.
- [ ] Prove vendored file manifest against reviewed upstream commit.
- [ ] Create a GUT canary under `tests/gut` and JUnit report path.
- [ ] Use HiGodot separately for any approved `project.godot` activation; do not combine with GUT test changes.
- [ ] Run exact Godot 4.7 import, GUT CLI smoke, existing regression, Windows, and Android gates.
