# 승인된 전술계획 의존성 DAG·Provisional ID 계약

- 승인일: 2026-07-26
- 상태: `V2_SPEC_APPROVED / PRODUCT_CODE_NOT_AUTHORIZED`
- 승인 근거: 사용자 권장안 승인
- 상위 책임:
  - `docs/design/APPROVED_V2_PLANNING_REVALIDATION_ALL_OR_NOTHING_2026-07-26.md`
  - `docs/design/APPROVED_V2_SPIN_SESSION_TACTICAL_RESUME_GATE_2026-07-26.md`
  - `docs/design/APPROVED_MAPRUN_STAGE_WAVE_AND_MIDPOINT_CORE_V1.md`
  - `docs/design/APPROVED_V2_TRANSACTION_FOUNDATION_SEQUENCE_2026-07-26.md`

이 문서는 일반 `TACTICAL_PLANNING`의 같은 원자 batch 안에서 선행 예약이 생산할 객체나 상태를 후속 예약이 참조할 때의 명시적 의존성 그래프, provisional ID, 가상 상태 계산, 수명주기와 receipt 계약을 소유한다.

## 1. 승인된 핵심 결정

```text
PLANNING_DEPENDENCY_MODEL: EXPLICIT_DAG
PROVISIONAL_ID_REQUIRED_FOR_INTRA_BATCH_REFERENCE: YES
DEPENDENCY_EDGE_MUST_POINT_TO_EARLIER_SEQUENCE: YES
IMPLICIT_INTRA_BATCH_REFERENCE: FORBIDDEN
MISSING_PRODUCER: BLOCK_ENTIRE_PLAN
FORWARD_REFERENCE: BLOCK_ENTIRE_PLAN
DEPENDENCY_CYCLE: INVARIANT_VIOLATION
TIME_ACCELERATION_IN_VIRTUAL_STATE: FORBIDDEN
PROVISIONAL_TO_ACTUAL_ID_MAP_IN_RECEIPT: REQUIRED
PLANNING_BATCH_COMMIT: ATOMIC_ALL_OR_NOTHING
```

같은 batch의 예약은 독립 예약과 의존 예약으로 구분한다.

- 독립 예약은 현재 authoritative snapshot만 참조한다.
- 의존 예약은 `depends_on_reservation_ids`와 생산자가 발급한 provisional output을 명시적으로 참조한다.
- UI 위치, 이름 일치, 같은 건물 유형, 가장 최근 예약과 같은 암묵적 추론은 참조 근거가 아니다.

## 2. 예약 데이터 계약

의존성을 사용하는 예약은 최소 다음 정보를 가진다.

```text
planning_session_id
queue_revision
reservation_id
reservation_sequence
command_type
depends_on_reservation_ids
input_references
output_declarations
required_capabilities
```

생산 예약의 output declaration은 최소 다음을 가진다.

```text
provisional_id
producer_reservation_id
output_slot
object_kind
lifecycle_state
provided_capabilities
```

소비 예약의 input reference는 최소 다음을 가진다.

```text
provisional_id
expected_producer_reservation_id
expected_object_kind
required_lifecycle_state
required_capabilities
```

생산자가 선언하지 않은 출력이나 capability를 소비자가 추정해서 사용해서는 안 된다.

## 3. Provisional ID

provisional ID는 planning session 안에서 안정적이고 충돌하지 않아야 한다.

권장 결정론적 basis:

```text
planning_session_id
producer_reservation_id
output_slot
object_kind
```

예:

```text
reservation R-17: 병영 건설
output slot 0
→ provisional_building_id = PB-R17-0
```

필수 규칙:

- 같은 `queue_revision`에서 동일 producer와 output slot은 동일 provisional ID를 반환한다.
- 서로 다른 출력이 같은 provisional ID를 공유하면 invariant violation이다.
- provisional ID는 authoritative 실제 객체 ID namespace와 구분한다.
- queue 수정으로 생산 예약의 정체성 또는 출력이 바뀌면 이전 provisional ID 참조는 stale이다.
- provisional ID 자체는 실제 객체가 아니며 commit 전 authoritative registry에 등록하지 않는다.

## 4. 의존성 DAG 검증

모든 명시적 의존성은 다음 조건을 만족해야 한다.

```text
producer exists in same planning queue
producer.reservation_sequence < consumer.reservation_sequence
producer declares referenced provisional output
object kind matches
required lifecycle and capabilities are provided
no dependency cycle
```

다음은 전체 계획을 차단한다.

- 존재하지 않는 producer 참조.
- producer 삭제 뒤 남은 dangling reference.
- consumer보다 뒤 sequence의 producer를 참조하는 future reference.
- 잘못된 output slot 또는 provisional ID.
- 객체 유형 불일치.
- 제공되지 않는 capability 요구.
- stale queue revision의 provisional reference.

