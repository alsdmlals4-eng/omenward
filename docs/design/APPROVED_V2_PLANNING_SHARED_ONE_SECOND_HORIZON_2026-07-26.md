# 승인된 전술계획 공유 1초 Horizon 계약

- 승인일: 2026-07-26
- 상태: `V2_SPEC_APPROVED / PRODUCT_CODE_NOT_AUTHORIZED`
- 승인 근거: 사용자 권장안 승인
- 상위 책임:
  - `docs/design/APPROVED_V2_PLANNING_SHORT_WORK_COMPLETION_2026-07-26.md`
  - `docs/design/APPROVED_V2_PLANNING_ONE_SECOND_HEADSTART_2026-07-26.md`
  - `docs/design/APPROVED_V2_PLANNING_DEPENDENCY_DAG_AND_PROVISIONAL_IDS_2026-07-26.md`
  - `docs/design/APPROVED_V2_FIXED_COMMAND_ORDER_AND_SPIN_SNAPSHOT_2026-07-26.md`
  - `docs/design/APPROVED_V2_PLANNING_REVALIDATION_ALL_OR_NOTHING_2026-07-26.md`
  - `docs/design/APPROVED_V2_TRANSACTION_FOUNDATION_SEQUENCE_2026-07-26.md`

이 문서는 일반 `TACTICAL_PLANNING`의 transactional planning branch에서 여러 시간 기반 명령이 공유하는 단일 1초 가상 시간축, dependency 완료 시각에 따른 후속 작업 시작, 독립 작업의 병렬 진행, replay와 confirm 시 누적 금지를 소유한다.

이 문서는 다음 미결정 상태를 명시적으로 대체한다.

```text
MULTI_STAGE_SHORT_WORK_CHAIN_POLICY: REVIEW_PENDING
```

## 1. 승인된 핵심 결정

```text
PLANNING_HEADSTART_TIME_MODEL: SHARED_GLOBAL_ONE_SECOND_HORIZON
PLANNING_HORIZON_DURATION: ONE_SECOND
PER_COMMAND_HEADSTART_BUDGET: FORBIDDEN
INDEPENDENT_READY_COMMANDS_START_AT_T0: REQUIRED
INDEPENDENT_COMMANDS_PROGRESS_CONCURRENTLY: REQUIRED
DEPENDENT_COMMAND_EARLIEST_START: REQUIRED_PRODUCER_CAPABILITY_TIME
DEPENDENT_START_TIME: MAX_REQUIRED_PRODUCER_AVAILABLE_TIME
HORIZON_PROGRESS_CLAMP: REQUIRED
MULTI_STAGE_CHAIN_USES_REMAINING_HORIZON_ONLY: REQUIRED
HORIZON_END_ZERO_PROGRESS_START: ALLOWED
GLOBAL_SIMULATION_CLOCK_DURING_HORIZON: PAUSED
NON_COMMAND_SYSTEM_TIME_DURING_HORIZON: ZERO
PLANNING_REPLAY_HORIZON_ACCUMULATION: FORBIDDEN
CONFIRM_REAPPLIES_HORIZON: FORBIDDEN
POST_CONFIRM_REMAINING_DURATION: TOTAL_MINUS_BRANCH_ELAPSED
PRODUCT_CODE_AUTHORIZED: NO
```

승인된 시간축:

```text
planning horizon start = t0 = 0 tick
planning horizon end   = t1 = canonical 1 second tick

모든 계획 명령은 같은 [t0, t1] 구간을 공유한다.
```

명령마다 별도의 무료 1초를 주지 않는다.

## 2. Canonical fixed-point horizon

가상 시간은 렌더 프레임이나 부동소수점 초 단위를 직접 사용하지 않는다.

```text
horizon_start_tick = 0
horizon_end_tick = CANONICAL_ONE_SECOND_TICKS
```

각 시간 기반 명령은 최소 다음 값을 계산한다.

```text
virtual_start_tick
virtual_available_ticks
virtual_elapsed_ticks
virtual_completion_tick or NONE
branch_lifecycle
```

기본식:

```text
virtual_available_ticks = max(0, horizon_end_tick - virtual_start_tick)
virtual_elapsed_ticks = min(total_duration_ticks, virtual_available_ticks)

if virtual_elapsed_ticks >= total_duration_ticks:
    branch_lifecycle = COMPLETED
    virtual_completion_tick = virtual_start_tick + total_duration_ticks
else:
    branch_lifecycle = IN_PROGRESS
    virtual_completion_tick = NONE
```

필수 규칙:

- 모든 duration, 시작 시각, 완료 시각은 canonical fixed-point tick이다.
- horizon 종료를 넘는 진행량은 잘라낸다.
- UI 표시 반올림이 scheduling 결과를 바꾸지 않는다.
- 동일 entry snapshot과 동일 queue revision은 동일 timeline hash를 만든다.

## 3. 독립 작업의 병렬 시작

`t=0`에 선행 dependency가 충족된 시간 기반 명령은 모두 동시에 시작한다.

예:

```text
R1: 병영 건설 4초
R2: 화살탑 건설 3초
R3: 성벽 업그레이드 6초
```

세 명령이 서로 독립이고 entry snapshot에서 모두 유효하다면:

```text
t=0.0  R1, R2, R3 시작
t=1.0  horizon 종료

R1 elapsed = 1초
R2 elapsed = 1초
R3 elapsed = 1초
```

금지:

- `reservation_sequence`에 따라 R1에 1초를 준 뒤 R2와 R3에 시간이 남지 않는 직렬 처리.
- 명령 수만큼 global simulation 시간을 증가.
- 독립 명령마다 별도의 1초 budget 부여.

`reservation_sequence`는 dependency replay와 같은 tick의 결정론적 처리 순서를 소유하지만, 독립 작업의 시간 예산을 직렬 분할하지 않는다.

## 4. Dependency 작업의 시작 시각

후속 명령이 producer의 완료 capability를 요구하면 producer가 planning branch에서 해당 capability를 제공하는 가상 시각부터 시작할 수 있다.

```text
consumer.virtual_start_tick = max(
    horizon_start_tick,
    required_capability_available_tick_1,
    required_capability_available_tick_2,
    ...
)
```

여러 producer를 요구하면 가장 늦게 준비되는 producer의 available tick을 사용한다.

예:

```text
R1: Tier 1 건설 0.5초
R2: R1의 Tier 2 업그레이드 0.8초
R3: R2의 Tier 3 업그레이드 0.7초
```

결과:

```text
t=0.0  R1 시작
t=0.5  R1 완료, Tier 1 capability 제공
       R2 시작
t=1.0  horizon 종료

R1 = COMPLETED, elapsed 0.5초
R2 = IN_PROGRESS, elapsed 0.5초 / 총 0.8초
R3 = NOT_STARTED, elapsed 0초
```

R2 duration이 0.5초라면:

```text
t=0.5  R2 시작
t=1.0  R2 완료, Tier 2 capability 제공
       R3 시작 상태 성립

R3 elapsed = 0초
```

horizon 종료 tick에서 시작 조건이 충족된 작업은 `STARTED_WITH_ZERO_PROGRESS` 또는 해당 schema의 동등한 branch 상태를 가질 수 있다. 추가 진행 시간은 없다.

## 5. Capability available time

producer output은 output contract가 요구하는 lifecycle에 도달한 가상 시각에 사용 가능하다.

완료를 요구하는 capability:

```text
available_tick = producer.virtual_completion_tick
```

건설 중 상태에서도 허용되는 capability가 명시적으로 존재한다면:

```text
available_tick = producer.virtual_start_tick
```

단, 현재 기본값은 완료 요구다. 다음을 금지한다.

- 같은 건물 이름이라는 이유로 capability를 즉시 제공.
- output contract에 없는 건설 중 capability 추론.
- producer 완료 전에 consumer를 0초부터 진행.
- UI 렌더 완료 애니메이션 시각을 authoritative available tick으로 사용.

consumer는 explicit provisional ID, output slot, required capability를 참조해야 한다.

## 6. 동일 tick의 결정론적 처리

같은 가상 tick에서 여러 완료와 시작 조건이 발생할 수 있다.

기본 처리 단계:

```text
1. 해당 tick까지 진행된 producer 완료 판정
2. 완료된 output capability 공개
3. dependency가 충족된 consumer 활성화 판정
4. reservation_sequence 오름차순으로 동일 tick 상태 transition 기록
5. 다음 tick 구간 진행
```

같은 tick에 완료한 producer의 capability는 그 tick에 시작하는 consumer가 사용할 수 있다.

같은 tick 정렬은 명령에 추가 시간을 주지 않는다. 오직 결정론적 receipt와 branch hash를 위한 순서다.

## 7. 여러 단계 chain의 1초 제한

연속된 모든 단계는 동일 horizon에서 실제로 남은 시간만 사용한다.

예:

```text
R1 0.2초
R2 0.3초
R3 0.4초
R4 0.5초
```

결과:

```text
t=0.0~0.2  R1 완료
t=0.2~0.5  R2 완료
t=0.5~0.9  R3 완료
t=0.9~1.0  R4 0.1초 진행
```

R4에 별도 1초를 주지 않는다.

금지:

- R1 완료 후 R2 horizon을 새로 시작.
- 각 tier마다 1초 headstart 반복.
- queue replay 횟수만큼 chain 진행 증가.
- 명령 추가 순서를 이용해 horizon을 연장.

## 8. Branch-visible 결과

horizon replay가 끝나면 각 명령의 branch 상태를 고정한다.

최소 상태 예:

```text
NOT_STARTED
STARTED_WITH_ZERO_PROGRESS
IN_PROGRESS
COMPLETED
BLOCKED
```

각 결과는 최소 다음을 포함한다.

```text
planning_command_id
reservation_sequence
virtual_start_tick
virtual_elapsed_ticks
virtual_completion_tick
branch_lifecycle
provided_capability_ticks
required_dependency_edges
result_fingerprint
```

planning 화면과 후속 명령 검증은 이 결과를 사용한다.

live world는 confirm 전까지 변경하지 않는다.

## 9. Global simulation 정지

공유 horizon은 계획 명령의 branch-local scheduling 도구다. 전투 전체가 1초 흐르는 것이 아니다.

planning 중 정지:

- 적과 아군 이동·공격.
- projectile, damage, status tick.
- wave와 spawn timer.
- 일반 생산·치유·수리 tick.
- skill cooldown.
- midpoint 진행.
- roulette cooldown.
- stage timer와 clear time.
- live simulation clock.

다음 식은 금지한다.

```text
planning horizon 1초
=
live world 1초 경과
```

## 10. Queue mutation과 전체 replay

명령 추가·수정·취소 시 기존 timeline을 부분 수정하지 않는다.

```text
queue mutation
→ queue_revision 증가
→ PlanningEntrySnapshot 복사
→ 고정 reservation_sequence로 DAG 검증
→ 단일 [0, 1초] horizon timeline 전체 재생성
→ 모든 start·completion·capability 시각 재계산
→ resource·node·lifecycle 전체 재검증
```

필수 규칙:

- 과거 virtual elapsed를 새 replay에 carry하지 않는다.
- 같은 명령의 1초를 다시 더하지 않는다.
- producer duration 변경 시 downstream start tick을 전부 재계산한다.
- producer 취소 시 승인된 dependent cascade 정책을 적용한다.
- stale report, preview, consent, commit plan은 재사용하지 않는다.

같은 queue revision의 순수 replay는 동일 결과를 반환해야 한다.

## 11. Resource와 node 판정

가상 시간축과 virtual ledger는 함께 replay한다.

- 명령 accept 시 planned debit과 hold를 반영한다.
- short work가 horizon 안에 완료해도 live 수입·생산 tick은 만들지 않는다.
- 완료된 구조가 제공하는 structural capacity는 output contract에 따라 후속 planning 검증에 사용할 수 있다.
- 작업별 비용은 reservation sequence와 command schema에 따라 한 번만 예약한다.
- horizon 내 completion을 이유로 비용을 재차감하거나 환불하지 않는다.

독립 명령이 같은 node나 exclusive target을 요구하면 시간 병렬성보다 node·lifecycle invariant가 우선한다. 유효하지 않은 동시 점유는 BLOCKED다.

## 12. Confirm과 live 승격

