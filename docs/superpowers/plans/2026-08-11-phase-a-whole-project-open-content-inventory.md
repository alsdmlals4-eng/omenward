# Phase A Whole-Project Open-Content Inventory Plan

> **Execution authority:** approved continuous Phase A planning only. No product/Godot implementation and no new gameplay choice is auto-approved by this plan.

**Goal:** Distinguish the already-completed onboarding 10/10 batch from whole-project Phase A completion, identify only genuine current product-decision groups still open, and prevent HELD Hero/Legendary/Meta history from being consumed as implementation input.

**Fresh baseline:**

```text
Base main = 315c66eea9614c284b9c11c4d522141065dfa4b0
Base open PRs = 0
OMENWARD main = 652ced07d70fac33a4d3415eacaaec8bd2523e78
OMENWARD open PRs = 175 runtime Draft / 177 reference-only Draft
activation Decision = OMW-DEC-20260811-OPS-ACTIVATE-INTEGRATED-CONTRACT-V4-5-R2-V1
work phase = PHASE_A_GPT_CHAT_PLANNING
PHASE_C = BLOCKED
```

## Source-derived current boundary

- `MAIN_CANONICAL_APPROVED_10_OF_10` remains valid for the onboarding planning batch and must remain as a compatibility/current-onboarding marker.
- Core guardrails define content order through Hero·Legendary family readjustment and Meta·Hub readjustment after the core systems/onboarding work.
- Hero family documents are currently `HELD_FOR_CURRENT_CONTENT_RECONCILIATION`, `implementation_authority: NONE`.
- Meta/Hub documents are currently `HELD_FOR_CORE_CONTENT_REVALIDATION`, `implementation_authority: NONE`.
- Current building-tier owner explicitly leaves building T3 identities/effects and defense branch final naming to later decisions.
- Troop T3 lineage document approves role/grade ability structure while identifying names/numerics as PoC hypotheses; later Archer correction is authoritative for Archer T3 (`CROSSBOW_ARCHER / RAPID_FIRE_ARCHER`).
- Final FV/product numerics and platform/release work remain outside the semantic open-content list per the merged readiness classification.

## Required additive state model

```text
ONBOARDING_PLANNING_STATUS = MAIN_CANONICAL_APPROVED_10_OF_10
ONBOARDING_10_OF_10_SCOPE = ONBOARDING_BATCH_ONLY
WHOLE_PROJECT_PHASE_A_STATUS = OPEN_CONTENT_REMAINING
WHOLE_PROJECT_PLANNING_COMPLETE = FALSE
USER_EXPLICIT_PLANNING_COMPLETE_DECLARATION = NOT_RECEIVED
PHASE_B_FINAL_PLANNING_REVIEW = NOT_RUN
PHASE_C_BLOCKED
```

Genuine open product-decision groups for the next Grill Me phase:

```text
OPEN_GROUP_1 = BUILDING_T3_DETAILS_AND_FINAL_BRANCH_NAMING
OPEN_GROUP_2 = HERO_LEGENDARY_FAMILY_REVALIDATION
OPEN_GROUP_3 = META_HUB_REVALIDATION
```

Protected non-blocker/deferred groups:

```text
ISSUE176_7_GAPS = IMPLEMENTATION_COMPLETENESS
FINAL_FV_AND_PRODUCT_NUMERICS = POST_RUNTIME_EVIDENCE_TUNING
PLATFORM_SAVE_EXPORT_STORE = RELEASE_PHASE_DEFERRED_FOR_PR175
TROOP_T3_EXACT_NUMERICS = POST_RUNTIME_OR_LATER_BALANCE_TUNING
LEVEL_COORDINATES_AND_NON_SEMANTIC_TIMING = IMPLEMENTATION_DETAIL_DEFERRED
```

## Task 1 — TDD fail-closed inventory contract

Files:
- create `tests/python/test_phase_a_whole_project_open_content_inventory.py`
- modify `tests/python/test_canon_freshness_v45_scope.py`
- modify `tools/validate_canon_freshness_v45_scope.py`
- modify `.github/workflows/validate-canon-freshness-v4-5.yml`

Steps:
- [ ] Add RED assertions for additive onboarding-vs-whole-project state markers.
- [ ] Assert HELD Hero/Meta docs cannot be presented as current implementation input.
- [ ] Assert exactly three genuine current decision groups above.
- [ ] Assert final FV/platform/release/Issue176 remain in their previously classified categories.
- [ ] Add exact fail-closed PR surface mode and ensure partial/extra surfaces fail.
- [ ] Make v4.5 workflow path-trigger, compile, and run the new contract.
- [ ] Observe server RED before current-router changes.

## Task 2 — Current-router and review propagation

Files:
- modify `AGENTS.md`
- modify `docs/ACTIVE_CONTEXT.md`
- modify `docs/CURRENT_IMPLEMENTATION_STATUS.md`
- modify `docs/DECISIONS_PENDING.md`
- modify `docs/OMENWARD_GDD_CURRENT_CANON.md`
- modify `docs/PROJECT_CORE.md`
- modify `docs/PROJECT_GOOGLE_SHEET_WORKBOOK.md`
- create `docs/reviews/PHASE_A_WHOLE_PROJECT_OPEN_CONTENT_INVENTORY_2026-08-11.md`

Steps:
- [ ] Keep `MAIN_CANONICAL_APPROVED_10_OF_10` intact as onboarding compatibility/current-batch marker.
- [ ] Add explicit whole-project-open fields so nobody can infer whole planning completion from 10/10.
- [ ] Inventory building T3, Hero/Legendary, Meta/Hub as the only new product-decision groups currently identified.
- [ ] Preserve troop T3 role structure and Archer correction without treating PoC names/numerics as final values.
- [ ] Preserve final-FV/platform/release dependency classifications from PR184.
- [ ] Keep `USER_EXPLICIT_PLANNING_COMPLETE_DECLARATION_REQUIRED` and `PHASE_C_BLOCKED` everywhere.

## Task 3 — Sheet reconciliation and closure

Sheet current/append surfaces:
- current hub and current Decision
- append work-order row 70
- append audit row 639
- append history row 185
- add/append current status note in `42_병종_Tier_등급` without overwriting historical role rows
- add/append current status note in `50_메인콘텐츠` marking detailed Hero rows as HELD historical/reference, not current implementation input

Steps:
- [ ] Write proposed state with same activation Decision ID.
- [ ] Bounded reread every changed range.
- [ ] Exact-head CI all Green, review threads 0, no protected product paths.
- [ ] Adversarial review: reject accidental Hero/Meta reactivation, invented building T3 choices, final numeric selection, or Phase C opening.
- [ ] Fresh Base/project race check.
- [ ] Expected-head squash merge if gates pass.
- [ ] Merged-main readback and push CI.
- [ ] Promote Sheet to MERGED and reread.
- [ ] Then stop at the genuine user Grill Me gate with a <=10-decision recommended batch. Do not auto-approve new product choices.
