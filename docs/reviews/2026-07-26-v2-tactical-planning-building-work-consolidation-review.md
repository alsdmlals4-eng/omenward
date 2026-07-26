# V2 전술계획 건물 작업 통합 적대적 검수

- 검수일: 2026-07-26
- 대상: `APPROVED_V2_TACTICAL_PLANNING_BUILDING_WORK_CONSOLIDATED_2026-07-26.md`
- 검수 ID: `F-29`
- 상태: `F-29: RESOLVED`
- 결과: `F-29_RESULT: APPROVED`
- 사용자 결정: 건설 중 구조물 유료 수리 `A`
- 사용자 요청: 지금까지 결정 통합 요약 및 PR 병합

## 1. 검수 목적

이번 검수는 PR #82~#91에서 개별 승인된 전술계획 건물 작업 규칙이 한 문서에서 모순 없이 연결되는지, 과거 통합 원장의 상충 필드가 최신 승인으로 명시적으로 대체되는지, 건설 중 구조물 수리가 planning horizon과 live repair settlement를 혼합하지 않는지 확인한다.

```text
F-29_RESULT: APPROVED
TACTICAL_PLANNING_BUILDING_WORK_CONSOLIDATION: APPROVED
CONSTRUCTING_STRUCTURE_PAID_REPAIR_POLICY: APPROVED
PRODUCT_CODE_AUTHORIZED: NO
```

## 2. 최신 정본 우선순위 검수

| 과거 또는 분산 규칙 | 최신 통합 결과 | 판정 |
|---|---|---|
| 사용자가 명령 순서를 재정렬할 수 있다는 가정 | reorder UI 없음, 시스템 생성 순서 고정 | PASS |
| planning 전후 룰렛 결과 재계산 가능성 | immutable SpinSnapshot과 PendingReward identity 유지 | PASS |
| 확정 전 live world mutation | planning branch와 virtual ledger만 변경 | PASS |
| 통합 원장 GM-44 자발적 취소 일괄 50% | 기존 진행 건설 70%, 업그레이드 50% | PASS |
| 통합 원장 GM-47 누적 투자금 50% 철거 환급 | 최초 기본 건설 실제 지불액 40%만 | PASS |
| 통합 원장 GM-46 tactical planning 철거 시간 진행 | branch 즉시 제거·node 해제, confirm 시 승격 | PASS |
| 전술계획 중 모든 공사 정지 | live 공사는 정지, 신규 branch 작업만 공유 1초 horizon | PASS |
| 수리를 신규 공사 1초 horizon에 포함 | 수리 제외, live settlement까지 HP·비용 0 | PASS |

## 3. 공유 1초 horizon 공격 검수

### F-29-A — 독립 명령마다 별도 무료 1초

공격:

```text
건물 A 신규 건설
건물 B 신규 건설
각각 별도 1초를 받는가?
```

결과:

- 둘 다 같은 `t=0~1초` 구간에서 병렬 진행한다.
- 세션이 사용하는 가상 시간은 총 1초다.
- 명령 수만큼 시간축이 늘어나지 않는다.

판정: PASS.

### F-29-B — queue replay로 진행도 누적

공격:

```text
건설 추가
→ 1초 진행
→ 수리 작업자 변경
→ replay
→ 건설이 2초 진행되는가?
```

결과:

- entry snapshot과 전체 명령 집합에서 다시 계산한다.
- 이전 branch progress에 덧붙이지 않는다.
- 건설 진행도는 동일한 공유 horizon 결과다.

판정: PASS.

### F-29-C — 기존 live 작업에 무료 1초

공격:

- 9.5초 진행된 10초 건설 상태에서 planning 반복 진입.

결과:

- existing live work는 entry progress에서 정지한다.
- 공유 horizon eligibility가 없다.
- 반복 진입으로 완료할 수 없다.

판정: PASS.

## 4. 철거·취소·환급 공격 검수

### F-29-D — 업그레이드 누적 투자금 철거 환급

공격:

```text
기본 건설 실제 지불 40
완료 업그레이드 실제 지불 45
철거 시 (40+45)의 40% 또는 50% 지급 시도
```

결과:

```text
floor(40 * 40 / 100) = 16
```

완료 업그레이드 45는 철거 basis에서 제외한다.

판정: PASS.

### F-29-E — active upgrade와 완공 건물 철거를 하나의 credit으로 합치기

공격:

- 진행 중 업그레이드 취소 50%와 기본 건설 40% 철거 환급의 provenance를 하나로 합쳐 중복 또는 누락 유발.

결과:

- 별도 ledger entry type과 payment snapshot을 사용한다.
- 하나의 demolition transaction에서 원자 승격할 수 있으나 계산 basis는 분리한다.

