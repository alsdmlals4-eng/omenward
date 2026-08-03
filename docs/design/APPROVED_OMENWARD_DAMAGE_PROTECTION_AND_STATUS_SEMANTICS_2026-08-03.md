# OMENWARD Damage·Protection·Status Semantics

```yaml
decision_id: OMW-DEC-20260803-VALIDATION-DAMAGE-PROTECTION-AND-STATUS-SEMANTICS-V1
updated_at: 2026-08-03
status: USER_APPROVED / ACTIVE_PLANNING_BRANCH / NOT_IMPLEMENTED
work_mode: TOTAL_PLANNING
parent_decision: OMW-DEC-20260803-VALIDATION-COMMON-COMBAT-SCHEMA-AND-RESOLUTION-ORDER-V1
parent_validation_decision: OMW-DEC-20260803-VALIDATION-DETERMINISTIC-SIMULATION-HARNESS-SCOPE-V1
grill_me_count: 3_OF_10
product_code_authority: NONE
simulation_tool_code_authority: NONE
simulation: NOT_RUN
runtime_validation: NOT_RUN
human_validation: NOT_RUN
```

## 1. 결정

OMENWARD 전투의 최초 피해 계약은 **2개 피해 채널과 독립 태그 구조**로 구성한다.

```text
KINETIC → ARMOR
ARCANE  → RESISTANCE
```

피해 채널은 방어축만 결정한다. 공격 방식·범위·지속·대상 종류는 채널에 섞지 않고 독립 태그와 Target Profile로 표현한다.

```text
DAMAGE_CHANNEL = exactly one of [KINETIC, ARCANE]
DELIVERY_TAGS = zero or more of [BASIC, SKILL, AREA, DAMAGE_OVER_TIME, ENVIRONMENT, TRANSFERRED]
TARGET_PROFILE = UNIT / BUILDING / OBJECTIVE + GROUND / FLYING eligibility
```

현 버티컬 슬라이스에서는 다음을 지원하지 않는다.

```text
TRUE_DAMAGE = FORBIDDEN
EXECUTE_OR_INSTANT_KILL = FORBIDDEN
REVIVE = FORBIDDEN
FRIENDLY_FIRE = FORBIDDEN_BY_DEFAULT
SELF_DAMAGE = FORBIDDEN_BY_DEFAULT
```

미래 콘텐츠가 이를 요구하면 기존 enum에 조용히 추가하지 않고 별도 사용자 Decision과 적대적 검토를 거친다.

## 2. 제품 코어와의 연결

이 계약의 목적은 피해 상성표를 늘리는 것이 아니다. 플레이어가 세 전선의 공세를 읽고 룰렛에서 만든 병력을 어느 전선에 비가역 배치할지 판단할 수 있도록 **읽을 수 있는 최소 방어축**을 제공하는 것이다.

```text
공세 예고에서 KINETIC / ARCANE 위협 확인
→ 룰렛·TokenSource로 병력 구성
→ Armor / Resistance 대응 병력·건물 선택
→ 한 전선에 비가역 커밋
→ barrier·status·damage event를 원인별 복기
→ 다음 Stage 릴·건물 설계에 환류
```

피해 채널이 3개 이상으로 늘어나 세 릴·세 전선·건물·병종·영웅 판단을 상성 암기로 덮는 것을 금지한다.

## 3. 범위

### 3.1 포함

- `KINETIC`, `ARCANE` 피해 채널.
- `ARMOR`, `RESISTANCE` 방어축.
- delivery tag와 target profile의 독립 분류.
- `DamageIntent`, `RestoreIntent`, `ProtectionIntent`, `StatusApplicationIntent`.
- barrier·absorption·HP-loss redirection·health floor의 의미와 적용 위치.
- restore와 negative damage의 분리.
- status taxonomy·stacking policy·expiry·dispel 의미.
- 같은 tick에서 보호·피해·상태가 기존 commit을 소급 변경하지 않는 규칙.
- raw damage·mitigated damage·barrier absorption·resolved HP loss의 event 분리.
- 유닛·건물·목표 및 ground·flying 대상 경계.

