# [현행] 오멘워드 로드맵

```yaml
updated_at: 2026-08-05
current_decision: OMW-DEC-20260805-PLANNING-STAGE-END-MERCHANT-V1
current_count: 6_OF_10
next_decision: OMW-DEC-20260805-PLANNING-FIRST-10-15-MINUTES-FLOW-V1
product_code_authority: NONE
```

## Planning Batch

```text
[완료 1/10] 핵심 재미·콘텐츠 가드레일
[완료 2/10] Stage·Wave·Danger·Boss 압력 매트릭스
[완료 3/10] 건물 6종 분기·카운터
[완료 4/10] 병종 역할·시너지·카운터
[완료 5/10] 전술스킬·마력
[현행 6/10] Stage 종료 상인
[다음 7/10] 첫 10~15분 흐름
[8/10] Hero·Legendary 재조정
[9/10] Meta·Hub 재조정
[10/10] 전체 Run 콘텐츠·UX·아트 종합 검토
```

## 6/10 Stage 종료 상인 결과

- Stage 1~19 종료 정비시간에만 상인이 방문한다.
- Stage 20 종료 뒤에는 상인이 아니라 MapRun 최종 정산으로 이동한다.
- 재고는 룰렛 제어·복구·성장 보조·가변 기회의 유한 4칸이다.
- 이동권이 3개 미만이면 이동권, 3/3이면 다음 룰렛 1회 할인을 제시한다.
- 구매 통화는 골드 하나다.
- 상인은 병종·T3·Hero·Legendary·전술스킬·마력·건물 분기를 직접 판매하지 않는다.
- 상시 HUD 상점·전투 중 재진입·무한 구매·무한 reroll·할인 중첩은 금지한다.
- 정확 가격·재고 수·등장률·할인율과 거래 상태머신은 후속 시뮬레이션·Codex 계획 대상이다.

## 7/10 첫 10~15분 목표

- Stage 1 시작부터 첫 Danger·Boss까지의 선택·시간 흐름.
- 건설·룰렛·배치·마력탑·전술 연구·상인의 첫 노출 순서.
- 첫 실패 원인과 다음 선택을 설명하는 피드백.
- 첫 5 Stage의 강제 정답·필수 구매·과도한 튜토리얼 방지.
- 사람 플레이 검증 시나리오와 Stop-ship 기준.

## 구현 순서

```text
6/10 Stage 종료 상인 정본
→ 7/10 첫 10~15분 흐름
→ Hero·Legendary / Meta·Hub 재조정
→ 전체 Run 종합 검토
→ 경제·수치 시뮬레이션
→ 별도 Codex 구현 계획
→ 제품 RED 테스트
→ 최소 구현
→ 런타임·사람 QA
```

제품 코드·Scene·Resource·게임 데이터·실제 아트 자산은 별도 승인 전 변경하지 않는다.

제품 구현: `NOT_STARTED`

## TDD 증거

- 6/10 RED: Validate Project Core Documentation run 986.
- 기존 55개 문서·CI·건물·병종·전술 계약은 통과하고 새 6/10 계약만 실패했다.
- GREEN/REFACTOR: final exact HEAD에서 fresh 검증 후 기록한다.

## Legacy 자동 검증 증거

기존 기술 기준선·C1·C2·C3 자동 증거 확보

C1 승인 룰렛 핵심 계약 원격 검증·병합 완료

상태: **REMOTE_PROVEN**

위 증거는 과거 계약 검증만 의미하며 최신 6/10 기획의 제품 구현을 의미하지 않는다.

## 완료 이력

```text
OMW-DEC-20260805-PLANNING-SIX-BUILDING-T2-T3-BRANCHES-AND-COUNTERS-V1
3_OF_10
OMW-DEC-20260805-PLANNING-TROOP-ROLES-SYNERGIES-AND-COUNTERS-V1
4_OF_10
OMW-DEC-20260805-PLANNING-TACTICAL-SKILLS-AND-MANA-V1
5_OF_10
LEGACY_C1_C2_C3_PROVEN
```
