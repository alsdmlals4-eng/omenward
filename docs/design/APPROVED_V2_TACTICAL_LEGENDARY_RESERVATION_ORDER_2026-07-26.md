# 승인된 V2 전술계획 전설 예약 순서 계약

- 승인일: 2026-07-26
- 상태: `APPROVED_POST_LEGENDARY_POLICY_AMENDMENT / V2_IMPLEMENTATION_NOT_STARTED`
- 제품 코드 승인: `NO`
- 승인 근거: 사용자가 예약 순서 기반 가상 상태 검증 권장안을 승인
- 상위 책임: 최신 사용자 지시, `docs/PROJECT_CORE.md`
- 부모 계약: `docs/design/APPROVED_V2_LEGENDARY_DEPLOYMENT_LIMIT_2026-07-26.md`
- 관련 시간 규칙: `docs/design/APPROVED_MAPRUN_STAGE_WAVE_AND_MIDPOINT_CORE_V1.md`

이 문서는 일반 전투의 `TACTICAL_PLANNING`에서 전설 배치 예약이 둘 이상일 때의 순서·경고·동의·재개 transaction을 확정한다. 부모 전설 계약을 확장하며 충돌 시 이 문서의 전술계획 조항이 우선한다. 위험 전투의 즉시 배치는 부모 계약의 live 커밋 재검증을 그대로 사용한다.

## 1. 해결하는 충돌

```text
현재 생존 전설 0기
→ 전설 A 배치 예약
→ 전설 B 배치 예약
→ [전투 재개]
```

예약 명령은 아직 실제 spawn되지 않았으므로 live 생존 전설 수에는 포함되지 않는다. 그러나 두 명령을 모두 전설로 예약하면 동시 적용 순간 생존 전설 상한 1을 위반한다.

승인된 해법은 예약 명령을 안정적 순서로 가상 적용하여 첫 적격 전설만 전설 슬롯을 차지하고, 후속 전설에는 재개 전에 영웅 2기 변환 동의를 받는 것이다.

## 2. 안정적 식별자와 순서

각 세션과 예약 명령은 다음 식별자를 가진다.

```text
planning_session_id
planning_revision
planning_command_id
reservation_sequence
```

- `planning_command_id`는 예약 내용을 수정해도 유지한다.
- 삭제 후 새로 생성한 명령은 새 ID를 받는다.
- `reservation_sequence`는 세션 안에서 중복될 수 없다.
- 평가 순서는 `reservation_sequence` 오름차순이다.
- 같은 sequence나 command ID 충돌은 invariant violation이다.
- 라인, UI 카드 위치, Dictionary 순회 또는 spawn 호출 순서를 암묵적 우선순위로 사용하지 않는다.

## 3. 가상 전장 상태

전술계획 진입 또는 큐 재평가 시 authoritative 전장의 실제 생존 전설 수를 시작값으로 사용한다.

```text
virtual_alive_legendary_count = authoritative alive legendary count

for command in ordered reservations:
    일반 명령 → preview-only 자원 효과 적용
    전설 명령 + virtual count 0 → 전설 1기 preview, virtual count = 1
    전설 명령 + virtual count 1 → 변환 경고, 동의 후 영웅 2기 preview
    virtual count 2 이상 → invariant violation
```

- 아직 spawn되지 않은 예약은 live 생존 전설 수에는 포함하지 않는다.
- 같은 계획 큐의 후속 명령 검증에는 가상 전설 슬롯 점유로 포함한다.
- 순서상 가장 이른 적격 전설 명령이 전설 1기 결과를 가진다.
- 후속 충돌 명령은 명시적 동의 전까지 미완료 경고 상태다.
- 동의가 없으면 `[전투 재개]`를 차단한다.
- preview는 PendingReward·식량·전장·로그를 변경하지 않는다.

## 4. 예약 수정·삭제·재정렬

예약 큐가 변경될 때마다 첫 명령부터 전체 큐를 다시 계산한다.

- 앞선 전설 예약을 삭제하거나 뒤로 옮기면 후속 명령이 전설 1기로 복원될 수 있다.
- 앞선 전설 예약을 추가하거나 앞으로 옮기면 후속 명령에 새 변환 경고가 필요할 수 있다.
- 충돌이 사라지면 기존 영웅 변환 동의를 폐기하고 전설 1기 preview로 복원한다.
- 새 충돌에는 과거 다른 충돌의 동의를 재사용하지 않는다.
- 예상 식량은 현재 결과에 따라 전설 1기분 또는 영웅 2기분으로 다시 계산한다.

## 5. 동의 근거와 stale 방지

영웅 변환 동의는 단순 boolean이 아니라 다음 근거와 묶는다.

```text
planning_session_id
planning_revision
planning_command_id
conflict_basis_hash
expected_source_pending_reward_id
expected_output = hero_x2
```

`conflict_basis_hash`는 최소 다음을 결정론적으로 포함한다.

- authoritative 생존 전설 ID 또는 0기 상태.
- 현재 명령보다 앞선 전설 예약 command ID와 예상 결과.
- 현재 `reservation_sequence`.
- 원본 전설 PendingReward ID.
- 선택 라인.
- 영웅 2기분 식량 요구량.

