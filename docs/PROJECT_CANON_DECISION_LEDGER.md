# 오멘워드 기획 정본 결정 원장

```yaml
updated_at: 2026-08-03
status: CURRENT_DECISION_LEDGER / MAIN_CANONICAL / MAINTENANCE_SYNC_ACTIVE
current_recovery_decision: OMW-DEC-20260802-CANON-RECOVERY-V1
current_planning_decision: OMW-DEC-20260803-GAMEPLAY-HERO-UNIQUE-SKILL-2-TRIGGER-TARGET-AND-POWER-BUDGET-VALIDATION-V1
current_sync: OMW-SYNC-20260803-IMPLEMENTATION-STATUS-AND-PENDING-REFRESH-V1
current_world_decision: OMW-DEC-20260802-WORLD-VEILSPECIES-PURPOSE-V1
current_operating_decision: OMW-DEC-20260802-GRILL-ME-MERGE-CADENCE-V1
current_benchmark_policy: OMW-PROC-20260803-GRILL-ME-BENCHMARK-PRODUCTION-COMPARISON-V1
current_main: RESOLVE_FROM_REPOSITORY_DEFAULT_BRANCH
working_branch: gpt/omenward-status-pending-refresh-20260803-v2
current_planning_pr: PENDING_CREATION
last_merged_planning_pr: 129
last_merged_planning_commit: 173a408eb7b89992a81165438d97946167db0e14
last_maintenance_pr: 131
last_maintenance_commit: 8ecbb78df47813a6332963db16d235131e65981a
active_base: 9.4.3
product_code_authority: NONE
sheet_id: 1VLwRtXGDtyj0JFt98wdIOtG6Zqc3wtdfCzSF9Fo6lpw
grill_me_approved_since_last_merge: 0
future_merge_cadence: 10_APPROVED_GRILL_ME_DECISIONS
planning_docs_merge_policy: AUTO_PROCEED_AFTER_GREEN_PREFLIGHT_UNDER_STANDING_USER_AUTHORIZATION
product_code_merge_policy: SEPARATE_CONTRACT_REQUIRED
preflight: MAINTENANCE_SYNC_REQUIRED
next_gate: OMW-DEC-20260803-VALIDATION-DETERMINISTIC-SIMULATION-HARNESS-SCOPE-V1
```

`current_main`은 저장소 기본 브랜치에서 실행 시점에 해석한다. PR #129의 squash merge commit은 병합 이력 증거이며 최신 기획 Decision은 main 정본이다. PR #131은 개별 문서의 과거 branch 표식보다 원장·Active·Map의 현재 생명주기 분류가 우선한다는 규칙을 확정했다.

## 1. 상태 언어

```text
USER_APPROVED_PLAN
!= PRODUCT_IMPLEMENTED
!= AUTOMATED_VALIDATED
!= HUMAN_VALIDATED
!= RELEASE_READY
```

```text
MAIN_CANONICAL_NOT_IMPLEMENTED
= approved planning is merged into main
+ product code/data/Scene/Resource remains unchanged
```

## 2. PR #129에서 병합된 10개 Decision

