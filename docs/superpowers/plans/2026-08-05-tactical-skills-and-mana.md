# OMENWARD Tactical Skills and Mana Canon Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 승인된 5/10 전술스킬·마력 설계를 현행 정본으로 만들고, 구형 `마석` 및 마력탑 분기 계약을 대체하며, GitHub와 Google Sheet를 같은 Decision ID로 동기화한다.

**Architecture:** 문서 계약 테스트가 새 책임 원본·용어·4·3·3 전술 목록·MapRun 초기화·단일 마력탑·중앙 라우팅·수명주기 상태를 검증한다. 제품 코드와 수치 데이터는 수정하지 않으며, 문서 RED를 확인한 뒤 최소 정본과 적대적 검토를 추가하고 중앙 권위와 Sheet를 갱신한다.

**Tech Stack:** Markdown canon, Python 3.12 `unittest`, GitHub Actions, Google Sheets authority mirror.

## Global Constraints

- Decision ID: `OMW-DEC-20260805-PLANNING-TACTICAL-SKILLS-AND-MANA-V1`.
- Planning counter: `5_OF_10`.
- 현행 용어는 `마력`; `마석`은 구형 용어 설명과 비현행 역사 문서에서만 허용한다.
- 마력탑 활성 인스턴스 최대 1개, 분기 없는 `T1 → T2 → T3`.
- 전술스킬 기준선은 `T1 4 / T2 3 / T3 3`, 총 10종.
- 연구 비용은 골드+시간, 시전 비용은 마력.
- 연구·해금·보유 마력·마력탑 Tier는 MapRun 동안 유지하고 새 MapRun에서 초기화한다.
- Stage 전 편성·자동 시전·연구 마력 비용·T3 자동 승리·전선 자유 재배치는 금지한다.
- 정확 수급량·상한·비용·쿨다운·범위·지속시간은 `PENDING_SIMULATION`.
- 제품 코드·Scene·Resource·게임 데이터·아트 자산은 변경하지 않는다.
- 모든 GitHub 쓰기는 `gpt/omenward-tactical-skills-mana-spec-20260805`에서만 수행한다.

---

### Task 1: Add the RED documentation contract

**Files:**
- Create: `tests/python/test_tactical_skill_mana_canon.py`
- Modify: `.github/workflows/validate-project-core-docs.yml`

**Interfaces:**
- Consumes: approved Spec `docs/superpowers/specs/2026-08-05-tactical-skills-and-mana-design.md`.
- Produces: executable contract for authority files, terminology, tower rules, 4·3·3 roster, reset rules, central routing, lifecycle, and implementation boundary.

- [ ] **Step 1: Write the failing test**

Create a `unittest` module that requires:

```python
DECISION_ID = "OMW-DEC-20260805-PLANNING-TACTICAL-SKILLS-AND-MANA-V1"
TACTICAL_SKILLS = (
    "속박진", "수호장", "집중 명령", "충격파",
    "폭풍 억제", "파쇄 명령", "봉쇄 결계",
    "결전의 깃발", "성역", "시간 왜곡",
)
```

Assertions must verify:

```text
MANA_TOWER_MAX_ACTIVE_INSTANCES = 1
BRANCHING = FORBIDDEN
TOTAL_TACTICAL_SKILLS = 10
T1 = 4 / T2 = 3 / T3 = 3
연구 비용 = 골드 + 연구 시간
시전 비용 = 마력
STAGE_LOADOUT = NONE
AUTO_CAST = FORBIDDEN
RESET_SCOPE = NEW_MAPRUN
EXACT_NUMERICS = PENDING_SIMULATION
PRODUCT_CODE = UNCHANGED
```

The test must also require the new canon and adversarial review files, `5_OF_10` routing in central files, and lifecycle replacement of `유량 마력탑 / 저장 마력탑`.

- [ ] **Step 2: Register the test in CI**

Add the new file to workflow path filters, `py_compile`, and the unittest command.

- [ ] **Step 3: Run CI and verify RED**

Expected: only the new tactical/mana contract fails because canon, review, 5/10 routing, terminology migration, and lifecycle replacement do not exist yet. Existing contracts remain Green.

- [ ] **Step 4: Commit the RED state**

Commit message:

```text
test: add failing tactical skill and mana canon contract
```

---

### Task 2: Create the tactical/mana authority and adversarial review

**Files:**
- Create: `docs/design/APPROVED_OMENWARD_TACTICAL_SKILLS_AND_MANA_2026-08-05.md`
- Create: `docs/reviews/ADVERSARIAL_TACTICAL_SKILLS_MANA_AND_RESEARCH_REVIEW_2026-08-05.md`

**Interfaces:**
- Consumes: approved Spec and Decisions 1–4.
- Produces: current 5/10 authority and audit `OMW-AUD-444~467`.

- [ ] **Step 1: Write the minimal canon**

The canon must define:

```text
마력탑 T1 → T2 → T3
one active tower
one concurrent research
research = gold + time
cast = mana
unlocked skills persist for current MapRun
new MapRun resets tower/research/unlocks/mana
```

Include the exact 10 tactical skills, targets, pressure coverage, limitations, UI requirements, invalid-target no-spend behavior, and `PENDING_SIMULATION` boundaries.

- [ ] **Step 2: Write the adversarial review**

Audit at least:

