# F-24 적대적 검수 — 전술계획 공유 1초 Horizon

- 검수일: 2026-07-26
- 대상: `docs/design/APPROVED_V2_PLANNING_SHARED_ONE_SECOND_HORIZON_2026-07-26.md`
- 결과: `APPROVED_WITH_CONTRACT_TESTS`
- 제품 코드 승인: `NO`

## 1. 검수 목적

전술계획의 1초 선행 진행이 명령별 무료 시간으로 중복되지 않고, 하나의 공유 horizon에서 독립 작업의 병렬 진행과 dependency chain의 남은 시간 진행을 결정론적으로 계산하는지 검증한다.

## 2. 핵심 위험

### F-24-1 명령별 1초 중복

실패 예:

```text
R1 1초
R2 1초
R3 1초
→ 총 3초의 무료 작업 진행
```

판정:

```text
PER_COMMAND_HEADSTART_BUDGET: FORBIDDEN
```

모든 명령은 동일한 `[0, 1초]` horizon을 공유해야 한다.

### F-24-2 독립 작업의 잘못된 직렬화

실패 예:

```text
R1이 reservation_sequence 선두이므로 1초 전부 사용
R2와 R3은 0초 진행
```

판정:

```text
INDEPENDENT_READY_COMMANDS_START_AT_T0: REQUIRED
INDEPENDENT_COMMANDS_PROGRESS_CONCURRENTLY: REQUIRED
```

독립 작업은 시간 예산을 서로 소모하지 않는다.

### F-24-3 dependency consumer 조기 시작

실패 예:

```text
R1 0.5초 건설
R2 R1 완료 필요
R2를 t=0부터 진행
```

판정:

```text
DEPENDENT_COMMAND_EARLIEST_START: REQUIRED_PRODUCER_CAPABILITY_TIME
```

R2는 t=0.5부터 시작해야 한다.

### F-24-4 여러 producer 중 이른 시각 선택

실패 예:

```text
R3는 R1(t=0.2)과 R2(t=0.8)를 모두 요구
R3를 t=0.2에 시작
```

판정:

```text
DEPENDENT_START_TIME: MAX_REQUIRED_PRODUCER_AVAILABLE_TIME
```

R3는 t=0.8부터 시작한다.

### F-24-5 horizon 종료 경계 누락

producer가 정확히 t=1에 완료하면 dependent의 시작 조건은 성립하지만 진행 시간은 없다.

승인 결과:

```text
dependent.virtual_start_tick = horizon_end_tick
dependent.virtual_elapsed_ticks = 0
```

### F-24-6 replay 누적

실패 예:

```text
queue edit 3회
→ 같은 작업 elapsed 3초
```

판정:

```text
PLANNING_REPLAY_HORIZON_ACCUMULATION: FORBIDDEN
```

매 replay는 entry snapshot에서 동일 1초 horizon을 새로 계산한다.

### F-24-7 confirm 재적용

실패 예:

```text
branch elapsed 0.5초
→ confirm에서 다시 1초 적용
→ live elapsed 1.5초
```

판정:

```text
CONFIRM_REAPPLIES_HORIZON: FORBIDDEN
```

live 잔여 시간은 `total - branch elapsed`다.

### F-24-8 global simulation 혼합

실패 예:

```text
planning horizon 1초
→ 적 이동·wave timer·cooldown도 1초 진행
```

판정:

```text
GLOBAL_SIMULATION_CLOCK_DURING_HORIZON: PAUSED
NON_COMMAND_SYSTEM_TIME_DURING_HORIZON: ZERO
```

horizon은 branch-local scheduling만 수행한다.

## 3. 대표 시나리오

### 독립 병렬 작업

```text
R1 4초, R2 3초, R3 6초
→ 모두 t=0 시작
→ 모두 elapsed 1초
```

### 연속 chain

```text
R1 0.2초
R2 0.3초
R3 0.4초
R4 0.5초
```

승인 결과:

```text
R1 completed at 0.2
R2 completed at 0.5
R3 completed at 0.9
R4 elapsed 0.1, in progress
```

### 다중 dependency

```text
R1 available at 0.4
R2 available at 0.7
R3 requires R1 + R2
→ R3 starts at 0.7
→ R3 available time = 0.3초
```

## 4. 원자성 검수

confirm 실패 시 다음은 모두 0이어야 한다.

- live object promotion.
- resource debit.
- timer registration.
- completion side effect.
- simulation time advance.

부분 승격은 금지한다.

## 5. Idempotency 검수

동일 planning commit transaction 재요청은 기존 receipt를 반환해야 한다.

중복 금지:

- horizon 재실행.
- elapsed 증가.
- completion event 재발행.
- 비용 재차감.
- timer 중복 등록.

## 6. 범위 검수

이번 결정은 다음을 포함하지 않는다.

- 기존 live 진행 작업이 planning 진입만으로 1초 headstart를 얻는지 여부.
- 준비 화면 즉시 처리 변경.
- 위험 전투 실시간 처리 변경.
- repair·production queue의 별도 시간축.
- 제품 코드 구현.

## 7. 최종 판정

```text
F-24_RESULT: APPROVED
PLANNING_HEADSTART_TIME_MODEL: SHARED_GLOBAL_ONE_SECOND_HORIZON
MULTI_STAGE_SHORT_WORK_CHAIN_POLICY: RESOLVED_SHARED_HORIZON
PRODUCT_CODE_AUTHORIZED: NO
```
