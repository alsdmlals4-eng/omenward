# Current MapRun Economy and Pressure Baseline Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add the approved Stage 1~5 economy, production, maintenance-clock, pressure, and opportunity-cost simulation baseline.

**Architecture:** Keep the human authority, machine JSON, adversarial review, static contract test, routers, and Google Sheet synchronized by one Decision ID. The result unlocks smoke simulation only and does not modify gameplay files.

**Tech Stack:** Markdown, JSON, Python unittest, GitHub PR, Google Sheets.

## Global Constraints

- Decision ID: `OMW-DEC-20260806-PLANNING-CURRENT-MAPRUN-ECONOMY-AND-PRESSURE-BASELINE-V1`.
- Approval count: `3_OF_10`.
- Do not modify GDScript, Scene, Resource, project.godot, or gameplay data.
- Keep PR #154 Draft and do not merge.
- Preserve legacy documents as evidence; supersede through lifecycle routing.
- Smoke sweep becomes ready but is not executed in this plan.

---

### Task 1: RED contract

**Files:**
- Create: `tests/python/test_current_maprun_economy_pressure_baseline.py`

**Interfaces:**
- Consumes: proposed Decision ID and expected authority paths.
- Produces: static markers for authority, JSON, review, routers, and gates.

- [ ] Write the failing unittest.
- [ ] Run `python -m unittest tests.python.test_current_maprun_economy_pressure_baseline -v` in a reconstructed directory.
- [ ] Confirm `FileNotFoundError` for the missing approved authority.
- [ ] Commit `test: add RED current MapRun baseline contract`.

### Task 2: Human and machine baseline

**Files:**
- Create: `docs/design/APPROVED_OMENWARD_CURRENT_MAPRUN_ECONOMY_AND_PRESSURE_BASELINE_2026-08-06.md`
- Create: `docs/analysis/barracks_simulation/current_maprun_economy_pressure_baseline.v1.json`
- Create: `docs/reviews/ADVERSARIAL_CURRENT_MAPRUN_ECONOMY_AND_PRESSURE_BASELINE_REVIEW_2026-08-06.md`
- Create: `docs/superpowers/specs/2026-08-06-current-maprun-economy-pressure-baseline-design.md`
- Create: `docs/superpowers/plans/2026-08-06-current-maprun-economy-pressure-baseline.md`

**Interfaces:**
- Consumes: 1/10 simulation contract, 2/10 provenance manifest, onboarding flow, MapRun structure, pressure matrix, physical-reel rules.
- Produces: exact Stage 1~5 smoke inputs and run-gate state.

- [ ] Add exact economy and construction values.
- [ ] Add the maintenance clock matrix.
- [ ] Add general and five-special production intervals.
- [ ] Add Stage 1~5 Threat Unit budgets and target offsets.
- [ ] Add vector opportunity-cost formulas.
- [ ] Mark smoke ready and later sweeps blocked.
- [ ] Commit the authority, JSON, review, spec, and plan.

### Task 3: Router synchronization

**Files:**
- Modify: `docs/ACTIVE_CONTEXT.md`
- Modify: `docs/DECISIONS_PENDING.md`
- Modify: `docs/PROJECT_CANON_DECISION_LEDGER.md`
- Modify: `docs/DOCUMENTATION_MAP.md`
- Modify: `docs/DOCUMENT_LIFECYCLE_REGISTRY.md`

**Interfaces:**
- Consumes: approved 3/10 authority.
- Produces: one current routing path and next Gate `BARRACKS_SMOKE_SWEEP_EXECUTION`.

- [ ] Update counters and latest authority.
- [ ] Move the six 2/10 blockers to resolved-by-3/10 history.
- [ ] Keep product implementation unauthorized.
- [ ] Commit router synchronization.

### Task 4: Focused GREEN verification

**Files:**
- Create: `docs/reviews/PR154_CURRENT_MAPRUN_BASELINE_LOCAL_VERIFICATION_2026-08-06.md`

**Interfaces:**
- Consumes: files read by the focused unittest.
- Produces: bounded local evidence only.

- [ ] Reconstruct the focused files from exact PR HEAD.
- [ ] Run the focused unittest and require 11/11 PASS.
- [ ] Run `python -m py_compile tests/python/test_current_maprun_economy_pressure_baseline.py`.
- [ ] Parse the JSON and record SHA-256.
- [ ] State that full checkout, full suite, Godot, simulation, runtime, and human QA were not run.
- [ ] Commit the verification record.

### Task 5: Google Sheet and PR synchronization

**Files:**
- Edit Sheet ranges for hub, decision, evidence, audit, simulation matrix, new baseline tab, and change history.
- Update PR #154 title/body.

**Interfaces:**
- Consumes: final GitHub HEAD.
- Produces: same Decision ID and exact HEAD in GitHub and Sheet.

- [ ] Read target ranges and metadata.
- [ ] Add `46_MapRun_경제_압력_기준선`.
- [ ] Append 3/10 decision, evidence, audit, and history rows.
- [ ] Run bounded read-back.
- [ ] Recheck main/head ancestry, mergeability, and Actions annotations.
- [ ] Keep PR Draft and do not merge.
