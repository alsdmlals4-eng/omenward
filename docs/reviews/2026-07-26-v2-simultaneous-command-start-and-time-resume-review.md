# V2 동시 명령 시작·정상 시간 재개 검수 기록

- 검수일: 2026-07-26
- 상태: `PLANNING_COMPLETE / REVIEW_IN_PROGRESS`
- 검수 항목: `F-20`
- 대상 문서: `docs/design/APPROVED_V2_SIMULTANEOUS_COMMAND_START_AND_TIME_RESUME_2026-07-26.md`
- 사용자 결정: 권장안 승인
- 제품 코드 승인: `NO`

## F-20: RESOLVED

### 검수 질문

일반 `TACTICAL_PLANNING`에서 여러 예약 명령을 확정할 때 건설·업그레이드 시간을 즉시 완료하거나 순차 합산할 것인가, 아니면 모든 명령을 같은 simulation 경계에서 시작하고 전투 재개 후 실제 경과 시간으로 완료할 것인가?

### 승인 결과

```text
SIMULTANEOUS_START_AT_ONE_COMMIT_BOUNDARY
THEN_NORMAL_SIMULATION_RESUME
```

모든 시간 기반 명령은 동일 `command_start_simulation_time`을 사용한다. 확정은 명령을 시작시키지만 duration을 완료시키지 않는다.

## 검수한 대안

### A. 공통 시작 경계 후 정상 시간 재개 — 승인

- 전체 명령을 최종 검증한다.
- 단일 simulation boundary에서 원자 적용한다.
- 건설·업그레이드는 `UNDER_CONSTRUCTION` 또는 `UPGRADING`으로 시작한다.
- 성공 receipt 기록 후 전투 시간을 정상 재개한다.
- 실제 simulation elapsed time으로 각 명령을 독립 완료한다.

### B. 최대 duration까지 즉시 진행 — 거부

- 적 행동과 웨이브 시간을 건너뛸 수 있다.
- pause 상태에서 사실상 안전한 시간 가속이 가능하다.
- 완료 과정의 전투 상호작용을 별도 계산해야 한다.

### C. 명령별 duration 순차 합산 — 거부

- planning batch의 동시 적용 의미를 깨뜨린다.
- 시스템 생성 순서가 의도하지 않은 시작 시간 차이를 만든다.
- dependency 순서를 시간 직렬화로 오해하게 한다.

## 적대적 사례

### 사례 1 — 서로 다른 duration

```text
A 건설 10초
B 업그레이드 20초
확정 시점 t = 100초
```

기대 결과:

```text
A.started_at = 100초
B.started_at = 100초
A 완료 = 110초
B 완료 = 120초
```

### 사례 2 — 처리 지연

확정 버튼 이후 receipt 기록까지 wall-clock 2초가 걸려도 simulation time은 진행하지 않는다.

### 사례 3 — 부분 commit 실패

건설 mutation 준비 후 유닛 spawn이 실패하면 건설 시작, 자원 차감, timer 등록, simulation resume를 전부 rollback한다.

### 사례 4 — 같은 batch 완료 상태 참조

```text
R1 병영 건설 시작
R2 완성 병영 요구 업그레이드
```

R1과 R2가 같은 시작 시간을 가져도 R1은 완료되지 않았으므로 R2는 차단한다.

### 사례 5 — 신규 배치 유닛

commit tick에 spawn과 식량 점유는 기록되지만 신규 유닛의 이동·공격은 다음 simulation tick부터 시작한다.

### 사례 6 — 중복 transaction

동일 `planning_commit_transaction_id` 재요청은 기존 receipt를 반환하며 timer·spawn·비용·시간 재개를 중복하지 않는다.

## 부모 계약 정합성

- 고정 명령 순서 계약의 `AUTHORITATIVE_MUTATION_BEFORE_CONFIRM: FORBIDDEN`을 유지한다.
- 전체 재검증 실패 시 all-or-nothing 차단을 유지한다.
- dependency DAG의 시간 가속 금지를 유지한다.
- transaction foundation의 receipt·rollback·idempotency를 유지한다.
- MapRun 일반 전술계획의 pause와 명시적 재개 규칙을 유지한다.
- 준비 화면과 위험 전투의 기존 즉시 적용 규칙을 변경하지 않는다.

## 자동 검증 요구

- 공통 시작 tick marker 존재.
- confirm 즉시 완료 금지 marker 존재.
- duration fast-forward와 순차 합산 금지 marker 존재.
- receipt 이전 시간 진행 금지 marker 존재.
- simulation elapsed time 기반 완료 marker 존재.
- 신규 배치 유닛 next tick 행동 marker 존재.
- 준비·위험 scope 제외 marker 존재.
- 실패·중복 요청의 시간 진행 0 계약 존재.

## 범위 보호

```text
PRODUCT_CODE_AUTHORIZED: NO
V2_IMPLEMENTATION: NOT_STARTED
HUMAN_QA: NOT_RUN
CORE_LOCK_V2: PENDING
```

이번 검수는 문서 설계만 승인한다. Scene, Resource, 제품 스크립트, 게임 데이터와 실제 simulation timer 구현은 승인하지 않는다.
