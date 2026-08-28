# [현행] OMENWARD 전진기지 고정 방어와 점령 건설 노드 계약

```yaml
decision_id: OMW-PLAN-20260828-FORWARD-DEFENSE-OCCUPATION-NODES-01
approved_at: 2026-08-28 KST
approval: USER_APPROVED
status: CONFIRMED__PLANNING_ONLY__NOT_IMPLEMENTED
planning_contract: PROJECT_TOTAL_PLANNING_IMPLEMENTATION_AND_DELIVERY_INSTRUCTION_v4.8
scope: STAGE1_FTUE / FORWARD_BASE_FIXED_DEFENSE / OCCUPATION_CONSTRUCTION_NODE
amended_at: 2026-08-28 KST
amended_by: OMW-PLAN-20260828-BASE-FORWARD-BATTLEFIELD-CONSTRUCTION-LAYOUT-01
current_capacity_owner: docs/design/APPROVED_OMENWARD_BASE_FORWARD_BATTLEFIELD_CONSTRUCTION_LAYOUT_2026-08-28.md
product_code_authority: NONE
simulation: NOT_RUN
runtime: NOT_RUN
human_validation: NOT_RUN
```

## 1. 결정 요약

전진기지는 한 개의 포탑만 있는 장식이 아니다. 플레이어가 전진기지를 읽을 때 **시간을 버는 바리케이드**, **지속 화력을 주는 자동공격탑**, 그리고 **거점을 안정적으로 점령했을 때 선택권을 여는 건설 노드**를 구분해야 한다.

```text
FORWARD_BASE_DEFENSE_STACK = BARRICADE + AUTO_ATTACK_TOWER
BARRICADE_RUNTIME_ID = FORWARD_BARRICADE
TACTICAL_COMMAND_BARRICADE_RUNTIME_ID = TACTICAL_COMMAND_BARRICADE
BARRICADE_IDENTITY_COLLISION = FORBIDDEN
BARRICADE_ROLE = PREDICTABLE_FIRST_PRESSURE_BUFFER
AUTO_ATTACK_TOWER_ROLE = LANE_LOCAL_AUTOMATIC_DAMAGE_SUPPORT
OCCUPATION_NODE_ROLE = CONTROLLED_OUTPOST_BUILD_CHOICE
FIXED_DEFENSE_CAPTURE_POWER = 0
FIXED_DEFENSE_SOLO_CLEAR = FORBIDDEN
```

바리케이드와 자동공격탑은 전진기지에 이미 배치된 **고정 방어 시설**이다. 건설 노드는 별도의 **플레이어 선택형 건설 자리**이며, 고정 방어 시설을 다시 건설하는 버튼이나 Stage 1의 직접 건설 과제가 아니다.

기존 문서의 금화 소모형 전술 명령 `바리케이드`는 전장에 일시 설치하는 `TACTICAL_COMMAND_BARRICADE`다. 새 `FORWARD_BARRICADE`는 전진기지에 고정된 방어 시설이므로 두 시스템의 데이터 ID·수명·소유권·UI 진입점은 공유하지 않는다.

## 2. Player Promise와 핵심 경험

```text
전진기지 방어
→ 바리케이드가 적의 첫 압력을 지연
→ 자동공격탑이 그 시간에 전투 지원
→ 플레이어 병력·룰렛 결과·전술이 실제 승부를 결정
→ 거점을 안정적으로 확보하면 건설 노드가 열림
→ 다음 전선을 위한 원하는 해금 건물을 선택
```

- **대표 행동:** 어느 전선에 병력을 비가역 커밋할지 결정하고, 확보한 거점의 노드에 어떤 건물을 넣을지 선택한다.
- **의미 있는 고민:** 즉시 전투 보강을 위해 위험한 전선을 지킬지, 안정적으로 확보한 거점의 장기 생산·확률·지원 가치를 키울지 판단한다.
- **관찰 가능한 결과:** 바리케이드의 저지, 탑의 표적·피해, 노드의 잠금/해금, 건물 효과의 활성/비활성이 전선 상태와 함께 보인다.
- **실패 학습:** 고정 방어만으로는 점령도 승리도 만들 수 없으므로, 병력 커밋·룰렛 설계·제한 전술의 인과를 복기한다.

## 3. 시스템 계약

