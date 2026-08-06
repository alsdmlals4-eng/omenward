# OMENWARD Building Tier Realignment Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Replace the invalid universal A/B building-branch canon with the user-approved general barracks, special barracks, three-way defense tower, and four linear-upgrade building structure.

**Architecture:** Add one new authority document that owns the current building Tier grammar, preserve the rejected design as historical evidence with explicit supersession, update onboarding checkpoint 6 and central routing, then synchronize the same Decision ID to Google Sheets. Product files and exact numerics remain untouched.

**Tech Stack:** Markdown authority documents, Python `unittest` contract tests, GitHub Contents API, Google Sheets API.

## Global Constraints

- `DECISION_ID = OMW-DEC-20260806-PLANNING-BUILDING-TIER-REALIGNMENT-V1`
- `PARENT_DECISION = OMW-DEC-20260805-PLANNING-FIRST-10-15-MINUTES-FLOW-V1`
- `PARTIAL_APPROVAL = 6_OF_10`
- `PRODUCT_CODE = UNCHANGED`
- `EXACT_NUMERICS = PENDING_SIMULATION`
- `SPECIAL_T1_TOKEN_SOURCE = NONE`
- `SPECIAL_T2_TOKEN_SOURCE = SELECTED_SPECIAL_UNIT`
- `DIRECT_MAIN_WRITE = FORBIDDEN`

---

### Task 1: Add failing canon contract

**Files:**
- Create: `tests/python/test_building_tier_realignment_canon.py`
- Modify: `tests/python/test_building_branch_canon.py`

**Interfaces:**
- Consumes: approved markers from `docs/superpowers/specs/2026-08-06-building-tier-realignment-design.md`
- Produces: a fail-closed contract for authority, supersession, onboarding checkpoint, and product boundaries

- [ ] **Step 1: Add the new failing contract**

Require the new authority and review files, the 7-building roster, general/special barracks production and TokenSource rules, three defense tower branches, four linear buildings, pending numerics, and checkpoint 6 routing.

- [ ] **Step 2: Convert the old branch test into a supersession test**

The old test must no longer require the universal A/B grammar as current canon. It must require the old authority to declare `SUPERSEDED / IMPLEMENTATION_INPUT_FORBIDDEN` and route to the new Decision ID.

- [ ] **Step 3: Verify RED**

Run:

```bash
python -m unittest tests.python.test_building_tier_realignment_canon -v
python -m unittest tests.python.test_building_branch_canon -v
```

Expected: FAIL because the new authority/review and supersession markers are absent.

- [ ] **Step 4: Commit RED**

```bash
git add tests/python/test_building_tier_realignment_canon.py tests/python/test_building_branch_canon.py
git commit -m "test: require building tier realignment canon"
```

### Task 2: Add current authority and adversarial review

**Files:**
- Create: `docs/design/APPROVED_OMENWARD_BUILDING_TIER_REALIGNMENT_2026-08-06.md`
- Create: `docs/reviews/ADVERSARIAL_BUILDING_TIER_REALIGNMENT_REVIEW_2026-08-06.md`
- Modify: `docs/design/APPROVED_OMENWARD_SIX_BUILDING_T2_T3_BRANCHES_AND_COUNTERS_2026-08-05.md`

**Interfaces:**
- Consumes: user-approved building structure
- Produces: current building Tier authority and explicit lifecycle precedence

- [ ] **Step 1: Write the current authority**

Record:

```text
GENERAL_T1 = BASIC_INFANTRY_AUTO_PRODUCTION + BASIC_INFANTRY_TOKEN_SOURCE
GENERAL_T2 = FIVE_GENERAL_SPECIALIZATIONS + SELECTED_UNIT_AUTO_PRODUCTION + SELECTED_UNIT_TOKEN_SOURCE
SPECIAL_T1 = RANDOM_SPECIAL_AUTO_PRODUCTION + NO_TOKEN_SOURCE
SPECIAL_T2 = FIVE_SPECIAL_SPECIALIZATIONS + SELECTED_UNIT_AUTO_PRODUCTION + SELECTED_UNIT_TOKEN_SOURCE
DEFENSE_TOWER_T2 = ARTILLERY / DEFENSE_ENHANCEMENT / SNIPER
VAULT_FARM_COMMAND_MANA = LINEAR_TIER_GROWTH
```

- [ ] **Step 2: Write the adversarial review**

Cover special T1 token leakage, special-unit power/production double advantage, automatic-production versus TokenSource conflation, defense branch overlap, old-canon leakage, Stage 1 seven-building overload, and premature T3/numeric fixation.

