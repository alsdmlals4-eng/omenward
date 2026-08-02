# 오멘워드 영웅 등급 토큰 변환·배치 승인 계약

```yaml
decision_id: OMW-DEC-20260802-GAMEPLAY-HERO-BATTLEFIELD-ACTIVATION-V1
approved_at: 2026-08-02 16:11 KST
approval: USER_DIRECT_APPROVAL
status: USER_APPROVED_STRUCTURE / UNIQUENESS_AND_VALUES_PENDING / NOT_IMPLEMENTED
work_mode: TOTAL_PLANNING
product_code_authority: NONE
simulation: NOT_RUN
runtime: NOT_RUN
human_validation: NOT_RUN
```

## 1. 결정 요약

룰렛은 이름이 정해진 영웅을 직접 뽑지 않는다. 룰렛에서 특정 병종의 `[영웅] 등급 토큰`이 나오면 먼저 보관함에 들어간다. 플레이어는 보관함에서 해당 토큰을 선택하고, 같은 병종에 연결된 해금 영웅 중 하나로 변경하여 배치할지 결정한다.

```text
룰렛 결과
→ [영웅] 등급 + UnitArchetype 토큰
→ 보관함
→ 원본 영웅 등급 병종 유지 또는 해금된 동병종 영웅으로 변경
→ 상·중·하 한 전선에 비가역 배치
```

## 2. 영웅 해금·명부 정정

- 각 영웅은 하나의 기존 `UnitArchetype`에 고정 연결된다.
- 하나의 병종에 서로 다른 해금 영웅이 여러 명 존재할 수 있다.
- 영웅 해금 시 Profile 영웅 명부에 영구 등록된다.
- 별도의 런 시작 전 영웅 등록·계약 단계는 요구하지 않는다.
- 이전 문서의 `pre-run registration` 해석은 이 결정으로 대체한다.
- 해금되지 않은 영웅은 변환 후보에 나타나지 않는다.

## 3. 보관함 변환 절차

영웅 변환 UI는 다음 조건을 모두 만족할 때만 활성화된다.

```text
token.grade == HERO
AND token.unit_archetype_id == hero.unit_archetype_id
AND hero.id IN unlocked_hero_ids
```

플레이어 선택:

1. 원본 `[영웅] 등급 병종 토큰`을 그대로 유지한다.
2. 같은 병종의 해금 영웅 목록을 열어 한 명을 선택한다.
3. 변환 결과와 전선 배치 영향을 미리 확인한다.
4. 상·중·하 중 한 전선을 선택하고 확정한다.

확정 전에는 취소하거나 다른 동병종 영웅을 선택할 수 있다. 확정 뒤에는 토큰 변환과 전선 배치를 되돌리지 않는다.

## 4. 수량·인과 불변식

```text
ONE_HERO_GRADE_TOKEN
→ ONE_DEPLOYED_UNIT
```

- 영웅 변환은 추가 유닛을 생성하지 않는다.
- 원본 토큰 하나를 선택 영웅 하나로 치환한다.
- 영웅으로 변경하지 않으면 원본 영웅 등급 병종을 배치할 수 있다.
- 일치하는 해금 영웅이 없어도 원본 토큰은 정상적으로 사용 가능하다.
- 변환은 다른 보관 토큰·과거 SpinSnapshot·릴 구조·당첨 확률을 변경하지 않는다.
- 전선 배치는 기존 PendingReward의 한 전선 비가역 커밋 규칙을 따른다.

## 5. 복수 동병종 영웅

- 한 병종에 여러 영웅을 해금할 수 있다.
- 보관함의 영웅 선택 목록에는 해당 토큰과 병종이 일치하는 모든 해금 영웅을 표시한다.
- 각 영웅은 단순 수치 상위호환이 아니라 다른 역할·조건·약점을 제공해야 한다.
- 같은 이름의 영웅을 한 런에 여러 번 배치할 수 있는지, 서로 다른 동병종 영웅을 몇 명까지 활성화할 수 있는지는 다음 Decision에서 확정한다.

## 6. UX·데이터 책임

```yaml
HeroProfileState:
  unlocked_hero_ids
  hero_unit_archetype_bindings

StoredRewardToken:
  token_instance_id
  unit_archetype_id
  grade
  conversion_state
  selected_hero_id

HeroConversionPreview:
  source_token_instance_id
  candidate_hero_ids
  selected_hero_id
  target_lane_id
```

- 후보에는 이름·초상·연결 병종·핵심 역할·변환 후 변화·현재 사용 가능 여부를 표시한다.
- 해금되지 않은 영웅은 잠금 이유를 보여 줄 수 있지만 선택할 수 없다.
- 병종 불일치 영웅은 후보에 포함하지 않는다.
- 확정 시 원본 token instance와 선택 영웅 ID, 대상 전선을 한 transaction으로 기록한다.
- 중복 확정·부분 저장·원본 토큰 잔존을 허용하지 않는다.

## 7. 적대적 검토

| 공격 | 판정 | 보완 |
|---|---|---|
| 영웅 해금이 릴 확률을 직접 높인다 | 유효 | 룰렛은 익명 영웅 등급 병종 토큰만 생성, 해금은 보관함 변환 후보만 추가 |
| 영웅 변경으로 병력이 하나 더 생긴다 | 유효 | 1토큰→1유닛 치환 불변식 |
| 같은 병종 영웅이 여러 명이면 자유 직업 변경처럼 변한다 | 유효 | 모든 후보는 동일 UnitArchetype 고정 바인딩 |
| 강한 영웅 하나가 모든 선택을 지배한다 | 유효 | 역할·조건·약점 기반 sidegrade, 수치·사용률 simulation 필요 |
| 보관함 선택이 복잡해진다 | 유효 | 영웅 등급 토큰에서만 목록 노출, 동병종 후보만 필터링 |
| 영웅 미해금 플레이가 손해만 보는 미완성판이 된다 | 유효 | 원본 영웅 등급 토큰 사용 가능·기본 Profile 완주 유지 |
| 같은 영웅을 무한 복제한다 | 유효 | 동일 영웅 중복 배치 규칙을 다음 Gate로 분리 |

## 8. 미확정 항목

- 동일 영웅의 한 런 중복 배치 허용 여부.
- 서로 다른 동병종 영웅의 동시 활성 상한.
- 원본 `[영웅] 등급 병종 토큰`의 정확한 능력 계약.
- 영웅별 능력·등급·명단·수치.
- 변환 UI의 정확한 화면 배치·키 입력.
- 영웅 사망·재출전·런 종료 처리.

## 9. 다음 Gate

```text
OMW-DEC-20260802-GAMEPLAY-HERO-UNIQUENESS-AND-ACTIVE-LIMIT-V1
= 영웅 등급 토큰이 여러 번 나왔을 때 같은 영웅과 동병종 영웅을 한 런에 몇 번 배치할 수 있는가
```

## 10. 상태 경계

```text
DESIGN: USER_APPROVED_TOKEN_CONVERSION_AND_DEPLOYMENT
PRE_RUN_HERO_REGISTRATION: SUPERSEDED
EXACT_VALUES: PENDING
SIMULATION: NOT_RUN
RUNTIME: NOT_RUN
HUMAN_QA: NOT_RUN
PRODUCT_CODE: UNCHANGED
```
