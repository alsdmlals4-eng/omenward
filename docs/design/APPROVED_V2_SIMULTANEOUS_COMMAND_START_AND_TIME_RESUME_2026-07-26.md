# 승인된 동시 명령 시작·정상 시간 재개 계약

- 승인일: 2026-07-26
- 상태: `V2_SPEC_APPROVED / PRODUCT_CODE_NOT_AUTHORIZED`
- 승인 근거: 사용자 권장안 승인
- 상위 책임:
  - `docs/design/APPROVED_V2_FIXED_COMMAND_ORDER_AND_SPIN_SNAPSHOT_2026-07-26.md`
  - `docs/design/APPROVED_V2_PLANNING_REVALIDATION_ALL_OR_NOTHING_2026-07-26.md`
  - `docs/design/APPROVED_V2_PLANNING_DEPENDENCY_DAG_AND_PROVISIONAL_IDS_2026-07-26.md`
  - `docs/design/APPROVED_V2_TRANSACTION_FOUNDATION_SEQUENCE_2026-07-26.md`
  - `docs/design/APPROVED_MAPRUN_STAGE_WAVE_AND_MIDPOINT_CORE_V1.md`

이 문서는 일반 `TACTICAL_PLANNING`에서 `[확정]` 또는 `[전투 재개]`가 성공할 때 시간 기반 명령과 즉시 명령을 어느 simulation 경계에서 시작하는지, 시간 재개와 완료 판정이 어떻게 이루어지는지를 소유한다.

준비 화면의 즉시 적용과 `DANGER_COMBAT`의 실시간 명령은 이 문서 범위가 아니다.

## 1. 승인된 핵심 결정

```text
TACTICAL_CONFIRM_TIME_POLICY: SIMULTANEOUS_START_THEN_NORMAL_RESUME
COMMAND_START_BOUNDARY: SINGLE_AUTHORITATIVE_SIMULATION_BOUNDARY
TIME_BASED_COMMANDS_SHARE_START_TIME: YES
TIME_BASED_COMMAND_AUTO_COMPLETE_ON_CONFIRM: FORBIDDEN
COMMAND_DURATION_FAST_FORWARD_ON_CONFIRM: FORBIDDEN
SEQUENTIAL_DURATION_ACCUMULATION: FORBIDDEN
PLANNING_COMMIT_PROCESSING_TIME_COUNTS_AS_SIMULATION_TIME: NO
TIME_ADVANCE_BEFORE_SUCCESSFUL_RECEIPT: FORBIDDEN
POST_COMMIT_COMPLETION_BASIS: SIMULATION_ELAPSED_TIME
NEW_DEPLOYMENT_ACTION_START: NEXT_SIMULATION_TICK
PREPARATION_SCOPE: EXCLUDED
DANGER_COMBAT_SCOPE: EXCLUDED
```

승인된 흐름:

```text
명령 확정 요청
→ authoritative 상태와 queue revision 재확인
→ 전체 PlanningCommitPlan 순수 계산
→ 단일 commit simulation boundary 결정
→ 모든 명령을 같은 boundary에서 원자 적용
→ PlanningCommitReceipt 기록
→ TACTICAL_PLANNING 종료
→ NORMAL_COMBAT 정상 재개
→ 이후 simulation elapsed time으로 개별 완료 판정
```

## 2. 공통 시작 경계

성공한 planning batch는 하나의 authoritative simulation 시작 경계를 가진다.

`PlanningCommitPlan`과 `PlanningCommitReceipt`는 최소 다음 값을 보존한다.

```text
planning_commit_transaction_id
planning_session_id
queue_revision
commit_simulation_tick
command_start_simulation_time
ordered_reservation_ids
started_time_based_command_ids
applied_immediate_command_ids
```

필수 규칙:

- batch 안의 모든 시간 기반 명령은 동일 `command_start_simulation_time`을 사용한다.
- 렌더 프레임, UI callback 시간, wall-clock timestamp는 시작 순서를 결정하지 않는다.
- 시스템 생성 `reservation_sequence`는 검증과 deterministic mutation ordering에 사용하지만 명령별 시작 시간을 순차적으로 밀지 않는다.
- 한 명령을 적용한 뒤 다음 명령의 duration만큼 시간을 진행하는 방식은 금지한다.
- 가장 긴 명령의 완료 시점까지 simulation을 자동 진행하는 방식도 금지한다.

## 3. 시간 기반 명령 상태

건설과 업그레이드처럼 duration을 가진 명령은 확정 성공 직후 완료 상태가 아니다.

대표 상태:

```text
건설 명령 성공
→ lifecycle = UNDER_CONSTRUCTION
→ started_at_simulation_time = command_start_simulation_time
→ remaining_duration = configured_build_duration

업그레이드 명령 성공
→ lifecycle = UPGRADING
→ started_at_simulation_time = command_start_simulation_time
→ remaining_duration = configured_upgrade_duration
```

완료 판정:

```text
current_simulation_time - started_at_simulation_time >= required_duration
→ authoritative completion event
```

계획 확정 처리 시간, 네트워크 대기, 프레임 지연, 모달 애니메이션은 simulation elapsed time에 포함하지 않는다.

## 4. 즉시 명령과 다음 Tick

시간 기반 명령과 즉시 명령은 같은 원자 commit에 포함될 수 있다.

예:

- 유닛 배치.
- 전술 스킬 예약.
- 건설 시작.
- 업그레이드 시작.

즉시 명령의 authoritative 상태 전이는 commit boundary에서 기록할 수 있다. 다만 새로 배치된 유닛의 이동·공격·AI 행동은 기존 계약대로 다음 simulation tick부터 시작한다.

```text
commit tick N
→ unit spawn와 식량 점유 기록
→ receipt 기록
→ combat resume

tick N+1
→ 신규 유닛 행동 가능
```

스킬 효과의 정확한 발동 tick과 대상 판정은 후속 command schema가 소유하되, planning 확정 중 wall-clock 시간이나 callback 순서로 앞당겨서는 안 된다.

## 5. 동시 시작과 독립 완료

같은 batch의 시간 기반 명령은 같은 시점에 시작하지만 각자 duration에 따라 독립적으로 완료한다.

```text
명령 A: 건설 10초
명령 B: 업그레이드 20초
명령 C: 수리 5초

공통 시작 t = 100초
→ C 완료 t = 105초
→ A 완료 t = 110초
→ B 완료 t = 120초
```

금지:

- C 완료 뒤 A를 시작.
- A 완료 뒤 B를 시작.
- 총 35초를 즉시 진행.
- 가장 긴 20초를 즉시 건너뜀.
- UI 생성 순서를 실제 시작 시간 차이로 해석.

## 6. Dependency와 시간 가속 금지

같은 planning batch의 producer output은 commit 직후 실제로 제공하는 lifecycle과 capability만 consumer가 사용할 수 있다.

```text
R1: 병영 건설 시작
→ lifecycle = UNDER_CONSTRUCTION

R2: 완성 병영 요구 업그레이드
→ requires lifecycle = COMPLETED
→ BLOCKED
```

모든 명령이 같은 시점에 시작하더라도 건설 duration이 완료된 것으로 간주하지 않는다.

허용 가능한 consumer는 producer가 commit boundary에서 실제 제공하는 capability를 명시적으로 요구해야 한다.

## 7. 성공 Commit과 시간 재개 순서

시간은 성공 receipt보다 먼저 진행하지 않는다.

```text
최종 basis 검증
→ 자원·pending·capacity 예약
→ 모든 mutation 준비
→ 단일 boundary에서 전체 상태 전이
→ PlanningCommitReceipt 영속 기록
→ planning 상태 종료
→ simulation resume 허용
```

`PlanningCommitReceipt` 기록에 실패하거나 전체 mutation 중 하나라도 실패하면 시간 재개를 포함해 전부 rollback한다.

허용 결과:

```text
전체 명령 시작 + receipt + 정상 시간 재개
또는
전체 상태 변경 0 + 시간 진행 0
```

## 8. 검증 실패와 Commit 실패

전체 재검증에서 하나라도 실패하면:

```text
PlanningRevalidationReport = BLOCKED
→ 명령 시작 0
→ 자원 차감 0
→ 건물·유닛·스킬 mutation 0
→ simulation time advance 0
→ TACTICAL_PLANNING 유지
```

재검증은 통과했지만 commit 중 실패한 경우에도 전체 batch를 rollback하고 planning 상태를 유지한다.

부분적으로 건설만 시작하거나 유닛만 배치한 채 시간을 재개해서는 안 된다.

## 9. Idempotency

동일 `planning_commit_transaction_id` 재요청은 기존 `PlanningCommitReceipt`를 반환한다.

중복 요청은 다음을 만들지 않는다.

- 시간 기반 명령 재시작.
- `started_at_simulation_time` 변경.
- duration timer 중복 등록.
- 유닛 중복 spawn.
- 스킬 중복 적용.
- 자원 재차감.
- simulation 중복 재개.

Receipt의 `commit_simulation_tick`과 `command_start_simulation_time`은 재요청에서도 동일하다.

## 10. Scope 분리

### PREPARATION

준비 화면은 상위 MapRun 계약의 즉시 적용 규칙을 유지한다. 이 문서는 준비 화면 명령을 planning batch로 변경하지 않는다.

### DANGER_COMBAT

위험 전투는 실시간 즉시 명령 경로를 유지한다. 이 문서의 pause·batch·simultaneous resume 계약을 적용하지 않는다.

### TACTICAL_PLANNING

이 문서의 전체 계약은 일반 전투 중 명시적으로 정지된 `TACTICAL_PLANNING`에서만 적용한다.

## 11. 자동 검증 계약

최소 다음 사례를 검증한다.

1. 건설과 업그레이드 예약을 함께 확정 → 동일 시작 simulation time.
2. 서로 다른 duration → 실제 elapsed time에 따라 독립 완료.
3. 확정 직후 건설·업그레이드가 완료 상태가 아님.
4. 명령 duration 합산 fast-forward 0.
5. 최대 duration까지 자동 진행 0.
6. planning commit 처리 wall-clock 지연 → simulation time 영향 0.
7. 신규 배치 유닛 → commit tick에는 행동하지 않고 다음 tick부터 행동.
8. 완성 lifecycle을 요구하는 같은 batch consumer → 시간 가속 없이 차단.
9. 전체 재검증 실패 → 명령 시작과 시간 진행 0.
10. commit 중 하나 실패 → 전체 rollback과 시간 진행 0.
11. receipt 기록 실패 → simulation resume 0.
12. 동일 transaction 재요청 → 시작 시간·timer·spawn·비용·재개 중복 0.
13. 준비 화면과 위험 전투 경로는 기존 규칙 유지.
14. 서로 다른 렌더 프레임률에서도 같은 command log가 같은 시작 tick과 완료 tick 생성.

## 12. 현재 상태

```text
TACTICAL_CONFIRM_TIME_POLICY: SIMULTANEOUS_START_THEN_NORMAL_RESUME
COMMAND_START_BOUNDARY: SINGLE_AUTHORITATIVE_SIMULATION_BOUNDARY
TIME_BASED_COMMAND_AUTO_COMPLETE_ON_CONFIRM: FORBIDDEN
COMMAND_DURATION_FAST_FORWARD_ON_CONFIRM: FORBIDDEN
SEQUENTIAL_DURATION_ACCUMULATION: FORBIDDEN
TIME_ADVANCE_BEFORE_SUCCESSFUL_RECEIPT: FORBIDDEN
POST_COMMIT_COMPLETION_BASIS: SIMULATION_ELAPSED_TIME
PRODUCT_CODE_AUTHORIZED: NO
V2_IMPLEMENTATION: NOT_STARTED
HUMAN_QA: NOT_RUN
CORE_LOCK_V2: PENDING
```