### 3.1 바리케이드

```text
SYSTEM_ID = SYS-FORWARD-BARRICADE-01
BARRICADE_RUNTIME_ID = FORWARD_BARRICADE
BARRICADE_FUNCTION = DELAY_AND_ABSORB_FIRST_PRESSURE
BARRICADE_ATTACK = NONE
BARRICADE_CAPTURE_CONTRIBUTION = 0
BARRICADE_REWARD_GENERATION = NONE
BARRICADE_NUMERICS = PENDING_SIMULATION
```

- 적의 첫 진입 압력을 예측 가능하게 늦추고 일부 피해를 흡수한다.
- 아군의 핵심 병력, 룰렛 결과, 전술 명령을 대체하지 않는다.
- 처치 보상·점령력·룰렛 TokenSource를 만들지 않는다.
- 체력, 저지 시간, 통과 규칙, 파괴 연출은 simulation과 Phase 2 구현 계약에서 정한다.

### 3.2 자동공격탑

```text
SYSTEM_ID = SYS-AUTO_ATTACK_TOWER-01
AUTO_ATTACK_TOWER_FUNCTION = LANE_LOCAL_AUTOMATIC_DAMAGE_SUPPORT
AUTO_ATTACK_TOWER_CAPTURE_CONTRIBUTION = 0
AUTO_ATTACK_TOWER_SOLO_CLEAR = FORBIDDEN
AUTO_ATTACK_TOWER_NUMERICS = PENDING_SIMULATION
```

- 해당 전선의 적에게 자동으로 공격 지원을 제공한다.
- 점령력은 없으며, 유닛 커밋과 전술 판단을 대체하지 않는다.
- 표적 우선순위, 사거리, 공격력, 재장전, 피해 유형은 아직 확정하지 않는다.
- 기존 방어탑의 T2 전문화(`ARTILLERY / DEFENSE_ENHANCEMENT / SNIPER`) 계보는 유지한다. 다만 이 T1 고정탑의 정확한 수치와 런타임 동작은 본 문서로 구현 완료가 되지 않는다.

### 3.3 고정 방어의 소유·점령 전환

```text
FIXED_DEFENSE_OWNER = CURRENT_STABLE_OUTPOST_OWNER
FIXED_DEFENSE_ACTIVE = STABLE_OWNER_ONLY
FIXED_DEFENSE_DURING_CAPTURE = DISABLED
FIXED_DEFENSE_AFTER_HOSTILE_CAPTURE = STABLE_NEW_OWNER_RESTORED
FIXED_DEFENSE_TRANSITION_RUNTIME = NOT_IMPLEMENTED
FORWARD_DEFENSE_RUNTIME = NOT_IMPLEMENTED
```

- 본진과 전진기지는 양 진영에 같은 구조 언어를 사용한다. 수량 owner는 `APPROVED_OMENWARD_BASE_FORWARD_BATTLEFIELD_CONSTRUCTION_LAYOUT_2026-08-28.md`다. 본진에는 진영당 고정탑 2개·패드 4개, 전진기지에는 기지당 고정탑 1개·패드 2개가 있다.
- 거점이 중립화·점령·안정화 중이면 고정 방어는 작동하지 않는다.
- 상대가 점령을 완료하고 안정화되면 그 거점의 고정 방어는 새 안정 소유자를 위해 복구된다.
- 이 규칙은 **계획 계약**이다. 현재 코드에는 바리케이드/자동공격탑의 런타임 소비자가 없으므로 `NOT_IMPLEMENTED`다.

### 3.4 점령 건설 노드

```text
SYSTEM_ID = SYS-OCCUPATION-NODE-01
OCCUPATION_NODE_ACTIVATION = STABLE_PLAYER_OWNED_OUTPOST_ONLY
CONSTRUCTION_NODE_CAPACITY_PER_FORWARD_BASE = 2
CONSTRUCTION_NODE_BUILD_OPTIONS = UNLOCKED_APPROVED_BUILDING_ROSTER
CONSTRUCTION_NODE_DURING_CAPTURE = LOCKED
PLAYER_BUILT_EFFECTS_WHILE_NOT_OWNED = DISABLED
PLAYER_BUILT_EFFECTS_AFTER_HOSTILE_CAPTURE = RUINED
```

