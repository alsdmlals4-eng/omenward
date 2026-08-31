# Approved · 전투 우선 화면과 전진 미니맵

```yaml
decision_id: OMW-PLAN-20260830-BATTLE-PRIMARY-MARCH-MINIMAP-01
status: USER_CONFIRMED__IMPLEMENTATION_AUTHORIZED__MODULAR_BATTLEFIELD_ASSETS_USER_APPROVED
approved_at: 2026-08-30
updated_at: 2026-08-31
approval_source: "user: 확정해"
scope: single_march_front_battle_presentation
implementation_state: IMPLEMENTED__MODULAR_CLOSE_BATTLEFIELD__FULL_HEADLESS_GODOT_SUITE_PASS
machine_verification: PASS__FULL_HEADLESS_GODOT_SUITE
runtime_verification: TECHNICAL_SMOKE_PASS
human_validation: NOT_RUN
supersedes_in_scope:
  - OMW-PLAN-20260830-SINGLE-MARCH-FRONT-THREE-TAB-01::wide_strategic_map_as_primary_front_surface
retains:
  - OMW-PLAN-20260830-SINGLE-MARCH-FRONT-THREE-TAB-01::one_front_five_sector_route_and_three_tabs
  - OMW-PLAN-20260830-GLOBAL-BUILDING-ROSTER-OCCUPATION-SLOTS-01
  - OMW-PLAN-20260820-BATTLEFIELD-SCALE-READABILITY-01::two_to_three_readable_combat_rows
```

## 결정

`BATTLE`에서 플레이어가 보는 주 화면은 넓은 전략 지도나 별도의 건물 배치 화면이 아니라, 실제 `StageRun` 전투 상태를 읽는 가까운 **전투 우선 뷰**다. 진행 맥락은 상단 한 줄의 읽기 전용 **전진 미니맵**에만 압축한다.

```text
PRIMARY = BattleFocusViewport
SECONDARY = MarchMinimap
MAP_TOPOLOGY = WARD_CITADEL -> WARD_FORWARD -> CLASH -> VEIL_FORWARD -> VEIL_CITADEL
MARCH_MINIMAP = READ_ONLY
MARCH_MINIMAP_LAYOUT = TOP_SINGLE_ROW_STRIP
MARCH_MINIMAP_CONTENTS = FIVE_SECTOR_OWNERSHIP + CONTESTED + FIXED_TOWER + CURRENT_SECTOR
WIDE_STRATEGIC_MAP_AS_BATTLE_PRIMARY = REMOVED
INTERACTIVE_SECOND_BATTLEFIELD = FORBIDDEN
```

## 화면 계약

- `BattleFocusViewport`는 수호·장막 유닛의 실제 위치, 병력 수, 교전 상태, 현 구간, 단일 고정 방어탑의 소유 상태를 하나의 가까운 교전 장면으로 읽는다.
- 전장에는 지형, 유닛, 전투 효과, 고정 방어탑만 보인다. 건물, 건설 패드, 건설 노드와 건물 설치 조작은 금지한다.
- `MarchMinimap`은 전투 뷰 위의 한 줄에서 다섯 구간의 소유/접전/현재 주목 위치와 단일 방어탑 소유 표식만 보여 준다. 개별 유닛 아트·전력 덩어리·배치 조작을 복제하지 않는다.
- 전진 상태가 변하면 두 뷰는 같은 `StageRun.battle.route_state_for(&"front")`에서 갱신한다. 미니맵이 게임 상태를 쓰거나 전투를 조작하지 않는다.
- 내정과 룰렛은 기존 `내정 / 룰렛 / 전선` 탭 및 phase gate를 유지한다. `BATTLE`에서는 전투 뷰가 전선 탭의 주 표면이다.

## 자산과 증거 경계

기존 승인 Shield Guard 양 진영 페어를 계속 사용한다. 사용자가 2026-08-31에 정확히 잠근 modular foundation 및 Lumern/Veil prop set은 `docs/images/approved/OMENWARD_CLOSE_SINGLE_FRONT_BATTLEFIELD_MODULAR_V1.md`로 등록되어 `BattleFocusView`에 바인딩됐다. 이 소품은 병사의 통행·교전 구간(`y=0.36..0.80`)을 침범할 수 없고, Lumern은 좌측 경계·Veil은 우측 경계에서만 렌더된다. 예전 runtime backdrop 파일은 보존하지만 더 이상 close battle view의 소비자가 아니다.

기계 테스트와 Godot 기술 스모크는 구현/실행 증거일 뿐 사람 가독성, 최종 아트 적합성, 밸런스 또는 출시 승인 증거가 아니다.
