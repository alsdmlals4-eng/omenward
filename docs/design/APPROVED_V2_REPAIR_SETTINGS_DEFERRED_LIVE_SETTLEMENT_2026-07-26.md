# 승인된 전술계획 수리 설정·live 정산 지연 계약

- 승인일: 2026-07-26
- 상태: `V2_SPEC_APPROVED / PRODUCT_CODE_NOT_AUTHORIZED`
- 승인 근거: 사용자 권장안 승인
- 적용 범위: 일반 `TACTICAL_PLANNING`
- 상위 책임:
  - `docs/design/APPROVED_CORE_V2_INTEGRATED_DECISION_LEDGER_2026-07-25.md`
  - `docs/design/APPROVED_V2_PLANNING_SHARED_ONE_SECOND_HORIZON_2026-07-26.md`
  - `docs/design/APPROVED_V2_EXISTING_LIVE_WORK_FROZEN_IN_PLANNING_2026-07-26.md`
  - `docs/design/APPROVED_V2_PLANNING_REVALIDATION_ALL_OR_NOTHING_2026-07-26.md`
  - `docs/design/APPROVED_V2_TRANSACTION_FOUNDATION_SEQUENCE_2026-07-26.md`

이 문서는 전술계획 중 수리 작업자 수를 설정할 때 planning branch에서 허용되는 미리보기, 금지되는 진행·비용 처리, 최종 확정 승격과 전투 재개 후 첫 1초 정산 경계의 처리 순서를 소유한다.

## 1. 승인된 핵심 결정

```text
REPAIR_PLANNING_POLICY: SETTINGS_ONLY_NO_PROGRESS
REPAIR_PLANNING_HORIZON_ELIGIBILITY: EXCLUDED
PLANNED_REPAIR_WORKER_COUNT: PREVIEW_ONLY
REPAIR_HP_GAIN_DURING_PLANNING: ZERO
REPAIR_GOLD_DEBIT_DURING_PLANNING: ZERO
REPAIR_GOLD_HOLD_DURING_PLANNING: NONE
REPAIR_SETTING_LATEST_PER_STRUCTURE: WINS
REPAIR_SETTING_PROMOTION: ATOMIC_WITH_PLANNING_COMMIT
REPAIR_SETTLEMENT_START: FIRST_LIVE_ONE_SECOND_BOUNDARY_AFTER_RESUME
REPAIR_SETTLEMENT_ORDER: APPLY_REQUESTS_THEN_GLOBAL_AFFORDABILITY_THEN_DEBIT_THEN_HEAL
REPAIR_GLOBAL_BUDGET_POLICY: PRESERVED
REPAIR_PLANNING_REPLAY: FROM_ENTRY_SNAPSHOT
REPAIR_QUEUE_REVISION_INCREMENT: EXACTLY_ONCE_PER_SETTING_MUTATION
FAILED_REPAIR_SETTING_CONFIRM_LIVE_MUTATION: ZERO
REPAIR_SETTING_DUPLICATE_TRANSACTION: SAME_RECEIPT
DANGER_COMBAT_SCOPE: EXCLUDED
PRODUCT_CODE_AUTHORIZED: NO
```

승인 흐름:

```text
전술계획 진입
→ live 수리 상태와 HP·금화 snapshot 캡처
→ 구조물별 requested worker count 편집
→ 예상 초당 비용·치유량 preview
→ planning 중 HP 증가 0 / 금화 차감 0
→ [확정/전투 재개]
→ requested worker count를 pending live request로 원자 승격
→ 첫 live 1초 정산 경계
→ 요청 수 적용
→ 글로벌 금화 부족 해소
→ 금화 차감
→ 실제 치유
```

## 2. Planning branch 상태

전술계획 진입 시 다음 entry basis를 캡처한다.

```text
RepairPlanningEntrySnapshot
- planning_session_id
- entry_simulation_tick
- live_gold_fixed_point
- structure_id별 current_hp / max_hp
- structure_id별 current_live_worker_count
- structure_id별 repair_profile_id
- structure_id별 ownership / lifecycle / eligibility
- next_live_repair_settlement_boundary
```

planning branch는 구조물별 최신 requested worker count를 보유한다.

```text
PlannedRepairSetting
- planning_command_id
- structure_id
- requested_worker_count
- estimated_marginal_worker_costs
- estimated_total_cost_per_settlement
- estimated_heal_per_settlement
- entry_repair_basis_hash
```

같은 구조물의 설정을 여러 번 변경하면 최신 requested worker count가 이전 값을 대체한다. 사용자가 명령 순서를 직접 재정렬하는 기능은 없으며, 구조물별 최종 설정만 확정 대상으로 사용한다.

## 3. Planning 중 금지되는 변화

전술계획 동안 다음 authoritative 변화는 모두 금지한다.

- 구조물 HP 증가.
- 글로벌 금화 차감.
- 작업자 임금 정산.
- 최대 HP 도달 판정에 따른 live 작업자 자동 해제.
- 금화 부족에 따른 live 작업자 자동 감소.
- 수리 완료 로그·업적·통계 발생.
- 수리 요청을 이유로 공유 1초 planning horizon 소비.
- planning 화면 반복 진입에 따른 무료 치유.

기존 live 수리 작업도 entry snapshot 상태에서 정지한다. planning 중 경과한 현실 시간은 repair settlement clock에 포함하지 않는다.

## 4. Preview

UI는 구조물별로 최소 다음을 표시한다.

```text
현재 HP / 최대 HP
현재 live 작업자 수
계획된 작업자 수
예상 다음 정산 비용
예상 다음 정산 치유량
금화가 부족할 경우 실제 작업자 수가 줄어들 수 있음
```

