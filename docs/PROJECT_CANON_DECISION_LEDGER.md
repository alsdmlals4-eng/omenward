# 오멘워드 기획 정본 결정 원장

```yaml
updated_at: 2026-08-02
status: CURRENT_DECISION_LEDGER / ACTIVE_PLANNING_BRANCH
current_recovery_decision: OMW-DEC-20260802-CANON-RECOVERY-V1
current_planning_decision: OMW-DEC-20260802-GAMEPLAY-HERO-INITIAL-ROSTER-ARCHETYPE-SELECTION-V1
current_world_decision: OMW-DEC-20260802-WORLD-VEILSPECIES-PURPOSE-V1
current_operating_decision: OMW-DEC-20260802-GRILL-ME-MERGE-CADENCE-V1
current_main: RESOLVE_FROM_REPOSITORY_DEFAULT_BRANCH
working_branch: gpt/omenward-hero-kit-planning-20260802
current_planning_pr: 129
active_base: 9.4.3
product_code_authority: NONE
sheet_id: 1VLwRtXGDtyj0JFt98wdIOtG6Zqc3wtdfCzSF9Fo6lpw
grill_me_approved_since_last_merge: 4
future_merge_cadence: 10_APPROVED_GRILL_ME_DECISIONS
planning_docs_merge_policy: AUTO_PROCEED_AFTER_GREEN_PREFLIGHT_UNDER_STANDING_USER_AUTHORIZATION
product_code_merge_policy: SEPARATE_CONTRACT_REQUIRED
preflight: NEXT_AT_10_OF_10
next_gate: OMW-DEC-20260802-GAMEPLAY-HERO-FIRST-FIVE-SIGNATURE-CONCEPTS-V1
```

`current_main`은 저장소 기본 브랜치에서 실행 시점에 해석한다.

## 1. 상태 언어

```text
USER_APPROVED_PLAN
!= PRODUCT_IMPLEMENTED
!= AUTOMATED_VALIDATED
!= HUMAN_VALIDATED
!= RELEASE_READY
```

## 2. 현재 묶음 Decision 4/10

| Decision ID | 상태 | 결정 | 책임 원본 | 미완료 경계 |
|---|---|---|---|---|
| `OMW-DEC-20260802-GAMEPLAY-HERO-INITIAL-ROSTER-ARCHETYPE-SELECTION-V1` | `USER_APPROVED / ACTIVE_BRANCH_SYNCED / NOT_IMPLEMENTED` | 초기 5명은 방패병·궁병·사제·마법사·암살자이며 패시브형 3명·자동 사용스킬형 2명으로 구성한다 | `design/APPROVED_OMENWARD_HERO_INITIAL_ROSTER_ARCHETYPE_SELECTION_2026-08-02.md` | 영웅 정체성·이름·단일 차이·상쇄 축·자산·simulation pending |
| `OMW-DEC-20260802-GAMEPLAY-HERO-INITIAL-ROSTER-SCOPE-V1` | `USER_APPROVED / REFINED / NOT_IMPLEMENTED` | 초기 로스터는 서로 다른 원본 병종에 1명씩 배치하는 제작·검증 범위이며 최종 출시 상한이 아니다. 최신 수량은 5명이다 | `design/APPROVED_OMENWARD_HERO_INITIAL_ROSTER_SCOPE_2026-08-02.md` | 확장 조건·출시 전체 로스터 상한 pending |
| `OMW-DEC-20260802-GAMEPLAY-HERO-SIGNATURE-DELTA-BALANCE-V1` | `USER_APPROVED / ACTIVE_BRANCH_SYNCED / NOT_IMPLEMENTED` | 원본 데이터를 복사하고 단일 차이와 직접 관련된 상쇄 축 하나만 조정한다 | `design/APPROVED_OMENWARD_HERO_SIGNATURE_DELTA_BALANCE_2026-08-02.md` | 정확 효과·수치·허용 편차·simulation pending |
| `OMW-DEC-20260802-GAMEPLAY-HERO-ABILITY-KIT-STRUCTURE-V1` | `USER_APPROVED / ACTIVE_BRANCH_SYNCED / NOT_IMPLEMENTED` | 이름 지정 영웅은 스킨형 변주이며 패시브 또는 자동 사용스킬 하나만 가진다 | `design/APPROVED_OMENWARD_HERO_ABILITY_KIT_STRUCTURE_2026-08-02.md` | 실제 효과·자산·simulation pending |

## 3. 현행 초기 영웅 로스터

```text
shield_guard / 방패병   → PASSIVE
archer / 궁병           → PASSIVE
assassin / 암살자       → PASSIVE
priest / 사제           → AUTOMATIC_ACTIVE_SKILL
mage / 마법사           → AUTOMATIC_ACTIVE_SKILL
```

```text
INITIAL_NAMED_HERO_COUNT = 5
INITIAL_SOURCE_ARCHETYPE_COUNT = 5
PASSIVE_VARIANT_COUNT = 3
AUTOMATIC_ACTIVE_SKILL_VARIANT_COUNT = 2
```

- 최신 사용자 직접 선택이 이전 4명·2:2 수량 부분을 대체한다.
- 동일 병종 복수 영웅은 초기 로스터에서 금지한다.
- 5명은 최종 출시 전체 로스터 상한이 아니다.
- 거인·기병은 이번 초기 범위에서 제외한다.

## 4. 검증 역할

- 방패병: frontline·nearest·ranged defense.
- 궁병: ranged·flying priority·anti-air.
- 암살자: bypass·backline priority.
- 사제: support·lowest-health ally.
- 마법사: ranged control·cluster priority.

궁병과 마법사는 모두 ranged이나 지속 대공과 군집 광역 자동 스킬로 판단을 분리한다.

## 5. 공통 영웅 계약

```text
원본 [영웅] 등급 병종
+ 스킨·이름·최소 식별 연출
+ PASSIVE XOR AUTOMATIC_ACTIVE_SKILL
- 직접 관련된 상쇄 축 1개
= 이름 지정 영웅
```

- 원본 역할·공격·사거리·이동·AI·리그·기본 애니메이션을 우선 재사용한다.
- 무료 능력·다축 하향·전체 성장 곡선 재설계를 금지한다.
- 원본 병종 우위 상황을 병종마다 하나 이상 유지한다.

## 6. 충돌 해소

- 활성 문서의 4명·4병종·2:2 표현은 5명·5병종·3:2로 갱신한다.
- 사제와 마법사의 자동 능력은 수동 버튼이 아니다.
- 암살자 패시브는 기존 후열 타기팅을 단순 반복하는 장식 효과가 아니어야 한다.
- 초기 5명을 완전 신규 유닛으로 제작하지 않는다.

## 7. 구현·검증 경계

```text
CURRENT_PRODUCT = LEGACY_PROTOTYPE
LATEST_APPROVED = DOCUMENTED_NOT_IMPLEMENTED
PRODUCT_CODE_AUTHORITY = NONE
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

## 8. 카운터·병합 규칙

```text
CURRENT_COUNT_SINCE_MERGE = 4_OF_10
NEXT_PREFLIGHT_AT = 10_OF_10
```

- 승인 즉시 GitHub·Sheet에 같은 Decision ID로 반영한다.
- 10번째 승인 뒤 문서·기획 PR이 Green preflight와 blocker 0을 만족하면 standing authorization에 따라 병합한다.
- 제품 코드 구현·병합은 별도 계약 대상이다.
