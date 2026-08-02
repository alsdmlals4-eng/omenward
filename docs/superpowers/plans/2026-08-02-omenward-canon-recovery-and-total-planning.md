# OMENWARD Canon Recovery and Total Planning Restart Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Recover OMENWARD planning authority from current `main`, preserve approved PR #116 decisions without importing obsolete Base v9.3 assumptions, synchronize GitHub and Google Sheets with one Decision ID, and restart total planning from validated conflicts and gaps.

**Architecture:** Treat current `main@9a39f6869f95ec4e6e1f6b96a6a2f896a22c5739` and released Base v9.4 as the operating baseline. Preserve PR #116 as historical evidence, promote only explicitly approved planning decisions into concise current authority documents, and keep product code, scenes, resources, runtime data, and assets unchanged. Separate automatic canon repairs from user decisions and research/test-dependent values.

**Tech Stack:** Markdown planning canon, GitHub branches/PRs/Actions, Google Sheets planning workspace, Godot 4.7/GDScript repository evidence.

## Global Constraints

- Decision ID: `OMW-DEC-20260802-CANON-RECOVERY-V1`.
- Work Mode: `TOTAL_PLANNING` beginning with `REVIEW`.
- Primary platform: PC. Mobile remains a future consideration and is not an implementation target.
- Base authority: released Base v9.4 operating contract; Base unreleased main changes are observations only.
- Product code, scenes, resources, runtime data, assets, and Godot behavior are out of scope.
- Detailed numerical values use `RECOMMENDED_DEFAULT`, `TEST_VALUE`, or `NOT_APPROVED`; they are not product canon until evidence and approval exist.
- Important planning conflicts and decisions are asked through Grill Me one decision at a time.
- GitHub is the canonical source; Google Sheets is a synchronized user-facing planning workspace.
- PR #116 is historical evidence and must not be merged as the recovery unit.
- Do not claim runtime, human, accessibility, performance, simulation, or current-product validation unless executed.

---

### Task 1: Establish recovery authority and findings ledger

**Files:**
- Create: `docs/audits/OMENWARD_CANON_RECOVERY_AND_TOTAL_PLANNING_RESTART_2026-08-02.md`
- Create: `docs/PROJECT_CANON_DECISION_LEDGER.md`

**Interfaces:**
- Consumes: `main@9a39f686...`, Base v9.4 adoption records, PR #116 approved decisions, Sheet 25-tab audit, actual Legacy Godot code.
- Produces: the single recovery decision, explicit protected strengths, auto-fix findings, Grill Me queue, research/test queue, and replacement relationship for PR #116.

- [ ] Record baseline, permissions, protected paths, actual implementation boundary, and unverified evidence.
- [ ] Record approved decisions inherited from PR #116 without changing their meaning.
- [ ] Record P0/P1 conflicts: Base version drift, PR scope drift, stale Sheet head, stale validators, authority duplication, and Sheet schema defects.
- [ ] Classify every finding as `AUTO_FIX_ELIGIBLE`, `USER_DECISION_REQUIRED`, or `RESEARCH_OR_TEST_REQUIRED`.
- [ ] Define the first Grill Me decision using the highest-impact unresolved player-experience conflict.
- [ ] Commit the recovery authority and ledger.

### Task 2: Restore cold-start context and responsibility routing

**Files:**
- Modify: `docs/ACTIVE_CONTEXT.md`
- Modify: `docs/HANDOFF_CONTEXT.md`
- Modify: `docs/DOCUMENTATION_MAP.md`
- Modify: `docs/PROJECT_GOOGLE_SHEET_WORKBOOK.md`

**Interfaces:**
- Consumes: Task 1 decision ledger.
- Produces: one current entry route for project direction, implementation status, next planning gate, Sheet role, and prohibited work.

- [ ] Replace Base v9.1/v9.3 migration language with current Base v9.4 operating authority.
- [ ] Route approved planning to `PROJECT_CANON_DECISION_LEDGER.md` and actual implementation to `CURRENT_IMPLEMENTATION_STATUS.md`.
- [ ] State that latest planning is approved but not implemented and that product implementation remains blocked.
- [ ] Point the next work to total planning and the first validated Grill Me decision, not to simulator or Codex execution.
- [ ] Preserve PC-primary and mobile-future boundaries.
- [ ] Commit cold-start routing changes.

