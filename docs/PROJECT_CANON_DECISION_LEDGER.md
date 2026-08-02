# 오멘워드 기획 정본 결정 원장

```yaml
updated_at: 2026-08-02
status: CURRENT_DECISION_LEDGER / ACTIVE_PLANNING_BRANCH
current_recovery_decision: OMW-DEC-20260802-CANON-RECOVERY-V1
current_planning_decision: OMW-DEC-20260802-GAMEPLAY-HERO-UNIQUE-SKILL-UPGRADE-MODEL-V1
current_world_decision: OMW-DEC-20260802-WORLD-VEILSPECIES-PURPOSE-V1
current_operating_decision: OMW-DEC-20260802-GRILL-ME-MERGE-CADENCE-V1
current_main: RESOLVE_FROM_REPOSITORY_DEFAULT_BRANCH
working_branch: gpt/omenward-hero-kit-planning-20260802
current_planning_pr: 129
active_base: 9.4.3
product_code_authority: NONE
sheet_id: 1VLwRtXGDtyj0JFt98wdIOtG6Zqc3wtdfCzSF9Fo6lpw
grill_me_approved_since_last_merge: 5
future_merge_cadence: 10_APPROVED_GRILL_ME_DECISIONS
planning_docs_merge_policy: AUTO_PROCEED_AFTER_GREEN_PREFLIGHT_UNDER_STANDING_USER_AUTHORIZATION
product_code_merge_policy: SEPARATE_CONTRACT_REQUIRED
preflight: NEXT_AT_10_OF_10
next_gate: OMW-DEC-20260802-GAMEPLAY-HERO-FIRST-FIVE-UNIQUE-SKILL-CONCEPTS-V1
```

`current_main`은 저장소 기본 브랜치에서 실행 시점에 해석한다. 이 문서는 현재 승인 Decision과 10건 카운터를 소유한다.

## 1. 상태 언어

```text
USER_APPROVED_PLAN
!= PRODUCT_IMPLEMENTED
!= AUTOMATED_VALIDATED
!= HUMAN_VALIDATED
!= RELEASE_READY
```

## 2. 현재 묶음 Decision 5/10

| Decision ID | 상태 | 결정 | 책임 원본 | 미완료 경계 |
|---|---|---|---|---|
| `OMW-DEC-20260802-GAMEPLAY-HERO-UNIQUE-SKILL-UPGRADE-MODEL-V1` | `USER_APPROVED / ACTIVE_BRANCH_SYNCED / NOT_IMPLEMENTED` | 모든 해금 이름 지정 영웅은 원본 `[영웅]` 등급 기본 성능을 계승하고 고유 자동 사용스킬 하나를 추가하는 제한형 상위호환이며 패시브·강제 상쇄 축은 없다 | `design/APPROVED_OMENWARD_HERO_UNIQUE_SKILL_UPGRADE_MODEL_2026-08-02.md` | 정확 영웅·스킬·trigger·cooldown·VFX/SFX·수치 pending |
| `OMW-DEC-20260802-GAMEPLAY-HERO-INITIAL-ROSTER-ARCHETYPE-SELECTION-V1` | `USER_APPROVED / REFINED_TO_ALL_AUTO_ACTIVE / NOT_IMPLEMENTED` | 초기 5개 병종은 방패병·궁병·사제·마법사·암살자이며 다섯 영웅 모두 고유 자동 사용스킬형이다 | `design/APPROVED_OMENWARD_HERO_INITIAL_ROSTER_ARCHETYPE_SELECTION_2026-08-02.md` | 정확 영웅 이름·스킬 콘셉트·수치·자산 pending |
| `OMW-DEC-20260802-GAMEPLAY-HERO-INITIAL-ROSTER-SCOPE-V1` | `USER_APPROVED / REFINED_TO_FIVE_AUTO_ACTIVE / NOT_IMPLEMENTED` | 초기 검증 로스터는 서로 다른 병종 5종에 영웅 1명씩 총 5명이며 최종 출시 상한이 아니다 | `design/APPROVED_OMENWARD_HERO_INITIAL_ROSTER_SCOPE_2026-08-02.md` | 정확 스킬·자산·simulation pending |
| `OMW-DEC-20260802-GAMEPLAY-HERO-SIGNATURE-DELTA-BALANCE-V1` | `SUPERSEDED_HISTORY / NOT_IMPLEMENTED` | 과거 강제 상쇄 축 sidegrade 결정; 현행 정본에 사용하지 않는다 | `design/APPROVED_OMENWARD_HERO_SIGNATURE_DELTA_BALANCE_2026-08-02.md` | 계보만 유지 |
| `OMW-DEC-20260802-GAMEPLAY-HERO-ABILITY-KIT-STRUCTURE-V1` | `USER_APPROVED / REFINED_TO_UNIQUE_ACTIVE_ONLY / NOT_IMPLEMENTED` | 패시브 선택 구조를 폐기하고 고유 자동 사용스킬 정확히 1개로 고정 | `design/APPROVED_OMENWARD_HERO_ABILITY_KIT_STRUCTURE_2026-08-02.md` | 정확 스킬 pending |

