# OMENWARD Incident · 열린 전장 의도와 fenced/barricade 보드의 충돌

```yaml
incident_id: OMW-INC-20260828-OPEN-BATTLEFIELD-NO-BARRICADE-01
date: 2026-08-28
class: PROJECT_INCIDENT / CANON_CORRECTION
status: RESOLVED_IN_PLANNING__RUNTIME_NOT_RUN
owner: docs/design/APPROVED_OMENWARD_OPEN_BATTLEFIELD_TOWER_ONLY_FORWARD_LAYOUT_2026-08-28.md
```

## Incident

v5 planning board와 직전 base/forward layout은 울타리와 고정 전진 바리케이드를 사용했다. 이 표현은 사용자 요청인 “전투 중인 넓고 자유로운 전장” 대신 닫힌 outpost 보드처럼 읽혔고, 고정 패드의 발견·점령 보상도 경계 장식에 가려졌다.

## Solution

고정 패드/탑 수량과 세 shared front topology는 보존하고, 울타리·벽·닫힌 링·고정 전진 바리케이드를 삭제했다. v6 generated exploration은 지형, 깃발, 진영색, 유닛 밀도, 전투 흔적으로 영역을 읽는다. “자유로운 전장”은 `DISCOVERABLE_FIXED_PADS_IN_OPEN_TERRAIN`이며 freeform terrain grid가 아니다.

## Lesson / disposition

```text
LESSON = OPEN_BATTLEFIELD_READABILITY_REQUIRES_TERRAIN_AND_CONFLICT_SIGNALS_NOT_ENCLOSED_BOUNDARIES
RETAINED = HOME_4_PADS_2_TOWERS / FORWARD_2_PADS_1_TOWER / THREE_SHARED_FRONTS
REMOVED = FENCED_BOUNDARIES / FIXED_FORWARD_BARRICADE
TACTICAL_COMMAND_BARRICADE = OUT_OF_SCOPE__RETAINED
NO_BASE_PROMOTION = PROJECT_SPECIFIC_THREE_FRONT_OCCUPATION_LAYOUT_AND_VISUAL_GRAMMAR
```

현재 교정은 정본·planning board 수준이다. Godot Scene/Resource/data/runtime/human/player evidence는 `NOT_RUN`이며, 새 보드는 runtime asset이나 release-rights PASS가 아니다.
