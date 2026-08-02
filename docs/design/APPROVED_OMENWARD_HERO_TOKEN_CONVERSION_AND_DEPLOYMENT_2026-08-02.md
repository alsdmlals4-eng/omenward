# 오멘워드 영웅 등급 토큰 변환·배치 승인 계약

```yaml
decision_id: OMW-DEC-20260802-GAMEPLAY-HERO-BATTLEFIELD-ACTIVATION-V1
approved_at: 2026-08-02 16:11 KST
approval: USER_DIRECT_APPROVAL
status: USER_APPROVED_STRUCTURE / SINGLE_ACTIVE_EXIT_STAGE_AND_REDEPLOYMENT_RULES_APPROVED / NOT_IMPLEMENTED
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
→ 원본 영웅 등급 병종 유지 또는 조건을 충족한 해금 동병종 영웅으로 변경
→ 상·중·하 한 전선에 비가역 배치
```

이름 지정 영웅의 첫 출전에는 일반 변환 조건을 적용한다. 이름 지정 영웅이 사망·완전 제거된 뒤의 재출전에는 추가로 **사망 이후 룰렛 결과에서 생성된 토큰 provenance**가 필요하다.

## 2. 영웅 해금·명부 정정

- 각 영웅은 하나의 기존 `UnitArchetype`에 고정 연결된다.
- 하나의 병종에 서로 다른 해금 영웅이 여러 명 존재할 수 있다.
- 영웅 해금 시 Profile 영웅 명부에 영구 등록된다.
- 별도의 런 시작 전 영웅 등록·계약 단계는 요구하지 않는다.
- 이전 문서의 `pre-run registration` 해석은 이 결정으로 대체한다.
- 해금되지 않은 영웅은 변환 후보에 나타나지 않는다.

## 3. 보관함 변환 절차

기본 영웅 변환 UI는 다음 조건을 모두 만족할 때만 활성화된다.

```text
token.grade == HERO
AND token.unit_archetype_id == hero.unit_archetype_id
AND hero.id IN unlocked_hero_ids
AND active_hero_unit_instance_id == null
AND (
  no_named_hero_has_died_in_this_maprun
  OR token.created_sequence > latest_named_hero_death_sequence
)
```

플레이어 선택:

1. 원본 `[영웅] 등급 병종 토큰`을 그대로 유지한다.
2. 모든 변환 조건을 만족하면 같은 병종의 해금 영웅 목록을 열어 한 명을 선택한다.
3. 변환 결과와 전선 배치 영향을 미리 확인한다.
4. 상·중·하 중 한 전선을 선택하고 확정한다.

확정 전에는 취소하거나 다른 동병종 영웅을 선택할 수 있다. 확정 뒤에는 토큰 변환과 전선 배치를 되돌리지 않는다.

활성 영웅이 이미 존재하면 영웅 변환은 차단되지만 토큰은 보관함에 유지하거나 원본 영웅 등급 병종 유닛으로 배치할 수 있다.

활성 영웅이 사망한 뒤에는 다음 규칙을 추가 적용한다.

- 사망 전에 보관한 영웅 등급 토큰은 원본 영웅 등급 병종으로 사용할 수 있다.
- 사망 전에 보관한 토큰은 이름 지정 영웅 재출전 변환 후보가 아니다.
- 사망 이후 룰렛에서 새로 확정된 동병종 영웅 등급 토큰만 이름 지정 영웅 재출전에 사용할 수 있다.

## 4. 수량·인과 불변식

```text
ONE_ELIGIBLE_HERO_GRADE_TOKEN
→ ONE_DEPLOYED_UNIT
```

- 영웅 변환은 추가 유닛을 생성하지 않는다.
- 원본 토큰 하나를 선택 영웅 하나로 치환한다.
- 영웅으로 변경하지 않으면 원본 영웅 등급 병종을 배치할 수 있다.
- 일치하는 해금 영웅이 없어도 원본 토큰은 정상적으로 사용 가능하다.
- 변환은 다른 보관 토큰·과거 SpinSnapshot·릴 구조·당첨 확률을 변경하지 않는다.
- 영웅 사망은 토큰 반환·보장·pity·확률 보정을 생성하지 않는다.
- 사망 후 재출전 변환은 토큰의 생성 sequence가 최신 영웅 사망 sequence보다 커야 한다.
- 전선 배치는 기존 PendingReward의 한 전선 비가역 커밋 규칙을 따른다.

## 5. 복수 동병종 영웅·단일 활성·퇴각 금지

- 한 병종에 여러 영웅을 해금할 수 있다.
- 보관함의 영웅 선택 목록에는 해당 토큰과 병종이 일치하고 현재 provenance 조건을 만족하는 모든 해금 영웅을 표시한다.
- 각 영웅은 단순 수치 상위호환이 아니라 다른 역할·조건·약점을 제공해야 한다.
- 전장 전체에는 이름이 지정된 해금 영웅 유닛이 동시에 최대 1명만 존재할 수 있다.
- 동일한 `hero_id`도 이전 인스턴스가 사망·완전 제거된 뒤 사망 이후 새 룰렛 결과에서 획득한 동병종 영웅 등급 토큰을 소비해 다시 배치할 수 있다.
- 서로 다른 영웅도 기존 active hero가 남아 있는 동안에는 추가 배치할 수 없다.
- 배치한 영웅은 수동 퇴각·교대·판매·재보관할 수 없다.
- Stage·Act 전환만으로 영웅을 귀환시키거나 active 슬롯을 비우지 않는다.
- 영웅 사망·완전 제거 또는 MapRun 종료 시 active 상태를 종료한다.

주 책임 원본:

- 단일 활성·반복 출전: `APPROVED_OMENWARD_HERO_SINGLE_ACTIVE_AND_REPEAT_DEPLOYMENT_2026-08-02.md`
- 퇴각·교대·종료 사건: `APPROVED_OMENWARD_HERO_EXIT_AND_REPLACEMENT_2026-08-02.md`
- 사망 무회수·post-death 결과·새 인스턴스: `APPROVED_OMENWARD_HERO_REDEPLOYMENT_INITIAL_STATE_2026-08-02.md`

## 6. UX·데이터 책임

```yaml
HeroProfileState:
  unlocked_hero_ids
  hero_unit_archetype_bindings

StoredRewardToken:
  token_instance_id
  unit_archetype_id
  grade
  created_by_spin_id
  created_sequence
  conversion_state
  selected_hero_id

HeroConversionPreview:
  source_token_instance_id
  candidate_hero_ids
  selected_hero_id
  target_lane_id
  redeployment_provenance_eligible
  ineligible_reason

HeroBattlefieldState:
  active_hero_unit_instance_id
  active_hero_id
  active_hero_lane_id
  latest_named_hero_death_sequence
```

- 후보에는 이름·초상·연결 병종·핵심 역할·변환 후 변화·현재 사용 가능 여부를 표시한다.
- active hero가 있으면 후보를 `전장 영웅 1명 제한` 사유로 비활성화한다.
- 사망 전 보관 토큰은 `사망 이후 새 영웅 등급 결과 필요` 사유로 이름 지정 영웅 후보를 비활성화한다.
- 사망 전 토큰의 원본 영웅 등급 병종 사용은 차단하지 않는다.
- 해금되지 않은 영웅은 잠금 이유를 보여 줄 수 있지만 선택할 수 없다.
- 병종 불일치 영웅은 후보에 포함하지 않는다.
- 확정 시 active slot, 토큰 provenance, 원본 token instance, 선택 영웅 ID, 대상 전선을 한 transaction으로 검증·기록한다.
- 중복 확정·부분 저장·원본 토큰 잔존·동시 영웅 둘 생성을 허용하지 않는다.
- 수동 퇴각·교체 버튼을 노출하지 않으며 Stage 전환에도 현재 영웅 유지 상태를 표시한다.

## 7. 적대적 검토

| 공격 | 판정 | 보완 |
|---|---|---|
| 영웅 해금이 릴 확률을 직접 높인다 | 유효 | 룰렛은 익명 영웅 등급 병종 토큰만 생성, 해금은 보관함 변환 후보만 추가 |
| 영웅 변경으로 병력이 하나 더 생긴다 | 유효 | 1토큰→1유닛 치환 불변식 |
| 같은 병종 영웅이 여러 명이면 자유 직업 변경처럼 변한다 | 유효 | 모든 후보는 동일 UnitArchetype 고정 바인딩 |
| 강한 영웅 하나가 모든 선택을 지배한다 | 유효 | 역할·조건·약점 기반 sidegrade, 반복 선택률 simulation 필요 |
| 보관함 선택이 복잡해진다 | 유효 | 영웅 등급 토큰에서만 목록 노출, 동병종 후보만 필터링 |
| 영웅 미해금 플레이가 손해만 보는 미완성판이 된다 | 유효 | 원본 영웅 등급 토큰 사용 가능·기본 Profile 완주 유지 |
| 사망 전 토큰을 쌓아 즉시 영웅 교대한다 | 유효 | 사망 후 재출전 변환은 post-death created_sequence 토큰만 허용 |
| 같은 영웅을 여러 번 배치해 복제된다 | 사용자 승인 | 동시 활성은 1명, 사망 후 새 적격 토큰으로만 반복 출전 허용 |
| 저장·동시 입력으로 영웅 둘이 생긴다 | 유효 | active slot·provenance 검증과 토큰 변환·배치를 원자 transaction으로 처리 |
| 살아 있는 영웅을 퇴각해 새 영웅으로 즉시 바꾼다 | 유효 | 수동 퇴각·교대·판매·재보관 금지 |
| Stage 종료마다 무료 교체한다 | 유효 | Stage·Act 전환에도 동일 영웅 인스턴스 유지 |

## 8. 미확정 항목

- 원본 `[영웅] 등급 병종 토큰`과 이름 지정 영웅의 정확한 power budget.
- 영웅별 능력·등급·명단·수치.
- 변환 UI의 정확한 화면 배치·키 입력.
- 영웅 사망 연출·결과 로그.
- post-death provenance 저장·Retry fault test.

## 9. 후속 Gate

```text
OMW-DEC-20260802-GAMEPLAY-HERO-POWER-BUDGET-AND-SIDEGRADE-V1
= 이름 지정 영웅과 원본 영웅 등급 병종의 총 전투 예산·전문화·약점 관계
```

## 10. 상태 경계

```text
DESIGN: USER_APPROVED_TOKEN_CONVERSION_AND_DEPLOYMENT
PRE_RUN_HERO_REGISTRATION: SUPERSEDED
SIMULTANEOUS_ACTIVE_HEROES: MAX_1
SAME_HERO_REPEAT_DEPLOYMENT: ALLOWED_WITH_POST_DEATH_RESULT
MANUAL_RETREAT_AND_REPLACEMENT: FORBIDDEN
STAGE_AND_ACT_TRANSITION: SAME_INSTANCE_REMAINS
ACTIVE_SLOT_CLEAR: HERO_DEATH_OR_MAPRUN_END
PRE_DEATH_STORED_TOKEN_FOR_REDEPLOYMENT: FORBIDDEN
POST_DEATH_MATCHING_HERO_GRADE_RESULT: REQUIRED
EXACT_VALUES: PENDING
SIMULATION: NOT_RUN
RUNTIME: NOT_RUN
HUMAN_QA: NOT_RUN
PRODUCT_CODE: UNCHANGED
```