# OMENWARD 전투 우선 계층 복구 블루프린트 V2

```yaml
blueprint_id: OMW-BLUEPRINT-20260902-BATTLE-PRIMARY-HIERARCHY-RECOVERY-V2
status: USER_CONFIRMED__IMPLEMENTED__FULL_MACHINE_VERIFIED__RUNTIME_TECHNICAL_SMOKE_PRECOMMIT_CAPTURED__HUMAN_NOT_RUN
approved_authoring_at: 2026-09-02 KST
approval_source: USER_CHAT__"승인,권장안대로 작업진행해 그리고 블루프린트가 이전버전보다 퇴행했다. 다시 확인하고 작업해"
scope: SINGLE_FRONT_BATTLE_SCREEN_HIERARCHY / BLUEPRINT_DRIFT_REPAIR / CURRENT_CONSUMER_ALIGNMENT
new_product_decision: NONE
product_authority: docs/CURRENT_CONFIRMED_DECISIONS.md
active_context: docs/ACTIVE_CONTEXT.md
supersedes_in_scope: docs/superpowers/specs/2026-09-01-single-front-command-blueprint-design.md::battle_surface_wireframe_only
retains: OMW-PLAN-20260830-BATTLE-PRIMARY-MARCH-MINIMAP-01
runtime_mutation: BATTLE_PRESENTATION_ONLY
asset_mutation: NONE__REUSE_LOCKED_TERRAIN_AND_APPROVED_ROLE_PROFILES
human_validation: NOT_RUN
```

## 1. 문제 판정

단일 전선 전환은 유지한다. 퇴행은 전선 수가 아니라 그 전환을 화면으로 옮기는 과정에서 생겼다.

| 현재 상태 | 확인된 원인 | 복구 목표 | 기대 효과 |
| --- | --- | --- | --- |
| BATTLE 전투 프레임이 `926×256`이고 그 아래 설명 영역이 `928×164` | 이전 블루프린트가 넓은 전략 보드를 제거하면서 단일 전투의 세로 시각 질량을 정하지 않았다 | BATTLE에서 전투를 `926×304`로 확대하고 하단 덱을 `928×106`으로 축소 | 병종·지형·탑·교전이 설명문보다 먼저 읽힌다 |
| 미니맵이 선·점·작은 라벨로만 보인다 | “한 줄 맥락”은 고정했지만 다섯 구간의 정보 단위를 시각적으로 설계하지 않았다 | 하나의 연결된 5구간 상태 리본으로 정리 | 전선의 위치·소유·접전·탑을 두 번째 전장 없이 읽는다 |
| 유닛 밑의 큰 원형 표식이 전장보다 강하게 보인다 | 초기에 적은 유닛을 기술적으로 확인하기 위한 표시가 그대로 남았다 | 작은 접지 그림자와 더 큰 역할 실루엣으로 교체 | 병사·무기·마법이 전술 말판이 아니라 전투 부대로 읽힌다 |
| 자산 기록이 폐기된 우측 미니맵 `686×302 + 230×302`을 계속 설명한다 | 2026-08-31 상단 스트립 변경 뒤 기록이 동기화되지 않았다 | 새 960×540 BATTLE 격자와 실제 소비자를 같은 문서로 기록 | 블루프린트·씬·테스트·증거가 같은 화면을 가리킨다 |

## 2. 검토한 대안

| 안 | 내용 | 판정 | 이유 |
| --- | --- | --- | --- |
| A. V1 유지 | 현재의 낮은 전투 프레임과 큰 하단 덱을 보존 | REJECT | 사용자가 지적한 정보 계층·전장 밀도 문제를 남긴다 |
| B. 과거 넓은 전략 보드 복귀 | 예전 다중 전장 보드의 시각 밀도를 되살림 | REJECT | 세 전선, 긴 도로, 지도 건물 배치가 현재 단일 전선 정본과 충돌한다 |
| C. 단일 전선의 밀도 복구 | 상단 1줄 맥락, 넓은 실제 전투, 짧은 행동 덱으로 재분배 | ADOPT | 현재 제품 규칙과 승인된 지형·자산을 보존하면서 퇴행 지점만 바로잡는다 |

