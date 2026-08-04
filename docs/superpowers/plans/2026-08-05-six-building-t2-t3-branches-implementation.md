# OMENWARD Six-Building T2/T3 Branches Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Canonize two mutually exclusive T2 branches and one matching T3 specialization for each of OMENWARD's six current buildings, with explicit pressure coverage, opportunity costs, process policy, automated documentation tests, Sheet synchronization, and PR evidence.

**Architecture:** Documentation-only planning authority. A focused Python unittest suite defines the RED contract; new spec/canon/review/process documents provide the GREEN behavior; central routing files and the Google Sheet expose one Decision ID and `3_OF_10`. No product code or balance values are authorized.

**Tech Stack:** Markdown, Python 3.12 `unittest`, GitHub Actions, GitHub pull requests, Google Sheets bounded read-back.

## Global Constraints

- Decision ID: `OMW-DEC-20260805-PLANNING-SIX-BUILDING-T2-T3-BRANCHES-AND-COUNTERS-V1`.
- Common grammar: `T1 → one of two T2 → matching T3` per building instance.
- Cross-branch and dual-T3 acquisition on one instance are forbidden.
- Exact costs, percentages, ranges, cooldowns, income rates, and Threat Budgets remain `PENDING_SIMULATION`.
- Product code, scenes, resources, game data, runtime, and actual art assets remain unchanged.
- Benchmarking and relevant industry comparison are mandatory inputs.
- Maximum approval batch is 10; high-risk conflict, session end, or large canon impact permits an early checkpoint.
- Every change follows `RED → GREEN → REFACTOR`.
- Every GitHub mutation must name an explicit non-default branch until the PR merge action.

---

### Task 1: Establish the RED contract

**Files:**
- Create: `tests/python/test_building_branch_canon.py`
- Modify: `.github/workflows/validate-project-core-docs.yml`

**Interfaces:**
- Consumes: existing documentation workflow and repository root.
- Produces: failing checks for authority files, branch grammar, pressure coverage, process policy, central routing, and adversarial review.

- [x] **Step 1: Write failing authority and marker tests**

The test requires the four authority files, twelve `얻는 것`/`포기하는 것` branch entries, twelve T3 entries, all six buildings, all five pressure tags, and process-policy markers.

- [x] **Step 2: Wire the test into the documentation workflow**

Run:

```bash
python -m py_compile tests/python/test_building_branch_canon.py
python -m unittest tests.python.test_building_branch_canon -v
```

Expected before GREEN: failure because the 3/10 authority documents and central routes do not exist.

- [x] **Step 3: Verify RED on the Draft PR**

Evidence:

```text
Validate Project Core Documentation run 888 = FAILURE
Existing project-core validator = PASS
Existing CI usage validator = PASS
New building branch tests = expected missing-authority and 2/10-routing failures
```

### Task 2: Record the approved design and operating policy

**Files:**
- Create: `docs/superpowers/specs/2026-08-05-six-building-t2-t3-branches-design.md`
- Create: `docs/process/APPROVED_BENCHMARK_TDD_AND_APPROVAL_BATCH_POLICY_2026-08-05.md`

**Interfaces:**
- Consumes: user-approved common branch grammar, Stage pressure canon, current six-building roster.
- Produces: design constraints and reusable process rules consumed by canon, review, central routing, and tests.

- [ ] **Step 1: Document official benchmark evidence**

Use official sources only:

```text
Kingdom Rush = readable specialized tower roles
Age of Empires IV = strategic identity and opportunity cost
Against the Storm = limited upgrade breadth to control complexity
```

- [ ] **Step 2: Define the process markers**

The policy must contain:

```text
BENCHMARK_REQUIRED
INDUSTRY_COMPARISON_REQUIRED
MAX_APPROVAL_BATCH: 10
EARLY_CHECKPOINT_ON_HIGH_RISK_CONFLICT
EARLY_CHECKPOINT_ON_SESSION_END
EARLY_CHECKPOINT_ON_LARGE_CANON_IMPACT
TDD_MANDATORY
RED → GREEN → REFACTOR
EXPLICIT_BRANCH_REQUIRED_FOR_GITHUB_MUTATION
```

