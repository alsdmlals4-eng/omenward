# [현행] OMENWARD 본진·전진기지 전장 건설 배치 계약

```yaml
decision_id: OMW-PLAN-20260828-BASE-FORWARD-BATTLEFIELD-CONSTRUCTION-LAYOUT-01
approved_at: 2026-08-28 KST
approval: USER_APPROVED_IN_CHAT
status: CONFIRMED__PLANNING_ONLY__NOT_IMPLEMENTED
planning_contract: PROJECT_TOTAL_PLANNING_IMPLEMENTATION_AND_DELIVERY_INSTRUCTION_v4.8
scope: THREE_FRONT_BATTLEFIELD_LAYOUT / HOME_BASE_DEFENSE / CONSTRUCTION_NODE_CAPACITY / STAGE1_FTUE_RESEQUENCING
supersedes_in_scope:
  - OMW-PLAN-20260828-STAGE1-PREBUILT-EXPLAIN-01__HOME_BARRACKS_AND_FARM_VISUAL_FACILITIES
  - OMW-PLAN-20260828-FORWARD-DEFENSE-OCCUPATION-NODES-01__SINGLE_NODE_CAPACITY_ONLY
product_code_authority: NONE
runtime: NOT_RUN
human_validation: NOT_RUN
player_experience_validation: NOT_RUN
```

## 1. 사용자 승인 구조

본진은 더 이상 병영·농장 같은 **사전 구축 생산 건물 묶음**으로 보이지 않는다. 양 진영의 본진은 한 개의 지휘 표식과 고정 방어탑, 앞으로 선택할 수 있는 건설 자리만 남긴 **방어 가능한 지휘 거점**이다. 양쪽은 같은 구조 수를 쓰되, Ward/Veil의 형태·색·VFX 언어만 다르다.

```text
MAP_TOPOLOGY = ONE_WARD_CITADEL_ROOT__THREE_SHARED_FRONTS__ONE_VEIL_CITADEL_ROOT
HOME_BASE_PREBUILT_PRODUCTION_BUILDINGS = NONE
HOME_BASE_ROLE = DEFENDED_COMMAND_ROOT
HOME_BASE_CONSTRUCTION_NODE_COUNT_PER_FACTION = 4
HOME_BASE_FIXED_AUTO_ATTACK_TOWER_COUNT_PER_FACTION = 2
FORWARD_BASE_COUNT_PER_FACTION = 3
FORWARD_BASE_CONSTRUCTION_NODE_COUNT_PER_BASE = 2
FORWARD_BASE_FIXED_AUTO_ATTACK_TOWER_COUNT_PER_BASE = 1
FORWARD_BASE_FIXED_DEFENSE_STACK = FORWARD_BARRICADE + AUTO_ATTACK_TOWER
TOTAL_CONSTRUCTION_NODE_CAPACITY_PER_FACTION = 10
TOTAL_CONSTRUCTION_NODE_CAPACITY_MAPRUN = 20
```

### 1.1 노드·고정 방어·기존 생산 시스템의 구분

| 요소 | 본진 | 전진기지 | 플레이어에게 보이는 의미 |
|---|---:|---:|---|
| 건설 노드 | 4 | 2 | 비어 있는 선택형 건설 자리. 한 노드에는 승인된 건물 하나만 설치한다. |
| 자동공격탑 | 2 | 1 | 이미 있는 방어 지원. 점령력·처치 보상·단독 승리를 만들지 않는다. |
| 고정 바리케이드 | 없음 | 1 | 첫 압력을 지연하는 전진기지 전용 고정 방어. |
| 병영·농장 외형 | 없음 | 없음 | Stage 1의 지도를 건물 설명 보드로 만들지 않는다. |

`FORWARD_BARRICADE`는 `TACTICAL_COMMAND_BARRICADE`와 데이터 ID·수명·UI 진입점이 다르다. 고정탑과 고정 바리케이드는 플레이어의 노드 건설로 다시 사거나 교체하는 시설이 아니다.

```text
BARRICADE_IDENTITY_COLLISION = FORBIDDEN
FIXED_DEFENSE_CAPTURE_CONTRIBUTION = 0
FIXED_DEFENSE_SOLO_CLEAR = FORBIDDEN
HOME_BASE_FIXED_DEFENSE_ROLE = ROOT_APPROACH_SUPPORT__NO_CAPTURE_POWER
HOME_BASE_FIXED_DEFENSE_NUMERICS = PENDING_SIMULATION
```

