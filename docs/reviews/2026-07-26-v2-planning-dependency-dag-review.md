# V2 전술계획 의존성 DAG·Provisional ID 적대적 검수

- 작성일: 2026-07-26
- 상태: `REVIEW_DECISION_RECORDED / PRODUCT_CODE_NOT_AUTHORIZED`
- 대상 Issue: `#69`
- 승인 문서: `docs/design/APPROVED_V2_PLANNING_DEPENDENCY_DAG_AND_PROVISIONAL_IDS_2026-07-26.md`
- 상위 계약:
  - `docs/design/APPROVED_V2_PLANNING_REVALIDATION_ALL_OR_NOTHING_2026-07-26.md`
  - `docs/design/APPROVED_MAPRUN_STAGE_WAVE_AND_MIDPOINT_CORE_V1.md`

## F-16 — 같은 planning batch 내부의 선행 결과 참조

### 공격 시나리오

플레이어가 다음 예약을 한 계획에 넣는다.

```text
예약 1: 병영 건설 시작
예약 2: 예약 1의 병영을 업그레이드
예약 3: 예약 1이 생산할 객체에 후속 명령
```

예약 2와 3이 실제로 아직 존재하지 않는 객체를 이름·유형·UI 위치로 추정해 찾으면 다음 오류가 발생할 수 있다.

- 다른 기존 병영에 잘못 연결.
- 건설 중 병영을 완성된 것으로 간주.
- 건설 시간과 업그레이드 시간을 계획 단계에서 생략.
- 선행 예약 일부가 실제 적용된 뒤 후속 검증 실패.
- rollback 뒤 고아 객체 또는 ID 잔존.
- replay에서 provisional target과 실제 객체의 대응 불명.

## 검토한 선택지

### A. 명시적 DAG와 provisional ID — 승인

```text
producer reservation
→ 안정적 provisional output 선언
→ dependent reservation이 producer와 output을 명시 참조
→ reservation_sequence 기반 가상 상태 계산
→ 전체 검증
→ 원자 commit
```

채택 이유:

- 사용자 의도를 명시적으로 보존한다.
- 아직 없는 객체를 안전하게 참조할 수 있다.
- 순수 plan 단계와 실제 commit 단계를 분리한다.
- 전체 batch 원자성과 rollback 계약을 유지한다.
- receipt에서 계획 객체와 실제 객체를 추적할 수 있다.

### B. batch 내부 참조 전면 금지 — 기각

기각 이유:

- 계획 모드에서 연계 명령을 표현할 수 없다.
- 사용자가 같은 전술계획 안에서 객체 생성과 허용된 후속 설정을 묶을 수 없다.
- 안전성은 높지만 기능 제약이 과도하다.

### C. 선행 예약 실제 적용 뒤 후속 검증 — 기각

기각 이유:

- 중간 authoritative 상태를 노출한다.
- 후속 실패 시 부분 성공과 복잡한 rollback이 생긴다.
- 승인된 `PLANNING_BATCH_COMMIT: ATOMIC_ALL_OR_NOTHING`과 충돌한다.

## 승인된 불변 조건

```text
PLANNING_DEPENDENCY_MODEL: EXPLICIT_DAG
PROVISIONAL_ID_REQUIRED_FOR_INTRA_BATCH_REFERENCE: YES
DEPENDENCY_EDGE_MUST_POINT_TO_EARLIER_SEQUENCE: YES
IMPLICIT_INTRA_BATCH_REFERENCE: FORBIDDEN
TIME_ACCELERATION_IN_VIRTUAL_STATE: FORBIDDEN
PROVISIONAL_TO_ACTUAL_ID_MAP_IN_RECEIPT: REQUIRED
```

## 수명주기 공격

건설 예약의 commit 직후 상태는 `UNDER_CONSTRUCTION`이다.

```text
producer provides: CONSTRUCTION_SITE_EXISTS
consumer requires: COMPLETED_BUILDING
→ BLOCKED
```

가상 상태 계산은 전투 시간이나 건설 시간을 진행시키지 않는다. 업그레이드 시작도 완료 Tier를 같은 batch에 제공하지 않는다.

제품 command schema가 명시적으로 허용하는 capability만 dependent 예약이 소비할 수 있다.

## 그래프 무결성 공격

다음은 전체 차단 또는 invariant violation이다.

- 누락된 producer.
- 삭제된 producer의 dangling reference.
- consumer 이후 sequence의 future producer 참조.
- self-dependency.
- cycle.
- 중복 provisional ID.
- 잘못된 object kind 또는 output slot.
- 제공되지 않는 capability.
- stale queue revision reference.

DAG가 reservation sequence를 재정렬해서는 안 된다. dependency edge는 항상 더 낮은 sequence를 가리켜야 한다.

## rollback 공격

producer 객체 생성 뒤 consumer mutation이 실패하는 경우:

```text
전체 건물·ID registry·금화·식량·TokenSource·PendingReward·spawn·스킬 rollback
→ planning 유지
→ simulation 재개 0
```

producer 객체나 tentative actual ID가 고아 상태로 남는 것은 허용하지 않는다.

## idempotency 공격

동일 `planning_commit_transaction_id` 재요청은 기존 receipt와 동일 provisional-to-actual map을 반환한다.

중복 mapping, 객체 생성, 비용 차감 또는 후속 mutation은 0이어야 한다.

## 사용자 수정 공격

producer 삭제·수정·재정렬 시:

```text
queue_revision 증가
→ 과거 report·map stale
→ 전체 DAG 재검증
```

dependent 예약을 자동 삭제하거나 다른 producer로 자동 연결하지 않는다.

생산자 취소 시 dependent 예약을 UX에서 어떻게 정리할지는 후속 검수로 남긴다.

## 범위 판정

이번 결정은 다음을 확정하지 않는다.

- 각 command type의 전체 capability 목록.
- 생산자 취소 시 dependent 예약의 일괄 취소·개별 수정 UX.
- 제품 UI의 구체적인 그래프 표현.
- 실제 Godot 객체 ID 생성 구현.

## 검수 결론

```text
F-16: RESOLVED
DECISION: EXPLICIT_DEPENDENCY_DAG_WITH_PROVISIONAL_IDS
TIME_ACCELERATION: FORBIDDEN
PRODUCER_CANCEL_DEPENDENT_UX_POLICY: REVIEW_PENDING
PRODUCT_CODE_AUTHORIZED: NO
V2_IMPLEMENTATION: NOT_STARTED
FINAL_CODEX_HANDOFF: BLOCKED_UNTIL_EXACT_REVIEW_COMPLETE_COMMAND
```
