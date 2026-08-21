# [현행] OMENWARD Document Lifecycle Registry

```yaml
updated_at: 2026-08-21
status: CURRENT_DOCUMENT_LIFECYCLE_REGISTRY
planning_contract: PROJECT_TOTAL_PLANNING_IMPLEMENTATION_AND_DELIVERY_INSTRUCTION_v4.7
current_decision_index: docs/CURRENT_CONFIRMED_DECISIONS.md
current_next_gate: REBUILT_NORTH_STAR_ON_USER_IMAGE_REQUEST
visual_generation: USER_REQUEST_ONLY
implementation_authorized: false
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
[현행] docs/OMENWARD_GDD_CURRENT_CANON.md
[현행] docs/PROJECT_CORE.md
[현행] docs/CURRENT_IMPLEMENTATION_STATUS.md
[현행] docs/DECISIONS_PENDING.md
[현행] docs/OMENWARD_ROADMAP.md
[현행] docs/DOCUMENTATION_MAP.md
[현행] docs/DOCUMENT_LIFECYCLE_REGISTRY.md
```

GitHub PR/Issue 상태는 current document로 복제하지 않고 `FRESH_GITHUB_QUERY_REQUIRED`다.

## 3. Current 2026-08-20 Decision owners

```text
[현행] docs/design/APPROVED_OMENWARD_WORLD_ROLE_AND_OMEN_WARD_IDENTITY_2026-08-20.md
[현행] docs/design/APPROVED_OMENWARD_OMEN_CYCLE_MAPRUN_WORLD_2026-08-20.md
[현행] docs/design/APPROVED_OMENWARD_PRESSURE_LANGUAGE_AND_OMEN_SIGNATURES_2026-08-20.md
[현행] docs/design/APPROVED_OMENWARD_MOBILIZATION_REGISTRY_AND_TRIPLE_OMEN_WHEELS_2026-08-20.md
[현행] docs/design/APPROVED_OMENWARD_FIRST5_FTUE_MASTERY_LADDER_2026-08-20.md
[현행] docs/design/APPROVED_OMENWARD_RUN_COMMAND_SCREEN_FOCUS_MODES_2026-08-20.md
[현행] docs/design/APPROVED_OMENWARD_VEIL_CONVERGENCE_FRONT_AND_CORE_STORY_2026-08-20.md
[현행] docs/design/APPROVED_OMENWARD_20_STAGE_CONTENT_AND_BOSS_ARC_2026-08-20.md
[현행] docs/design/APPROVED_OMENWARD_NORMALIZED_BALANCE_BUDGET_2026-08-20.md
[현행] docs/design/APPROVED_OMENWARD_TEXT_UX_AND_STATE_TRANSITION_2026-08-20.md
[현행] docs/design/APPROVED_OMENWARD_VISUAL_STYLE_AND_COMPONENT_CONTRACT_2026-08-20.md
[현행] docs/design/APPROVED_OMENWARD_BATTLEFIELD_SCALE_AND_COMBAT_READABILITY_2026-08-20.md
[현행] docs/design/APPROVED_OMENWARD_3X3_ROULETTE_COMPONENT_SPEC_2026-08-20.md
[현행] docs/design/APPROVED_OMENWARD_TOKEN_COMPONENT_SPEC_2026-08-20.md
[현행] docs/design/APPROVED_OMENWARD_LOWER_CONTROL_DECK_SPEC_2026-08-20.md
[현행] docs/design/APPROVED_OMENWARD_ROULETTE_DDD_FEEDBACK_SPEC_2026-08-20.md
[현행] docs/design/APPROVED_OMENWARD_TOPDOWN_BATTLEFIELD_LAYOUT_SPEC_2026-08-20.md
[현행] docs/design/APPROVED_OMENWARD_TOPDOWN_UNIT_SILHOUETTE_RULES_2026-08-20.md
```

```text
CURRENT_APPROVED_REPLAN_DECISIONS = 18
CURRENT_NEXT = REBUILT_NORTH_STAR_ON_USER_IMAGE_REQUEST
VISUAL_GENERATION = USER_REQUEST_ONLY
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
```

Exact SHA/run은 위 evidence owner에서 보존한다. Current status/GDD/router에는 과거 exact run을 current proof처럼 복제하지 않는다.

## 6. Historical Vertical Slice / Evidence Pilot

```text
[증거/호환] docs/design/APPROVED_VERTICAL_SLICE_SYSTEM_CONTRACT_2026-07-27.md
[증거/호환] docs/reviews/ADVERSARIAL_VERTICAL_SLICE_REVIEW_2026-07-27.md
[증거/호환] docs/benchmarks/OMENWARD_ROULETTE_AGENCY_EVIDENCE_PACK_2026-07-29.md
[증거/호환] docs/reviews/PHASE_B_FINAL_PLANNING_REVIEW_2026-08-11.md
[증거/호환] docs/reviews/PHASE_C_C0_LOCAL_HIGODOT_CLOSURE_2026-08-11.md
```

