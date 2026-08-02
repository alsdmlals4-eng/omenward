# OMENWARD 영웅 이상 등급 단일 활성·해금 고유 스킬 교체 승인안

```yaml
decision_id: OMW-DEC-20260802-GAMEPLAY-HERO-GRADE-SLOT-AND-UNLOCKED-SKILL-REPLACEMENT-V1
approved_at: 2026-08-02 23:07 KST
approval: USER_DIRECT_REFINEMENT
status: USER_APPROVED / ACTIVE_PLANNING_BRANCH / NOT_IMPLEMENTED
scope: HERO_AND_LEGENDARY_GRADE_GLOBAL_SLOT_AND_UNLOCKED_SKILL_SLOT_REPLACEMENT
refines:
  - OMW-DEC-20260802-GAMEPLAY-HERO-UNIQUE-SKILL-UPGRADE-MODEL-V1
  - OMW-DEC-20260802-GAMEPLAY-HERO-UNIQUENESS-AND-ACTIVE-LIMIT-V1
  - OMW-DEC-20260802-GAMEPLAY-HERO-ABILITY-ACTIVATION-MODE-V1
base_grade_authority: APPROVED_UNIT_GRADE_AND_ABILITY_GROWTH.md
product_code_authority: NONE
exact_skills: PENDING
exact_values: PENDING
unlocked_legendary_implementation: FUTURE_NOT_NOW
simulation: NOT_RUN
runtime_validation: NOT_RUN
human_validation: NOT_RUN
```

## 1. 결정 요약

전장 전체에서 등급이 `[영웅]` 이상인 유닛은 이름 지정 여부와 관계없이 동시에 최대 1명만 활성화할 수 있다.

```text
ACTIVE_UNIT_COUNT_WHERE_GRADE_IN(HERO, LEGENDARY) <= 1
```

해금 이름 지정 영웅은 원본 `[영웅]` 등급 유닛에 스킬을 하나 더 추가하지 않는다. 원본 영웅 등급의 **2스킬 슬롯을 영웅 고유 스킬로 교체**한다.

향후 해금 이름 지정 `[전설]`을 제작할 때는 원본 전설 등급의 **3스킬 슬롯을 전설 고유 스킬로 교체**한다. 해금 전설은 현재 구현 범위가 아니며 미래 기획 슬롯만 예약한다.

## 2. 표준 등급 성장 구조

기존 등급 정본은 유지한다.

```text
[일반]
= 1스킬 기본형

[엘리트]
= 강화된 1스킬

[영웅]
= 강화된 1스킬 + 표준 2스킬

[전설]
= 강화된 1스킬 + 강화된 표준 2스킬 + 표준 3스킬
```

병영 Tier가 제공하는 핵심 패시브 성장과 룰렛 등급이 제공하는 일반 스킬 성장은 계속 별도 축이다.

## 3. 해금 이름 지정 영웅의 스킬 구조

```text
표준 [영웅]
= 강화된 1스킬 + 표준 2스킬

해금 이름 지정 [영웅]
= 강화된 1스킬 + 이름 지정 영웅 고유 2스킬
```

```text
NAMED_HERO_UNIQUE_SKILL_SLOT = SKILL_2
STANDARD_HERO_SKILL_2 = REPLACED
EXTRA_SKILL_SLOT_ADDED = FALSE
HERO_EXCLUSIVE_PASSIVE_COUNT = 0
```

- 고유 2스킬은 표준 2스킬과 같은 슬롯을 소유한다.
- 고유 스킬은 표준 2스킬보다 더 강하고 식별 가능한 전장 고점을 제공한다.
- 고유 스킬을 추가 능력처럼 중복 보유하지 않는다.
- 기본 공격·강화된 1스킬·병영 Tier 패시브는 원본 영웅 등급 계약을 따른다.
- 패시브나 숨은 상시 보너스로 추가 전투 예산을 우회하지 않는다.