## 3. 변하지 않는 제품 경계

```text
MAP_TOPOLOGY = WARD_CITADEL -> WARD_FORWARD -> CLASH -> VEIL_FORWARD -> VEIL_CITADEL
ACTIVE_FRONT_COUNT = 1
MARCH_MINIMAP = READ_ONLY_FIVE_SECTOR_CONTEXT
MARCH_MINIMAP_LAYOUT = TOP_SINGLE_ROW_STRIP
MARCH_MINIMAP_CONTENTS = OWNERSHIP + CONTESTED + FIXED_TOWER + CURRENT_SECTOR_ONLY
UNIT_BY_UNIT_MINIMAP_REPLICATION = FORBIDDEN
BUILDING_MAP_PLACEMENT = FORBIDDEN
FIXED_TOWER_COUNT_PER_ACTIVE_FRONT = 1
GLOBAL_BUILDING_ROSTER = 6 + STABLE_PLAYER_HELD_CAPTURE_POINT, MAX 9
RUN_COMMAND_TABS = DOMESTIC / ROULETTE / FRONT
ROULETTE_IDENTITY = PLAYER_CONSTRUCTED_PROBABILITY_ENGINE
GAMBLING_FANTASY_POSITIONING = FORBIDDEN
```

이 복구는 저장 구조, 점령 보상, 병력 상성, 룰렛 확률, 전투 수치, 탭 의미, 외부 모듈, 플랫폼, 출시 상태를 바꾸지 않는다.

## 4. 960×540 BATTLE 와이어프레임

```text
 x=16                                                               x=944
 ┌──────────────────────────────────────────────────────────────────────┐ y=12
 │ BATTLE      [내정] [룰렛] [전선]                 Gold · 병력/상한       │ 40
 └──────────────────────────────────────────────────────────────────────┘ y=52

 ┌──────────────────────────────────────────────────────────────────────┐ y=62
 │ 전진  [수호 성채]─[수호 전진·탑]─[접전]─[장막 전진]─[베일 성채]       │ 40
 └──────────────────────────────────────────────────────────────────────┘ y=102

 ┌──────────────────────────────────────────────────────────────────────┐ y=110
 │ 전투 초점 · 현재 구간                              수호 n · 장막 n     │
 │ Lumern 바깥 지형      방어탑  병력·무기·마법이 읽히는 교전 통로      │
 │                      ────────────────────────────  Veil 바깥 지형      │
 │         수호 전열 / 창 / 궁 / 마법        베일 전열 / 돌격 / 주문      │
 │                       (건물·노드·울타리 없음)                         │ 304
 └──────────────────────────────────────────────────────────────────────┘ y=414

 ┌──────────────────────────────────────────────────────────────────────┐ y=422
 │ 전투 진행 중 · 현재 위협 / 탑 상태 / 잠긴 조작 / 다음 관측             │ 106
 └──────────────────────────────────────────────────────────────────────┘ y=528
```

### 계층 규칙

1. `BattleFocusViewport`는 BATTLE에서만 `926×304`이며, 화면의 가장 큰 시각 질량이다.
2. `MarchMinimap`은 `926×40`의 **하나의** 상단 리본이다. 각 구간은 소유·접전·현재 위치·탑만 담는다.
3. `LowerDeck`은 BATTLE에서만 `928×106`으로 압축한다. 현재 스테이지의 규칙·상태만 보이며, 새 전술이나 가짜 행동을 만들지 않는다.
4. 다른 위상에서는 현재 `928×164` 덱을 유지한다. 내정·룰렛·커밋의 기능 흐름은 이 복구에서 재설계하지 않는다.
5. 기존 foundation과 여섯 지형 소품을 재사용한다. 소품은 `y=0.36..0.80` 통행·교전 통로를 침범하지 않는다.

