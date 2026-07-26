# 승인된 기존 live 작업 전술계획 정지 계약

- 승인일: 2026-07-26
- 상태: `V2_SPEC_APPROVED / PRODUCT_CODE_NOT_AUTHORIZED`
- 승인 근거: 사용자 직접 승인
- 상위 책임:
  - `docs/design/APPROVED_V2_PLANNING_SHARED_ONE_SECOND_HORIZON_2026-07-26.md`
  - `docs/design/APPROVED_V2_PLANNING_ONE_SECOND_HEADSTART_2026-07-26.md`
  - `docs/design/APPROVED_V2_PLANNING_SHORT_WORK_COMPLETION_2026-07-26.md`
  - `docs/design/APPROVED_V2_SIMULTANEOUS_COMMAND_START_AND_TIME_RESUME_2026-07-26.md`
  - `docs/design/APPROVED_V2_PLANNING_REVALIDATION_ALL_OR_NOTHING_2026-07-26.md`
  - `docs/design/APPROVED_V2_TRANSACTION_FOUNDATION_SEQUENCE_2026-07-26.md`

이 문서는 일반 `TACTICAL_PLANNING` 진입 전에 이미 live authoritative world에서 진행 중이던 건설·업그레이드 등 시간 기반 작업이 planning horizon의 1초 선행 진행을 받을 수 있는지와, 해당 작업의 progress·timer·completion capability·confirm 승격 규칙을 소유한다.

## 1. 승인된 핵심 결정

```text
EXISTING_LIVE_WORK_HEADSTART_ELIGIBILITY: NOT_ELIGIBLE
PLANNING_SESSION_CREATED_WORK_HEADSTART: ELIGIBLE
PLANNING_ENTRY_LIVE_WORK_PROGRESS_SNAPSHOT: PRESERVED
EXISTING_LIVE_WORK_PROGRESS_DURING_PLANNING: FROZEN
EXISTING_LIVE_WORK_COMPLETION_DURING_PLANNING_HORIZON: FORBIDDEN
PLANNING_REENTRY_FREE_PROGRESS: FORBIDDEN
EXISTING_LIVE_WORK_TIMER_REBASE_ON_CONFIRM: FORBIDDEN
POST_CONFIRM_EXISTING_LIVE_WORK_RESUME: FROM_ENTRY_PROGRESS
EXPLICIT_COMMAND_TRANSITION_ON_EXISTING_WORK: ALLOWED_BY_COMMAND_CONTRACT
PASSIVE_HORIZON_PROGRESS_ON_EXISTING_WORK: FORBIDDEN
FAILED_CONFIRM_EXISTING_LIVE_WORK_MUTATION: ZERO
DANGER_COMBAT_SCOPE: EXCLUDED
PRODUCT_CODE_AUTHORIZED: NO
```

승인된 기본 흐름:

```text
live 작업 progress 캡처
→ 전술계획 진입
→ 기존 live 작업 progress 고정
→ 현재 session에서 새로 생성된 작업만 공유 [0, 1초] horizon 사용
→ confirm 성공
→ 기존 live 작업은 캡처한 progress부터 정상 재개
```

## 2. 적용 범위

대상은 `TACTICAL_PLANNING` 진입 시점에 이미 live world에서 다음 상태인 작업이다.

- `UNDER_CONSTRUCTION`인 기존 건설 작업.
- `UPGRADING`인 기존 업그레이드 작업.
- 향후 승인되는 수리·생산·충전 작업 중 command schema가 이 계약을 참조하는 작업.

이 문서는 다음을 새로 정의하지 않는다.

- 위험 전투의 실시간 진행.
- 준비 화면의 즉시 적용.
- 룰렛 이동 또는 보상 산출.
- 기존 live 작업 취소 시 환불률.
- 수리·생산 queue의 세부 lifecycle.

## 3. PlanningEntrySnapshot

전술계획 진입 시 기존 live 작업마다 최소 다음 값을 캡처한다.

```text
ExistingLiveWorkEntrySnapshot
- work_id
- target_id
- work_type
- lifecycle
- total_duration_ticks
- elapsed_ticks_at_entry
- remaining_ticks_at_entry
- completion_output_fingerprint
- timer_basis_revision
- resource_commit_basis
```

필수 불변식:

```text
elapsed_ticks_in_planning = elapsed_ticks_at_entry
remaining_ticks_in_planning = remaining_ticks_at_entry
```