## 4. 향후 해금 이름 지정 전설의 스킬 구조

```text
표준 [전설]
= 강화된 1스킬 + 강화된 표준 2스킬 + 표준 3스킬

향후 해금 이름 지정 [전설]
= 강화된 1스킬 + 강화된 표준 2스킬 + 이름 지정 전설 고유 3스킬
```

```text
NAMED_LEGENDARY_UNIQUE_SKILL_SLOT = SKILL_3
STANDARD_LEGENDARY_SKILL_3 = REPLACED
EXTRA_LEGENDARY_SKILL_SLOT_ADDED = FALSE
IMPLEMENTATION_NOW = FALSE
```

- 해금 전설은 현재 초기 5명 제작·구현 범위에 포함하지 않는다.
- 해금 영웅과 해금 전설이 같은 캐릭터의 단계 상승인지, 별도 로스터인지 아직 확정하지 않는다.
- 해금 전설의 획득·토큰 변환·해금 비용·출전 규칙·정확 파워 차이는 별도 Decision으로 확정한다.
- 현재 문서는 3스킬 슬롯을 고유 스킬 슬롯으로 사용한다는 미래 방향만 승인한다.

## 5. 파워 계층

현재 승인 파워 계층:

```text
표준 [영웅] 등급
< 해금 이름 지정 [영웅]
< 표준 [전설] 등급
```

- 해금 영웅은 표준 영웅보다 더 강하고 더 큰 전장 임팩트를 제공한다.
- 해금 영웅의 단일 고유 2스킬은 전선을 흔들 수 있어야 하지만, 표준 전설의 강화 2스킬·3스킬·상위 기본 전투 예산을 합친 고점을 넘지 않는다.
- 향후 해금 전설과 표준 전설의 정확한 상대 파워는 별도 Decision과 simulation으로 확정한다.

```text
NAMED_HERO_POWER_FLOOR > STANDARD_HERO_POWER
NAMED_HERO_POWER_CEILING < STANDARD_LEGENDARY_POWER
```

정확 허용 오차·DPS·생존·지원·전장 가치 비율은 아직 고정하지 않는다.

## 6. 영웅 이상 등급 전역 단일 활성 슬롯

제한 대상은 이름 지정 영웅만이 아니다.

다음 유닛을 모두 합쳐 전장 전체에 최대 1명만 존재할 수 있다.

- 표준 `[영웅]` 등급 유닛.
- 해금 이름 지정 `[영웅]`.
- 표준 `[전설]` 등급 유닛.
- 향후 해금 이름 지정 `[전설]`.

```text
HIGH_GRADE_ACTIVE_CAP = 1
COUNTED_GRADES = HERO | LEGENDARY
COUNTED_VARIANTS = STANDARD | UNLOCKED_NAMED
SCOPE = ALL_THREE_LANES
```

- 상·중·하 전선을 합쳐 하나의 슬롯을 공유한다.
- 병종·이름·전선·표준/해금 여부를 바꾸어 제한을 우회할 수 없다.
- 일반·엘리트 등급은 이 슬롯에 포함하지 않는다.
- 활성 유닛이 사망·완전 제거되거나 MapRun이 종료되면 슬롯이 빈다.
- Stage·Act·정비시간 전환만으로 살아 있는 유닛을 제거하거나 슬롯을 비우지 않는다.
- 수동 퇴각·교대·판매·재보관으로 슬롯을 비우는 것은 금지한다.

## 7. 획득·보관·판매와 배치 제한

전역 제한은 룰렛 보상 획득 자체를 무효화하지 않고 **전장 배치에만 적용**한다.

```text
영웅 이상 등급 토큰 획득
→ 슬롯이 비어 있으면 합법 후보를 선택해 배치 가능
→ 슬롯이 차 있으면 보관 또는 판매 가능
→ 자동 소멸·자동 교체·강제 배치 금지
```

