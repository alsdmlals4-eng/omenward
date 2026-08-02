# OMENWARD Grill Me 승인 묶음 병합 계획

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 정치 역할·보조 허브·병합 주기 승인을 GitHub·Google Sheet 정본에 동기화하고 PR #119를 안전하게 main에 병합한다.

**Architecture:** 제품 코드와 기획 정본을 분리한다. 분야별 승인 문서가 의미를 소유하고 Decision Ledger·Documentation Map·Context가 라우팅하며 Google Sheet는 같은 Decision ID와 commit을 표시한다. 병합은 exact HEAD 검증과 적대적 preflight 뒤 squash 방식으로 수행한다.

**Tech Stack:** GitHub documents and PR metadata, Google Sheets 25-tab workbook, GitHub Actions validation.

## Global Constraints

- Product code, scenes, resources, data, assets, addons, tests, validators, and `project.godot` remain unchanged.
- `APPROVED_PLAN != IMPLEMENTED != VALIDATED`.
- Exact costs, node counts, hero counts, rarity taxonomy, stats, and deployment cap remain pending.
- Base Profile can complete all content.
- No random paid recruitment, infinite ranks, global combat multipliers, hidden reel-odds manipulation, or whole-run production multipliers.
- PR merge requires fresh exact-HEAD CI, Sheet read-back, review-thread check, path audit, and zero open P0/P1 blockers.

---

### Task 1: Restore current responsibility surfaces

**Files:**
- Create: `docs/design/APPROVED_OMENWARD_POLITICAL_ROLE_2026-08-02.md`
- Create: `docs/design/APPROVED_OMENWARD_AUXILIARY_HUB_PROGRESSION_2026-08-02.md`
- Create: `docs/design/APPROVED_OMENWARD_VISUAL_SCREEN_BOARD_V2_TEXT_SPEC_2026-08-01.md`
- Create: `docs/operations/GRILL_ME_MERGE_CADENCE_AND_PREFLIGHT_2026-08-02.md`
- Create: `docs/superpowers/specs/2026-08-02-omenward-political-auxiliary-merge-governance-design.md`

- [x] **Step 1: Record user-approved political authority and limits.**
- [x] **Step 2: Record Tavern, Barracks, Research, permanent node, and Hero+ guardrails.**
- [x] **Step 3: Restore Screen Board V2 as a current local authority and extend main-hub UX.**
- [x] **Step 4: Record the 10-approved-Grill-Me merge cadence and mandatory preflight.**
- [x] **Step 5: Self-review for placeholders, contradictions, scope, and ambiguity.**

### Task 2: Update canonical routing

**Files:**
- Modify: `docs/PROJECT_CANON_DECISION_LEDGER.md`
- Modify: `docs/ACTIVE_CONTEXT.md`
- Modify: `docs/HANDOFF_CONTEXT.md`
- Modify: `docs/DOCUMENTATION_MAP.md`
- Modify: `docs/PROJECT_GOOGLE_SHEET_WORKBOOK.md`
- Modify: `docs/design/APPROVED_OMENWARD_META_PROGRESSION_ROLE_2026-08-02.md`

- [ ] **Step 1: Add all three new Decision IDs and supersession/ownership boundaries.**
- [ ] **Step 2: Route current political, auxiliary hub, Screen Board, and merge protocol sources.**
- [ ] **Step 3: Set the post-merge next Gate to Veil-species purpose.**
- [ ] **Step 4: Preserve validator compatibility tokens and historical evidence boundaries.**
- [ ] **Step 5: Verify every current authority path exists on the working branch.**

### Task 3: Synchronize Google Sheet

**Ranges:**
- Update: `00_프로젝트_허브!E2:L2`
- Append: `01_작업순서`
- Append: `02_현재_확정결정`
- Append: `04_누락_충돌_감사`
- Update/append: `05_GDD_요약`, `11_세계관`, `13_주요인물`, `14_조연_세력_관계`, `41_성장_경제`, `60_UX_UI_접근성`
- Append: `99_변경이력`

- [ ] **Step 1: Re-read exact target ranges and confirm empty rows.**
- [ ] **Step 2: Write political Decision and world/organization relations.**
- [ ] **Step 3: Write auxiliary hub economy, UX, and audit findings.**
- [ ] **Step 4: Write merge cadence and approval counter state.**
- [ ] **Step 5: Perform bounded read-back and correct any schema drift.**

### Task 4: Run adversarial merge preflight

**Files:**
- Create: `docs/reviews/OMENWARD_PR119_PREMERGE_ADVERSARIAL_REVIEW_2026-08-02.md`

- [ ] **Step 1: Compare main to exact PR HEAD and list every changed path.**
- [ ] **Step 2: Confirm product paths remain unchanged.**
- [ ] **Step 3: Check PR state, mergeability, comments, reviews, and unresolved threads.**
- [ ] **Step 4: Verify all current authority files exist and no missing local authority remains.**
- [ ] **Step 5: Classify findings as resolved, accepted risk, test required, user decision required, or merge blocker.**
- [ ] **Step 6: Run all required workflows at the final exact HEAD and require success.**
- [ ] **Step 7: Re-read Sheet exact HEAD and Decision rows.**

### Task 5: Merge and close synchronization

- [ ] **Step 1: Update PR body with final Decisions, changed paths, Sheet ranges, findings, and exact HEAD.**
- [ ] **Step 2: Mark PR #119 ready for review after preflight passes.**
- [ ] **Step 3: Squash merge using the verified expected head SHA.**
- [ ] **Step 4: Verify `merged=true`, merge commit, and main file availability.**
- [ ] **Step 5: Replace Sheet PR-head tracking with merged main SHA and `SYNCED_TO_MAIN / MERGE_VERIFIED`.**
- [ ] **Step 6: Read back Sheet and reset future Grill Me counter to `0/10`.**
- [ ] **Step 7: Start future work on a new branch and Draft PR; do not reuse PR #119.**
