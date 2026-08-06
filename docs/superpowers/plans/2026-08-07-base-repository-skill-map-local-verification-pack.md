# Base recovery map and existing Actions validation simplification

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Preserve the fail-closed Base recovery map while removing the local verification pack and reusing the existing Full validation workflow.

**Architecture:** `validate-omenward-core.yml` is the single full-validation entrypoint. Its manual-dispatch matrix covers standard Ubuntu and Windows GitHub-hosted runners with Python 3.11, 3.12, and 3.13, while the existing Godot 4.7.1 job remains unchanged. Base recovery evidence stays separate and incomplete.

**Tech Stack:** GitHub Actions, Python `unittest`, Godot 4.7.1, Google Sheets decision ledger.

## Global Constraints

- Decision ID remains `OMW-DEC-20260807-PROCESS-BASE-REPOSITORY-SKILL-MAP-AND-LOCAL-VERIFICATION-PACK-V1`.
- Repository visibility is not changed.
- `RECOVERY_STATUS=INCOMPLETE`.
- `BASE_RECOVERY_BLOCKER_CLEARED=FALSE`.
- `ENTRY_GATE=BLOCK`.
- Do not claim `ACTIONS_GREEN` without an exact-head successful run.
- Do not authorize product, Godot authoring, GUT activation, audio import, Ready, or merge.

---

### Task 1: Strengthen the existing CI usage contract

**Files:**
- Modify: `tests/python/test_ci_usage_contract.py`
- Modify: `tools/validate_ci_usage_contract.py`
- Modify: `.github/workflows/validate-omenward-core.yml`

- [x] Write failing assertions for manual dispatch, standard runner labels, and Python 3.11/3.12/3.13.
- [x] Observe RED against the former Python 3.12/3.13 matrix.
- [x] Add Python 3.11 and reject `self-hosted`.
- [x] Run the focused CI usage suite to GREEN.

### Task 2: Remove the local verification pack

**Files:**
- Create: `tests/python/test_base_recovery_map.py`
- Modify: `docs/operations/BASE_WHOLE_REPOSITORY_AND_SKILL_MAP.v1.json`
- Modify: `docs/operations/BASE_WHOLE_REPOSITORY_AND_SKILL_MAP_2026-08-07.md`
- Delete: dedicated local workflow, matrix, launchers, receipt runner, validator, and local-pack regression tests

- [x] Write a failing test requiring the existing Actions workflow as the only validation path.
- [x] Observe RED while local pack files and old state remain.
- [x] Add `validation_strategy` and remove all local pack paths.
- [x] Run the Base recovery map contract to GREEN.

### Task 3: Synchronize authority records

**Files:**
- Modify: this plan and adversarial review
- Update: PR #159 title/body
- Update: Google Sheet rows under the same Decision ID

- [ ] Record the exact new PR head and changed-file list.
- [ ] Read back GitHub and Sheet values.
- [ ] Leave the PR Draft and merge blocked until exact-head Actions Green.