### 1.2 공간 배치 문법

- 양쪽 본진의 지휘 표식에서 상·중·하 세 branch가 **실제로 갈라져** 나간다. 병렬 도로 세 줄이나 본진 세 개로 읽히면 실패다.
- 각 본진의 네 노드는 지휘 표식 주변의 서로 다른 빈 건설 패드로 보인다. 본진을 성채 건물 군집으로 바꾸지 않는다.
- 각 전진기지는 route outpost이며, 바리케이드와 탑 한 개를 중심으로 두 개의 빈 건설 패드가 붙는다.
- 접전지는 전진기지보다 넓고, 작은 병력 군집·엄폐물·파편·연기·마법 흔적이 있어야 한다. 전장 크기를 키우고 유닛을 작게 그려 세 전선의 상태를 한 프레임에서 읽게 한다.
- 본진과 전진기지의 경계는 울타리·토루·깃발·진영색을 이용한 **간단한 경계감**만 쓴다. 별도의 거대 성벽, 건물 군집, 원형 미니요새를 만들지 않는다.

## 2. 핵심 경험과 선택의 연결

```text
징조 관측
→ 현재 세 전선의 압력과 확보한 건설 수용량을 비교
→ 룰렛 결과와 제한 조작으로 병력을 얻음
→ 한 전선에 비가역 커밋
→ 병력·고정 방어·제한 전술이 접전지를 버티거나 밀어 냄
→ 안정 점령한 전진기지의 두 노드가 다음 설계 선택으로 열림
→ 결과를 복기하고 다음 Stage의 분포를 다시 설계
```

- **의미 있는 고민:** 위험한 전선을 즉시 지킬 것인가, 안정 점령해 연 두 노드에 장기적인 TokenSource·수용량·방어 지원 중 무엇을 둘 것인가.
- **관찰 가능한 결과:** 두 전진기지 건설 패드의 잠금/해금, 고정 바리케이드의 지연, 탑의 보조 화력, 점령 중 비활성화, 적 점령 완료 뒤 폐허화가 지도에 구분되어 보인다.
- **실패 학습:** 탑·바리케이드가 시간을 벌어도 병력 커밋과 룰렛 설계가 틀리면 접전지를 잃는다. 실패는 “방어물이 약하다”가 아니라 “언제·어디에 설계와 병력을 썼는가”로 복기된다.

## 3. Stage 1 FTUE 재정렬

Stage 1은 직접 건설을 요구하지 않는다. 본진의 네 패드와 전진기지의 두 패드는 **보이지만 잠긴 미래 선택**으로 표시한다. 따라서 첫 룰렛과 비가역 커밋을 늦추지 않는다.

```text
STAGE_1_DIRECT_CONSTRUCTION = FORBIDDEN
STAGE_1_WARD_CITADEL_PREBUILT_PRODUCTION_BUILDINGS = NONE
STAGE_1_VISIBLE_HOME_CONSTRUCTION_NODES = 4
STAGE_1_VISIBLE_FORWARD_CONSTRUCTION_NODES_PER_BASE = 2
STAGE_1_NODE_INTERACTION_STATE = VISIBLE_LOCKED__FIRST_MEANINGFUL_BUILD_STAGE_2
STAGE_1_FIXED_DEFENSE_EXPLANATION = HOME_TOWERS__THEN_FORWARD_BARRICADE_AND_TOWER
FIRST_ROULETTE_UNLOCK = AFTER_THREE_EXPLANATION_UNITS
FIRST_MEANINGFUL_BUILD_OR_UPGRADE = STAGE_2_T2_UPGRADE
```

설명 단위는 다음 세 개다.

1. **본진의 지휘·방어:** 본진은 생산 건물 집합이 아니라 잃으면 MapRun이 끝나는 지휘 거점이며, 두 고정탑은 접근을 보조할 뿐 승리를 만들지 않는다.
2. **전진기지의 시간과 화력:** 바리케이드가 첫 압력을 늦추고 탑이 한 전선에 보조 화력을 준다. 두 건설 패드는 나중에 안정 점령의 보상으로 열린다.
3. **건설 패드와 징조륜:** 빈 패드는 미래 분포를 바꾸는 선택 자리이고, 이번 Stage에는 건설 대신 3×3 징조륜·전선 커밋으로 인과를 먼저 경험한다.

