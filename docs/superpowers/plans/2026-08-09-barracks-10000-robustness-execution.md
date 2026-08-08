# Barracks 10000-Seed Robustness Execution Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Execute and persist one deterministic 10,000-seed robustness-only run for the approved non-final V00 cost/interval envelope without overwriting the canonical 2,000-seed evidence or creating parameter-selection authority.

**Architecture:** Add a dedicated analysis runner with its own Decision ID, fixed seed count, unique output stem, input-hash binding, and V00 envelope assertions. Persist JSON/CSV results under a new 10k stem, validate them against a fresh exact-head rerun in CI, then advance only the robustness execution state while leaving functional value, final vector, 50k, product numerics, and product implementation blocked.

**Tech Stack:** Python 3.12, NumPy simulator modules already in `docs/analysis/barracks_simulation`, `unittest`, GitHub Actions, Google Sheet evidence sync.

## Global Constraints

- Decision ID: `OMW-DEC-20260809-PLANNING-BARRACKS-10000-SEED-ROBUSTNESS-EXECUTION-V1`.
- Parent Decision: `OMW-DEC-20260808-PLANNING-BARRACKS-10000-SEED-ROBUSTNESS-ONLY-REVIEW-V1`.
- Seed count is exactly `10000` with common random numbers.
- Robustness envelope is only `V00_BASELINE_COST_INTERVAL_ONLY`, special barracks cost `60`, special interval multiplier `1.70`.
- `SPECIAL_FUNCTIONAL_VALUE_INDEX = DEFERRED_UNTIL_PRODUCT_COMBAT_NUMERICS`.
- Combat/role metrics remain `DIAGNOSTIC_NON_IDENTIFIABLE` and cannot fail the robustness gate.
- `PARAMETER_SELECTION_10000 = NOT_AUTHORIZED`; `CONFIRMATION_SWEEP_50000 = BLOCKED`.
- Canonical 2k JSON/CSV and their hashes must remain unchanged.
- Product/Godot paths remain untouched and Entry Gate remains BLOCK.

---

### Task 1: Lock the dedicated execution contract with RED tests

**Files:**
- Create: `tests/python/test_barracks_10000_robustness_execution.py`
- Create: `.github/workflows/validate-barracks-10000-robustness-execution.yml`

**Interfaces:**
- Consumes: existing 2k evidence, current baseline/model/remediation JSON, current simulator modules.
- Produces: contract expected from `run_barracks_robustness_10000.py` and committed `robustness_sweep_10000.v1.{json,csv}`.

- [ ] **Step 1:** Write tests asserting the dedicated runner exists, exports fixed provenance constants, preserves 2k hashes, binds V00 cost/interval, and has committed 10k evidence with `seed_count=10000` and no selected parameter vector.
- [ ] **Step 2:** Run `python -m unittest tests.python.test_barracks_10000_robustness_execution`; expected RED because the dedicated runner and 10k evidence do not exist.
- [ ] **Step 3:** Record exact RED workflow run/job and expected failures.

### Task 2: Implement the minimum dedicated runner

**Files:**
- Create: `docs/analysis/barracks_simulation/run_barracks_robustness_10000.py`

**Interfaces:**
- Produces: `run_robustness_10000(root: Path, output_dir: Path | None = None) -> tuple[Path, Path]`, fixed `DECISION_ID`, `PARENT_DECISION_ID`, `SEED_COUNT`, `OUTPUT_STEM`.

- [ ] **Step 1:** Implement fail-closed assertions for parent Decision, baseline V00 cost/interval, functional-value deferral, fixed 10k seed count, and source 2k hashes.
- [ ] **Step 2:** Reuse `SmokeSimulator` and `aggregate_vector` for V00 only; preserve raw diagnostics but derive pass/fail only from decision-eligible non-combat thresholds.
- [ ] **Step 3:** Write uniquely named 10k JSON/CSV outputs without touching `smoke_sweep_2000.v2.*`.
- [ ] **Step 4:** Run focused tests; expected remaining RED only for missing committed 10k result files.

