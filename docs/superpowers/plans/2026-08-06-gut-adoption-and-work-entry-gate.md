# GUT Adoption and Work Entry Gate Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Formally adopt GUT 9.7.1 as OMENWARD's test authority while preserving HiGodot as the sole Godot authoring authority and enforcing a fail-closed current-state work-entry gate.

**Architecture:** A versioned adoption record owns provenance, compatibility, authority boundaries, consumption, CI, and rollback. A separate work-entry state records fresh GitHub/Sheet readback and blocks normal changes while allowing only exact bootstrap and remediation paths.

**Tech Stack:** Python 3.12, unittest, JSON, Markdown, GitHub Actions, Godot 4.7, GUT 9.7.1.

## Global Constraints

- HiGodot is the sole Scene/Node/Resource/project-setting mutation authority.
- GUT owns test discovery, execution, assertions, doubles, and reports only.
- Do not modify `project.godot`, Scene, Resource, gameplay code, or data in this Draft adoption PR.
- GUT activation requires exact vendor reconciliation, Godot import, CLI smoke, and project regression.
- The work-entry gate is fail-closed; only exact bootstrap/remediation scope may proceed while blocked.

---

### Task 1: Authority and entry-gate RED tests

**Files:**
- Create: `tests/python/test_godot_authoring_test_authority.py`

- [ ] Write failing tests for role overlap, premature activation, image READY/AWAITING promotion, and non-remediation entry.
- [ ] Run `python -m unittest tests.python.test_godot_authoring_test_authority -v` and confirm failure because the validator is missing.
- [ ] Commit the RED test.

### Task 2: Minimal validator and versioned records

**Files:**
- Create: `tools/validate_godot_authoring_test_authority.py`
- Create: `docs/operations/GUT_ADOPTION_RECORD.v1.json`
- Create: `docs/operations/WORK_ENTRY_GATE_STATE.v1.json`

- [ ] Implement exact schema and fail-closed entry evaluation.
- [ ] Record upstream and project vendor tree SHAs without claiming equality.
- [ ] Run the focused unittest and confirm seven tests pass.
- [ ] Run `python tools/validate_godot_authoring_test_authority.py --contract` and confirm contract PASS with blocked entry status.

### Task 3: Adoption specification, gate routing, and adversarial review

**Files:**
- Create: `docs/design/PROPOSED_OMENWARD_HIGODOT_GUT_AUTHORITY_AND_GUT_9_7_1_ADOPTION_2026-08-06.md`
- Create: `docs/operations/OMENWARD_WORK_ENTRY_GATE_2026-08-06.md`
- Create: `docs/reviews/ADVERSARIAL_GUT_ADOPTION_AND_WORK_ENTRY_GATE_REVIEW_2026-08-06.md`
- Modify: `AGENTS.md`

- [ ] Route all work through the validator command.
- [ ] Preserve current blockers and forbid READY/AWAITING promotion.
- [ ] Re-run tests and contract validation.

### Task 4: CI bootstrap gate and Draft PR

**Files:**
- Create: `.github/workflows/validate-godot-authoring-test-authority.yml`

- [ ] Compile validator/tests.
- [ ] Run focused tests and contract validation.
- [ ] Pass exact changed files to `--entry`; allow only bootstrap/remediation paths while blocked.
- [ ] Open a Draft PR from a branch based on exact main `7588317f294d602cfad5f7f15bfebcf849b8a77b`.
- [ ] Re-read the PR exact HEAD and Sheet Decision row.
