# 오멘워드 Documentation Map

```yaml
updated_at: 2026-08-03
work_mode: TOTAL_PLANNING
current_phase: HERO_TRIGGER_TARGET_POWER_MAIN_CANONICAL
current_recovery_decision: OMW-DEC-20260802-CANON-RECOVERY-V1
current_planning_decision: OMW-DEC-20260803-GAMEPLAY-HERO-UNIQUE-SKILL-2-TRIGGER-TARGET-AND-POWER-BUDGET-VALIDATION-V1
current_benchmark_policy: OMW-PROC-20260803-GRILL-ME-BENCHMARK-PRODUCTION-COMPARISON-V1
current_main: RESOLVE_FROM_REPOSITORY_DEFAULT_BRANCH
working_branch: NONE
active_base: 9.4.3_RELEASED
current_product: LEGACY_PROTOTYPE
latest_planning: MAIN_CANONICAL_NOT_IMPLEMENTED
product_code_authority: NONE
last_merged_planning_pr: 129
last_merged_planning_commit: 173a408eb7b89992a81165438d97946167db0e14
current_planning_pr: NONE
current_grill_me_count: 0
preflight: NEXT_AT_10_OF_10
planning_docs_merge_policy: AUTO_PROCEED_AFTER_GREEN_PREFLIGHT_UNDER_STANDING_USER_AUTHORIZATION
```

이 문서는 질문별 현행 책임 원본을 선택하는 라우터다. `current_main`은 저장소 기본 브랜치에서 실행 시점에 해석한다.

## 1. 기본 읽기 순서

```text
최신 사용자 지시
→ AGENTS.md
→ BASE_RULES_VERSION.md
→ DOCUMENTATION_MAP.md
→ PROJECT_CORE.md
→ PROJECT_CANON_DECISION_LEDGER.md
→ 현재 질문의 APPROVED 분야 문서
→ benchmark·production comparison 자료
→ CURRENT_IMPLEMENTATION_STATUS.md
→ ACTIVE_CONTEXT.md
→ HANDOFF_CONTEXT.md
→ 실제 code/data/Scene/Resource/tests
→ 연결 Google Sheet
```

## 2. 현재 책임 원본

