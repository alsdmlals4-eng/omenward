# [보존된 도메인] OMENWARD 단일 행군 전선과 세 탭 지휘 구조

```yaml
decision_id: OMW-PLAN-20260830-SINGLE-MARCH-FRONT-THREE-TAB-01
approved_at: 2026-08-30 KST
approval_source: USER_CHAT__"확정 게임진행해"
status: USER_CONFIRMED__IMPLEMENTATION_AUTHORIZED
scope: MAP_TOPOLOGY / BATTLE_SIMULATION / RUN_COMMAND_TABS / STAGE_DATA
presentation_state: SUPERSEDED_BY_OMW-PLAN-20260830-BATTLE-PRIMARY-MARCH-MINIMAP-01
implementation_state: IMPLEMENTED__28_HEADLESS_GODOT_CONTRACTS_PASS
machine_verification: PASS__28_HEADLESS_GODOT_CONTRACTS
runtime_verification: RUNTIME_TECHNICAL_SMOKE_PASS
human_validation: NOT_RUN
```

> 현재 전투 화면의 주/보조 시각 계층은
> `OMW-PLAN-20260830-BATTLE-PRIMARY-MARCH-MINIMAP-01`가 소유한다. 이 문서는 단일 전선,
> 5구간 route state, 세 탭, 단일 방어탑, 건물 로스터의 **도메인 규칙**만 유지한다.

## 1. Decision

OMENWARD의 전투 책임은 세 개의 동시 전선이 아니라 하나의 넓은 **단일 행군 전선**이다.
전략성은 전선 선택에서 나오지 않는다. 플레이어는 전역 건물 로스터로 확률 엔진을 구성하고,
3×3 징조륜을 직접 조작한 뒤 획득한 병력을 하나의 전선에 되돌릴 수 없게 투입한다.

```text
MAP_TOPOLOGY = ONE_WARD_CITADEL -> ONE_ACTIVE_MARCH_FRONT -> ONE_VEIL_CITADEL
ACTIVE_FRONT_ID = front
PARALLEL_THREE_FRONTS = REMOVED
TOP_MIDDLE_BOTTOM_FRONT_IDS = REMOVED
ROUTE_STATE_GRAMMAR = WARD_CITADEL -> WARD_FORWARD_BASE -> CLASH_ZONE -> VEIL_FORWARD_BASE -> VEIL_CITADEL
RUN_COMMAND_TABS = DOMESTIC / ROULETTE / FRONT
COMMAND_PHASE_FLOW = PREPARE -> STOPPED_3X3 -> MANIPULATE -> RESULT_CONFIRM -> COMMIT -> BATTLE -> REVIEW
IRREVERSIBLE_FRONT_COMMITMENT = REQUIRED
```

`DOMESTIC / ROULETTE / FRONT`는 표시와 탐색을 위한 탭이며, command phase는 규칙과 행동 권한을
소유한다. BATTLE 중 룰렛 탭을 열어 맥락을 볼 수 있어도 룰렛을 돌리거나 건물 로스터를 변경할 수는 없다.

## 2. Player-facing loop

```text
[내정] 전역 건물 로스터 설치·재정렬 → 다음 룰렛 확률·경제 변화 확인
    ↓
[룰렛] 정직한 stopped 3×3 결과 → 제한된 행·열 조작 → 단일 전선 대기열 생성
    ↓
[전선] 대기열 전체 비가역 커밋 → 단일 방향 전투 → 점령과 전투 원인 복기
```

```text
ROULETTE_IDENTITY = PLAYER_CONSTRUCTED_PROBABILITY_ENGINE
GAMBLING_FANTASY_POSITIONING = FORBIDDEN
SCRIPTED_FAKE_NEAR_MISS = FORBIDDEN
RNG_CAN_REMOVE_ALL_VALID_RESPONSES = FORBIDDEN
ROULETTE_RESULT_AUTO_FRONT_DEPLOYMENT = FORBIDDEN
POST_COMMIT_RECALL_SELL_OR_REDISTRIBUTION = FORBIDDEN
```

전선 선택 드롭다운은 존재하지 않는다. 결과 확정 뒤의 선택은 “어느 전선에 보낼까”가 아니라
“현재의 대기열을 지금 이 전선에 확정할까”이다. 전략성은 내정의 확률 설계, 행·열 조작,
병력 조합, 확정 시점, 제한된 전술로 이전된다.

## 3. Five-sector advancing battlefield

전선 탭은 세 길을 축소해 보여 주지 않는다. 전투의 현재 중심은 다음 다섯 구간 중 하나이며,
점령·후퇴에 따라 배경의 중심과 목표 표식이 이동한다.

| 순서 | 구간 | 읽히는 변화 |
|---|---|---|
| 1 | Ward Citadel | 수호 측 출발·후방 위협 |
| 2 | Ward Forward Base | 수호 전진기지와 고정 방어탑 소유권 |
| 3 | Clash Zone | 중립/접전/안정 점령의 주 교전지 |
| 4 | Veil Forward Base | 장막 전진기지 탈환 또는 반격의 목표 |
| 5 | Veil Citadel | 장막 성채 공성 또는 수호 측 패배 압박 |

