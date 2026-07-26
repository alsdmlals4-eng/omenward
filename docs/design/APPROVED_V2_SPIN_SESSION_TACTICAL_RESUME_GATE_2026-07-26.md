# 승인된 SpinSession 전술계획 재개 게이트

- 승인일: 2026-07-26
- 상태: `V2_SPEC_APPROVED / PRODUCT_CODE_NOT_AUTHORIZED`
- 승인 근거: 사용자 권장안 승인
- 상위 책임:
  - `docs/design/APPROVED_CORE_V2_INTEGRATED_DECISION_LEDGER_2026-07-25.md`
  - `docs/design/APPROVED_ROULETTE_CORE_RULES.md`
  - `docs/design/APPROVED_MAPRUN_STAGE_WAVE_AND_MIDPOINT_CORE_V1.md`
  - `docs/design/APPROVED_V2_TRANSACTION_FOUNDATION_SEQUENCE_2026-07-26.md`

이 문서는 일반 `TACTICAL_PLANNING`에서 미확정 `SpinSession`과 `[전투 재개]`가 동시에 존재할 때의 게이트, 예약 보존, 확정 뒤 재검증과 금지 동작을 소유한다.

## 1. 승인된 핵심 결정

```text
TACTICAL_RESUME_WITH_OPEN_SPIN_SESSION: BLOCKED
RESUME_COMMAND_REQUIRES_CLOSED_SPIN_SESSION: YES
SPIN_SESSION_AUTO_CONFIRM_ON_RESUME: FORBIDDEN
SPIN_SESSION_AUTO_CANCEL_ON_RESUME: FORBIDDEN
PLANNING_RESERVATIONS_WHILE_BLOCKED: PRESERVED_UNAPPLIED
RESUME_ATTEMPT_STATE_MUTATION: ZERO
POST_SPIN_CLOSE_REVALIDATION: REQUIRED
POST_CLOSE_REVALIDATION_FAILURE_POLICY: REVIEW_PENDING
```

일반 전술계획에서 `SpinSession.state == OPEN`이면 `[전투 재개]`를 실행할 수 없다.

```text
SpinSession OPEN
→ [전투 재개] 비활성 또는 명시적 BLOCKED 응답
→ 기존 예약 큐 보존
→ 예약 비용 차감 0
→ 예약 명령 적용 0
→ 룰렛 이동·preview·[확정] 처리
→ SpinSession CLOSED
→ 기존 예약 큐 전체 재검증
→ 재검증 결과를 표시한 뒤 재개 가능 여부 판정
```

## 2. 기존 SpinSession 권한 유지

통합 결정 원장의 미확정 세션 규칙은 유지한다.

허용:

- 전장 관찰.
- 상점 열람과 허용된 이동 아이템 구매.
- 보유 또는 럭키 무료 이동 사용.
- 이동 뒤 보상 preview.
- 세션 UI 닫기와 다시 열기.
- 명시적 `[확정]`.

금지:

- 새 룰렛 회전.
- 건설·업그레이드·철거의 실제 실행.
- `[전투 재개]`를 통한 예약 큐 커밋.
- `[전투 재개]`를 우회한 simulation 재개.

이번 결정은 미확정 세션 중 허용되는 새 계획 명령 범위를 확장하지 않는다.

## 3. 재개 요청의 무변경 실패

`SpinSession`이 열려 있을 때의 재개 요청은 순수한 게이트 검사로 종료한다.

```text
ResumeGateResult.status = SPIN_SESSION_OPEN
state mutation = 0
```

변경해서는 안 되는 상태:

- `SpinSnapshot`.
- 현재 릴 배열과 이동 결과.
- 럭키 무료 이동과 실패 카운터.
- `BlankMoveCounter`와 `PendingMoveReward`.
- 회전 비용과 글로벌 금화.
- PendingReward.
- 계획 예약 큐.
- 예약 자원과 식량.
- 건물·업그레이드·철거 상태.
- 전장 유닛과 simulation clock.

재개 버튼을 반복 클릭해도 같은 차단 결과만 반환하며 추가 로그·비용·상태 전이를 만들지 않는다.

## 4. 자동 확정·자동 취소 금지

`[전투 재개]`는 룰렛 세션의 의사결정을 대신하지 않는다.

금지:

- 현재 보드를 자동 `[확정]`.
- 럭키 무료 이동을 자동 소비 또는 소멸.
- 미사용 이동 기회를 포기한 것으로 간주.
- SpinSession 취소와 회전 비용 환불.
- snapshot 폐기와 live 릴 복원.
- 무보상·보상·카운터를 임의 최종화.

세션은 오직 승인된 명시적 `[확정]` 거래가 성공했을 때 닫힌다. 확정 거래가 실패하면 세션은 열린 상태로 유지되고 재개 게이트도 계속 닫혀 있다.

이미 완료된 동일 `confirm_transaction_id`를 재요청한 경우 기존 `ConfirmReceipt`를 반환하며, receipt가 세션 종료를 증명할 때만 닫힌 상태로 취급한다.

## 5. 계획 예약 큐 보존

재개가 차단돼도 기존 계획 예약은 삭제하거나 적용하지 않는다.

보존 대상:

```text
planning_session_id
reservation_id
reservation_sequence
command_type
owner/building/unit/skill identifiers
target lane or anchor
quoted cost and food
validation basis revision
legendary conflict consent basis
```

보존은 성공을 보장하지 않는다. 예약 당시의 비용·건물·식량·전장 조건은 룰렛 확정 뒤 stale일 수 있다.

