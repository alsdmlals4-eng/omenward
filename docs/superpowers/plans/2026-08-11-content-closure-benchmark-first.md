# OMENWARD Content Closure and Benchmark-First Governance Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Canonicalize the user's approved nine whole-project content decisions, classify OMENWARD's genre from current benchmark evidence, establish benchmark/industry research as a mandatory pre-work gate, and correct the false Sheet claim that PR185 merged.

**Architecture:** Keep product semantics in one approved design Decision and operating policy in one approved process Decision. Current routers receive only compact pointers/status; Sheet uses corrective append rows rather than rewriting historical evidence. A fail-closed v4.5 planning scope and focused regression test protect the exact non-product surface.

**Tech Stack:** Markdown canon, Python `unittest`, GitHub Actions, existing `tools/validate_canon_freshness_v45_scope.py`, Google Sheets mirror.

## Global Constraints

- Base current main at work entry: `315c66eea9614c284b9c11c4d522141065dfa4b0`; Base open PRs: `0`.
- OMENWARD current main at work entry: `652ced07d70fac33a4d3415eacaaec8bd2523e78`.
- Product Decision: `OMW-DEC-20260811-PLANNING-WHOLE-PROJECT-CONTENT-CLOSURE-V1`.
- Process Decision: `OMW-DEC-20260811-OPS-BENCHMARK-INDUSTRY-RESEARCH-FIRST-V1`.
- `USER_EXPLICIT_PLANNING_COMPLETE_DECLARATION = NOT_RECEIVED`.
- `PHASE_B_FINAL_PLANNING_REVIEW = NOT_RUN`.
- `PHASE_C_BLOCKED`.
- No `data/`, `scripts/`, `scenes/`, `assets/`, `addons/`, or `project.godot` mutation.
- PR185 is `SUPERSEDED_UNMERGED`; its failed CI is historical evidence and must not be relabeled Green.
- Every future non-trivial work item must run fresh benchmarking/industry research before design/canon/implementation changes.
- Benchmark findings are classified `ADOPT / ADAPT / AVOID / TEST / IGNORE`; competitor behavior never overrides OMENWARD canon automatically.

## Execution variance — adversarial Thin Adapter refinement

The initial task list below proposed direct edits to GDD/Lifecycle. During adversarial review this was rejected as unnecessary duplication and a repeat risk of prior large-canon rewrite regressions. The approved product semantics are instead owned by one new design Decision, the operating rule by one new process Decision, and only current entry/status routers are updated.

Final GitHub surface is **11 files**:

```text
.github/workflows/validate-canon-freshness-v4-5.yml
AGENTS.md
docs/ACTIVE_CONTEXT.md
docs/DECISIONS_PENDING.md
docs/design/APPROVED_OMENWARD_WHOLE_PROJECT_CONTENT_CLOSURE_2026-08-11.md
docs/process/APPROVED_OMENWARD_BENCHMARK_INDUSTRY_RESEARCH_FIRST_2026-08-11.md
docs/superpowers/plans/2026-08-11-content-closure-benchmark-first.md
tests/python/test_canon_freshness_v45_scope.py
tests/python/test_content_closure_benchmark_first.py
tests/python/test_phase_a_readiness_dependency_classification.py
tools/validate_canon_freshness_v45_scope.py
```

```text
DIRECT_GDD_DUPLICATION = NOT_USED
DIRECT_LIFECYCLE_DUPLICATION = NOT_USED
PR184_READINESS_TEST = TRANSITION_AWARE_AFTER_USER_APPROVAL
CURRENT_RESPONSIBILITY_SOURCE_LINKS = PRESERVED_BY_REGRESSION_TEST
PRODUCT_GODOT_PATHS = NONE
```

The older readiness review remains historical evidence that T3/Hero/Meta were open **before** this user approval; current routers and the new Decision own the post-approval state.

---

### Task 1: TDD contract for approved content closure and benchmark-first gate

