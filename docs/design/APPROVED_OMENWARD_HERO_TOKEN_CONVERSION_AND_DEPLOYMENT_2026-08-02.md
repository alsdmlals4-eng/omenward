# 오멘워드 영웅 등급 토큰 변환·배치 승인 계약

```yaml
decision_id: OMW-DEC-20260802-GAMEPLAY-HERO-BATTLEFIELD-ACTIVATION-V1
approved_at: 2026-08-02 16:11 KST
refined_at: 2026-08-02 23:07 KST
status: USER_APPROVED / REFINED_BY_HIGH_GRADE_GLOBAL_SLOT / NOT_IMPLEMENTED
current_authority: OMW-DEC-20260802-GAMEPLAY-HERO-GRADE-SLOT-AND-UNLOCKED-SKILL-REPLACEMENT-V1
product_code_authority: NONE
simulation: NOT_RUN
runtime: NOT_RUN
human_validation: NOT_RUN
```

## 1. 영웅 등급 토큰과 해금 영웅 변환

룰렛은 이름 지정 영웅을 직접 뽑지 않는다.

```text
룰렛 [영웅] 등급 + UnitArchetype 토큰
→ 보관함
→ 표준 [영웅] 유닛 또는 해금된 동병종 이름 지정 [영웅] 선택
→ 전역 고등급 슬롯 검사
→ 상·중·하 한 전선에 비가역 배치
```

- 이름 지정 영웅은 토큰과 같은 `UnitArchetype`에 연결되어야 한다.
- 해금되지 않은 이름 지정 영웅은 후보에 나타나지 않는다.
- 변환은 `1토큰 → 1유닛`이며 추가 유닛을 만들지 않는다.
- 해금 영웅은 표준 2스킬 대신 고유 2스킬을 가진다.

## 2. 전역 고등급 슬롯

```text
ACTIVE_UNIT_COUNT_WHERE_GRADE_IN(HERO, LEGENDARY) <= 1
```

- 표준 영웅·해금 영웅·표준 전설·향후 해금 전설을 모두 합산한다.
- 슬롯이 차 있으면 표준 영웅으로의 배치도 허용하지 않는다.
- 과거 `이름 지정 영웅이 활성 중일 때 원본 영웅 등급 유닛 배치 가능` 문구는 폐기한다.
- 일반·엘리트는 슬롯에 포함하지 않는다.

## 3. 보관함 처리

```text
영웅 이상 토큰 획득
→ 슬롯 비어 있음: 합법 후보를 선택해 배치 가능
→ 슬롯 차 있음: 보관 또는 판매
```

- 슬롯 충돌로 토큰을 자동 소멸시키지 않는다.
- 현재 고등급 유닛을 자동 삭제하거나 새 토큰으로 강제 교체하지 않는다.
- 슬롯 상태·충돌 사유·보관·판매 선택을 UI에 표시한다.

## 4. 이름 지정 영웅 첫 출전 조건

```text
token.grade == HERO
AND token.unit_archetype_id == named_hero.unit_archetype_id
AND named_hero.id IN unlocked_named_hero_ids
AND active_high_grade_unit_instance_id == null
```

첫 출전에서는 위 조건을 만족하면 이름 지정 영웅으로 변환할 수 있다.

## 5. 이름 지정 영웅 사망 후 재출전

```text
active_high_grade_unit_instance_id == null
AND previous_named_hero.ended_reason == DEATH_OR_REMOVAL
AND token.grade == HERO
AND token.unit_archetype_id == named_hero.unit_archetype_id
AND token.created_sequence > previous_named_hero.ended_sequence
→ 같은 이름 지정 영웅 재출전 가능
```

- 사망 전에 보관한 영웅 등급 토큰은 이름 지정 영웅 재출전에 사용할 수 없다.
- 반복 출전마다 새 적격 토큰 1개를 소비한다.
- 이전 인스턴스의 HP·cooldown·상태·누적 효과를 승계하지 않는다.
- 표준 영웅·전설의 보관 토큰 후속 배치 세부는 기존 공통 보관 계약을 따르며 post-death provenance를 임의 확장하지 않는다.

## 6. 배치 원자성

```text
slot 검증
+ token provenance 검증
+ 표준/해금 후보 확정
+ token 소비
+ unit instance 생성
+ lane 비가역 배치
+ active high-grade slot 기록
= 하나의 transaction
```

- 중복 확정·부분 저장·토큰 잔존·동시 고등급 둘 생성을 허용하지 않는다.
- 확정 뒤 undo·회수·판매·재보관·전선 이동은 금지한다.

## 7. UX

영웅 등급 토큰 선택 화면은 다음을 표시한다.

- 등급·병종·출처 Tier.
- 표준 영웅의 표준 2스킬.
- 해금 이름 지정 영웅의 고유 2스킬.
- `표준 영웅 < 해금 영웅 < 표준 전설` 파워 계층.
- 전장 고등급 슬롯 `0/1` 또는 `1/1`.
- 슬롯 충돌 시 보관·판매만 가능하다는 설명.
- 이름 지정 영웅 사망 후 재출전 provenance 충족 여부.

과거 sidegrade 비교용 `명시적 약점·원본 선택 상황` 표시는 현행 필수 계약이 아니다. 해금 영웅은 의도된 수직 보상이다.

## 8. 향후 해금 전설

향후 해금 이름 지정 전설은 전설 등급 토큰 변환 후보가 되며 고유 3스킬을 사용한다.

```text
FUTURE_NAMED_LEGENDARY_UNIQUE_SKILL_SLOT = 3
FUTURE_NAMED_LEGENDARY_IMPLEMENTATION = NOT_NOW
```

현재 문서는 해금 전설 후보 UI·해금 조건·provenance·수치를 구현하지 않는다.

## 9. 데이터 방향

```yaml
StoredRewardToken:
  token_instance_id
  unit_archetype_id
  grade
  created_by_spin_id
  created_sequence
  conversion_state

HighGradeConversionPreview:
  source_token_instance_id
  source_grade
  standard_candidate_id
  unlocked_named_candidate_ids
  selected_variant_id
  target_lane_id
  high_grade_slot_available
  named_redeployment_provenance_eligible
  ineligible_reason

HighGradeBattlefieldState:
  active_high_grade_unit_instance_id
  active_grade
  active_variant_type
  active_lane_id
  latest_named_hero_death_sequence
```

## 10. 적대적 검토

| 공격 | 판정 | 보완 |
|---|---|---|
| 이름 지정 영웅 활성 중 표준 영웅으로 제한 우회 | 금지 | 모든 HERO·LEGENDARY 등급 합산 |
| 전설 당첨이 슬롯 충돌로 소멸 | 금지 | 정상 획득·보관·판매 |
| 해금 영웅 변환으로 보너스 유닛 생성 | 금지 | 1토큰→1유닛 치환 |
| 사망 전 보관 토큰으로 이름 지정 영웅 즉시 재출전 | 금지 | post-death created_sequence 요구 |
| 더 높은 등급 획득 시 기존 유닛 강제 교체 | 금지 | 비가역 배치·수동 교체 금지 |
| 해금 영웅이 표준 2스킬까지 함께 보유 | 금지 | 표준 2스킬을 고유 2스킬로 교체 |

## 11. 구현 경계

```text
PRODUCT_CODE = UNCHANGED
EXACT_HERO_IDENTITIES = PENDING
EXACT_UNIQUE_SKILL_2 = PENDING
FUTURE_NAMED_LEGENDARY = NOT_NOW
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
```
