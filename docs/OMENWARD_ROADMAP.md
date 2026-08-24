# [현행] OMENWARD Roadmap

```yaml
updated_at: 2026-08-24
status: CURRENT_ROADMAP
planning_contract: PROJECT_TOTAL_PLANNING_IMPLEMENTATION_AND_DELIVERY_INSTRUCTION_v4.8
current_decision_index: docs/CURRENT_CONFIRMED_DECISIONS.md
current_next_gate: FINAL_PLANNING_ADVERSARIAL_REVIEW_AND_DRIFT_CHECK
visual_generation: USER_REQUEST_ONLY
implementation_authorized: false
```

## 1. Product north star

> 건물로 룰렛을 만들고, 룰렛으로 전선을 지휘한다.

```text
징조 관측
→ 확률 설계
→ 3×3 징조륜 / 제한 조작
→ 병력 획득
→ 비가역 전선 커밋
→ 자동전투 / 전술
→ 인과 Review
```

## 2. Planning closure status

```text
CURRENT_APPROVED_REPLAN_DECISIONS = 19
WORLD / MAPRUN / PRESSURE = COMPLETE
FIRST5_FTUE / RUN_COMMAND = COMPLETE
WORLD_CONFLICT / 20_STAGE_BOSS_ARC = COMPLETE
NORMALIZED_BALANCE_BUDGET = COMPLETE_AS_ENVELOPE
TEXT_UX_STATE = COMPLETE
VISUAL_STYLE_COMPONENTS = COMPLETE
BATTLEFIELD_SCALE = COMPLETE
ROULETTE_3X3 = COMPLETE
TOKEN_COMPONENT = COMPLETE
LOWER_CONTROL_DECK = COMPLETE
ROULETTE_DDD = COMPLETE
TOPDOWN_BATTLEFIELD_LAYOUT = COMPLETE
TOPDOWN_UNIT_SILHOUETTE = COMPLETE
NORTH_STAR_V2_1_AREA_AUDIT = COMPLETE
LOWER_DECK_AND_ROULETTE_CORRECTION_BRIEF = COMPLETE
COMPONENT_BREAKDOWN = COMPLETE_FOR_FINAL_PLANNING_INPUT
```

## 3. Current visual route

```text
TOPDOWN_BATTLEFIELD_LAYOUT
→ TOPDOWN_UNIT_SILHOUETTE
→ NORTH_STAR_V2_1_AREA_AUDIT
→ LOWER_DECK_AND_ROULETTE_CORRECTION_BRIEF
→ COMPONENT_BREAKDOWN
→ FINAL_PLANNING_ADVERSARIAL_REVIEW_AND_DRIFT_CHECK
```

- North Star v2.1 = `APPROVED_REFERENCE_WITH_BOUNDARY`.
- Battlefield / Art Mood = `APPROVED_DIRECTION`.
- Lower Deck / Roulette interaction = `NEEDS_CORRECTION`; correction brief로 요구사항을 확정했다.
- Exact text / values / micro-layout = `NON_CANON_REFERENCE`.
- `CORRECTED_NORTH_STAR_IMAGE = USER_EXPLICIT_IMAGE_REQUEST_ONLY`.
- `VISUAL_GENERATION = USER_REQUEST_ONLY`.

Current visual audit owner:
- `docs/design/APPROVED_OMENWARD_NORTH_STAR_V2_1_AUDIT_AND_CORRECTION_BRIEF_2026-08-24.md`

## 4. G1 — Canon / evidence reconciliation

현재 Current 문서는 v4.8 의미를 소유하고, 과거 C1/C2/C3 exact proof는 전용 historical evidence owner가 소유한다.

```text
LEGACY_C1_C2_C3_PROVEN
CURRENT_GODOT_RUNTIME = NOT_RUN
CURRENT_WINDOWS_RUNTIME = NOT_RUN
CURRENT_PLAYER_EXPERIENCE_EVIDENCE = NOT_RUN
```

정확한 과거 proof:
- `docs/C1_ROULETTE_RECOVERY_REPORT_2026-07-22.md`
- `docs/C2_BATTLE_OBJECTIVE_AUDIT_2026-07-22.md`
- `docs/C3_CORE_UX_AUDIT_2026-07-23.md`
- `docs/archive/2026-07/pre-v2-canon/CURRENT_IMPLEMENTATION_STATUS_PRE_V2.md`

## 5. G2 — Economy reconciliation

```text
ECONOMY_BASELINE_DRIFT = OPEN_RECONCILIATION
FINAL_PARAMETER_VECTOR = NOT_SELECTED
FINAL_PRODUCT_NUMERICS = NOT_APPROVED
```

구현 전에 fresh main/runtime 기준으로 economy baseline을 재대조한다. 기존 수치가 있다는 이유만으로 final 제품 숫자로 승격하지 않는다.

