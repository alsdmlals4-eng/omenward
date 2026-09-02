# [Approved] OMENWARD Five Sequential Front Maps

```yaml
decision_id: OMW-PLAN-20260902-FIVE-SEQUENTIAL-FRONT-MAPS-01
approved_at: 2026-09-02 KST
approval_source: USER_CHAT__2026-09-02__"전선맵을_5단계로_나누면_될거같다...하나의_전선을_이기면_다음_전선_맵으로_넘어가는_식"
status: USER_CONFIRMED__RESEARCHED__FEASIBLE__SPECIFIED__DOMAIN_AND_UI_IMPLEMENTED__MACHINE_VERIFIED__LIVE_REGULAR_TRANSITION_NOT_RUN__MAP_ART_CANDIDATES_AWAITING_USER_VISUAL_CONFIRMATION__HUMAN_NOT_RUN
supersedes_in_scope: OMW-PLAN-20260830-BATTLE-PRIMARY-MARCH-MINIMAP-01__FIVE_SECTOR_CONTEXT_ONLY
retains: SINGLE_ACTIVE_FRONT / THREE_WORK_TABS / GLOBAL_BUILDING_ROSTER / ONE_FIXED_TOWER / BATTLE_PRIMARY_SURFACE
runtime_evidence: LIVE_ENTRY_SMOKE_PASS__REGULAR_SEQUENTIAL_TRANSITION_NOT_RUN
human_evidence: NOT_RUN
```

## 1. Decision

상단의 `수호 성채 → 수호 전진 → 접전 → 장막 전진 → 베일 성채` 리본은 더 이상
단순 위치 표지가 아니다. 각 구간은 서로 다른 지형·파도 묶음·전투 결과를 가진 **독립 전선 맵**이며,
한 번에 현재 맵 하나만 실제 전투 화면에 열린다.

```text
FRONT_MAP_COUNT = 5
ACTIVE_BATTLE_MAP_COUNT = 1
MAP_ORDER = WARD_CITADEL -> WARD_FORWARD -> CLASH -> VEIL_FORWARD -> VEIL_CITADEL
MAP_UNLOCK_RULE = CURRENT_MAP_VICTORY_UNLOCKS_EXACTLY_NEXT_MAP
MAP_SELECTION_AHEAD_OF_CURRENT = FORBIDDEN
PARALLEL_FRONT_MAPS = FORBIDDEN
FINAL_RUN_VICTORY = VEIL_CITADEL_MAP_VICTORY_ONLY
CURRENT_MAP_DEFEAT = NO_FUTURE_MAP_UNLOCK
```

이는 세 전선을 복구하거나 하나의 긴 길을 다시 그리는 결정이 아니다. 한 방향의 한 진군을
읽기 쉬운 다섯 개 전투장으로 나누는 결정이다.

## 2. Player flow

```text
현재 맵 PREPARE
  -> 룰렛 / 전역 로스터 / 비가역 단일 전선 커밋
  -> 현재 맵 BATTLE
  -> 현재 맵 승리 REVIEW
  -> "다음 전선 진입" 명시 행동
  -> 다음 맵 PREPARE

다섯 번째 맵 승리
  -> 최종 REVIEW / StageRun VICTORY
```

맵 1~4의 승리는 Stage 전체의 `VICTORY`가 아니다. `REVIEW`에서 현재 맵을 완료로 기록하고
정확히 하나의 다음 맵만 해금한다. 명시 CTA를 누르기 전에는 자동으로 순간이동하지 않는다.
패배 시에는 현재 맵 이후를 해금하지 않으며, 기존 재시작 경로는 같은 Stage의 최초 맵부터 다시
시작한다. 이 수직 슬라이스에는 이미 끝낸 개별 맵을 임의 선택·재생하는 별도 메뉴를 만들지 않는다.

## 3. Retained boundaries

| Boundary | Retained rule |
|---|---|
| 전선 | 항상 하나의 활성 전선 `front`만 존재한다. |
| 건물 | 지도에 배치하지 않는다. `6 + 안정 점령지`, 최대 9칸 전역 로스터만 유지한다. |
| 방어탑 | 현재 활성 전선에 고정 방어탑은 정확히 1개다. 맵마다 탑을 누적하거나 건설하지 않는다. |
| 전투 화면 | BATTLE은 현재 맵의 가까운 전투 장면이 주 화면이며, 상단 리본은 상태/해금 맥락만 보여 준다. |
| 룰렛 | 3×3 플레이어 구성 확률 엔진, 비가역 단일 전선 커밋, 카지노 표현 금지는 변하지 않는다. |
| 지형 | 중앙 병력 이동 회랑은 계속 비워 둔다. 전장 건물·건설 노드·울타리·바리케이드·이동을 막는 강은 금지한다. |

## 4. Content and visual packet

각 맵은 단순 색상 변형이 아니라 다음의 서로 다른 전장 목적을 가져야 한다. 새 배경은 실제
`BattleFocusView` consumer와 Visual Requirement가 연결된 후보로 먼저 생성하고, 후보/사용자
확정/정본 등록/런타임 검증 상태를 구분한다.

