# [현행] OMENWARD 열린 전장·전진기지 탑 전용 배치 계약

```yaml
decision_id: OMW-PLAN-20260828-OPEN-BATTLEFIELD-TOWER-ONLY-01
approved_at: 2026-08-28 KST
approval: USER_APPROVED_IN_CHAT
status: CONFIRMED__PLANNING_ONLY__NOT_IMPLEMENTED
scope: OPEN_BATTLEFIELD_VISUAL_GRAMMAR / FORWARD_FIXED_DEFENSE_REMOVAL / CONSTRUCTION_PAD_READABILITY / STAGE1_FTUE
supersedes_in_scope:
  - OMW-PLAN-20260828-BASE-FORWARD-BATTLEFIELD-CONSTRUCTION-LAYOUT-01__FENCED_BOUNDARIES_AND_FORWARD_BARRICADE_ONLY
  - OMW-PLAN-20260828-FORWARD-DEFENSE-OCCUPATION-NODES-01__FIXED_FORWARD_BARRICADE_ONLY
product_code_authority: NONE
runtime: NOT_RUN
human_validation: NOT_RUN
player_experience_validation: NOT_RUN
visual_direction_lock_packet: docs/design/APPROVED_OMENWARD_OPEN_BATTLEFIELD_V6_VISUAL_DIRECTION_LOCK_2026-08-29.md
```

## 1. 현재 사용자 승인 구조

전장은 울타리·성벽·원형 요새·바리케이드로 구획된 보드가 아니라, 전투 흔적과 지형 속에서 세 전선이 자연스럽게 갈라지는 **열린 전장**이다. Ward/Veil의 본진과 전진기지는 건물 군집이 아니라 전장 안에서 찾아 읽을 수 있는 지휘·점령 landmark다.

```text
MAP_TOPOLOGY = ONE_WARD_CITADEL_ROOT__THREE_SHARED_FRONTS__ONE_VEIL_CITADEL_ROOT
HOME_BASE_PREBUILT_PRODUCTION_BUILDINGS = NONE
HOME_BASE_CONSTRUCTION_NODE_COUNT_PER_FACTION = 4
HOME_BASE_FIXED_AUTO_ATTACK_TOWER_COUNT_PER_FACTION = 2
FORWARD_BASE_COUNT_PER_FACTION = 3
FORWARD_BASE_CONSTRUCTION_NODE_COUNT_PER_BASE = 2
FORWARD_BASE_FIXED_AUTO_ATTACK_TOWER_COUNT_PER_BASE = 1
FORWARD_BASE_FIXED_DEFENSE_STACK = AUTO_ATTACK_TOWER_ONLY
FORWARD_BARRICADE = REMOVED__NOT_A_FIXED_DEFENSE_OR_MAP_VISUAL
FENCED_OR_ENCLOSED_BASE_BOUNDARY = FORBIDDEN
TOTAL_CONSTRUCTION_NODE_CAPACITY_PER_FACTION = 10
TOTAL_CONSTRUCTION_NODE_CAPACITY_MAPRUN = 20
```

`FORWARD_BARRICADE`만 이번 Decision으로 제거한다. 기존 `TACTICAL_COMMAND_BARRICADE`의 룰·데이터·전술 UI는 이번 열린 전장 시각/전진기지 배치 범위 밖이며, 그 시스템의 삭제를 뜻하지 않는다.

## 2. 공간·시각 문법

