# 오멘워드 Documentation Map

```yaml
updated_at: 2026-08-02
work_mode: TOTAL_PLANNING
current_phase: HERO_INITIAL_ROSTER_ARCHETYPE_SELECTION
current_recovery_decision: OMW-DEC-20260802-CANON-RECOVERY-V1
current_planning_decision: OMW-DEC-20260802-GAMEPLAY-HERO-INITIAL-ROSTER-ARCHETYPE-SELECTION-V1
current_main: RESOLVE_FROM_REPOSITORY_DEFAULT_BRANCH
working_branch: gpt/omenward-hero-kit-planning-20260802
active_base: 9.4.3_RELEASED
current_product: LEGACY_PROTOTYPE
latest_planning: USER_APPROVED_ACTIVE_BRANCH_NOT_IMPLEMENTED
product_code_authority: NONE
last_merged_planning_pr: 127
current_planning_pr: 129
current_grill_me_count: 4
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
→ CURRENT_IMPLEMENTATION_STATUS.md
→ ACTIVE_CONTEXT.md
→ HANDOFF_CONTEXT.md
→ 실제 code/data/Scene/Resource/tests
→ 연결 Google Sheet
```

## 2. 현재 책임 원본

| 질문 | 현행 책임 원본 | 권한 |
|---|---|---|
| 제품 정체성·불변 조건 | `PROJECT_CORE.md` | `CURRENT_CORE_AUTHORITY` |
| 승인 Decision·4/10 카운터 | `PROJECT_CANON_DECISION_LEDGER.md` | `CURRENT_DECISION_AUTHORITY` |
| 전체 시스템 Vertical Slice | `design/APPROVED_VERTICAL_SLICE_SYSTEM_CONTRACT_2026-07-27.md` | `CURRENT_VERTICAL_SLICE_AUTHORITY / NOT_IMPLEMENTED` |
| 현행 적대적 검토·blocker 계보 | `reviews/ADVERSARIAL_VERTICAL_SLICE_REVIEW_2026-07-27.md` | `CURRENT_ADVERSARIAL_REVIEW_LINEAGE` |
| 룰렛 통제감 Evidence Pilot | `benchmarks/OMENWARD_ROULETTE_AGENCY_EVIDENCE_PACK_2026-07-29.md` | `PILOT_RECOMMENDATION / NOT_CANON` |
| 영웅 해금·토큰·활성·생명주기 | 관련 `APPROVED_OMENWARD_HERO_*_2026-08-02.md` | `MERGED_USER_APPROVED_LIFECYCLE` |
| 이름 지정 영웅 스킨형 단일 차이 | `design/APPROVED_OMENWARD_HERO_ABILITY_KIT_STRUCTURE_2026-08-02.md` | `USER_APPROVED_SINGLE_DELTA_VARIANT` |
| 단일 차이의 상쇄 | `design/APPROVED_OMENWARD_HERO_SIGNATURE_DELTA_BALANCE_2026-08-02.md` | `USER_APPROVED_ONE_RELATED_COMPENSATION_AXIS` |
| 초기 영웅 로스터 범위 | `design/APPROVED_OMENWARD_HERO_INITIAL_ROSTER_SCOPE_2026-08-02.md` | `USER_APPROVED_FIVE_HERO_VALIDATION_ROSTER` |
| 초기 정확 병종·유형 배정 | `design/APPROVED_OMENWARD_HERO_INITIAL_ROSTER_ARCHETYPE_SELECTION_2026-08-02.md` | `CURRENT_USER_APPROVED_ARCHETYPE_SELECTION` |
| 공용 10병종·진영 비주얼 데이터 | `design/APPROVED_SHARED_UNIT_ARCHETYPE_AND_FACTION_VISUAL_DATA_V1.md` | `MERGED_ARCHETYPE_DATA_AUTHORITY` |
| 실제 구현·Legacy 경계 | `CURRENT_IMPLEMENTATION_STATUS.md` | `CURRENT_IMPLEMENTATION_AUTHORITY` |
| 현재 작업·다음 Gate | `ACTIVE_CONTEXT.md` | `CURRENT_CONTEXT_PACK` |
| 새 작업자 인계 | `HANDOFF_CONTEXT.md` | `CURRENT_HANDOFF` |
| Google Sheet 동기화 | `PROJECT_GOOGLE_SHEET_WORKBOOK.md` | `CURRENT_SHEET_CONTRACT` |