| Decision ID | 상태 | 결정 | 책임 원본 | 미완료 경계 |
|---|---|---|---|---|
| `OMW-DEC-20260803-GAMEPLAY-HERO-UNIQUE-SKILL-2-TRIGGER-TARGET-AND-POWER-BUDGET-VALIDATION-V1` | `USER_APPROVED / MAIN_CANONICAL / NOT_IMPLEMENTED` | 공개 Trigger·same-lane Filter·Priority·stable tie-break·commit Snapshot, A/B/C encounter 파워 위계 검증 | `design/APPROVED_OMENWARD_HERO_UNIQUE_SKILL_2_TRIGGER_TARGET_AND_POWER_BUDGET_VALIDATION_2026-08-03.md` | exact schema·threshold·values·simulation·runtime·human pending |
| `OMW-DEC-20260803-GAMEPLAY-HERO-UNIQUE-SKILL-2-TIMER-PERSISTENCE-AND-STAGE-BOUNDARY-POLICY-V1` | `USER_APPROVED / MAIN_CANONICAL / NOT_IMPLEMENTED` | 전투 clock만 timer 진행, 정비 pause, READY·잔여시간 carry, active·미해결 commit Stage carry 금지 | `design/APPROVED_OMENWARD_HERO_UNIQUE_SKILL_2_TIMER_PERSISTENCE_AND_STAGE_BOUNDARY_POLICY_2026-08-03.md` | exact seconds·simulation·runtime·human pending |
| `OMW-DEC-20260803-GAMEPLAY-HERO-UNIQUE-SKILL-2-COOLDOWN-CHARGE-AND-FAILURE-POLICY-V1` | `USER_APPROVED / MAIN_CANONICAL_REFINED / NOT_IMPLEMENTED` | 단일 cooldown, READY 1회, charge·mana 없음, initial warmup, precommit 실패 무소모 | `design/APPROVED_OMENWARD_HERO_UNIQUE_SKILL_2_COOLDOWN_CHARGE_AND_FAILURE_POLICY_2026-08-03.md` | exact warmup·cooldown pending |
| `OMW-DEC-20260803-GAMEPLAY-HERO-FIRST-FIVE-UNIQUE-SKILL-2-CONCEPTS-V1` | `USER_APPROVED / MAIN_CANONICAL_REFINED / NOT_IMPLEMENTED` | 불퇴의 성벽·천공 소거·생명의 서약·메테오·그림자 분신 | `design/APPROVED_OMENWARD_FIRST_FIVE_UNIQUE_SKILL_2_CONCEPTS_2026-08-03.md` | exact duration·value·asset pending |
| `OMW-DEC-20260802-GAMEPLAY-HERO-GRADE-SLOT-AND-UNLOCKED-SKILL-REPLACEMENT-V1` | `USER_APPROVED / MAIN_CANONICAL / NOT_IMPLEMENTED` | `[영웅]·[전설]` 전장 전체 최대 1명; 해금 영웅 고유 2스킬 교체; 미래 해금 전설 고유 3스킬 교체 | `design/APPROVED_OMENWARD_HERO_GRADE_SLOT_AND_UNLOCKED_SKILL_REPLACEMENT_2026-08-02.md` | 미래 해금 전설 상세 pending |
| `OMW-DEC-20260802-GAMEPLAY-HERO-UNIQUE-SKILL-UPGRADE-MODEL-V1` | `USER_APPROVED / MAIN_CANONICAL_REFINED / NOT_IMPLEMENTED` | 표준 영웅보다 강하고 표준 전설보다 약한 해금 영웅 | `design/APPROVED_OMENWARD_HERO_UNIQUE_SKILL_UPGRADE_MODEL_2026-08-02.md` | exact values pending |
| `OMW-DEC-20260802-GAMEPLAY-HERO-INITIAL-ROSTER-ARCHETYPE-SELECTION-V1` | `USER_APPROVED / MAIN_CANONICAL_REFINED / NOT_IMPLEMENTED` | 방패병·궁병·사제·마법사·암살자 | `design/APPROVED_OMENWARD_HERO_INITIAL_ROSTER_ARCHETYPE_SELECTION_2026-08-02.md` | identities·assets pending |
| `OMW-DEC-20260802-GAMEPLAY-HERO-INITIAL-ROSTER-SCOPE-V1` | `USER_APPROVED / MAIN_CANONICAL_REFINED / NOT_IMPLEMENTED` | 초기 검증 로스터 5명, 최종 출시 상한 아님 | `design/APPROVED_OMENWARD_HERO_INITIAL_ROSTER_SCOPE_2026-08-02.md` | production validation pending |
| `OMW-DEC-20260802-GAMEPLAY-HERO-ABILITY-KIT-STRUCTURE-V1` | `USER_APPROVED / MAIN_CANONICAL_REFINED / NOT_IMPLEMENTED` | 패시브 선택 폐기, 해금 영웅은 고유 2스킬 슬롯 사용 | `design/APPROVED_OMENWARD_HERO_ABILITY_KIT_STRUCTURE_2026-08-02.md` | assets·values pending |
| `OMW-DEC-20260802-GAMEPLAY-HERO-SIGNATURE-DELTA-BALANCE-V1` | `SUPERSEDED_HISTORY / MAIN_LINEAGE / NOT_IMPLEMENTED` | 과거 강제 상쇄 축 sidegrade 결정 | `design/APPROVED_OMENWARD_HERO_SIGNATURE_DELTA_BALANCE_2026-08-02.md` | 계보만 유지 |