## 3. 현행 영웅 모델

```text
원본 병종 [영웅] 등급 기본 전투 성능
+ 이름·초상·스킨·식별 연출
+ 고유 자동 사용스킬 정확히 1개
= 제한형 상위호환 이름 지정 영웅
```

```text
HERO_POWER_MODEL = CONSTRAINED_UPGRADE
UNIQUE_AUTOMATIC_ACTIVE_SKILL_COUNT = 1_PER_HERO
HERO_EXCLUSIVE_PASSIVE_COUNT = 0
MANDATORY_COMPENSATION_AXIS_COUNT = 0
SOURCE_BASELINE_STATS = INHERITED
GLOBAL_ACTIVE_NAMED_HERO_CAP = 1
```

- 패시브형 이름 지정 영웅은 없다.
- 의무 능력치 하향·강제 상쇄 축은 없다.
- 밸런스는 전역 활성 1명·해금·적격 토큰·비가역 배치·스킬 cooldown/charge·trigger·효과 범위로 통제한다.
- 원본 유닛은 미해금과 다른 이름 지정 영웅 활성 상황에서 계속 필요하다.

## 4. 초기 5명

```text
shield_guard → UNIQUE_AUTOMATIC_ACTIVE_SKILL
archer       → UNIQUE_AUTOMATIC_ACTIVE_SKILL
priest       → UNIQUE_AUTOMATIC_ACTIVE_SKILL
mage         → UNIQUE_AUTOMATIC_ACTIVE_SKILL
assassin     → UNIQUE_AUTOMATIC_ACTIVE_SKILL
```

```text
INITIAL_HERO_COUNT = 5
INITIAL_PASSIVE_COUNT = 0
INITIAL_AUTOMATIC_ACTIVE_SKILL_COUNT = 5
INITIAL_ROSTER_IS_FINAL_RELEASE_CAP = FALSE
```

## 5. 기존 main 정본 연결

PR #121에서 승인된 영웅 해금·동병종 바인딩·토큰 변환·전역 단일 활성·Stage 상태·사망 후 재출전·자동 발동·결정론 계약은 계속 유지한다.

## 6. 충돌 해소

- `패시브 XOR 자동 사용스킬`은 폐기됐다.
- `단일 차이 + 관련 상쇄 축 1개`와 평균 예산 동등 sidegrade 의무는 폐기됐다.
- 이전 5명 패시브 3·자동 스킬 2 분배는 폐기됐다.
- 이름 지정 영웅은 해금 보상으로 원본보다 조금 더 강해야 한다.
- 상위호환은 전역 활성 1명 제한을 제거하는 근거가 아니다.
- 완전 신규 유닛·새 AI·전체 신규 애니메이션 제작은 계속 금지한다.

## 7. 구현·검증 경계

```text
CURRENT_PRODUCT = LEGACY_PROTOTYPE
LATEST_APPROVED = DOCUMENTED_NOT_IMPLEMENTED
PRODUCT_CODE_AUTHORITY = NONE
EXACT_HERO_IDENTITIES = PENDING
EXACT_UNIQUE_SKILLS = PENDING
EXACT_VALUES = PENDING
ASSETS = NOT_CREATED
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
```

## 8. 카운터·병합 규칙

```text
CURRENT_COUNT_SINCE_MERGE = 5_OF_10
NEXT_PREFLIGHT_AT = 10_OF_10
```

- 승인 즉시 GitHub·Sheet에 같은 Decision ID로 반영한다.
- 10번째 승인 뒤 문서·기획 PR이 Green preflight와 blocker 0을 만족하면 별도 승인 대기 없이 병합한다.
- 제품 코드 구현·병합은 별도 계약 대상이다.
