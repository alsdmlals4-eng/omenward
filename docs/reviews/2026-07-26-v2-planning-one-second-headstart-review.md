# V2 전술계획 즉시 반영·1초 선행 진행 적대적 검수

- 검수일: 2026-07-26
- 검수 항목: `F-21`
- 결과: `RESOLVED`
- 사용자 결정: 예약 단계에서 철거는 즉시 반영하고, 건설·업그레이드는 1초 진행 상태에서 멈춘 뒤 예약 단계 종료 후 계속 진행
- 제품 코드 승인: `NO`

## F-21: 예약 명령의 적용 시점과 첫 1초

### 기존 충돌

이전 계약은 일반 `TACTICAL_PLANNING`에서 다음을 전제했다.

```text
계획 편집은 plan data만 변경
→ confirm 시 모든 명령 시작
→ confirm 뒤 simulation time 진행
```

사용자 지정 동작은 다르다.

```text
철거 명령
→ 계획 화면에서 즉시 건물 제거
→ 같은 node 재사용 가능

건설·업그레이드 명령
→ 계획 화면에서 작업 시작
→ 1초 진행 상태에서 정지
→ 계획 종료 후 1초 이후부터 계속 진행
```

따라서 단순 command list 모델은 사용자 의도를 표현하지 못한다.

## 검토한 접근

### A. Transactional planning branch — 승인

전술계획 입장 snapshot에서 가역적 branch를 만들고 명령을 즉시 replay한다.

- 철거는 branch에서 즉시 structural transition.
- node는 즉시 해제되어 후속 건설이 참조 가능.
- 시간 기반 작업은 command-local elapsed 1초 상태.
- global simulation clock과 적·wave·cooldown은 정지.
- edit/cancel은 snapshot부터 전체 replay.
- confirm은 branch를 live world로 원자 승격.

이 접근은 사용자에게 즉시 결과를 보여주면서 기존 rollback·idempotency·all-or-nothing 계약을 유지한다.

### B. Live authoritative world를 명령마다 직접 변경 — 기각

명령 입력 즉시 실제 건물과 원장을 직접 변경하면 다음 문제가 생긴다.

- 무료 수정·취소를 위해 복잡한 역연산 필요.
- 철거 후 새 건설, 다시 철거 취소 같은 chain rollback이 불안정.
- commit 실패 시 이미 변경된 live world 복구 필요.
- duplicate callback에서 진행도와 비용 중복 위험.

### C. 화면 연출만 변경하고 후속 판정은 기존 상태 사용 — 기각

겉으로만 건물이 사라지고 node 판정은 점유 상태라면 같은 node 건설 예시를 만족하지 못한다.

## 승인된 결정

```text
F-21: RESOLVED
DECISION: TRANSACTIONAL_BRANCH_WITH_COMMAND_LOCAL_ONE_SECOND_HEADSTART
```

## 검수된 불변 조건

1. 철거 후 같은 planning session에서 node를 즉시 재사용할 수 있다.
2. 새 건물은 provisional identity를 가지며 1초 건설 상태에서 정지한다.
3. 업그레이드는 목표 tier 완료가 아니라 upgrade work elapsed 1초 상태다.
4. global simulation time은 증가하지 않는다.
5. 적·wave·cooldown·접전지는 진행하지 않는다.
6. 가상 자원 원장은 후속 명령 검증에 반영되지만 live ledger는 confirm 전 변경하지 않는다.
7. edit/cancel은 역연산이 아니라 entry snapshot 전체 replay를 사용한다.
8. confirm은 1초를 다시 적용하지 않는다.
9. confirm 실패 시 live building·node·resource·timer·time mutation은 0이다.
10. duplicate transaction은 progress·비용·건물 mutation을 중복하지 않는다.

## 기존 계약과의 관계

다음 역사적 문구는 live authoritative world에 대해서는 유지한다.

```text
AUTHORITATIVE_MUTATION_BEFORE_CONFIRM: FORBIDDEN
SIMULATION_TIME_ADVANCE_BEFORE_CONFIRM: FORBIDDEN
```

하지만 `PLANNING_EDIT_SCOPE: PLAN_DATA_ONLY`를 단순 command list로 해석하는 것은 폐기한다.

정확한 새 의미:

```text
confirm 전 live world mutation = 금지
confirm 전 transactional planning branch mutation = 필수
```

`APPROVED_V2_SIMULTANEOUS_COMMAND_START_AND_TIME_RESUME_2026-07-26.md`의 “confirm에서 모든 시간 기반 명령이 처음 시작” 해석은 이 문서가 대체한다.

- 작업은 planning branch에서 이미 1초 상태로 시작한다.
- confirm은 branch 승격과 global simulation 재개 시점이다.
- confirm 후에는 1초 이후 진행을 계속한다.

## 적대적 사례

### 철거 → 같은 node 건설

```text
entry: node N에 building B
R1: B 철거
R2: N에 building C 건설
```

예상:

- branch에서 B 없음.
- N 비점유.
- C는 provisional building.
- C elapsed 1초.
- live world는 confirm 전 B 유지.

### 철거 취소

```text
R1 삭제
→ entry snapshot replay
```

예상:

- branch에 B 복원.
- C가 R1의 node 해제를 요구하면 dependency cascade 또는 blocked 처리.
- live world 변화 0.

### 업그레이드 replay 중복

```text
R1: Tier 1 → Tier 2 업그레이드
→ unrelated R2 추가
→ 전체 replay
```

예상:

- R1 progress는 2초가 아니라 계속 1초.

### confirm 중 receipt 실패

예상:

- 건물 철거 0.
- provisional building 승격 0.
- gold debit 0.
- timer registration 0.
- simulation resume 0.

## 남은 검수

다음 항목은 별도 결정이 필요하다.

```text
SHORT_DURATION_AT_OR_BELOW_ONE_SECOND_POLICY: REVIEW_PENDING
```

총 duration이 1초 이하인 작업이 planning branch의 선행 진행으로 완료 상태가 되는지, 1초 경계 직전에 멈추는지는 본 검수에서 확정하지 않는다.

## 범위 확인

- `TACTICAL_PLANNING`만 적용.
- `PREPARATION` 즉시 적용 규칙 유지.
- `DANGER_COMBAT` 실시간 규칙 유지.
- 룰렛 이동 즉시 실행 규칙 유지.
- 제품 코드·Scene·Resource·게임 데이터 변경 없음.
- 최종 Codex 인계 없음.

```text
F-21: RESOLVED
PRODUCT_CODE_AUTHORIZED: NO
V2_IMPLEMENTATION: NOT_STARTED
HUMAN_QA: NOT_RUN
```