- 활성 영웅 이상 유닛이 존재해도 새 영웅·전설 결과는 정상 생성한다.
- 슬롯이 차 있으면 해당 토큰을 전장 유닛으로 변환·배치할 수 없다.
- 보관함 용량·판매 가치·UI 표시는 기존 공통 시스템을 따른다.
- 전설 당첨이 슬롯 충돌 때문에 무가치하게 느껴지지 않도록 보관·판매 가치와 충돌 안내를 검증한다.
- 사망 전 보관 토큰의 재출전 provenance 규칙은 이름 지정 영웅의 기존 계약을 유지하며, 표준 영웅·전설의 세부 교대 규칙은 별도 확정 전 임의 확대하지 않는다.

## 8. 고유 스킬 자동 발동 공통 프레임

사용자가 승인한 권장 발동 구조를 적용한다.

```text
COOLDOWN
→ READY_WAITING_FOR_VALID_CONDITION
→ 유효 조건·대상 확인
→ target filter·priority·deterministic tie-break
→ 발동 직전 재검증
→ CAST_COMMIT
→ 효과·VFX/SFX·로그
→ COOLDOWN
```

- 고유 2스킬은 규칙 기반 자동 발동이다.
- 공통 cooldown 구조를 사용하되 병종별 유효 조건과 타기팅은 다르게 둔다.
- cooldown이 끝나도 유효 조건이 없으면 준비 상태를 보존한다.
- 유효 대상이 없다는 이유로 cooldown을 낭비하지 않는다.
- 수동 스킬 버튼·수동 타깃·수동 보류는 사용하지 않는다.
- 동일 저장 상태와 동일 입력 순서에서는 동일 발동 결과를 내야 한다.

## 9. 초기 5명 적용

초기 해금 이름 지정 영웅 5명은 모두 고유 2스킬형이다.

```text
shield_guard / 방패병 → UNIQUE_SKILL_2
archer / 궁병         → UNIQUE_SKILL_2
priest / 사제         → UNIQUE_SKILL_2
mage / 마법사         → UNIQUE_SKILL_2
assassin / 암살자     → UNIQUE_SKILL_2
```

- 정확 영웅 이름과 고유 2스킬 효과는 후속 Decision으로 확정한다.
- 각 고유 2스킬은 한 번의 발동으로 해당 병종이 배치된 전선의 국면에 식별 가능한 변화를 만들어야 한다.
- 다섯 스킬은 공통 자동 스킬 프레임을 공유하고 새 AI 아키텍처·새 전체 리그를 요구하지 않는다.

## 10. 핵심 시스템 적합성

오멘워드의 핵심 재미는 다음 인과다.

```text
예고된 공세 읽기
→ 건물로 토큰·릴 구조 설계
→ 룰렛 결과 조작·확정
→ 희귀 병력 획득
→ 어느 전선에 비가역 커밋할지 판단
→ 전황 역전
→ 결과를 다음 설계에 환류
```

영웅 이상 단일 활성 슬롯은 희귀 등급 결과를 단순 누적 전력으로 만들지 않고 **세 전선 중 어디에 최고 전력을 커밋할지 선택하는 전략 자원**으로 만든다.

해금 영웅의 고유 2스킬은 새로운 독립 시스템이 아니라 영웅 등급 당첨의 전장 보상과 해금 성장 기대를 강화한다.

## 11. 적대적 검토