기존 Stage 1의 `GENERAL_BARRACKS x1 + FARM x1`은 **본진에 보이는 사전 구축물이라는 의미에서만** supersede된다. 기존 MapRun 시작 자원·병력 한도·초기 룰렛 가능 여부가 본진 건물의 시각 삭제만으로 사라진다고 가정하지 않는다.

```text
STAGE_1_STARTING_MOBILIZATION_AND_CAPACITY = EXISTING_MAPRUN_BASELINE__NOT_A_VISIBLE_BUILDING
STARTING_BASELINE_TUNING = RETAINED__REQUIRES_PHASE2_RECONCILIATION_BEFORE_RUNTIME_CHANGE
```

## 4. 점령·소유 상태 계약

| 지점 | 정상 소유 | 점령 중 | 적 점령 완료 뒤 | Stage 1 |
|---|---|---|---|---|
| 플레이어 본진 노드 | 보유하되 Stage gate에 따라 잠금/해금 | 본진 점령 상태를 만들지 않음 | MapRun 종료 경계는 별도 전투 규칙 | 4개 표시·잠김 |
| 플레이어 전진기지 노드 | 안정 소유 + Stage gate 통과 시 사용 가능 | 잠김 | 기존 건물 폐허, 재안정화 뒤 재건 | 2개씩 표시·잠김 |
| Veil 전진기지 노드 | 적 소유에서는 플레이어가 사용 불가 | 잠김 | 플레이어가 안정화 완료하면 새 빈 노드로 사용 가능 | 적 소유·잠김 |
| Veil 본진 노드 | 적 소유, 플레이어 사용 불가 | 본진 점령 상태를 만들지 않음 | MapRun 종료 경계 | 4개 표시·잠김 |

`OCCUPATION_NODE_ACTIVATION = STABLE_PLAYER_OWNED_OUTPOST_ONLY`는 전진기지에 유지한다. 본진 네 노드의 전투 중 설치·손실·재건 규칙은 아직 구현/시뮬레이션되지 않았으므로, 현재는 **보이는 capacity와 Stage gate**만 확정한다.

## 5. 실제 구현 대조와 Phase 2 경계

| 항목 | actual code / data evidence | 판정 |
|---|---|---|
| 전진기지 여러 노드 등록 | `BuildingService.register_outpost(outpost_id, state, node_ids: Array)` | 구현 기반 존재; 2개 노드로 확장 가능 |
| 점령 중 잠금·적 점령 뒤 폐허 | `OutpostState`, `BuildingService`, `economy_roulette_test.gd`, `c2_battle_objective_test.gd` | 기존 전진기지 계약 일부 구현됨 |
| 본진 4노드 | `BaseState`에는 건설 노드/소유/잠금 모델 없음 | NOT_IMPLEMENTED |
| 본진 고정탑 2개 | `BattleSimulator`에는 본진 피해 상태만 있고 탑 consumer 없음 | NOT_IMPLEMENTED |
| 전진기지 고정 바리케이드/자동공격탑 | runtime combat consumer 없음 | NOT_IMPLEMENTED |
| 전략 지도에서 패드·탑·점령 상태 표현 | Run Command는 이전 UI/전장 표현 | NOT_IMPLEMENTED |
| 수치·밸런스·사람 가독성 | simulation / human test 없음 | NOT_RUN |

Phase 2는 별도 GitHub Issue, 승인된 implementation packet, RED 테스트, target-resolution GUI 검증이 있을 때만 열 수 있다.

```text
REQUIRED_PHASE2_TESTS =
  HOME_BASE_EXPOSES_EXACTLY_FOUR_CONSTRUCTION_NODES_PER_FACTION
  HOME_BASE_EXPOSES_EXACTLY_TWO_FIXED_TOWERS_PER_FACTION
  FORWARD_BASE_EXPOSES_EXACTLY_TWO_CONSTRUCTION_NODES_AND_ONE_FIXED_TOWER
  FIXED_DEFENSE_NEVER_GENERATES_CAPTURE_POWER_OR_SOLO_CLEAR
  STAGE1_SHOWS_ALL_NODE_CAPACITY_BUT_REJECTS_CONSTRUCTION
  STABLE_CAPTURE_UNLOCKS_FORWARD_NODE_CHOICE_ONLY
  STRATEGIC_MAP_REMAINS_LEGIBLE_AT_TARGET_RESOLUTIONS
PHASE_2_PRODUCT_CODE_AUTHORITY = NONE
```