**Files:**
- Create: `tests/python/test_content_closure_benchmark_first.py`
- Modify: `tests/python/test_canon_freshness_v45_scope.py`
- Modify: `tools/validate_canon_freshness_v45_scope.py`
- Modify: `.github/workflows/validate-canon-freshness-v4-5.yml`

**Interfaces:**
- Consumes: current v4.5 phase markers and fail-closed scope validator.
- Produces: exact planning-only scope mode `CONTENT_CLOSURE_BENCHMARK_FIRST` and a workflow-executed regression contract.

- [x] **Step 1: Write failing content tests**

Assert the approved Decision documents do not exist yet and require these exact product literals:

```text
BUILDING_T3_GRAMMAR = SINGLE_CAPSTONE_DEEPENS_SELECTED_T2_IDENTITY
BUILDING_T3_REBRANCH = FORBIDDEN
DEFENSE_T2_DISPLAY_NAMES = 포격탑 / 요새탑 / 저격탑
HERO_STRATEGIC_ROLE = CONTEXTUAL_AMPLIFIER
HERO_SELECTION_PER_MAPRUN = 1
HERO_STAGE_BY_STAGE_FREE_SWAP = FORBIDDEN
LEGENDARY_GRAMMAR = RARE_CONSTRAINED_SIDEGRADE
LEGENDARY_PLAIN_RAW_STAT_SUPERIOR_TIER = FORBIDDEN
META_HUB_PROGRESSION = HORIZONTAL_CONTEXTUAL
PERMANENT_PURE_COMBAT_STAT_ACCUMULATION = FORBIDDEN
MANDATORY_GRIND_CURRENCY = FORBIDDEN
```

Also require:

```text
PRIMARY_GENRE = ROGUELITE_STRATEGY_AUTO_BATTLER
MECHANICAL_SUBGENRE = ROULETTE_PROBABILITY_BUILDER
BENCHMARK_AND_INDUSTRY_RESEARCH_REQUIRED_BEFORE_WORK = TRUE
BENCHMARK_DISPOSITION = ADOPT / ADAPT / AVOID / TEST / IGNORE
WHOLE_PROJECT_CONTENT_DECISIONS = CLOSED_PENDING_USER_PLANNING_COMPLETE_DECLARATION
PHASE_C_BLOCKED
```

- [x] **Step 2: Run/observe server RED**

Observed semantic RED: v4.5 run `31449860775`; existing routing/scope/readiness Green, new content-closure/benchmark-first contract Red before canonical Decision documents/current markers landed.

- [x] **Step 3: Add exact fail-closed surface mode**

Allow only the final 11-file Thin Adapter surface; reject missing anchors, unrelated files, historical v4.4 authority mutation, and protected product paths.

- [x] **Step 4: Route the focused test through v4.5 workflow**

Compile and execute `tests.python.test_content_closure_benchmark_first` in `validate-canon-freshness-v4-5.yml` and include every intended changed path in the workflow trigger.

- [x] **Step 5: Verify scope Green/content RED separation**

Verified during the RED lineage. A later adversarial regression test also reproduced missing current responsibility sources as a focused Red before their restoration.

### Task 2: Canonicalize the approved nine product decisions and genre classification

**Initial proposed files:**
- Create: `docs/design/APPROVED_OMENWARD_WHOLE_PROJECT_CONTENT_CLOSURE_2026-08-11.md`
- Initially considered: direct `docs/OMENWARD_GDD_CURRENT_CANON.md` / `docs/DOCUMENT_LIFECYCLE_REGISTRY.md` edits

**Final Thin Adapter execution:** product semantics are owned by the new Decision; direct GDD/Lifecycle duplication was intentionally not performed.

**Interfaces:**
- Consumes: user's explicit approval, current building-tier/Hero/Legendary/Meta owners, benchmark evidence.
- Produces: canonical product Decision `OMW-DEC-20260811-PLANNING-WHOLE-PROJECT-CONTENT-CLOSURE-V1`.

- [x] **Step 1: Record benchmark-derived genre classification**

