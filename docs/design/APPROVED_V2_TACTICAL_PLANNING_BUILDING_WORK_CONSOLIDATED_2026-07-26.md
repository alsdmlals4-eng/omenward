# 승인된 V2 전술계획 건물 작업 통합 계약

- 승인일: 2026-07-26
- 상태: `V2_SPEC_APPROVED / REVIEW_COMPLETE / PRODUCT_CODE_NOT_AUTHORIZED`
- 승인 근거:
  - 사용자: 건설 중 구조물 유료 수리 A안 승인
  - 사용자: 지금까지 상황을 정리하여 PR로 병합 요청
- 적용 범위: 일반 `TACTICAL_PLANNING`의 건설·업그레이드·철거·취소·환급·수리 설정
- 비적용 범위: 위험 전투의 실시간 명령, 준비 화면의 별도 즉시 처리, 제품 구현

이 문서는 PR #82부터 PR #91까지 확정된 전술계획 건물 작업 계약과 이번 건설 중 구조물 수리 결정을 하나의 최신 읽기 진입점으로 통합한다. 세부 승인 문서는 증거로 유지하며, 이 문서가 아래에 명시한 필드의 최신 적용 우선순위를 소유한다.

## 1. 정본 계보

| PR | 핵심 결정 |
|---:|---|
| #82 | 명령 재정렬 UI 없음, 생성 순서 고정, 룰렛 결과 snapshot 불변 |
| #83 | 확정 시 같은 simulation boundary에서 원자 승격 후 정상 시간 재개 |
| #84 | planning branch 즉시 전이와 신규 시간 작업 1초 선행 진행 |
| #85 | 철거가 미확정 건설·업그레이드와 종속 예약을 명시적으로 취소 |
| #86 | 총 duration이 1초 이하인 신규 작업은 branch에서 완료 가능 |
| #87 | planning session 전체가 하나의 공유 `[0, 1초]` horizon 사용 |
| #88 | 진입 전에 진행 중이던 live 작업은 entry progress에서 정지 |
| #89 | 기존 진행 건설 취소 70%, 업그레이드 취소 50% 고정 환불 |
| #90 | 완공 건물 철거는 최초 기본 건설 실제 지불액의 40%만 환급 |
| #91 | planning에서는 수리 설정만 예약, 실제 비용·치유는 live 정산부터 |
| 현재 | 건설 중 구조물도 현재 허용 최대 HP 범위에서 유료 수리 가능 |

연결 정본:

- `APPROVED_V2_FIXED_COMMAND_ORDER_AND_SPIN_SNAPSHOT_2026-07-26.md`
- `APPROVED_V2_SIMULTANEOUS_COMMAND_START_AND_TIME_RESUME_2026-07-26.md`
- `APPROVED_V2_PLANNING_ONE_SECOND_HEADSTART_2026-07-26.md`
- `APPROVED_V2_DEMOLITION_CANCELS_PLANNED_WORK_2026-07-26.md`
- `APPROVED_V2_PLANNING_SHORT_WORK_COMPLETION_2026-07-26.md`
- `APPROVED_V2_PLANNING_SHARED_ONE_SECOND_HORIZON_2026-07-26.md`
- `APPROVED_V2_EXISTING_LIVE_WORK_FROZEN_IN_PLANNING_2026-07-26.md`
- `APPROVED_V2_EXISTING_WORK_CANCEL_REFUND_2026-07-26.md`
- `APPROVED_V2_COMPLETED_BUILDING_DEMOLITION_REFUND_2026-07-26.md`
- `APPROVED_V2_REPAIR_SETTINGS_DEFERRED_LIVE_SETTLEMENT_2026-07-26.md`
- `APPROVED_CORE_V2_INTEGRATED_DECISION_LEDGER_2026-07-25.md`

## 2. 최신 적용 우선순위