- 양쪽 한 개의 지휘 표식에서 상·중·하 세 branch가 넓은 지형을 따라 갈라진다. 세 병렬 도로·독립 본진 세 개·닫힌 경기장은 금지다.
- 본진은 깃발/지휘 표식·고정탑 2개·서로 떨어진 빈 패드 4개만으로 읽힌다. 울타리·성벽·원형 테두리·병영·농장은 없다.
- 전진기지는 고정 자동공격탑 1개와 서로 떨어진 빈 패드 2개로 읽힌다. 바리케이드·문·방어선·울타리가 없다.
- 건설 패드는 전장을 막는 원형 미니요새가 아니라, 지면 문양·낮은 석재 기반·마력 흔적으로 드러나는 **발견 가능한 고정 선택 자리**다.
- `BUILD_PLACEMENT_FREEDOM = DISCOVERABLE_FIXED_PADS_IN_OPEN_TERRAIN__NOT_FREEFORM_TERRAIN_GRID`다. 전장 감각은 자유롭게 만들되, 점령 보상과 세 전선 선택을 무너뜨리는 임의 지형 건설로 확장하지 않는다.
- 세 접전지는 넓고 서로 다른 엄폐물·바위 능선·얕은 물길·분화구·부서진 석재·연기·마법 흔적을 쓴다. 유닛은 작게, 집단과 교전 방향은 실루엣으로 읽혀야 한다.
- 영역 구분은 지형, 깃발, 진영색, 유닛 밀도, 전투 흔적만 사용한다. 울타리·벽·선 긋기·닫힌 링을 경계 표기로 사용하지 않는다.

## 3. 플레이 경험·FTUE 영향

```text
세 전선의 열린 지형·압력·패드를 동시에 관측
→ 룰렛 결과와 제한 조작으로 병력을 확보
→ 지형마다 다른 압력 아래 한 전선에 비가역 커밋
→ 병력·고정탑의 보조 화력·제한 전술로 접전지를 밀거나 버팀
→ 안정 점령한 전진기지의 두 패드가 Stage gate에 따라 다음 설계 선택을 엶
→ 결과와 실패 원인을 복기하고 다음 분포를 설계
```

- **의미 있는 고민:** 지연 시설 뒤에서 버티는 것이 아니라, 열린 지형에서 위험한 전선을 병력으로 즉시 보강할지, 안정 전선을 점령해 두 패드의 장기 선택을 열지 판단한다.
- **즉시 피드백:** 탑의 보조 화력, 작은 병력 군집의 전진/후퇴, 전진기지 패드의 잠금/해금, 지형별 교전 밀도가 함께 변한다.
- **실패 학습:** 탑이 있어도 병력 커밋·룰렛 설계가 틀리면 열린 접전지를 잃는다. 실패 원인은 ‘바리케이드가 약했다’가 아니라 ‘어느 전선에 언제 병력과 설계를 썼는가’다.

Stage 1은 건설을 직접 시키지 않는다. 본진의 패드 4개·탑 2개와 전진기지의 패드 2개·탑 1개는 보이되 잠긴 미래 선택이다. 설명은 본진 지휘·방어, 열린 전진기지와 패드, 3×3 징조륜/커밋 순서로 진행한다.

```text
STAGE_1_DIRECT_CONSTRUCTION = FORBIDDEN
STAGE_1_VISIBLE_HOME_CONSTRUCTION_NODES = 4
STAGE_1_VISIBLE_FORWARD_CONSTRUCTION_NODES_PER_BASE = 2
STAGE_1_FIXED_DEFENSE_EXPLANATION = HOME_TOWERS__THEN_FORWARD_TOWER_ONLY
STAGE_1_NODE_INTERACTION_STATE = VISIBLE_LOCKED__FIRST_MEANINGFUL_BUILD_STAGE_2
FIRST_MEANINGFUL_BUILD_OR_UPGRADE = STAGE_2_T2_UPGRADE
```

## 4. 실제 구현 대조와 Phase 2 경계

| 항목 | actual code / data evidence | 판정 |
|---|---|---|
| 전진기지 node 배열 | `BuildingService.register_outpost(..., node_ids: Array)`와 existing headless tests | 배열 확장 기반 존재; 현재 `stage_run.gd`는 3 node를 등록하므로 2 node runtime 적용은 아직 미구현 |
| 전진기지 바리케이드 | 새 `FORWARD_BARRICADE` runtime consumer 없음 | 삭제로 새 consumer가 필요 없어짐; 기존 전술 명령 바리케이드와 혼동 금지 |
| 고정탑 | `BaseState`/`BattleSimulator`/Run Command에 tower state/combat/map consumer 없음 | NOT_IMPLEMENTED |
| 본진 4 node | home node state·소유·잠금 모델 없음 | NOT_IMPLEMENTED |
| 열린 지형·패드 지도 | target-resolution Control/Scene consumer 없음 | NOT_IMPLEMENTED |
| 수치·가독성·플레이 경험 | simulation/human evidence 없음 | NOT_RUN |

