# V2 철거 시 계획 작업 취소·가상 비용 해제 검수

- 검수일: 2026-07-26
- 검수 항목: F-22
- 상태: `RESOLVED`
- 범위: 일반 `TACTICAL_PLANNING` 문서 계약
- 제품 코드 승인: `NO`

## 1. 검수 질문

업그레이드 또는 건설이 planning branch에서 1초 진행 상태일 때 같은 건물을 철거하면, 진행 중 작업과 가상 비용을 어떻게 처리해야 하는가?

## 2. 검토한 대안

### A. 영향 preview 후 작업 취소·비용 해제·철거 원자 적용

- 취소될 작업과 dependent를 표시한다.
- 명시적 동의가 있을 때만 적용한다.
- 미확정 planned debit을 제거한다.
- 철거와 작업 취소를 하나의 queue mutation으로 처리한다.

### B. 작업을 사용자가 먼저 직접 취소해야 철거 허용

- 안전하지만 불필요한 수동 단계가 추가된다.
- target 작업과 철거 관계를 시스템이 이미 알고 있음에도 플레이어가 별도로 찾아야 한다.

### C. 작업 비용을 유지한 채 철거

- 완료 불가능한 작업에 비용이 남는다.
- planning virtual ledger와 사용자 기대를 위반한다.

## 3. 결정

사용자가 권장안 A를 승인했다.

```text
F-22: RESOLVED
DECISION: PREVIEW_CONFIRM_CANCEL_WORK_RELEASE_VIRTUAL_COST_THEN_DEMOLISH
```

## 4. 필수 불변 조건

```text
DEMOLITION_WITH_PLANNED_WORK_POLICY: PREVIEW_CONFIRM_CANCEL_THEN_DEMOLISH
PLANNED_WORK_IMPACT_PREVIEW: REQUIRED
PLANNED_WORK_CANCEL_CONFIRMATION: REQUIRED
PLANNED_WORK_VIRTUAL_COST_RELEASE: REQUIRED
DEMOLITION_AND_WORK_CANCEL: ATOMIC_SINGLE_QUEUE_MUTATION
SILENT_PLANNED_WORK_DISCARD: FORBIDDEN
PLANNED_WORK_COST_WASTE: FORBIDDEN
STALE_DEMOLITION_CONFIRMATION: REJECT_WITH_ZERO_MUTATION
QUEUE_REVISION_INCREMENT_PER_DEMOLITION_OVERRIDE: EXACTLY_ONCE
POST_DEMOLITION_FULL_REPLAY: REQUIRED
LIVE_LEDGER_MUTATION_BEFORE_CONFIRM: FORBIDDEN
```

## 5. 적대적 사례

### 5.1 업그레이드 1초 상태에서 철거

```text
R1 Tier 2 업그레이드
R2 같은 건물 철거
```

기대:

- R1과 가상 비용을 preview에 표시.
- 동의 전 mutation 0.
- 동의 후 R1 제거, planned debit 해제, target 철거.

### 5.2 preview 뒤 비용 변경

기대:

- 과거 basis hash는 stale.
- 과거 동의로 철거하지 않음.
- 최신 preview와 재동의 필요.

### 5.3 provisional 건설 중 철거

기대:

- 아직 live 건물이 아니므로 건설 예약 취소로 처리.
- provisional output과 dependent cascade 제거.
- 별도 live demolition event 0.

### 5.4 작업 취소 성공 후 철거 실패

기대:

- 부분 상태를 남기지 않음.
- queue, branch, virtual ledger를 mutation 전 상태로 rollback.

### 5.5 철거 후 같은 node 재건설

기대:

- node는 planning branch에서 즉시 FREE.
- 후속 건설 허용.
- 새 건설은 elapsed 1초 상태.

### 5.6 동일 transaction 재요청

기대:

- 동일 `QueueMutationReceipt` 반환.
- revision 추가 증가 0.
- 비용 재해제와 target 재철거 0.

## 6. 기존 계약과의 정합성

- `APPROVED_V2_PLANNING_ONE_SECOND_HEADSTART_2026-07-26.md`의 transactional planning branch를 유지한다.
- `APPROVED_V2_PRODUCER_CANCEL_CASCADE_2026-07-26.md`의 explicit dependent cascade를 유지한다.
- `APPROVED_V2_PLANNING_REVALIDATION_ALL_OR_NOTHING_2026-07-26.md`의 전체 차단·원자 적용을 유지한다.
- live authoritative ledger는 confirm 전 변경하지 않는다.
- 준비 화면과 위험 전투의 기존 규칙을 변경하지 않는다.

## 7. 범위 보호

이번 검수에서 승인하지 않은 항목:

- 제품 코드 구현.
- Scene·Resource·게임 데이터 변경.
- 일반 수리·생산 queue 취소 정책.
- 총 duration이 1초 이하인 작업의 완료 경계.
- 최종 Codex 인계.

```text
PRODUCT_CODE_AUTHORIZED: NO
V2_IMPLEMENTATION: NOT_STARTED
HUMAN_QA: NOT_RUN
CORE_LOCK_V2: PENDING
```
