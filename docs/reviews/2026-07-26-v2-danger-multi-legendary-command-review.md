# V2 위험 전투 복수 전설 명령 적대적 검수

- 작성일: 2026-07-26
- 상태: `REVIEW_DECISION_RECORDED / PRODUCT_CODE_NOT_AUTHORIZED`
- 대상 Issue: `#69`
- 상위 결정:
  - `docs/design/APPROVED_V2_LEGENDARY_DEPLOYMENT_LIMIT_2026-07-26.md`
  - `docs/design/APPROVED_V2_DANGER_TICK_LEGENDARY_DEPLOYMENT_ORDER_2026-07-26.md`
- 승인 문서: `docs/design/APPROVED_V2_DANGER_MULTI_LEGENDARY_COMMAND_ORDER_2026-07-26.md`

## F-13 — 같은 commit phase의 복수 신규 전설 명령

### 공격 시나리오

전투 정산 뒤 생존 전설이 0기이며 같은 cutoff에 다음 명령이 포함된다.

```text
command 101: 전설 A 배치
command 102: 전설 B 배치
```

두 명령이 같은 초기 snapshot을 병렬 검증하면 전설 2기가 모두 배치되어 `PLAYER_ALIVE_LEGENDARY_BATTLEFIELD_CAP: 1`을 위반할 수 있다.

### 검토한 선택지

#### A. command_sequence 순차 독립 원자 처리 — 승인

```text
command 101 검증·커밋
→ 성공 시 생존 전설 index 갱신
→ command 102를 새 revision으로 재검증
```

- 앞선 성공은 후속 실패 때문에 rollback하지 않는다.
- 후속 명령은 최신 충돌 근거에 유효한 동의가 없으면 `CONSENT_REQUIRED`.
- 앞선 명령이 무변경 실패하면 슬롯을 점유하지 않으며 다음 명령은 전설로 성공할 수 있다.

#### B. commit phase 전체 batch 원자 처리 — 기각

후속 명령의 동의 부족이나 자원 부족 때문에 이미 유효한 앞선 즉시 배치까지 취소된다. 위험 전투의 실시간 명령 의미와 맞지 않는다.

#### C. tick당 전설 명령 하나만 처리 — 기각

숨은 throttling과 불필요한 지연을 만들며 command log의 실제 순서를 설명하지 못한다.

### 승인 결과

```text
DANGER_MULTI_LEGENDARY_COMMAND_ORDER: COMMAND_SEQUENCE_SERIAL_COMMIT
COMMAND_ATOMICITY: PER_COMMAND
ALIVE_LEGENDARY_INDEX_REFRESH_AFTER_SUCCESS: REQUIRED
EARLIER_SUCCESS_ROLLBACK_ON_LATER_FAILURE: FORBIDDEN
FAILED_COMMAND_RESERVES_LEGENDARY_SLOT: NO
STALE_CONSENT_AUTO_DOWNGRADE: FORBIDDEN
```

### 결정론 보정

- 순서는 authoritative `command_sequence`만 사용한다.
- sequence 중복은 invariant violation이며 임의 tie-break를 금지한다.
- 각 성공 뒤 `AliveLegendaryIndexRevision`을 갱신한다.
- 후속 동의는 최신 revision과 `conflict_basis_hash`에 결합한다.
- wall-clock, 렌더 callback, UI 카드 위치는 우선순위 근거가 아니다.
- 새 spawn은 같은 phase의 후속 전설 판정에는 포함되지만 전투 행동은 다음 tick부터 시작한다.

### 실패·rollback 보정

앞선 명령 실패:

```text
상태 변경 0
→ 전설 슬롯 점유 0
→ 다음 명령은 동일 revision에서 독립 재검증
```

후속 명령 실패:

```text
후속 명령만 상태 변경 0
→ 앞선 성공 receipt 유지
```

commit phase 전체 rollback은 적용하지 않는다.

### 검증 요구

- 첫 성공 뒤 후속 `CONSENT_REQUIRED`.
- 최신 동의가 있는 후속 명령의 영웅 2기 원자 배치.
- 첫 실패 뒤 두 번째 전설 성공.
- stale 동의 자동 강등 금지.
- 후속 실패가 앞선 성공을 취소하지 않음.
- transaction 재요청 중복 spawn 0.
- sequence 중복 invariant 거부.
- frame rate와 무관한 receipt 순서.

## 범위 판정

```text
R1_R2_SCOPE: UNCHANGED
DANGER_CONSTRUCTION_AND_SKILL_RULES: UNCHANGED
PRODUCT_CODE_AUTHORIZED: NO
FINAL_CODEX_HANDOFF: BLOCKED_UNTIL_EXACT_REVIEW_COMPLETE_COMMAND
```

이번 결정은 후속 S1-C·L1·MapRun command queue 계약이다. 현재 R1+R2 구현 계획을 확장하지 않는다.

## 다음 적대적 검토 후보

`SpinSession`이 열린 상태에서 일반 `TACTICAL_PLANNING`의 `[전투 재개]`를 허용할지, 차단할지와 기존 예약 명령의 처리 순서를 별도로 결정해야 한다.