### 3.2 제외

- Armor·Resistance 정확 공식과 계수.
- channel별 기본 수치·관통·상한·최소 피해.
- barrier 최대치·지속시간·source별 budget의 정확 값.
- status stack cap·duration·tick interval의 정확 값.
- critical hit·lifesteal·overheal conversion.
- true damage·execute·revive.
- 다섯 영웅 고유 2스킬의 exact 피해·보호·status 값.
- GDScript·Scene·Resource·fixture·test 구현.
- simulation 실행과 밸런스 결론.

## 4. 공통 Intent Schema

### 4.1 `DamageIntent`

```text
intent_id
root_effect_id
source_id
original_source_id
target_id
commit_id
impact_tick
impact_sequence
damage_channel
delivery_tags
raw_amount_q
source_modifier_refs
target_modifier_refs
target_profile_requirement
mitigation_policy
barrier_policy
hp_loss_redirection_policy
health_floor_policy
post_hit_payload_refs
deployment_id_if_applicable
```

- `damage_channel`은 정확히 하나여야 한다.
- delivery tag는 복수 허용하지만 방어축을 바꾸지 않는다.
- `AREA`는 범위 표현이며 새로운 damage channel이 아니다.
- `DAMAGE_OVER_TIME`은 예약된 반복 DamageIntent이며 별도 방어 공식을 만들지 않는다.
- `TRANSFERRED`는 HP-loss 재배분 provenance이며 true damage가 아니다.

### 4.2 `RestoreIntent`

```text
intent_id
root_effect_id
source_id
target_id
restore_amount_q
restore_category
max_hp_clamp_policy
overheal_policy
status_payload_refs
```

Restore는 음수 DamageIntent가 아니다. 피해 방어·barrier·on-hit 피해 trigger를 거꾸로 통과하지 않는다.

### 4.3 `ProtectionIntent`

```text
intent_id
source_id
target_id
protection_type
start_tick
end_tick_exclusive
remaining_budget_q
channel_filter
delivery_filter
consume_priority
spillover_policy
health_floor_q_if_any
```

현재 `protection_type`:

```text
BARRIER
IMMUNITY
HEALTH_FLOOR
HP_LOSS_REDIRECTION
```

### 4.4 `StatusApplicationIntent`

```text
intent_id
source_id
target_id
status_definition_id
status_family
start_tick
end_tick_exclusive
stacking_group_id
stacking_policy
stack_delta
payload
```

status definition이 stacking policy를 제공하지 않으면 fixture와 data는 invalid다.

## 5. Damage Channel·Defense Axis

### 5.1 KINETIC

```text
KINETIC_DAMAGE → ARMOR_FORMULA_HOOK
```

기본 공격·투사체·근접 공격·물리 충격·공성 타격의 기본 채널 후보지만, delivery tag나 animation만으로 채널을 추론하지 않는다. 각 action data가 명시한다.

### 5.2 ARCANE

```text
ARCANE_DAMAGE → RESISTANCE_FORMULA_HOOK
```

마법·베일 에너지·주문·비물리적 효과의 기본 채널 후보지만, 영웅 이름이나 VFX 색상만으로 채널을 추론하지 않는다.

### 5.3 금지된 혼합

```text
KINETIC_AREA != third channel
ARCANE_DOT != third channel
FLYING_DAMAGE != third channel
SIEGE_DAMAGE != third channel
```

하나의 action이 두 채널을 동시에 가해야 한다면 두 개의 명시적 DamageIntent로 분리하고 각각 event와 amount를 가진다. 숨은 hybrid channel은 금지한다.

## 6. Delivery Tags

```text
BASIC
SKILL
AREA
DAMAGE_OVER_TIME
ENVIRONMENT
TRANSFERRED
```

- `BASIC`: 표준 공격 계열.
- `SKILL`: 능력·영웅·건물 active 계열.
- `AREA`: 하나의 source intent가 복수 target을 가질 수 있음.
- `DAMAGE_OVER_TIME`: 명시된 due tick마다 새 DamageIntent를 생성.
- `ENVIRONMENT`: 전장 규칙·위험·objective 외부 효과.
- `TRANSFERRED`: 해결된 HP loss의 재배분 provenance.

