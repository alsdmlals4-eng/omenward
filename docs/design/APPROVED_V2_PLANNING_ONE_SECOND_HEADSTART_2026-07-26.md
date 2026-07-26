# 승인된 전술계획 즉시 반영·1초 선행 진행 계약

- 승인일: 2026-07-26
- 상태: `V2_SPEC_APPROVED / PRODUCT_CODE_NOT_AUTHORIZED`
- 승인 근거: 사용자 직접 규칙 지정
- 상위 책임:
  - `docs/design/APPROVED_V2_FIXED_COMMAND_ORDER_AND_SPIN_SNAPSHOT_2026-07-26.md`
  - `docs/design/APPROVED_V2_SIMULTANEOUS_COMMAND_START_AND_TIME_RESUME_2026-07-26.md`
  - `docs/design/APPROVED_V2_PLANNING_REVALIDATION_ALL_OR_NOTHING_2026-07-26.md`
  - `docs/design/APPROVED_V2_PLANNING_DEPENDENCY_DAG_AND_PROVISIONAL_IDS_2026-07-26.md`
  - `docs/design/APPROVED_MAPRUN_STAGE_WAVE_AND_MIDPOINT_CORE_V1.md`

이 문서는 일반 `TACTICAL_PLANNING`에서 명령을 입력하는 즉시 철거·건설·업그레이드 상태를 계획 화면과 후속 명령 판정에 반영하고, 시간 기반 작업은 1초 진행 상태에서 정지한 뒤 전술계획 종료 시 그 이후 시간을 정상 진행하는 규칙을 소유한다.

이 문서는 이전 문서의 다음 해석을 수정한다.

```text
AUTHORITATIVE_MUTATION_BEFORE_CONFIRM: FORBIDDEN
PLANNING_EDIT_SCOPE: PLAN_DATA_ONLY
모든 시간 기반 명령은 confirm 경계에서 처음 시작
```

정정된 의미는 다음과 같다.

- live authoritative world와 영구 자원 원장은 confirm 전까지 변경하지 않는다.
- 그러나 플레이어가 보는 전술계획 분기 상태는 명령 입력 즉시 변경한다.
- 전술계획 분기 상태는 후속 명령의 node 점유, building lifecycle, dependency와 가상 자원 판정에 권위가 있다.
- confirm 성공 시 이 분기 상태를 원자적으로 live world에 승격한다.

## 1. 승인된 핵심 결정

```text
TACTICAL_PLANNING_STATE_MODEL: TRANSACTIONAL_PLANNING_BRANCH
PLANNING_BRANCH_VISIBLE_STATE: IMMEDIATE
PLANNING_COMMAND_ON_ACCEPT: APPLY_INITIAL_TRANSITION
INSTANT_DEMOLITION_IN_PLANNING_BRANCH: REQUIRED
FREED_NODE_REUSE_IN_SAME_PLANNING_SESSION: ALLOWED
TIMED_WORK_PLANNING_HEADSTART: ONE_SECOND
GLOBAL_SIMULATION_CLOCK_DURING_PLANNING: PAUSED
NON_COMMAND_SYSTEMS_DURING_HEADSTART: FROZEN
PLANNING_EDIT_REBUILD: ENTRY_SNAPSHOT_FULL_REPLAY
AUTHORITATIVE_LEDGER_COMMIT_BEFORE_CONFIRM: FORBIDDEN
CONFIRM_ATOMIC_BRANCH_PROMOTION: REQUIRED
INITIAL_HEADSTART_REAPPLICATION_ON_CONFIRM: FORBIDDEN
POST_PLANNING_PROGRESS_CONTINUATION: FROM_ONE_SECOND
PREVIOUS_ZERO_MUTATION_INTERPRETATION: SUPERSEDED_FOR_PLANNING_BRANCH
```

## 2. 전술계획 입장 Snapshot과 분기 상태

`TACTICAL_PLANNING` 진입 시 다음 기준을 캡처한다.

```text
PlanningEntrySnapshot
- planning_session_id
- entry_simulation_tick
- entry_simulation_time
- building and node state
- building work progress
- gold and food basis
- battlefield and deployment basis
- PendingReward basis
- cooldown and wave basis
- dependency and provisional ID basis
```

이 snapshot에서 `PlanningBranchState`를 만든다.

```text
live authoritative world = entry snapshot에서 정지
planning branch = 플레이어 명령을 즉시 반영하는 가역적 분기
```

분기 상태는 화면 표시와 후속 계획 명령 검증에 사용한다.

- 건물 존재 여부.
- node 점유 여부.
- 건설·업그레이드 진행 상태.
- provisional building identity.
- planned gold와 food 사용 가능량.
- 후속 dependency target.