| 공격 | 판정 | 보완 |
|---|---|---|
| 표준 영웅이 활성 중이면 전설 당첨을 즉시 사용할 수 없어 잭팟 감정이 깨진다 | 유효 | 획득 유지·보관/판매·명확한 슬롯 충돌 UI·전설 판매가치 검증 |
| 3~7줄 영웅 결과가 잦으면 슬롯 충돌 보상이 너무 많이 쌓인다 | 유효 | 영웅 결과 빈도·보관함 압력·판매 경제 simulation 필요 |
| 해금 영웅이 표준 2스킬까지 보유하면 사실상 전설을 침범한다 | 해소 | 표준 2스킬을 고유 2스킬로 교체하고 추가 슬롯 금지 |
| 고유 2스킬이 전설 3스킬보다 강해 파워 계층을 역전한다 | 유효 | `named Hero < standard Legendary` 검증 매트릭스 필수 |
| 한 고등급 유닛이 오래 생존해 이후 룰렛 고점의 배치 기회를 막는다 | 유효 | 장기 생존·토큰 보관·판매·교체 불가의 재미와 좌절을 사람 QA로 검증 |
| 전설을 얻으면 기존 영웅을 자동 제거해 강제 교체한다 | 금지 | 자동 삭제·자동 교체 금지, 비가역 커밋 유지 |
| 해금 전설 예약이 현재 구현 범위를 폭증시킨다 | 유효 | 미래 계획만 기록, 데이터·자산·코드·로스터 작업은 NOT_NOW |
| 모든 희귀 등급을 한 슬롯으로 묶으면 세 전선 다양성이 약해진다 | 유효 | 일반·엘리트·건물·타워·전선 운영이 주력이고 고등급은 단일 역전 카드로 유지 |

## 12. 데이터 계약 방향

```yaml
HighGradeBattlefieldSlot:
  active_unit_instance_id: null_or_string
  active_grade: null_or_HERO_or_LEGENDARY
  active_variant_type: null_or_STANDARD_or_UNLOCKED_NAMED
  active_unit_archetype_id: null_or_string
  active_lane_id: null_or_string

UnlockedGradeVariantSpec:
  variant_id: string
  source_grade_template_id: string
  grade: HERO_or_LEGENDARY
  replaced_skill_slot: 2_or_3
  unique_skill_id: string
  source_skill_id_replaced: string
  activation_mode: AUTOMATIC_RULE_BASED
  cooldown_state_machine: COMMON_COOLDOWN_READY_WAITING_CAST
  hero_exclusive_passive: null
```

불변식:

```text
active_high_grade_count_across_all_lanes <= 1
named_hero.replaced_skill_slot == 2
named_hero.extra_skill_count == 0
future_named_legendary.replaced_skill_slot == 3
future_named_legendary.implementation_now == false
```

## 13. 금지

- 이름 지정 영웅이 표준 2스킬과 고유 2스킬을 동시에 보유.
- 이름 지정 영웅에 별도 3번째 스킬 슬롯 추가.
- 해금 전설을 현재 초기 5명 구현 범위에 포함.
- 표준/해금 여부를 이용한 영웅 이상 등급 동시 활성 2명.
- 서로 다른 전선에 영웅과 전설을 각각 배치해 슬롯 우회.
- 활성 고등급 유닛 자동 삭제·자동 교체.
- 슬롯 충돌을 이유로 룰렛 결과 자동 소멸.
- 고유 2스킬이 전설 전체 키트를 항상 압도하도록 설계.
- 패시브·숨은 상시 보너스·수동 스킬로 스킬 슬롯 계약 우회.

## 14. 구현·검증 경계

```text
CURRENT_PRODUCT = LEGACY_PROTOTYPE
LATEST_APPROVED = DOCUMENTED_NOT_IMPLEMENTED
PRODUCT_CODE = UNCHANGED
INITIAL_NAMED_HERO_COUNT = 5
INITIAL_UNIQUE_SKILL_SLOT = 2
FUTURE_NAMED_LEGENDARY_UNIQUE_SKILL_SLOT = 3
FUTURE_NAMED_LEGENDARY_IMPLEMENTATION = NOT_NOW
EXACT_SKILLS = PENDING
EXACT_VALUES = PENDING
ASSETS = NOT_CREATED
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
```

## 15. 다음 Gate

```text
OMW-DEC-20260802-GAMEPLAY-HERO-FIRST-FIVE-UNIQUE-SKILL-2-CONCEPTS-V1
= 초기 다섯 해금 영웅의 전장 임팩트형 고유 2스킬 콘셉트 확정
```
