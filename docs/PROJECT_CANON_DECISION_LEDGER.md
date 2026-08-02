# 오멘워드 기획 정본 결정 원장

```yaml
updated_at: 2026-08-03
status: CURRENT_DECISION_LEDGER / ACTIVE_PLANNING_BRANCH
current_recovery_decision: OMW-DEC-20260802-CANON-RECOVERY-V1
current_planning_decision: OMW-DEC-20260803-GAMEPLAY-HERO-FIRST-FIVE-UNIQUE-SKILL-2-CONCEPTS-V1
current_world_decision: OMW-DEC-20260802-WORLD-VEILSPECIES-PURPOSE-V1
current_operating_decision: OMW-DEC-20260802-GRILL-ME-MERGE-CADENCE-V1
current_benchmark_policy: OMW-PROC-20260803-GRILL-ME-BENCHMARK-PRODUCTION-COMPARISON-V1
current_main: RESOLVE_FROM_REPOSITORY_DEFAULT_BRANCH
working_branch: gpt/omenward-hero-kit-planning-20260802
current_planning_pr: 129
active_base: 9.4.3
product_code_authority: NONE
sheet_id: 1VLwRtXGDtyj0JFt98wdIOtG6Zqc3wtdfCzSF9Fo6lpw
grill_me_approved_since_last_merge: 7
future_merge_cadence: 10_APPROVED_GRILL_ME_DECISIONS
planning_docs_merge_policy: AUTO_PROCEED_AFTER_GREEN_PREFLIGHT_UNDER_STANDING_USER_AUTHORIZATION
product_code_merge_policy: SEPARATE_CONTRACT_REQUIRED
preflight: NEXT_AT_10_OF_10
next_gate: OMW-DEC-20260803-GAMEPLAY-HERO-UNIQUE-SKILL-2-COOLDOWN-CHARGE-AND-FAILURE-POLICY-V1
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

## 2. 현재 묶음 Decision 7/10

| Decision ID | 상태 | 결정 | 책임 원본 | 미완료 경계 |
|---|---|---|---|---|
| `OMW-DEC-20260803-GAMEPLAY-HERO-FIRST-FIVE-UNIQUE-SKILL-2-CONCEPTS-V1` | `USER_APPROVED / ACTIVE_BRANCH_SYNCED / NOT_IMPLEMENTED` | 방패병 `불퇴의 성벽`, 궁병 `천공 소거`, 사제 `생명의 서약`, 마법사 `메테오`, 암살자 `그림자 분신`을 초기 5명 고유 2스킬 전술 콘셉트로 승인 | `design/APPROVED_OMENWARD_FIRST_FIVE_UNIQUE_SKILL_2_CONCEPTS_2026-08-03.md` | exact trigger·cooldown·duration·value·final name·asset pending |
| `OMW-DEC-20260802-GAMEPLAY-HERO-GRADE-SLOT-AND-UNLOCKED-SKILL-REPLACEMENT-V1` | `USER_APPROVED / ACTIVE_BRANCH_SYNCED / NOT_IMPLEMENTED` | 표준·해금 여부와 관계없이 `[영웅]·[전설]` 등급을 합쳐 전장 전체 최대 1명; 해금 영웅은 표준 2스킬을 고유 2스킬로 교체; 향후 해금 전설은 3스킬을 고유 3스킬로 교체 | `design/APPROVED_OMENWARD_HERO_GRADE_SLOT_AND_UNLOCKED_SKILL_REPLACEMENT_2026-08-02.md` | 정확 수치·미래 해금 전설 상세 pending |
| `OMW-DEC-20260802-GAMEPLAY-HERO-UNIQUE-SKILL-UPGRADE-MODEL-V1` | `USER_APPROVED / REFINED_TO_SKILL_2_REPLACEMENT / NOT_IMPLEMENTED` | 해금 영웅은 표준 영웅보다 강하고 표준 전설보다 약하며 추가 스킬이 아니라 고유 2스킬을 사용 | `design/APPROVED_OMENWARD_HERO_UNIQUE_SKILL_UPGRADE_MODEL_2026-08-02.md` | exact value pending |
| `OMW-DEC-20260802-GAMEPLAY-HERO-INITIAL-ROSTER-ARCHETYPE-SELECTION-V1` | `USER_APPROVED / REFINED_TO_UNIQUE_SKILL_2 / NOT_IMPLEMENTED` | 초기 5개 병종은 방패병·궁병·사제·마법사·암살자 | `design/APPROVED_OMENWARD_HERO_INITIAL_ROSTER_ARCHETYPE_SELECTION_2026-08-02.md` | hero identity·asset pending |
| `OMW-DEC-20260802-GAMEPLAY-HERO-INITIAL-ROSTER-SCOPE-V1` | `USER_APPROVED / REFINED_TO_FIVE_UNIQUE_SKILL_2 / NOT_IMPLEMENTED` | 초기 검증 로스터 5명, 최종 출시 상한 아님 | `design/APPROVED_OMENWARD_HERO_INITIAL_ROSTER_SCOPE_2026-08-02.md` | simulation·production pending |
| `OMW-DEC-20260802-GAMEPLAY-HERO-ABILITY-KIT-STRUCTURE-V1` | `USER_APPROVED / REFINED_TO_UNIQUE_SKILL_2 / NOT_IMPLEMENTED` | 패시브 선택 구조 폐기, 해금 영웅의 고유 스킬은 2스킬 슬롯 소유 | `design/APPROVED_OMENWARD_HERO_ABILITY_KIT_STRUCTURE_2026-08-02.md` | exact value pending |
| `OMW-DEC-20260802-GAMEPLAY-HERO-SIGNATURE-DELTA-BALANCE-V1` | `SUPERSEDED_HISTORY / NOT_IMPLEMENTED` | 과거 강제 상쇄 축 sidegrade 결정 | `design/APPROVED_OMENWARD_HERO_SIGNATURE_DELTA_BALANCE_2026-08-02.md` | 계보만 유지 |

## 3. 비카운트 운영 정책

| Process ID | 상태 | 정책 | 책임 원본 |
|---|---|---|---|
| `OMW-PROC-20260803-GRILL-ME-BENCHMARK-PRODUCTION-COMPARISON-V1` | `ACTIVE_STANDING_POLICY` | 앞으로 모든 Grill Me 질문과 승인 작업에 공식 상용 게임 벤치마크, OMENWARD 차이, 구현·AI·animation·VFX·UI·save/load·determinism·QA 비교, 적대적 검토와 권장안을 포함 | `process/APPROVED_GRILL_ME_BENCHMARK_AND_PRODUCTION_COMPARISON_POLICY_2026-08-03.md` |

이 운영 정책은 제품 Grill Me 카운터에 포함하지 않는다.

## 4. 표준 등급·해금 변형

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

## 5. 전역 고등급 슬롯

```text
ACTIVE_UNIT_COUNT_WHERE_GRADE_IN(HERO, LEGENDARY) <= 1
```

- 표준 영웅·해금 영웅·표준 전설·향후 해금 전설을 모두 합산한다.
- 상·중·하 전선 전체가 하나의 슬롯을 공유한다.
- 제한은 획득이 아니라 전장 배치에 적용한다.
- 슬롯 충돌 토큰은 보관·판매 가능하다.
- 자동 삭제·자동 교체·수동 퇴각·수동 교대는 금지한다.
- 과거 `named Hero만 1명`과 `다른 named Hero 활성 중 표준 Hero 배치 가능` 표현은 현행 정본이 아니다.
- 같은 Stage의 재전설 결과는 즉시 영웅 유닛 2명이 아니라 같은 계열 영웅 등급 보상 토큰 2개다.

## 6. 초기 5명 고유 2스킬

```text
shield_guard / 방패병 → 불퇴의 성벽
archer / 궁병         → 천공 소거
priest / 사제         → 생명의 서약
mage / 마법사         → 메테오
assassin / 암살자     → 그림자 분신
```

핵심 계약:

- `불퇴의 성벽`: 새 지형 없이 짧은 전열 유지와 피해 흡수.
- `천공 소거`: 같은 전선의 유효 비행 표적 동시 일제사격.
- `생명의 서약`: 회복 없이 짧은 체력 하한 보호. `min(current_hp_at_cast, configured_floor)`.
- `메테오`: deterministic 적 밀집 지점에 예고 후 단발 지연 낙하.
- `그림자 분신`: 독립 AI 없이 원본 표적·기본 공격 일부를 복제하는 owner-bound proxy 1체.

공통 금지:

- 다른 전선 직접 영향.
- 표준 2스킬과 동시 보유.
- 사제의 회복·부활·건물 보호.
- 메테오의 즉발·전역·기본 다중 낙하·기본 장판.
- 분신의 독립 target/pathfinding·스킬·CC·보상 생성·고등급 슬롯 점유.
- 방벽의 영구 지형·navmesh 변경.

## 7. 자동 발동

```text
COOLDOWN
→ READY_WAITING_FOR_VALID_CONDITION
→ 유효 조건·대상·priority·tie-break
→ CAST_COMMIT
→ 효과·VFX/SFX·로그
→ COOLDOWN
```

유효 조건이 없으면 준비 상태를 보존하고 cooldown을 낭비하지 않는다. 정확 cooldown·충전·발동 실패 정책은 다음 Decision에서 확정한다.

## 8. 핵심 시스템 적합성

영웅 이상 단일 슬롯은 희귀 등급을 누적 전력이 아니라 `어느 전선에 최고 전력을 비가역 커밋할지` 판단하는 전략 자원으로 만든다. 해금 고유 2스킬은 건설→룰렛→희귀 보상→전선 역전의 감정 고점을 강화한다.

주요 위험:

- 살아 있는 영웅이 후속 전설 당첨의 즉시 배치를 막는 좌절.
- 영웅 결과 빈도와 장기 생존으로 인한 보관함 압력.
- 고유 2스킬이 표준 전설 전체 키트를 침범하는 파워 역전.
- 한 고등급 유닛이 세 전선의 유일한 승리 조건이 되는 현상.
- 체력 하한이 광역 무적으로 변하는 현상.
- 메테오가 즉발 또는 지나치게 빗나가 대응성과 보상감 중 하나를 잃는 현상.
- 분신이 독립 유닛 시스템으로 팽창하는 현상.

상세 검토는 `design/APPROVED_OMENWARD_FIRST_FIVE_UNIQUE_SKILL_2_CONCEPTS_2026-08-03.md`, `reviews/ADVERSARIAL_HERO_GRADE_SLOT_AND_CORE_FIT_REVIEW_2026-08-02.md`가 소유한다.

## 9. 구현·검증 경계

```text
CURRENT_PRODUCT = LEGACY_PROTOTYPE
LATEST_APPROVED = DOCUMENTED_NOT_IMPLEMENTED
PRODUCT_CODE_AUTHORITY = NONE
EXACT_HERO_IDENTITIES = PENDING
UNIQUE_SKILL_2_CONCEPTS = APPROVED
EXACT_TRIGGER_THRESHOLDS = PENDING
EXACT_COOLDOWNS = PENDING
EXACT_DURATIONS_AND_VALUES = PENDING
FINAL_DISPLAY_NAMES = PENDING
FUTURE_NAMED_LEGENDARY = NOT_NOW
REPEAT_LEGENDARY_STORAGE_OVERFLOW_POLICY = PENDING
ASSETS = NOT_CREATED
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
```

## 10. 카운터·병합 규칙

```text
CURRENT_COUNT_SINCE_MERGE = 7_OF_10
NEXT_PREFLIGHT_AT = 10_OF_10
```

- 승인 즉시 GitHub·Sheet에 같은 Decision ID로 반영한다.
- 10번째 승인 뒤 문서·기획 PR이 Green preflight와 blocker 0을 만족하면 별도 승인 대기 없이 병합한다.
- 제품 코드 구현·병합은 별도 계약 대상이다.