preview는 정보 제공용이며 다음 정산 결과를 보장하지 않는다. 다른 planning 명령의 비용, 환불, 건물 철거, 소유권·lifecycle 변화와 전투 재개 시점의 live 금화에 따라 실제 첫 정산 결과가 달라질 수 있다.

planning 중 수리 비용을 별도 escrow로 예약하지 않는다. 후속 planning 명령의 자원 검증에서 미래 수리 임금을 planned debit으로 차감하지 않는다.

## 5. 유효성

수리 설정 대상은 entry snapshot과 최종 replay에서 모두 다음 조건을 만족해야 한다.

- 현재 플레이어 소유 구조물.
- HP가 0보다 크고 최대 HP보다 작음.
- 해당 `RepairProfile`이 존재함.
- 철거·파괴·적 교체·성문 재건 전용 상태가 아님.
- 승인된 유지보수 채널과 충돌하지 않음.

대상이 철거되거나 소유권을 잃거나 HP 0이 되도록 planning branch가 변경되면 해당 repair setting은 유효하지 않다. 전체 확정은 기존 all-or-nothing revalidation 정책에 따라 차단되며 자동으로 다른 구조물에 재지정하지 않는다.

요청 작업자 수는 음수가 될 수 없다. `0`은 수리 중지 요청이다.

## 6. Queue mutation과 replay

수리 작업자 설정 추가·수정·제거는 planning queue mutation이다.

필수 규칙:

- mutation 하나당 `queue_revision` 정확히 1회 증가.
- entry snapshot부터 전체 planning branch replay.
- replay로 HP, 금화, 정산 횟수 또는 worker count가 누적되지 않음.
- 같은 구조물의 이전 설정은 최신 설정으로 결정론적으로 대체.
- 독립된 건설·배치·철거 명령의 생성 순서는 변경하지 않음.
- stale session 또는 revision 기반 요청은 상태 변경 0.

## 7. 최종 확정

`[확정/전투 재개]`는 다음을 하나의 transaction으로 처리한다.

```text
전체 planning 재검증
→ 구조물별 최종 requested worker count 확정
→ RepairWorkerChangeRequest 등록
→ PlanningCommitReceipt 기록
→ 전투 시간 재개
```

확정 시점에는 다음을 하지 않는다.

- 1초분 금화 즉시 차감.
- 1초분 HP 즉시 치유.
- 글로벌 예산 부족 해소를 조기 실행.
- repair settlement boundary를 현재 시점으로 강제 이동.
- 공유 planning horizon을 재적용.

확정 실패 시 worker request, HP, 금화, timer, resume 상태 변경은 모두 0이다.

## 8. 첫 live 1초 정산 경계

전투 재개 후 기존 deterministic repair settlement clock의 첫 경계에서 다음 순서를 사용한다.

```text
1. 구조물별 최신 requested worker count 적용
2. 유효하지 않은 구조물의 수리 요청 종료
3. 글로벌 금화로 감당할 수 없는 작업자를 기존 우선순위로 자동 해제
4. 확정된 실제 작업자 임금 차감
5. 실제 치유량 적용
6. 최대 HP 도달 구조물의 작업자 해제
```

기존 글로벌 부족 해소 및 동률 순서를 유지한다.

```text
실제 한계 임금 높은 작업자 우선 제거
→ 현재 HP 비율 높은 구조물
→ StableStructureId
```

planning preview의 예상값보다 live 금화가 적으면 첫 정산에서 실제 작업자 수를 낮춘다. 자동 재고용은 하지 않는다.

## 9. 경계 사례

### 9.1 기존 수리 3명에서 planning 중 5명 요청

```text
planning 중: 3명 상태 정지, 비용 0, 치유 0
확정: 5명 요청 등록
첫 live 정산: 5명 요청 적용 후 글로벌 affordability 계산
```

### 9.2 planning 중 5명→2명→0명 변경

최종 branch에는 0명 요청만 남는다. 확정 후 첫 live 정산 경계에서 수리 중지로 적용한다.

### 9.3 planning 중 대상 철거

철거가 적용된 branch에서는 수리 설정이 invalid다. 전체 확정을 차단하고 사용자에게 수리 설정 제거 또는 철거 취소를 요구한다. 자동 삭제는 하지 않는다.

### 9.4 planning 중 HP가 이미 최대인 entry 구조물

새 수리 요청을 만들 수 없다. entry 이후 live HP는 planning 동안 변하지 않으므로 자동으로 수리 가능 상태가 되지 않는다.

### 9.5 중복 확정 transaction

동일 `planning_commit_transaction_id` 재요청은 기존 receipt를 반환하며 repair request, 금화 차감, 치유, 시간 재개를 중복 적용하지 않는다.

## 10. Scope 보호

- 일반 `TACTICAL_PLANNING`에만 적용한다.
- 위험 전투는 기존 실시간 수리 규칙을 유지한다.
- 준비 화면의 별도 시간 진행 계약을 변경하지 않는다.
- 건설·업그레이드 공유 1초 horizon을 변경하지 않는다.
- 수리 단가, 치유량, 작업자 상한 수치는 이 문서에서 확정하지 않는다.
- 제품 코드, Scene, Resource, 게임 데이터를 변경하거나 승인하지 않는다.

```text
V2_IMPLEMENTATION: NOT_STARTED
PRODUCT_CODE_AUTHORIZED: NO
FINAL_CODEX_HANDOFF: NOT_AUTHORIZED
```