### Task 3: Execute exactly 10,000 seeds and persist evidence

**Files:**
- Create: `docs/analysis/barracks_simulation/robustness_sweep_10000.v1.json`
- Create: `docs/analysis/barracks_simulation/robustness_sweep_10000.v1.csv`

**Interfaces:**
- Consumes: exact branch runner and exact input files.
- Produces: durable 10k evidence with input hashes, output hashes recorded by authority/state docs, V00-only result, and explicit diagnostic boundary.

- [ ] **Step 1:** Execute `python docs/analysis/barracks_simulation/run_barracks_robustness_10000.py --root . --output-dir <isolated-output>` from the exact branch checkout.
- [ ] **Step 2:** Verify `seed_count=10000`, `parameter_vector_count=1`, `baseline_vector.vector_id=V00_BASELINE`, `selected_parameter_vector=null`, and decision failures separately from diagnostic failures.
- [ ] **Step 3:** Verify existing 2k JSON/CSV SHA-256 remain `a02c4e0bad6a7113937fbd23f4521c364d109944c7f05c94eb5839b9119d00e2` and `3b6a164a4ca847d29b82d73b3841100f246cdc36b9b86f30198bfcfe586f6560`.
- [ ] **Step 4:** Persist the exact generated 10k JSON/CSV and rerun focused tests to GREEN.

### Task 4: Reconcile authority and durable state

**Files:**
- Create: `docs/design/APPROVED_OMENWARD_BARRACKS_10000_SEED_ROBUSTNESS_EXECUTION_RESULTS_2026-08-09.md`
- Modify: `docs/operations/ACTIVE_INTEGRATED_CONTRACT_STATE.v1.json`
- Modify: `docs/DECISIONS_PENDING.md`
- Modify: `docs/PROJECT_CANON_DECISION_LEDGER.md`
- Modify: `docs/process/ACTIVE_INTEGRATED_CONTRACT_BINDING_2026-08-06.md`
- Modify: `tools/validate_active_integrated_contract_v4_4.py`
- Modify: `tests/python/test_active_integrated_contract_v4_4.py`
- Modify: `.github/workflows/validate-active-integrated-contract-v4-4.yml`

**Interfaces:**
- Consumes: exact 10k result/hashes and current Entry Gate.
- Produces: robustness execution complete state while functional-value combat numerics remain the barracks design blocker.

- [ ] **Step 1:** Record exact metrics, hashes, provenance, and result status without converting diagnostic combat failures into balance failures.
- [ ] **Step 2:** Remove only the user-approval/dedicated-runner blockers that this Gate actually closes.
- [ ] **Step 3:** Keep `BARRACKS_FUNCTIONAL_VALUE_COMBAT_NUMERICS_REQUIRED`, 50k, final vector, final numerics, product implementation, and tooling/local blockers intact.
- [ ] **Step 4:** Run the full focused v4.4/barracks contract suite.

### Task 5: Exact-head validation, Sheet sync, adversarial review, and merge

**Files:**
- Google Sheet: `00_프로젝트_허브`, `02_현재_확정결정`, `04_누락_충돌_감사`, `47_병영_Smoke_결과`, `99_변경이력`.

**Interfaces:**
- Produces: same Decision ID in GitHub and Sheet, one real 10k result row, exact-head CI evidence, role-separated review, squash merge, merged-main readback.

- [ ] **Step 1:** Confirm all exact-head workflows are Green and the CI rerun reproduces committed 10k JSON/CSV byte-for-byte or by documented canonical hash comparison.
- [ ] **Step 2:** Adversarially verify product paths are zero, 2k evidence hashes are unchanged, no parameter-selection/final numerics authority leaked, and actual 10k evidence is unique.
- [ ] **Step 3:** Sync the same Decision ID and exact-head evidence to Sheet; add exactly one `47_병영_Smoke_결과` row because a real 10k run now exists.
- [ ] **Step 4:** Add role-separated review, mark Ready, squash merge with expected head SHA, read merged main, and update Sheet to the merge SHA.
