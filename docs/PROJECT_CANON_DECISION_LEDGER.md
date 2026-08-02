# 오멘워드 기획 정본 결정 원장

```yaml
updated_at: 2026-08-03
status: CURRENT_DECISION_LEDGER / ACTIVE_PLANNING_BRANCH
current_recovery_decision: OMW-DEC-20260802-CANON-RECOVERY-V1
current_planning_decision: OMW-DEC-20260803-GAMEPLAY-HERO-UNIQUE-SKILL-2-TIMER-PERSISTENCE-AND-STAGE-BOUNDARY-POLICY-V1
current_world_decision: OMW-DEC-20260802-WORLD-VEILSPECIES-PURPOSE-V1
current_operating_decision: OMW-DEC-20260802-GRILL-ME-MERGE-CADENCE-V1
current_benchmark_policy: OMW-PROC-20260803-GRILL-ME-BENCHMARK-PRODUCTION-COMPARISON-V1
current_main: RESOLVE_FROM_REPOSITORY_DEFAULT_BRANCH
working_branch: gpt/omenward-hero-kit-planning-20260802
current_planning_pr: 129
active_base: 9.4.3
product_code_authority: NONE
sheet_id: 1VLwRtXGDtyj0JFt98wdIOtG6Zqc3wtdfCzSF9Fo6lpw
grill_me_approved_since_last_merge: 9
future_merge_cadence: 10_APPROVED_GRILL_ME_DECISIONS
planning_docs_merge_policy: AUTO_PROCEED_AFTER_GREEN_PREFLIGHT_UNDER_STANDING_USER_AUTHORIZATION
product_code_merge_policy: SEPARATE_CONTRACT_REQUIRED
preflight: NEXT_AT_10_OF_10
next_gate: OMW-DEC-20260803-GAMEPLAY-HERO-UNIQUE-SKILL-2-TRIGGER-TARGET-AND-POWER-BUDGET-VALIDATION-V1
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

## 2. 현재 묶음 Decision 9/10

| Decision ID | 상태 | 결정 | 책임 원본 | 미완료 경계 |
|---|---|---|---|---|
| `OMW-DEC-20260803-GAMEPLAY-HERO-UNIQUE-SKILL-2-TIMER-PERSISTENCE-AND-STAGE-BOUNDARY-POLICY-V1` | `USER_APPROVED / ACTIVE_BRANCH_SYNCED / NOT_IMPLEMENTED` | 전투 clock에서만 warmup·cooldown 진행, 정비시간 pause, READY·잔여시간 carry, active·미해결 commit Stage carry 금지 | `design/APPROVED_OMENWARD_HERO_UNIQUE_SKILL_2_TIMER_PERSISTENCE_AND_STAGE_BOUNDARY_POLICY_2026-08-03.md` | exact seconds·trigger·simulation·runtime·human pending |
| `OMW-DEC-20260803-GAMEPLAY-HERO-UNIQUE-SKILL-2-COOLDOWN-CHARGE-AND-FAILURE-POLICY-V1` | `USER_APPROVED / REFINED_BY_TIMER_STAGE_POLICY / NOT_IMPLEMENTED` | 단일 cooldown, READY 1회, charge·mana 없음, initial warmup, precommit 실패 무소모, 효과 종료 뒤 cooldown | `design/APPROVED_OMENWARD_HERO_UNIQUE_SKILL_2_COOLDOWN_CHARGE_AND_FAILURE_POLICY_2026-08-03.md` | exact warmup·cooldown pending |
| `OMW-DEC-20260803-GAMEPLAY-HERO-FIRST-FIVE-UNIQUE-SKILL-2-CONCEPTS-V1` | `USER_APPROVED / ACTIVE_BRANCH_SYNCED / NOT_IMPLEMENTED` | 불퇴의 성벽·천공 소거·생명의 서약·메테오·그림자 분신 | `design/APPROVED_OMENWARD_FIRST_FIVE_UNIQUE_SKILL_2_CONCEPTS_2026-08-03.md` | exact trigger·duration·value·asset pending |
| `OMW-DEC-20260802-GAMEPLAY-HERO-GRADE-SLOT-AND-UNLOCKED-SKILL-REPLACEMENT-V1` | `USER_APPROVED / ACTIVE_BRANCH_SYNCED / NOT_IMPLEMENTED` | `[영웅]·[전설]` 전장 전체 최대 1명; 해금 영웅 고유 2스킬 교체; 미래 해금 전설 고유 3스킬 교체 | `design/APPROVED_OMENWARD_HERO_GRADE_SLOT_AND_UNLOCKED_SKILL_REPLACEMENT_2026-08-02.md` | 미래 해금 전설 상세 pending |
| `OMW-DEC-20260802-GAMEPLAY-HERO-UNIQUE-SKILL-UPGRADE-MODEL-V1` | `USER_APPROVED / REFINED_TO_SKILL_2_REPLACEMENT / NOT_IMPLEMENTED` | 표준 영웅보다 강하고 표준 전설보다 약한 해금 영웅 | `design/APPROVED_OMENWARD_HERO_UNIQUE_SKILL_UPGRADE_MODEL_2026-08-02.md` | exact values pending |
| `OMW-DEC-20260802-GAMEPLAY-HERO-INITIAL-ROSTER-ARCHETYPE-SELECTION-V1` | `USER_APPROVED / REFINED_TO_UNIQUE_SKILL_2 / NOT_IMPLEMENTED` | 방패병·궁병·사제·마법사·암살자 | `design/APPROVED_OMENWARD_HERO_INITIAL_ROSTER_ARCHETYPE_SELECTION_2026-08-02.md` | identities·assets pending |
| `OMW-DEC-20260802-GAMEPLAY-HERO-INITIAL-ROSTER-SCOPE-V1` | `USER_APPROVED / REFINED_TO_FIVE_UNIQUE_SKILL_2 / NOT_IMPLEMENTED` | 초기 검증 로스터 5명, 최종 출시 상한 아님 | `design/APPROVED_OMENWARD_HERO_INITIAL_ROSTER_SCOPE_2026-08-02.md` | production validation pending |
| `OMW-DEC-20260802-GAMEPLAY-HERO-ABILITY-KIT-STRUCTURE-V1` | `USER_APPROVED / REFINED_TO_UNIQUE_SKILL_2 / NOT_IMPLEMENTED` | 패시브 선택 폐기, 해금 영웅 고유 스킬은 2스킬 슬롯 소유 | `design/APPROVED_OMENWARD_HERO_ABILITY_KIT_STRUCTURE_2026-08-02.md` | assets·values pending |
| `OMW-DEC-20260802-GAMEPLAY-HERO-SIGNATURE-DELTA-BALANCE-V1` | `SUPERSEDED_HISTORY / NOT_IMPLEMENTED` | 과거 강제 상쇄 축 sidegrade 결정 | `design/APPROVED_OMENWARD_HERO_SIGNATURE_DELTA_BALANCE_2026-08-02.md` | 계보만 유지 |

## 3. 비카운트 운영 정책

| Process ID | 상태 | 정책 | 책임 원본 |
|---|---|---|---|
| `OMW-PROC-20260803-GRILL-ME-BENCHMARK-PRODUCTION-COMPARISON-V1` | `ACTIVE_STANDING_POLICY` | Grill Me 질문과 승인 작업에 공식 벤치마크·OMENWARD 차이·제작비·QA·적대적 검토·선택지와 권장안을 포함 | `process/APPROVED_GRILL_ME_BENCHMARK_AND_PRODUCTION_COMPARISON_POLICY_2026-08-03.md` |

직접 비교 사례가 없으면 `DIRECT_COMPARABLE_NOT_FOUND`를 기록하며 이 정책은 제품 카운터에 포함하지 않는다.

## 4. 표준 등급·파워 위계

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

## 5. 초기 5명 고유 2스킬

```text
shield_guard → 불퇴의 성벽
archer       → 천공 소거
priest       → 생명의 서약
mage         → 메테오
assassin     → 그림자 분신
```

- 모든 능력은 한 전선·한 전술 목적·자동 규칙 발동이다.
- 표준 2스킬과 동시에 보유하지 않는다.
- 표준 전설 전체 키트보다 낮은 총 전투 가치여야 한다.

## 6. 공통 timer·failure 계약

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

- commit 전 무효화는 READY 복귀·cooldown 0.
- 단발 해결형은 천공 소거·메테오.
- owner-bound 지속형은 방벽·서약·분신.

## 7. timer 지속·Stage 경계

```text
ACTIVE_COMBAT = TIMER_PROGRESS
MAINTENANCE_OR_PREPARATION = TIMER_PAUSED
READY = CARRY
WARMUP_OR_COOLDOWN_REMAINING = CARRY_ON_SAME_INSTANCE
ACTIVE_EFFECT = TERMINATE_AT_COMBAT_END
UNRESOLVED_COMMIT = CANCEL_AND_CONSUME_AT_COMBAT_END
```

- Stage·Act 전환은 상태 초기화 지점이 아니다.
- 정비시간 대기로 cooldown을 무료 회복할 수 없다.
- 미해결 commit은 새 Stage의 표적으로 재지정하지 않는다.
- 사망·완전 제거 시 timer·READY·payload를 삭제하고 고등급 슬롯을 해제한다.
- save/load·Retry는 상태와 잔여시간을 그대로 복원하며 이중 해결·재굴림을 금지한다.

## 8. 적대적 감사 추가

- `OMW-AUD-182`: 정비시간 무료 cooldown 회복 차단.
- `OMW-AUD-183`: Stage 초기화 exploit 차단.
- `OMW-AUD-184`: 지속효과 다음 Stage 이월 차단.
- `OMW-AUD-185`: 미해결 메테오·일제사격 새 Stage 재타깃 차단.
- `OMW-AUD-186`: 짧은 전투에서 스킬 무가치화 위험은 simulation 필요.
- `OMW-AUD-187`: 전투 종료 직전 commit 손실은 후속 trigger 조건 검증 필요.
- `OMW-AUD-188`: save/load commit 이중 해결 차단.
- `OMW-AUD-189`: Act 전환 숨은 초기화 차단.
- `OMW-AUD-190`: timer pause 이유 UX 표시 필요.

## 9. 구현·검증 경계

```text
CURRENT_PRODUCT = LEGACY_PROTOTYPE
LATEST_APPROVED = DOCUMENTED_NOT_IMPLEMENTED
PRODUCT_CODE_AUTHORITY = NONE
COMMON_TIMER_POLICY = APPROVED
TIMER_STAGE_BOUNDARY_POLICY = APPROVED
EXACT_TRIGGER_THRESHOLDS = PENDING
EXACT_SECONDS = PENDING
EXACT_DURATIONS_AND_VALUES = PENDING
ASSETS = NOT_CREATED
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
```

## 10. 카운터·병합 규칙

```text
CURRENT_COUNT_SINCE_MERGE = 9_OF_10
NEXT_PREFLIGHT_AT = 10_OF_10
```

- 승인 즉시 GitHub·Sheet에 같은 Decision ID로 반영한다.
- 10번째 승인 뒤 문서·기획 PR이 fresh Green preflight와 blocker 0을 만족하면 standing authorization에 따라 별도 승인 대기 없이 병합한다.
- 제품 코드 구현·병합은 별도 계약 대상이다.