```text
FRONT_PRESENTATION = SINGLE_WIDE_DIRECTIONAL_BATTLEFIELD
SECTOR_CAMERA = ADVANCES_OR_RETREATS_WITH_ROUTE_STATE
VISIBLE_BATTLEFIELD = TERRAIN + ONE_FIXED_TOWER + UNITS + OBJECTIVE_MARKERS + COMBAT_EFFECTS
VISIBLE_BATTLEFIELD_EXCLUDES = BUILDING_MODELS + CONSTRUCTION_NODES + BUILDING_PLACEMENT + PARALLEL_ROUTE_CARDS
```

한 화면의 구간 전환은 전장 연출이며 전투 규칙을 바꾸지 않는다. 모든 목표 상태와 전투 좌표는
결정론적 단일 front state에서 읽는다.

## 4. Buildings, occupation, and tower

```text
BASE_BUILDING_SLOT_CAPACITY = 6
OCCUPATION_SLOT_BONUS = 1_PER_STABLE_PLAYER_HELD_ELIGIBLE_POINT
ELIGIBLE_SLOT_POINTS = WARD_FORWARD_BASE + CLASH_ZONE + VEIL_FORWARD_BASE
SINGLE_FRONT_MAXIMUM_SLOT_CAPACITY = 9
ROSTER_ORDER = EXPLICIT_PLAYER_PRIORITY_TOP_TO_BOTTOM
INACTIVE_OVERFLOW = RETAINED_WITHOUT_REFUND
FIXED_TOWER_COUNT_PER_ACTIVE_FRONT = 1
TOWER_BEARING_OBJECTIVE = WARD_FORWARD_BASE
TOWER_OWNERSHIP = OBJECTIVE_STABLE_OWNER
TOWER_CAPTURE_POWER = 0
TOWER_GOLD_EFFECT = EXISTING_OBJECTIVE_OWNERSHIP_INCOME_PATH_ONLY
```

- 수호 진영이 안정적으로 어느 한 전진기지 또는 접전지를 보유할 때마다 슬롯 하나가 열린다.
- 점령지가 접전·중립·적 소유가 되면 그 보너스는 즉시 사라진다.
- 잠긴 경계 아래의 기존 건물은 삭제되지 않고 `INACTIVE_LOCKED`가 된다. 비용·등급·이력은 남지만,
  식량 상한·수입·자동생산·룰렛 TokenSource를 제공하지 않는다.
- 잠금이 풀리면 위에서부터 우선순위 순서대로 다시 활성화된다.

방어탑은 전선마다 하나라는 기존 사용자 지시를 단일 전선에 맞게 **총 하나**로 변환한다. 탑은
전진기지의 안정 소유자와 같은 소유권만 표시하며, 독립 점령이나 탑에 의한 중복 골드 지급은 없다.

## 5. UI architecture

```text
TOP_HUD = RESOURCES + COMMAND_PHASE + ACTIVE_TAB + TOP_SINGLE_ROW_MARCH_MINIMAP
MARCH_MINIMAP_LAYOUT = TOP_SINGLE_ROW_STRIP
MARCH_MINIMAP_CONTENTS = FIVE_SECTOR_OWNERSHIP + CONTESTED + FIXED_TOWER + CURRENT_SECTOR
DOMESTIC = GLOBAL_BUILDING_ROSTER + SLOT_CAPACITY + ACTIVE/LOCKED + ROULETTE_DELTA_PREVIEW
ROULETTE = 3X3_BOARD + ROW_COLUMN_CONTROLS + RESULT_FORECAST + PENDING_FRONT_QUEUE
FRONT = WIDE_BATTLEFIELD + SECTOR_STATE + ONE_TOWER + UNITS + OBJECTIVE + CAUSAL_FEEDBACK
```

- 기본 탭은 PREPARE의 `DOMESTIC`이다.
- 룰렛 시작은 `ROULETTE`를 자동 선택하고 내정 변경을 잠근다.
- 결과 확인과 커밋은 `FRONT`에서 단일 전선 투입 확정을 제공한다.
- BATTLE은 `FRONT`를 자동 선택한다.
- REVIEW는 탭을 유지하지만 결과 인과를 우선하며 정답 빌드를 지시하지 않는다.

탭 전환은 별도 UI state인 `active_tab`이며 `command_phase`를 우회하거나 변경하지 않는다.

## 6. Runtime data transition

```text
RUNTIME_FRONT_COLLECTION = EXACTLY_ONE(front)
LEGACY_RUNTIME_LANE_IDS = top / middle / bottom
LEGACY_RUNTIME_LANE_IDS_STATUS = REMOVED_FROM_NEW_STAGE_DATA_AND_UI
NEW_STAGE_SPAWNS = front
```

- 현재 제품에는 실제 MapRun 저장/불러오기 스키마가 구현되어 있지 않다. 따라서 존재하지 않는 저장 파일의
  변환을 주장하거나 임의 마이그레이션 파일을 만들지 않는다.