태그는 면역·status·trigger filter에 사용될 수 있으나 channel defense를 대체하지 않는다.

## 7. Target Profile

```text
ENTITY_CLASS = UNIT | BUILDING | OBJECTIVE
MOVEMENT_CLASS = GROUND | FLYING
SIDE_RELATION = ALLY | ENEMY | SELF
```

기본 규칙:

```text
UNIT = targetable when action filter allows
BUILDING = targetable only when action has BUILDING eligibility
OBJECTIVE = not an HP damage target by default
FLYING = targeting eligibility, not damage channel
GROUND = targeting eligibility, not damage channel
```

Objective의 소유권 변화는 기본적으로 `R100 OBJECTIVE_AND_OWNERSHIP_RESOLVE`가 소유한다. 명시적 파괴형 Objective가 승인되기 전에는 일반 DamageIntent로 Objective HP를 감소시키지 않는다.

## 8. R80 내부 의미 순서

상위 `R80 DAMAGE_PROTECTION_STATUS_APPLY`는 다음 의미 barrier를 가진다.

```text
R80A VALIDITY_AND_ELIGIBILITY
R80B PROTECTION_SETUP
R80C DAMAGE_MITIGATION_AND_BARRIER
R80D HP_LOSS_REDIRECTION_AND_FLOOR
R80E HP_DELTA_AND_RESTORE
R80F STATUS_APPLICATION_AND_POST_HIT_QUEUE
R80G DEATH_OR_DESTRUCTION_MARK
```

### R80A — Validity·Eligibility

- target 존재·alive/operational 상태·side relation·entity class·ground/flying filter를 검사한다.
- immunity는 channel·delivery·status family 중 명시된 filter에만 적용한다.
- 무효화는 조용히 버리지 않고 이유 event를 남긴다.

### R80B — Protection Setup

- R60에서 합법적으로 commit된 same-tick `ProtectionIntent`는 피해 전에 공통 protection snapshot에 materialize한다.
- 낮은 entity ID가 먼저 처리돼 보호를 얻거나 잃지 않는다.
- 일반 status는 이 단계에서 기존 commit을 소급 취소하지 않는다.

### R80C — Damage·Mitigation·Barrier

```text
raw_amount_q
→ source outgoing modifiers
→ target incoming modifiers / vulnerability
→ KINETIC: armor hook | ARCANE: resistance hook
→ barrier / absorption
→ candidate_hp_loss_q
```

정확 공식과 rounding은 다음 numeric Decision이 소유한다.

### R80D — HP-Loss Redirection·Health Floor

- barrier가 흡수한 양은 HP loss가 아니므로 redirection 대상이 아니다.
- redirection은 해결된 candidate HP loss를 재배분한다.
- 재배분된 양은 방어 공식을 다시 통과하지 않는다.
- 각 recipient의 health floor는 재배분 뒤 독립적으로 적용한다.
- health floor는 HP를 증가시키지 않으며 heal event를 만들지 않는다.

### R80E — HP Delta·Restore

- 피해와 restore는 별도 intent·event다.
- restore는 `max_hp_q`를 넘지 않는다.
- 기본 overheal은 폐기하며 barrier로 자동 변환하지 않는다.
- death_pending 또는 dead 상태를 revive하지 않는다.

### R80F — Status·Post-Hit

- 이미 commit된 same-tick action은 새 control status 때문에 소급 취소하지 않는다.
- 일반 status의 이동·target·action 제한은 다음 해당 phase부터 적용한다.
- 즉시 protection은 반드시 `ProtectionIntent`로 표현한다.
- post-hit trigger는 별도 queue와 root effect provenance를 가진다.

### R80G — Death Mark

- 최종 HP가 사망 조건에 도달하면 `death_pending`만 표시한다.
- 실제 death·destruction finalize는 R90이 소유한다.

## 9. Barrier·Absorption

Barrier는 실제 HP와 분리된 임시 보호 budget이다.

