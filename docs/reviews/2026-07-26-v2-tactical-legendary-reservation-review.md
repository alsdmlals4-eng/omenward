# 오멘워드 V2 전술계획 전설 예약 검수 기록

- 검수일: 2026-07-26
- 상태: `REVIEW_DECISION_APPROVED / V2_IMPLEMENTATION_NOT_STARTED`
- 대상: 일반 `TACTICAL_PLANNING`의 복수 전설 배치 예약
- 상위 정본: `docs/PROJECT_CORE.md`
- 부모 계약: `docs/design/APPROVED_V2_LEGENDARY_DEPLOYMENT_LIMIT_2026-07-26.md`
- 승인 보정: `docs/design/APPROVED_V2_TACTICAL_LEGENDARY_RESERVATION_ORDER_2026-07-26.md`
- 실제 구현 상태: `docs/CURRENT_IMPLEMENTATION_STATUS.md`
- 제품 코드 승인: `NO`

## F-11 — 복수 전설 예약의 동시 적용 충돌

### 발견

일반 전술계획에서는 배치 명령을 예약하고 `[전투 재개]` 때 비용을 일괄 차감한 뒤 동시에 적용한다. 실제 spawn 전 예약은 live 생존 전설 수에 포함되지 않으므로 현재 생존 전설이 0기일 때 전설 A와 B를 모두 전설로 예약할 수 있는 모호성이 있었다.

```text
생존 전설 0기
→ 전설 A 예약
→ 전설 B 예약
→ 동시 적용 시 생존 전설 2기 위험
```

### 사용자 결정

예약 순서 기반 가상 상태 검증 권장안을 승인했다.

### 확정된 보정

```text
최종 예약 순서 오름차순 평가
→ 첫 적격 전설 예약은 전설 1기
→ 이후 충돌 예약은 경고·명시적 동의 후 영웅 2기
→ 예약 수정 시 전체 큐 재평가
→ [전투 재개] 시 authoritative 상태로 전체 재검증
→ 전체 성공 또는 전체 무변경
```

- `reservation_sequence`가 전설 슬롯 우선순위를 소유한다.
- spawn 호출 순서나 UI 카드 위치는 우선순위가 아니다.
- 예약 삭제·재정렬로 충돌 근거가 바뀌면 이후 명령을 처음부터 다시 계산한다.
- 변환 동의는 `conflict_basis_hash`와 묶으며 stale 동의를 자동 적용하지 않는다.
- 새 충돌 또는 stale 동의가 있으면 비용·pending·전장 변경 없이 전술계획을 유지한다.
- 충돌이 사라지면 불필요한 영웅 변환 없이 전설 1기로 복원한다.
- 재개 batch의 일부 spawn 실패 시 비용·pending·spawn·로그를 전부 rollback한다.

### 패키지 책임

- `M1 / StageFlow`: planning session·revision·명령 순서·가상 재평가·재개 batch.
- `S1-C`: PendingReward·식량·변환 동의·원자 상태 전이.
- `U1-C`: 승인된 명령의 동일 세부 병종 영웅 payload 2개 조합.
- `L1 / Battle`: 실제 spawn과 `is_alive` authoritative 상태 제공.
- `X1`: 예상 결과·식량·경고·차단 이유 표시.

### 범위 판정

```text
R1_R2_SCOPE: UNCHANGED
PRODUCT_CODE_AUTHORIZED: NO
FINAL_CODEX_HANDOFF: BLOCKED_UNTIL_EXACT_REVIEW_COMPLETE_COMMAND
V2_IMPLEMENTATION: NOT_STARTED
HUMAN_QA: NOT_RUN
CORE_LOCK_V2: PENDING
```

이 결정은 R1+R2 구현 범위를 확장하지 않는다. 후속 M1·S1-C·U1-C·L1·X1 패키지의 계약 입력이다.
