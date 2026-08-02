# OMENWARD 전설 재당첨·영웅 이상 단일 슬롯 충돌 해소안

```yaml
decision_id: OMW-DEC-20260802-GAMEPLAY-HERO-GRADE-SLOT-AND-UNLOCKED-SKILL-REPLACEMENT-V1
resolution_id: OMW-RES-20260802-REPEAT-LEGENDARY-TO-HERO-TOKENS-V1
resolved_at: 2026-08-02 23:07 KST
status: CANON_CONFLICT_RESOLUTION / ACTIVE_PLANNING_BRANCH / NOT_IMPLEMENTED
base_grade_authority: APPROVED_UNIT_GRADE_AND_ABILITY_GROWTH.md
current_slot_authority: APPROVED_OMENWARD_HERO_GRADE_SLOT_AND_UNLOCKED_SKILL_REPLACEMENT_2026-08-02.md
product_code_authority: NONE
simulation: NOT_RUN
runtime_validation: NOT_RUN
human_validation: NOT_RUN
```

## 1. 충돌

기존 등급 계약은 한 Stage에서 전설이 이미 생성된 뒤 다시 9칸 전체 동일 결과가 나오면 해당 계열 `영웅 2명`으로 변환한다고 정의한다.

최신 전역 슬롯 계약은 표준·해금 여부와 관계없이 `[영웅]`·`[전설]` 등급 유닛을 세 전선 전체에 동시에 최대 1명만 활성화한다.

`영웅 2명`을 전장 유닛 두 개로 즉시 생성하면 최신 전역 슬롯을 위반한다.

## 2. 현행 해석

```text
한 Stage에서 표준 [전설] 결과가 이미 생성됨
+ 이후 다시 9칸 전체 동일 결과 확정
→ 같은 병종 계열 [영웅] 등급 보상 토큰 2개 생성
→ 각 토큰을 보관함에 별도 저장
→ 판매 또는 이후 합법 배치
→ 전장 배치는 영웅 이상 전역 슬롯 최대 1명 적용
```

```text
REPEAT_LEGENDARY_RESULT_OUTPUT = 2_HERO_GRADE_REWARD_TOKENS
IMMEDIATE_BATTLEFIELD_UNIT_SPAWN_COUNT = 0
TOKEN_INSTANCE_COUNT = 2
HIGH_GRADE_ACTIVE_CAP = 1
```

- 두 토큰은 서로 다른 `token_instance_id`를 가진다.
- 두 토큰 모두 같은 확정된 룰렛 결과와 병종 계열 provenance를 기록한다.
- 슬롯이 비어 있더라도 한 번에 하나의 영웅 이상 유닛만 변환·배치할 수 있다.
- 남은 토큰은 보관하거나 판매한다.
- 활성 `[영웅]`·`[전설]`이 존재하면 두 토큰 모두 즉시 배치할 수 없지만 정상 획득한다.
- 토큰을 자동 삭제·합성·저등급화하지 않는다.

## 3. 표준·해금 후보

각 영웅 등급 보상 토큰은 기존 동병종 변환 계약을 따른다.

```text
영웅 등급 토큰 1개
→ 표준 [영웅] 등급 유닛
OR
→ 같은 UnitArchetype에 연결되고 해금된 이름 지정 [영웅]
```

- 이름 지정 영웅을 선택하면 표준 2스킬 대신 고유 2스킬을 가진다.
- 두 토큰이 있다고 해서 이름 지정 영웅 두 명을 동시에 배치할 수 없다.
- 이름 지정 영웅 사망 후 재출전 provenance는 기존 전용 계약을 유지한다.

## 4. 보관함 예외 처리

재전설 결과는 한 번에 토큰 2개를 생성하므로 보관함 용량 경계가 필요하다.

현재 승인 해석:

- 보관함에 두 칸 이상이 비어 있으면 두 토큰을 모두 저장한다.
- 한 칸만 비어 있거나 가득 찬 경우의 초과 보상 처리 방식은 아직 확정하지 않는다.
- 초과 토큰을 자동 삭제하거나 강제 판매했다고 가정하지 않는다.
- 정확한 `보관함 부족 → 선택 판매/기존 토큰 정리/임시 보상 대기` UX는 별도 Decision으로 확정한다.

```text
INSUFFICIENT_STORAGE_OVERFLOW_POLICY = PENDING
AUTO_DELETE_OVERFLOW_TOKEN = FORBIDDEN
AUTO_SELL_OVERFLOW_TOKEN = NOT_APPROVED
```

## 5. 적대적 검토

| 공격 | 판정 | 보완 |
|---|---|---|
| 영웅 2명을 즉시 생성해 전역 cap 1을 위반한다 | 유효 충돌 | 유닛이 아니라 보상 토큰 2개 생성 |
| 토큰 하나만 주면 기존 재전설 보상이 약화된다 | 유효 | token instance 2개 유지 |
| 두 토큰을 한 유닛으로 합쳐 해금 영웅을 강화한다 | 미승인 | 각 토큰은 독립적인 1토큰→1유닛 후보 |
| 슬롯이 차 있으면 재전설 잭팟이 무가치하다 | 유효 | 정상 획득·보관·판매, 가치와 UX 사람 검증 |
| 보관함이 한 칸만 남았을 때 토큰이 사라진다 | 유효 미결정 | 자동 삭제 금지, overflow policy 후속 Decision |
| 사망 전 저장한 두 토큰으로 이름 지정 영웅을 즉시 연속 재출전한다 | 기존 계약 충돌 | 이름 지정 영웅 재출전은 post-death provenance 규칙 유지 |

## 6. 데이터 방향

```yaml
RepeatLegendaryRewardBatch:
  source_spin_id: string
  source_unit_archetype_id: string
  created_sequence: integer
  token_instance_ids: [string, string]
  grade: HERO
  token_count: 2

StoredRewardToken:
  token_instance_id: string
  reward_batch_id: string
  unit_archetype_id: string
  grade: HERO
  created_by_spin_id: string
  created_sequence: integer
  conversion_state: STORED_or_SOLD_or_DEPLOYED
```

## 7. 검증 요구

- 재전설 확정 시 정확히 두 개의 영웅 등급 토큰이 생성된다.
- 전장 유닛은 즉시 생성되지 않는다.
- 두 토큰의 ID는 다르며 결과 provenance는 동일 batch를 가리킨다.
- 활성 고등급 슬롯이 차 있어도 토큰 획득은 유지된다.
- 한 토큰을 배치해 슬롯이 차면 두 번째 토큰 배치는 차단된다.
- 저장·Retry로 토큰 수·병종·ID·배치 가능 여부를 재굴림할 수 없다.
- 보관함 overflow policy 확정 전 자동 삭제·자동 판매를 구현하지 않는다.

## 8. 구현 경계

```text
CURRENT_PRODUCT = LEGACY_PROTOTYPE
PRODUCT_CODE = UNCHANGED
REPEAT_LEGENDARY_TOKEN_COUNT = 2
IMMEDIATE_UNIT_SPAWN = 0
STORAGE_OVERFLOW_POLICY = PENDING
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
```