- [ ] **Step 3: Replace the old current authority with a superseded evidence notice**

Preserve the old Decision ID and historical branch summary, but mark every previous building branch as implementation-forbidden and route to the new authority.

- [ ] **Step 4: Run the two focused tests**

Expected: the authority-specific requirements pass; central routing requirements may remain RED until Task 3.

- [ ] **Step 5: Commit authority**

```bash
git add docs/design docs/reviews
git commit -m "docs: canonize building tier realignment"
```

### Task 3: Update onboarding checkpoint and central routing

**Files:**
- Modify: `docs/design/APPROVED_OMENWARD_FIRST_10_15_MINUTES_FLOW_2026-08-05.md`
- Modify: `docs/ACTIVE_CONTEXT.md`
- Modify: `docs/DOCUMENTATION_MAP.md`
- Modify: `docs/DOCUMENT_LIFECYCLE_REGISTRY.md`
- Modify: `docs/PROJECT_CANON_DECISION_LEDGER.md`
- Modify: `docs/OMENWARD_GDD_CURRENT_CANON.md`
- Modify: `docs/DECISIONS_PENDING.md`
- Modify: `docs/HANDOFF_CONTEXT.md`
- Modify: `docs/PROJECT_GOOGLE_SHEET_WORKBOOK.md`

**Interfaces:**
- Consumes: current building Tier authority
- Produces: discoverable checkpoint 6 state and exact next gate

- [ ] **Step 1: Update Stage 1 required buildings**

Use:

```text
금고 / 농장 / 일반병 병영 / 방어탑 / 지휘소 / 마력탑
SPECIAL_BARRACKS_STAGE1_REQUIRED = FALSE
```

- [ ] **Step 2: Record checkpoint 6**

Set `PARTIAL_APPROVAL_6_OF_10`. Keep the first Stage 2 T2 candidate and gold policy pending.

- [ ] **Step 3: Route lifecycle precedence**

The new authority supersedes the universal A/B branch grammar, the old barracks weights, and old tower references while preserving unrelated troop and tactical roles.

- [ ] **Step 4: Run focused and documentation tests**

```bash
python -m unittest tests.python.test_building_tier_realignment_canon -v
python -m unittest tests.python.test_building_branch_canon -v
python -m unittest tests.python.test_first_10_15_minutes_flow_canon -v
```

- [ ] **Step 5: Commit routing**

```bash
git add docs tests/python/test_first_10_15_minutes_flow_canon.py
git commit -m "docs: route building realignment checkpoint six"
```

### Task 4: Synchronize Google Sheet

**Files:**
- Update native spreadsheet `1VLwRtXGDtyj0JFt98wdIOtG6Zqc3wtdfCzSF9Fo6lpw`

**Interfaces:**
- Consumes: final exact GitHub PR head SHA
- Produces: same Decision ID and exact-head evidence in planning, decision, GDD, system, audit, and history tabs

- [ ] **Step 1: Read exact append rows and headers**

Bound reads to the existing table ends. Do not overwrite prior decision history.

- [ ] **Step 2: Append decision and audit rows**

Record the new roster, general/special barracks rules, tower branches, linear buildings, superseded old branch grammar, pending numerics, and product boundary.

- [ ] **Step 3: Update hub/checkpoint cells**

Set the current planning checkpoint to `PARTIAL_APPROVAL_6_OF_10` and preserve platform authority rows.

- [ ] **Step 4: Bounded read-back**

Verify the Decision ID, exact PR head, `SPECIAL_T1_TOKEN_SOURCE = NONE`, and next gate.

### Task 5: Final verification and PR metadata

**Files:**
- Update PR #142 title/body

**Interfaces:**
- Consumes: final branch head and Sheet read-back
- Produces: truthful Draft PR state

- [ ] **Step 1: Compare branch to main**

Confirm exact head, ahead/behind counts, mergeability, and changed paths.

- [ ] **Step 2: Inspect comments and review threads**

Do not claim review clearance without connector evidence.

- [ ] **Step 3: Update Draft PR metadata**

Title: `[Planning] First 10–15 minutes flow — checkpoint 6/10`

Body must state that automated Green is not proven when Actions remain billing-blocked.

- [ ] **Step 4: Final fail-closed report**

Report product code unchanged, exact numerics pending, simulation/runtime/human QA not run, and next GrillMe as `FIRST_STAGE2_T2_CANDIDATES_AND_GOLD_RULES`.