planning 화면 체류 시간, wall-clock 시간, UI 애니메이션 프레임 수는 위 값을 바꾸지 않는다.

## 4. 공유 1초 horizon eligibility

공유 planning horizon은 현재 planning session에서 받아들인 신규 시간 기반 명령에만 적용한다.

```text
if work.created_by_current_planning_session:
    shared_horizon_eligible = true
else if work.existed_in_live_world_at_entry:
    shared_horizon_eligible = false
```

예:

```text
병영 건설 총 10초
전술계획 진입 시 elapsed = 6초

planning horizon 종료
→ elapsed = 6초
→ remaining = 4초
→ COMPLETED 아님
```

금지:

- 진입마다 기존 작업에 1초 추가.
- planning queue replay마다 기존 작업에 1초 추가.
- confirm 때 기존 작업에 horizon 재적용.
- session을 반복 진입해 작업을 무료 가속.
- 남은 시간이 1초 이하라는 이유로 planning 중 자동 완료.

## 5. 기존 작업과 신규 작업의 병존

기존 live 작업과 현재 session 신규 작업은 서로 다른 progress 규칙을 사용한다.

```text
기존 live 작업 A: entry progress에서 정지
신규 planning 작업 B: 공유 [0, 1초] horizon에서 진행
```

예:

```text
A: 기존 성벽 업그레이드, entry elapsed 6초 / 총 10초
B: 신규 병영 건설, 총 3초

planning 결과
A elapsed = 6초
B elapsed = 1초
```

독립 여부와 관계없이 A는 horizon time을 소비하지도, horizon에서 진행하지도 않는다. B는 다른 신규 ready 작업과 같은 가상 시간축에서 병렬 진행할 수 있다.

## 6. Completion capability

기존 live 작업이 entry 시점에 미완료라면 planning horizon 동안 완료 capability를 새로 제공하지 않는다.

```text
entry lifecycle = IN_PROGRESS
→ planning lifecycle = IN_PROGRESS
→ completion output unavailable
```

남은 시간이 0.2초여도 동일하다.

```text
entry remaining = 0.2초
→ planning 중 progress 증가 0
→ planning 중 completion capability 없음
```

따라서 해당 완료 output을 필수로 참조하는 신규 명령은 현재 planning branch에서 유효하지 않다.

```text
DEPENDENT_REQUIRES_FROZEN_EXISTING_WORK_COMPLETION
→ BLOCKED_OR_REJECTED_BY_COMMAND_CONTRACT
```

이미 entry 시점에 완료된 live capability는 일반 authoritative input으로 사용할 수 있다.

## 7. 명시적 명령에 의한 상태 변경

기존 작업이 planning 중 자동 진행하지 않는다는 것은 해당 대상을 명시적으로 조작할 수 없다는 뜻이 아니다.

허용 예:

- 기존 업그레이드 중 건물 철거 요청.
- 향후 승인된 작업 취소 명령.
- 대상 lifecycle을 변경하는 별도 명령.

이 경우 상태 변화는 planning horizon의 passive elapsed가 아니라 command contract의 명시적 transition으로 계산한다.

```text
existing work frozen
+ explicit demolition command
→ impact preview
→ explicit confirmation
→ command-defined cancellation or demolition transition
```

금지:

- 철거 preview를 만들기 위해 기존 작업을 1초 진행.
- 작업 취소 전에 completion을 먼저 계산.
- command transition과 passive horizon progress를 혼합.

## 8. Queue mutation과 replay

명령 추가·수정·취소 시 planning branch를 entry snapshot부터 전체 replay한다.

```text
queue mutation
→ queue_revision 증가
→ PlanningEntrySnapshot 복사
→ 기존 live 작업 progress를 entry 값으로 복원
→ 고정 reservation_sequence로 명시적 명령 replay
→ 신규 시간 기반 작업에만 공유 horizon 계산
→ 전체 dependency·resource·lifecycle 재검증
```

필수 규칙:

- 기존 live 작업의 `elapsed_ticks_at_entry`는 모든 replay에서 동일하다.
- 기존 live 작업에 과거 planning 결과를 carry하지 않는다.
- 신규 작업 horizon도 replay 횟수에 따라 누적하지 않는다.
- 동일 queue revision의 순수 replay는 동일 branch hash를 만든다.

