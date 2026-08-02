# 오멘워드 기획 정본 결정 원장

```yaml
updated_at: 2026-08-02
status: CURRENT_DECISION_LEDGER / ACTIVE_PLANNING_BRANCH
current_recovery_decision: OMW-DEC-20260802-CANON-RECOVERY-V1
current_planning_decision: OMW-DEC-20260802-GAMEPLAY-HERO-INITIAL-ROSTER-SCOPE-V1
current_world_decision: OMW-DEC-20260802-WORLD-VEILSPECIES-PURPOSE-V1
current_operating_decision: OMW-DEC-20260802-GRILL-ME-MERGE-CADENCE-V1
current_main: RESOLVE_FROM_REPOSITORY_DEFAULT_BRANCH
working_branch: gpt/omenward-hero-kit-planning-20260802
current_planning_pr: 129
active_base: 9.4.3
product_code_authority: NONE
sheet_id: 1VLwRtXGDtyj0JFt98wdIOtG6Zqc3wtdfCzSF9Fo6lpw
grill_me_approved_since_last_merge: 3
future_merge_cadence: 10_APPROVED_GRILL_ME_DECISIONS
planning_docs_merge_policy: AUTO_PROCEED_AFTER_GREEN_PREFLIGHT_UNDER_STANDING_USER_AUTHORIZATION
product_code_merge_policy: SEPARATE_CONTRACT_REQUIRED
preflight: NEXT_AT_10_OF_10
next_gate: OMW-DEC-20260802-GAMEPLAY-HERO-INITIAL-ROSTER-ARCHETYPE-SELECTION-V1
```

`current_main`은 저장소 기본 브랜치에서 실행 시점에 해석한다. 이 문서는 현재 승인 Decision과 다음 10건 카운터를 소유한다.

## 1. 상태 언어

```text
USER_APPROVED_PLAN
!= PRODUCT_IMPLEMENTED
!= AUTOMATED_VALIDATED
!= HUMAN_VALIDATED
!= RELEASE_READY
```

## 2. 현재 묶음 Decision 3/10

| Decision ID | 상태 | 결정 | 책임 원본 | 미완료 경계 |
|---|---|---|---|---|
| `OMW-DEC-20260802-GAMEPLAY-HERO-INITIAL-ROSTER-SCOPE-V1` | `USER_APPROVED / ACTIVE_BRANCH_SYNCED / NOT_IMPLEMENTED` | 최초 제작·검증 로스터는 서로 다른 기존 핵심 병종 4종에 이름 지정 영웅 1명씩 총 4명이며 패시브형 2명·자동 사용스킬형 2명으로 구성한다 | `design/APPROVED_OMENWARD_HERO_INITIAL_ROSTER_SCOPE_2026-08-02.md` | 정확 병종·영웅·역할 배정·능력·자산·simulation pending |
| `OMW-DEC-20260802-GAMEPLAY-HERO-SIGNATURE-DELTA-BALANCE-V1` | `USER_APPROVED / ACTIVE_BRANCH_SYNCED / NOT_IMPLEMENTED` | 이름 지정 영웅은 원본 `[영웅]` 등급 병종 데이터를 복사하고 단일 차이와 직접 관련된 상쇄 축 하나만 하향·조건화하며 나머지 원본 데이터는 유지한다 | `design/APPROVED_OMENWARD_HERO_SIGNATURE_DELTA_BALANCE_2026-08-02.md` | 정확 상쇄 축·수치·허용 편차·simulation pending |
| `OMW-DEC-20260802-GAMEPLAY-HERO-ABILITY-KIT-STRUCTURE-V1` | `USER_APPROVED / ACTIVE_BRANCH_SYNCED / NOT_IMPLEMENTED` | 이름 지정 영웅은 기존 병종 `[영웅]` 등급 유닛을 기반으로 한 스킨형 변주이며, 영웅 전용 차이는 패시브 1개 또는 자동 `[사용스킬]` 1개 중 정확히 하나만 가진다 | `design/APPROVED_OMENWARD_HERO_ABILITY_KIT_STRUCTURE_2026-08-02.md` | 실제 영웅 명단·단일 차이 효과·자산 범위·simulation pending |