## 6. 벤치마크 처분과 독자성

| Reference | 확인한 구조 | 처분 | OMENWARD 적용 / 미적용 |
|---|---|---|---|
| [Commander Quest](https://commanderquest.itch.io/commanderquest) | 카드/유닛 배치와 자동전투 사이의 전술적 전장 읽기 | ADAPT | 넓은 전장과 역할 실루엣만 참고; 카드 배치·전장 표현·고유 콘텐츠는 복제하지 않음 |
| [Thronefall](https://store.steampowered.com/app/2239150/Thronefall/) | 짧은 세션 안에서 건설과 방어의 trade-off를 읽게 하는 구조 | ADAPT | 빈 패드와 방어 결과의 관계만 채택; 일/야 리듬과 직접 영웅 전투는 채택하지 않음 |
| [Cataclismo](https://store.steampowered.com/app/1422440/Cataclismo/) | 자유형 성벽 조립이 별도 깊이·생산비를 만든다는 구조 | REJECT | 자유 배치·brick-by-brick 건설은 세 전선의 forecast/commit 판단을 가리고 제작 범위를 폭증시키므로 제외 |

```text
DIFFERENTIATION = PLAYER_CONSTRUCTED_PROBABILITY_ENGINE + IRREVERSIBLE_THREE_FRONT_COMMIT + OCCUPATION_UNLOCKED_NODE_CAPACITY
REFERENCE_COPYING = FORBIDDEN
```

조사일은 2026-08-28 KST다. 위 외부 사례는 구조 stress test일 뿐 권위가 아니며, 채택 여부는 이 계약과 protected product identity가 결정한다. UI 구현 가능성은 Godot의 [Custom GUI Controls](https://docs.godotengine.org/en/stable/tutorials/ui/custom_gui_controls.html)와 [Control 입력 경계](https://docs.godotengine.org/en/stable/classes/class_control.html)도 대조했다. target-resolution에서 단일 전략 지도 위의 node hover/focus/선택 처리는 가능하지만, 현재 프로젝트에는 본진 node State나 해당 Control consumer가 없으므로 Phase 2 전에는 `NOT_IMPLEMENTED`다.

## 7. 리스크와 검증 순서

1. 본진 패드 네 개가 선택지를 과도하게 보이게 하지 않는지 target-resolution mock/runtime에서 검증한다.
2. 고정 방어가 병력·룰렛·전술의 중요성을 침식하지 않는지 시뮬레이션한다.
3. Stage 1에서 “잠긴 패드”가 눌러야 하는 과제로 오해되지 않는지 사람 플레이로 검증한다.
4. 실제 본진 모델·전진기지 노드 목록·UI interaction을 동일 Resource/State contract로 연결한다.

```text
NUMERICS = PENDING_SIMULATION
TARGET_RESOLUTION_READABILITY = NOT_RUN
HUMAN_USABILITY = NOT_RUN
PLAYER_EXPERIENCE = NOT_RUN
NO_BASE_PROMOTION = PROJECT_SPECIFIC_THREE_FRONT_ROOT_AND_OCCUPATION_CAPACITY_LAYOUT
```

## 8. Incident / Solution / Lesson

```text
INCIDENT = HOME_BASE_WAS_VISUALLY_SPECIFIED_AS_PREBUILT_BARRACKS_AND_FARM_AFTER_USER_REMOVED_HOME_BUILDINGS
SOLUTION = REMOVE_VISIBLE_HOME_PRODUCTION_BUILDINGS_AND_DEFINE_HOME_AS_COMMAND_ROOT_WITH_4_EMPTY_NODES_AND_2_FIXED_TOWERS
LESSON = VISUAL_REMOVAL_OF_A_FACILITY_MUST_EXPLICITLY_SEPARATE_MAP_PRESENTATION_FROM_EXISTING_STARTING_SYSTEM_EFFECTS_AND_RUNTIME_MODEL_GAPS
```

이 문서는 제품 자산 승인, Godot 적용, 수치 승인, Human usability / Player Experience PASS를 뜻하지 않는다.