`[확정/전투 재개]`는 horizon을 다시 재생하는 실행 시간이 아니다.

```text
SpinSession CLOSED 확인
→ 최신 authoritative basis 재확인
→ 최신 queue revision에서 동일 1초 horizon 순수 replay
→ PlanningCommitPlan 생성
→ branch final state·resource debit·deferred side effect 원자 적용
→ PlanningCommitReceipt 기록
→ NORMAL_COMBAT 재개
```

confirm 성공 후 각 미완료 작업의 잔여 시간:

```text
remaining_duration_ticks = total_duration_ticks - branch_virtual_elapsed_ticks
```

예:

```text
R1 total 0.8초, branch completed
→ live completed 상태로 승격

R2 total 2.0초, branch elapsed 0.5초
→ live remaining 1.5초

R3 total 0.7초, branch elapsed 0초
→ live remaining 0.7초
```

confirm 시 horizon이나 완료 event를 재적용하지 않는다.

## 13. Confirm 실패와 rollback

최종 검증이 하나라도 실패하면 다음은 모두 0이다.

- live 건물 생성·업그레이드·철거.
- live 작업 timer 등록.
- live 금화·식량 변경.
- deferred completion side effect.
- simulation time advance.
- wave·cooldown 변화.

planning branch와 queue는 최신 BLOCKED report와 함께 유지한다.

부분 승격을 금지한다.

## 14. Idempotency

동일 `planning_commit_transaction_id` 재요청은 기존 `PlanningCommitReceipt`를 반환한다.

중복 금지:

- horizon 재적용.
- virtual elapsed 추가.
- completion event 중복.
- resource 재차감.
- timer 중복 등록.
- simulation 재개 중복.

동일 queue mutation transaction도 기존 `QueueMutationReceipt`를 반환하며 queue revision을 추가 증가시키지 않는다.

## 15. 범위 경계

이 문서는 다음을 새로 정의하지 않는다.

- 준비 화면의 즉시 적용 정책.
- 위험 전투의 실시간 명령 처리.
- 룰렛 이동의 즉시 실행.
- 기존 live 작업이 planning 진입만으로 headstart를 받는지 여부.
- repair·production queue의 별도 scheduling schema.

특히 기존 live 작업의 planning headstart eligibility는 후속 검수 항목이다.

## 16. 자동 검증 계약

최소 다음 사례를 검증한다.

1. 독립 명령 3개가 모두 t=0에 시작하고 각각 1초 진행.
2. 명령별 독립 1초 budget 금지.
3. 0.5초 producer 완료 후 consumer가 t=0.5에 시작해 0.5초만 진행.
4. consumer가 여러 producer를 요구할 때 가장 늦은 available tick 사용.
5. producer가 t=1에 완료하면 consumer는 t=1 시작·elapsed 0.
6. 0.2+0.3+0.4+0.5초 chain에서 마지막 작업은 0.1초만 진행.
7. queue replay 반복으로 elapsed 누적 0.
8. producer duration 수정 후 downstream start tick 전체 재계산.
9. global simulation·wave·cooldown 시간 변경 0.
10. confirm 성공 시 `remaining = total - branch elapsed`.
11. confirm에서 horizon과 completion event 재적용 0.
12. confirm 실패 시 live mutation과 time advance 0.
13. duplicate planning commit에서 progress·비용·timer 중복 0.
14. 제품 코드·Scene·Resource·게임 데이터 변경 없음.

## 17. 현재 상태

```text
PLANNING_HEADSTART_TIME_MODEL: SHARED_GLOBAL_ONE_SECOND_HORIZON
PLANNING_HORIZON_DURATION: ONE_SECOND
PER_COMMAND_HEADSTART_BUDGET: FORBIDDEN
MULTI_STAGE_SHORT_WORK_CHAIN_POLICY: RESOLVED_SHARED_HORIZON
GLOBAL_SIMULATION_CLOCK_DURING_HORIZON: PAUSED
PRODUCT_CODE_AUTHORIZED: NO
V2_IMPLEMENTATION: NOT_STARTED
HUMAN_QA: NOT_RUN
CORE_LOCK_V2: PENDING
```