중복 sequence, self-dependency, 순환 dependency는 임의 보정하지 않고 `INVARIANT_VIOLATION`으로 보고한다.

## 5. 순서와 위상 계산

사용자가 보는 기본 우선순위는 `reservation_sequence`다.

DAG edge는 이 순서를 뒤집는 수단이 아니다. 모든 edge가 더 낮은 sequence의 producer를 가리켜야 하므로, 순수 plan 계산은 `reservation_sequence` 오름차순으로 수행하면서도 dependency precondition을 검증할 수 있다.

```text
authoritative snapshot 복제
→ reservation_sequence 오름차순
→ producer output을 virtual state에 선언
→ consumer input·capability 검증
→ 모든 예약 통과
→ PlanningCommitPlan 생성
```

독립 예약 사이의 tie-break 역시 sequence만 사용한다. UI 배열 순서, 생성 시각, 객체 ID 사전식 정렬은 권위가 아니다.

## 6. 수명주기와 시간 가속 금지

가상 상태는 commit 직후의 논리적 상태만 표현한다. 전투 시간, 건설 시간, 업그레이드 시간, cooldown 시간이 흐른 것으로 간주하지 않는다.

대표 사례:

```text
예약 1: 병영 건설 시작
→ provisional output lifecycle = UNDER_CONSTRUCTION
→ capability = CONSTRUCTION_SITE_EXISTS

예약 2: 예약 1 병영을 Tier 2로 업그레이드
→ requires lifecycle = COMPLETED
→ BLOCKED
```

건설 시작 예약은 같은 batch에서 다음을 생산하지 않는다.

- 완성 건물.
- 활성 TokenSource.
- 완성 Tier 패시브.
- 사용 가능한 생산·업그레이드 capability.
- 건설 시간이 경과한 상태.

업그레이드 시작도 같은 batch 후속 예약에 완료 Tier를 제공하지 않는다.

후속 예약은 producer가 commit 직후 실제로 제공하는 lifecycle과 capability만 사용할 수 있다. 완료 이벤트가 필요한 상태는 이후 simulation에서 authoritative 완료가 발생한 뒤 새 planning session에서 참조한다.

## 7. 허용 가능한 intra-batch 참조

다음 조건을 모두 만족할 때만 provisional output 참조가 가능하다.

- producer가 같은 batch에서 해당 객체를 commit 시점에 실제 생성한다.
- 소비자가 요구하는 lifecycle이 commit 직후 제공된다.
- producer가 required capability를 명시적으로 선언한다.
- 제품 규칙상 해당 command가 미완성 객체를 대상으로 허용된다.

예를 들어 제품 규칙이 건설 중 사이트의 rally marker 설정을 허용한다면 다음은 가능할 수 있다.

```text
예약 1: 건설 사이트 생성
→ capability = ACCEPTS_RALLY_MARKER
예약 2: provisional site의 rally marker 설정
```

반대로 완료 건물만 가능한 업그레이드·생산·TokenSource 활성화는 차단한다.

이 문서는 구체적으로 어떤 command가 어떤 capability를 제공하거나 요구하는지는 후속 패키지의 command schema가 명시하도록 요구한다. 암묵적 허용은 금지한다.

## 8. 생산자 삭제·수정·재정렬

생산 예약을 삭제하거나 출력 정체성을 바꾸면 모든 dependent reference는 stale이다.

```text
producer mutation
→ queue_revision 증가
→ dependency graph 재구축
→ 과거 PlanningRevalidationReport 폐기
→ 과거 provisional ID map 폐기
→ 전체 큐 재검증
```

dependent 예약을 자동으로 삭제하거나 다른 producer에 자동 연결하는 것은 금지한다.

생산자 취소 시 dependent 예약의 구체적인 UX 처리, 예를 들어 일괄 취소 제안 또는 개별 수정 요구는 별도 검수 대상으로 남긴다. 정본 불변 조건은 동의 없는 자동 삭제가 없다는 점이다.

## 9. 순수 PlanningCommitPlan

DAG 검증과 가상 상태 계산은 실제 상태를 변경하지 않는 순수 단계다.

`PlanningCommitPlan`은 최소 다음을 포함한다.

```text
planning_commit_transaction_id
planning_session_id
queue_revision
basis_revision_hash
ordered_reservation_ids
dependency_edges
provisional_output_declarations
provisional_to_tentative_actual_id_map
aggregate resource reservations
ordered mutations
rollback journal
```

plan 계산 중에는 다음을 하지 않는다.