## 3. 철거 명령

철거 명령이 planning branch에서 유효하면 건물을 즉시 제거한다.

```text
철거 명령 입력
→ building identity를 branch에서 REMOVED 처리
→ node 점유 해제
→ 철거 결과를 후속 명령 판정에 즉시 노출
```

예:

```text
R1: 기존 병영 철거
→ branch에서 병영 즉시 제거
→ node 즉시 빈 상태
R2: 같은 node에 새 병영 건설
→ 허용
→ 새 provisional building 생성
→ 건설 진행 1초에서 정지
```

철거로 인한 live world 변경은 confirm 전까지 발생하지 않는다. 화면과 후속 계획에서는 철거된 상태가 실제 상태처럼 동작한다.

## 4. 건설과 업그레이드 1초 선행 진행

시간 기반 작업은 명령이 planning branch에 받아들여질 때 시작 상태를 만들고 정확히 1초만 진행한다.

```text
work_elapsed_in_planning = min(1.0 second, total_duration)
```

건설 예:

```text
건설 명령 입력
→ provisional building 생성
→ lifecycle = UNDER_CONSTRUCTION
→ elapsed = 1.0 second
→ global simulation은 정지
```

업그레이드 예:

```text
Tier 1 병영 업그레이드 명령 입력
→ branch의 병영 lifecycle = UPGRADING_TO_TIER_2
→ upgrade elapsed = 1.0 second
→ Tier 2 완료 효과는 duration 충족 전까지 비활성
```

1초 선행 진행은 명령 대상 작업의 진행량이다. 전투 전체 simulation 1초가 아니다.

## 5. Planning 중 정지하는 시스템

1초 선행 진행을 적용해도 다음은 움직이지 않는다.

- 적과 아군 유닛 이동·공격.
- projectile과 damage tick.
- wave timer와 spawn timer.
- 생산·치유·수리의 일반 시간 경과.
- 스킬 cooldown.
- 접전지 진행.
- 룰렛 cooldown.
- stage timer와 clear time.
- simulation clock.

따라서 명령을 여러 개 입력해도 전투 시간이 명령 수만큼 증가하지 않는다.

```text
명령 10개 입력
≠ global simulation 10초 경과
```

각 허용된 시간 기반 명령이 자신의 작업 진행도만 1초 상태로 시작한다.

## 6. 가상 자원과 live 원장

planning branch는 후속 명령 검증을 위해 가상 자원 원장을 사용한다.

```text
PlanningVirtualLedger
- planned gold debit
- planned food occupation
- planned refund or release allowed by command contract
- node and capacity reservations
```

후속 명령은 이 가상 원장을 기준으로 검증한다.

금지:

- confirm 전 live gold ledger 차감.
- confirm 전 live food occupation 변경.
- 철거·건설을 이용한 실제 자원 복제.
- branch와 live 원장을 혼합한 이중 차감.

confirm 성공 시 모든 자원 mutation을 정확히 한 번 live 원장에 반영한다.

## 7. 명령 추가·수정·취소

planning branch는 역연산을 연속 적용하지 않는다. 큐가 바뀔 때마다 입장 snapshot에서 전체를 다시 만든다.

```text
명령 추가·수정·취소
→ queue_revision 증가
→ PlanningEntrySnapshot 복사
→ 고정 reservation_sequence 순서로 전체 명령 replay
→ 각 명령의 즉시 transition 적용
→ 각 시간 기반 작업을 1초 상태로 설정
→ dependency·자원·node·lifecycle 전체 재검증
```

이 방식으로 다음을 보장한다.

- 철거 취소 시 기존 건물 복원.
- 철거에 의존한 새 건설은 producer 취소 cascade 정책 적용.
- 업그레이드 취소 시 Tier 1 상태 복원.
- 명령 수정 뒤 과거 1초 진행도를 누적하지 않음.
- 같은 명령 replay가 2초·3초로 증가하지 않음.

## 8. Confirm과 branch 승격

`[확정/전투 재개]`는 branch를 처음 실행하는 시점이 아니다. 이미 계산된 branch 상태를 최신 live basis에 대해 재검증하고 원자 승격하는 시점이다.

```text
SpinSession CLOSED 확인
→ live authoritative basis 재확인
→ entry snapshot 이후 허용된 외부 변화 검사
→ planning branch 전체 재생성
→ PlanningCommitPlan 생성
→ 자원 debit과 branch state를 원자 적용
→ PlanningCommitReceipt 기록
→ NORMAL_COMBAT 재개
```

성공한 live 상태 예:

