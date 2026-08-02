# 오멘워드 기획 정본 결정 원장

```yaml
updated_at: 2026-08-03
status: CURRENT_DECISION_LEDGER / ACTIVE_PLANNING_BRANCH
current_recovery_decision: OMW-DEC-20260802-CANON-RECOVERY-V1
current_planning_decision: OMW-DEC-20260803-GAMEPLAY-HERO-UNIQUE-SKILL-2-COOLDOWN-CHARGE-AND-FAILURE-POLICY-V1
current_world_decision: OMW-DEC-20260802-WORLD-VEILSPECIES-PURPOSE-V1
current_operating_decision: OMW-DEC-20260802-GRILL-ME-MERGE-CADENCE-V1
current_benchmark_policy: OMW-PROC-20260803-GRILL-ME-BENCHMARK-PRODUCTION-COMPARISON-V1
current_main: RESOLVE_FROM_REPOSITORY_DEFAULT_BRANCH
working_branch: gpt/omenward-hero-kit-planning-20260802
current_planning_pr: 129
active_base: 9.4.3
product_code_authority: NONE
sheet_id: 1VLwRtXGDtyj0JFt98wdIOtG6Zqc3wtdfCzSF9Fo6lpw
grill_me_approved_since_last_merge: 8
future_merge_cadence: 10_APPROVED_GRILL_ME_DECISIONS
planning_docs_merge_policy: AUTO_PROCEED_AFTER_GREEN_PREFLIGHT_UNDER_STANDING_USER_AUTHORIZATION
product_code_merge_policy: SEPARATE_CONTRACT_REQUIRED
preflight: NEXT_AT_10_OF_10
next_gate: OMW-DEC-20260803-GAMEPLAY-HERO-UNIQUE-SKILL-2-TIMER-PERSISTENCE-AND-STAGE-BOUNDARY-POLICY-V1
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

## 2. 현재 묶음 Decision 8/10

| Decision ID | 상태 | 결정 | 책임 원본 | 미완료 경계 |
|---|---|---|---|---|
| `OMW-DEC-20260803-GAMEPLAY-HERO-UNIQUE-SKILL-2-COOLDOWN-CHARGE-AND-FAILURE-POLICY-V1` | `USER_APPROVED / ACTIVE_BRANCH_SYNCED / NOT_IMPLEMENTED` | 단일 cooldown, READY 1회, charge 없음, 배치 후 INITIAL_WARMUP, precommit 실패 시 READY 복귀, 효과 종료 뒤 cooldown 시작 | `design/APPROVED_OMENWARD_HERO_UNIQUE_SKILL_2_COOLDOWN_CHARGE_AND_FAILURE_POLICY_2026-08-03.md` | exact warmup·per-skill cooldown·Stage/maintenance timer policy pending |
| `OMW-DEC-20260803-GAMEPLAY-HERO-FIRST-FIVE-UNIQUE-SKILL-2-CONCEPTS-V1` | `USER_APPROVED / ACTIVE_BRANCH_SYNCED / NOT_IMPLEMENTED` | 방패병 `불퇴의 성벽`, 궁병 `천공 소거`, 사제 `생명의 서약`, 마법사 `메테오`, 암살자 `그림자 분신` 승인 | `design/APPROVED_OMENWARD_FIRST_FIVE_UNIQUE_SKILL_2_CONCEPTS_2026-08-03.md` | exact trigger·duration·value·final name·asset pending |
| `OMW-DEC-20260802-GAMEPLAY-HERO-GRADE-SLOT-AND-UNLOCKED-SKILL-REPLACEMENT-V1` | `USER_APPROVED / ACTIVE_BRANCH_SYNCED / NOT_IMPLEMENTED` | 표준·해금 여부와 관계없이 `[영웅]·[전설]` 등급 전장 전체 최대 1명; 해금 영웅은 표준 2스킬을 고유 2스킬로 교체 | `design/APPROVED_OMENWARD_HERO_GRADE_SLOT_AND_UNLOCKED_SKILL_REPLACEMENT_2026-08-02.md` | 정확 수치·미래 해금 전설 상세 pending |
| `OMW-DEC-20260802-GAMEPLAY-HERO-UNIQUE-SKILL-UPGRADE-MODEL-V1` | `USER_APPROVED / REFINED_TO_SKILL_2_REPLACEMENT / NOT_IMPLEMENTED` | 해금 영웅은 표준 영웅보다 강하고 표준 전설보다 약함 | `design/APPROVED_OMENWARD_HERO_UNIQUE_SKILL_UPGRADE_MODEL_2026-08-02.md` | exact value pending |
| `OMW-DEC-20260802-GAMEPLAY-HERO-INITIAL-ROSTER-ARCHETYPE-SELECTION-V1` | `USER_APPROVED / REFINED_TO_UNIQUE_SKILL_2 / NOT_IMPLEMENTED` | 초기 병종은 방패병·궁병·사제·마법사·암살자 | `design/APPROVED_OMENWARD_HERO_INITIAL_ROSTER_ARCHETYPE_SELECTION_2026-08-02.md` | identity·asset pending |
| `OMW-DEC-20260802-GAMEPLAY-HERO-INITIAL-ROSTER-SCOPE-V1` | `USER_APPROVED / REFINED_TO_FIVE_UNIQUE_SKILL_2 / NOT_IMPLEMENTED` | 초기 검증 로스터 5명, 최종 출시 상한 아님 | `design/APPROVED_OMENWARD_HERO_INITIAL_ROSTER_SCOPE_2026-08-02.md` | simulation·production pending |
| `OMW-DEC-20260802-GAMEPLAY-HERO-ABILITY-KIT-STRUCTURE-V1` | `USER_APPROVED / REFINED_TO_UNIQUE_SKILL_2 / NOT_IMPLEMENTED` | 해금 영웅의 고유 스킬은 2스킬 슬롯 소유 | `design/APPROVED_OMENWARD_HERO_ABILITY_KIT_STRUCTURE_2026-08-02.md` | exact value pending |
| `OMW-DEC-20260802-GAMEPLAY-HERO-SIGNATURE-DELTA-BALANCE-V1` | `SUPERSEDED_HISTORY / NOT_IMPLEMENTED` | 과거 강제 상쇄 축 sidegrade 결정 | `design/APPROVED_OMENWARD_HERO_SIGNATURE_DELTA_BALANCE_2026-08-02.md` | 계보만 유지 |

## 3. 비카운트 운영 정책

| Process ID | 상태 | 정책 | 책임 원본 |
|---|---|---|---|
| `OMW-PROC-20260803-GRILL-ME-BENCHMARK-PRODUCTION-COMPARISON-V1` | `ACTIVE_STANDING_POLICY` | 모든 Grill Me에 공식 벤치마크, OMENWARD 차이, 구현·AI·animation·VFX·UI·save/load·determinism·QA 비교, 적대적 검토와 권장안 포함 | `process/APPROVED_GRILL_ME_BENCHMARK_AND_PRODUCTION_COMPARISON_POLICY_2026-08-03.md` |

이 운영 정책은 제품 Grill Me 카운터에 포함하지 않는다.

## 4. 등급·전역 슬롯

```text
[일반] = 1스킬
[엘리트] = 강화된 1스킬
[영웅] = 강화된 1스킬 + 표준 2스킬
해금 이름 지정 [영웅] = 강화된 1스킬 + 고유 2스킬
[전설] = 강화된 1스킬 + 강화된 표준 2스킬 + 표준 3스킬
```

```text
STANDARD_HERO_POWER < UNLOCKED_NAMED_HERO_POWER < STANDARD_LEGENDARY_POWER
ACTIVE_UNIT_COUNT_WHERE_GRADE_IN(HERO, LEGENDARY) <= 1
```

- 표준 영웅·해금 영웅·표준 전설·향후 해금 전설 모두 전역 슬롯 하나를 공유한다.
- 제한은 획득이 아니라 전장 배치에 적용한다.
- 슬롯 충돌 토큰은 보관·판매 가능하다.
- 같은 Stage의 재전설 결과는 동일 계열 영웅 등급 보상 토큰 2개다.

## 5. 초기 5명 고유 2스킬

```text
shield_guard / 방패병 → 불퇴의 성벽
archer / 궁병         → 천공 소거
priest / 사제         → 생명의 서약
mage / 마법사         → 메테오
assassin / 암살자     → 그림자 분신
```

- `불퇴의 성벽`: 새 지형 없이 피해 예산을 흡수하는 짧은 전열 방벽.
- `천공 소거`: 같은 전선 유효 비행 표적 일제사격.
- `생명의 서약`: 회복 없이 짧은 체력 하한 보호.
- `메테오`: 적 밀집 지점에 예고 후 단발 지연 낙하.
- `그림자 분신`: 독립 AI 없이 기본 공격 일부를 복제하는 owner-bound proxy 1체.

## 6. 공통 timer·charge·실패 정책

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

- 새 배치 뒤 첫 발동 전에 initial warmup을 거친다.
- 유효 조건이 없으면 READY를 보존한다.
- precommit 무효화는 READY 복귀·cooldown 소비 0이다.
- 천공 소거·메테오는 commit 뒤 단발 사건을 한 번 해결한다.
- 불퇴의 성벽·생명의 서약·그림자 분신은 owner-bound 지속형이며 시전자 제거 시 종료한다.
- cooldown은 각 능력의 해결 또는 지속효과 종료 뒤 시작한다.
- save/load·Retry로 warmup·cooldown·target·READY를 재굴림하거나 복제할 수 없다.

## 7. 핵심 시스템 적합성·위험

고등급 슬롯과 자동 고유 스킬은 `희귀 병력을 어느 전선에 비가역 커밋할지` 판단을 강화한다. 단일 cooldown과 READY 1회는 발동 원인을 설명하면서 별도 영웅 자원·다중 charge·스킬별 상태 머신을 피한다.

주요 위험:

- warmup이 너무 짧아 배치 즉시 폭발하거나 너무 길어 해금 보상이 죽는 것.
- active effect 중 cooldown이 흘러 상시 유지되는 것.
- save/load·Retry·Stage 전환으로 timer가 초기화되는 것.
- commit 뒤 시전자 사망 처리의 불일치.
- READY 대기 이유와 cooldown이 UI에서 구분되지 않는 것.
- Stage·정비시간 timer 정책이 아직 미확정인 것.

## 8. 구현·검증 경계

```text
CURRENT_PRODUCT = LEGACY_PROTOTYPE
LATEST_APPROVED = DOCUMENTED_NOT_IMPLEMENTED
PRODUCT_CODE_AUTHORITY = NONE
UNIQUE_SKILL_2_CONCEPTS = APPROVED
COMMON_STATE_MACHINE = APPROVED
SINGLE_READY_STORAGE = APPROVED
CHARGE_ACCUMULATION = FORBIDDEN
INITIAL_WARMUP = APPROVED
EXACT_WARMUP_SECONDS = PENDING
EXACT_PER_SKILL_COOLDOWN_SECONDS = PENDING
STAGE_AND_MAINTENANCE_TIMER_POLICY = PENDING
EXACT_TRIGGER_THRESHOLDS = PENDING
EXACT_DURATIONS_AND_VALUES = PENDING
ASSETS = NOT_CREATED
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
```

## 9. 카운터·병합 규칙

```text
CURRENT_COUNT_SINCE_MERGE = 8_OF_10
NEXT_PREFLIGHT_AT = 10_OF_10
```

- 승인 즉시 GitHub·Sheet에 같은 Decision ID로 반영한다.
- 10번째 승인 뒤 문서·기획 PR이 Green preflight와 blocker 0을 만족하면 별도 승인 대기 없이 병합한다.
- 제품 코드 구현·병합은 별도 계약 대상이다.
