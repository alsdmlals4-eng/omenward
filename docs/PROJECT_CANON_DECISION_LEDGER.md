# 오멘워드 기획 정본 결정 원장

```yaml
updated_at: 2026-08-02
status: CURRENT_DECISION_LEDGER / ACTIVE_PLANNING_BRANCH
current_recovery_decision: OMW-DEC-20260802-CANON-RECOVERY-V1
current_planning_decision: OMW-DEC-20260802-GAMEPLAY-HERO-GRADE-SLOT-AND-UNLOCKED-SKILL-REPLACEMENT-V1
current_world_decision: OMW-DEC-20260802-WORLD-VEILSPECIES-PURPOSE-V1
current_operating_decision: OMW-DEC-20260802-GRILL-ME-MERGE-CADENCE-V1
current_main: RESOLVE_FROM_REPOSITORY_DEFAULT_BRANCH
working_branch: gpt/omenward-hero-kit-planning-20260802
current_planning_pr: 129
active_base: 9.4.3
product_code_authority: NONE
sheet_id: 1VLwRtXGDtyj0JFt98wdIOtG6Zqc3wtdfCzSF9Fo6lpw
grill_me_approved_since_last_merge: 6
future_merge_cadence: 10_APPROVED_GRILL_ME_DECISIONS
planning_docs_merge_policy: AUTO_PROCEED_AFTER_GREEN_PREFLIGHT_UNDER_STANDING_USER_AUTHORIZATION
product_code_merge_policy: SEPARATE_CONTRACT_REQUIRED
preflight: NEXT_AT_10_OF_10
next_gate: OMW-DEC-20260802-GAMEPLAY-HERO-FIRST-FIVE-UNIQUE-SKILL-2-CONCEPTS-V1
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

## 2. 현재 묶음 Decision 6/10

| Decision ID | 상태 | 결정 | 책임 원본 | 미완료 경계 |
|---|---|---|---|---|
| `OMW-DEC-20260802-GAMEPLAY-HERO-GRADE-SLOT-AND-UNLOCKED-SKILL-REPLACEMENT-V1` | `USER_APPROVED / ACTIVE_BRANCH_SYNCED / NOT_IMPLEMENTED` | 표준·해금 여부와 관계없이 `[영웅]·[전설]` 등급을 합쳐 전장 전체 최대 1명; 해금 영웅은 표준 2스킬을 고유 2스킬로 교체; 향후 해금 전설은 3스킬을 고유 3스킬로 교체 | `design/APPROVED_OMENWARD_HERO_GRADE_SLOT_AND_UNLOCKED_SKILL_REPLACEMENT_2026-08-02.md` | 초기 5명 고유 2스킬·정확 수치·미래 해금 전설 상세 pending |
| `OMW-DEC-20260802-GAMEPLAY-HERO-UNIQUE-SKILL-UPGRADE-MODEL-V1` | `USER_APPROVED / REFINED_TO_SKILL_2_REPLACEMENT / NOT_IMPLEMENTED` | 해금 영웅은 표준 영웅보다 강하고 표준 전설보다 약하며 추가 스킬이 아니라 고유 2스킬을 사용 | `design/APPROVED_OMENWARD_HERO_UNIQUE_SKILL_UPGRADE_MODEL_2026-08-02.md` | 정확 스킬·수치 pending |
| `OMW-DEC-20260802-GAMEPLAY-HERO-INITIAL-ROSTER-ARCHETYPE-SELECTION-V1` | `USER_APPROVED / REFINED_TO_UNIQUE_SKILL_2 / NOT_IMPLEMENTED` | 초기 5개 병종은 방패병·궁병·사제·마법사·암살자 | `design/APPROVED_OMENWARD_HERO_INITIAL_ROSTER_ARCHETYPE_SELECTION_2026-08-02.md` | 이름·스킬·자산 pending |
| `OMW-DEC-20260802-GAMEPLAY-HERO-INITIAL-ROSTER-SCOPE-V1` | `USER_APPROVED / REFINED_TO_FIVE_UNIQUE_SKILL_2 / NOT_IMPLEMENTED` | 초기 검증 로스터 5명, 최종 출시 상한 아님 | `design/APPROVED_OMENWARD_HERO_INITIAL_ROSTER_SCOPE_2026-08-02.md` | simulation·production pending |
| `OMW-DEC-20260802-GAMEPLAY-HERO-ABILITY-KIT-STRUCTURE-V1` | `USER_APPROVED / REFINED_TO_UNIQUE_SKILL_2 / NOT_IMPLEMENTED` | 패시브 선택 구조 폐기, 해금 영웅의 고유 스킬은 2스킬 슬롯 소유 | `design/APPROVED_OMENWARD_HERO_ABILITY_KIT_STRUCTURE_2026-08-02.md` | 정확 스킬 pending |
| `OMW-DEC-20260802-GAMEPLAY-HERO-SIGNATURE-DELTA-BALANCE-V1` | `SUPERSEDED_HISTORY / NOT_IMPLEMENTED` | 과거 강제 상쇄 축 sidegrade 결정 | `design/APPROVED_OMENWARD_HERO_SIGNATURE_DELTA_BALANCE_2026-08-02.md` | 계보만 유지 |

## 3. 표준 등급·해금 변형

```text
[일반] = 1스킬
[엘리트] = 강화된 1스킬
[영웅] = 강화된 1스킬 + 표준 2스킬
해금 이름 지정 [영웅] = 강화된 1스킬 + 고유 2스킬
[전설] = 강화된 1스킬 + 강화된 표준 2스킬 + 표준 3스킬
향후 해금 이름 지정 [전설] = 강화된 1스킬 + 강화된 표준 2스킬 + 고유 3스킬
```

```text
STANDARD_HERO_POWER < UNLOCKED_NAMED_HERO_POWER < STANDARD_LEGENDARY_POWER
FUTURE_NAMED_LEGENDARY_IMPLEMENTATION = NOT_NOW
```

## 4. 전역 고등급 슬롯

```text
ACTIVE_UNIT_COUNT_WHERE_GRADE_IN(HERO, LEGENDARY) <= 1
```

- 표준 영웅·해금 영웅·표준 전설·향후 해금 전설을 모두 합산한다.
- 상·중·하 전선 전체가 하나의 슬롯을 공유한다.
- 제한은 획득이 아니라 전장 배치에 적용한다.
- 슬롯 충돌 토큰은 보관·판매 가능하다.
- 자동 삭제·자동 교체·수동 퇴각·수동 교대는 금지한다.
- 과거 `named Hero만 1명`과 `다른 named Hero 활성 중 표준 Hero 배치 가능` 표현은 현행 정본이 아니다.

## 5. 초기 5명·자동 발동

```text
shield_guard / archer / priest / mage / assassin
→ 각 병종 해금 이름 지정 영웅 1명
→ 고유 2스킬 1개
```

```text
COOLDOWN
→ READY_WAITING_FOR_VALID_CONDITION
→ 유효 조건·대상·priority·tie-break
→ CAST_COMMIT
→ 효과·VFX/SFX·로그
→ COOLDOWN
```

유효 조건이 없으면 준비 상태를 보존하고 cooldown을 낭비하지 않는다.

## 6. 핵심 시스템 적합성

영웅 이상 단일 슬롯은 희귀 등급을 누적 전력이 아니라 `어느 전선에 최고 전력을 비가역 커밋할지` 판단하는 전략 자원으로 만든다. 해금 고유 2스킬은 건설→룰렛→희귀 보상→전선 역전의 감정 고점을 강화한다.

주요 위험:

- 살아 있는 영웅이 후속 전설 당첨의 즉시 배치를 막는 좌절.
- 영웅 결과 빈도와 장기 생존으로 인한 보관함 압력.
- 고유 2스킬이 표준 전설 전체 키트를 침범하는 파워 역전.
- 한 고등급 유닛이 세 전선의 유일한 승리 조건이 되는 현상.

상세 검토는 `reviews/ADVERSARIAL_HERO_GRADE_SLOT_AND_CORE_FIT_REVIEW_2026-08-02.md`가 소유한다.

## 7. 구현·검증 경계

```text
CURRENT_PRODUCT = LEGACY_PROTOTYPE
LATEST_APPROVED = DOCUMENTED_NOT_IMPLEMENTED
PRODUCT_CODE_AUTHORITY = NONE
EXACT_HERO_IDENTITIES = PENDING
EXACT_UNIQUE_SKILL_2 = PENDING
FUTURE_NAMED_LEGENDARY = NOT_NOW
EXACT_VALUES = PENDING
ASSETS = NOT_CREATED
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
```

## 8. 카운터·병합 규칙

```text
CURRENT_COUNT_SINCE_MERGE = 6_OF_10
NEXT_PREFLIGHT_AT = 10_OF_10
```

- 승인 즉시 GitHub·Sheet에 같은 Decision ID로 반영한다.
- 10번째 승인 뒤 문서·기획 PR이 Green preflight와 blocker 0을 만족하면 별도 승인 대기 없이 병합한다.
- 제품 코드 구현·병합은 별도 계약 대상이다.
