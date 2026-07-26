# 승인된 전술계획 1초 이하 작업 완료 계약

- 승인일: 2026-07-26
- 상태: `V2_SPEC_APPROVED / PRODUCT_CODE_NOT_AUTHORIZED`
- 승인 근거: 사용자 권장안 승인
- 상위 책임:
  - `docs/design/APPROVED_V2_PLANNING_ONE_SECOND_HEADSTART_2026-07-26.md`
  - `docs/design/APPROVED_V2_SIMULTANEOUS_COMMAND_START_AND_TIME_RESUME_2026-07-26.md`
  - `docs/design/APPROVED_V2_PLANNING_REVALIDATION_ALL_OR_NOTHING_2026-07-26.md`
  - `docs/design/APPROVED_V2_PLANNING_DEPENDENCY_DAG_AND_PROVISIONAL_IDS_2026-07-26.md`
  - `docs/design/APPROVED_V2_TRANSACTION_FOUNDATION_SEQUENCE_2026-07-26.md`

이 문서는 일반 `TACTICAL_PLANNING`의 transactional planning branch에서 총 작업 시간이 1초 이하인 건설·업그레이드 등 시간 기반 작업의 완료 경계, branch-visible capability, confirm 승격, 취소·재생성과 idempotency를 소유한다.

## 1. 승인된 핵심 결정

```text
PLANNING_HEADSTART_COMPLETION_THRESHOLD: DURATION_LE_ONE_SECOND
ONE_SECOND_COMPLETION_BOUNDARY: INCLUSIVE
SHORT_TIMED_WORK_BRANCH_RESULT: COMPLETED
SHORT_TIMED_WORK_LIVE_PROMOTION: CONFIRM_ONLY
BRANCH_COMPLETION_CAPABILITIES: AVAILABLE_TO_LATER_COMMANDS
BRANCH_COMPLETION_EXTERNAL_SIDE_EFFECTS: DEFERRED_TO_COMMIT
FIXED_POINT_DURATION_COMPARISON: REQUIRED
PLANNING_REPLAY_COMPLETION_ACCUMULATION: FORBIDDEN
CONFIRM_REAPPLIES_HEADSTART: FORBIDDEN
CONFIRM_DUPLICATES_COMPLETION_EVENT: FORBIDDEN
FAILED_CONFIRM_LIVE_COMPLETION: ZERO
MULTI_STAGE_SHORT_WORK_CHAIN_POLICY: REVIEW_PENDING
PRODUCT_CODE_AUTHORIZED: NO
```

승인된 기본식:

```text
planning_headstart = 1 second
work_elapsed_in_planning = min(planning_headstart, total_duration)

if work_elapsed_in_planning >= total_duration:
    planning_branch_lifecycle = COMPLETED
else:
    planning_branch_lifecycle = IN_PROGRESS
```

`total_duration == 1초`는 완료에 포함한다.

## 2. Fixed-point 완료 판정

완료 경계는 부동소수점 근사나 렌더 프레임에 의존하지 않는다.

```text
total_duration_ticks
planning_headstart_ticks
elapsed_ticks = min(planning_headstart_ticks, total_duration_ticks)
completed = elapsed_ticks >= total_duration_ticks
```

필수 규칙:

- duration과 elapsed는 승인된 canonical fixed-point time unit을 사용한다.
- `0.999999`, `1.000001` 같은 float 오차로 완료 여부가 달라져서는 안 된다.
- 정확히 1초에 해당하는 tick 수는 inclusive 완료다.
- UI 표시 반올림 값이 아니라 원본 canonical duration으로 판정한다.
- planning replay마다 동일 입력은 동일 완료 상태를 만든다.

## 3. 1초 미만 작업

예:

```text
건설 총 duration = 0.5초
→ 명령 accept
→ branch elapsed = 0.5초
→ lifecycle = COMPLETED
```

결과:

- planning branch 화면에서는 완성된 건물로 표시한다.
- node는 완성 건물이 점유한 상태다.
- 완성 건물이 제공하는 branch capability를 후속 명령이 참조할 수 있다.
- live authoritative world에는 confirm 전 건물이 생성되지 않는다.
- live gold·food·registry·simulation clock은 confirm 전 변경하지 않는다.

## 4. 정확히 1초 작업

예:

```text
업그레이드 총 duration = 1.0초
→ 명령 accept
→ branch elapsed = 1.0초
→ lifecycle = COMPLETED
→ target tier 활성
```

정확히 1초인 작업을 `duration - epsilon`에서 강제 정지하지 않는다.

