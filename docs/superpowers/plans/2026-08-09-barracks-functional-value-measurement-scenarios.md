# Barracks Functional-Value Measurement Scenarios Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Persist a planning-only deterministic measurement-scenario contract that turns approved role relationships into same-input role vectors while marking unavailable runtime outputs as `BLOCKED_RUNTIME_OUTPUT`.

**Architecture:** Add one focused authority document and durable-state block backed by tests that recover current fixture resources and parent functional-review constraints. No product code or data is modified; the Gate closes only the measurement-scenario-definition blocker and leaves role-output runtime implementation blocked.

**Tech Stack:** Markdown authority docs, JSON durable state, Python 3.12 `unittest`, GitHub Actions, Google Sheets evidence sync.

## Global Constraints

- Decision ID: `OMW-DEC-20260809-PLANNING-BARRACKS-FUNCTIONAL-VALUE-MEASUREMENT-SCENARIOS-DEFINITION-V1`.
- Parent Decision: `OMW-DEC-20260809-PLANNING-BARRACKS-FUNCTIONAL-VALUE-COMBAT-NUMERICS-DEFINITION-REVIEW-V1`.
- `FIXTURE_POLICY = DETERMINISTIC_SAME_INPUT`.
- `FUNCTIONAL_VALUE_COMPARISON = ROLE_SPECIFIC_VECTOR_NO_SINGLE_WEIGHTED_SCORE`.
- `POST_HOC_WEIGHT_TUNING = FORBIDDEN`.
- Runtime-unavailable metrics are `BLOCKED_RUNTIME_OUTPUT`; they are never synthesized as zero.
- No Monte Carlo role-value run, no product/Godot mutation, no final functional-value index, no final parameter vector, no parameter-selection 10k, and no 50k.
- Product archetype IDs use current resources, not historical smoke membership labels.

---

### Task 1: Lock the scenario-definition contract with RED tests

**Files:**
- Create: `tests/python/test_barracks_functional_value_measurement_scenarios.py`
- Create: `.github/workflows/validate-barracks-functional-value-measurement-scenarios.yml`

**Interfaces:**
- Consumes current resource IDs, PR169 authority, and current state.
- Produces assertions for the new authority/status matrix and durable next action.

- [ ] Write tests that verify existing fixture resources and PR169 comparison rules, then require a new measurement-scenario authority and state block.
- [ ] Run `python -m unittest tests.python.test_barracks_functional_value_measurement_scenarios`; expected RED only for missing new authority/state advancement.
- [ ] Record RED workflow run/job and exact failure pattern.

### Task 2: Persist the scenario authority

**Files:**
- Create: `docs/design/APPROVED_OMENWARD_BARRACKS_FUNCTIONAL_VALUE_MEASUREMENT_SCENARIOS_2026-08-09.md`

**Interfaces:**
- Produces scenario IDs `FV-COMMON-01`, `FV-PRIEST-01`, `FV-MAGE-01`, `FV-FLIER-01`, `FV-GIANT-01` and output availability classes.

- [ ] Copy the validated design’s deterministic fixtures and role outputs into the authority document.
- [ ] Mark each role-defining unavailable metric `BLOCKED_RUNTIME_OUTPUT` and current/partial outputs explicitly.
- [ ] State that missing outputs block functional-value selection and that no scalar/weighted score is created.

### Task 3: Advance durable state without authorizing product mutation

**Files:**
- Modify: `docs/operations/ACTIVE_INTEGRATED_CONTRACT_STATE.v1.json`
- Modify: `docs/DECISIONS_PENDING.md`
- Modify: `docs/PROJECT_CANON_DECISION_LEDGER.md`
- Modify: `docs/process/ACTIVE_INTEGRATED_CONTRACT_BINDING_2026-08-06.md`
- Modify: `tools/validate_active_integrated_contract_v4_4.py`
- Modify: `tests/python/test_active_integrated_contract_v4_4.py`
- Modify: `.github/workflows/validate-active-integrated-contract-v4-4.yml`

**Interfaces:**
- Closes only `BARRACKS_FUNCTIONAL_VALUE_MEASUREMENT_SCENARIOS_REQUIRED`.
- Keeps `BARRACKS_ROLE_OUTPUT_RUNTIME_IMPLEMENTATION_REQUIRED`.
- Advances first next action to `BARRACKS_ROLE_OUTPUT_RUNTIME_IMPLEMENTATION_PACKAGE`.

- [ ] Add a durable measurement-scenario block with approved fixture IDs, output-status matrix, null final values, and parent Decision lineage.
- [ ] Remove only the measurement-scenario blocker; keep role-output runtime/tool/local blockers and Entry Gate `BLOCK`.
- [ ] Keep product implementation/Godot mutation/parameter-selection 10k/50k forbidden.
- [ ] Run focused v4.4 and lower-Gate regression suites.

### Task 4: Exact-head review, Sheet sync, and merge

**Files:**
- Google Sheet: `00_프로젝트_허브`, `02_현재_확정결정`, `04_누락_충돌_감사`, `99_변경이력`.

**Interfaces:**
- Produces same Decision ID in GitHub+Sheet and no new `47_병영_Smoke_결과` row.

- [ ] Confirm all exact-head workflows Green and protected product paths = 0.
- [ ] Confirm no seed evidence files changed and 9/10 hashes remain exact.
- [ ] Sync exact-head state to Sheet; leave `47_병영_Smoke_결과` unchanged.
- [ ] Add role-separated adversarial review, mark Ready, squash merge with expected head SHA, read merged main, and sync merge SHA to Sheet.

## Plan self-review

- Every spec requirement maps to one task.
- No product mutation or runtime implementation is included.
- Scenario IDs and status labels match the design spec.
- The only blocker closed is measurement-scenario definition; role-output runtime remains blocking.