| Order | Map ID | Player label | Terrain direction | Runtime wave package |
|---:|---|---|---|---|
| 1 | `ward_citadel` | 수호 성채 | 밝은 수호 성채 외곽과 넓은 초지, 성벽은 측면에만 | W1–W4 |
| 2 | `ward_forward` | 수호 전진 | 낮은 석판·푸른 꽃·전진 초지, 중앙 통로는 비움 | W5–W8 |
| 3 | `clash` | 접전 | 짓밟힌 황토 초지와 멀리 흩어진 깃발/잔해, 장애물 없음 | W9–W12 |
| 4 | `veil_forward` | 장막 전진 | 보랏빛 황혼·장막 수정/가시가 외곽에만 있는 진군로 | W13–W16 |
| 5 | `veil_citadel` | 베일 성채 | 어두운 보랏빛 현무암 접근로와 멀리 보이는 성채 윤곽 | W17–W20 |

`regular_stage`의 기존 스무 Wave는 각 맵 네 Wave씩으로 보존한다. 그러므로 기존 W15
전설 적 처치는 맵 4의 종료 조건이 아니라 그 맵의 위협 일부이고, 최종 승리는 W17–W20이 속한
베일 성채 맵을 끝낸 뒤에만 일어난다. 기존 네 Wave tutorial은 빠른 입문 Stage로 보존하며,
다섯 맵 캠페인 구조의 완전한 검증 대상은 regular Stage다. tutorial을 억지로 다섯 Wave로
바꾸어 오래된 입문 계약·밸런스 가정을 조용히 바꾸지 않는다.

## 5. Research comparison

| Source pattern | Adopt / Adapt / Reject | OMENWARD application |
|---|---|---|
| Bad North의 서로 다른 전술 지형 | ADAPT | 다섯 맵은 서로 다른 전장 읽기와 파도 묶음을 가져야 하며 단순 재색칠이 아니다. 격자·섬 선택은 도입하지 않는다. |
| The Last Spell의 서로 다른 Haven/최종 맵 해금 | ADAPT | 완료한 맵만 다음 맵을 열고, 마지막 맵만 run 결과를 확정한다. 턴제·도시 복구는 도입하지 않는다. |
| Kingdom Two Crowns의 한 방향 준비·방어·진군 | ADAPT | 하나의 수호→장막 진군 방향과 전역 준비의 인과만 취한다. 벽·전장 건설은 금지한다. |
| 기존 Slotbound/Commander Quest 벤치마크 | RETAIN | 현재 전투 하나 + 맥락 하나, 준비한 조합의 자동전투 결과, 제한된 전역 로스터를 유지한다. |

## 6. Implementation contract

`StageRun`이 `front_map_index`, 각 맵의 `locked/current/cleared` 상태, 다음 맵 진입 전이,
그리고 final-only Stage victory를 소유한다. `WaveDirector`는 활성 맵의 Wave package만
시간을 진행하며, 다음 맵 입장 때 그 맵의 Wave package로 새로 만들어진다. 전역 경제와
건물 로스터는 새로 만들지 않으며, 맵 전용 BattleSimulator/적 상태와 WaveDirector만
다음 맵에 맞게 초기화한다.

필수 기계 계약은 다음을 포함한다.

1. 새 regular run은 5개 상태 중 1번만 current, 나머지는 locked다.
2. 맵 1~4 승리는 `REVIEW`에 머물고 final `VICTORY`나 Stage progression을 기록하지 않는다.
3. `enter_next_front_map()`은 정확히 다음 맵 하나만 열고 `PREPARE`로 되돌린다.
4. 전역 경제/로스터는 다음 맵 전환에도 보존되고, 다음 맵의 battle/waves만 새 상태다.
5. 5번 맵의 승리만 Stage progression을 기록한다.
6. 상단 리본은 5개 맵의 `cleared/current/locked` 상태를 읽기 전용으로 표시하며, 유닛/전투를 복제하지 않는다.
7. 한 front, 한 고정탑, 지도 건물 금지, 중앙 이동 회랑 규칙이 유지된다.
8. 적 본진이 일찍 파괴되어도 아직 도착하지 않은 현재 맵 Wave package를 건너뛸 수 없다. 해당 package가 전부 발생하고 살아 있는 베일 병력이 해소되어야 맵 승리를 기록한다. 전환 순간 우회 중인 살아 있는 루메른 병력도 다음 맵 진입 병력으로 보존한다.

## 7. Evidence ceiling and rollback

이 Decision은 명시 사용자 승인과 현재 code/data architecture의 feasibility를 가진다. 전용 Godot
계약과 full machine suites는 통과했지만, live regular-map handoff와 사람 가독성 PASS는 아직
주장하지 않는다. `docs/qa/OMENWARD_FIVE_SEQUENTIAL_FRONT_MAPS_RUNTIME_SMOKE_2026-09-02.md`는
튜토리얼 entry만의 기술적 실행 증거이며, 다섯 맵 후보 이미지는 여전히 user confirmation 전이다.
rollback은 이 Decision으로
추가하는 `FrontMapDefinition`, stage wave ownership, `StageRun` map state, top ribbon state,
review CTA, map-specific terrain consumer, tests와 새 assets에 국한한다. 보호된 main과 기존
사용자 잠금 자산은 변경하지 않는다.