- 노드는 플레이어가 안정적으로 점령한 거점에서만 활성화된다.
- 점령 과정(중립화·점령·안정화)에는 건설할 수 없다.
- 한 노드는 한 건물 자리이며, 선택지는 해금된 승인 건물 roster 중 해당 비용·고유 제한·노드 조건을 만족하는 것뿐이다.
- 현재 실행 가능한 구현 roster는 `BARRACKS / TOWER / FARM` 세 종류다. 7종 계획 roster를 실제 구현됐다고 주장하지 않는다.
- 플레이어 소유가 아니면 그 노드 건물의 효과는 비활성화되며, 적의 점령이 완료되면 폐허가 된다. 재점령·안정화 뒤에 다시 건설할 수 있다.

## 4. Stage 1 FTUE 연결

Stage 1은 직접 건설을 요구하지 않는다. 본진 4개·전진기지당 2개의 패드는 보이지만 잠겨 있으며, 다음 **세 가지 설명 단위**로 전장 역할을 읽게 한다.

```text
1. 본진 지휘·방어: 고정탑 2개는 접근을 보조하지만 승리를 만들지 않음
2. 전진기지 방어 체계: 바리케이드 + 자동공격탑 + 미래 건설 패드 2개
3. 3×3 룰렛: 결과를 제한적으로 수정하고 한 전선에 비가역 커밋
```

```text
STAGE_1_DIRECT_CONSTRUCTION = FORBIDDEN
STAGE_1_WARD_CITADEL_PREBUILT_PRODUCTION_BUILDINGS = NONE
STAGE_1_VISIBLE_HOME_CONSTRUCTION_NODES = 4
STAGE_1_VISIBLE_FORWARD_CONSTRUCTION_NODES_PER_BASE = 2
STAGE_1_FORWARD_BASE_DEFENSE_SYSTEM = BARRICADE x1 + AUTO_ATTACK_TOWER x1 PER_WARD_FORWARD_BASE
FIRST_ROULETTE_UNLOCK = AFTER_THREE_EXPLANATION_UNITS
FIRST_MEANINGFUL_BUILD_OR_UPGRADE = STAGE_2_T2_UPGRADE
```

점령 건설 노드는 Stage 1의 필수 교습이 아니다. Stage 2 이후, 플레이어가 거점을 실제로 안정화시켜 확보했을 때만 지도 장악의 보상·선택 비용으로 드러난다.

## 5. UI·피드백 계약

| 요소 | 플레이어가 읽어야 하는 정보 | 피드백 |
|---|---|---|
| 바리케이드 | 남은 저지력/상태, 보호하는 전진기지 | 맞음·균열·붕괴가 한 전선의 첫 압력 변화를 명확히 보임 |
| 자동공격탑 | 현재 표적, 사거리 안의 위협, 공격 상태 | 표적선·발사·명중이 병력 전투와 구분되되 과장되지 않음 |
| 건설 노드 | 안정 점령 여부, 잠긴 이유, 설치 가능 건물·비용·제한 | 안정화 완료 시 열림; 점령 시작 시 잠김; 적 점령 완료 시 건물은 폐허 상태 |

화면의 긴 설명문이나 이미지 속 pseudo-text는 정본이 아니다. 정확한 규칙·비용·상태 명칭은 이 문서와 추후 구조화 데이터가 소유한다.

## 6. 실제 구현 대조

| 항목 | 실제 근거 | 판정 |
|---|---|---|
| 안정화된 플레이어 소유 거점에서만 노드 건설 | `scripts/buildings/building_service.gd`, `scripts/battle/outpost_state.gd`, headless economy tests | IMPLEMENTED / AUTOMATED_EVIDENCE_EXISTS |
| 점령 중 노드 잠금, 적 점령 뒤 효과 비활성·폐허, 재점령 뒤 재건 | `scripts/buildings/building_service.gd`, `tests/headless/c2_battle_objective_test.gd` | IMPLEMENTED / AUTOMATED_EVIDENCE_EXISTS |
| 현 구현 건물 roster | `BARRACKS / TOWER / FARM` | IMPLEMENTED / LIMITED_ROSTER |
| 바리케이드 고정 방어 | 런타임 consumer 없음 | NOT_IMPLEMENTED |
| 자동공격탑의 전투 지원 | 런타임 consumer 없음 | NOT_IMPLEMENTED |
| 새 전략 지도 topology에 이 계약을 표현 | 현재 런타임은 이전 parallel lane 성격 | NOT_IMPLEMENTED |
| 사람 플레이에서 이해 가능성 | human/player evidence 없음 | NOT_RUN |