금지:

- 완료 직전 상태를 인위적으로 유지.
- 전투 재개 후 첫 tick까지 완료를 늦춤.
- 렌더 프레임에 따라 완료 여부 변경.
- confirm에서 추가 1초를 적용해 2초로 만듦.

## 5. Branch-visible 완료 capability

완료된 short work는 planning branch의 후속 명령 판정에 완료 상태로 사용한다.

예:

```text
R1: 0.5초 시설 건설
→ branch에서 COMPLETED
→ capability = RALLY_POINT_TARGET 제공

R2: 해당 시설 집결지 설정
→ R1의 완료 capability를 참조
→ dependency가 유효하면 허용
```

필수 규칙:

- consumer는 explicit provisional ID와 output slot을 참조한다.
- producer의 `reservation_sequence`는 consumer보다 앞서야 한다.
- 완료 capability는 producer output contract에 명시되어야 한다.
- UI 이름 유사성이나 같은 node라는 이유로 암묵 연결하지 않는다.
- 후속 명령은 현재 planning branch와 virtual ledger를 기준으로 검증한다.

## 6. 완료 상태와 외부 부작용 분리

planning branch에서 lifecycle이 `COMPLETED`여도 live 외부 부작용은 아직 발생하지 않는다.

branch에서 허용:

- 완료 lifecycle 표시.
- node 점유.
- target tier·구조적 capability 노출.
- 후속 dependency 판정.
- virtual capacity·virtual resource 계산.

confirm까지 보류:

- live 객체 registry 등록.
- live TokenSource 등록.
- 실제 생산 tick 시작.
- 실제 쿨다운 시작 또는 감소.
- 로그·업적·통계 기록.
- 오디오·VFX·알림 이벤트.
- 실제 자원 원장 반영.

필수 원칙:

```text
branch structural completion
!=
live external side-effect execution
```

주기적 생산·회복·수리·쿨다운은 global simulation이 정지되어 있으므로 planning 중 tick하지 않는다.

## 7. Planning queue replay

명령 추가·수정·취소 시 `PlanningEntrySnapshot`부터 전체 queue를 다시 재생성한다.

```text
queue mutation
→ queue_revision 증가
→ entry snapshot 복사
→ reservation_sequence 순서로 전체 replay
→ 각 short work에 canonical headstart 한 번 적용
→ completion과 capability 재계산
→ 전체 dependency·resource·lifecycle 검증
```

금지:

- 기존 branch elapsed에 다시 1초를 더함.
- replay 횟수에 따라 0.5초 작업이 여러 번 완료 이벤트를 생성.
- 명령 수정으로 과거 completion side effect를 유지.
- 취소된 producer의 완료 capability를 dependent가 계속 사용.

같은 queue revision을 순수 재평가하면 동일한 branch hash와 완료 결과를 만들어야 한다.

## 8. 취소와 수정

완료된 short work 명령을 취소하면 완료 상태도 가역적으로 사라진다.

예:

```text
R1: 0.5초 시설 건설 → branch COMPLETED
R2: R1 시설을 참조

R1 취소
→ 승인된 dependent cascade preview
→ 명시적 동의
→ R1과 영향 dependent 제거
→ entry snapshot부터 replay
→ 시설·capability·virtual debit 제거
```

수정으로 total duration 또는 output contract가 달라지면 최신 값으로 처음부터 판정한다.

- 0.5초에서 2초로 변경 → `IN_PROGRESS`, elapsed 1초.
- 2초에서 0.5초로 변경 → `COMPLETED`, elapsed 0.5초.
- output identity 변경 → 기존 consumer reference는 재검증한다.
- stale preview·consent는 재사용하지 않는다.

## 9. Confirm과 원자 승격

`[확정/전투 재개]`는 short work를 다시 실행하는 시점이 아니다. 최신 authoritative basis에서 branch를 재생성하고 최종 branch 상태를 live world에 원자 승격하는 시점이다.

```text
SpinSession CLOSED 확인
→ authoritative basis 재확인
→ 최신 queue revision 전체 replay
→ short work completion 재계산
→ PlanningCommitPlan 생성
→ resource debit + final object state + completion side effects 원자 적용
→ PlanningCommitReceipt 기록
→ NORMAL_COMBAT 재개
```

성공 시:

- branch `COMPLETED` 객체는 live에서도 완료 상태가 된다.
- 완료 capability와 registry entry를 정확히 한 번 생성한다.
- completion event를 정확히 한 번 기록한다.
- 후속 명령 결과도 같은 atomic batch에 적용한다.
- planning에서 사용한 headstart를 다시 더하지 않는다.

