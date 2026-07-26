# V2 고정 명령 순서·SpinSnapshot 검수 기록

- 검수일: 2026-07-26
- 상태: `F-19: RESOLVED`
- 제품 코드 승인: `NO`
- 구현 상태: `NOT_STARTED`

## 1. 검수 대상

사용자 확인:

```text
명령 순서를 변경하는 기능은 없다.
명령 확정과 시간 진행 전에는 authoritative 상태가 변하지 않는다.
룰렛 결과는 룰렛을 돌린 시점을 기준으로 고정할 수 있다.
```

검수 질문:

- 존재하지 않는 명령 재정렬 기능을 전제로 별도 UX 계약이 필요한가?
- 계획 편집이 룰렛 결과 또는 실제 게임 상태를 다시 산출해야 하는가?

## 2. 결론

```text
F-19: RESOLVED
RESOLUTION: FIXED_CREATION_ORDER_NO_REORDER_AND_IMMUTABLE_SPIN_SNAPSHOT
```

- 명령 재정렬 UI는 지원하지 않는다.
- 명령 처리 순서는 시스템이 생성 시 부여한 `reservation_sequence`로 고정한다.
- 계획 추가·수정·취소는 확정 전 planning 데이터만 변경한다.
- authoritative 상태와 simulation clock은 확정 성공 뒤에만 변경한다.
- 룰렛 결과는 불변 `SpinSnapshot`, 정지 결과, 명시적 이동 내역으로 산출한다.
- planning queue mutation은 룰렛 결과와 확정된 PendingReward를 다시 계산하지 않는다.

## 3. 폐기한 가정

다음 가정은 제품 UX와 일치하지 않아 폐기했다.

```text
플레이어가 예약 카드를 드래그해 명령 순서를 바꾼다.
```

따라서 다음 설계는 필요하지 않다.

- dependency-safe drop range.
- producer와 dependent의 block drag.
- invalid reorder 상태 유지.
- reorder confirmation UX.

## 4. 유지되는 순서 불변 조건

재정렬 UI가 없어도 순서는 결정론적으로 유지되어야 한다.

- 새 명령은 기존 명령 뒤에 추가.
- 수정은 command ID와 sequence 유지.
- 삭제 뒤 sequence gap 유지.
- 삭제된 sequence 재사용 금지.
- consumer 생성은 이미 존재하는 이전 producer만 참조.

## 5. 룰렛과 계획 분리

룰렛 결과 정체성:

```text
immutable SpinSnapshot
+ stop result
+ accepted movement history
→ ConfirmReceipt
→ immutable PendingReward
```

전술계획 재검증 대상:

```text
cost
food
building and target preconditions
dependency validity
legendary deployment form
mandatory consent
spawn readiness
```

전술계획 재검증 비대상:

```text
roulette grade reroll
roulette cell reselection
unit family reroll
source building/tier reinterpretation
confirmed PendingReward identity replacement
```

## 6. 적대적 검토

### A. 계획 중 TokenSource 건설 예약

실제 TokenSource가 아직 생성되지 않았으므로 열린 SpinSnapshot에 포함하지 않는다.

### B. 계획 확정 뒤 TokenSource가 생성됨

기존 SpinSession 또는 확정 보상은 변하지 않는다. 이후 새 회전부터 새 authoritative TokenSource 상태를 snapshot에 포함한다.

### C. 전설 배치 명령 추가

전설 PendingReward 정체성은 유지한다. 배치 시 생존 전설 상태에 따라 전설 1기 또는 동의된 영웅 2기 형태만 재검증한다.

### D. 계획 명령 삭제

남은 sequence를 재번호화하지 않는다. 과거 planning report와 consent만 stale 처리한다.

### E. 확정 실패

금화·식량·건물·유닛·시간 변경 0. 계획 데이터는 보존한다.

## 7. 범위 보호

이번 결정은 다음을 변경하지 않는다.

- 기존 SpinSession confirm/cancel 정책.
- 이동 아이템 종류와 사용 제한.
- producer cancel 또는 output fingerprint cascade 정책.
- planning all-or-nothing commit 정책.
- 전설 배치 제한과 동의 정책.

제품 코드, Scene, Resource, 게임 데이터는 수정하지 않는다.

## 8. 검증 결론

```text
COMMAND_REORDER_UI: NOT_SUPPORTED
DEPENDENCY_REORDER_POLICY: RESOLVED_NOT_SUPPORTED
AUTHORITATIVE_MUTATION_BEFORE_CONFIRM: FORBIDDEN
ROULETTE_REWARD_BASIS: IMMUTABLE_SPIN_SNAPSHOT
PLANNING_QUEUE_MUTATION_RECOMPUTES_ROULETTE_RESULT: FORBIDDEN
PRODUCT_CODE_AUTHORIZED: NO
```