특히 `[증거/호환] docs/design/APPROVED_VERTICAL_SLICE_SYSTEM_CONTRACT_2026-07-27.md`는 July 구현/validation lineage를 증명하지만 2026-08-20 v4.7 Decision index를 덮어쓰는 current spec가 아니다.

## 7. Durable historical product lineage

아래 항목은 후속 정본으로 대체되거나 더 높은 owner에 흡수됐지만, 승인 계보·회귀 테스트·위험 근거를 보존하기 위해 남긴다. **현재 구현 입력으로 재활성화하지 않는다.**

### Building branches — historical 3_OF_10

```text
[증거/호환] OMW-DEC-20260805-PLANNING-SIX-BUILDING-T2-T3-BRANCHES-AND-COUNTERS-V1
3_OF_10 = HISTORICAL_PLANNING_LINEAGE
LEGACY_UNIVERSAL_BUILDING_BRANCHES = SUPERSEDED_BY_BUILDING_TIER_REALIGNMENT
SUPERSEDED_BY_BUILDING_TIER_REALIGNMENT
CURRENT_SUCCESSOR = OMW-DEC-20260806-PLANNING-BUILDING-TIER-REALIGNMENT-V1
IMPLEMENTATION_INPUT_FORBIDDEN
```

### Troop roles — historical 4_OF_10

```text
[증거/호환] OMW-DEC-20260805-PLANNING-TROOP-ROLES-SYNERGIES-AND-COUNTERS-V1
4_OF_10 = HISTORICAL_PLANNING_LINEAGE
[증거] data/units/*.tres
LEGACY_PROTOTYPE_UNIT_DATA
IMPLEMENTATION_INPUT_FORBIDDEN
```

`data/units/*.tres`의 과거 prototype 값은 historical runtime/bootstrap evidence다. current 병종 역할·Tier·수치 authority로 사용하지 않는다.

### Tactical skills / 마력 — historical 5_OF_10

```text
[증거/호환] OMW-DEC-20260805-PLANNING-TACTICAL-SKILLS-AND-MANA-V1
5_OF_10 = HISTORICAL_PLANNING_LINEAGE
LEGACY_MANA_TOWER_BRANCHES = SUPERSEDED
LEGACY_TERM_MASOK = SUPERSEDED
CURRENT_TACTICAL_RESOURCE = 마력
IMPLEMENTATION_INPUT_FORBIDDEN
```

### Stage-end merchant — historical 6_OF_10

```text
[증거/호환] OMW-DEC-20260805-PLANNING-STAGE-END-MERCHANT-V1
6_OF_10 = HISTORICAL_PLANNING_LINEAGE
LEGACY_ALWAYS_AVAILABLE_SHOP = SUPERSEDED
LEGACY_INFINITE_MERCHANT_STOCK = SUPERSEDED
LEGACY_DIRECT_CORE_REWARD_SALES = SUPERSEDED
IMPLEMENTATION_INPUT_FORBIDDEN
```

## 8. Legacy master / replaced planning

```text
[대체됨] docs/OMENWARD_GAME_DESIGN.md
```

Legacy master의 과거 C1/C2/C3 및 v0.26 정보는 compatibility/history로만 읽고 current v4.7 기획 의미는 `OMENWARD_GDD_CURRENT_CANON.md`와 current owner를 따른다.

## 9. Historical work-items

```text
PR175 = CLOSED_UNMERGED_HISTORICAL
PR177 = CLOSED_UNMERGED_REFERENCE_HISTORY
PR197 = CLOSED_UNMERGED_SUPERSEDED_BY_198
CURRENT_OPEN_PRS_AND_ISSUES = FRESH_GITHUB_QUERY_REQUIRED
```

Unmerged branch나 old Handoff를 current product truth로 승격하지 않는다.

## 10. Human workspace

```text
NOTION = CURRENT_HUMAN_FACING_CANON
REPOSITORY = CURRENT_STRUCTURED_RUNTIME_CANON
GOOGLE_SHEET = COMPATIBILITY_HISTORY_ONLY
```

Google Sheet는 current human authority가 아니다. Notion/GitHub 의미 변경은 양쪽 destination readback을 요구한다.

## 11. Current transition

```text
TOPDOWN_BATTLEFIELD_LAYOUT
→ TOPDOWN_UNIT_SILHOUETTE
→ REBUILT_NORTH_STAR_ON_USER_IMAGE_REQUEST
→ COMPONENT_SHEET
→ FINAL_PLANNING_ADVERSARIAL_REVIEW
→ IMPLEMENTATION_AUTHORITY_REQUIRED
```
