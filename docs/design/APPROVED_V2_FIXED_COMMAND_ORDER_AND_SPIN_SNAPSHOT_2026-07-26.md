# 승인된 고정 명령 순서·불변 SpinSnapshot 계약

- 승인일: 2026-07-26
- 상태: `V2_SPEC_APPROVED / PRODUCT_CODE_NOT_AUTHORIZED`
- 승인 근거: 사용자 확인 — 명령 순서 변경 기능이 없고, 명령 확정·시간 진행 전에는 authoritative 상태가 변하지 않음
- 상위 책임:
  - `docs/design/APPROVED_V2_PRODUCER_OUTPUT_FINGERPRINT_CASCADE_2026-07-26.md`
  - `docs/design/APPROVED_V2_PLANNING_DEPENDENCY_DAG_AND_PROVISIONAL_IDS_2026-07-26.md`
  - `docs/design/APPROVED_V2_SPIN_SESSION_TACTICAL_RESUME_GATE_2026-07-26.md`
  - `docs/design/APPROVED_V2_PLANNING_REVALIDATION_ALL_OR_NOTHING_2026-07-26.md`
  - `docs/design/APPROVED_V2_TRANSACTION_FOUNDATION_SEQUENCE_2026-07-26.md`

이 문서는 일반 `TACTICAL_PLANNING`에서 명령 순서를 사용자가 재정렬하지 않는 UI 계약, 확정 전 무변경 원칙, 룰렛 결과의 불변 snapshot 기준과 계획 재검증 범위를 소유한다.

이 문서는 다음 미결정 상태를 명시적으로 대체한다.

```text
DEPENDENCY_REORDER_POLICY: REVIEW_PENDING
```

## 1. 승인된 핵심 결정

```text
COMMAND_REORDER_UI: NOT_SUPPORTED
COMMAND_EXECUTION_ORDER: SYSTEM_ASSIGNED_CREATION_SEQUENCE
RESERVATION_SEQUENCE_USER_MUTATION: FORBIDDEN
AUTHORITATIVE_MUTATION_BEFORE_CONFIRM: FORBIDDEN
SIMULATION_TIME_ADVANCE_BEFORE_CONFIRM: FORBIDDEN
PLANNING_EDIT_SCOPE: PLAN_DATA_ONLY
ROULETTE_REWARD_BASIS: IMMUTABLE_SPIN_SNAPSHOT
PLANNING_QUEUE_MUTATION_RECOMPUTES_ROULETTE_RESULT: FORBIDDEN
CONFIRMED_PENDING_REWARD_IDENTITY: IMMUTABLE
PLANNING_REVALIDATION_SCOPE: COMMAND_EFFECTS_AND_CURRENT_PRECONDITIONS_ONLY
```

## 2. 전술계획 명령 순서

플레이어는 예약 명령을 드래그하거나 위·아래 버튼으로 재정렬할 수 없다.

명령이 생성될 때 시스템이 안정적인 순서를 부여한다.

```text
planning_session_id
planning_command_id
reservation_sequence
created_from_queue_revision
```

필수 규칙:

- `reservation_sequence`는 planning session 안에서 고유하다.
- 새 명령은 기존 명령 뒤의 새 sequence를 받는다.
- 명령 수정은 기존 command ID와 sequence를 유지한다.
- 명령 삭제 뒤 남은 sequence를 사용자 표시 편의를 위해 재번호화하지 않는다.
- 삭제된 sequence를 같은 session에서 새 명령에 재사용하지 않는다.
- UI 카드 배열, 렌더 순서, dictionary 순회 순서는 권위가 아니다.
- 사용자가 임의 sequence를 입력하거나 변경할 수 없다.

## 3. 확정 전 무변경

계획 중 명령 추가·수정·취소는 planning 데이터만 변경한다.

확정 전 변경 금지 대상:

```text
global gold ledger
food usage and capacity
building authoritative state
TokenSource and live reel
PendingReward consumption
battlefield units
skill cost, cooldown, and effects
simulation clock
wave progression
```

따라서 계획 편집은 실제 건설, 업그레이드, 배치, 스킬 실행 또는 시간 진행이 아니다.

```text
계획 편집
→ queue_revision 증가
→ preview·report·consent stale 처리
→ 순수 재검증
→ authoritative mutation 0
```

## 4. 명령 확정과 시간 진행

플레이어가 `[확정]` 또는 해당 UX의 명령 확정·시간 진행 동작을 선택할 때만 전체 계획 commit을 시도한다.

```text
SpinSession CLOSED 확인
→ 현재 authoritative basis 읽기
→ 시스템 생성 순서대로 전체 명령 순수 replay
→ dependency·비용·식량·동의·spawn 조건 검증
→ PlanningCommitPlan 생성
→ 전체 batch 원자 commit
→ receipt 기록
→ simulation 시간 진행
```

하나라도 실패하면:

```text
PlanningRevalidationReport = BLOCKED
→ authoritative mutation 0
→ simulation time advance 0
→ 계획 화면 유지
```

## 5. Dependency와 순서

재정렬 UI가 없으므로 dependency-safe drop 범위나 자동 block 이동 정책은 존재하지 않는다.

대신 생성 시 다음을 검증한다.

- consumer는 이미 큐에 존재하는 더 이른 producer만 참조할 수 있다.
- 미래 producer를 참조하는 명령 생성은 거부한다.
- producer 삭제·수정은 승인된 영향 preview와 cascade 정책을 따른다.
- consumer를 producer보다 앞으로 이동시키는 사용자 동작은 지원하지 않는다.

이로써 큐는 편집 중에도 `producer.reservation_sequence < consumer.reservation_sequence` 불변 조건을 유지한다.

## 6. 룰렛 결과 기준

룰렛 보상은 룰렛 회전 시점에 캡처한 불변 `SpinSnapshot`을 기준으로 판독한다.

```text
회전 시작
→ SpinSnapshot 캡처
→ 정지 위치 판독
→ 허용된 이동 아이템 명령 적용
→ 같은 snapshot과 이동 내역으로 최종 결과 계산
→ ConfirmReceipt
→ PendingReward 생성
```

`SpinSnapshot`은 최소 다음 회전 기준 정보를 고정한다.

```text
spin_session_id
spin_snapshot_revision
roulette reel contents
TokenSource contribution state
lane and reel identity
rotation seed or deterministic stop basis
eligible movement item state captured by roulette contract
```

계획 큐의 다음 변화는 이미 열린 또는 확정된 룰렛 결과를 다시 계산하지 않는다.

- 건물 건설·업그레이드 예약 추가·수정·취소.
- TokenSource 관련 계획 명령 변경.
- 배치·스킬 예약 변경.
- 계획 비용·식량 preview 변경.
- producer dependency 변경.
- planning queue revision 변경.

## 7. 이동 아이템과 최종 보상

회전 직후 허용된 이동 아이템은 동일 `SpinSnapshot` 위에서 결과 위치를 변경한다.

```text
immutable SpinSnapshot
+ deterministic stop result
+ explicitly accepted movement history
= final reward payload basis
```

계획 큐 변화가 이동 내역을 자동 추가·삭제하거나 룰렛을 재회전시키지 않는다.

확정된 `PendingReward`의 정체성은 이후 planning 재검증으로 변경하지 않는다.

변경 금지 예:

- 보상 등급 재추첨.
- 보상 unit family 재추첨.
- source building 또는 source tier 재해석.
- 다른 roulette cell로 자동 이동.
- 현재 live TokenSource 상태를 사용한 재산출.

## 8. 전설 배치와 룰렛 보상의 분리

전설 `PendingReward` 자체는 불변이다.

다만 전장 배치 시점의 생존 전설 상태와 명령 생성 순서에 따라 실제 배치 형태는 재검증할 수 있다.