- 철거 건물은 제거됨.
- 해당 node의 새 건물은 `UNDER_CONSTRUCTION`, elapsed 1초.
- 업그레이드 대상은 `UPGRADING_TO_TIER_2`, elapsed 1초.
- gold와 food는 receipt 기준으로 정확히 한 번 반영.

confirm 시 1초를 다시 적용하지 않는다.

```text
branch elapsed 1초
→ confirm
→ live elapsed 1초
→ 다음 simulation tick부터 1초 이후 진행
```

금지:

- confirm에서 elapsed를 2초로 만드는 중복 적용.
- confirm 직후 건설·업그레이드를 자동 완료.
- 가장 긴 duration까지 fast-forward.
- 명령별 duration 합산.

## 9. Confirm 실패와 rollback

하나라도 실패하면 live world는 변경하지 않는다.

```text
PlanningRevalidationReport = BLOCKED
→ live building mutation 0
→ live node mutation 0
→ live gold and food mutation 0
→ live timer registration 0
→ simulation resume 0
```

planning branch는 플레이어에게 계속 표시할 수 있으나, 실패 사유와 최신 basis를 사용해 재생성해야 한다.

receipt 기록 실패도 전체 commit 실패다.

## 10. Idempotency

동일 `planning_transaction_id` 재요청은 기존 `PlanningCommitReceipt`를 반환한다.

중복 요청은 다음을 만들지 않는다.

- 건물 재철거.
- node 중복 해제.
- provisional building 중복 생성.
- 건설·업그레이드 1초 추가 진행.
- gold 재차감.
- food 중복 점유.
- simulation resume 중복.

Receipt는 최소 다음을 보존한다.

```text
planning_transaction_id
planning_session_id
entry_simulation_tick
commit_simulation_tick
ordered_command_ids
removed_building_ids
provisional_to_actual_building_ids
initial_work_elapsed_by_operation
resource_mutations
```

## 11. 범위 제외

이 계약은 일반 `TACTICAL_PLANNING`에만 적용한다.

- `PREPARATION`의 즉시 적용 규칙은 기존 문서 유지.
- `DANGER_COMBAT`의 실시간 명령은 기존 문서 유지.
- 룰렛 이동의 즉시 소비·비가역 규칙은 기존 문서 유지.
- 제품 코드 구현은 승인하지 않는다.

## 12. 자동 검증 계약

최소 다음 사례를 검증한다.

1. planning 진입 → live simulation clock 정지.
2. 철거 명령 → branch에서 건물 즉시 제거·node 해제.
3. 같은 node 새 건설 → provisional building 생성·elapsed 1초.
4. 업그레이드 명령 → `UPGRADING_TO_TIER_2`, elapsed 1초.
5. 명령 여러 개 입력 → global simulation time 증가 0.
6. 적·wave·cooldown·접전지 진행 0.
7. 후속 명령은 branch node와 virtual ledger 기준으로 검증.
8. 철거 취소 → entry snapshot replay로 건물 복원.
9. 건설 명령 수정 replay → elapsed 누적 없이 1초 유지.
10. confirm 성공 → branch 상태와 자원 원자 승격.
11. confirm 시 initial 1초 재적용 0.
12. confirm 후 첫 simulation 진행 → 1초 이후부터 계속.
13. 하나의 명령 실패 → live mutation과 시간 재개 0.
14. 동일 transaction 재요청 → 철거·건설·progress·비용 중복 0.
15. 준비 화면·위험 전투 경로 영향 0.

## 13. 현재 상태

```text
TACTICAL_PLANNING_STATE_MODEL: TRANSACTIONAL_PLANNING_BRANCH
PLANNING_BRANCH_VISIBLE_STATE: IMMEDIATE
INSTANT_DEMOLITION_IN_PLANNING_BRANCH: REQUIRED
FREED_NODE_REUSE_IN_SAME_PLANNING_SESSION: ALLOWED
TIMED_WORK_PLANNING_HEADSTART: ONE_SECOND
GLOBAL_SIMULATION_CLOCK_DURING_PLANNING: PAUSED
PLANNING_EDIT_REBUILD: ENTRY_SNAPSHOT_FULL_REPLAY
CONFIRM_ATOMIC_BRANCH_PROMOTION: REQUIRED
INITIAL_HEADSTART_REAPPLICATION_ON_CONFIRM: FORBIDDEN
SHORT_DURATION_AT_OR_BELOW_ONE_SECOND_POLICY: REVIEW_PENDING
PRODUCT_CODE_AUTHORIZED: NO
V2_IMPLEMENTATION: NOT_STARTED
HUMAN_QA: NOT_RUN
CORE_LOCK_V2: PENDING
```
