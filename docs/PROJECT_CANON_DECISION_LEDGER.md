# 오멘워드 기획 정본 결정 원장

```yaml
updated_at: 2026-08-03
status: CURRENT_DECISION_LEDGER / ACTIVE_PLANNING_BRANCH
current_recovery_decision: OMW-DEC-20260802-CANON-RECOVERY-V1
current_planning_decision: OMW-DEC-20260803-GAMEPLAY-HERO-UNIQUE-SKILL-2-TRIGGER-TARGET-AND-POWER-BUDGET-VALIDATION-V1
current_world_decision: OMW-DEC-20260802-WORLD-VEILSPECIES-PURPOSE-V1
current_operating_decision: OMW-DEC-20260802-GRILL-ME-MERGE-CADENCE-V1
current_benchmark_policy: OMW-PROC-20260803-GRILL-ME-BENCHMARK-PRODUCTION-COMPARISON-V1
current_main: RESOLVE_FROM_REPOSITORY_DEFAULT_BRANCH
working_branch: gpt/omenward-hero-kit-planning-20260802
current_planning_pr: 129
active_base: 9.4.3
product_code_authority: NONE
sheet_id: 1VLwRtXGDtyj0JFt98wdIOtG6Zqc3wtdfCzSF9Fo6lpw
grill_me_approved_since_last_merge: 10
future_merge_cadence: 10_APPROVED_GRILL_ME_DECISIONS
planning_docs_merge_policy: AUTO_PROCEED_AFTER_GREEN_PREFLIGHT_UNDER_STANDING_USER_AUTHORIZATION
product_code_merge_policy: SEPARATE_CONTRACT_REQUIRED
preflight: REQUIRED_NOW
next_gate: FRESH_PREFLIGHT_AND_DOCUMENTATION_PR_MERGE
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

## 2. 현재 묶음 Decision 10/10

| Decision ID | 상태 | 결정 | 책임 원본 | 미완료 경계 |
|---|---|---|---|---|
| `OMW-DEC-20260803-GAMEPLAY-HERO-UNIQUE-SKILL-2-TRIGGER-TARGET-AND-POWER-BUDGET-VALIDATION-V1` | `USER_APPROVED / ACTIVE_BRANCH_SYNC_REQUIRED / NOT_IMPLEMENTED` | 공개 Trigger·같은 전선 후보 Filter·Priority Score·stable tie-break·commit Snapshot, A/B/C encounter 파워 위계 검증 | `design/APPROVED_OMENWARD_HERO_UNIQUE_SKILL_2_TRIGGER_TARGET_AND_POWER_BUDGET_VALIDATION_2026-08-03.md` | exact schema·threshold·values·simulation·runtime·human pending |
| `OMW-DEC-20260803-GAMEPLAY-HERO-UNIQUE-SKILL-2-TIMER-PERSISTENCE-AND-STAGE-BOUNDARY-POLICY-V1` | `USER_APPROVED / ACTIVE_BRANCH_SYNCED / NOT_IMPLEMENTED` | 전투 clock에서만 timer 진행, 정비 pause, READY·잔여시간 carry, active·미해결 commit Stage carry 금지 | `design/APPROVED_OMENWARD_HERO_UNIQUE_SKILL_2_TIMER_PERSISTENCE_AND_STAGE_BOUNDARY_POLICY_2026-08-03.md` | exact seconds·simulation·runtime·human pending |
| `OMW-DEC-20260803-GAMEPLAY-HERO-UNIQUE-SKILL-2-COOLDOWN-CHARGE-AND-FAILURE-POLICY-V1` | `USER_APPROVED / REFINED_BY_TIMER_AND_TRIGGER_POLICIES / NOT_IMPLEMENTED` | 단일 cooldown, READY 1회, charge·mana 없음, initial warmup, precommit 실패 무소모, 효과 종료 뒤 cooldown | `design/APPROVED_OMENWARD_HERO_UNIQUE_SKILL_2_COOLDOWN_CHARGE_AND_FAILURE_POLICY_2026-08-03.md` | exact warmup·cooldown pending |
| `OMW-DEC-20260803-GAMEPLAY-HERO-FIRST-FIVE-UNIQUE-SKILL-2-CONCEPTS-V1` | `USER_APPROVED / REFINED_BY_TRIGGER_POLICY / NOT_IMPLEMENTED` | 불퇴의 성벽·천공 소거·생명의 서약·메테오·그림자 분신 | `design/APPROVED_OMENWARD_FIRST_FIVE_UNIQUE_SKILL_2_CONCEPTS_2026-08-03.md` | exact duration·value·asset pending |
| `OMW-DEC-20260802-GAMEPLAY-HERO-GRADE-SLOT-AND-UNLOCKED-SKILL-REPLACEMENT-V1` | `USER_APPROVED / ACTIVE_BRANCH_SYNCED / NOT_IMPLEMENTED` | `[영웅]·[전설]` 전장 전체 최대 1명; 해금 영웅 고유 2스킬 교체; 미래 해금 전설 고유 3스킬 교체 | `design/APPROVED_OMENWARD_HERO_GRADE_SLOT_AND_UNLOCKED_SKILL_REPLACEMENT_2026-08-02.md` | 미래 해금 전설 상세 pending |
| `OMW-DEC-20260802-GAMEPLAY-HERO-UNIQUE-SKILL-UPGRADE-MODEL-V1` | `USER_APPROVED / REFINED_TO_SKILL_2_REPLACEMENT / NOT_IMPLEMENTED` | 표준 영웅보다 강하고 표준 전설보다 약한 해금 영웅 | `design/APPROVED_OMENWARD_HERO_UNIQUE_SKILL_UPGRADE_MODEL_2026-08-02.md` | exact values pending |
| `OMW-DEC-20260802-GAMEPLAY-HERO-INITIAL-ROSTER-ARCHETYPE-SELECTION-V1` | `USER_APPROVED / REFINED_TO_UNIQUE_SKILL_2 / NOT_IMPLEMENTED` | 방패병·궁병·사제·마법사·암살자 | `design/APPROVED_OMENWARD_HERO_INITIAL_ROSTER_ARCHETYPE_SELECTION_2026-08-02.md` | identities·assets pending |
| `OMW-DEC-20260802-GAMEPLAY-HERO-INITIAL-ROSTER-SCOPE-V1` | `USER_APPROVED / REFINED_TO_FIVE_UNIQUE_SKILL_2 / NOT_IMPLEMENTED` | 초기 검증 로스터 5명, 최종 출시 상한 아님 | `design/APPROVED_OMENWARD_HERO_INITIAL_ROSTER_SCOPE_2026-08-02.md` | production validation pending |
| `OMW-DEC-20260802-GAMEPLAY-HERO-ABILITY-KIT-STRUCTURE-V1` | `USER_APPROVED / REFINED_TO_UNIQUE_SKILL_2 / NOT_IMPLEMENTED` | 패시브 선택 폐기, 해금 영웅 고유 스킬은 2스킬 슬롯 소유 | `design/APPROVED_OMENWARD_HERO_ABILITY_KIT_STRUCTURE_2026-08-02.md` | assets·values pending |
| `OMW-DEC-20260802-GAMEPLAY-HERO-SIGNATURE-DELTA-BALANCE-V1` | `SUPERSEDED_HISTORY / NOT_IMPLEMENTED` | 과거 강제 상쇄 축 sidegrade 결정 | `design/APPROVED_OMENWARD_HERO_SIGNATURE_DELTA_BALANCE_2026-08-02.md` | 계보만 유지 |

## 3. 비카운트 운영 정책

| Process ID | 상태 | 정책 | 책임 원본 |
|---|---|---|---|
| `OMW-PROC-20260803-GRILL-ME-BENCHMARK-PRODUCTION-COMPARISON-V1` | `ACTIVE_STANDING_POLICY` | 공식 벤치마크·OMENWARD 차이·제작비·QA·적대적 검토·선택지와 권장안을 포함 | `process/APPROVED_GRILL_ME_BENCHMARK_AND_PRODUCTION_COMPARISON_POLICY_2026-08-03.md` |

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

## 5. 공개 Trigger·대상 Resolver

```text
READY
→ public trigger
→ same-lane legal filter
→ public priority score
→ stability window
→ stable ID / stable position tie-break
→ CAST_PRECHECK
→ immutable CAST_COMMIT snapshot
```

```text
PUBLIC_TRIGGER_RULE = REQUIRED
PUBLIC_TARGET_PRIORITY = REQUIRED
DETERMINISTIC_TIE_BREAK = REQUIRED
ARBITRARY_FALLBACK_RETARGET = FORBIDDEN
HIDDEN_FUTURE_BATTLE_END_ORACLE = FORBIDDEN
```

- 방패병은 전열 압력과 보호 가치.
- 궁병은 비행 수·가중 위협도.
- 사제는 기준 이하 체력의 같은 전선 생존 아군.
- 마법사는 적중 수 → 총 위협도 → stable 위치.
- 암살자는 역할 우선순위 → 후열 깊이 → 위협도 → stable ID.

## 6. 파워 검증 계약

```text
A = 표준 [영웅]
B = 같은 source archetype 해금 이름 지정 [영웅]
C = 같은 계열 표준 [전설]
```

동일 source Tier·seed·Stage·적 구성·건물·다른 두 전선 조건에서 비교한다.

대표 family:

```text
NEUTRAL_MIXED
FRONTLINE_PRESSURE
FLYING_HEAVY
ALLY_BURST_CRISIS
DENSE_ENEMY_CLUSTER
DISPERSED_ENEMY_FORMATION
HIGH_VALUE_BACKLINE
LONG_ATTRITION
SHORT_STAGE
LATE_COMMIT_BOUNDARY
```

- B는 의도된 family에서 A보다 명확히 강해야 한다.
- C는 전체 대표 family 합산 가치에서 B보다 높아야 한다.
- 해금 영웅 하나가 모든 family에서 자동 최선이면 실패다.
- 고등급 한 명이 다른 두 전선을 무의미하게 만들면 실패다.
- 정확 sample size·tolerance는 simulation 계획에서 고정한다.

## 7. 적대적 감사 추가

- `OMW-AUD-191`: 숨은 AI 판단 차단.
- `OMW-AUD-192`: 한 프레임 Trigger 깜빡임 검증.
- `OMW-AUD-193`: stable tie-break 강제.
- `OMW-AUD-194`: 방벽 상시 uptime 위험.
- `OMW-AUD-195`: 천공 소거의 비행 공세 무력화 위험.
- `OMW-AUD-196`: 생명의 서약의 광역 무적·회복 변질 위험.
- `OMW-AUD-197`: 메테오 counterplay·miss rate 위험.
- `OMW-AUD-198`: 분신 독립 AI·스킬 복제 팽창 위험.
- `OMW-AUD-199`: 해금 영웅의 전설 파워 침범 위험.
- `OMW-AUD-200`: 모든 encounter 자동 최선 위험.
- `OMW-AUD-201`: 종료 직전 commit 취소 체감 위험.
- `OMW-AUD-202`: 다른 두 전선 비결정화 위험.

## 8. 구현·검증 경계

```text
CURRENT_PRODUCT = LEGACY_PROTOTYPE
LATEST_APPROVED = DOCUMENTED_NOT_IMPLEMENTED
PRODUCT_CODE_AUTHORITY = NONE
PUBLIC_TRIGGER_TARGET_RESOLVER = APPROVED_CONCEPT
POWER_VALIDATION_MATRIX = APPROVED_CONCEPT
EXACT_SCHEMA = PENDING
EXACT_TRIGGER_THRESHOLDS = PENDING
EXACT_STABILITY_WINDOWS = PENDING
EXACT_SECONDS = PENDING
EXACT_DURATIONS_AND_VALUES = PENDING
ASSETS = NOT_CREATED
SIMULATION_PLAN = REQUIRED_BEFORE_IMPLEMENTATION
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
```

## 9. 카운터·병합 규칙

```text
CURRENT_COUNT_SINCE_MERGE = 10_OF_10
PREFLIGHT = REQUIRED_NOW
```

- 승인 즉시 GitHub·Sheet에 같은 Decision ID로 반영한다.
- fresh Green preflight와 blocker 0을 만족하면 standing authorization에 따라 PR #129를 별도 승인 대기 없이 병합한다.
- 제품 코드 구현·병합은 별도 계약 대상이다.