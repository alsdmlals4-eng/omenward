# V2 SpinSession 전술계획 재개 게이트 적대적 검수

- 작성일: 2026-07-26
- 상태: `REVIEW_DECISION_RECORDED / PRODUCT_CODE_NOT_AUTHORIZED`
- 대상 Issue: `#69`
- 승인 문서: `docs/design/APPROVED_V2_SPIN_SESSION_TACTICAL_RESUME_GATE_2026-07-26.md`
- 상위 계약:
  - `docs/design/APPROVED_CORE_V2_INTEGRATED_DECISION_LEDGER_2026-07-25.md`
  - `docs/design/APPROVED_MAPRUN_STAGE_WAVE_AND_MIDPOINT_CORE_V1.md`
  - `docs/design/APPROVED_V2_TRANSACTION_FOUNDATION_SEQUENCE_2026-07-26.md`

## F-14 — 열린 SpinSession과 `[전투 재개]`

### 공격 시나리오

일반 `TACTICAL_PLANNING`에 건설·업그레이드·병력 배치·스킬 예약이 존재하고, 룰렛은 정지 후 미확정 `SpinSession` 상태다.

이때 `[전투 재개]`가 허용되면 다음 거래가 겹친다.

```text
계획 예약 검증·비용 차감·적용
+
전투 simulation 재개
+
SpinSession 미확정 유지
```

예약된 TokenSource 건설·업그레이드, 금화·식량 소비와 전장 배치가 열린 snapshot 및 룰렛 확정 결과의 설명 가능성을 훼손할 수 있다.

### 검토한 선택지

#### A. SpinSession 종료 전 재개 차단 — 승인

```text
SpinSession OPEN
→ [전투 재개] BLOCKED
→ 예약 큐 보존·미적용
→ 명시적 [확정]
→ SpinSession CLOSED
→ 최신 authoritative 상태로 전체 예약 재검증
→ 재개 가능 여부 표시
```

장점:

- 룰렛 확정과 계획 커밋의 거래 순서가 명확하다.
- snapshot은 예약 건물 변경으로 오염되지 않는다.
- 전투가 재개된 뒤 미확정 룰렛 UI가 남지 않는다.
- 자동 확정·자동 취소 없이 플레이어 의사결정을 보존한다.
- 예약 비용은 룰렛 확정 결과를 반영해 다시 계산할 수 있다.

#### B. 전투를 재개하고 SpinSession 유지 — 기각

일반 전투가 위험 전투처럼 바뀌며, 계획 커밋 뒤 과거 snapshot을 확정하는 이중 시간축이 생긴다.

#### C. 재개 시 자동 확정 — 기각

이동 기회, preview와 명시적 `[확정]` 계약을 침해한다.

#### D. 재개 시 자동 취소 — 기각

이미 지불한 비용과 영구 이동 결과의 복구 의미가 정의되지 않는다.

## 승인된 판정

```text
TACTICAL_RESUME_WITH_OPEN_SPIN_SESSION: BLOCKED
RESUME_COMMAND_REQUIRES_CLOSED_SPIN_SESSION: YES
SPIN_SESSION_AUTO_CONFIRM_ON_RESUME: FORBIDDEN
SPIN_SESSION_AUTO_CANCEL_ON_RESUME: FORBIDDEN
PLANNING_RESERVATIONS_WHILE_BLOCKED: PRESERVED_UNAPPLIED
RESUME_ATTEMPT_STATE_MUTATION: ZERO
POST_SPIN_CLOSE_REVALIDATION: REQUIRED
```

## 보존해야 할 인과

1. 룰렛 `[확정]`이 성공해야 SpinSession이 닫힌다.
2. 닫힌 뒤에도 예약은 즉시 적용되지 않는다.
3. 최신 금화·PendingReward·식량·건물·전장 상태로 재검증한다.
4. 재검증 결과를 플레이어에게 표시한다.
5. 별도의 `[전투 재개]` 입력이 계획 커밋과 simulation 재개를 촉발한다.

## 금지 상태

- 재개 클릭으로 룰렛 자동 확정.
- 재개 클릭으로 세션 자동 취소 또는 비용 환불.
- 열린 세션 중 예약 비용 차감.
- 세션 종료만으로 예약 자동 적용.
- 재검증 완료 전에 simulation 재개.
- stale 예약을 그대로 커밋.
- 재검증 실패 예약을 조용히 삭제하거나 일부만 숨겨서 적용.

## 범위 보호

```text
R1_PLUS_R2_SCOPE: UNCHANGED
PRODUCT_CODE_AUTHORIZED: NO
V2_IMPLEMENTATION: NOT_STARTED
FINAL_CODEX_HANDOFF: BLOCKED
```

이번 결정은 일반 전술계획의 재개 게이트만 소유한다.

변경하지 않는 항목:

- 위험 전투의 실시간 SpinSession 동작.
- 룰렛 snapshot·이동·확정 계산.
- 계획 예약 명령 자체의 비용·순서.
- 전설 배치 제한과 위험 전투 command ordering.

## 다음 검수 분리

SpinSession 확정 뒤 전체 재검증에서 하나 이상의 예약이 실패할 때의 처리 정책은 아직 확정하지 않았다.

```text
POST_CLOSE_REVALIDATION_FAILURE_POLICY: REVIEW_PENDING
```

후속 검수에서 다음을 비교해야 한다.

- 전체 planning commit 차단 후 사용자가 수정.
- 실패 예약만 비활성화하고 유효 예약 적용.
- 실패 예약 자동 취소.

자동 취소 또는 부분 적용을 이번 결정에 암묵적으로 포함하지 않는다.