```text
TACTICAL_PLANNING_BUILDING_WORK_CANON: THIS_DOCUMENT
COMMAND_REORDER_UI: NOT_SUPPORTED
COMMAND_EXECUTION_ORDER: SYSTEM_CREATION_ORDER
ROULETTE_RESULT_RECOMPUTE_FROM_PLANNING_MUTATION: FORBIDDEN
PLANNING_BRANCH_PROJECTION: REQUIRED
LIVE_WORLD_MUTATION_BEFORE_CONFIRM: FORBIDDEN
NEW_WORK_SHARED_PLANNING_HORIZON: ONE_SECOND_PER_SESSION
EXISTING_LIVE_WORK_PASSIVE_PLANNING_PROGRESS: ZERO
EXISTING_CONSTRUCTION_CANCEL_REFUND_RATE: 70_PERCENT
EXISTING_UPGRADE_CANCEL_REFUND_RATE: 50_PERCENT
COMPLETED_BUILDING_DEMOLITION_REFUND_RATE: 40_PERCENT_BASE_CONSTRUCTION_ONLY
COMPLETED_UPGRADE_COST_IN_DEMOLITION_REFUND: EXCLUDED
TACTICAL_PLANNING_DEMOLITION_BRANCH_EFFECT: IMMEDIATE_REMOVE_AND_FREE_NODE
REPAIR_PLANNING_HEAL_AND_DEBIT: ZERO
REPAIR_FIRST_LIVE_SETTLEMENT_AFTER_RESUME: REQUIRED
CONSTRUCTING_STRUCTURE_PAID_REPAIR: ALLOWED
PRODUCT_CODE_AUTHORIZED: NO
```

### 2.1 과거 통합 원장 대체 범위

- `GM-44`의 자발적 건설·업그레이드 취소 일괄 50%는 폐기한다.
  - 기존 진행 건설 취소: 실제 지불액 70%.
  - 기존 진행 업그레이드 취소: 실제 지불액 50%.
- `GM-47`의 최초 건설비와 완료 업그레이드 합계 50% 철거 환급은 폐기한다.
  - 완공 건물 철거: 최초 기본 건설 실제 지불액의 40%만 환급.
  - 완료된 Tier 업그레이드 지불액은 합산하지 않는다.
- `GM-46`의 시간 기반 자기 건물 철거는 일반 `TACTICAL_PLANNING`에서 발행한 철거 명령에 한해 대체한다.
  - planning branch에서 건물을 즉시 제거하고 node를 비운다.
  - 실제 live 제거는 전체 확정 성공 시 원자 승격한다.
  - 위험 전투 등 다른 입력 모드는 별도 승인 전 기존 규칙을 유지한다.
- `GM-42`의 전술 일시정지 중 공사 정지는 live world에는 유지한다.
  - 해당 세션에서 새로 만든 작업만 별도 planning branch의 공유 1초 horizon에서 진행한다.
  - 적·아군 이동, 공격, wave, cooldown, 수입, 기존 live 작업은 진행하지 않는다.

## 3. 전술계획 상태 모델

```text
live entry snapshot 캡처
→ deterministic planning branch 생성
→ 명령 추가·수정·취소
→ entry snapshot부터 시스템 생성 순서로 full replay
→ 신규 시간 작업에 공유 [0, 1초] horizon 적용
→ branch 결과·가상 원장·영향 범위 preview
→ [확정/전투 재개]
→ 전체 commit-time revalidation
→ 하나의 simulation boundary에서 원자 승격
→ receipt 기록
→ live simulation 정상 재개
```

필수 불변식:

- 사용자가 명령 순서를 직접 변경하는 기능은 없다.
- 명령 추가·수정·취소는 planning branch와 virtual ledger만 변경한다.
- live gold, HP, 건물 registry, timer, simulation time은 확정 전 변경하지 않는다.
- replay는 이전 결과에 덧붙이지 않고 entry snapshot부터 재계산한다.
- 확정 실패 시 건물, 자원, HP, timer, spawn, 수리 요청, 시간 재개 변경은 모두 0이다.
- 동일 transaction 재요청은 같은 receipt를 반환하며 효과를 중복하지 않는다.

## 4. 룰렛 결과 불변

```text
ROULETTE_REWARD_BASIS: IMMUTABLE_SPIN_SNAPSHOT
CONFIRMED_PENDING_REWARD_IDENTITY: IMMUTABLE
PLANNING_QUEUE_MUTATION_RECOMPUTES_ROULETTE_RESULT: FORBIDDEN
```

건설·업그레이드·철거·수리 설정 변경은 이미 산출된 룰렛 결과와 `PendingReward` identity를 다시 계산하지 않는다.

## 5. planning branch 즉시 전이

### 5.1 철거

```text
철거 명령
→ branch에서 즉시 건물 제거
→ node 즉시 사용 가능
→ linked capability와 dependent 영향 계산
→ virtual demolition refund 계산
```

진행 중 업그레이드가 있다면 `active upgrade cancel refund`와 `completed building demolition refund`를 별도 ledger entry로 표시한다.

### 5.2 신규 건설과 업그레이드

