# Barracks 2,000-Seed Smoke Sweep Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build and execute a deterministic, audit-ready 2,000-seed smoke simulator for the approved barracks economy, production, physical reel, and Stage 1–5 pressure baseline.

**Architecture:** A standard-library Python script loads the canon baseline and a separate non-canon assumption manifest. It applies common random numbers to nine parameter vectors, writes JSON and CSV results, and classifies identifiability before any balance recommendation. Static tests validate inputs, output schema, deterministic reruns, hard Stop-ship results, and product-file boundaries.

**Tech Stack:** Python 3 standard library, `unittest`, JSON, CSV, SHA-256.

## Global Constraints

- Decision ID: `OMW-DEC-20260806-PLANNING-BARRACKS-SMOKE-SWEEP-RESULTS-AND-IDENTIFIABILITY-GATE-V1`.
- Use exactly 2,000 smoke seeds and common random numbers.
- Do not modify GDScript, Scene, Resource, project.godot, or gameplay data.
- Natural centerline, normal-grade rewards only; Lucky, move optimization, casualty, and lane commitment are not modeled.
- The 15-minute snapshot is censored at the approved Stage 5 end, 830 seconds.
- Do not select a final product parameter vector from smoke results.

---

### Task 1: RED smoke contract

**Files:**
- Create: `tests/python/test_barracks_smoke_sweep.py`

**Interfaces:**
- Consumes: 3/10 baseline JSON and the approved KPI contract.
- Produces: failing assertions for missing model, runner, result, authority, and review artifacts.

- [ ] Write the contract test with exact Decision ID, seed count, input SHA checks, output schema, threshold markers, identifiability classification, and product-boundary assertions.
- [ ] Run `python -m unittest tests.python.test_barracks_smoke_sweep -v`.
- [ ] Confirm RED is caused by missing Gate 4 artifacts.
- [ ] Commit the RED test separately.

### Task 2: Model assumptions and deterministic runner

**Files:**
- Create: `docs/analysis/barracks_simulation/smoke_model_assumptions.v1.json`
- Create: `docs/analysis/barracks_simulation/run_barracks_smoke_sweep.py`

**Interfaces:**
- Consumes: `current_maprun_economy_pressure_baseline.v1.json` and the assumption JSON.
- Produces: `run_smoke_sweep(root, seed_count=2000)` and CLI JSON/CSV output.

- [ ] Add nine parameter vectors, pressure affinities, LOW/MID/HIGH support envelopes, model omissions, and exact thresholds to the assumption manifest.
- [ ] Implement SplitMix64-derived deterministic streams without third-party packages.
- [ ] Implement phase timing, income, construction, production, physical reel source counts, natural centerline spins, build plans, and fixed special results.
- [ ] Calculate primary KPIs, support sensitivity, failure markers, and SHA provenance.
- [ ] Run a 32-seed development pass and verify deterministic byte-identical JSON output.

### Task 3: Execute 2,000-seed smoke

**Files:**
- Create: `docs/analysis/barracks_simulation/smoke_sweep_2000.v1.json`
- Create: `docs/analysis/barracks_simulation/smoke_sweep_2000.v1.csv`

**Interfaces:**
- Consumes: runner and both input manifests.
- Produces: complete smoke results with 9 vectors and the baseline summary.

- [ ] Execute `python docs/analysis/barracks_simulation/run_barracks_smoke_sweep.py --root . --seeds 2000`.
- [ ] Verify seed count, vector count, common-random-number marker, and input SHA-256 values.
- [ ] Re-run and verify JSON and CSV hashes are unchanged.
- [ ] Independently recompute the baseline threshold failures from JSON.

### Task 4: Decision and adversarial review

**Files:**
- Create: `docs/design/APPROVED_OMENWARD_BARRACKS_SMOKE_SWEEP_RESULTS_2026-08-06.md`
- Create: `docs/reviews/ADVERSARIAL_BARRACKS_SMOKE_SWEEP_REVIEW_2026-08-06.md`
- Create: `docs/reviews/PR154_BARRACKS_SMOKE_SWEEP_LOCAL_VERIFICATION_2026-08-06.md`

**Interfaces:**
- Consumes: exact smoke result hashes and threshold outcomes.
- Produces: 4/10 authority, Stop-ship classification, next Gate, and bounded verification evidence.

- [ ] Record `SMOKE_COMPLETED_CONDITIONAL_FAIL` when general validity is support-sensitive or token burst exceeds 0.45.
- [ ] Separate robust economy/reel findings from non-identifiable battle findings.
- [ ] Prohibit 10,000-seed escalation and product implementation.
- [ ] Record full-checkout, full-suite, Godot, runtime, and human-QA boundaries.

### Task 5: Router and Sheet synchronization

**Files:**
- Modify: `docs/ACTIVE_CONTEXT.md`
- Modify: `docs/CURRENT_IMPLEMENTATION_STATUS.md`
- Modify: `docs/DECISIONS_PENDING.md`
- Modify: `docs/PROJECT_CANON_DECISION_LEDGER.md`
- Modify: `docs/DOCUMENTATION_MAP.md`
- Modify: `docs/DOCUMENT_LIFECYCLE_REGISTRY.md`

**Interfaces:**
- Consumes: exact PR HEAD and result hashes.
- Produces: a single current 4/10 route and next Gate.

- [ ] Update the six router documents without changing product files.
- [ ] Run the focused unittest and `py_compile`.
- [ ] Synchronize GitHub and Google Sheet with the same Decision ID.
- [ ] Perform bounded read-back of every written range.