## 3. 현행 초기 로스터 라우팅

```text
shield_guard / 방패병   → PASSIVE
archer / 궁병           → PASSIVE
assassin / 암살자       → PASSIVE
priest / 사제           → AUTOMATIC_ACTIVE_SKILL
mage / 마법사           → AUTOMATIC_ACTIVE_SKILL
```

```text
INITIAL_HERO_COUNT = 5
UNIQUE_SOURCE_ARCHETYPE_COUNT = 5
PASSIVE_COUNT = 3
AUTOMATIC_ACTIVE_COUNT = 2
```

- 최신 사용자 직접 선택이 이전 4명 권장 수량을 대체한다.
- 5명은 초기 제작·검증 범위이며 최종 출시 상한이 아니다.
- 구체 영웅 이름·단일 차이 효과·상쇄 축·수치는 pending이다.
- 거인·기병은 초기 5명에 포함되지 않는다.

## 4. 검증 커버리지

```text
shield_guard → nearest / frontline / ranged defense
archer       → flying first / ranged / anti-air
assassin     → backline / bypass
priest       → lowest-health ally / support
mage         → cluster / ranged control
```

궁병과 마법사는 모두 ranged지만 지속 대공과 군집 광역 자동 스킬로 역할을 구분한다.

## 5. 공통 영웅 불변식

```text
PASSIVE XOR AUTOMATIC_ACTIVE_SKILL
SIGNATURE_DELTA_COUNT = 1
COMPENSATION_AXIS_COUNT = 1
ALL_OTHER_SOURCE_AXES_INHERITED = TRUE
```

- 원본 역할·공격·사거리·이동·AI·리그·기본 애니메이션을 우선 재사용한다.
- 무료 능력·다축 하향·전체 스탯 재설계를 금지한다.
- 원본 병종 우위 상황을 병종마다 하나 이상 유지한다.

## 6. 계보·증거 경계

- `APPROVED_VERTICAL_SLICE_SYSTEM_CONTRACT_2026-07-27.md`는 현행 전체 시스템 기획 권위지만 구현 완료 증거가 아니다.
- `ADVERSARIAL_VERTICAL_SLICE_REVIEW_2026-07-27.md`는 현행 적대적 검토와 제품 코드 blocker 경계의 책임 원본이다.
- `OMENWARD_ROULETTE_AGENCY_EVIDENCE_PACK_2026-07-29.md`는 **`PILOT_RECOMMENDATION / NOT_CANON`**이다.
- Evidence Pilot은 별도 사용자 승인 전 정본·구현 권한을 가지지 않는다.

## 7. 구현 경계

```text
CURRENT_PRODUCT = LEGACY_PROTOTYPE
LATEST_APPROVED = DOCUMENTED_NOT_IMPLEMENTED
PRODUCT_CODE = UNCHANGED
CODEX = BLOCKED
INITIAL_HERO_COUNT = 5
EXACT_ARCHETYPES = [shield_guard, archer, priest, mage, assassin]
EXACT_HERO_IDENTITIES = PENDING
EXACT_SIGNATURE_EFFECTS = PENDING
EXACT_COMPENSATION_AXES = PENDING
ASSETS = NOT_CREATED
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
```

## 8. 운영·다음 Gate

- 현재 카운터는 `4/10`이다.
- 10번째 승인에서 적대적 preflight를 실행한다.

```text
NEXT_GATE = OMW-DEC-20260802-GAMEPLAY-HERO-FIRST-FIVE-SIGNATURE-CONCEPTS-V1
```