Use:

```text
PRIMARY_GENRE = ROGUELITE_STRATEGY_AUTO_BATTLER
MECHANICAL_SUBGENRE = ROULETTE_PROBABILITY_BUILDER
SUPPORTING_DESCRIPTORS = TACTICAL_LANE_DEPLOYMENT / ENGINE_BUILDING / RESOURCE_MANAGEMENT / MANUAL_TACTICAL_SKILL_TIMING
MARKETING_SHORT = 룰렛을 설계해 군대를 만드는 로그라이트 전략 오토배틀러
```

Benchmark mapping:
- Mechabellum: `ADAPT` — formation/counter/readability, strategy over APM.
- The Last Flame: `ADAPT` — run-based auto-battler build/decision framing.
- Spin Hero: `ADAPT` — reel manipulation as build engine; do not copy deck structure.
- Luck be a Landlord: `ADAPT` — player-built slot probability composition; avoid slot-as-end-in-itself framing.
- Backpack Battles: `ADAPT` — pre-combat build/arrangement agency.
- CloverPit: `TEST/AVOID` — probability manipulation is relevant, but gambling/horror identity and unrestricted snowball are not OMENWARD's positioning.

- [x] **Step 2: Record all nine approved decisions without inventing final numerics**

Preserve Archer T3 later owner `CROSSBOW_ARCHER / RAPID_FIRE_ARCHER`; leave role-specific exact capstone numerics to later runtime/balance evidence.

- [x] **Step 3: Preserve held-owner boundary**

Prior Hero/Legendary and Meta/Hub detailed held documents remain historical/reference lineage. The new closure Decision is current high-level product authority; old exact kits or exact meta power values are not silently reactivated.

- [x] **Step 4: Route current status through Thin Adapter owners**

`AGENTS.md`, `ACTIVE_CONTEXT.md`, and `DECISIONS_PENDING.md` point to the new product Decision. No direct large GDD/Lifecycle rewrite was required.

### Task 3: Canonicalize benchmark-first operating policy

**Files:**
- Create: `docs/process/APPROVED_OMENWARD_BENCHMARK_INDUSTRY_RESEARCH_FIRST_2026-08-11.md`
- Modify: `AGENTS.md`
- Modify: `docs/ACTIVE_CONTEXT.md`
- Modify: `docs/DECISIONS_PENDING.md`

**Interfaces:**
- Consumes: Base `analyzing-and-refining-game-concepts` benchmark workflow and user's standing project instruction.
- Produces: project process Decision `OMW-DEC-20260811-OPS-BENCHMARK-INDUSTRY-RESEARCH-FIRST-V1`.

- [x] **Step 1: Define mandatory pre-work sequence**

```text
FRESH_BASE_PROJECT_SHEET_READ
→ TARGETED_BENCHMARK_AND_INDUSTRY_RESEARCH
→ SOURCE_DATE_AND_RELEVANCE_RECORD
→ ADOPT_ADAPT_AVOID_TEST_IGNORE
→ PROJECT_CANON_CONFLICT_CHECK
→ DESIGN_CANON_IMPLEMENTATION_WORK
```

- [x] **Step 2: Define bounded exceptions**

Trivial same-work-item readback/status synchronization may reuse the benchmark packet from the same work item. Urgent correctness/security remediation may use a minimal targeted industry/primary-source verification first; it does not waive fresh authority reads or evidence recording in the same work item.

- [x] **Step 3: Update entry router**

`AGENTS.md` requires the benchmark gate before non-trivial work and points to the process Decision rather than duplicating all detailed procedure.

- [x] **Step 4: Close Phase-A semantic inventory without opening Phase B/C**

Current state:

```text
WHOLE_PROJECT_CONTENT_DECISION_GROUPS_OPEN = 0
WHOLE_PROJECT_CONTENT_DECISIONS = CLOSED_PENDING_USER_PLANNING_COMPLETE_DECLARATION
USER_EXPLICIT_PLANNING_COMPLETE_DECLARATION = NOT_RECEIVED
PHASE_B_FINAL_PLANNING_REVIEW = NOT_RUN
PHASE_C_BLOCKED
```