- authoritative ID registry 영구 등록.
- 실제 건물 생성.
- 실제 unit spawn.
- 금화·식량 차감.
- PendingReward 소비.
- simulation clock 진행.

## 10. 실제 ID 배정

commit 전에 각 provisional output에 대응하는 tentative actual ID를 결정론적으로 배정할 수 있다.

필수 조건:

- 동일 transaction 재시도에서 동일 대응 관계를 얻는다.
- 이미 존재하는 authoritative ID와 충돌하지 않는다.
- provisional ID 하나는 actual ID 하나에만 대응한다.
- producer mutation이 있으면 새 transaction과 새 map을 사용한다.
- map 배정만으로 객체가 authoritative하게 존재하는 것으로 간주하지 않는다.

성공 receipt는 다음 mapping을 보존한다.

```text
provisional_id → actual_id
producer_reservation_id
object_kind
committed_lifecycle_state
```

후속 시스템과 replay는 이 receipt를 통해 사용자가 계획에서 본 provisional target과 실제 객체를 추적할 수 있다.

## 11. 원자 commit과 rollback

모든 DAG·수명주기·자원·동의 검증이 통과했을 때만 전체 batch를 커밋한다.

```text
최종 basis·queue revision 재확인
→ tentative actual ID 충돌 검사
→ aggregate 자원 예약
→ producer·consumer mutation 준비
→ 전체 상태 전이
→ provisional-to-actual map과 receipt 기록
→ simulation 재개
```

허용 결과:

```text
전체 성공 + PlanningCommitReceipt
또는
전체 상태 변경 0
```

producer 생성 뒤 consumer mutation이 실패해도 producer 객체를 남기지 않는다. 금화, 식량, 건물, TokenSource, PendingReward, 유닛, 스킬, ID registry, receipt와 재개 상태를 전체 rollback한다.

## 12. idempotency

동일 `planning_commit_transaction_id` 재요청은 기존 `PlanningCommitReceipt`를 반환한다.

중복 요청은 다음을 만들지 않는다.

- provisional-to-actual mapping 재배정.
- 실제 객체 중복 생성.
- 후속 mutation 중복 실행.
- 자원 재차감.
- simulation 중복 재개.

queue 또는 authoritative basis가 바뀌면 기존 transaction ID와 plan을 재사용하지 않는다.

## 13. UI 계약

UI는 dependent 예약에 최소 다음을 표시할 수 있어야 한다.

- 생산 예약.
- provisional target의 식별 가능한 이름.
- 현재 lifecycle.
- 요구 capability.
- dependency가 유효한지 여부.
- 생산자 변경·삭제 시 영향을 받는 dependent 예약.

차단 예:

```text
이 업그레이드는 완성된 병영이 필요합니다.
같은 계획에서 새로 시작하는 병영은 아직 건설 중이므로 대상이 될 수 없습니다.
```

실제 ID가 아직 없다는 사실을 숨기기 위해 임의 기존 객체에 연결해서는 안 된다.

## 14. 자동 검증 계약

최소 다음 사례를 검증한다.

1. 선행 producer와 명시적 provisional output 참조 → DAG 유효.
2. producer 없는 reference → 전체 차단.
3. consumer보다 뒤 sequence의 producer 참조 → 전체 차단.
4. self-dependency 또는 cycle → invariant violation.
5. 같은 provisional ID 중복 생산 → invariant violation.
6. 객체 유형 또는 output slot 불일치 → 전체 차단.
7. 요구 capability 미제공 → 전체 차단.
8. 건설 시작 뒤 완료 건물 요구 업그레이드 → 시간 가속 없이 차단.
9. 허용된 `UNDER_CONSTRUCTION` capability 소비 → 순수 plan 생성 가능.
10. producer 삭제 뒤 dependent 자동 삭제 0, 전체 재검증.
11. commit 중 consumer 실패 → producer 실제 객체와 ID registry까지 rollback.
12. 성공 receipt가 provisional-to-actual mapping 보존.
13. 동일 transaction 재요청 → mapping·객체·비용 중복 0.
14. 서로 다른 렌더 프레임률에서도 같은 queue log가 같은 plan·mapping 생성.

## 15. 현재 상태

```text
PLANNING_DEPENDENCY_DAG: APPROVED
PROVISIONAL_ID_CONTRACT: APPROVED
TIME_ACCELERATION_IN_VIRTUAL_STATE: FORBIDDEN
PRODUCER_CANCEL_DEPENDENT_UX_POLICY: REVIEW_PENDING
PRODUCT_CODE_AUTHORIZED: NO
V2_IMPLEMENTATION: NOT_STARTED
HUMAN_QA: NOT_RUN
CORE_LOCK_V2: PENDING
```