```text
BARRIER != HP
BARRIER != HEAL
BARRIER != ARMOR_OR_RESISTANCE
```

필수 규칙:

- channel mitigation 뒤 남은 피해를 흡수한다.
- 남은 budget이 0이 되면 제거한다.
- 만료 시 잔여 budget은 폐기한다.
- barrier가 HP를 max 이상으로 만들지 않는다.
- 여러 barrier instance는 `(consume_priority, start_tick, protection_id)` canonical order로 소비한다.
- barrier 전체 cap·지속시간·source별 budget은 다음 numeric Decision이 소유한다.
- barrier 상시 유지가 공세 대응과 병종 선택을 대체하면 stop-ship 후보다.

## 10. HP-Loss Redirection·Sharing

HP-loss sharing은 새로운 공격이나 true damage가 아니라 최종 HP loss의 명시적 재배분이다.

```text
candidate_hp_loss
→ redirect allocation
→ per-recipient floor clamp
→ final HP deltas
```

안전 규칙:

```text
TRANSFER_DEPTH_MAX = 1
RECURSIVE_REDIRECTION = FORBIDDEN
SECOND_MITIGATION_PASS = FORBIDDEN
ROOT_EFFECT_ID_PRESERVED = REQUIRED
TOTAL_REDIRECTED_PLUS_REMAINDER <= ORIGINAL_CANDIDATE_HP_LOSS
```

recipient가 무효하거나 사망 상태면 명시된 `CANCEL_SHARE` 또는 `RETURN_TO_ORIGINAL_TARGET` 정책만 허용한다. 숨은 fallback target은 금지한다.

## 11. Restore·Health Floor·Death

### Restore

- 실제 HP를 회복한다.
- max HP clamp를 적용한다.
- 기본 overheal은 폐기한다.
- 피해 event와 별도 metric이다.

### Health Floor

- 이번 해결에서 허용되는 최소 HP를 정하는 damage clamp다.
- HP를 증가시키지 않는다.
- floor가 제거된 뒤 과거 피해를 재적용하지 않는다.
- death 또는 revive system이 아니다.

### Death

- R80은 `death_pending`만 표시한다.
- R90 이전에 entity를 collection에서 제거하지 않는다.
- revive는 현 버티컬 슬라이스에서 금지한다.

## 12. Status Taxonomy

현재 status family:

```text
STAT_MODIFIER
CONTROL
DAMAGE_OVER_TIME
HEAL_OVER_TIME
IMMUNITY
TARGETING_RULE
MOVEMENT_RULE
MARK
```

Barrier·health floor·HP-loss redirection은 일반 status stacking이 아니라 `ProtectionIntent / ProtectionInstance`가 소유한다.

### Stacking Policy

각 status definition은 정확히 하나를 선언한다.

```text
REPLACE_IF_STRONGER
REFRESH_DURATION
ADD_STACKS_CAPPED
INDEPENDENT_BY_SOURCE
EXCLUSIVE_GROUP
```

- `REPLACE_IF_STRONGER`: 비교 key가 명시되지 않으면 invalid.
- `REFRESH_DURATION`: stack 수를 자동 증가시키지 않는다.
- `ADD_STACKS_CAPPED`: exact cap은 parameter data가 소유한다.
- `INDEPENDENT_BY_SOURCE`: source별 instance를 분리한다.
- `EXCLUSIVE_GROUP`: 우선순위·교체 이유 event를 남긴다.

### Duration·Expiry

```text
ACTIVE_INTERVAL = [start_tick, end_tick_exclusive)
EXPIRY = R00 when end_tick_exclusive <= current_tick
```

DoT·HoT pulse는 status duration을 암묵적으로 프레임 delta로 나누지 않는다. 명시된 due tick마다 R70/R80 intent를 생성한다.

### Dispel·Immunity

- Dispel은 status family 또는 tag filter를 명시한다.
- status immunity는 hidden boss exception이 아니라 공개 data다.
- immunity로 거부된 status도 `STATUS_REJECTED_IMMUNE` event를 남긴다.
- owner 사망 시 제거되는 status와 남는 world effect는 cleanup policy를 명시한다.