판정: PASS.

### F-29-F — provisional 건물 제거에 live 환급 지급

공격:

- 같은 planning session에서 아직 지불되지 않은 신규 건물을 제거하고 70% 또는 40% 환급 생성.

결과:

- live payment가 없으므로 refund가 아니다.
- planned debit release만 수행한다.

판정: PASS.

## 5. 건설 중 수리 공격 검수

### F-29-G — planning 1초 동안 무료 치유

공격:

```text
provisional 건물 생성
→ 수리 작업자 설정
→ planning horizon에서 HP 증가 또는 금화 차감
```

결과:

- repair는 공유 신규 작업 horizon에서 제외한다.
- planning branch HP 증가 0.
- planning gold debit 0.
- 확정 후 첫 live settlement부터 처리한다.

판정: PASS.

### F-29-H — 건설 허용 최대 HP 초과 수리

공격:

- 현재 construction progress에서 허용 최대 HP가 40인데 HP 35에 20 치유 시도.

결과:

```text
repairable_missing_hp = 40 - 35 = 5
actual_repair_hp = min(20, 5) = 5
```

- overheal 비용은 부과하지 않는다.
- 건설 진행 후 허용 최대 HP가 증가해도 자동 무료 보충하지 않는다.

판정: PASS.

### F-29-I — 파괴된 provisional target에 수리 비용 부과

공격:

- confirm 뒤 첫 settlement 전에 건설물이 HP 0으로 파괴됨.

결과:

- construction failure.
- repair request 종료.
- 실행되지 않은 settlement의 금화 차감과 치유 0.
- 다른 target으로 자동 이전 없음.

판정: PASS.

### F-29-J — provisional ID dangling

공격:

- 신규 건설 R1에 수리 R2를 설정한 뒤 R1 취소.

결과:

- R2는 R1의 provisional output dependent다.
- producer cancel cascade로 함께 제거한다.
- stable provisional ID를 재사용하거나 다른 건물에 rebind하지 않는다.

판정: PASS.

### F-29-K — 건설 완료와 첫 수리 settlement 경계

공격:

- confirm 후 첫 repair settlement 전에 건설이 완료됨.

결과:

- settlement 시점의 실제 lifecycle을 사용한다.
- active가 됐다면 active structure 최대 HP와 수리 규칙을 적용한다.
- construction cap을 과거 snapshot처럼 고정하지 않는다.

판정: PASS.

## 6. stale·원자성·idempotency 검수

### F-29-L — 오래된 preview 승인

공격:

- repair worker preview 이후 building lifecycle, queue revision 또는 dependent set 변경.

결과:

```text
STALE_TACTICAL_PLANNING_BUILDING_WORK_PREVIEW
→ 상태 변경 0
→ 최신 preview 재생성
```

판정: PASS.

### F-29-M — confirm 일부 성공

공격:

- 건설은 승격되지만 repair request 또는 refund ledger만 실패.

결과:

- 전체 planning commit이 실패한다.
- 건물, node, work timer, gold, HP, repair request, resume mutation 모두 0이다.

판정: PASS.

### F-29-N — duplicate transaction

공격:

- 동일 `planning_commit_transaction_id` 재전송.

결과:

- 동일 receipt 반환.
- 건설 headstart, refund, repair request, gold debit, healing, simulation resume를 중복하지 않는다.

판정: PASS.

## 7. 문서 정합성 결론

통합 문서는 다음 분리를 유지한다.

```text
planning branch projection
≠ live world mutation

new work shared one-second progress
≠ existing live work progress
≠ repair healing

planned debit release
≠ active work cancellation refund
≠ completed building demolition refund

repair setting promotion
≠ repair settlement
```

기존 세부 승인 문서는 증거로 유지하며, 최신 통합 문서는 해당 필드의 읽기 진입점과 우선순위를 제공한다.

## 8. 남은 검수

다음 한 가지 ordering은 별도 검수가 필요하다.

```text
F-30: construction progress와 repair settlement가 같은 live timestamp에 있을 때 순서
CONSTRUCTION_PROGRESS_REPAIR_SETTLEMENT_SAME_TIMESTAMP_ORDER: REVIEW_PENDING
```

이번 PR에서는 순서를 추측해 고정하지 않는다.

## 9. 범위 보호

```text
V2_IMPLEMENTATION: NOT_STARTED
PRODUCT_CODE_AUTHORIZED: NO
FINAL_CODEX_HANDOFF: NOT_AUTHORIZED
```

- 제품 코드 변경 없음.
- Scene 변경 없음.
- Resource 변경 없음.
- 게임 데이터 변경 없음.
- 최종 Codex 구현 인계 없음.
