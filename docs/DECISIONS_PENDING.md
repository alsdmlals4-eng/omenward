# [현행] OMENWARD Decisions / Gates Pending

```yaml
updated_at: 2026-08-21
status: CURRENT_PENDING_GATE_INDEX
planning_contract: PROJECT_TOTAL_PLANNING_IMPLEMENTATION_AND_DELIVERY_INSTRUCTION_v4.7
current_decision_index: docs/CURRENT_CONFIRMED_DECISIONS.md
implementation_authorized: false
visual_generation: USER_REQUEST_ONLY
```

## 1. 이미 닫힌 주요 기획 Decision

다음은 더 이상 pending이 아니다.

```text
WORLD_CONFLICT_AND_CORE_STORY = CONFIRMED
20_STAGE_CONTENT_AND_BOSS_STRUCTURE = CONFIRMED
NORMALIZED_BALANCE_BUDGET = CONFIRMED_AS_PLANNING_ENVELOPE
TEXT_UX_AND_STATE_TRANSITION = CONFIRMED
VISUAL_STYLE_AND_COMPONENTS = CONFIRMED
BATTLEFIELD_SCALE_AND_READABILITY = CONFIRMED
ROULETTE_3X3_COMPONENT = CONFIRMED
TOKEN_COMPONENT = CONFIRMED
LOWER_CONTROL_DECK = CONFIRMED
ROULETTE_DDD_FEEDBACK = CONFIRMED
TOPDOWN_BATTLEFIELD_LAYOUT = CONFIRMED
TOPDOWN_UNIT_SILHOUETTE = CONFIRMED
```

## 2. P0 — Current canon / validator reconciliation

```text
CURRENT_CANON_RECONCILIATION = REQUIRED_UNTIL_EXACT_HEAD_GREEN_AND_MERGED_MAIN_READBACK
HISTORICAL_PROOF_OWNER_SEPARATION = REQUIRED
```

- Current 문서는 current v4.7 state만 소유한다.
- C1/C2/C3 exact SHA/run은 historical audit/archive evidence owner가 소유한다.
- July Vertical Slice는 `[증거/호환]`, current product authority가 아니다.
- Google Sheet는 current human authority가 아니다.

## 3. P1 — Economy baseline

```text
ECONOMY_BASELINE_DRIFT = OPEN_RECONCILIATION
FINAL_FUNCTIONAL_VALUE = POST_RUNTIME_EVIDENCE_TUNING
FINAL_PARAMETER_VECTOR = NOT_SELECTED
FINAL_PRODUCT_NUMERICS = NOT_APPROVED
```

Fresh main/runtime을 실행할 구현 단계에서 현재 데이터와 normalized planning envelope를 다시 대조한다.

## 4. P1 — Visual North Star

```text
REBUILT_NORTH_STAR_ON_USER_IMAGE_REQUEST
VISUAL_GENERATION = USER_REQUEST_ONLY
```

선행 계약은 완료됐다.

- Battlefield Scale / Wide Road
- 3×3 Roulette
- Token
- Lower Control Deck
- Roulette DDD
- Top-down Battlefield Layout
- Top-down Unit Silhouette

사용자 이미지 생성 요청 전에는 임의 생성하지 않는다.

## 5. P1 — Component sheet / reusable asset breakup

North Star가 승인된 경우에만 실제 화면을 재사용 가능한 component/asset 단위로 분해한다.

## 6. P1 — Final planning adversarial review

```text
MINIMUM_FULL_LOOPS = 5
GITHUB_NOTION_DRIFT_CHECK = REQUIRED
CLEAN_REVIEW_EXIT = REQUIRED_BEFORE_IMPLEMENTATION_HANDOFF
```

## 7. P1 — Implementation authority

```text
IMPLEMENTATION_AUTHORITY_REQUIRED
CURRENT_IMPLEMENTATION_AUTHORITY = NONE
```

승인 전 제품 code/data/scene/balance/player-facing runtime을 변경하지 않는다.

## 8. Runtime evidence pending

```text
CURRENT_GODOT_RUNTIME = NOT_RUN
CURRENT_WINDOWS_RUNTIME = NOT_RUN
CURRENT_UI_EVIDENCE = NOT_RUN
CURRENT_HUMAN_USABILITY_EVIDENCE = NOT_RUN
CURRENT_PLAYER_EXPERIENCE_EVIDENCE = NOT_RUN
```

과거 C1/C2/C3 technical evidence는 `LEGACY_C1_C2_C3_PROVEN`으로 보존되지만 현재 재기획 경험 증거를 대신하지 않는다.

## 9. Implementation-stage reconciliation candidates

구현 권한이 열릴 때 다음을 fresh main에서 재대조한다.

- legacy `tutorial_stage`와 `FIRST_SESSION = REAL_MAPRUN`의 관계.
- 기존 StageRun/RunCommand orchestration gap.
- 3×3 stopped/manipulation session.
- battlefield graybox와 top-down presentation adapter.
- economy drift.
- historical Issue176 role-output package 중 current design에 여전히 필요한 부분.

과거 packet을 그대로 실행하지 않는다.

## 10. Platform / release later gates

```text
COMMON_PLATFORM_GATE = NOT_RUN
PC_RELEASE_GATE = NOT_RUN
MOBILE_RELEASE_GATE = NOT_RUN
ANDROID_DEVICE = DEFERRED_RELEASE_NEAR
EXPORT_PRESETS = ABSENT
```

## 11. GitHub live-state rule

```text
CURRENT_OPEN_PRS_AND_ISSUES = FRESH_GITHUB_QUERY_REQUIRED
PR175 = CLOSED_UNMERGED_HISTORICAL
PR177 = CLOSED_UNMERGED_REFERENCE_HISTORY
PR197 = CLOSED_UNMERGED_SUPERSEDED_BY_198
```

## 12. Next gate

```text
CURRENT_NEXT = REBUILT_NORTH_STAR_ON_USER_IMAGE_REQUEST
THEN = COMPONENT_SHEET
THEN = FINAL_PLANNING_ADVERSARIAL_REVIEW
THEN = IMPLEMENTATION_AUTHORITY_REQUIRED
```