Final FV/numerics, Issue176 implementation completeness, and platform/release deferred work remain in their prior categories and do not reopen semantic content planning.

### Task 4: Correct Sheet authority drift and sync both Decisions

**Sheet surfaces:**
- `00_프로젝트_허브`
- `01_작업순서`
- `02_현재_확정결정`
- `04_누락_충돌_감사`
- `42_병종_Tier_등급`
- `43_건물_Tier_효과`
- `50_메인콘텐츠`
- `99_변경이력`

**Interfaces:**
- Consumes: final exact GitHub PR head and both Decision IDs.
- Produces: history-safe corrective Sheet state with bounded reread evidence.

- [x] **Step 1: Correct PR185 false merge claim**

Corrective evidence records:

```text
PR185 = CLOSED_UNMERGED_SUPERSEDED
PR185_HEAD = b49fee351a2d9fa3d2f471f0e826728fbacc575a
PR185_CANON_V45 = FAILURE
PR185_ACTIVE_V44 = FAILURE
SHEET_PRIOR_PR185_MERGED_CLAIM = CORRECTED
```

The erroneous historical row was preserved rather than deleted.

- [x] **Step 2: Add approved product Decision row**

The nine approved semantics, genre classification, no-final-numerics boundary, and Phase C block are present as `PROPOSED_SHEET_CHANGE` while PR186 is Draft.

- [x] **Step 3: Add benchmark-first process Decision row**

The mandatory pre-work research, disposition taxonomy, current-source preference, and no-competitor-copy authority are present as `PROPOSED_SHEET_CHANGE`.

- [x] **Step 4: Add current system notes**

`42`: Hero one-per-run commitment and troop T3 role preservation.
`43`: single-capstone T3 grammar and `포격탑 / 요새탑 / 저격탑`.
`50`: contextual-amplifier Hero, constrained-sidegrade Legendary, horizontal/contextual Meta/Hub.

- [x] **Step 5: Bounded reread every changed range**

The proposed Sheet ranges were read back and matched. Final `MERGED_CANON` promotion remains blocked until the GitHub merge/readback gate.

### Task 5: Adversarial verification and merge

**Files:** final 11-file GitHub surface above; Sheet evidence from Task 4.

- [ ] **Step 1: Exact-head CI**

Require every triggered workflow Green, including v4.5, active v4.4 compatibility, Base adoption, GDD Sheet adoption, Project Core, and Omenward Core when triggered.

- [x] **Step 2: Adversarial diff review — pre-final-head findings**

Validated findings already refined:
- stale PR184 “T3 must remain open” test was transitioned rather than weakening/removing the test;
- current responsibility source links removed during simplification received a dedicated regression test and were restored;
- no old Hero exact kits or Meta exact power values were reactivated;
- no role-specific T3 final numerics or final FV/product numerics were selected;
- no competitor behavior was elevated to automatic authority;
- no product/Godot path is in the PR surface;
- Phase B/C remain closed.

- [ ] **Step 3: Fresh race check**

Re-read Base main/open PRs, OMENWARD main/open PRs, exact PR head, and review threads.

- [ ] **Step 4: Expected-head squash merge only if all gates pass**

Use exact PR head protection.

- [ ] **Step 5: Merged-main readback and Sheet promotion**

Promote proposed Sheet rows to `MERGED_CANON` only after GitHub merge and merged-main verification.

- [x] **Step 6: Preserve the user gate**

```text
WHOLE_PROJECT_CONTENT_DECISIONS_CLOSED
USER_EXPLICIT_PLANNING_COMPLETE_DECLARATION_REQUIRED
PHASE_B_NOT_RUN
PHASE_C_BLOCKED
```

Do not treat the user's approval of these nine decisions as the separate literal `기획 완료` declaration.