- [ ] **Step 3: Commit the design and policy**

```bash
git add docs/superpowers/specs/2026-08-05-six-building-t2-t3-branches-design.md docs/process/APPROVED_BENCHMARK_TDD_AND_APPROVAL_BATCH_POLICY_2026-08-05.md
git commit -m "docs: define building branch design and planning policy"
```

### Task 3: Create the current building branch authority

**Files:**
- Create: `docs/design/APPROVED_OMENWARD_SIX_BUILDING_T2_T3_BRANCHES_AND_COUNTERS_2026-08-05.md`

**Interfaces:**
- Consumes: Task 2 design spec and Stage pressure authority.
- Produces: current player-visible branch roles for later troop and tactical decisions.

- [ ] **Step 1: Add the common branch grammar**

Required contract:

```text
T1 → T2 A → T3 A
T1 → T2 B → T3 B
CROSS_BRANCH: FORBIDDEN
DUAL_T3: FORBIDDEN
MAPRUN_PERMANENT_CHOICE
```

`MAPRUN_PERMANENT_CHOICE` means the choice persists for that building instance; demolition removes the instance and any later rebuild is a new choice.

- [ ] **Step 2: Add twelve T2 branch contracts**

Each T2 entry contains exactly these player-facing fields:

```text
얻는 것
포기하는 것
유리한 압력
핵심 루프 영향
```

- [ ] **Step 3: Add twelve T3 decision changes**

Each T3 entry must change payoff curve, target priority, commitment doctrine, resource timing, or route coverage. Pure stat text is rejected.

- [ ] **Step 4: Add the pressure coverage matrix and forbidden behaviors**

Required markers:

```text
압력별 최소 두 대응 경로
단일 만능 분기 금지
FREE_RECALL: FORBIDDEN
FREE_CROSS_LANE_MOVE: FORBIDDEN
AUTO_TACTICAL_CAST: FORBIDDEN
INFINITE_GOLD_OR_MANA: FORBIDDEN
T3_ROULETTE_TOKEN: FORBIDDEN
HIDDEN_COUNTER_CHANGE: FORBIDDEN
정확 수치: PENDING_SIMULATION
```

- [ ] **Step 5: Commit the authority document**

```bash
git add docs/design/APPROVED_OMENWARD_SIX_BUILDING_T2_T3_BRANCHES_AND_COUNTERS_2026-08-05.md
git commit -m "docs: canonize six building specialization branches"
```

### Task 4: Run adversarial review and lifecycle audit

**Files:**
- Create: `docs/reviews/ADVERSARIAL_BUILDING_BRANCH_COUNTER_AND_OPPORTUNITY_COST_REVIEW_2026-08-05.md`
- Modify: `docs/DOCUMENT_LIFECYCLE_REGISTRY.md`

**Interfaces:**
- Consumes: Task 3 canon.
- Produces: audit IDs `OMW-AUD-398~419`, mitigations, lifecycle routing, and implementation blocker state.

- [ ] **Step 1: Attack branch dominance and false choice**

Required categories:

```text
DOMINANT_BRANCH_RISK
FALSE_CHOICE_RISK
COMPLEXITY_BUDGET_RISK
PRESSURE_COVERAGE_GAP
```

- [ ] **Step 2: Attack building-specific exploits**

Cover gold double-dipping, farm cap exceptions, Barracks troop-canon preemption, hidden anti-air, Command Post stacking, mana hoarding, demolition resets, and T3-token regression.

- [ ] **Step 3: Preserve implementation boundary**

Required verdict:

```text
PRODUCT_CODE = UNCHANGED
IMPLEMENTATION_READINESS = BLOCKED_BY_TROOP_AND_TACTICAL_DECISIONS
```

- [ ] **Step 4: Register current and superseded authority**

Add the new spec, canon, process policy, and review to `[현행]`; preserve previous building roster as a base-role authority partially extended by this decision rather than superseded wholesale.

### Task 5: Synchronize central authority documents

