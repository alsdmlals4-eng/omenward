# [현행] OMENWARD Decisions / Gates Pending

```yaml
updated_at: 2026-08-24
status: CURRENT_PENDING_GATE_INDEX
planning_contract: PROJECT_TOTAL_PLANNING_IMPLEMENTATION_AND_DELIVERY_INSTRUCTION_v4.8
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
NORTH_STAR_V2_1_AREA_AUDIT = CONFIRMED
LOWER_DECK_AND_ROULETTE_CORRECTION_BRIEF = COMPLETE
COMPONENT_BREAKDOWN = COMPLETE_FOR_FINAL_PLANNING_INPUT
FINAL_PLANNING_ADVERSARIAL_REVIEW = PASS_5_OF_5
GITHUB_NOTION_DRIFT_CHECK = PASS
```

Final planning review owner:
`docs/reviews/FINAL_PLANNING_ADVERSARIAL_REVIEW_AND_DRIFT_CHECK_2026-08-24.md`

## 2. P0 — Current canon / validator reconciliation

```text
CURRENT_CANON_RECONCILIATION = REQUIRED_UNTIL_EXACT_HEAD_GREEN_AND_MERGED_MAIN_READBACK
HISTORICAL_PROOF_OWNER_SEPARATION = REQUIRED
```

- Current 문서는 current v4.8 state만 소유한다.
- C1/C2/C3 exact SHA/run은 historical audit/archive evidence owner가 소유한다.
- July Vertical Slice는 `[증거/호환]`, current product authority가 아니다.
- Google Sheet는 current human authority가 아니다.
- Current validator는 19개 Decision, North Star v2.1 audit owner, final planning review owner를 인식해야 한다.

## 3. P1 — Economy baseline

```text
ECONOMY_BASELINE_DRIFT = OPEN_RECONCILIATION
FINAL_FUNCTIONAL_VALUE = POST_RUNTIME_EVIDENCE_TUNING
FINAL_PARAMETER_VECTOR = NOT_SELECTED
FINAL_PRODUCT_NUMERICS = NOT_APPROVED
```

Fresh main/runtime을 실행할 구현 단계에서 현재 데이터와 normalized planning envelope를 다시 대조한다.

## 4. Visual North Star — 영역별 감사 완료

```text
NORTH_STAR_V2_1 = APPROVED_REFERENCE_WITH_BOUNDARY
NORTH_STAR_BATTLEFIELD = APPROVED_DIRECTION
NORTH_STAR_ART_MOOD = APPROVED_DIRECTION
NORTH_STAR_LOWER_DECK = NEEDS_CORRECTION
NORTH_STAR_ROULETTE_INTERACTION = NEEDS_CORRECTION
NORTH_STAR_EXACT_TEXT_VALUES_MICROLAYOUT = NON_CANON_REFERENCE
CORRECTED_NORTH_STAR_IMAGE = USER_EXPLICIT_IMAGE_REQUEST_ONLY
VISUAL_GENERATION = USER_REQUEST_ONLY
```

전장·분위기는 보호하고, Lower Deck·Roulette interaction은 기존 owner를 바꾸지 않고 correction brief로 교정 요구를 확정했다.

## 5. Component sheet / reusable asset breakup — 비이미지 분해 완료

North Star v2.1을 다음 구현·시각 handoff 단위로 분해했다.

- Battlefield viewport / lane / road / clash / node components.
- Top HUD resource/status components.
- Focus-adaptive Lower Shell.
- 3×3 Roulette + 12 direct arrows + Spin/Confirm/preview.
- COMMIT stored unit / pending lane / irreversible warning / one CTA.
- Build / Battle / Review focused components.

상세 owner:
`docs/design/APPROVED_OMENWARD_NORTH_STAR_V2_1_AUDIT_AND_CORRECTION_BRIEF_2026-08-24.md`

새 corrected image는 자동 생성하지 않는다.

## 6. Final planning adversarial review — 완료

```text
MINIMUM_FULL_LOOPS = 5
ADVERSARIAL_REVIEW = PASS_5_OF_5
GITHUB_NOTION_DRIFT_CHECK = PASS
NEW_PRODUCT_DECISION_REQUIRED = FALSE
PLANNING_BLOCKER = NONE
```

## 7. P1 — Implementation authority

```text
CURRENT_NEXT = IMPLEMENTATION_AUTHORITY_REQUIRED
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

## 9. Historical Barracks simulation lineage

다음은 현재 next gate가 아니라 과거 시뮬레이션/판정 계보다. 후속 economy reconciliation에서 당시 결과를 재사용할 수 있도록 보존하되 현재 수치 authority로 승격하지 않는다.

```text
5_OF_10 = REMEDIATION_SMOKE_PASS
6_OF_10_REVIEW = 10000_DECISION_SWEEP_REVIEW_COMPLETE
OMW-DEC-20260808-PLANNING-BARRACKS-10000-SEED-DECISION-SWEEP-REVIEW-V1
PARAMETER_SELECTION_NOT_IDENTIFIABLE = HISTORICAL_REVIEW_CONCLUSION
DECISION_SWEEP_10000_EXECUTION = NOT_AUTHORIZED_BY_THAT_REVIEW
FINAL_PARAMETER_VECTOR = NOT_SELECTED
```

후속 robustness 10k 및 role-output evidence는 historical experiment 범위로 보존한다. 이 계보는 `CURRENT_NEXT`를 바꾸지 않는다.

## 10. Implementation-stage reconciliation candidates

구현 권한이 열릴 때 다음을 fresh main에서 재대조한다.

- legacy `tutorial_stage`와 `FIRST_SESSION = REAL_MAPRUN`의 관계.
- 기존 StageRun/RunCommand orchestration gap.
- 3×3 stopped/manipulation session.
- battlefield graybox와 top-down presentation adapter.
- economy drift.
- historical role-output package 중 current design에 여전히 필요한 부분.

과거 packet을 그대로 실행하지 않는다.

## 11. Platform / release later gates

```text
COMMON_PLATFORM_GATE = NOT_RUN
PC_RELEASE_GATE = NOT_RUN
MOBILE_RELEASE_GATE = NOT_RUN
ANDROID_DEVICE = DEFERRED_RELEASE_NEAR
EXPORT_PRESETS = ABSENT
```

## 12. GitHub live-state rule

```text
CURRENT_OPEN_PRS_AND_ISSUES = FRESH_GITHUB_QUERY_REQUIRED
```

## 13. Next gate

```text
CURRENT_NEXT = IMPLEMENTATION_AUTHORITY_REQUIRED
CURRENT_IMPLEMENTATION_AUTHORITY = NONE
CORRECTED_NORTH_STAR_IMAGE = USER_EXPLICIT_IMAGE_REQUEST_ONLY
```