## 5. 전투와 미니맵의 역할 분리

| 표면 | 반드시 보이는 것 | 보이면 안 되는 것 | 소비자 |
| --- | --- | --- | --- |
| 전투 초점 | 실제 유닛, 역할 실루엣, 체력, 전투 진영, 한 개의 고정탑, 현재 구간, 승인 지형 | 지도 건물, 건설 노드, 건물 슬롯, 긴 전체 도로, 두 번째 전장 | `BattleFocusView` |
| 전진 리본 | 5구간 순서, 소유·접전, 현재 구간, 수호 전진기지의 탑 | 개별 유닛, 병력 수 반복, 배치 입력, 교전 효과, 두 번째 탑 | `MarchMinimapView` |
| 행동 덱 | 전투 상태와 조작 잠금의 짧은 설명 | 전투를 가리는 장문 설명, 새로운 기술 버튼, 룰렛/건설 쓰기 | `RunCommandScreen` |

## 6. 실제 Godot 소유 경계

```text
StageRun / BattleSimulator
    └── front route, tower, actual units, command_phase

RunCommandScreen
    └── BATTLE일 때만 BattleFocus/Minimap/LowerDeck rect를 재배치

BattleFocusView
    └── 승인 role texture와 작은 접지 그림자만으로 실제 front units를 투영

MarchMinimapView
    └── read-only presentation_contract + 5개 연결 sector cell을 그림
```

UI는 domain state를 계산하거나 변경하지 않는다. `presentation_contract()`는 검증과 문서 정합성을 위한 read-only 설명 값이며 게임 데이터 정본이 아니다.

## 7. 구현 전 RED / 구현 후 GREEN 계약

```text
BATTLE_LAYOUT = BattleFocus 926x304 + MarchMinimap 926x40 + LowerDeck 928x106
NON_BATTLE_LOWER_DECK = 928x164
MARCH_MINIMAP = top_single_row + five_sector + read_only + no_unit_replication
ROLE_DISPLAY_CELL = 104x104
BATTLE_UNIT_MARKER = small_ground_shadow_only
ONE_FIXED_TOWER_MAX = retained
NO_MAP_BUILDINGS_OR_CONSTRUCTION_NODES = retained
TERRAIN_PROPS_OUTSIDE_TRAVEL_CORRIDOR = retained
```

| 검증 층 | 성공 기준 | 현재 상태 |
| --- | --- | --- |
| RED 계약 | 새 배치·리본·표시 셀 조건이 변경 전 실제 씬에서 실패 | PASS — 2026-09-02 변경 전 의도된 7개 조건 실패 확인 |
| Godot focused | 새 계약과 기존 battle/minimap/layout 계약 통과 | PASS — 새 V2 + retained contract 3개 |
| 전체 기계 검증 | 영향 범위의 headless·Python·project validator 통과 | PASS — Godot headless 34/34, Python 570/570, approved project operating contract |
| 런타임 기술 캡처 | 현재 exact HEAD 960×540 BATTLE 캡처와 오류/경고 확인 | PRECOMMIT_CAPTURED — exact commit capture and evidence record remain pending |
| 사람 가독성 | 병종·전선 맥락·전투 우선성을 실제 사람이 확인 | NOT_RUN |
| 권리·출시 | 기존 separate gate | NOT_RUN |

## 8. 문서 정합성 및 롤백

- `docs/images/approved/OMENWARD_CLOSE_SINGLE_FRONT_BATTLEFIELD_MODULAR_V1.md`의 폐기된 우측 미니맵 치수는 이 V2의 실제 BATTLE 격자로 갱신한다.
- V1 블루프린트, 넓은 전략 보드, 이전 캡처 및 승인 자산은 역사·참고 자료로 보존한다. 삭제나 바이너리 교체는 하지 않는다.
- 롤백은 이 V2 후속 커밋을 되돌리고, 원래의 scene/script rect와 marker drawing으로 복귀하는 것이다. 저장·자산·도메인 데이터에는 마이그레이션이 없다.