```text
PHASE_2_PRODUCT_CODE_AUTHORITY = NONE
REQUIRED_PHASE2_TESTS =
  HOME_BASE_EXPOSES_EXACTLY_FOUR_CONSTRUCTION_NODES_AND_TWO_TOWERS
  FORWARD_BASE_EXPOSES_EXACTLY_TWO_CONSTRUCTION_NODES_AND_ONE_TOWER
  FORWARD_BASE_HAS_NO_FIXED_BARRICADE_STATE_OR_MAP_CONSUMER
  FIXED_TOWER_NEVER_GENERATES_CAPTURE_POWER_OR_SOLO_CLEAR
  STAGE1_SHOWS_ALL_PADS_BUT_REJECTS_CONSTRUCTION
  OPEN_BATTLEFIELD_MAP_REMAINS_LEGIBLE_AT_TARGET_RESOLUTIONS
```

## 5. 벤치마크 처분·권리 경계

| Reference | 확인한 원칙 | 처분 |
|---|---|---|
| [Commander Quest](https://commanderquest.itch.io/commanderquest) | 전투 중인 넓은 지면 위에서 유닛 군집·장애물·위협을 먼저 읽는 전장 감각 | ADAPT: 열린 전장 밀도와 정보 우선순위만 참고. UI, 카드, 캐릭터, 고유 배치, 로고, 색 체계는 복제하지 않음. |
| [Thronefall](https://store.steampowered.com/app/2239150/Thronefall/) | 각 지형이 건설/방어 판단에 영향을 준다는 원칙 | ADAPT: 지형 차이와 선택의 관계만 참고. 벽·바리케이드/일야 루프/직접 영웅 전투는 채택하지 않음. |
| [Cataclismo](https://store.steampowered.com/app/1422440/Cataclismo/) | 자유형 벽 건설은 별도 핵심 시스템이 된다는 경고 | REJECT: 자유형 terrain grid 건설은 scope와 세 전선 commit 판단을 과도하게 확장함. |

```text
DIFFERENTIATION = PLAYER_CONSTRUCTED_PROBABILITY_ENGINE + IRREVERSIBLE_THREE_FRONT_COMMIT + OPEN_TERRAIN_OCCUPATION_UNLOCKED_FIXED_PADS
USER_REFERENCE_RIGHTS = REFERENCE_ONLY__NOT_PROJECT_ASSET
GENERATED_BOARD_RIGHTS = PLANNING_REFERENCE_ONLY__NOT_RUNTIME_ASSET__NOT_RELEASE_RIGHTS_PASS
```

## 6. Incident / Solution / Lesson

```text
INCIDENT = V5_BOARD_USED_FENCES_AND_FORWARD_BARRICADES_THAT_MADE_OPEN_BATTLEFIELD_INTENT_READ_AS_ENCLOSED_OUTPOST_BOARD
SOLUTION = REMOVE_ALL_FENCED_BOUNDARIES_AND_FIXED_FORWARD_BARRICADES__RETAIN_EXACT_PAD_AND_TOWER_COUNTS__REGENERATE_V6
LESSON = FREE_BATTLEFIELD_FEEL_REQUIRES_OPEN_TERRAIN_AND_DISCOVERABLE_FIXED_CHOICES__NOT_UNBOUNDED_FREEFORM_BUILDING_OR_VISUAL_BARRIERS
NO_BASE_PROMOTION = PROJECT_SPECIFIC_THREE_FRONT_OCCUPATION_AND_FIXED_PAD_LAYOUT
```

이 문서는 실제 Godot Scene/UI/Resource, runtime asset, 밸런스 수치, target-resolution 가독성, Human usability / Player Experience PASS를 뜻하지 않는다.

2026-08-29 사용자는 v6 planning board를 확정했다. 선택한 rendering/layer/Keep-Avoid/variation은 `APPROVED_OMENWARD_OPEN_BATTLEFIELD_V6_VISUAL_DIRECTION_LOCK_2026-08-29.md`가 소유하며, 이 layout contract의 code authority는 계속 `NONE`이다.