| 질문 | 현행 책임 원본 | 권한 |
|---|---|---|
| 제품 정체성·플레이어 약속 | `PROJECT_CORE.md` | `CURRENT_CORE_AUTHORITY` |
| 승인 Decision·병합 후 0/10 카운터 | `PROJECT_CANON_DECISION_LEDGER.md` | `CURRENT_DECISION_AUTHORITY / MAIN_CANONICAL` |
| Grill Me 벤치마크·현업 비교 | `process/APPROVED_GRILL_ME_BENCHMARK_AND_PRODUCTION_COMPARISON_POLICY_2026-08-03.md` | `ACTIVE_STANDING_POLICY / NON_COUNTER` |
| 전체 시스템 Vertical Slice | `design/APPROVED_VERTICAL_SLICE_SYSTEM_CONTRACT_2026-07-27.md` | `CURRENT_VERTICAL_SLICE_AUTHORITY / NOT_IMPLEMENTED` |
| Vertical Slice 적대적 검토 | `reviews/ADVERSARIAL_VERTICAL_SLICE_REVIEW_2026-07-27.md` | `CURRENT_ADVERSARIAL_REVIEW_LINEAGE` |
| 룰렛 통제감 Evidence Pilot | `benchmarks/OMENWARD_ROULETTE_AGENCY_EVIDENCE_PACK_2026-07-29.md` | `PILOT_RECOMMENDATION / NOT_CANON` |
| 병종 등급·Tier·표준 스킬 | `design/APPROVED_UNIT_GRADE_AND_ABILITY_GROWTH.md` | `MERGED_STANDARD_GRADE_AUTHORITY` |
| 영웅 이상 전역 단일 활성·해금 스킬 교체 | `design/APPROVED_OMENWARD_HERO_GRADE_SLOT_AND_UNLOCKED_SKILL_REPLACEMENT_2026-08-02.md` | `MAIN_CANONICAL_GRADE_SLOT_AND_SKILL_AUTHORITY` |
| 초기 5명 고유 2스킬 콘셉트 | `design/APPROVED_OMENWARD_FIRST_FIVE_UNIQUE_SKILL_2_CONCEPTS_2026-08-03.md` | `MAIN_CANONICAL_FIRST_FIVE_SKILL_CONCEPT_AUTHORITY` |
| 고유 2스킬 자동 발동 계보 | `design/APPROVED_OMENWARD_HERO_ABILITY_ACTIVATION_MODE_2026-08-02.md` | `COMMON_AUTOMATIC_ACTIVATION_LINEAGE` |
| cooldown·charge·실패 정책 | `design/APPROVED_OMENWARD_HERO_UNIQUE_SKILL_2_COOLDOWN_CHARGE_AND_FAILURE_POLICY_2026-08-03.md` | `MAIN_CANONICAL_TIMER_AND_FAILURE_PARENT` |
| timer 지속·Stage·정비시간 경계 | `design/APPROVED_OMENWARD_HERO_UNIQUE_SKILL_2_TIMER_PERSISTENCE_AND_STAGE_BOUNDARY_POLICY_2026-08-03.md` | `MAIN_CANONICAL_TIMER_STAGE_AUTHORITY` |
| Trigger·대상·파워 예산 검증 | `design/APPROVED_OMENWARD_HERO_UNIQUE_SKILL_2_TRIGGER_TARGET_AND_POWER_BUDGET_VALIDATION_2026-08-03.md` | `MAIN_CANONICAL_TRIGGER_TARGET_POWER_AUTHORITY` |
| 재전설 결과와 전역 슬롯 충돌 | `design/APPROVED_OMENWARD_REPEAT_LEGENDARY_RESULT_HIGH_GRADE_SLOT_RESOLUTION_2026-08-02.md` | `MAIN_CANONICAL_REPEAT_LEGENDARY_TOKEN_RESOLUTION` |
| 영웅 슬롯·핵심 재미 적대적 검토 | `reviews/ADVERSARIAL_HERO_GRADE_SLOT_AND_CORE_FIT_REVIEW_2026-08-02.md` | `CURRENT_HERO_GRADE_SLOT_REVIEW` |
| 실제 구현·Legacy 경계 | `CURRENT_IMPLEMENTATION_STATUS.md` | `CURRENT_IMPLEMENTATION_AUTHORITY` |
| 현재 작업·다음 Gate | `ACTIVE_CONTEXT.md` | `CURRENT_CONTEXT_PACK` |
| 새 작업자 인계 | `HANDOFF_CONTEXT.md` | `CURRENT_HANDOFF` |
| Google Sheet 동기화 | `PROJECT_GOOGLE_SHEET_WORKBOOK.md` | `CURRENT_SHEET_CONTRACT` |

## 3. Evidence Pilot 경계

`benchmarks/OMENWARD_ROULETTE_AGENCY_EVIDENCE_PACK_2026-07-29.md`는 반드시 라우팅하지만 상태는 정확히 다음과 같다.

```text
PILOT_RECOMMENDATION / NOT_CANON
```

Pilot은 APPROVED 정본과 실제 구현 완료 증거가 아니며 Project Core를 자동 변경하지 않는다.

## 4. 등급·전역 슬롯

```text
[일반] = 1스킬
[엘리트] = 강화 1스킬
[영웅] = 강화 1스킬 + 표준 2스킬
해금 이름 지정 [영웅] = 강화 1스킬 + 고유 2스킬
[전설] = 강화 1스킬 + 강화 표준 2스킬 + 표준 3스킬
향후 해금 이름 지정 [전설] = 강화 1스킬 + 강화 표준 2스킬 + 고유 3스킬
```

```text
STANDARD_HERO_POWER < UNLOCKED_NAMED_HERO_POWER < STANDARD_LEGENDARY_POWER
ACTIVE_UNIT_COUNT_WHERE_GRADE_IN(HERO, LEGENDARY) <= 1
FUTURE_NAMED_LEGENDARY_IMPLEMENTATION = NOT_NOW
```

## 5. 초기 5명