## 7. 구현 전 검증 계약

Phase 2가 별도 Issue와 RED 테스트로 열리기 전에는 Scene·Resource·code·asset을 만들거나 적용하지 않는다. 열릴 경우 최소한 다음을 검증한다.

```text
TEST_BARRICADE_DELAYS_FIRST_PRESSURE_WITHOUT_ATTACK_OR_CAPTURE_POWER
TEST_AUTO_ATTACK_TOWER_SUPPORTS_LOCAL_FRONT_WITHOUT_SOLO_CLEAR_OR_CAPTURE_POWER
TEST_FIXED_DEFENSE_DISABLES_DURING_CAPTURE_AND_RESTORES_FOR_STABLE_OWNER
TEST_OCCUPATION_NODE_REJECTS_NEUTRAL_CAPTURING_AND_STABILIZING_OUTPOST
TEST_OCCUPATION_NODE_ACCEPTS_STABLE_PLAYER_OWNED_OUTPOST
TEST_PLAYER_BUILDING_EFFECT_DISABLES_ON_CONTROL_LOSS_AND_RUINS_AFTER_HOSTILE_CAPTURE
TEST_STAGE1_EXPLAINS_COMMAND_ROOT_FORWARD_DEFENSE_AND_LOCKED_NODE_CAPACITY_BEFORE_ROULETTE
```

Human verification must show that a first-session player can name the difference between “time”, “damage support”, and “future building choice” before any `PASS` claim.

## 8. Supersession, risks, and provenance

```text
SUPERSEDES = FORWARD_TOWER_FUNCTIONAL_EFFECT_UNDECIDED
SUPERSEDES = VEIL_FORWARD_TOWER_VISUAL_SYMMETRY_UNDECIDED
SUPERSEDED_IN_SCOPE = SINGLE_CONSTRUCTION_NODE_CAPACITY
RETAINS = STAGE_1_DIRECT_CONSTRUCTION_FORBIDDEN
RETAINS = FIRST_MEANINGFUL_BUILD_OR_UPGRADE_STAGE_2_T2_UPGRADE
RETAINS = DEFENSE_TOWER_T2_ARTILLERY_DEFENSE_ENHANCEMENT_SNIPER
NO_BASE_PROMOTION = PROJECT_SPECIFIC_MAPRUN_FRONT_AND_OUTPOST_RULES
```

- `APPROVED_OMENWARD_BUILDING_TIER_REALIGNMENT_2026-08-06.md`의 Stage 1 six-T1 직접 건설 문구는 이미 `OMW-PLAN-20260828-STAGE1-PREBUILT-EXPLAIN-01`에 의해 **Stage 1 범위에서만** supersede됐다. 그 문서의 Tier 2 분기 계보는 유지한다.
- 방어 수치·비용·표적 규칙은 simulation 전 확정하지 않는다.
- 새 시각 방향은 별도 Visual Decision의 storybook watercolor SD 문법을 따른다. 이 문서는 이미지·runtime asset·권리 PASS를 만들지 않는다.
- 외부 게임 표현이나 첨부 레퍼런스의 고유 표현을 제품 자산으로 복제하지 않는다.

## 9. Incident / Solution / Lesson

```text
INCIDENT = STAGE1_PREBUILT_FORWARD_TOWER_WAS_EXPLAINED_BUT_PLAYER_VALUE_WAS_UNSPECIFIED
SOLUTION = SPLIT_FIXED_DEFENSE_INTO_BARRICADE_AND_AUTO_ATTACK_TOWER_AND_SEPARATE_OCCUPATION_NODE
LESSON = A_STATIC_MAP_PROP_MUST_STATE_ITS_PLAYER_DECISION_AND_CONTROL_LIFECYCLE_BEFORE_VISUAL_OR_RUNTIME_WORK
BASE_PROMOTION = NO_BASE_PROMOTION__PROJECT_SPECIFIC_FRONT_STRUCTURE
```