**Files:**
- Modify: `README.md`
- Modify: `AGENTS.md`
- Modify: `docs/PROJECT_CORE.md`
- Modify: `docs/ACTIVE_CONTEXT.md`
- Modify: `docs/DOCUMENTATION_MAP.md`
- Modify: `docs/DOCUMENT_LIFECYCLE_REGISTRY.md`
- Modify: `docs/OMENWARD_GDD_CURRENT_CANON.md`
- Modify: `docs/DECISIONS_PENDING.md`
- Modify: `docs/OMENWARD_ROADMAP.md`
- Modify: `docs/CURRENT_IMPLEMENTATION_STATUS.md`
- Modify: `docs/HANDOFF_CONTEXT.md`
- Modify: `docs/PROJECT_CANON_DECISION_LEDGER.md`
- Modify: `docs/PROJECT_GOOGLE_SHEET_WORKBOOK.md`

**Interfaces:**
- Consumes: Tasks 2–4.
- Produces: one current Decision ID, `3_OF_10`, next Decision 4/10, and no product authorization.

- [ ] **Step 1: Route the current decision and counter**

Every primary router must contain:

```text
OMW-DEC-20260805-PLANNING-SIX-BUILDING-T2-T3-BRANCHES-AND-COUNTERS-V1
3_OF_10
```

- [ ] **Step 2: Add the process policy to AGENTS and documentation map**

Require relevant benchmarks, industry comparison, TDD, explicit branch writes, ten-approval batch maximum, and early checkpoints.

- [ ] **Step 3: Set the next planning gate**

```text
OMW-DEC-20260805-PLANNING-TROOP-ROLES-SYNERGIES-AND-COUNTERS-V1
```

### Task 6: Synchronize the Google Sheet

**Files:**
- External workbook: `1VLwRtXGDtyj0JFt98wdIOtG6Zqc3wtdfCzSF9Fo6lpw`

**Interfaces:**
- Consumes: exact PR head after GitHub documentation changes.
- Produces: same Decision ID, exact head, `3/10`, branch matrix summary, process policy, audit IDs, and next gate.

- [ ] **Step 1: Write the Decision and process policy**

Update project hub, work order, current decisions, evidence, audit, GDD summary, core loop, rules, main content, economy, UX, art brief, and history tabs.

- [ ] **Step 2: Read back bounded ranges**

Expected:

```text
Decision ID exact match
PR head exact match
counter = 3/10
OMW-AUD-398~419 present
READBACK_PASS
```

### Task 7: GREEN verification and refactor

**Files:**
- Modify only if tests reveal ambiguity or duplication.

**Interfaces:**
- Consumes: all previous tasks.
- Produces: exact-head Green evidence and compact, non-duplicated canon.

- [ ] **Step 1: Run the documentation test suite**

```bash
python -m unittest tests.python.test_project_core_docs tests.python.test_ci_usage_contract tests.python.test_building_branch_canon -v
```

Expected: PASS.

- [ ] **Step 2: Run repository workflows**

Expected exact-head results:

```text
Validate Project Core Documentation = PASS
Validate Omenward GDD Sheet Adoption = PASS
Validate Base v9 adoption = PASS
```

- [ ] **Step 3: Refactor duplicate prose without changing behavior**

Keep the full branch matrix in the responsibility owner. Central docs contain only routing, summary, and boundaries.

- [ ] **Step 4: Re-run all tests after refactor**

Expected: all Green and no warnings that affect the contract.

### Task 8: Fresh PR preflight and merge

**Files:**
- Pull request metadata and Sheet post-merge status only.

**Interfaces:**
- Consumes: exact Green head.
- Produces: merged main canon and post-merge Sheet read-back.

- [ ] **Step 1: Verify preflight**

```text
behind = 0
product paths = 0
reviews = 0 or addressed
unresolved threads = 0
OPEN_P0 = 0
OPEN_P1 = 0
MERGE_BLOCKER = 0
TODO/TBD placeholders = 0
```

- [ ] **Step 2: Mark ready and squash merge with expected head SHA**

- [ ] **Step 3: Update Sheet to merged main SHA and read back**

- [ ] **Step 4: Report unrun evidence honestly**

```text
product implementation = NOT_RUN
simulation = NOT_RUN
runtime = NOT_RUN
human QA = NOT_RUN
actual art asset production = NOT_RUN
```