```text
shield_guard → 불퇴의 성벽
archer       → 천공 소거
priest       → 생명의 서약
mage         → 메테오
assassin     → 그림자 분신
```

## 6. 공통 상태·Stage 정책

```text
INITIAL_WARMUP
→ READY_WAITING_FOR_VALID_CONDITION
→ CAST_PRECHECK
→ CAST_COMMIT
→ RESOLUTION_OR_ACTIVE_EFFECT
→ COOLDOWN
→ READY
```

```text
MAX_STORED_READY_COUNT = 1
CHARGE_ACCUMULATION = FALSE
MANA_OR_ENERGY_RESOURCE = FALSE
COOLDOWN_DURING_ACTIVE_EFFECT = FALSE
ACTIVE_COMBAT = TIMER_PROGRESS
MAINTENANCE_OR_PREPARATION = TIMER_PAUSED
READY_AND_REMAINING_TIME = CARRY_ON_SAME_INSTANCE
ACTIVE_EFFECT_OR_UNRESOLVED_COMMIT_STAGE_CARRY = FORBIDDEN
```

## 7. Trigger·대상 라우팅

```text
READY
→ public trigger
→ same-lane legal filter
→ public priority score
→ stability window
→ stable ID / stable position tie-break
→ CAST_PRECHECK
→ immutable CAST_COMMIT snapshot
```

- 방패병: 전열 압력·보호 가치.
- 궁병: 비행 수·가중 위협도와 비행 Snapshot.
- 사제: 체력 기준 이하 생존 아군 집합.
- 마법사: 적중 수 → 총 위협도 → stable 위치.
- 암살자: 역할 → 후열 깊이 → 위협도 → stable ID; 분신 독립 재탐색 금지.

```text
PUBLIC_TRIGGER_RULE = REQUIRED
PUBLIC_TARGET_PRIORITY = REQUIRED
DETERMINISTIC_TIE_BREAK = REQUIRED
ARBITRARY_FALLBACK_RETARGET = FORBIDDEN
HIDDEN_FUTURE_BATTLE_END_ORACLE = FORBIDDEN
```

## 8. 파워 위계 검증 라우팅

```text
A = 표준 [영웅]
B = 해금 이름 지정 [영웅]
C = 표준 [전설]
```

동일 source Tier·seed·Stage·건물·다른 두 전선 조건으로 대표 encounter family를 비교한다. B는 의도된 family에서 A보다 강하고, C는 전체 대표 family 합산 가치에서 B보다 강해야 한다. 모든 family 자동 최선 또는 다른 두 전선 비결정화는 실패다.

## 9. 계보·구형 표현

- named Hero만 1명 제한은 현행이 아니다.
- 표준 2스킬과 고유 2스킬 동시 보유는 현행이 아니다.
- 패시브/active 선택형·강제 상쇄 sidegrade는 계보 보존용이다.
- Stage마다 timer 초기화 또는 정비시간 cooldown 진행은 현행이 아니다.
- 미해결 commit 다음 Stage 이월·재타깃은 금지한다.
- 영웅별 숨은 AI·랜덤 tie-break·수동 target은 현행이 아니다.

## 10. 구현 경계

```text
CURRENT_PRODUCT = LEGACY_PROTOTYPE
LATEST_APPROVED = MAIN_CANONICAL_NOT_IMPLEMENTED
PRODUCT_CODE = UNCHANGED
CODEX = BLOCKED
PUBLIC_TRIGGER_TARGET_RESOLVER = APPROVED_CONCEPT
POWER_VALIDATION_MATRIX = APPROVED_CONCEPT
EXACT_SCHEMA = PENDING
EXACT_TRIGGER_THRESHOLDS = PENDING
EXACT_STABILITY_WINDOWS = PENDING
EXACT_SECONDS = PENDING
EXACT_DURATIONS_AND_VALUES = PENDING
ASSETS = NOT_CREATED
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
```

## 11. 운영 Gate

```text
CURRENT_COUNT = 0/10
NEXT_PREFLIGHT = AFTER_10_MORE_APPROVED_GRILL_ME_DECISIONS
CURRENT_PLANNING_PR = NONE
LAST_MERGED_PLANNING_PR = 129
```