`SpinSession`이 열린 동안 예약 큐를 자동 취소하거나 자동 커밋하는 것은 금지한다.

## 6. SpinSession 종료 뒤 전체 재검증

성공한 `[확정]`은 금화, PendingReward, 럭키·무보상 카운터와 세션 상태를 원자적으로 최종화한다. 그 후 전술계획 예약 큐를 authoritative 현재 상태로 다시 검증한다.

재검증 입력:

- 최신 글로벌 금화와 실제 확정 비용·금화 보상.
- 최신 PendingReward와 보관 상태.
- 최신 식량 사용량·상한·예약 가능량.
- 최신 건물 존재·소유·blocked·Tier·업그레이드 상태.
- 최신 TokenSource와 live 릴 상태.
- 최신 전장 유닛·생존 전설 index·라인 조건.
- 최신 스킬 비용·쿨다운·대상 조건.
- 예약 순서와 동의 basis revision.

재검증은 기존 예약의 quoted result를 신뢰하지 않고 현재 authoritative 상태에서 `PlanningCommitPlan`을 새로 계산한다.

## 7. 재검증과 재개의 분리

`SpinSession` 종료 자체가 예약 명령을 즉시 적용하거나 전투를 자동 재개하지 않는다.

```text
ConfirmReceipt 성공
→ SpinSession CLOSED
→ PlanningRevalidationReport 생성
→ UI에 변경·실패 사유 표시
→ 사용자의 [전투 재개] 입력 대기
```

따라서 룰렛 확정 직후에도 플레이어는 재검증 결과를 확인할 수 있다.

재개 버튼의 활성 조건은 최소 다음을 만족해야 한다.

```text
SpinSession CLOSED
AND planning revalidation completed
AND no unresolved mandatory consent
AND selected failure policy permits commit
```

재검증 실패 예약을 유지·취소할지, 전체 batch를 차단할지는 별도 검수 결정으로 남긴다. 해당 정책이 확정되기 전에는 일부 예약을 숨겨서 적용하거나 조용히 삭제해서는 안 된다.

## 8. snapshot과 TokenSource 일관성

SpinSnapshot은 정지 시점 데이터의 불변 복사이므로 기존 계획 예약이 가리키는 건설·업그레이드가 대기 중이어도 변경되지 않는다.

```text
열린 SpinSession
→ 예약 TokenSource 건설/업그레이드 미적용
→ snapshot 불변
→ [확정]
→ 세션 close
→ 예약 재검증
→ 이후 승인된 planning commit에서만 live 건물·릴 변경
```

확정 보상은 live 건물이나 예약 결과를 다시 읽지 않고 snapshot과 최종 세션 보드에서 생성한다.

## 9. 위험 전투와의 구분

이 게이트는 일반 `TACTICAL_PLANNING`에 적용한다.

위험 전투는 전술계획 정지가 없고 룰렛 처리 중에도 simulation이 진행되므로 `[전투 재개]` 게이트가 존재하지 않는다. 위험 전투의 즉시 명령 순서와 전설 배치 명령 계약은 별도 승인 문서를 따른다.

일반 전투를 미확정 SpinSession 상태로 재개해 위험 전투처럼 동작시키는 것은 금지한다.

## 10. UI 계약

`SpinSession`이 열려 있으면 `[전투 재개]`는 비활성화하거나 클릭 시 다음 의미의 명확한 사유를 표시한다.

```text
룰렛 결과를 먼저 확정해야 전투를 재개할 수 있습니다.
현재 계획 예약은 유지되며, 룰렛 확정 후 최신 상태로 다시 검증됩니다.
```

금지되는 표현:

- 재개 버튼이 자동 확정을 수행하는 것처럼 보이는 표현.
- 예약이 이미 적용됐다고 오인시키는 자원 차감 표시.
- 세션을 닫기만 하면 확정된 것으로 표시.
- 재검증 실패 예약을 이유 없이 사라지게 하는 UI.

## 11. 자동 검증 계약

최소 다음 사례를 검증한다.

1. 열린 SpinSession에서 재개 요청 → `SPIN_SESSION_OPEN`, 상태 변경 0.
2. 재개 반복 클릭 → 금화·이동·예약·로그 중복 변경 0.
3. 재개 요청이 자동 확정하지 않음.
4. 재개 요청이 자동 취소·환불하지 않음.
5. 확정 실패 → 세션 OPEN 유지, 재개 계속 차단.
6. 확정 성공 → 세션 CLOSED, 예약은 미적용 상태로 보존.
7. 확정 금화 보상 뒤 예약 비용 재검증.
8. 확정 PendingReward 뒤 식량·전설 배치 예약 재검증.
9. 예약 TokenSource 건설이 열린 snapshot에 반영되지 않음.
10. 재검증 완료 전 전투 simulation이 재개되지 않음.
11. 재검증 보고 뒤에도 명시적 `[전투 재개]` 전까지 예약 적용 0.
12. 동일 confirm transaction 재요청 → 보상 중복 0, 게이트 결과 동일.

## 12. 현재 상태

```text
SPIN_SESSION_TACTICAL_RESUME_GATE: APPROVED
POST_CLOSE_REVALIDATION: REQUIRED
POST_CLOSE_REVALIDATION_FAILURE_POLICY: REVIEW_PENDING
PRODUCT_CODE_AUTHORIZED: NO
V2_IMPLEMENTATION: NOT_STARTED
HUMAN_QA: NOT_RUN
CORE_LOCK_V2: PENDING
```
