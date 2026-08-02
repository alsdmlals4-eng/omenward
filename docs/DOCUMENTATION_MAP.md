# 오멘워드 Documentation Map

```yaml
updated_at: 2026-08-03
work_mode: TOTAL_PLANNING
current_phase: HERO_UNIQUE_SKILL_2_COOLDOWN_POLICY_APPROVED
current_recovery_decision: OMW-DEC-20260802-CANON-RECOVERY-V1
current_planning_decision: OMW-DEC-20260803-GAMEPLAY-HERO-UNIQUE-SKILL-2-COOLDOWN-CHARGE-AND-FAILURE-POLICY-V1
current_benchmark_policy: OMW-PROC-20260803-GRILL-ME-BENCHMARK-PRODUCTION-COMPARISON-V1
current_main: RESOLVE_FROM_REPOSITORY_DEFAULT_BRANCH
working_branch: gpt/omenward-hero-kit-planning-20260802
active_base: 9.4.3_RELEASED
current_product: LEGACY_PROTOTYPE
latest_planning: USER_APPROVED_ACTIVE_BRANCH_NOT_IMPLEMENTED
product_code_authority: NONE
last_merged_planning_pr: 127
current_planning_pr: 129
current_grill_me_count: 8
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
| 제품 정체성·플레이어 약속·불변 조건 | `PROJECT_CORE.md` | `CURRENT_CORE_AUTHORITY` |
| 승인 Decision·8/10 카운터 | `PROJECT_CANON_DECISION_LEDGER.md` | `CURRENT_DECISION_AUTHORITY` |
| Grill Me 벤치마크·현업 비교 | `process/APPROVED_GRILL_ME_BENCHMARK_AND_PRODUCTION_COMPARISON_POLICY_2026-08-03.md` | `ACTIVE_STANDING_POLICY / NON_COUNTER` |
| 전체 시스템 Vertical Slice | `design/APPROVED_VERTICAL_SLICE_SYSTEM_CONTRACT_2026-07-27.md` | `CURRENT_VERTICAL_SLICE_AUTHORITY / NOT_IMPLEMENTED` |
| Vertical Slice 적대적 검토 | `reviews/ADVERSARIAL_VERTICAL_SLICE_REVIEW_2026-07-27.md` | `CURRENT_ADVERSARIAL_REVIEW_LINEAGE` |
| 룰렛 통제감 Evidence Pilot | `benchmarks/OMENWARD_ROULETTE_AGENCY_EVIDENCE_PACK_2026-07-29.md` | `PILOT_RECOMMENDATION / NOT_CANON` |
| 병종 등급·Tier·표준 스킬 성장 | `design/APPROVED_UNIT_GRADE_AND_ABILITY_GROWTH.md` | `MERGED_STANDARD_GRADE_AUTHORITY` |
| 영웅 이상 전역 단일 활성·해금 스킬 교체 | `design/APPROVED_OMENWARD_HERO_GRADE_SLOT_AND_UNLOCKED_SKILL_REPLACEMENT_2026-08-02.md` | `CURRENT_GRADE_SLOT_AND_SKILL_AUTHORITY` |
| 초기 5명 고유 2스킬 콘셉트 | `design/APPROVED_OMENWARD_FIRST_FIVE_UNIQUE_SKILL_2_CONCEPTS_2026-08-03.md` | `CURRENT_FIRST_FIVE_SKILL_CONCEPT_AUTHORITY` |
| 고유 2스킬 cooldown·charge·실패 정책 | `design/APPROVED_OMENWARD_HERO_UNIQUE_SKILL_2_COOLDOWN_CHARGE_AND_FAILURE_POLICY_2026-08-03.md` | `CURRENT_TIMER_CHARGE_FAILURE_AUTHORITY` |
| 자동 발동 공통 계보 | `design/APPROVED_OMENWARD_HERO_ABILITY_ACTIVATION_MODE_2026-08-02.md` | `REFINED_BY_CURRENT_TIMER_POLICY` |
| 재전설 결과와 전역 슬롯 충돌 | `design/APPROVED_OMENWARD_REPEAT_LEGENDARY_RESULT_HIGH_GRADE_SLOT_RESOLUTION_2026-08-02.md` | `CURRENT_REPEAT_LEGENDARY_TOKEN_RESOLUTION` |
| 영웅 슬롯·핵심 재미 적합성 검토 | `reviews/ADVERSARIAL_HERO_GRADE_SLOT_AND_CORE_FIT_REVIEW_2026-08-02.md` | `CURRENT_HERO_GRADE_SLOT_REVIEW` |
| 초기 영웅 병종 5종 | `design/APPROVED_OMENWARD_HERO_INITIAL_ROSTER_ARCHETYPE_SELECTION_2026-08-02.md` | `USER_APPROVED_FIVE_ARCHETYPE_ROSTER` |
| 초기 영웅 검증 범위 | `design/APPROVED_OMENWARD_HERO_INITIAL_ROSTER_SCOPE_2026-08-02.md` | `USER_APPROVED_INITIAL_SCOPE` |
| 실제 구현·Legacy 경계 | `CURRENT_IMPLEMENTATION_STATUS.md` | `CURRENT_IMPLEMENTATION_AUTHORITY` |
| 현재 작업·다음 Gate | `ACTIVE_CONTEXT.md` | `CURRENT_CONTEXT_PACK` |
| 새 작업자 인계 | `HANDOFF_CONTEXT.md` | `CURRENT_HANDOFF` |
| Google Sheet 동기화 | `PROJECT_GOOGLE_SHEET_WORKBOOK.md` | `CURRENT_SHEET_CONTRACT` |

## 3. 등급·전역 슬롯 라우팅

```text
[일반] = 1스킬
[엘리트] = 강화 1스킬
[영웅] = 강화 1스킬 + 표준 2스킬
해금 이름 지정 [영웅] = 강화 1스킬 + 고유 2스킬
[전설] = 강화 1스킬 + 강화 표준 2스킬 + 표준 3스킬
```

```text
STANDARD_HERO_POWER < UNLOCKED_NAMED_HERO_POWER < STANDARD_LEGENDARY_POWER
ACTIVE_UNIT_COUNT_WHERE_GRADE_IN(HERO, LEGENDARY) <= 1
```

- 영웅·전설 표준/해금 변형은 전장 전체 슬롯 하나를 공유한다.
- 제한은 획득이 아니라 배치에 적용한다.
- 재전설 결과는 동일 계열 영웅 등급 보상 토큰 2개다.

## 4. 초기 5명 고유 2스킬

```text
shield_guard → 불퇴의 성벽
archer       → 천공 소거
priest       → 생명의 서약
mage         → 메테오
assassin     → 그림자 분신
```

상세 trigger·대상·금지·제작 경계는 `APPROVED_OMENWARD_FIRST_FIVE_UNIQUE_SKILL_2_CONCEPTS_2026-08-03.md`가 소유한다.

## 5. timer·charge·실패 라우팅

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
```