## 13. Event·Metric Contract

필수 event family:

```text
DAMAGE_INTENT_CREATED
DAMAGE_REJECTED
DAMAGE_MODIFIED
CHANNEL_MITIGATION_APPLIED
BARRIER_APPLIED
BARRIER_CONSUMED
BARRIER_EXPIRED
HP_LOSS_REDIRECTED
HEALTH_FLOOR_CLAMPED
HP_LOSS_APPLIED
RESTORE_APPLIED
OVERHEAL_DISCARDED
STATUS_APPLIED
STATUS_REFRESHED
STATUS_STACKED
STATUS_REPLACED
STATUS_REJECTED
STATUS_EXPIRED
STATUS_DISPELLED
DEATH_PENDING
```

raw damage와 resolved HP loss를 같은 metric에 중복 집계하지 않는다.

```text
RAW_DAMAGE != POST_MITIGATION_DAMAGE != BARRIER_ABSORBED != FINAL_HP_LOSS
```

모든 event는 `root_effect_id`, source, target, channel/tag, tick·phase·sequence를 추적한다. 배치 유닛이면 `deployment_id`까지 역추적한다.

## 14. UX·접근성 경계

- KINETIC·ARCANE은 아이콘·문자 라벨을 제공하며 색상만으로 구분하지 않는다.
- Armor·Resistance는 서로 다른 아이콘과 툴팁을 사용한다.
- Barrier는 HP bar와 분리된 임시 구간으로 표시한다.
- immunity·invalid target·barrier absorption·health floor는 combat log 원인에 나타난다.
- 세 전선 전체를 동시에 보는 PC-first 화면에서 상성 아이콘을 과도하게 늘리지 않는다.
- 모바일 검토 시에도 두 채널 구조를 유지하고 UI 밀도만 별도 조정한다.

## 15. 벤치마크·현업 비교

### Teamfight Tactics

Riot의 공식 Roles·Item 문서는 Armor와 Magic Resistance를 분리된 방어 stat으로 사용하며 role 정보와 damage type을 플레이어가 inspect할 수 있게 한다.

- 참고: `https://teamfighttactics.leagueoflegends.com/en-us/news/game-updates/roles-revamped-and-item-changes/`
- 채택: 두 방어축과 읽을 수 있는 아이콘·정보.
- 비채택: 아이템 조합 중심의 복잡한 상성·관통·혼합 damage 메타.

### Guild Wars 2 Barrier

Guild Wars 2 Wiki는 barrier를 실제 HP 전에 피해를 흡수하는 임시 health buffer로 설명하고 UI에서 HP와 분리해 표시한다.

- 참고: `https://wiki.guildwars2.com/wiki/Barrier`
- 채택: HP와 분리된 임시 budget·명확한 UI·cap 필요성.
- 비채택: 외부 게임의 지속시간·cap 수치 직접 복사.

### Overwatch Barrier Tuning

Overwatch 공식 2019-12 patch note는 barrier에 소비하는 시간이 전투 pace를 지배하자 barrier health를 줄이고 다른 영웅 능력을 보완한 제작 의도를 설명한다.

- 참고: `https://overwatch.blizzard.com/news/patch-notes/live/2019/12`
- 채택: barrier 상시 유지가 전투 선택과 pace를 대체하면 stop-ship.
- 비채택: shooter용 barrier 수치와 실시간 조작 계약.

### 생산 비교

| 접근 | 제작비 | QA 조합 | 플레이어 해석 | OMENWARD 판정 |
|---|---:|---:|---|---|
| 단일 channel | 낮음 | 낮음 | 쉬우나 병종·공세 대응이 평평해짐 | 기각 |
| 2 channel + 독립 tag | 중간 | 관리 가능 | Armor/Resistance 대응과 delivery 의미가 분리됨 | 채택 |
| 3+ channel + true/execute | 높음 | 급증 | 세 릴·세 전선 판단을 상성 암기가 덮을 위험 | 기각/후속 승인 필요 |

## 16. 적대적 검토

