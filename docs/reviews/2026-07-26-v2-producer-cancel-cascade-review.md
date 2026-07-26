# V2 Producer 취소 영향 확인·연쇄 취소 적대적 검수

- 작성일: 2026-07-26
- 상태: `REVIEW_DECISION_RECORDED / PRODUCT_CODE_NOT_AUTHORIZED`
- 대상 Issue: `#69`
- 승인 문서: `docs/design/APPROVED_V2_PRODUCER_CANCEL_CASCADE_2026-07-26.md`
- 상위 계약:
  - `docs/design/APPROVED_V2_PLANNING_DEPENDENCY_DAG_AND_PROVISIONAL_IDS_2026-07-26.md`
  - `docs/design/APPROVED_V2_PLANNING_REVALIDATION_ALL_OR_NOTHING_2026-07-26.md`

## F-17 — Producer 취소 시 dependent 처리

### 공격 시나리오

```text
R1: 병영 건설
└─ R2: 건설 사이트 집결지 설정
   └─ R3: 집결지 후속 명령
```

R1만 즉시 삭제하면 R2와 R3가 dangling reference로 남는다. 구현이 이를 자동 보정하려 하면 다음 문제가 발생할 수 있다.

- R2·R3를 사용자 동의 없이 조용히 삭제.
- 같은 유형의 다른 병영에 자동 연결.
- R2만 삭제하고 R3를 남김.
- invalid queue를 유지해 전투 재개를 영구 차단.
- 확인창이 열린 뒤 새 dependent가 추가됐는데 과거 동의로 함께 삭제.
- 연쇄 삭제 중 일부만 성공해 graph가 손상됨.

## 검토한 선택지

### A. 영향 확인 후 명시적 원자 연쇄 취소 — 승인

```text
producer 취소 요청
→ reverse transitive closure 계산
→ 제거될 전체 예약 preview
→ 사용자 [돌아가기] 또는 [모두 취소]
→ 최신 basis 재확인
→ 전체 removal set 원자 삭제
→ queue_revision 1회 증가
→ 전체 큐 재검증
```

채택 이유:

- 사용자가 삭제 범위를 사전에 안다.
- dangling dependency를 만들지 않는다.
- 자동 rebind로 계획 의미가 바뀌지 않는다.
- queue mutation과 rollback 경계가 하나다.
- stale 확인으로 새 dependent가 의도 없이 삭제되는 것을 막는다.

### B. Dependent를 먼저 수동 삭제해야 producer 취소 — 기각

안전하지만 깊은 dependency chain과 diamond graph에서 사용자가 삭제 순서를 역으로 추적해야 한다. 계획 모드의 조작 비용이 불필요하게 커진다.

### C. Producer만 삭제하고 dependent를 BLOCKED로 유지 — 기각

명령 보존처럼 보이지만 missing producer 상태를 의도적으로 남긴다. 전체 all-or-nothing 재개 게이트 때문에 사용자는 결국 dependent를 수동 정리해야 하고, invalid queue가 장시간 유지된다.

## 승인된 불변 조건

```text
PRODUCER_CANCEL_DEPENDENT_UX_POLICY: EXPLICIT_PREVIEW_THEN_ATOMIC_CASCADE
TRANSITIVE_DEPENDENT_CLOSURE: REQUIRED
SILENT_DEPENDENT_AUTO_DELETE: FORBIDDEN
AUTO_REBIND_TO_OTHER_PRODUCER: FORBIDDEN
DANGLING_DEPENDENT_AFTER_CANCEL: FORBIDDEN
CASCADE_CONFIRMATION_BASIS_HASH: REQUIRED
STALE_CASCADE_CONFIRMATION: REJECT_WITH_ZERO_MUTATION
CASCADE_QUEUE_MUTATION: ATOMIC
QUEUE_REVISION_INCREMENT_PER_CASCADE: EXACTLY_ONCE
POST_CASCADE_FULL_QUEUE_REVALIDATION: REQUIRED
```

## Transitive closure 공격

직접 dependent만 제거하면 다음 chain에서 R3가 dangling 상태로 남는다.

```text
R1 → R2 → R3
```

따라서 영향 집합은 root에서 reverse dependency edge를 따라 도달 가능한 모든 예약을 포함한다.

다이아몬드 graph에서도 같은 예약을 중복 제거하거나 revision을 여러 번 증가시키지 않는다.

## 공유 dependency 공격

```text
R1 producer
R2 producer
R3 requires R1 and R2
R4 depends on R3
```

R1 취소 시 R3은 필수 입력을 잃으므로 제거 대상이며 R4도 transitive dependent로 제거한다. R2가 남아 있다는 이유로 R3을 자동 유지하거나 다른 producer로 자동 연결하지 않는다.

## Stale 확인 공격

```text
queue revision 10에서 preview
→ 제거 집합 {R1, R2}
→ 확인창 열린 상태에서 R3가 R1 dependent로 추가
→ 사용자가 과거 [모두 취소] 실행
```

허용 결과:

```text
STALE_CASCADE_PREVIEW
상태 변경 0
최신 제거 집합 {R1, R2, R3} 재표시
재동의 요구
```

과거 동의로 R3까지 삭제하거나 과거 집합만 삭제해 dangling reference를 남기는 결과는 모두 금지한다.

## 원자성 공격

R1·R2·R3 삭제 중 R2 처리에 실패하면 허용 결과는 전체 mutation 전 상태뿐이다.

금지:

- R1만 삭제.
- R2·R3만 삭제.
- revision만 증가.
- report만 invalidation.
- 일부 planning hold만 해제.

## Queue revision과 stale artifact

성공한 cascade는 하나의 큐 mutation이므로 `queue_revision`을 정확히 한 번 증가시킨다.

다음 artifact는 모두 stale이다.

- `PlanningRevalidationReport`.
- `PlanningCommitPlan`.
- mandatory consent basis.
- legendary conflict consent basis.
- provisional-to-tentative-actual mapping.

남은 큐는 새 revision에서 전량 재검증한다.

## Idempotency 공격

동일 `queue_mutation_transaction_id`를 재요청해도 기존 `QueueMutationReceipt`만 반환한다.

금지:

- revision 추가 증가.
- 삭제 로그 중복.
- 새로운 removal set 계산 뒤 추가 삭제.
- stale confirm을 성공으로 취급.

## 범위 판정

이번 결정은 다음을 확정하지 않는다.

- producer 예약의 출력 일부만 제거하는 partial-output mutation UX.
- 하나의 producer가 여러 provisional output을 제공할 때 output 단위 dependency 편집 정책.
- 예약 재지정 UI의 구체적인 조작 방식.
- command type별 optional dependency schema.

현재 계약에서는 producer 예약 전체 취소와 모든 선언 dependency를 필수 입력으로 취급한다.

## 검수 결론

```text
F-17: RESOLVED
DECISION: PREVIEW_TRANSITIVE_DEPENDENTS_AND_REQUIRE_ATOMIC_CASCADE_CONFIRMATION
PRODUCT_CODE_AUTHORIZED: NO
V2_IMPLEMENTATION: NOT_STARTED
FINAL_CODEX_HANDOFF: BLOCKED_UNTIL_EXACT_REVIEW_COMPLETE_COMMAND
```