## 9. Confirm과 정상 재개

`[확정/전투 재개]` 성공 시 기존 live 작업 timer를 새로 시작하거나 1초 앞당기지 않는다.

```text
existing_elapsed_after_commit = elapsed_ticks_at_entry
existing_remaining_after_commit = remaining_ticks_at_entry
```

단, planning branch에서 명시적 취소·철거 transition이 승인됐다면 해당 command 결과를 원자 적용한다.

일반적인 untouched 기존 작업:

```text
entry elapsed 6초
→ planning 중 6초
→ confirm 성공
→ live elapsed 6초
→ 다음 simulation tick부터 6초 이후 진행
```

필수 규칙:

- `PlanningCommitReceipt` 기록 이전에 live simulation을 재개하지 않는다.
- confirm 처리 wall-clock 시간은 progress에 포함하지 않는다.
- timer epoch를 현재 wall-clock에 맞춰 재설정해 progress를 보정하지 않는다.
- 기존 작업 completion event는 실제 remaining duration이 live simulation에서 경과한 뒤 발생한다.

## 10. Confirm 실패와 rollback

confirm 검증이 하나라도 실패하면 다음 mutation은 모두 0이다.

- 기존 live 작업 progress 변경.
- 기존 live 작업 timer basis 변경.
- 기존 live 작업 completion.
- 신규 planning 작업 promotion.
- resource debit.
- simulation time resume.

```text
FAILED_CONFIRM_EXISTING_LIVE_WORK_MUTATION: ZERO
```

플레이어는 기존 planning session을 유지한 채 문제를 수정할 수 있으며, 기존 live 작업은 entry progress로 계속 표시한다.

## 11. Idempotency

동일 `planning_commit_transaction_id` 재요청은 같은 receipt를 반환한다.

중복 금지:

- 기존 작업 progress 추가.
- 기존 timer 재등록.
- 신규 작업 horizon 재적용.
- completion event 중복.
- resource debit 중복.
- simulation resume 중복.

`PlanningCommitReceipt`에는 최소 다음 증거를 포함한다.

```text
planning_commit_transaction_id
planning_session_id
entry_simulation_tick
ordered_existing_live_work_ids
existing_work_entry_elapsed_ticks
ordered_new_planning_work_ids
new_work_branch_elapsed_ticks
queue_revision
branch_hash
```

## 12. 사용자 예시

```text
병영 건설 총 10초
현재 live 진행도 6초
→ 전술계획 진입
→ planning 중 6초 유지
→ 신규 화살탑 건설 명령은 공유 horizon에서 1초 진행
→ 확정
→ 병영은 6초부터 재개
→ 화살탑은 branch에서 계산한 1초 상태로 승격 후 이후 진행
```

반복 진입:

```text
병영 6초
→ planning 진입·아무 명령 없이 종료
→ 병영 6초
→ 다시 planning 진입
→ 병영 6초
```

## 13. 적대적 검수 체크리스트

- [ ] 기존 live 작업은 shared horizon eligibility가 없다.
- [ ] entry progress가 planning 중 유지된다.
- [ ] 남은 시간이 1초 이하라도 planning 중 완료되지 않는다.
- [ ] 반복 planning 진입으로 무료 progress를 얻을 수 없다.
- [ ] 신규 planning 작업만 공유 horizon에서 진행한다.
- [ ] 기존 작업 완료를 요구하는 dependent는 capability가 없으면 차단된다.
- [ ] 명시적 철거·취소 transition과 passive progress를 구분한다.
- [ ] replay가 기존 progress 또는 신규 horizon을 누적하지 않는다.
- [ ] confirm에서 기존 timer를 rebase하거나 1초를 추가하지 않는다.
- [ ] 실패 시 live mutation이 0이다.
- [ ] duplicate transaction이 같은 receipt를 반환한다.
- [ ] 위험 전투와 제품 코드 범위를 확장하지 않는다.

## 14. 상태

```text
F-25_RESULT: APPROVED
EXISTING_LIVE_WORK_HEADSTART_POLICY: RESOLVED_FROZEN_AT_ENTRY_PROGRESS
EXISTING_LIVE_WORK_CANCELLATION_ECONOMICS: REVIEW_PENDING
V2_IMPLEMENTATION: NOT_STARTED
PRODUCT_CODE_AUTHORIZED: NO
```