```text
빈 node 건설
→ provisional building stable ID 생성
→ branch에서 CONSTRUCTING
→ 공유 1초 horizon 범위에서 진행

업그레이드
→ branch에서 UPGRADING_TO_TARGET_TIER
→ 공유 1초 horizon 범위에서 진행
```

## 6. 공유 1초 planning horizon

```text
PLANNING_HORIZON_START: t=0
PLANNING_HORIZON_END: t=1_SECOND
INDEPENDENT_NEW_WORK_START: t=0
DEPENDENT_NEW_WORK_START: MAX_REQUIRED_PRODUCER_COMPLETION_TIME
HORIZON_REPLAY_ACCUMULATION: FORBIDDEN
```

- 독립 신규 작업은 모두 `t=0`에 병렬 시작한다.
- dependent는 모든 필수 producer가 준비된 가장 늦은 가상 시각부터 시작한다.
- 총 duration이 1초 이하면 branch에서 완료할 수 있다.
- 정확히 `t=1`에 시작 조건을 얻으면 진행도는 0이다.
- queue replay, planning 반복 진입, confirm으로 1초를 중복 적용하지 않는다.

예시:

```text
R1 건설 0.5초
R2 업그레이드 0.8초, R1 의존
R3 업그레이드 0.7초, R2 의존

R1 완료
R2 0.5초 진행
R3 미시작
```

## 7. 기존 live 작업

```text
EXISTING_LIVE_WORK_ENTRY_PROGRESS: IMMUTABLE_DURING_PLANNING
EXISTING_LIVE_WORK_SHARED_HORIZON_ELIGIBILITY: NONE
REPEATED_PLANNING_ENTRY_FREE_PROGRESS: FORBIDDEN
CONFIRM_EXISTING_TIMER_REBASE: FORBIDDEN
```

전술계획 진입 전에 진행 중이던 건설·업그레이드는 entry progress에서 정지한다. 명시적 취소·철거는 branch transition을 만들 수 있지만 진입 자체는 진행도와 완료 capability를 만들지 않는다.

## 8. 취소와 철거 환불

### 8.1 기존 진행 건설 취소

```text
refund = floor(construction_actual_paid_gold * 70 / 100)
result = remove constructing object and free node
```

### 8.2 기존 진행 업그레이드 취소

```text
refund = floor(upgrade_actual_paid_gold * 50 / 100)
result = restore previous active tier and keep node occupied
```

### 8.3 완공 건물 철거

```text
refund = floor(base_construction_actual_paid_gold * 40 / 100)
completed_upgrade_cost = excluded
result = remove building and free node
```

공통 규칙:

- 현재 가격이 아니라 작업 시작 당시 actual payment snapshot을 사용한다.
- 양의 정수 금화 기준 내림이다.
- same-session provisional work 제거는 refund가 아니라 `planned debit release`다.
- 적에 의한 파괴는 환불 없음이다.
- preview에는 진행도, 실제 지불액, 환불액, 손실액, dependent를 표시한다.
- virtual refund credit은 planning 검증에 사용할 수 있지만 live gold는 confirm 전 증가하지 않는다.

## 9. 수리 설정의 planning 처리

```text
REPAIR_SHARED_ONE_SECOND_HORIZON_ELIGIBILITY: NONE
REPAIR_PLANNING_HP_CHANGE: ZERO
REPAIR_PLANNING_GOLD_DEBIT: ZERO
REPAIR_FUTURE_WAGE_ESCROW: NONE
REPAIR_SETTING_PER_STRUCTURE: LATEST_REQUEST_WINS
REPAIR_SETTING_ZERO_WORKERS: STOP_REQUEST
```

전술계획에서는 구조물별 최신 수리 작업자 요청과 예상 비용·치유량만 표시한다. affordability는 live 정산까지 보장하지 않는다.

```text
confirm 성공
→ repair worker change request 승격
→ live simulation 재개
→ 첫 live 1초 settlement
→ 요청 수 적용
→ 글로벌 금화 부족 해소
→ 금화 차감
→ 실제 치유
```

기존 글로벌 수리 예산, 한계 임금, 자동 작업자 해제, tie-break, fixed-point ledger 규칙을 유지한다.

## 10. 건설 중 구조물 유료 수리

