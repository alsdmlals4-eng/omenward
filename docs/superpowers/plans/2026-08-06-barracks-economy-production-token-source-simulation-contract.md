# Barracks Economy, Production, and TokenSource Simulation Contract Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Publish and verify a proposed simulation contract that can later drive reproducible barracks balance sweeps.

**Architecture:** Keep current planning canon immutable, define dimensionless PoC ranges and KPI guardrails in documents and Google Sheet, and validate routing/markers with one focused Python unittest. No simulation engine or product behavior is added in this change.

**Tech Stack:** Markdown, Python `unittest`, GitHub PR workflow, Google Sheets.

## Global Constraints

- Decision ID: `OMW-DEC-20260806-PLANNING-BARRACKS-ECONOMY-PRODUCTION-TOKEN-SOURCE-SIMULATION-CONTRACT-V1`.
- Status remains `PROPOSED_SIMULATION_CONTRACT / USER_REVIEW_PENDING`.
- Do not modify GDScript, Scene, Resource, project.godot, or gameplay data.
- Do not claim balance Green from static document tests.
- Preserve same-unit separate-path barracks identity and forbid free reroll.
- Keep `C:/Users/user/Documents/GitHub/Ninza/omenward` unchanged.

---

### Task 1: RED contract

**Files:**
- Create: `tests/python/test_barracks_economy_production_token_source_simulation_contract.py`

**Interfaces:**
- Consumes: repository Markdown files.
- Produces: structural contract assertions for proposal status, inputs, scenarios, KPIs, risks, and routing.

- [ ] **Step 1: Create the failing test before proposal documents exist**

Use the exact test file in this PR.

- [ ] **Step 2: Verify RED**

Run:

```bash
python -m unittest tests.python.test_barracks_economy_production_token_source_simulation_contract -v
```

Expected before Task 2: `FileNotFoundError` for the proposed contract document.

- [ ] **Step 3: Commit**

```bash
git add tests/python/test_barracks_economy_production_token_source_simulation_contract.py
git commit -m "test: add RED barracks simulation contract"
```

### Task 2: Contract and adversarial review

**Files:**
- Create: `docs/design/PROPOSED_OMENWARD_BARRACKS_ECONOMY_PRODUCTION_TOKEN_SOURCE_SIMULATION_CONTRACT_2026-08-06.md`
- Create: `docs/reviews/ADVERSARIAL_BARRACKS_ECONOMY_PRODUCTION_TOKEN_SOURCE_SIMULATION_REVIEW_2026-08-06.md`
- Create: `docs/superpowers/specs/2026-08-06-barracks-economy-production-token-source-simulation-contract-design.md`

**Interfaces:**
- Consumes: approved barracks amendment and onboarding canon.
- Produces: required-input schema, PoC search space, scenario matrix, KPI thresholds, Stop-ship rules, and artifact schema.

- [ ] **Step 1: Write the proposed contract with all mandatory markers**
- [ ] **Step 2: Write the adversarial review with exploit and dominance checks**
- [ ] **Step 3: Write the architecture spec separating simulation artifacts from product implementation**
- [ ] **Step 4: Commit**

```bash
git add docs/design docs/reviews docs/superpowers/specs
git commit -m "docs: define barracks simulation contract"
```

### Task 3: Authority routing repair

**Files:**
- Modify: `docs/ACTIVE_CONTEXT.md`
- Modify: `docs/DECISIONS_PENDING.md`
- Modify: `docs/PROJECT_CANON_DECISION_LEDGER.md`
- Modify: `docs/DOCUMENTATION_MAP.md`
- Modify: `docs/DOCUMENT_LIFECYCLE_REGISTRY.md`
- Modify: `docs/HANDOFF_CONTEXT.md`
- Modify: `docs/CURRENT_IMPLEMENTATION_STATUS.md`

**Interfaces:**
- Consumes: main-canonical 10/10 onboarding and barracks amendment.
- Produces: proposal routing without incrementing the approved GrillMe counter.

- [ ] **Step 1: Mark the new Decision as `[제안] / USER_REVIEW_PENDING`**
- [ ] **Step 2: Remove stale 6/10, 7/10, and no-TokenSource authority markers from current routers**
- [ ] **Step 3: Keep historical documents as evidence instead of silently rewriting them**
- [ ] **Step 4: Commit**

```bash
git add docs/ACTIVE_CONTEXT.md docs/DECISIONS_PENDING.md docs/PROJECT_CANON_DECISION_LEDGER.md docs/DOCUMENTATION_MAP.md docs/DOCUMENT_LIFECYCLE_REGISTRY.md docs/HANDOFF_CONTEXT.md docs/CURRENT_IMPLEMENTATION_STATUS.md
git commit -m "docs: route proposed barracks simulation gate"
```

### Task 4: Google Sheet matrix

**Files:**
- Create tab: `44_병영_경제_시뮬레이션`
- Update: `00_프로젝트_허브`
- Update: `04_누락_충돌_감사`
- Update: `99_변경이력`

**Interfaces:**
- Consumes: proposed contract axes and thresholds.
- Produces: bounded, reviewable experiment matrix with the same Decision ID and exact PR HEAD.

- [ ] **Step 1: Create the tab and write input ranges, scenarios, KPIs, and decision rules**
- [ ] **Step 2: Record the stale-router audit and proposal status**
- [ ] **Step 3: Read back bounded ranges and record `SHEET_BOUNDED_READBACK_PASS`**

### Task 5: GREEN candidate verification

**Files:**
- Test: `tests/python/test_barracks_economy_production_token_source_simulation_contract.py`

**Interfaces:**
- Consumes: all files from Tasks 1–4.
- Produces: exact-head verification report.

- [ ] **Step 1: Run focused test**

```bash
python -m unittest tests.python.test_barracks_economy_production_token_source_simulation_contract -v
```

Expected: 9 tests pass.

- [ ] **Step 2: Compile the test**

```bash
python -m py_compile tests/python/test_barracks_economy_production_token_source_simulation_contract.py
```

Expected: exit code 0.

- [ ] **Step 3: Compare branch to main**

Expected: documents and one Python contract test only; product paths changed = 0.

- [ ] **Step 4: Open a Draft PR**

The PR must state that simulation results, full Python suite, Godot runtime, and human QA are not run.
