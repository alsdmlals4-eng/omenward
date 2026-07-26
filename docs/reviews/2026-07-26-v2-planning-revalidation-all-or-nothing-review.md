# V2 전술계획 재검증 실패 처리 적대적 검수

- 작성일: 2026-07-26
- 상태: `REVIEW_DECISION_RECORDED / PRODUCT_CODE_NOT_AUTHORIZED`
- 대상 Issue: `#69`
- 승인 문서: `docs/design/APPROVED_V2_PLANNING_REVALIDATION_ALL_OR_NOTHING_2026-07-26.md`
- 상위 계약:
  - `docs/design/APPROVED_V2_SPIN_SESSION_TACTICAL_RESUME_GATE_2026-07-26.md`
  - `docs/design/APPROVED_MAPRUN_STAGE_WAVE_AND_MIDPOINT_CORE_V1.md`

## F-15 — 재검증 실패 예약이 포함된 계획의 처리

### 공격 시나리오

룰렛 확정 뒤 기존 예약 큐를 최신 상태로 재검증한다.

```text
예약 1: 병영 건설 — VALID
예약 2: 전설 배치 — BLOCKED / FOOD_INSUFFICIENT
예약 3: 전술 스킬 — VALID
```

정책이 없으면 구현이 다음 중 하나를 임의로 선택할 수 있다.

- 유효 예약 1과 3만 적용.
- 실패 예약 2를 자동 삭제.
- 전체 예약을 적용한 뒤 2만 실패 처리.
- 자원을 일부 차감한 상태로 planning 유지.
- 전투를 재개하면서 실패 예약을 UI에서 숨김.

이 결과들은 플레이어가 구성한 하나의 계획, 예약 간 공유 자원과 기존 `비용 일괄 차감·동시 적용` 계약을 훼손한다.

## 검토한 선택지

### A. 실패 하나라도 전체 커밋 차단 — 승인

```text
전체 큐 재검증
→ 실패 또는 필수 동의 미해결 발견
→ 전체 미적용
→ [전투 재개] 차단
→ 플레이어 수정·취소
→ 전체 큐 재검증
→ 전부 유효하면 원자 커밋
```

채택 이유:

- 사용자 계획의 의미를 유지한다.
- 유효 예약과 실패 예약의 숨은 의존성을 보존한다.
- 자동 취소나 부분 적용으로 인한 동의 침해가 없다.
- 기존 전술계획 batch 계약과 일치한다.
- rollback 경계가 하나로 명확하다.

### B. 유효 예약만 부분 적용 — 기각

기각 이유:

- 일부 건설이나 배치가 이후 예약의 자원·대상 상태를 바꾼다.
- UI에서 본 계획과 실제 적용 결과가 달라진다.
- 실패 예약 수정 뒤 이미 적용된 명령과의 재결합이 복잡하다.
- 부분 성공 receipt와 rollback 정책이 불필요하게 늘어난다.

### C. 실패 예약 자동 취소 — 기각

기각 이유:

- 사용자가 작성한 명령을 명시적 동의 없이 삭제한다.
- 일시적 자원 부족과 영구 invalid를 구분하지 못할 수 있다.
- 전설 변환 동의처럼 사용자가 해결할 수 있는 상태를 잃는다.

## 승인된 불변 조건

```text
PLANNING_REVALIDATION_FAILURE_POLICY: APPROVED_ALL_OR_NOTHING
ANY_INVALID_RESERVATION_BLOCKS_RESUME: YES
UNRESOLVED_MANDATORY_CONSENT_BLOCKS_RESUME: YES
PARTIAL_APPLY: FORBIDDEN
AUTO_CANCEL_FAILED_RESERVATION: FORBIDDEN
PLANNING_BATCH_COMMIT: ATOMIC
```

차단 중에는 다음 상태가 모두 변하지 않아야 한다.

- 금화.
- 식량.
- 건물·업그레이드·철거.
- TokenSource와 live 릴.
- PendingReward.
- 전장 유닛.
- 스킬 비용·쿨다운·효과.
- simulation clock.

## 재검증 보고

각 예약은 `VALID`, `BLOCKED`, `INVARIANT_VIOLATION` 중 하나로 보고한다.

`BLOCKED`에는 최신 요구값과 플레이어가 취할 수 있는 수정·취소·동의 갱신 행동이 포함되어야 한다.

큐 변경 시:

```text
queue_revision 증가
→ 과거 PlanningRevalidationReport stale
→ 과거 mandatory consent basis stale 가능
→ 전체 큐 재검증
```

## commit 실패 공격

모든 예약이 사전 검증을 통과해도 실제 commit 중 spawn 또는 건물 mutation이 실패할 수 있다.

승인된 결과:

```text
전체 성공
또는
전체 rollback + planning 유지
```

금지되는 결과:

- 금화만 차감.
- 건물만 생성.
- 영웅 1기만 spawn.
- 일부 스킬만 발동.
- 실패 뒤 simulation만 재개.
- 기존 성공 부분을 조용히 유지.

## idempotency 공격

동일 `planning_commit_transaction_id`가 재호출되어도 기존 `PlanningCommitReceipt`만 반환하고 중복 적용하지 않는다.

큐나 authoritative basis가 바뀌었다면 기존 transaction을 재사용하지 않고 새 plan과 transaction ID를 만든다.

## 범위 판정

이번 결정은 다음을 확정하지 않는다.

- 한 batch 안에서 선행 예약이 만든 provisional 건물·유닛을 후속 예약이 참조할 수 있는지.
- 허용되는 예약 의존성 그래프와 내부 plan 계산 순서.
- 제품 UI의 구체적인 색상·레이아웃.

이 항목은 후속 적대적 검수 대상으로 남긴다.

## 검수 결론

```text
F-15: RESOLVED
DECISION: BLOCK_ENTIRE_PLANNING_COMMIT_ON_ANY_FAILURE
PRODUCT_CODE_AUTHORIZED: NO
V2_IMPLEMENTATION: NOT_STARTED
FINAL_CODEX_HANDOFF: BLOCKED_UNTIL_EXACT_REVIEW_COMPLETE_COMMAND
```