## 6. G3 — North Star / component evidence

North Star의 목표는 그림 완성이 아니라 다음 플레이어 판단을 한 화면에서 검증하는 것이다.

- 3개 전선을 동시에 읽을 수 있는가.
- 역할 실루엣이 전장 줌에서 읽히는가.
- 3×3 + 12 direct arrows의 조작 대상이 즉시 이해되는가.
- 전장이 PRIMARY, 하단 Control Deck이 SECONDARY로 유지되는가.
- Roulette result와 lane deployment가 분리되어 보이는가.

현재 v2.1에서 전장 방향은 승인했고, Lower Deck / Roulette interaction은 correction brief를 통해 다음 구현·시각 입력으로 분해했다.

## 7. P1 — Implementation handoff gate

```text
IMPLEMENTATION_AUTHORITY_REQUIRED
CURRENT_IMPLEMENTATION_AUTHORITY = NONE
```

Final planning adversarial review와 drift check가 clean exit한 뒤에만 별도 구현 권한으로 전환한다.

## 8. P2 — Run Command implementation

승인 뒤 구현 순서:

```text
PREPARE
→ COMMIT
→ BATTLE
→ REVIEW
```

기존 StageRun/Battle/Roulette foundation을 전면 rewrite하지 않고 orchestration/state layer를 추가하는 것을 기본안으로 한다.

## 9. P3 — Roulette manipulation session

기존 deterministic board/line resolution을 재사용하고 다음 player agency를 추가한다.

```text
SPIN
→ HONEST_STOPPED_3X3
→ ROW/COLUMN_PREVIEW
→ MOVE_TICKET_COMMIT
→ CENTER_LINE_LOCK
→ LINE_CASCADE
→ RESULT_STORAGE
```

## 10. P4 — Battlefield / Focus Deck presentation

- Full three-lane top-down camera.
- Wide combat road and readable clash nodes.
- Silhouette-first unit presentation.
- Focus-adaptive lower control deck.
- top HUD = resource total single owner.
- Roulette Focus = 3×3 + 12 direct arrows dominant.
- COMMIT Focus = stored units → pending lane → irreversible warning → one CTA.

## 11. P5 — Runtime / human vertical slice

실행 증거를 다음처럼 분리한다.

```text
GODOT_IMPORT
HEADLESS_CONTRACTS
RUNTIME_SMOKE
HUMAN_USABILITY
PLAYER_EXPERIENCE
```

앞 단계 PASS를 다음 단계로 자동 전이하지 않는다.

## 12. P6 — Platform / release

PC/Steam을 먼저 검증한다. Android/Google Play 실기기·모바일 UI·lifecycle은 PC 제품 구현 완료 후 출시 준비 직전까지 deferred 가능하다.

## 13. Historical product-planning lineage

다음 2026-08-05 planning batch는 현재 next gate가 아니지만 후속 정본이 어떤 문제를 승계했는지 추적하기 위해 보존한다.

```text
OMW-DEC-20260805-PLANNING-SIX-BUILDING-T2-T3-BRANCHES-AND-COUNTERS-V1
3_OF_10 = HISTORICAL_LINEAGE_ONLY

OMW-DEC-20260805-PLANNING-TROOP-ROLES-SYNERGIES-AND-COUNTERS-V1
4_OF_10 = HISTORICAL_LINEAGE_ONLY

OMW-DEC-20260805-PLANNING-TACTICAL-SKILLS-AND-MANA-V1
5_OF_10 = HISTORICAL_LINEAGE_ONLY

OMW-DEC-20260805-PLANNING-STAGE-END-MERCHANT-V1
6_OF_10 = HISTORICAL_LINEAGE_ONLY
```

이 계보는 current v4.8 owner보다 높은 권한이 아니며 과거 상태를 current 작업 순서로 되살리지 않는다.

## 14. Historical work-items

```text
CURRENT_OPEN_PRS_AND_ISSUES = FRESH_GITHUB_QUERY_REQUIRED
```

과거 work-item 상태를 current roadmap gate로 고정하지 않는다.

## 15. 단계 변경 시 문서 동기화

```text
Decision owner
→ CURRENT_CONFIRMED_DECISIONS
→ ACTIVE_CONTEXT / PROJECT_CORE / GDD / ROADMAP / PENDING / MAP / LIFECYCLE
→ Project Notion human-facing surface
→ destination readback
```

## 16. 지금 실행할 단 하나의 작업

```text
CURRENT_NEXT = FINAL_PLANNING_ADVERSARIAL_REVIEW_AND_DRIFT_CHECK
CORRECTED_NORTH_STAR_IMAGE = USER_EXPLICIT_IMAGE_REQUEST_ONLY
VISUAL_GENERATION = USER_REQUEST_ONLY
IMPLEMENTATION_AUTHORITY = NONE
```
