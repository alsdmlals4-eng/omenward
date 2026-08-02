# 오멘워드 Documentation Map

```yaml
updated_at: 2026-08-03
work_mode: TOTAL_PLANNING
current_phase: FIRST_FIVE_HERO_UNIQUE_SKILL_2_CONCEPTS_APPROVED
current_recovery_decision: OMW-DEC-20260802-CANON-RECOVERY-V1
current_planning_decision: OMW-DEC-20260803-GAMEPLAY-HERO-FIRST-FIVE-UNIQUE-SKILL-2-CONCEPTS-V1
current_benchmark_policy: OMW-PROC-20260803-GRILL-ME-BENCHMARK-PRODUCTION-COMPARISON-V1
current_main: RESOLVE_FROM_REPOSITORY_DEFAULT_BRANCH
working_branch: gpt/omenward-hero-kit-planning-20260802
active_base: 9.4.3_RELEASED
current_product: LEGACY_PROTOTYPE
latest_planning: USER_APPROVED_ACTIVE_BRANCH_NOT_IMPLEMENTED
product_code_authority: NONE
last_merged_planning_pr: 127
current_planning_pr: 129
current_grill_me_count: 7
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
→ 현재 질문의 benchmark·production comparison 자료
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
| 승인 Decision·7/10 카운터 | `PROJECT_CANON_DECISION_LEDGER.md` | `CURRENT_DECISION_AUTHORITY` |
| Grill Me 벤치마크·현업 제작 비교 방식 | `process/APPROVED_GRILL_ME_BENCHMARK_AND_PRODUCTION_COMPARISON_POLICY_2026-08-03.md` | `ACTIVE_STANDING_POLICY / NON_COUNTER` |
| 전체 시스템 Vertical Slice | `design/APPROVED_VERTICAL_SLICE_SYSTEM_CONTRACT_2026-07-27.md` | `CURRENT_VERTICAL_SLICE_AUTHORITY / NOT_IMPLEMENTED` |
| Vertical Slice 적대적 검토 | `reviews/ADVERSARIAL_VERTICAL_SLICE_REVIEW_2026-07-27.md` | `CURRENT_ADVERSARIAL_REVIEW_LINEAGE` |
| 룰렛 통제감 Evidence Pilot | `benchmarks/OMENWARD_ROULETTE_AGENCY_EVIDENCE_PACK_2026-07-29.md` | `PILOT_RECOMMENDATION / NOT_CANON` |
| 병종 등급·Tier·표준 스킬 성장 | `design/APPROVED_UNIT_GRADE_AND_ABILITY_GROWTH.md` | `MERGED_STANDARD_GRADE_AUTHORITY` |
| 영웅 이상 전역 단일 활성·해금 스킬 슬롯 교체 | `design/APPROVED_OMENWARD_HERO_GRADE_SLOT_AND_UNLOCKED_SKILL_REPLACEMENT_2026-08-02.md` | `USER_APPROVED_CURRENT_GRADE_SLOT_AND_SKILL_AUTHORITY` |
| 초기 5명 고유 2스킬 전술 콘셉트 | `design/APPROVED_OMENWARD_FIRST_FIVE_UNIQUE_SKILL_2_CONCEPTS_2026-08-03.md` | `USER_APPROVED_CURRENT_FIRST_FIVE_SKILL_CONCEPT_AUTHORITY` |
| 재전설 결과와 전역 슬롯 충돌 해소 | `design/APPROVED_OMENWARD_REPEAT_LEGENDARY_RESULT_HIGH_GRADE_SLOT_RESOLUTION_2026-08-02.md` | `CURRENT_REPEAT_LEGENDARY_TOKEN_RESOLUTION` |
| 영웅 등급 해금 상위호환 | `design/APPROVED_OMENWARD_HERO_UNIQUE_SKILL_UPGRADE_MODEL_2026-08-02.md` | `REFINED_TO_UNIQUE_SKILL_2_REPLACEMENT` |
| 고유 2스킬 자동 발동·공통 cooldown | `design/APPROVED_OMENWARD_HERO_ABILITY_ACTIVATION_MODE_2026-08-02.md` | `USER_APPROVED_COMMON_COOLDOWN_READY_FRAMEWORK` |
| 영웅 슬롯·핵심 재미 적합성 적대적 검토 | `reviews/ADVERSARIAL_HERO_GRADE_SLOT_AND_CORE_FIT_REVIEW_2026-08-02.md` | `CURRENT_HERO_GRADE_SLOT_REVIEW` |
| 영웅 해금·병종 등록 | `design/APPROVED_OMENWARD_HERO_UNLOCK_REGISTRATION_2026-08-02.md` | `MERGED_USER_APPROVED_ROSTER` |
| 영웅 토큰 변환·배치 | `design/APPROVED_OMENWARD_HERO_TOKEN_CONVERSION_AND_DEPLOYMENT_2026-08-02.md` | `MERGED_USER_APPROVED_ACTIVATION / REFINED_BY_HIGH_GRADE_SLOT` |
| 과거 이름 지정 영웅 단일 활성·반복 출전 | `design/APPROVED_OMENWARD_HERO_SINGLE_ACTIVE_AND_REPEAT_DEPLOYMENT_2026-08-02.md` | `MERGED_HISTORY / ACTIVE_LIMIT_REFINED_BY_HIGH_GRADE_SLOT` |
| 영웅 Stage 상태·사망·재출전 | `design/APPROVED_OMENWARD_HERO_STAGE_STATE_PERSISTENCE_2026-08-02.md`, `design/APPROVED_OMENWARD_HERO_REDEPLOYMENT_INITIAL_STATE_2026-08-02.md` | `MERGED_USER_APPROVED_LIFECYCLE` |
| 초기 영웅 병종 5종 | `design/APPROVED_OMENWARD_HERO_INITIAL_ROSTER_ARCHETYPE_SELECTION_2026-08-02.md` | `USER_APPROVED_FIVE_ARCHETYPE_ROSTER` |
| 초기 영웅 검증 범위 | `design/APPROVED_OMENWARD_HERO_INITIAL_ROSTER_SCOPE_2026-08-02.md` | `USER_APPROVED_FIVE_UNIQUE_SKILL_2_HEROES` |
| 영웅 스킨형 자산 구조 | `design/APPROVED_OMENWARD_HERO_ABILITY_KIT_STRUCTURE_2026-08-02.md` | `REFINED_TO_UNIQUE_SKILL_2` |
| 영웅 전투 예산 | `design/APPROVED_OMENWARD_HERO_POWER_BUDGET_AND_SIDEGRADE_2026-08-02.md` | `REFINED_TO_HERO_LT_NAMED_HERO_LT_LEGENDARY` |
| 과거 강제 상쇄 축 | `design/APPROVED_OMENWARD_HERO_SIGNATURE_DELTA_BALANCE_2026-08-02.md` | `SUPERSEDED_HISTORY / NOT_CURRENT` |
| 이계 생물종·경계파쇄자 | `design/APPROVED_OMENWARD_VEILSPECIES_GAMEPLAY_SCOPE_2026-08-02.md` | `MERGED_USER_APPROVED_GAMEPLAY_SCOPE` |
| 실제 구현·Legacy 경계 | `CURRENT_IMPLEMENTATION_STATUS.md` | `CURRENT_IMPLEMENTATION_AUTHORITY` |
| 현재 작업·다음 Gate | `ACTIVE_CONTEXT.md` | `CURRENT_CONTEXT_PACK` |
| 새 작업자 인계 | `HANDOFF_CONTEXT.md` | `CURRENT_HANDOFF` |
| Google Sheet 동기화 | `PROJECT_GOOGLE_SHEET_WORKBOOK.md` | `CURRENT_SHEET_CONTRACT` |

## 3. 등급·스킬 라우팅

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
FUTURE_NAMED_LEGENDARY_IMPLEMENTATION = NOT_NOW
```

