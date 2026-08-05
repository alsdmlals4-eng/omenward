# [현행] 오멘워드 미확정 결정 목록

```yaml
updated_at: 2026-08-05
current_decision: OMW-DEC-20260805-PLANNING-STAGE-END-MERCHANT-V1
current_count: 6_OF_10
next_decision: OMW-DEC-20260805-PLANNING-FIRST-10-15-MINUTES-FLOW-V1
product_code_authority: NONE
```

시스템 연결 기준선은 `APPROVED_VERTICAL_SLICE_SYSTEM_CONTRACT_2026-07-27.md`다. 최신 6/10 기획은 제품에 구현되지 않았다.

## 확정된 6/10 범위

- Stage 1~19 종료 정비시간에 상인이 방문한다.
- Stage 20 종료 뒤에는 상인이 아니라 MapRun 최종 정산으로 이동한다.
- 상시 HUD 상점과 전투 중 재진입은 없다.
- 재고는 룰렛 제어·복구·성장 보조·가변 기회의 유한 4칸이다.
- 이동권 3개 미만에는 이동권, 3/3에는 다음 룰렛 1회 할인을 제시한다.
- 구매 통화는 골드 하나다.
- 상인은 병종·T3·Hero·Legendary·전술스킬·마력·건물 분기·Stage 정보를 직접 판매하지 않는다.
- 무한 구매·무한 reroll·할인 중첩을 금지한다.
- 정확 가격·재고 수·등장률·할인율은 시뮬레이션 전 확정하지 않는다.

책임 원본:

- `docs/design/APPROVED_OMENWARD_STAGE_END_MERCHANT_2026-08-05.md`
- `docs/reviews/ADVERSARIAL_STAGE_END_MERCHANT_ECONOMY_AND_INVENTORY_REVIEW_2026-08-05.md`

## 다음 7/10 — 첫 10~15분 흐름

확정해야 할 항목:

1. 첫 MapRun 시작부터 첫 Danger·Boss까지의 시간·선택 순서.
2. 건설·룰렛·배치·마력탑·전술 연구·상인의 첫 노출 시점.
3. 첫 실패가 이해 가능한 피드백으로 연결되는지.
4. 튜토리얼 강제와 자율성의 경계.
5. 첫 5 Stage에서 특정 병종·전술·상인 구매를 강제하지 않는지.
6. 사람 플레이 검증 시나리오와 Stop-ship 기준.

## 후속 미확정

- 8/10 Hero·Legendary 재조정.
- 9/10 Meta·Hub 재조정.
- 10/10 전체 Run 콘텐츠·UX·아트 종합 검토.
- 병종·전술·건물·상인의 정확 수치.
- 연구 취소 환불·마력 수급 가능 시간·제어 효과 감소 규칙.
- 상인 구매 거래 상태머신·재고 생성 알고리즘·저장 복구.

## 구현 차단

```text
PRODUCT_CODE = UNCHANGED
IMPLEMENTATION_READINESS = BLOCKED_BY_NUMERIC_AND_RUNTIME_PLAN
DATA_MIGRATION = NOT_AUTHORIZED
EXACT_NUMERICS = PENDING_SIMULATION
SIMULATION = NOT_RUN
HUMAN_QA = NOT_RUN
```

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