```text
CONSTRUCTING_STRUCTURE_PAID_REPAIR: ALLOWED
CONSTRUCTING_REPAIR_OWNER_REQUIREMENT: PLAYER_OWNED
CONSTRUCTING_REPAIR_MINIMUM_HP: GREATER_THAN_ZERO
CONSTRUCTING_REPAIR_CHANNEL: PARALLEL_WITH_CONSTRUCTION
CONSTRUCTING_REPAIR_MAX_HP_CAP: CURRENT_CONSTRUCTION_ALLOWED_MAX_HP
CONSTRUCTING_REPAIR_AUTO_FILL_ON_CAP_GROWTH: FORBIDDEN
CONSTRUCTING_REPAIR_ZERO_HP_RESULT: CONSTRUCTION_FAIL_AND_REPAIR_STOP
PROVISIONAL_CONSTRUCTING_REPAIR_TARGET: ALLOWED_WITH_STABLE_PROVISIONAL_ID
PROVISIONAL_REPAIR_HEAL_OR_DEBIT_BEFORE_CONFIRM: ZERO
CONSTRUCTING_REPAIR_FIRST_LIVE_SETTLEMENT: AFTER_CONFIRM_AND_RESUME
```

### 10.1 대상 조건

다음을 모두 만족해야 한다.

- 플레이어 소유.
- `CONSTRUCTING` lifecycle.
- HP가 0보다 큼.
- 철거·제거·소유권 전환으로 branch에서 사라지지 않음.
- 수리 가능한 `RepairProfile` 보유.

same-session provisional 건물도 stable provisional ID로 수리 대상이 될 수 있다. 건설 producer가 취소되면 repair setting도 producer cancel cascade로 제거하고 다른 건물에 자동 rebind하지 않는다.

### 10.2 planning과 live 분리

```text
provisional 건설
→ branch construction progress 계산
→ repair worker count 설정 가능
→ 예상 비용·치유량 표시
→ planning HP 증가 0
→ planning gold debit 0
```

confirm 성공 후 첫 live settlement에서만 비용과 치유를 계산한다.

### 10.3 건설 중 최대 HP cap

```text
repairable_missing_hp =
  max(0, construction_allowed_max_hp_at_settlement - current_hp)

actual_repair_hp =
  min(requested_repair_hp_after_budget_resolution, repairable_missing_hp)
```

- 수리로 현재 건설 진행도가 허용하는 최대 HP를 초과할 수 없다.
- 건설 진행으로 나중에 허용 최대 HP가 증가해도 과거 수리비로 자동 보충하지 않는다.
- 다음 live settlement에서 새 missing HP를 다시 유료 치유할 수 있다.
- actual heal이 0이면 overheal 임금을 부과하지 않는다.

### 10.4 파괴·완공 경계

- settlement 전에 HP가 0이면 건설 실패, repair request 종료, 미실행 비용 0이다.
- settlement 전에 건설이 완료되면 settlement 시점의 active structure 수리 규칙과 최대 HP를 사용한다.
- confirm-time revalidation에서 target이 유효하지 않으면 전체 confirm을 차단한다.
- confirm 뒤 target이 파괴되면 request를 종료하고 자동 이전하지 않는다.

## 11. stale, cascade, atomicity

preview basis는 최소 다음을 포함한다.

```text
planning_session_id
queue_revision
entry_snapshot_fingerprint
ordered_command_ids
target stable or provisional ID
building lifecycle
payment snapshot fingerprint
refund and repair preview values
ordered dependent impact set
virtual ledger fingerprint
```

basis가 바뀌면:

```text
STALE_TACTICAL_PLANNING_BUILDING_WORK_PREVIEW
→ 상태 변경 0
→ 최신 preview 재생성
→ 필요한 경우 사용자 재동의
```

건물 lifecycle, node occupancy, timer, progress, ledger, repair request, dependent cascade, receipt와 simulation resume는 전체 확정 성공 시 원자 승격한다.

## 12. 남은 검수와 범위 보호

이번 통합은 다음을 아직 고정하지 않는다.

- 건설 진행도별 허용 최대 HP 곡선의 실제 수치.
- 건물 종류별 수리 단가와 초당 치유량.
- 같은 live timestamp에서 construction progress와 repair settlement 중 어느 것을 먼저 계산할지.
- 위험 전투에서 provisional 수리 설정을 허용할지.

```text
CONSTRUCTION_PROGRESS_REPAIR_SETTLEMENT_SAME_TIMESTAMP_ORDER: REVIEW_PENDING
V2_IMPLEMENTATION: NOT_STARTED
PRODUCT_CODE_AUTHORIZED: NO
FINAL_CODEX_HANDOFF: NOT_AUTHORIZED
```

이 승인은 문서 계약과 검수 기준만 고정한다. Godot 제품 코드, Scene, Resource, 게임 데이터 작성 또는 최종 Codex 구현 인계를 승인하지 않는다.
