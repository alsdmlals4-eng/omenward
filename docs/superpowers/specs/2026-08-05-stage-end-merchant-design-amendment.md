# OMENWARD Stage 종료 상인 Spec 보정

```yaml
decision_id: OMW-DEC-20260805-PLANNING-STAGE-END-MERCHANT-V1
status: DESIGN_SPEC_AMENDMENT / NOT_IMPLEMENTED
precedence: THIS_FILE_OVERRIDES_SLOT_A_IN_2026-08-05-STAGE-END-MERCHANT-DESIGN
```

## 룰렛 제어 슬롯 보정

기존 Spec의 `SLOT_A = GUARANTEED_MOVE_TICKET`은 이동권 보유 상한 3개에 도달한 경우 죽은 슬롯을 만들 수 있다. 다음 규칙으로 교정한다.

```text
SLOT_A = ROULETTE_CONTROL

보관 이동권 < 3
→ 보관형 이동권 1개 판매

보관 이동권 = 3
→ 다음 룰렛 1회 비용 할인으로 대체
```

- 매 방문 룰렛 제어 상품 하나는 보장한다.
- 이동권 상한을 초과하지 않는다.
- 할인은 한 번만 적용되고 중첩되지 않는다.
- 사용하지 않은 할인은 다음 Stage 시작 시 소멸한다.
- 이동권과 할인 중 무엇이 제시되는지 재고 생성 시점에 확정하고 구매 후 바꾸지 않는다.
- 최종 정본과 TDD 계약은 `GUARANTEED_MOVE_TICKET`이 아니라 `GUARANTEED_ROULETTE_CONTROL_SLOT`을 요구한다.