### Task 3: Synchronize Google Sheets with the recovery decision

**Sheets:**
- Update: `00_프로젝트_허브`
- Update: `01_작업순서`
- Append: `02_현재_확정결정`
- Append: `04_누락_충돌_감사`
- Repair schema/data alignment: `03_근거_라이브러리`, `40_핵심시스템_메인콘텐츠`, `60_UX_UI_접근성`, `90_본제작_출시_사업`
- Append: `99_변경이력`

**Interfaces:**
- Consumes: exact GitHub recovery commit and paths.
- Produces: same Decision ID, exact authority commit, separate main/PR head fields, current Base v9.4 state, and a visible Grill Me planning queue.

- [ ] Update project hub to Base v9.4 and current recovery branch/head semantics.
- [ ] Mark PR #116 as historical/superseded, not current synchronized head.
- [ ] Add the recovery Decision ID and authority path.
- [ ] Record stale validator and Sheet schema findings without claiming they are fixed until read-back passes.
- [ ] Repair only verified column-shift/schema errors; do not invent planning content.
- [ ] Re-read every written range and record `SYNCED` only on exact match.

### Task 4: Open replacement Draft PR and supersede PR #116

**GitHub:**
- Create Draft PR from `gpt/omenward-canon-recovery-20260802` to `main`.
- Update or close PR #116 after the replacement PR exists.

**Interfaces:**
- Consumes: Tasks 1-3 exact HEAD and Sheet read-back.
- Produces: a small reviewable recovery PR and an explicit historical relationship to PR #116.

- [ ] Create Draft PR with product-code exclusion, Decision ID, changed files, Sheet ranges, evidence statuses, and rollback.
- [ ] Mark PR #116 `SUPERSEDED_BY_OMW-DEC-20260802-CANON-RECOVERY-V1` and close it without merging.
- [ ] Verify exact HEAD, changed-file inventory, mergeability, checks, reviews, and unresolved threads.
- [ ] Keep the replacement PR Draft while Grill Me decisions remain open.

### Task 5: Begin adversarial total planning and Grill Me

**Files:**
- Update: `docs/audits/OMENWARD_CANON_RECOVERY_AND_TOTAL_PLANNING_RESTART_2026-08-02.md`
- Update after each answer: `docs/PROJECT_CANON_DECISION_LEDGER.md`, relevant design canon, context/handoff, Sheet decision/change rows.

**Interfaces:**
- Consumes: validated planning conflict queue.
- Produces: one user decision at a time, immediately synchronized before the next decision.

- [ ] Attack and validate conflicts across player promise, core loop, economy, onboarding, content production, UX, world/character function, save/retry, accessibility, and vertical-slice scope.
- [ ] Reject taste-only or evidence-free criticism.
- [ ] Auto-fix safe planning omissions and routing errors only.
- [ ] Ask the first highest-impact Grill Me decision with options, tradeoffs, recommendation, and affected canon.
- [ ] After the user answer, update GitHub and Sheet with the same Decision ID and re-read before asking the next question.

## Verification

- GitHub baseline and branch are exact.
- Changed files contain no product paths.
- Base v9.4 is current; v9.3 migration is historical.
- PR #116 is not merged.
- Decision IDs, authority paths, commit SHAs, and Sheet rows match on read-back.
- No numerical proposal is labeled approved without evidence and user approval.
- No Codex or product implementation handoff exists while planning decisions remain open.
- Runtime, simulation, human QA, accessibility, performance, and mobile validation remain explicitly `NOT_RUN` or `OUT_OF_SCOPE`.

## Rollback

- Close the replacement Draft PR without merge.
- Delete or abandon the recovery branch.
- Restore Sheet ranges from the pre-write export/revision if read-back fails.
- PR #116 remains historical evidence and can be reopened only by explicit user decision; it is never merged as the recovery unit.