## 3. 비카운트 운영 정책·동기화

| ID | 상태 | 정책·동기화 | 책임 원본 |
|---|---|---|---|
| `OMW-PROC-20260803-GRILL-ME-BENCHMARK-PRODUCTION-COMPARISON-V1` | `ACTIVE_STANDING_POLICY / MAIN_CANONICAL` | 공식 벤치마크·OMENWARD 차이·제작비·QA·적대적 검토·선택지와 권장안을 포함 | `process/APPROVED_GRILL_ME_BENCHMARK_AND_PRODUCTION_COMPARISON_POLICY_2026-08-03.md` |
| `OMW-SYNC-20260803-LIFECYCLE-STATUS-CLEANUP-V1` | `MAINTENANCE_SYNC / MAIN_CANONICAL / NON_COUNTER` | 현행 Trigger 책임 원본과 생명주기 우선순위를 main 상태로 교정 | `DOCUMENTATION_MAP.md`, Trigger 책임 원본 |
| `OMW-SYNC-20260803-IMPLEMENTATION-STATUS-AND-PENDING-REFRESH-V1` | `MAINTENANCE_SYNC / ACTIVE / NON_COUNTER` | 7월 27일에 멈춘 구현 상태·미확정 목록을 8월 3일 main 영웅 정본과 다음 simulation gate에 동기화 | `CURRENT_IMPLEMENTATION_STATUS.md`, `DECISIONS_PENDING.md` |

직접 비교 사례가 없으면 `DIRECT_COMPARABLE_NOT_FOUND`를 기록한다. 운영 정책과 유지보수 Sync는 제품 Decision 카운터에 포함하지 않는다.

## 4. 현행 등급·전역 슬롯

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

## 5. Trigger·대상 Resolver

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
MANUAL_CAST_OR_TARGET = FORBIDDEN
```

## 6. 파워 검증 계약

```text
A = 표준 [영웅]
B = 같은 source archetype 해금 이름 지정 [영웅]
C = 같은 계열 표준 [전설]
```

- B는 의도된 encounter family에서 A보다 명확히 강해야 한다.
- C는 전체 대표 encounter 합산 가치에서 B보다 강해야 한다.
- 모든 encounter 자동 최선 또는 다른 두 전선 비결정화는 stop-ship이다.
- exact sample size·tolerance·수치는 simulation 계획에서 확정한다.

## 7. 구현·미확정 추적 정본

`CURRENT_IMPLEMENTATION_STATUS.md`는 실제 제품과 main 기획 사이의 경계를 소유한다.

`DECISIONS_PENDING.md`는 다음 P0~P6를 소유한다.

```text
P0 = deterministic simulation harness 범위·재현성·입출력 계약
P1 = 전체 병종 공통 전투 schema와 피해·방어·위협도 기준
P2 = 다섯 해금 영웅 exact Trigger·timer·효과값
P3 = A/B/C 통과선·표본 수·stop-ship 기준
P4 = 100,000시드 룰렛·경제 simulation 계약
P5 = checkpoint·save schema
P6 = 첫 제품 구현 패키지·Red tests·회귀·롤백 계획
```

## 8. 구현·검증 경계

```text
CURRENT_PRODUCT = LEGACY_PROTOTYPE
LATEST_APPROVED = MAIN_CANONICAL_NOT_IMPLEMENTED
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

## 9. 카운터·다음 Gate

```text
CURRENT_COUNT_SINCE_MERGE = 0_OF_10
CURRENT_MAINTENANCE_SYNC = OMW-SYNC-20260803-IMPLEMENTATION-STATUS-AND-PENDING-REFRESH-V1
NEXT_GRILL_ME_DECISION = OMW-DEC-20260803-VALIDATION-DETERMINISTIC-SIMULATION-HARNESS-SCOPE-V1
NEXT_PREFLIGHT_AT = 10_OF_10
```

- 승인 Decision은 즉시 GitHub·Sheet에 같은 ID로 반영한다.
- 다음 10번째 승인 뒤 문서·기획 PR이 fresh Green preflight와 blocker 0을 만족하면 standing authorization에 따라 병합한다.
- 제품 코드 구현·병합은 별도 계약 대상이다.