- 유효 조건이 없으면 READY를 유지한다.
- precommit 무효화는 cooldown을 소비하지 않는다.
- 단발 해결형은 commit payload를 한 번 해결한다.
- owner-bound 지속형은 시전자 제거 시 종료한다.
- cooldown은 해결 또는 지속효과 종료 뒤 시작한다.
- save/load·Retry로 상태·대상·READY를 재굴림하지 않는다.

## 6. Grill Me 벤치마크 라우팅

```text
project canon
→ official/commercial benchmark 2~4
→ OMENWARD difference
→ production cost and dependencies
→ adversarial review
→ options and recommendation
```

공식 1차 자료를 우선하고 직접 비교가 없으면 `DIRECT_COMPARABLE_NOT_FOUND`를 기록한다.

## 7. 계보·증거·구현 경계

- `APPROVED_VERTICAL_SLICE_SYSTEM_CONTRACT_2026-07-27.md`는 기획 권위이며 구현 완료 증거가 아니다.
- `ADVERSARIAL_VERTICAL_SLICE_REVIEW_2026-07-27.md`는 전체 시스템 적대적 검토 계보다.
- `OMENWARD_ROULETTE_AGENCY_EVIDENCE_PACK_2026-07-29.md`는 반드시 `PILOT_RECOMMENDATION / NOT_CANON`으로 취급하며 현행 APPROVED 정본을 덮어쓸 수 없다.

```text
CURRENT_PRODUCT = LEGACY_PROTOTYPE
LATEST_APPROVED = DOCUMENTED_NOT_IMPLEMENTED
PRODUCT_CODE = UNCHANGED
CODEX = BLOCKED
COMMON_STATE_MACHINE = APPROVED
SINGLE_READY_STORAGE = APPROVED
INITIAL_WARMUP = APPROVED
EXACT_WARMUP_SECONDS = PENDING
EXACT_PER_SKILL_COOLDOWNS = PENDING
STAGE_AND_MAINTENANCE_TIMER_POLICY = PENDING
EXACT_TRIGGER_THRESHOLDS = PENDING
EXACT_DURATIONS_AND_VALUES = PENDING
ASSETS = NOT_CREATED
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
```

## 8. 운영·다음 Gate

- 현재 카운터는 `8/10`이다.
- 10번째 승인에서 적대적 preflight를 실행한다.
- 문서·기획 PR은 latest main 동기화·필수 CI Green·Sheet read-back·blocker 0·제품 경로 0이면 standing authorization에 따라 병합한다.

```text
NEXT_GATE = OMW-DEC-20260803-GAMEPLAY-HERO-UNIQUE-SKILL-2-TIMER-PERSISTENCE-AND-STAGE-BOUNDARY-POLICY-V1
```