## 3. 초기 영웅 로스터 계약

```text
서로 다른 UnitArchetype 4종
→ 병종마다 이름 지정 영웅 1명
→ 패시브형 2명
→ 자동 사용스킬형 2명
→ 초기 검증 로스터 4명
```

```text
INITIAL_NAMED_HERO_COUNT = 4
INITIAL_SOURCE_ARCHETYPE_COUNT = 4
HEROES_PER_SOURCE_ARCHETYPE = 1
PASSIVE_VARIANT_COUNT = 2
AUTOMATIC_ACTIVE_SKILL_VARIANT_COUNT = 2
```

- 동일 병종 복수 영웅은 초기 로스터에서 금지한다.
- 정확 병종·영웅 이름·능력·상쇄 축은 후속 Decision에서 확정한다.
- 네 병종은 역할·전투 판단 중복을 최소화한다.
- 4명은 초기 제작·검증 범위이며 최종 출시 로스터 상한이 아니다.
- 후보는 원본 완성도·자산 재사용성·전술 차별성·상쇄 가독성·콘텐츠 노출성을 기준으로 선정한다.

## 4. 영웅 단일 차이·상쇄 계약

```text
기존 병종 [영웅] 등급 유닛
+ 스킨·이름·최소 식별 연출
+ PASSIVE XOR AUTOMATIC_ACTIVE_SKILL
- 직접 관련된 상쇄 축 1개
= 이름 지정 영웅
```

```text
SIGNATURE_DELTA_COUNT = 1
COMPENSATION_AXIS_COUNT = 1
COMPENSATION_MUST_BE_CAUSALLY_RELATED = TRUE
ALL_OTHER_SOURCE_AXES_INHERITED = TRUE
```

- 원본 병종의 역할·기본 공격·사거리·이동·AI·리그·기본 애니메이션을 우선 재사용한다.
- 고유 자원·궁극기·새 AI·전체 신규 리그·전체 신규 애니메이션은 기본 금지다.
- 여러 스탯 동시 조정·전체 성장 곡선 재설계·공통 고정 세금은 금지한다.
- 원본 병종이 더 나은 대표 상황을 유지한다.

## 5. 기존 main 정본 연결

PR #121에서 승인된 영웅 해금·동병종 바인딩·토큰 변환·전역 단일 활성·Stage 상태·사망 후 재출전·자동 발동·전문화 sidegrade 계약은 계속 유지한다.

## 6. 충돌 해소

- 초기 4명을 최종 출시 전체 로스터 수로 해석하지 않는다.
- 2:2 할당을 맞추기 위해 병종에 맞지 않는 능력을 억지로 부여하지 않는다. 자연스럽게 2:2가 되는 후보 병종을 선정한다.
- 서로 다른 병종이어도 역할이 겹칠 수 있으므로 기능 중복 최소화를 별도 Gate로 검토한다.
- 초기 4명을 완전 신규 유닛으로 제작하지 않는다.
- 인기·서사만으로 후보를 선정하지 않고 제작 가능성과 시스템 검증 가치를 우선한다.

## 7. 구현·검증 경계

```text
CURRENT_PRODUCT = LEGACY_PROTOTYPE
LATEST_APPROVED = DOCUMENTED_NOT_IMPLEMENTED
PRODUCT_CODE_AUTHORITY = NONE
INITIAL_HERO_COUNT = 4
EXACT_ARCHETYPES = PENDING
EXACT_HEROES = PENDING
EXACT_VALUES = PENDING
ASSETS = NOT_CREATED
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
```

## 8. 카운터·병합 규칙

```text
CURRENT_COUNT_SINCE_MERGE = 3_OF_10
NEXT_PREFLIGHT_AT = 10_OF_10
```

- 승인 즉시 GitHub·Sheet에 같은 Decision ID로 반영한다.
- 10번째 승인 뒤 문서·기획 PR이 Green preflight와 blocker 0을 만족하면 별도 승인 대기 없이 병합한다.
- 제품 코드 구현·병합은 별도 계약 대상이다.