```text
resource hoarding dominance
research snowball
single-tower destruction lockout
rebuild exploit
research cancellation refund exploit
auto-cast regression
T3 panic-button dominance
hard-counter unlock dependency
flying/siege coverage gaps
route information cheating
mana overflow and infinite storage
cooldown-only balancing failure
UI overload with ten unlocked skills
legacy masok terminology leak
legacy branched mana-tower authority leak
```

Record required fixes and preserve `PRODUCT_CODE = UNCHANGED`.

- [ ] **Step 3: Run the tactical contract**

Expected: authority-specific assertions pass; central routing and terminology migration may still fail.

- [ ] **Step 4: Commit**

Commit message:

```text
docs: define tactical skill and mana canon
```

---

### Task 3: Migrate current authority and lifecycle

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
- Modify: `docs/design/APPROVED_OMENWARD_COMBAT_HUD_ROULETTE_RESOURCE_MERCHANT_AND_BUILDING_ROSTER_2026-08-04.md`
- Modify: `docs/design/APPROVED_OMENWARD_SIX_BUILDING_T2_T3_BRANCHES_AND_COUNTERS_2026-08-05.md`

**Interfaces:**
- Consumes: Task 2 authority.
- Produces: one current terminology and 5/10 authority graph.

- [ ] **Step 1: Route 5/10 centrally**

Every central file must include the Decision ID and `5_OF_10`; 4/10 remains in completed history.

- [ ] **Step 2: Replace current `마석` terminology**

Current authority must use `마력`. The new canon may retain one explicit migration statement `구형 용어: 마석`.

- [ ] **Step 3: Replace the mana-tower branch contract**

In the building canon, mark `유량 마력탑 → 맥동 도관` and `저장 마력탑 → 징조 저장고` as `[대체됨]` and route to the 5/10 linear tower authority. Update the global six-building rule to state that the mana tower is the sole linear-growth exception.

- [ ] **Step 4: Update lifecycle rules**

Register the new canon, Spec, plan, and review as `[현행]`; register the old mana-tower branch section and `마석` terminology as `[대체됨]`; forbid them as new implementation input.

- [ ] **Step 5: Run all documentation workflows**

Expected: Project Core, GDD Sheet, Omenward Core, and Base v9 workflows are Green after preserving Legacy C1/C2/C3 evidence markers.

- [ ] **Step 6: Commit**

Commit message:

```text
docs: route tactical mana canon through current authority
```

---

### Task 4: Sync Google Sheet and complete REFACTOR

**Files:**
- Modify: Google Sheet `1VLwRtXGDtyj0JFt98wdIOtG6Zqc3wtdfCzSF9Fo6lpw`
- Modify: `docs/superpowers/plans/2026-08-05-tactical-skills-and-mana.md`

**Interfaces:**
- Consumes: exact PR HEAD and Green CI evidence.
- Produces: mirrored Decision 5/10, evidence, audit, and next Gate.

- [ ] **Step 1: Append Sheet records**

Write new rows rather than overwriting 4/10 history. Record:

```text
Decision 5/10
10 skills = 4·3·3
mana tower max 1 and linear tiers
research gold+time / cast mana
MapRun reset
OMW-AUD-444~467
RED and Green run IDs
exact PR HEAD
next Gate = Stage-end merchant 6/10
```

- [ ] **Step 2: Perform bounded read-back**

Confirm Decision ID, exact HEAD, counter, terminology, skill names, lifecycle replacement, audit range, and next Gate.

- [ ] **Step 3: Refactor the plan into an evidence record**

Replace unchecked steps with actual RED/GREEN/REFACTOR evidence without changing product scope.

- [ ] **Step 4: Re-run exact-head CI**

Because REFACTOR changes HEAD, run all four workflows again and update Sheet to the final candidate SHA.

- [ ] **Step 5: Commit**

Commit message:

```text
docs: finalize tactical mana evidence and Sheet sync
```

---

### Task 5: Fresh preflight and protected merge

**Files:**
- Modify: PR #140 body and status.
- Modify: current Sheet status cells after merge.

**Interfaces:**
- Consumes: final exact HEAD with Green CI and bounded Sheet read-back.
- Produces: merged main canon and post-merge Sheet evidence.

- [ ] **Step 1: Verify preflight**

Require:

```text
behind main = 0
product paths changed = 0
reviews addressed
unresolved threads = 0
OPEN_P0 = 0
OPEN_P1 = 0
MERGE_BLOCKER = 0
unfinished TODO/TBD = 0
Sheet exact-head read-back = PASS
```

- [ ] **Step 2: Update PR body**

Document the 4·3·3 roster, research/cast economy, terminology migration, single tower exception, RED→GREEN→REFACTOR evidence, lifecycle changes, Sheet ranges, and product boundaries.

- [ ] **Step 3: Mark ready and squash merge with expected HEAD**

Use exact SHA protection. Do not create a post-merge documentation PR because `current_main` is dynamically resolved.

- [ ] **Step 4: Update Sheet post-merge state**

Record merged main SHA and change only the current 5/10 status ranges.

- [ ] **Step 5: Perform final bounded read-back**

Expected: `MAIN_CANONICAL / READBACK_PASS / COUNTER_5_OF_10` and next Decision `OMW-DEC-20260805-PLANNING-STAGE-END-MERCHANT-V1`.