- 해금 영웅은 표준 2스킬을 고유 2스킬로 교체하며 추가 스킬 슬롯을 얻지 않는다.
- 향후 해금 전설은 표준 3스킬을 고유 3스킬로 교체한다.
- 패시브·숨은 상시 보너스·의무 능력치 하향은 없다.

## 4. 전역 고등급 슬롯 라우팅

```text
ACTIVE_UNIT_COUNT_WHERE_GRADE_IN(HERO, LEGENDARY) <= 1
```

- 표준·해금, 이름, 병종, 전선을 막론하고 `[영웅]·[전설]` 활성 유닛을 모두 합산한다.
- 일반·엘리트는 제외한다.
- 제한은 획득이 아니라 배치에 적용한다.
- 슬롯 충돌 토큰은 보관·판매 가능하다.
- 자동 삭제·자동 교체·수동 퇴각·수동 교대는 금지한다.
- 재전설 결과는 같은 계열 영웅 등급 보상 토큰 2개를 만들며 즉시 유닛을 생성하지 않는다.

## 5. 초기 5명 고유 2스킬 라우팅

```text
shield_guard / 방패병 → 불퇴의 성벽
archer / 궁병         → 천공 소거
priest / 사제         → 생명의 서약
mage / 마법사         → 메테오
assassin / 암살자     → 그림자 분신
```

