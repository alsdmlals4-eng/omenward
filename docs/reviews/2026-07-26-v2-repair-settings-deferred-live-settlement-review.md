# F-28 전술계획 수리 설정·live 정산 지연 적대적 검수

- 검수일: 2026-07-26
- 상태: `F-28: RESOLVED`
- 결과: `F-28_RESULT: APPROVED`
- 정책: `REPAIR_SETTINGS_POLICY: SETTINGS_ONLY_DEFERRED_TO_FIRST_LIVE_SETTLEMENT`
- 구현 상태: `V2_IMPLEMENTATION_NOT_STARTED`

## 1. 검수 질문

일반 `TACTICAL_PLANNING`에서 수리 작업자 수를 변경할 때 건설·업그레이드와 동일한 공유 1초 horizon을 적용할 것인지, 또는 설정만 planning branch에 반영하고 실제 비용·치유는 전투 재개 후 기존 1초 정산 경계에서 처리할 것인지 검수했다.

사용자는 권장안을 승인했다.

## 2. 승인된 결론

```text
planning 중 repair worker count 설정 가능
planning 중 repair HP gain = 0
planning 중 repair gold debit = 0
planning horizon repair eligibility = excluded
confirm 시 worker change request만 원자 승격
첫 live 1초 settlement에서 요청 적용→부족 해소→차감→치유
```

## 3. 기각한 대안

### 수리에도 planning 1초 horizon 적용

기각 사유:

- planning 진입 반복으로 무료 치유 악용 가능.
- 건설·업그레이드 작업과 글로벌 유지보수 예산을 같은 가상 시간축에 혼합.
- 여러 구조물의 한계 임금 제거 순서를 planning branch에서 조기 실행해야 함.
- confirm 시 동일 정산을 재적용할 위험.

### 확정 순간 즉시 1초분 차감·치유

기각 사유:

- deterministic live settlement boundary를 건너뜀.
- 요청 적용→글로벌 부족 해소→차감→치유 순서를 깨뜨림.
- 실제 전투 시간이 흐르지 않았는데 HP와 금화가 변함.

## 4. 주요 공격 시나리오

### F-28-A 반복 진입 무료 수리

전술계획을 반복해서 열고 닫아도 planning 중 HP 증가와 금화 차감은 모두 0이다.

### F-28-B 기존 수리 작업

진입 전에 이미 수리 중인 구조물도 entry 상태에서 정지한다. planning 중 정산 경계가 지나가지 않으며 현실 시간은 simulation time에 포함하지 않는다.

### F-28-C 여러 번 설정 변경

같은 구조물에 3명→5명→2명으로 변경하면 최종 2명 요청만 남는다. 변경 횟수만큼 수리 진행이나 비용이 누적되지 않는다.

### F-28-D 금화 부족

planning preview는 예상값이다. confirm 후 첫 live 정산에서 실제 live 금화를 기준으로 기존 글로벌 부족 해소 규칙이 작업자를 줄인다. preview가 affordability를 보장하거나 금화를 escrow하지 않는다.

### F-28-E 대상 철거·소유권 상실

최종 planning replay에서 대상이 수리 불가 상태면 전체 confirm을 차단한다. 수리 설정을 조용히 삭제하거나 다른 구조물에 자동 재지정하지 않는다.

### F-28-F 확정 실패

전체 transaction 실패 시 repair request 등록, HP, 금화, timer, 시간 재개 mutation은 모두 0이다.

### F-28-G 중복 transaction

동일 `planning_commit_transaction_id` 재요청은 같은 receipt를 반환하며 요청 등록·정산·치유·차감을 중복하지 않는다.

## 5. 계약 체크리스트

- [x] 수리는 공유 planning 1초 horizon에서 제외.
- [x] planning 중 HP 증가 0.
- [x] planning 중 금화 차감 0.
- [x] planning 중 금화 hold 없음.
- [x] 구조물별 최신 설정만 유지.
- [x] queue revision mutation당 정확히 1회.
- [x] entry snapshot부터 replay.
- [x] confirm 시 request만 승격.
- [x] 첫 live 정산에서 요청 적용.
- [x] 글로벌 affordability와 tie-break 유지.
- [x] stale·실패·중복 요청 zero-duplication.
- [x] 위험 전투 제외.
- [x] 제품 코드 승인 없음.

## 6. 범위 보호

```text
PRODUCT_CODE_AUTHORIZED: NO
V2_IMPLEMENTATION: NOT_STARTED
FINAL_CODEX_HANDOFF: NOT_AUTHORIZED
```

이번 검수는 수리 단가·치유량·작업자 상한 또는 위험 전투 UI를 확정하지 않는다.