큐 수정이나 authoritative 상태 변경으로 근거가 달라지면 동의를 stale로 폐기한다. stale 동의를 이용한 자동 강등은 금지한다.

## 6. 전투 재개 재검증

`[전투 재개]`는 UI preview를 신뢰해 바로 적용하지 않는다.

1. authoritative 전장·PendingReward·식량·planning revision을 다시 읽는다.
2. 최종 예약 순서로 가상 평가를 처음부터 다시 실행한다.
3. 각 영웅 변환 동의의 `conflict_basis_hash`를 검증한다.
4. 모든 예약 명령·비용·spawn 조건을 포함한 `PlanningCommitPlan`을 만든다.
5. 전체 검증이 통과한 경우에만 비용을 일괄 차감하고 명령을 동시에 적용한다.

다음 경우 전체 재개 transaction을 무변경 거부하고 전술계획을 유지한다.

- 새 충돌이 생겨 추가 동의가 필요함.
- 변환 동의가 stale임.
- 식량 또는 다른 비용 부족.
- PendingReward가 사라지거나 이미 처리됨.
- 예약 sequence·ID·revision 충돌.
- authoritative 생존 전설이 2기 이상임.
- 하나라도 필수 spawn 조건을 만족하지 못함.

충돌이 사라진 경우 불필요한 영웅 변환을 하지 않고 전설 1기로 재계산한다. 최종 preview도 같은 결과로 갱신돼 있어야 한다.

## 7. 동시 적용과 원자성

예약 명령은 재개 시 동시에 적용되지만 전설 슬롯과 변환 여부는 예약 순서 평가로 결정한다.

```text
현재 생존 전설 0기
sequence 10: 전설 A 상단 → 전설 A 1기
sequence 20: 전설 B 하단 → 동의 후 영웅 B 2기
[전투 재개] → A 전설 1기와 B 영웅 2기를 같은 원자 batch로 spawn
```

- 실제 spawn 호출 순서를 전설 우선순위로 사용하지 않는다.
- 일부 spawn 실패 시 해당 planning batch의 비용·pending·spawn·로그를 전부 rollback한다.
- 동일 `planning_session_id + planning_revision` 재요청은 새 유닛을 만들지 않고 기존 `PlanningCommitReceipt`를 반환한다.

## 8. UI 계약

- 각 예약 카드에 예상 결과 `전설 1기` 또는 `영웅 2기`를 표시한다.
- 예상 식량과 변환 이유를 함께 표시한다.
- 예약 삭제·재정렬 시 후속 카드와 경고 상태를 즉시 다시 계산한다.
- 미동의 또는 stale 동의 명령은 `[전투 재개]` 차단 이유를 명확히 표시한다.
- 충돌이 사라져 전설 1기로 복원된 경우 결과 변경을 표시한다.

## 9. 자동 검증 계약

1. 생존 전설 0기, 전설 예약 2개 → 첫 명령 전설 1기, 두 번째 경고 후 영웅 2기 preview.
2. 두 번째 명령 미동의 → 재개 무변경 거부.
3. 첫 명령 삭제 → 두 번째가 전설 1기로 복원되고 과거 동의 폐기.
4. 예약 순서 교환 → 새 첫 명령만 전설, 후속 동의 재검증.
5. 비전설 명령 이동으로 전설 상대 순서가 같으면 결과 불변.
6. 큐 수정 후 stale basis hash → 자동 강등 없이 재경고.
7. 재개 직전 authoritative 생존 전설 신규 발생 → 전체 무변경 거부·최신 경고 요구.
8. authoritative 생존 전설 소멸 → 불필요한 변환 없이 전설로 재계산.
9. 영웅 2기분 식량 부족 → 전체 batch 무변경 거부.
10. 일부 spawn 실패 → 비용·pending·spawn·로그 전체 rollback.
11. 동일 planning receipt 재요청 → 중복 spawn 0.
12. 위험 전투 즉시 배치 경로는 예약 큐 없이 부모 계약의 커밋 재검증 사용.

사람 검증은 플레이어가 예약 순서, 첫 전설 슬롯, 영웅 변환 preview, 재정렬 후 결과 변화와 재개 차단 이유를 설명할 수 있는지 확인한다.

## 10. 현재 상태

```text
TACTICAL_PLANNING_LEGENDARY_RESERVATION: ORDERED_VIRTUAL_SIMULATION
QUEUE_MUTATION_REEVALUATION: REQUIRED
CONSENT_BASIS_HASH: REQUIRED
TACTICAL_RESUME_REVALIDATION: REQUIRED
TACTICAL_BATCH_APPLY: ATOMIC
AUTO_DOWNGRADE_WITH_STALE_CONSENT: FORBIDDEN
PRODUCT_CODE_AUTHORIZED: NO
V2_IMPLEMENTATION: NOT_STARTED
HUMAN_QA: NOT_RUN
CORE_LOCK_V2: PENDING
```
