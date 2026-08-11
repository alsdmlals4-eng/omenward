# Quality Guardrails + Elite/Boss Cadence Canonization Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Canonicalize the approved six quality guardrails and replace separate Danger stages with final-wave Elite escalation on every Stage while preserving Boss stages 5/10/15/20.

**Architecture:** Add two focused planning Decision owners and route current gameplay canon to them. Preserve the 2026-08-04 pressure matrix as superseded lineage, update current routers, and add fail-closed semantic/scope validation without touching product/Godot paths. Sync the same Decision IDs to the connected Google Sheet after GitHub exact-head validation.

**Tech Stack:** Markdown canon, Python unittest, GitHub Actions YAML, Google Sheets API connector.

## Global Constraints

- `PHASE_A_GPT_CHAT_PLANNING` remains active.
- `PHASE_C_BLOCKED` remains true until literal user `기획 완료` and Phase B pass.
- No mutation under `data/`, `scripts/`, `scenes/`, `assets/`, `addons/`, or `project.godot`.
- `DANGER_STAGE_TYPE = REMOVED`.
- `ELITE_ESCALATION = EVERY_STAGE_FINAL_WAVE`.
- `BOSS_STAGES = 5 / 10 / 15 / 20`.
- Boss stages also retain the final-wave Elite requirement.
- Elite/Boss exact count, HP, damage, and spawn timing remain unselected.
- Same Decision IDs must be reflected in GitHub canon and Google Sheet.

---

### Task 1: Add failing semantic contract

**Files:**
- Create: `tests/python/test_quality_guardrails_elite_boss_cadence.py`
- Modify: `.github/workflows/validate-canon-freshness-v4-5.yml`

**Interfaces:**
- Consumes: current GDD, MapRun core, lifecycle, documentation map.
- Produces: exact markers required for the two new Decision owners and current routers.

- [ ] **Step 1: Write the failing test**

Assert both Decision IDs exist and require these markers:

```text
DANGER_STAGE_TYPE = REMOVED
ELITE_ESCALATION = EVERY_STAGE_FINAL_WAVE
BOSS_STAGES = 5 / 10 / 15 / 20
BOSS_STAGE_FINAL_WAVE_ELITE_REQUIRED = TRUE
RNG_CAN_REMOVE_ALL_VALID_RESPONSES = FORBIDDEN
SOFT_SYNERGY_DISCOVERY = PREFERRED
POST_STAGE_CAUSAL_REVIEW = FORECAST -> KEY_EVENTS -> PLAYER_RESPONSE_OUTCOME
HORIZONTAL_CHALLENGE_EXPANSION = ALLOWED
ROULETTE_IDENTITY = PLAYER_CONSTRUCTED_PROBABILITY_ENGINE
```

Also assert the old 2026-08-04 pressure matrix is not a current implementation owner.

- [ ] **Step 2: Add the focused test to v4.5 compile/run steps**

Run command to encode in workflow:

```bash
python -m unittest tests.python.test_quality_guardrails_elite_boss_cadence -v
```

- [ ] **Step 3: Verify RED on the PR exact head**

Expected: focused contract fails because new canonical owners/current markers are not yet present.

### Task 2: Add canonical Decision owners

**Files:**
- Create: `docs/design/APPROVED_OMENWARD_QUALITY_GUARDRAILS_2026-08-11.md`
- Create: `docs/design/APPROVED_OMENWARD_ELITE_WAVE_AND_BOSS_CADENCE_2026-08-11.md`

**Interfaces:**
- Produces Decision IDs:
  - `OMW-DEC-20260811-PLANNING-QUALITY-GUARDRAILS-V1`
  - `OMW-DEC-20260811-PLANNING-ELITE-WAVE-BOSS-CADENCE-V1`

- [ ] **Step 1: Write Quality Guardrails owner**

Include the six approved contracts: RNG fairness, seed/run variation, soft-synergy build identity, causal review, horizontal difficulty/challenge/seeded run, non-gambling roulette identity.

- [ ] **Step 2: Write Elite/Boss cadence owner**

Include:

```text
MAPRUN_STAGE_COUNT = 20
BASELINE_WAVE_BEATS = 3
DANGER_STAGE_TYPE = REMOVED
ELITE_ESCALATION = EVERY_STAGE_FINAL_WAVE
ELITE_PRESENCE_REQUIRED = TRUE
BOSS_STAGES = 5 / 10 / 15 / 20
BOSS_STAGE_BOSS_PRESENCE_REQUIRED = TRUE
BOSS_STAGE_FINAL_WAVE_ELITE_REQUIRED = TRUE
```

Explicitly defer exact Elite/Boss numerics and preserve prior 4/9/14/19 authored ideas only as optional normal-stage variations.

### Task 3: Re-route current gameplay canon

**Files:**
- Modify: `docs/OMENWARD_GDD_CURRENT_CANON.md`
- Modify: `docs/design/APPROVED_MAPRUN_STAGE_WAVE_AND_MIDPOINT_CORE_V1.md`
- Modify: `docs/design/APPROVED_OMENWARD_STAGE_WAVE_DANGER_BOSS_PRESSURE_MATRIX_2026-08-04.md`
- Modify: `docs/DOCUMENT_LIFECYCLE_REGISTRY.md`
- Modify: `docs/DOCUMENTATION_MAP.md`
- Modify: `docs/ACTIVE_CONTEXT.md`
- Modify: `docs/DECISIONS_PENDING.md`

**Interfaces:**
- Consumes: the two new Decision owners.
- Produces: one unambiguous current routing path.

- [ ] **Step 1: Replace current cadence summary in GDD and MapRun core**

Remove current authority for `Danger 4/9/14/19`; add final-wave Elite and Boss 5/10/15/20 markers.

- [ ] **Step 2: Supersede the old pressure matrix**

Mark it historical/superseded by `OMW-DEC-20260811-PLANNING-ELITE-WAVE-BOSS-CADENCE-V1`; do not delete its detailed authored stage ideas.

- [ ] **Step 3: Update lifecycle and documentation routing**

List the new two docs as current owners and the old pressure matrix as superseded lineage.

- [ ] **Step 4: Update current context/pending state**

Keep `WHOLE_PROJECT_CONTENT_DECISION_GROUPS_OPEN = 0`, user `기획 완료` not received, Phase B not run, Phase C blocked.

### Task 4: Extend fail-closed v4.5 scope

**Files:**
- Modify: `tests/python/test_canon_freshness_v45_scope.py`
- Modify: `tools/validate_canon_freshness_v45_scope.py`
- Modify: `.github/workflows/validate-canon-freshness-v4-5.yml`

**Interfaces:**
- Produces scope mode: `QUALITY_GUARDRAILS_ELITE_BOSS_CADENCE`.

- [ ] **Step 1: Add exact allowed/required file surface to test**

Reject partial surface, product paths, and unrelated files.

- [ ] **Step 2: Add matching validator mode**

Use the exact same file set as required anchors.

- [ ] **Step 3: Run focused tests**

```bash
python -m unittest tests.python.test_quality_guardrails_elite_boss_cadence -v
python -m unittest tests.python.test_canon_freshness_v45_scope -v
python -m unittest tests.python.test_content_closure_benchmark_first -v
```

Expected: all PASS.

### Task 5: Exact-head review and Sheet sync

**Files:**
- Google Sheet tabs: `00_프로젝트_허브`, `01_작업순서`, `02_현재_확정결정`, `04_누락_충돌_감사`, `50_메인콘텐츠`, `60_UX_UI_접근성`, `99_변경이력`.

- [ ] **Step 1: Open/update PR and verify exact-head workflows**

Require the focused v4.5 contract and all triggered checks to be Green before merge.

- [ ] **Step 2: Adversarial review**

Check that no current file still routes `Danger Stage = 4/9/14/19` as authority, while historical evidence may retain it with superseded status.

- [ ] **Step 3: Sync the same Decision IDs to Sheet**

Append history-safe rows instead of rewriting old historical rows. Current-facing rows must state:

```text
DANGER_STAGE_TYPE=REMOVED
ELITE_ESCALATION=EVERY_STAGE_FINAL_WAVE
BOSS_STAGES=5/10/15/20
BOSS_STAGE_FINAL_WAVE_ELITE_REQUIRED=TRUE
QUALITY_GUARDRAILS=APPROVED
```

- [ ] **Step 4: Final reread**

Re-read changed GitHub current owners and all changed Sheet ranges. Report any remaining conflict; otherwise record `SHEET_FINAL_REREAD_PASS`.