- 불퇴의 성벽: 비지형 방벽·전열 유지·피해 흡수.
- 천공 소거: 한 전선 유효 비행 표적 동시 일제사격.
- 생명의 서약: 회복 없는 짧은 아군 전투 유닛 체력 하한.
- 메테오: deterministic 적 밀집 지점에 예고 후 단발 낙하.
- 그림자 분신: 독립 AI 없는 owner-bound 종속 기본 공격 proxy 1체.

상세 trigger·대상·금지·제작 경계는 `design/APPROVED_OMENWARD_FIRST_FIVE_UNIQUE_SKILL_2_CONCEPTS_2026-08-03.md`가 소유한다.

## 6. 자동 발동

```text
COOLDOWN
→ READY_WAITING_FOR_VALID_CONDITION
→ 유효 조건·대상·priority·tie-break
→ CAST_COMMIT
→ 효과·VFX/SFX·로그
→ COOLDOWN
```

다음 Gate가 정확 cooldown·충전 구조·발동 실패 정책을 소유한다.

## 7. Grill Me 벤치마크 라우팅

앞으로 Grill Me 질문은 다음을 포함한다.

```text
project canon
→ official/commercial benchmark 2~4
→ OMENWARD difference
→ production cost and dependencies
→ adversarial review
→ options and recommendation
```

공식 1차 자료를 우선하고, 직접 비교 사례가 없으면 억지 사례 대신 `DIRECT_COMPARABLE_NOT_FOUND`를 기록한다. 벤치마크는 Project Core를 자동 변경하지 않는다.

## 8. 계보·증거 경계

- `APPROVED_VERTICAL_SLICE_SYSTEM_CONTRACT_2026-07-27.md`는 전체 시스템 기획 권위지만 구현 완료 증거가 아니다.
- `ADVERSARIAL_VERTICAL_SLICE_REVIEW_2026-07-27.md`는 현행 전체 시스템 적대적 검토 계보다.
- `OMENWARD_ROULETTE_AGENCY_EVIDENCE_PACK_2026-07-29.md`는 `PILOT_RECOMMENDATION / NOT_CANON`이다.
- 과거 named-only active limit과 강제 상쇄 축 문서는 계보 보존용이며 현재 제한·파워 모델을 덮어쓸 수 없다.

## 9. 구현 경계

```text
CURRENT_PRODUCT = LEGACY_PROTOTYPE
LATEST_APPROVED = DOCUMENTED_NOT_IMPLEMENTED
PRODUCT_CODE = UNCHANGED
CODEX = BLOCKED
EXACT_HERO_IDENTITIES = PENDING
UNIQUE_SKILL_2_CONCEPTS = APPROVED
EXACT_TRIGGER_THRESHOLDS = PENDING
EXACT_COOLDOWNS = PENDING
EXACT_DURATIONS_AND_VALUES = PENDING
FINAL_DISPLAY_NAMES = PENDING
FUTURE_NAMED_LEGENDARY = NOT_NOW
ASSETS = NOT_CREATED
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
```

## 10. 운영·다음 Gate

- 현재 카운터는 `7/10`이다.
- 10번째 승인에서 적대적 preflight를 실행한다.
- 문서·기획 PR은 latest main 동기화·필수 CI Green·Sheet read-back·blocker 0·제품 경로 0이면 standing authorization에 따라 병합한다.

```text
NEXT_GATE = OMW-DEC-20260803-GAMEPLAY-HERO-UNIQUE-SKILL-2-COOLDOWN-CHARGE-AND-FAILURE-POLICY-V1
```
