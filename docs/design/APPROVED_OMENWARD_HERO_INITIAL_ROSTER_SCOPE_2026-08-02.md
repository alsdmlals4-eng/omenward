# OMENWARD 이름 지정 영웅 초기 로스터 범위 승인안

```yaml
decision_id: OMW-DEC-20260802-GAMEPLAY-HERO-INITIAL-ROSTER-SCOPE-V1
approved_at: 2026-08-02 21:59 KST
refined_at: 2026-08-02 23:07 KST
status: USER_APPROVED / REFINED_TO_FIVE_UNIQUE_SKILL_2 / NOT_IMPLEMENTED
current_authority: OMW-DEC-20260802-GAMEPLAY-HERO-GRADE-SLOT-AND-UNLOCKED-SKILL-REPLACEMENT-V1
product_code_authority: NONE
```

## 1. 범위

초기 제작·검증 로스터는 서로 다른 기존 병종 5종에 이름 지정 `[영웅]` 1명씩, 총 5명이다.

```text
INITIAL_NAMED_HERO_COUNT = 5
INITIAL_SOURCE_ARCHETYPE_COUNT = 5
HEROES_PER_ARCHETYPE = 1
INITIAL_ROSTER_IS_FINAL_RELEASE_CAP = FALSE
```

초기 로스터는 방패병·궁병·사제·마법사·암살자다.

## 2. 키트 범위

```text
각 초기 영웅
= 원본 [영웅] 등급의 강화 1스킬
+ 표준 2스킬을 교체한 고유 2스킬
+ 이름·초상·스킨·식별 VFX/SFX
```

- 추가 3번째 스킬 슬롯 없음.
- 영웅 전용 패시브 없음.
- 의무 능력치 하향 없음.
- 원본 리그·기본 애니메이션·AI·기본 공격 재사용.

## 3. 검증 목적

초기 5명은 다음을 검증한다.

- 전열 유지.
- 대공·고가치 표적 제거.
- 아군 위기 복구.
- 적 군집 붕괴.
- 후열 핵심 제거.
- 공통 cooldown·준비 대기 상태.
- 전역 영웅 이상 슬롯과 세 전선 배치 기회비용.
- 표준 영웅 < 해금 영웅 < 표준 전설 파워 계층.
- 자산 재사용률과 고유 스킬 VFX/SFX 제작량.

## 4. 전역 제한

```text
ACTIVE_UNIT_COUNT_WHERE_GRADE_IN(HERO, LEGENDARY) <= 1
```

초기 해금 영웅 5명뿐 아니라 모든 표준 영웅·전설도 같은 슬롯을 사용한다.

## 5. 향후 해금 전설 제외

```text
FUTURE_NAMED_LEGENDARY_UNIQUE_SKILL_SLOT = 3
FUTURE_NAMED_LEGENDARY_IMPLEMENTATION = NOT_NOW
```

향후 해금 전설의 슬롯 방향은 예약하지만 현재 초기 제작 수량·자산·스킬 설계·구현 범위에 포함하지 않는다.

## 6. 성공 기준

- 다섯 고유 2스킬의 발동 순간과 전선 결과가 즉시 식별된다.
- 어떤 영웅도 모든 Stage·전선의 유일한 정답이 아니다.
- 표준 전설은 모든 초기 해금 영웅보다 높은 전체 전투 고점을 유지한다.
- 고등급 슬롯이 차 있을 때 새 영웅·전설 결과의 보관·판매가 의미 있는 선택이다.
- 기본·일반 난이도는 해금 영웅 없이도 완료 가능하다.
- 다섯 스킬이 다섯 완전 신규 유닛 제작으로 확대되지 않는다.

## 7. 구현 경계

```text
CURRENT_PRODUCT = LEGACY_PROTOTYPE
PRODUCT_CODE = UNCHANGED
EXACT_HERO_IDENTITIES = PENDING
EXACT_UNIQUE_SKILL_2 = PENDING
FUTURE_NAMED_LEGENDARY = NOT_NOW
ASSETS = NOT_CREATED
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
```
