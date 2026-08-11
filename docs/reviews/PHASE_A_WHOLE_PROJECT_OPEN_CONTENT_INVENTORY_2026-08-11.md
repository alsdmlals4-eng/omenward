# [검토] OMENWARD Phase A 전체 프로젝트 미확정 콘텐츠 인벤토리

```yaml
updated_at: 2026-08-11
decision_id: OMW-DEC-20260811-OPS-ACTIVATE-INTEGRATED-CONTRACT-V4-5-R2-V1
source_main_observed: 652ced07d70fac33a4d3415eacaaec8bd2523e78
base_main_observed: 315c66eea9614c284b9c11c4d522141065dfa4b0
work_phase: PHASE_A_GPT_CHAT_PLANNING
review_result: GENUINE_OPEN_PRODUCT_DECISIONS_IDENTIFIED / USER_APPROVAL_REQUIRED
product_code_mutation: NONE
godot_persistent_mutation: NONE
auto_approve_new_product_choices: FORBIDDEN
```

## 1. 온보딩 10/10과 전체 프로젝트 Phase A를 분리

현재 `MAIN_CANONICAL_APPROVED_10_OF_10`은 온보딩 planning batch의 완료 상태로 보존한다. 이를 전체 프로젝트의 모든 제품 결정 완료로 확대 해석하지 않는다.

```text
ONBOARDING_PLANNING_STATUS = MAIN_CANONICAL_APPROVED_10_OF_10
ONBOARDING_10_OF_10_SCOPE = ONBOARDING_BATCH_ONLY
WHOLE_PROJECT_PHASE_A_STATUS = OPEN_CONTENT_REMAINING
WHOLE_PROJECT_PLANNING_COMPLETE = FALSE
USER_EXPLICIT_PLANNING_COMPLETE_DECLARATION = NOT_RECEIVED
PHASE_B_FINAL_PLANNING_REVIEW = NOT_RUN
PHASE_C_BLOCKED
```

Core guardrail의 제품 결정 순서는 Stage/Wave/Danger/Boss → Building T2/T3 → Troop roles → Tactical skills → Merchant → Onboarding → Hero·Legendary revalidation → Meta·Hub revalidation이다. 현재 앞선 core/onboarding 계층이 정리되어도 마지막 두 family가 HELD이면 whole-project Phase A는 자동 완료되지 않는다.

## 2. Genuine new product Decision groups = 3

현재 최신 owner와 Lifecycle을 교차 확인해, 새 사용자 제품 승인이 필요한 그룹을 정확히 세 개로 한정한다.

```text
OPEN_GROUP_1 = BUILDING_T3_DETAILS_AND_FINAL_BRANCH_NAMING
OPEN_GROUP_2 = HERO_LEGENDARY_FAMILY_REVALIDATION
OPEN_GROUP_3 = META_HUB_REVALIDATION
```

이 세 그룹은 하나의 승인으로 뭉개지지 않는다. 다음 Grill Me에서 각 그룹을 10개 이하의 구체 결정으로 분해해 사용자에게 권장안을 제시한다.

## 3. Open Group 1 — Building T3

최신 building-tier owner는 T2 구조를 확정했지만 일부 T3 의미를 후속 결정으로 남긴다.

```text
BUILDING_T3_DETAILS = GENUINE_OPEN_PRODUCT_DECISION
DEFENSE_BRANCH_FINAL_DISPLAY_NAME = GENUINE_OPEN_PRODUCT_DECISION
```

특히 일반병 병영의 T3 방식, 방어탑 T3 세부, 일부 직선 강화 건물 T3의 정확 효과·정체성·최종 표시명은 새 결정 없이 추정 구현하지 않는다.

그러나 병종 T3 전체를 초기화하지 않는다. 병종 10개 계보의 역할/등급 구조는 PoC 승인 구조로 유지되고, 궁병은 후속 정정 owner가 더 구체적이다.

```text
TROOP_T3_ROLE_GRADE_STRUCTURE = APPROVED_POC_STRUCTURE
ARCHER_T3_CURRENT = CROSSBOW_ARCHER / RAPID_FIRE_ARCHER
TROOP_T3_EXACT_NUMERICS = POST_RUNTIME_OR_LATER_BALANCE_TUNING
```

`ANTI_AIR_ARCHER_T3`는 current implementation input이 아니다.

## 4. Open Group 2 — Hero·Legendary family

현재 Hero 계열 상세 문서는 역사적으로 구체적인 구조·수치·해금안을 포함하지만 최신 상태는 HELD다.

```text
HERO_LEGENDARY_CURRENT_STATUS = HELD_REVALIDATION_REQUIRED
HERO_LEGENDARY_IMPLEMENTATION_AUTHORITY = NONE
```

따라서 과거 Sheet/문서의 Hero 수치·해금·장비·Legendary 규칙을 현행 구현 입력으로 바로 소비하지 않는다. 재검토 시 핵심 제약은 다음이다.

