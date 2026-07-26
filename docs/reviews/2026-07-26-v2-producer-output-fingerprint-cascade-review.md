# V2 Producer Output Fingerprint·영향 가지 Cascade 적대적 검수

- 작성일: 2026-07-26
- 상태: `REVIEW_DECISION_RECORDED / PRODUCT_CODE_NOT_AUTHORIZED`
- 대상 Issue: `#69`
- 승인 문서: `docs/design/APPROVED_V2_PRODUCER_OUTPUT_FINGERPRINT_CASCADE_2026-07-26.md`
- 상위 계약:
  - `docs/design/APPROVED_V2_PLANNING_DEPENDENCY_DAG_AND_PROVISIONAL_IDS_2026-07-26.md`
  - `docs/design/APPROVED_V2_PRODUCER_CANCEL_CASCADE_2026-07-26.md`
  - `docs/design/APPROVED_V2_PLANNING_REVALIDATION_ALL_OR_NOTHING_2026-07-26.md`

## F-18 — Producer 수정이 일부 Output 계약만 깨뜨리는 경우

### 공격 시나리오

```text
R1 producer
├─ output A: 건설 사이트
│  └─ R2 → R4
└─ output B: 전술 앵커
   └─ R3 → R5
```

플레이어가 R1을 수정해 output B를 제거하거나 B의 required capability를 없앤다.

정책이 없으면 구현은 다음 오류를 만들 수 있다.

- R2·R4까지 포함한 모든 dependent 삭제.
- R3만 삭제하고 downstream R5를 dangling 상태로 유지.
- R3·R5를 동의 없이 자동 삭제.
- output B consumer를 이름이 비슷한 다른 producer에 자동 연결.
- producer만 수정하고 invalid dependent를 큐에 남김.
- 확인창 뒤 새 dependent가 추가됐는데 과거 동의로 함께 삭제.

## 검토한 선택지

### A. Output별 fingerprint와 영향 가지 cascade — 승인

```text
output별 old/new 계약 비교
→ consumer별 compatibility 판정
→ broken direct consumer 식별
→ 해당 consumer descendants만 영향 preview
→ 명시적 동의
→ producer 수정 + 영향 예약 제거 원자 mutation
```

채택 이유:

- 변경되지 않은 output branch를 보존한다.
- capability 추가처럼 기존 consumer를 깨지 않는 변경은 불필요한 삭제를 만들지 않는다.
- destructive 변경의 범위를 사용자에게 정확히 보여준다.
- 기존 dependency DAG, cascade 확인, all-or-nothing mutation 계약과 일치한다.
- stale 확인과 idempotency 경계를 명확히 유지한다.

### B. Producer 수정 시 모든 dependent 제거 — 기각

기각 이유:

- 변경되지 않은 output을 참조하는 예약까지 삭제한다.
- producer가 output을 여러 개 제공할수록 피해 범위가 과도해진다.
- 사용자의 연계 계획을 불필요하게 파괴한다.

### C. 모든 dependent 유지 후 BLOCKED — 기각

기각 이유:

- 명백히 깨진 reference가 큐에 남는다.
- 전투 재개가 계속 차단된다.
- 사용자는 어떤 예약이 수정 때문에 깨졌는지 수동 추적해야 한다.

## 승인된 불변 조건

```text
PRODUCER_MODIFICATION_OUTPUT_POLICY: OUTPUT_FINGERPRINT_BRANCH_CASCADE
OUTPUT_CONTRACT_FINGERPRINT: REQUIRED
CONSUMER_COMPATIBILITY_CHECK: REQUIRED
UNCHANGED_OUTPUT_DEPENDENTS: PRESERVED
COMPATIBLE_CHANGED_OUTPUT_DEPENDENTS: PRESERVED_REVALIDATED
INCOMPATIBLE_OUTPUT_BRANCH_CASCADE: PREVIEW_AND_CONFIRM
AUTO_REBIND_ON_OUTPUT_CHANGE: FORBIDDEN
PRODUCER_MODIFICATION_AND_CASCADE: ATOMIC
STALE_MODIFICATION_CONFIRMATION: REJECT_WITH_ZERO_MUTATION
QUEUE_REVISION_INCREMENT_PER_MODIFICATION: EXACTLY_ONCE
POST_MODIFICATION_FULL_QUEUE_REVALIDATION: REQUIRED
```

## 호환성 공격

Fingerprint가 달라졌다는 사실만으로 모든 consumer를 제거하면 additive 변경도 destructive하게 처리된다.

승인된 판정은 consumer별 요구 충족 여부다.

```text
same producer and output identity
AND required object kind matches
AND required lifecycle satisfied
AND all required capabilities provided
AND required target semantics preserved
```

모든 조건을 만족하는 consumer branch는 보존한다.

## 부분 가지 공격

같은 output을 R2와 R3가 참조하지만 R2는 새 capability 집합으로도 유효하고 R3만 제거된 capability를 요구할 수 있다.

승인된 결과:

```text
R2 branch 유지
R3 + transitive descendants만 영향 preview
```

Output 단위로 모든 consumer를 일괄 삭제하지 않는다.

## Identity 공격

Output slot, provisional ID basis, object kind 또는 target identity가 바뀌면 같은 output처럼 보이더라도 replacement다.

기존 consumer를 새 output에 암묵적으로 연결하지 않는다. 새 provisional ID를 사용하고 기존 consumer branch를 incompatible로 판정한다.

## Stale 확인 공격

Preview 뒤 다음 변경이 발생할 수 있다.

- producer 수정안 변경.
- 새 dependent 추가.
- 기존 dependent 재지정.
- 예약 재정렬.
- queue revision 변경.

과거 `producer_modification_basis_hash`가 현재와 다르면 다음 결과만 허용한다.

```text
STALE_PRODUCER_MODIFICATION_PREVIEW
→ 상태 변경 0
→ 최신 영향 preview
→ 재동의
```

## 원자성 공격

Producer 수정 뒤 dependent 삭제 중 실패하면 수정된 producer와 남은 invalid 예약이 함께 존재할 수 있다.

승인된 결과:

```text
전체 성공 + QueueMutationReceipt
또는
전체 상태 변경 0
```

Producer 수정, 영향 예약 삭제, revision 증가와 stale artifact 폐기는 하나의 queue mutation이다.

## 재검증 공격

호환 branch를 유지했더라도 producer 비용·위치·footprint 변경으로 다른 조건이 실패할 수 있다.

따라서 cascade가 없거나 일부 branch만 제거됐더라도 성공 mutation 뒤 남은 전체 큐를 새 revision에서 재검증한다.

## Idempotency 공격

동일 `queue_mutation_transaction_id` 재요청은 기존 receipt만 반환한다.

다음 중복은 금지한다.

- producer 재수정.
- dependent 재삭제.
- queue revision 추가 증가.
- provisional ID 재발급.

## 범위 판정

이번 결정은 다음을 확정하지 않는다.

- optional dependency와 fallback producer.
- 복수 대체 output 선택 schema.
- dependency가 있는 예약의 재정렬 UX.
- command별 capability taxonomy.

## 검수 결론

```text
F-18: RESOLVED
DECISION: COMPARE_OUTPUT_CONTRACTS_AND_CASCADE_ONLY_BROKEN_BRANCHES
PRODUCT_CODE_AUTHORIZED: NO
V2_IMPLEMENTATION: NOT_STARTED
FINAL_CODEX_HANDOFF: BLOCKED_UNTIL_EXACT_REVIEW_COMPLETE_COMMAND
```