| Audit ID | 공격 | 판정·대응 |
|---|---|---|
| `OMW-AUD-233` | damage channel과 AREA·DOT·SIEGE를 섞어 enum 폭증 | channel과 delivery/target tag 완전 분리 |
| `OMW-AUD-234` | FLYING을 damage type으로 취급 | movement/target eligibility로만 사용 |
| `OMW-AUD-235` | barrier가 HP·heal·defense와 중복 계산 | post-mitigation temporary budget으로 고정 |
| `OMW-AUD-236` | HP-loss sharing이 재귀 loop를 생성 | transfer depth 1·recursive 금지 |
| `OMW-AUD-237` | transferred loss가 방어를 다시 통과해 이중 감소 | second mitigation pass 금지 |
| `OMW-AUD-238` | same-tick control이 이미 commit된 행동을 소급 취소 | 일반 status는 다음 relevant phase부터 적용 |
| `OMW-AUD-239` | status stacking 규칙 누락으로 data별 임의 동작 | definition별 stacking policy 필수 |
| `OMW-AUD-240` | boss·building에 hidden immunity 예외 | immunity filter와 rejection event 공개 |
| `OMW-AUD-241` | heal을 negative damage로 처리해 trigger·metric 오염 | RestoreIntent 분리 |
| `OMW-AUD-242` | true damage·execute·revive가 세 전선 대응을 우회 | 현 slice 금지·추가 시 새 Decision |
| `OMW-AUD-243` | objective가 일반 공격에 우발적으로 파괴 | Objective HP target 기본 금지 |
| `OMW-AUD-244` | barrier 상시 유지가 병종·전선 선택을 대체 | cap·duration numeric Gate와 stop-ship |
| `OMW-AUD-245` | channel을 색상만으로 표시해 접근성 실패 | 아이콘·문자 라벨 필수 |
| `OMW-AUD-246` | raw damage와 final HP loss를 이중 집계 | event·metric 단계 분리 |

## 17. 검증 계약

```text
T0:
  exactly-one damage channel
  valid delivery tags and target profile
  ProtectionIntent/StatusApplicationIntent required fields
  stacking policy and expiry semantics

T1:
  same fixture/input/RNG에서 modifier·mitigation·barrier·redirect·status event parity

T2:
  no true/execute/revive
  no recursive transfer or second mitigation
  no retroactive same-tick status cancellation
  barrier != HP/heal
  objective damage eligibility
  raw/resolved metric separation

T3:
  KINETIC/ARCANE threat family와 Armor/Resistance 대응을 포함한 paired A/B/C
  barrier uptime·absorbed amount·final HP loss·other-two-lane contribution 기록
```

현재는 Red test 파일을 만들거나 simulation을 실행하지 않는다.

## 18. 경계·다음 Gate

```text
CURRENT_PRODUCT = LEGACY_PROTOTYPE
DAMAGE_PROTECTION_STATUS_SEMANTICS = USER_APPROVED_DOCUMENTED_NOT_IMPLEMENTED
PRODUCT_CODE = UNCHANGED
SIMULATION_TOOL_CODE = NOT_AUTHORIZED
DAMAGE_CHANNELS = KINETIC_AND_ARCANE
TRUE_DAMAGE_EXECUTE_REVIVE = FORBIDDEN_CURRENT_SLICE
EXACT_MITIGATION_FORMULA = PENDING
EXACT_ARMOR_RESISTANCE_DEFAULTS = PENDING
EXACT_BARRIER_BUDGET_CAP_DURATION = PENDING
EXACT_STATUS_STACK_CAP_DURATION = PENDING
EXACT_TICK_RATE_AND_ACTIVATION_POLICY = PENDING
EXACT_HERO_TRIGGER_TIMER_EFFECT_VALUES = PENDING
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
```

```text
GRILL_ME_COUNT = 3/10
NEXT_DECISION = OMW-DEC-20260803-VALIDATION-MITIGATION-FORMULA-AND-PROTECTION-NUMERIC-DEFAULTS-V1
NEXT_PREFLIGHT = AT_10_OF_10
```
