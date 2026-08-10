# OMENWARD Canon Freshness v4.5 Routing Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Reconcile OMENWARD active canon and Google Sheet to one current truth, activate the user-approved v4.5 Thin Adapter in Phase A, and preserve v4.4/runtime history without starting Phase C Godot implementation.

**Architecture:** Keep v4.4 state/validator surfaces immutable as historical regression evidence. Add a v4.5 current routing layer (`ACTIVE_INTEGRATED_CONTRACT_STATE.v2.json` + 2026-08-11 Thin Adapter binding), propagate approved Special T1 TokenSource truth only to active consumers, and sync the same Decision ID into bounded Sheet surfaces. Current planning/runtime history is carried by `main`, PR #175, Issue #176, and PR #177 with explicit phase gates.

**Tech Stack:** Markdown canon, JSON state/evidence, Python `unittest`, GitHub Actions with immutable Action SHAs, Google Sheets connector.

## Global Constraints

- Decision ID: `OMW-DEC-20260811-OPS-CANON-FRESHNESS-V45-ROUTING-V1`.
- Base current observed: `315c66eea9614c284b9c11c4d522141065dfa4b0`.
- OMENWARD activation baseline: `87339f87949c8faea0dfe1482c5d0887a04d94f4`.
- `project_local_path` and `godot_project_path`: `C:/Users/user/Documents/GitHub/Ninza/omenward`.
- v4.5 adapter policy: `THIN_ADAPTER_DO_NOT_DUPLICATE_BASE_CANON`.
- Current phase: `PHASE_A_GPT_CHAT_PLANNING`.
- Phase C remains blocked until `USER_EXPLICIT_PLANNING_COMPLETE_DECLARATION` and Phase B final review complete.
- Persistent PowerShell/Codex/Godot authoring is forbidden in this plan.
- PR #175 remains Draft with 7 runtime/fixture gaps; PR #177 remains `REFERENCE_ONLY_DO_NOT_MERGE`.
- Historical v4.4 state/validator/test/workflow remain intact.

---

### Task 1: Freeze RED contract

**Files:**
- Create: `tests/python/test_canon_freshness_v45_routing.py`
- Create: `.github/workflows/validate-canon-freshness-v4-5.yml`

**Interfaces:**
- Consumes: current main active canon and user-approved Decision.
- Produces: exact regression assertions for v4.5 authority, TokenSource propagation, entry routing, lifecycle, and Sheet sync evidence.

- [x] **Step 1: Write failing test**
- [x] **Step 2: Run exact-head GitHub Actions and verify intended failure**
- [x] **Step 3: Confirm existing Omenward Core/Base v9 checks remain Green at RED head**

Observed RED: run `31433522187`, 8 tests = 5 failures + 3 errors; missing v4.5 artifacts and stale active consumers are the failure causes.

### Task 2: Add v4.5 current authority layer

**Files:**
- Create: `docs/process/APPROVED_OMENWARD_CANON_FRESHNESS_AND_V4_5_THIN_ADAPTER_2026-08-11.md`
- Create: `docs/process/ACTIVE_INTEGRATED_CONTRACT_BINDING_2026-08-11.md`
- Create: `docs/operations/ACTIVE_INTEGRATED_CONTRACT_STATE.v2.json`

**Interfaces:**
- Consumes: v4.5 r2 user source, fresh Base/project/PR/Sheet state.
- Produces: current human and machine routing without mutating v4.4 history.

- [ ] **Step 1: Add approved Decision authority**
- [ ] **Step 2: Add project-specific Thin Adapter with OMENWARD paths**
- [ ] **Step 3: Add v2 machine state with Phase C BLOCK**

### Task 3: Repair active canon consumers

**Files:**
- Modify: `AGENTS.md`
- Modify: `docs/PROJECT_CORE.md`
- Modify: `docs/DOCUMENTATION_MAP.md`
- Modify: `docs/DOCUMENT_LIFECYCLE_REGISTRY.md`
- Modify: `docs/ACTIVE_CONTEXT.md`
- Modify: `docs/CURRENT_IMPLEMENTATION_STATUS.md`
- Modify: `docs/OMENWARD_GDD_CURRENT_CANON.md`
- Modify: `docs/PROJECT_GOOGLE_SHEET_WORKBOOK.md`
- Modify: `docs/PROJECT_CANON_DECISION_LEDGER.md`
- Modify: `docs/DECISIONS_PENDING.md`

**Interfaces:**
- Consumes: approved amendment + v4.5 current authority.
- Produces: one cold-start/current truth while preserving historical design docs.

- [ ] **Step 1: Route cold-start docs to 10/10 + v4.5 Phase A**
- [ ] **Step 2: Replace only active GDD Special T1 NONE output with selected-unit TokenSource truth**
- [ ] **Step 3: Remove current Workbook republication of NONE; mark old Tier rows historical**
- [ ] **Step 4: Route v4.4 binding/state as historical in Lifecycle**
- [ ] **Step 5: Keep 9/10/FV evidence and Issue #176 gap facts intact**

### Task 4: Synchronize Google Sheet

**Files:**
- Create after write/readback: `docs/operations/CANON_FRESHNESS_V45_SHEET_SYNC_EVIDENCE_2026-08-11.json`

**Interfaces:**
- Consumes: same Decision ID and exact Draft PR head.
- Produces: proposed Sheet state and bounded reread evidence.

- [ ] **Step 1: Fresh-read exact target ranges**
- [ ] **Step 2: Update hub/current decision/work order/audit/rules/history without overwriting history**
- [ ] **Step 3: Bounded reread all written ranges**
- [ ] **Step 4: Persist PASS evidence JSON**

### Task 5: Exact-head review and merge

**Files:**
- Modify only if review findings require bounded repair.

**Interfaces:**
- Consumes: complete PR diff and exact-head CI.
- Produces: merge-eligible planning canon or a truthful blocker.

- [ ] **Step 1: Run canon test and all triggered exact-head workflows**
- [ ] **Step 2: Perform adversarial attack → validate-critique → decision-report**
- [ ] **Step 3: Verify unresolved review threads = 0**
- [ ] **Step 4: Re-read Base main/open PRs and OMENWARD main/open PRs for race**
- [ ] **Step 5: Squash merge only if strict up-to-date and all gates pass**
- [ ] **Step 6: Read merged main and push CI**
- [ ] **Step 7: Change Sheet status from `PROPOSED_SHEET_CHANGE` to `MERGED_CANON` with merge SHA and reread**
- [ ] **Step 8: Refresh PR #175/#177 metadata; do not merge either**
