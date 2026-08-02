# 오멘워드 영웅 해금·병종 등록 승인 계약

```yaml
decision_id: OMW-DEC-20260802-GAMEPLAY-HERO-UNLOCK-REGISTRATION-V1
approved_at: 2026-08-02 15:58 KST
approval: USER_DIRECT_APPROVAL
status: USER_APPROVED_STRUCTURE / BATTLEFIELD_ACTIVATION_PENDING / NOT_IMPLEMENTED
work_mode: TOTAL_PLANNING
product_code_authority: NONE
simulation: NOT_RUN
runtime: NOT_RUN
human_validation: NOT_RUN
```

## 1. 결정 요약

영웅은 자유 편성 캐릭터 풀이 아니라 **기존 병종에 고정 대응하는 영웅**이다. 플레이어는 주점의 공개 노드에서 해당 영웅을 영구 해금한 뒤, 런 시작 전에 대응 병종에 등록해야 그 영웅을 사용할 수 있다.

```text
UNIT_ARCHETYPE
→ FIXED_ASSOCIATED_HERO
→ PERMANENT_UNLOCK
→ PRE_RUN_REGISTRATION
→ REGISTERED_HERO_ELIGIBLE_FOR_USE
```

## 2. 병종별 고정 연결

- 각 영웅은 하나의 기존 `UnitArchetype`에 고정 연결된다.
- 한 영웅을 다른 병종에 자유 배속하지 않는다.
- 영웅의 역할과 능력은 대응 병종의 정체성을 확장해야 한다.
- 영웅은 대응 병종을 삭제하거나 단순 상위 등급으로 교체하지 않는다.
- 정확한 병종별 영웅 명단과 이름·능력은 후속 콘텐츠 승인 대상이다.

## 3. 해금

- 영웅은 주점의 유한하고 공개된 노드에서 정산 영구재화로 해금한다.
- 후보·비용·선행 조건·연결 병종을 구매 전에 표시한다.
- 해금은 영구 Profile 소유권을 부여한다.
- 랜덤 뽑기·유료 재굴림·중복 합성·확률 승급은 사용하지 않는다.
- 영웅을 해금하지 않아도 대응 기본 병종과 전체 콘텐츠는 사용할 수 있어야 한다.

## 4. 등록

- 해금만으로 모든 런에 자동 적용되지 않는다.
- 런 시작 전 편성 단계에서 해금된 영웅을 대응 병종에 등록한다.
- 등록되지 않은 영웅은 해당 런에서 등장·발동·보정되지 않는다.
- 등록 상태는 런 시작 시 `RunLoadoutSnapshot`에 고정한다.
- 런 도중 영웅 등록 변경·교체·해제는 허용하지 않는다.
- 동시에 등록 가능한 영웅 수와 슬롯 수는 별도 승인 전 미확정이다.

## 5. 등록의 의미와 금지선

```text
REGISTRATION
= 해당 영웅의 런 사용 자격 활성화
!= 즉시 전장 배치
!= 자동 승리 보정
!= 전체 병종 영구 능력치 배율
!= 릴 확률 조작
```

등록은 사용 가능 상태만 만든다. 전장에서 영웅이 실제로 등장하는 조건과 방식은 다음 Decision에서 확정한다.

금지:

- 해금만으로 모든 런에 자동 장착.
- 다른 병종 영웅을 임의로 교차 등록.
- 영웅 등록으로 대응 병종 토큰의 숨은 당첨 확률 상승.
- 미등록 영웅의 패시브·전투 효과 잔존.
- 영웅이 없는 기본 병종을 의도적으로 불완전하게 설계.

## 6. 저장 책임

```yaml
HeroProfileState:
  unlocked_hero_ids
  hero_unit_archetype_bindings
  registered_hero_by_unit_archetype

RunLoadoutSnapshot:
  registered_hero_ids
  hero_unit_archetype_bindings
```

- `hero_id`, `unit_archetype_id`, `unlock_node_id`는 안정 식별자를 사용한다.
- 등록 시 잠금 상태·병종 불일치·중복 슬롯을 검증한다.
- Profile 저장과 런 스냅샷을 분리해 런 중 Profile 변경이 현재 런에 소급되지 않게 한다.

## 7. 적대적 검토

| 공격 | 판정 | 보완 |
|---|---|---|
| 영웅이 자유 편성되어 병종 정체성을 무너뜨린다 | 유효 | 영웅-병종 고정 바인딩 |
| 해금만 하면 모든 영웅 효과가 자동 누적된다 | 유효 | 명시적 런 전 등록과 슬롯 상한 |
| 영웅이 기본 병종의 필수 완성 부품이 된다 | 유효 | 미해금 기본 병종·기본 Profile 완주 보장 |
| 등록이 숨은 릴 확률 버프로 변한다 | 유효 | 등록은 사용 자격만 부여, odds 변경 금지 |
| 영웅 명단 증가가 조합 복잡도를 폭증시킨다 | 유효 | 기존 병종별 고정 연결·유한 노드·정확 명단 후속 승인 |
| 사용 가능의 의미가 모호하다 | 유효 | 전장 발동 방식은 다음 독립 Decision으로 분리 |

## 8. 미확정 항목

- 동시에 등록 가능한 영웅 수.
- 병종당 영웅 후보가 영구적으로 1명인지, 후속 확장에서 복수 후보를 허용할지.
- 등록 영웅이 전장에서 등장하는 조건과 표현.
- 영웅 능력·등급·정확 명단·수치.
- 등록 UI와 프리셋·교체 확인 절차.

## 9. 다음 Gate

```text
OMW-DEC-20260802-GAMEPLAY-HERO-BATTLEFIELD-ACTIVATION-V1
= 등록된 병종 영웅이 해당 병종의 룰렛 결과·배치와 어떤 방식으로 연결되어 전장에 등장하는가
```

## 10. 상태 경계

```text
DESIGN: USER_APPROVED_UNLOCK_AND_REGISTRATION
BATTLEFIELD_ACTIVATION: PENDING
EXACT_VALUES: PENDING
SIMULATION: NOT_RUN
RUNTIME: NOT_RUN
HUMAN_QA: NOT_RUN
PRODUCT_CODE: UNCHANGED
```
