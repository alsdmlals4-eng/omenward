# 오멘워드 영웅 해금·병종 명부 등록 승인 계약

```yaml
decision_id: OMW-DEC-20260802-GAMEPLAY-HERO-UNLOCK-REGISTRATION-V1
approved_at: 2026-08-02 15:58 KST
corrected_at: 2026-08-02 16:11 KST
approval: USER_DIRECT_APPROVAL_WITH_LATER_CLARIFICATION
status: USER_APPROVED_STRUCTURE / PRE_RUN_REGISTRATION_SUPERSEDED / NOT_IMPLEMENTED
work_mode: TOTAL_PLANNING
product_code_authority: NONE
simulation: NOT_RUN
runtime: NOT_RUN
human_validation: NOT_RUN
```

## 1. 결정 요약

영웅은 기존 병종에 고정 대응한다. 플레이어는 주점의 공개 노드에서 영웅을 영구 해금하며, 해금된 영웅은 Profile 영웅 명부에 등록된다.

```text
기존 UnitArchetype
→ 해당 병종에 연결된 영웅 후보 1명 이상
→ 주점에서 영구 해금
→ Profile 영웅 명부 등록
→ 동병종 [영웅] 등급 토큰의 보관함 변환 후보로 사용
```

이 문서의 초기 `런 시작 전 등록` 해석은 후속 사용자 설명으로 대체됐다. 별도의 pre-run hero loadout이나 계약은 요구하지 않는다.

## 2. 병종별 연결

- 각 영웅은 하나의 기존 `UnitArchetype`에 고정 연결된다.
- 하나의 병종에 서로 다른 영웅을 여러 명 해금할 수 있다.
- 한 영웅을 다른 병종에 자유 배속하지 않는다.
- 영웅의 역할은 대응 병종의 정체성을 확장해야 한다.
- 영웅은 대응 병종의 단순 수치 상위호환이 아니라 역할·조건·약점이 다른 선택지여야 한다.

## 3. 해금과 명부 등록

- 영웅은 주점의 유한하고 공개된 노드에서 정산 영구재화로 해금한다.
- 후보·비용·선행 조건·연결 병종을 구매 전에 표시한다.
- 해금은 영구 Profile 소유권과 영웅 명부 등록을 동시에 완료한다.
- 랜덤 뽑기·유료 재굴림·중복 합성·확률 승급은 사용하지 않는다.
- 영웅을 해금하지 않아도 대응 기본 병종과 원본 영웅 등급 토큰은 사용할 수 있어야 한다.

## 4. 사용 가능의 의미

```text
UNLOCKED_AND_ROSTERED_HERO
= 같은 UnitArchetype의 [영웅] 등급 보관 토큰을 변환할 때 선택 가능한 후보
!= 모든 런 자동 패시브
!= 런 시작 전 필수 편성
!= 즉시 전장 배치
!= 릴 확률 조작
```

전장 사용 절차는 `APPROVED_OMENWARD_HERO_TOKEN_CONVERSION_AND_DEPLOYMENT_2026-08-02.md`가 소유한다.

## 5. 저장 책임

```yaml
HeroProfileState:
  unlocked_hero_ids
  hero_unit_archetype_bindings
  unlocked_hero_ids_by_unit_archetype
```

- `hero_id`, `unit_archetype_id`, `unlock_node_id`는 안정 식별자를 사용한다.
- 하나의 병종에 복수 hero ID를 저장할 수 있다.
- 병종 불일치·중복 구매·부분 저장을 허용하지 않는다.
- Profile 변경은 이미 확정·배치된 현재 런의 token instance에 소급되지 않는다.

## 6. 적대적 검토

| 공격 | 판정 | 보완 |
|---|---|---|
| 영웅이 자유 편성되어 병종 정체성을 무너뜨린다 | 유효 | 영웅-병종 고정 바인딩 |
| 병종당 영웅 1명으로 콘텐츠 확장이 막힌다 | 유효 | 같은 병종 복수 해금 영웅 허용 |
| 해금만 하면 모든 영웅 효과가 자동 누적된다 | 유효 | 명부 등록은 보관함 변환 후보 자격만 제공 |
| 영웅이 기본 병종의 필수 완성 부품이 된다 | 유효 | 원본 영웅 등급 토큰과 기본 Profile 완주 보장 |
| pre-run 등록 화면이 불필요한 메뉴 단계를 만든다 | 유효 | 후속 승인으로 pre-run 등록 제거 |

## 7. 미확정 항목

- 병종별 영웅 명단·능력·등급·수치.
- 동일 영웅의 한 런 중복 배치 여부.
- 동병종 영웅의 동시 활성 상한.
- 주점 명부 UI·필터·비교 방식.

## 8. 상태 경계

```text
DESIGN: USER_APPROVED_UNLOCK_AND_ROSTER
PRE_RUN_REGISTRATION: SUPERSEDED
BATTLEFIELD_ACTIVATION: USER_APPROVED_IN_SEPARATE_AUTHORITY
EXACT_VALUES: PENDING
SIMULATION: NOT_RUN
RUNTIME: NOT_RUN
HUMAN_QA: NOT_RUN
PRODUCT_CODE: UNCHANGED
```