- Hero가 나쁜 릴 구성·전선 커밋을 지워버리는 정답 버튼이 되지 않는다.
- Legendary는 전략적 방향을 넓히되 직접적인 raw-stat 만능 해결책이 되지 않는다.
- 현재 core의 건물→룰렛→전선→전술 인과를 강화해야 한다.
- 과거 상세는 후보/참고 근거이지 자동 재활성화된 canon이 아니다.

이 review에서는 Hero/Legendary의 새 수치·슬롯·해금 단계·구체 영웅 identity를 선택하지 않는다.

## 5. Open Group 3 — Meta·Hub

Meta progression과 auxiliary Hub 문서도 최신 상태가 HELD이며 implementation authority가 없다.

```text
META_HUB_CURRENT_STATUS = HELD_REVALIDATION_REQUIRED
META_HUB_IMPLEMENTATION_AUTHORITY = NONE
```

재검토 시 핵심 가드레일:

- 기본은 horizontal/contextual progression.
- raw-stat 영구 상승으로 core run decision을 무력화하지 않는다.
- core 이해를 돕는 unlock, 정보, 선택 폭, 도전 구조를 우선한다.
- 출시/상점/플랫폼 meta와 게임 내 permanent progression을 섞지 않는다.

이 review에서는 새 meta currency, 영구 스탯, Hub 시설 수치, progression tree를 만들지 않는다.

## 6. 이전 readiness 분류 보존

PR184에서 분리한 다음 항목은 새 제품 Decision group으로 재개방하지 않는다.

```text
ISSUE176_7_GAPS = IMPLEMENTATION_COMPLETENESS
FINAL_FV_AND_PRODUCT_NUMERICS = POST_RUNTIME_EVIDENCE_TUNING
PLATFORM_SAVE_EXPORT_STORE = RELEASE_PHASE_DEFERRED_FOR_PR175
```

또한:

```text
TOKEN_INSTANCES_PER_REEL_PER_ACTIVE_SOURCE = 1
TOTAL_TOKEN_INSTANCES_PER_ACTIVE_SOURCE = 3
FRACTIONAL_TOKEN_WEIGHT = FORBIDDEN
SPECIAL_T1_SELECTION_DISTRIBUTION = POST_RUNTIME_EVIDENCE_TUNING
```

은 그대로 유지한다. 물리 TokenInstance 문법을 다시 open decision으로 만들지 않는다.

## 7. 정확히 open이 아닌 항목

다음은 전체 프로젝트에서 미완료일 수 있어도 이번 Grill Me의 새 semantic decision으로 세지 않는다.

```text
FINAL_FV_AND_PRODUCT_NUMERICS = POST_RUNTIME_EVIDENCE_TUNING
PLATFORM_SAVE_EXPORT_STORE = RELEASE_PHASE_DEFERRED_FOR_PR175
TROOP_T3_EXACT_NUMERICS = POST_RUNTIME_OR_LATER_BALANCE_TUNING
LEVEL_COORDINATES_AND_NON_SEMANTIC_TIMING = IMPLEMENTATION_DETAIL_DEFERRED
ISSUE176_7_GAPS = IMPLEMENTATION_COMPLETENESS
```

새 evidence가 의미 충돌을 발견하면 해당 항목은 다시 Phase A semantic decision으로 승격할 수 있다. 현재는 그렇지 않다.

## 8. Sheet 역사 보호

Sheet `42_병종_Tier_등급`, `50_메인콘텐츠` 등에 과거 Hero/Legendary/T3 상세가 남아 있어도 삭제·소급 덮어쓰지 않는다. 대신 current status note를 추가해 다음을 명시한다.

```text
HISTORICAL_HERO_DETAIL = HELD_REFERENCE_NOT_IMPLEMENTATION_INPUT
HISTORICAL_META_HUB_DETAIL = HELD_REFERENCE_NOT_IMPLEMENTATION_INPUT
TROOP_T3_ROLE_STRUCTURE = PRESERVED_POC
ARCHER_T3_CORRECTION = CURRENT
BUILDING_T3_DETAILS = USER_DECISION_PENDING
```

## 9. 다음 제품 Gate

```text
NEXT_PRODUCT_GATE = USER_GRILL_ME_APPROVAL_REQUIRED
AUTO_APPROVE_NEW_PRODUCT_CHOICES = FORBIDDEN
MAX_GRILL_ME_DECISIONS = 10
```

연속작업 승인은 audit·분류·정본 동기화에는 재사용할 수 있지만, 위 세 genuine open group의 새 gameplay/content 결정을 자동 승인하는 권한은 아니다.

## 10. 현재 종료 조건

이 inventory PR이 Green/병합/Sheet sync까지 닫히면 Phase A의 다음 동작은 구현이 아니라 사용자 Grill Me다.

```text
WHOLE_PROJECT_PHASE_A_STATUS = OPEN_CONTENT_REMAINING
WHOLE_PROJECT_PLANNING_COMPLETE = FALSE
NEXT_PRODUCT_GATE = USER_GRILL_ME_APPROVAL_REQUIRED
PHASE_C_BLOCKED
```
