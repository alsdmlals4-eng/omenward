# V2 전술계획 1초 이하 작업 완료 적대적 검수

- 검수일: 2026-07-26
- 상태: `F-23_RESOLVED / PRODUCT_CODE_NOT_AUTHORIZED`
- 대상 문서: `docs/design/APPROVED_V2_PLANNING_SHORT_WORK_COMPLETION_2026-07-26.md`
- 상위 계약:
  - `APPROVED_V2_PLANNING_ONE_SECOND_HEADSTART_2026-07-26.md`
  - `APPROVED_V2_SIMULTANEOUS_COMMAND_START_AND_TIME_RESUME_2026-07-26.md`
  - `APPROVED_V2_PLANNING_REVALIDATION_ALL_OR_NOTHING_2026-07-26.md`
  - `APPROVED_V2_PLANNING_DEPENDENCY_DAG_AND_PROVISIONAL_IDS_2026-07-26.md`
  - `APPROVED_V2_TRANSACTION_FOUNDATION_SEQUENCE_2026-07-26.md`

## F-23: RESOLVED

### 충돌

기존 1초 선행 진행 계약은 다음 식을 사용한다.

```text
work_elapsed_in_planning = min(1초, total_duration)
```

그러나 `total_duration <= 1초`인 작업을 완료로 볼지, 완료 직전에서 강제로 멈출지 정해지지 않았다.

### 검토안

#### A. Planning branch에서 완료

- canonical duration이 1초 이하이면 branch lifecycle을 `COMPLETED`로 판정한다.
- 정확히 1초인 경계를 포함한다.
- 완료 capability를 후속 planning consumer가 사용할 수 있다.
- live 상태와 외부 completion side effect는 confirm까지 보류한다.

#### B. 완료 직전 강제 정지

- duration보다 짧은 인위적 상태를 만든다.
- 전투 재개 후 첫 tick에 완료되므로 실제 duration보다 완료가 늦어진다.
- epsilon과 frame 경계가 계약에 침투한다.

#### C. 명령 종류별 예외

- 건설·업그레이드마다 별도 완료 정책이 필요하다.
- 동일한 1초 headstart 의미가 command schema마다 달라진다.

### 사용자 결정

사용자가 권장안 A를 승인했다.

```text
F-23: RESOLVED
DECISION: COMPLETE_DURATION_LE_ONE_SECOND_IN_PLANNING_BRANCH
ONE_SECOND_BOUNDARY: INCLUSIVE
LIVE_PROMOTION: CONFIRM_ONLY
```

## 적대적 사례

### 1. 정확히 1초

`duration == headstart`이면 완료다. `duration - epsilon`으로 강제 정지하지 않는다.

### 2. Float 경계

UI 표시값이나 float 근사로 완료를 판정하지 않는다. canonical fixed-point tick을 비교한다.

### 3. 완료 capability와 live side effect 혼합

branch 구조적 capability는 후속 명령에 제공하지만 live registry, TokenSource, 생산 tick, 로그, 업적은 confirm 전 실행하지 않는다.

### 4. Replay 누적

queue 재평가 횟수만큼 headstart를 누적하지 않는다. 매번 entry snapshot에서 같은 완료 상태를 다시 계산한다.

### 5. 취소 뒤 ghost capability

완료 producer가 취소되면 capability와 dependent를 승인된 cascade 정책으로 제거하고 entry snapshot부터 replay한다.

### 6. Confirm 중복

confirm은 완료 상태를 승격할 뿐 headstart 또는 completion event를 재적용하지 않는다.

### 7. Confirm 실패

자원·dependency·authoritative basis 중 하나라도 실패하면 live 완료, registry, 비용, 후속 명령, 시간 진행을 모두 0으로 유지한다.

### 8. 연속 short-work 체인

개별 작업 완료는 확정했지만 한 대상에서 여러 단계 short work를 연속 완료할 수 있는지는 별도 정책이 필요하다.

```text
MULTI_STAGE_SHORT_WORK_CHAIN_POLICY: REVIEW_PENDING
```

## 계약 검사 요약

자동 검증은 다음을 직접 강제한다.

- 상위 문서 routing.
- 1초 이하 inclusive 완료 marker.
- fixed-point duration 비교.
- branch 완료 capability 제공.
- 외부 side effect commit 지연.
- replay 누적 금지.
- 취소·수정 재계산.
- confirm headstart·completion event 중복 금지.
- 실패 시 live mutation 0.
- product code 미승인.

## 범위 결론

```text
F-23: RESOLVED
SHORT_WORK_COMPLETION: APPROVED
MULTI_STAGE_SHORT_WORK_CHAIN_POLICY: REVIEW_PENDING
PRODUCT_CODE_AUTHORIZED: NO
V2_IMPLEMENTATION: NOT_STARTED
HUMAN_QA: NOT_RUN
```