```text
PendingReward identity = legendary unit reward

planning deployment result:
- 전설 슬롯 비어 있음 → 전설 1기
- 선행 명령 또는 authoritative 전설과 충돌 → 최신 동의가 있으면 영웅 2기
```

이는 룰렛 보상 재산출이 아니라 배치 정책 적용이다.

금지:

```text
planning change
→ legendary reward를 hero reward로 다시 저장
```

허용:

```text
immutable legendary PendingReward
→ commit-time deployment policy
→ legendary one or consented hero two
```

## 9. 계획 편집과 stale 처리

명령 추가·수정·취소가 성공하면 `queue_revision`을 증가시키고 다음을 stale 처리한다.

- 기존 `PlanningRevalidationReport`.
- 기존 `PlanningCommitPlan`.
- 과거 mandatory consent basis.
- 과거 legendary conflict consent basis.
- producer modification 또는 cancel impact preview.
- provisional-to-tentative-actual mapping.

다음은 stale 처리하지 않는다.

- 불변 `SpinSnapshot`.
- 성공한 `ConfirmReceipt`.
- 확정된 `PendingReward` payload와 identity.

## 10. Idempotency

동일 planning queue mutation transaction 재요청은 기존 `QueueMutationReceipt`를 반환한다.

동일 planning commit transaction 재요청은 기존 `PlanningCommitReceipt`를 반환한다.

동일 spin confirm transaction 재요청은 기존 `ConfirmReceipt`를 반환한다.

중복 요청은 다음을 만들지 않는다.

- sequence 재배정.
- 금화 재차감.
- 시간 중복 진행.
- 룰렛 결과 재판독.
- PendingReward 중복 생성.
- 건물·유닛·스킬 중복 적용.

## 11. 자동 검증 계약

최소 다음 사례를 검증한다.

1. 명령 재정렬 UI가 없음.
2. 명령 수정 뒤 command ID와 reservation sequence 유지.
3. 명령 삭제 뒤 sequence gap 유지, 재번호화 0.
4. 새 명령은 항상 기존 최대 sequence 뒤에 추가.
5. consumer가 미래 producer를 참조하려는 생성 요청 → 무변경 거부.
6. 확정 전 계획 추가·수정·취소 → authoritative 상태와 simulation clock 변경 0.
7. 계획 전체 검증 성공 → 원자 commit 후에만 시간 진행.
8. 하나의 명령 실패 → 전체 mutation과 시간 진행 0.
9. 계획 큐 수정 뒤 열린 SpinSession 결과 기준 불변.
10. 계획 큐 수정 뒤 확정 PendingReward payload 불변.
11. 이동 아이템은 동일 SpinSnapshot 위에서만 최종 위치 변경.
12. 전설 배치 형태 재검증이 PendingReward 정체성을 변경하지 않음.
13. 동일 confirm·planning commit·queue mutation transaction 재요청 → 중복 0.

## 12. 현재 상태

```text
COMMAND_REORDER_UI: NOT_SUPPORTED
COMMAND_EXECUTION_ORDER: SYSTEM_ASSIGNED_CREATION_SEQUENCE
AUTHORITATIVE_MUTATION_BEFORE_CONFIRM: FORBIDDEN
SIMULATION_TIME_ADVANCE_BEFORE_CONFIRM: FORBIDDEN
ROULETTE_REWARD_BASIS: IMMUTABLE_SPIN_SNAPSHOT
PLANNING_QUEUE_MUTATION_RECOMPUTES_ROULETTE_RESULT: FORBIDDEN
DEPENDENCY_REORDER_POLICY: RESOLVED_NOT_SUPPORTED
PRODUCT_CODE_AUTHORIZED: NO
V2_IMPLEMENTATION: NOT_STARTED
HUMAN_QA: NOT_RUN
CORE_LOCK_V2: PENDING
```