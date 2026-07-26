# V2 위험 전투 tick 전설 배치 순서 적대적 검수

- 검수일: 2026-07-26
- 상태: `REVIEW_DECISION_APPROVED / DOCUMENTATION_ONLY`
- 관련 Issue: `#69`
- 제품 코드 승인: `NO`
- 최종 Codex 인계: `NO`
- 승인 문서: `docs/design/APPROVED_V2_DANGER_TICK_LEGENDARY_DEPLOYMENT_ORDER_2026-07-26.md`
- 부모 계약: `docs/design/APPROVED_V2_LEGENDARY_DEPLOYMENT_LIMIT_2026-07-26.md`

## F-12 — 위험 전투 동일 tick의 사망·배치 경쟁 상태

### 공격 시나리오

```text
기존 전설 A가 치명 피해를 받음
+
플레이어가 새 전설 B 배치를 클릭함
+
피해·사망 signal과 UI input callback이 같은 렌더 프레임에 실행됨
```

순서를 고정하지 않으면 같은 seed와 같은 플레이어 입력에서도 다음 결과가 모두 가능하다.

```text
입력 callback 우선
→ A 생존으로 조회
→ B 영웅 2기 변환
→ 직후 A 사망
```

```text
사망 signal 우선
→ A 사망으로 조회
→ B 전설 1기 배치
```

### 위험도

- 결정론·replay 불일치.
- FPS·플랫폼·signal 연결 순서에 따른 결과 차이.
- 전설 PendingReward의 무동의 강등 가능성.
- 식량 반환과 배치 비용의 부분 상태.
- 동일 입력 로그의 인과 보고 불일치.

### 사용자 승인 결정

권장 A안을 승인했다.

```text
전투 피해·사망 authoritative 정산
→ 식량 반환·제거 완료
→ 생존 전설 index revision 생성
→ player deployment command 검증
→ 원자 배치 commit
→ receipt·인과 로그
→ 새 spawn은 다음 tick부터 행동
```

### 검수 보정

1. UI 입력은 직접 spawn하지 않고 안정적 `command_sequence`로 enqueue한다.
2. fixed tick의 combat settlement 뒤 `command_cutoff_sequence`를 캡처한다.
3. cutoff 이후 입력은 다음 tick으로 넘긴다.
4. wall-clock timestamp와 렌더 callback 순서는 판정 근거가 아니다.
5. 배치 transaction은 하나의 `AliveLegendaryIndexRevision`만 읽는다.
6. 사망 애니메이션과 authoritative `is_alive`를 분리한다.
7. 같은 tick에 사망이 정산됐으면 새 보상은 전설 1기로 배치한다.
8. 사망이 아직 정산되지 않았으면 기존 전설은 생존으로 본다.
9. 유효한 변환 동의가 없으면 자동 강등하지 않고 `CONSENT_REQUIRED`로 무변경 종료한다.
10. 새 spawn은 같은 tick의 공격·피해 단계에 재진입하지 않는다.

### 범위 보호

- 일반 전술계획 복수 예약 순서는 PR #74 계약을 유지한다.
- 위험 전투의 건설·스킬 즉시 실행 규칙은 변경하지 않는다.
- R1+R2 범위는 변경하지 않는다.
- 제품 코드·Scene·Resource·데이터는 변경하지 않는다.
- 한 commit phase에 새 전설 배치 명령이 둘 이상일 때의 우선순위는 다음 별도 결정으로 남긴다.

### 판정

```text
F-12: REMEDIATED_IN_APPROVED_DOCUMENTATION
DETERMINISTIC_TICK_ORDER: APPROVED
PRODUCT_CODE_AUTHORIZED: NO
FINAL_CODEX_HANDOFF: BLOCKED_UNTIL_EXACT_REVIEW_COMPLETE_COMMAND
```