- 현재 Stage 리소스, 웨이브 정의, 룰렛 보상, 배포, 전투 시뮬레이터, UI는 모두 단일 `front`를 소비한다.
- 코드의 내부 1차원 보관 컨테이너 이름은 안전한 별도 리팩터링 전까지 남을 수 있지만, 공개 데이터·UI 문구·
  도메인 계약은 `top/middle/bottom`을 노출하지 않는다.
- 새 저장 시스템이 추가되는 시점에는 `save_schema_version`과 명시적 이관 규칙을 별도 승인·테스트한다.

## 7. Visual asset boundary

기존 넓은 세 전선 지형 래스터는 삭제하지 않는다. 이 결정 범위에서는
`SUPERSEDED_FOR_SINGLE_FRONT__NOT_A_RUNTIME_CONSUMER`로 기록한다. 최근 승인된 Lumern/Veil
방패병 true-alpha pair는 단일 전선에서도 유효한 runtime 자산으로 유지한다.

새 단일 전선 지형은 다음 순서 외에는 runtime에 연결하지 않는다.

```text
BRIEF_READY -> GENERATED_CANDIDATE -> USER_APPROVED -> CANON_REGISTERED -> IMPLEMENTED -> RUNTIME_VERIFIED
```

## 8. Benchmark decisions

| Reference group | Observation | Omenward decision |
|---|---|---|
| Slotbound | 3×3 슬롯 결과가 유닛과 자동전투에 직접 연결된다. | ADAPT — 룰렛→병력→단일 전선 인과, 흡수 시스템은 미채택. |
| Luck be a Landlord / Spin Hero / Slots & Daggers | 심볼·아이템·릴 설계가 확률 선택의 주체가 된다. | ADOPT — 내정 변화의 명확한 룰렛 영향 미리보기. |
| Commander Quest / Backpack Battles / Despot's Game | 전투 전 구성의 의미가 자동전투에서 읽혀야 한다. | ADOPT — 대기열, 확정, 전투 원인 복기. |
| Backpack Hero / Vivid Knight | 작은 슬롯 상한이 전략적 우선순위를 만든다. | ADOPT — 6+점령 슬롯과 비활성 overflow. |
| Loop Hero / Super Fantasy Kingdom / Thronefall | 조건 설계와 방어 결과의 짧은 인과 루프가 강하다. | ADAPT — 내정은 전장 건물이 아니라 확률·경제 조건이다. |
| Kingdom Two Crowns | 횡방향 단일 위협 축이 전장 가독성을 높인다. | ADOPT — 수호→장막의 단일 방향 전선. |
| The Last Flame | 과도한 빌드 폭은 초기 읽기 비용을 높인다. | REJECT — 초기 수백 종 확장과 복잡한 복수 전선. |

공식 참고 링크: [Slotbound](https://store.steampowered.com/app/4459590/Slotbound/?l=koreana),
[Luck be a Landlord](https://play.google.com/store/apps/details?hl=id&id=com.trampolinetales.lbal),
[Spin Hero](https://goblinzstudio.com/game/spin-hero/),
[Commander Quest](https://commanderquest.itch.io/commanderquest),
[Backpack Battles](https://game.shochiku.co.jp/games/backpack-battles/),
[Backpack Hero](https://thejaspel.itch.io/backpack-hero),
[Vivid Knight](https://www.asobism.co.jp/vividknight/en/),
[Loop Hero](https://www.devolverdigital.com/games/loop-hero),
[Super Fantasy Kingdom](https://store.steampowered.com/app/2289750/_Super_Fantasy_Kingdom/),
[Thronefall](https://throne-fall.github.io/), [Kingdom Two Crowns](https://kingdomthegame.com/kingdom-two-crowns/),
[Despot's Game](https://www.despotsgame.com/), [The Last Flame](https://store.steampowered.com/app/1830970/_The_Last_Flame/),
and [Slots & Daggers](https://store.steampowered.com/app/3631290/____Slots__Daggers/).

## 9. Supersession and evidence limits

This decision supersedes only the following scope:

- `OMW-VISUAL-20260828-STORYBOOK-SD-THREE-FRONT-STRATEGIC-MAP-01` — three shared-front topology,
  simultaneous-three-front presentation, per-front minimap context, and terrain consumer.
- `OMW-PLAN-20260830-GLOBAL-BUILDING-ROSTER-OCCUPATION-SLOTS-01` — `one tower per shared front` becomes
  `one tower per active front`; global roster and no-map-building rules remain retained.
- Earlier three-front commitment, UI copy, FTUE phrasing, and headless tests only where they require
  `top/middle/bottom` choice or simultaneous three-front display.

It retains the player-constructed probability engine, 3×3 direct manipulation, deterministic simulation,
global building roster, no battlefield buildings, silhouette-first units, storybook watercolor SD direction,
20-stage cadence, and evidence ceilings.

```text
AUTOMATED_TEST_PASS != RUNTIME_PASS
RUNTIME_PASS != HUMAN_UX_PASS
USER_APPROVAL_OF_ARCHITECTURE != USER_APPROVAL_OF_NEW_GENERATED_ASSET
```