허용 결과:

```text
전체 branch promotion 성공 + receipt
또는
live 상태 변경 0
```

## 10. Confirm 실패

하나라도 최종 검증에 실패하면 다음은 모두 0이어야 한다.

- live 건물 생성·업그레이드 완료.
- live node 점유 변경.
- live capability·TokenSource registry 등록.
- live gold·food 차감.
- completion event·로그·업적 기록.
- 후속 명령 적용.
- simulation time advance.

planning branch와 queue는 유지하며 최신 차단 이유를 표시한다.

## 11. Idempotency

동일 `planning_commit_transaction_id` 재요청은 기존 `PlanningCommitReceipt`를 반환한다.

중복 요청은 다음을 만들지 않는다.

- short work 재완료.
- completion event 중복.
- registry 중복 등록.
- 자원 재차감.
- node 재점유.
- dependent 재적용.
- simulation 재개 중복.

Receipt는 최소 다음을 포함한다.

```text
planning_session_id
queue_revision
planning_commit_transaction_id
completed_short_work_reservation_ids
committed_object_ids
committed_lifecycle_states
applied_completion_side_effect_ids
resource_mutation_receipt_ids
final_branch_hash
```

## 12. 범위 경계

이 문서는 다음을 새로 정의하지 않는다.

- `PREPARATION`의 기존 즉시 적용 규칙.
- `DANGER_COMBAT`의 실시간 명령 규칙.
- 룰렛 이동의 즉시 소비 규칙.
- 일반 생산 queue·수리 queue의 별도 정책.
- 여러 short work를 한 대상에서 연속 체인하는 허용 범위.

특히 다음은 후속 검수다.

```text
MULTI_STAGE_SHORT_WORK_CHAIN_POLICY: REVIEW_PENDING
```

예:

```text
R1: 0.5초 Tier 1 건설 → COMPLETED
R2: 0.5초 Tier 2 업그레이드 → ?
R3: 0.5초 Tier 3 업그레이드 → ?
```

현재 문서는 개별 short work가 1초 이하일 때 자신의 branch 완료 경계만 확정한다.

## 13. 자동 검증 계약

최소 다음 사례를 검증한다.

1. duration 0.5초 → branch `COMPLETED`, elapsed 0.5초.
2. duration 정확히 1초 → inclusive branch `COMPLETED`.
3. duration 1초 초과 → branch `IN_PROGRESS`, elapsed 1초.
4. fixed-point tick 비교로 float epsilon 비의존.
5. short work 완료 capability를 후속 explicit consumer가 사용 가능.
6. periodic production·cooldown·wave는 planning 중 tick 0.
7. queue replay 반복 → elapsed·completion 누적 0.
8. short work 취소 → entry snapshot부터 복원, capability 제거.
9. duration 수정 → 최신 duration으로 완료 상태 재계산.
10. confirm 성공 → final completed state와 completion side effect 정확히 1회.
11. confirm에서 headstart 재적용 0.
12. confirm 실패 → live completion·registry·resource·time mutation 0.
13. 동일 planning commit transaction 재요청 → 같은 receipt, 중복 0.
14. 준비·위험 전투 경로의 기존 규칙 불변.
15. multi-stage short-work chain은 현재 문서에서 승인하지 않음.

## 14. 현재 상태

```text
PLANNING_HEADSTART_COMPLETION_THRESHOLD: DURATION_LE_ONE_SECOND
ONE_SECOND_COMPLETION_BOUNDARY: INCLUSIVE
SHORT_TIMED_WORK_BRANCH_RESULT: COMPLETED
SHORT_TIMED_WORK_LIVE_PROMOTION: CONFIRM_ONLY
BRANCH_COMPLETION_CAPABILITIES: AVAILABLE_TO_LATER_COMMANDS
BRANCH_COMPLETION_EXTERNAL_SIDE_EFFECTS: DEFERRED_TO_COMMIT
FIXED_POINT_DURATION_COMPARISON: REQUIRED
CONFIRM_REAPPLIES_HEADSTART: FORBIDDEN
CONFIRM_DUPLICATES_COMPLETION_EVENT: FORBIDDEN
MULTI_STAGE_SHORT_WORK_CHAIN_POLICY: REVIEW_PENDING
PRODUCT_CODE_AUTHORIZED: NO
V2_IMPLEMENTATION: NOT_STARTED
HUMAN_QA: NOT_RUN
CORE_LOCK_V2: PENDING
```
