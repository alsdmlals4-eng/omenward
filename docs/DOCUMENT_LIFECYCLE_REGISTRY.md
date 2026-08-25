# [현행] OMENWARD Document Lifecycle Registry

```yaml
updated_at: 2026-08-25
status: CURRENT_DOCUMENT_LIFECYCLE_REGISTRY
planning_contract: PROJECT_TOTAL_PLANNING_IMPLEMENTATION_AND_DELIVERY_INSTRUCTION_v4.8
current_decision_index: docs/CURRENT_CONFIRMED_DECISIONS.md
current_next_gate: USER_EXPLICIT_REACTIVATION
visual_generation: USER_REQUEST_ONLY
implementation_authorized: true
implementation_execution: NOT_RESUMED
```

## 1. Lifecycle labels

- `[현행]`: 현재 질문의 책임 원본 또는 current router.
- `[증거/호환]`: 과거 승인·실행·Migration·compatibility를 보존하지만 current product authority가 아님.
- `[대체됨]`: 후속 owner가 의미를 승계했으며 신규 구현 입력으로 사용 금지.
- `[보류]`: future reconciliation 전 구현 입력 금지.
- `[폐기]`: current design에서 채택하지 않음.
- `[증거]`: historical runtime/data artifact; current implementation input 아님.

## 2. Current routers

```text
[현행] README.md
[현행] AGENTS.md
[현행] docs/CURRENT_CONFIRMED_DECISIONS.md
[현행] docs/ACTIVE_CONTEXT.md
[현행] docs/HANDOFF_CONTEXT.md
[현행] docs/OMENWARD_GDD_CURRENT_CANON.md
[현행] docs/PROJECT_CORE.md
[현행] docs/CURRENT_IMPLEMENTATION_STATUS.md
[현행] docs/DECISIONS_PENDING.md
[현행] docs/OMENWARD_ROADMAP.md
[현행] docs/DOCUMENTATION_MAP.md
[현행] docs/DOCUMENT_LIFECYCLE_REGISTRY.md
[현행] docs/PROJECT_CANON_DECISION_LEDGER.md
```

## 3. Current 2026-08-25 authority

```text
CURRENT_APPROVED_REPLAN_DECISIONS = 20
CURRENT_VISUAL_DECISION = OMW-PLAN-20260825-FRONT-STATE-MINIMAP-SD-FANTASY-01
APPROVED_VISUAL = OM-IMG-023
NORTH_STAR_V2_1 = REFERENCE_ONLY_AFTER_2026_08_25
BATTLEFIELD_PRESENTATION = THREE_SIMULTANEOUS_FRONT_STATE_VIEWS
PER_FRONT_MINIMAP = REQUIRED
VISUAL_STYLE = FANTASY_MAGIC_SD_TACTICAL_PIXEL_ILLUSTRATION
IMPLEMENTATION_AUTHORITY = SCOPED_APPROVED_RETAINED
PROJECT_ACTIVITY = PAUSED_QUEUED
CURRENT_NEXT = USER_EXPLICIT_REACTIVATION
IMAGE_GENERATION = USER_REQUEST_ONLY
```

Current owners:

```text
[현행] docs/superpowers/specs/2026-08-25-front-state-minimap-sd-fantasy-design.md
[현행] docs/images/planning/canonical/OMENWARD_APPROVED_FRONT_STATE_VISUAL_2026-08-25.md
[현행] docs/handoffs/2026-08-25-front-state-visual-approved-closeout.md
```

Retained 2026-08-20/24 design lineage:

```text
[증거/호환] docs/design/APPROVED_OMENWARD_VISUAL_STYLE_AND_COMPONENT_CONTRACT_2026-08-20.md
[증거/호환] docs/design/APPROVED_OMENWARD_BATTLEFIELD_SCALE_AND_COMBAT_READABILITY_2026-08-20.md
[증거/호환] docs/design/APPROVED_OMENWARD_3X3_ROULETTE_COMPONENT_SPEC_2026-08-20.md
[증거/호환] docs/design/APPROVED_OMENWARD_TOKEN_COMPONENT_SPEC_2026-08-20.md
[증거/호환] docs/design/APPROVED_OMENWARD_LOWER_CONTROL_DECK_SPEC_2026-08-20.md
[증거/호환] docs/design/APPROVED_OMENWARD_ROULETTE_DDD_FEEDBACK_SPEC_2026-08-20.md
[증거/호환] docs/design/APPROVED_OMENWARD_TOPDOWN_BATTLEFIELD_LAYOUT_SPEC_2026-08-20.md
[증거/호환] docs/design/APPROVED_OMENWARD_TOPDOWN_UNIT_SILHOUETTE_RULES_2026-08-20.md
[증거/호환] docs/design/APPROVED_OMENWARD_NORTH_STAR_V2_1_AUDIT_AND_CORRECTION_BRIEF_2026-08-24.md
[증거/호환] docs/reviews/FINAL_PLANNING_ADVERSARIAL_REVIEW_AND_DRIFT_CHECK_2026-08-24.md
```

Historical compatibility markers:

```text
HISTORICAL_20260824_CURRENT_APPROVED_REPLAN_DECISIONS = 19
HISTORICAL_20260824_NORTH_STAR_V2_1 = APPROVED_REFERENCE_WITH_BOUNDARY
FINAL_PLANNING_ADVERSARIAL_REVIEW = PASS_5_OF_5
GITHUB_NOTION_DRIFT_CHECK = PASS
HISTORICAL_20260824_CURRENT_NEXT = IMPLEMENTATION_AUTHORITY_REQUIRED
HISTORICAL_20260824_IMPLEMENTATION_AUTHORITY = NONE
```

## 4. Current machine envelopes

```text
[현행] docs/analysis/balance/current_normalized_balance_budget.v1.json
[현행] docs/analysis/ui/current_text_ux_state_contract.v1.json
[현행] docs/analysis/ui/current_3x3_roulette_component.v1.json
[현행] docs/analysis/ui/current_token_component.v1.json
[현행] docs/analysis/ui/current_lower_control_deck.v1.json
[현행] docs/analysis/ui/current_roulette_ddd_feedback.v1.json
[현행] docs/analysis/visual/current_battlefield_scale_readability.v1.json
[현행] docs/analysis/visual/current_topdown_unit_silhouette_rules.v1.json
```

## 5. Historical exact technical proof

```text
[증거/호환] docs/C1_ROULETTE_RECOVERY_REPORT_2026-07-22.md
[증거/호환] docs/C2_BATTLE_OBJECTIVE_AUDIT_2026-07-22.md
[증거/호환] docs/C3_CORE_UX_AUDIT_2026-07-23.md
[증거/호환] docs/archive/2026-07/pre-v2-canon/CURRENT_IMPLEMENTATION_STATUS_PRE_V2.md
[증거/호환] docs/design/APPROVED_VERTICAL_SLICE_SYSTEM_CONTRACT_2026-07-27.md
```

Exact SHA/run은 evidence owner에서 보존한다. Current router에는 과거 exact run을 current proof처럼 복제하지 않는다.

## 6. Historical process provenance

```text
[증거/호환] docs/reviews/ADVERSARIAL_VERTICAL_SLICE_REVIEW_2026-07-27.md
[증거/호환] docs/benchmarks/OMENWARD_ROULETTE_AGENCY_EVIDENCE_PACK_2026-07-29.md
[증거/호환] docs/process/PROJECT_TOTAL_PLANNING_IMPLEMENTATION_AND_DELIVERY_INSTRUCTION_v4.5_r2.md
[증거/호환] docs/process/ACTIVE_INTEGRATED_CONTRACT_BINDING_2026-08-11.md
[증거/호환] docs/operations/ACTIVE_INTEGRATED_CONTRACT_STATE.v2.json
[증거/호환] docs/reviews/PHASE_B_FINAL_PLANNING_REVIEW_2026-08-11.md
[증거/호환] docs/reviews/PHASE_C_C0_LOCAL_HIGODOT_CLOSURE_2026-08-11.md
HISTORICAL_V4_4_BINDING
PHASE_B_FINAL_PLANNING_REVIEW = HISTORICAL_PASS
PHASE_C_C0_OVERALL = HISTORICAL_PASS
LEGACY_DANGER_CADENCE_AUTHORITY = NONE
```

## 7. Durable historical product lineage

```text
3_OF_10 = HISTORICAL_PLANNING_LINEAGE
4_OF_10 = HISTORICAL_PLANNING_LINEAGE
5_OF_10 = HISTORICAL_PLANNING_LINEAGE
6_OF_10 = HISTORICAL_PLANNING_LINEAGE
LEGACY_UNIVERSAL_BUILDING_BRANCHES = SUPERSEDED_BY_BUILDING_TIER_REALIGNMENT
LEGACY_MANA_TOWER_BRANCHES = SUPERSEDED
LEGACY_TERM_MASOK = SUPERSEDED
CURRENT_TACTICAL_RESOURCE = 마력
LEGACY_ALWAYS_AVAILABLE_SHOP = SUPERSEDED
IMPLEMENTATION_INPUT_FORBIDDEN
```

## 8. Human workspace / live-state rule

```text
NOTION = CURRENT_HUMAN_FACING_CANON
REPOSITORY = CURRENT_STRUCTURED_RUNTIME_CANON
GOOGLE_SHEET = COMPATIBILITY_HISTORY_ONLY
CURRENT_OPEN_PRS_AND_ISSUES = FRESH_GITHUB_QUERY_REQUIRED
```

Google Sheet는 current human authority가 아니다.

## 9. Current transition

```text
CURRENT_VISUAL_DECISION = OMW-PLAN-20260825-FRONT-STATE-MINIMAP-SD-FANTASY-01
→ APPROVED_VISUAL = OM-IMG-023
→ VISUAL_CLOSEOUT = COMPLETE
→ CURRENT_NEXT = USER_EXPLICIT_REACTIVATION
```

Implementation authority is retained but execution is not resumed. Image generation remains `USER_REQUEST_ONLY`.