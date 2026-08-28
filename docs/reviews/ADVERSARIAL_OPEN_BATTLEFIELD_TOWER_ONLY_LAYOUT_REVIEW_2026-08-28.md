# OMENWARD · 열린 전장 / 탑 전용 배치 적대적 검토

```yaml
review_id: OMW-REV-20260828-OPEN-BATTLEFIELD-TOWER-ONLY-01
date: 2026-08-28
result: PASS_5_OF_5__PLANNING_SCOPE_ONLY
decision_id: OMW-PLAN-20260828-OPEN-BATTLEFIELD-TOWER-ONLY-01
board: OMW-VISUAL-BOARD-20260828-STORYBOOK-SD-THREE-FRONT-01__V6_OPEN_BATTLEFIELD_NO_BARRICADE
runtime: NOT_RUN
human_usability: NOT_RUN
player_experience: NOT_RUN
visual_lock: USER_CONFIRM_PENDING
```

| Loop | Failure assumption | Evidence and correction | Result |
|---|---|---|---|
| 1 | 열린 전장이 바리케이드의 시간을 잃어 core choice를 약화한다 | 고정탑은 국소 보조 화력만 제공하고 점령력/solo clear를 만들지 않는다. 비가역 커밋과 룰렛 설계가 주 선택으로 남는다. | PASS |
| 2 | 세 전선 구조나 각 거점 수량이 사라진다 | current owner와 v6 record에 본진 4 pad/2 tower, 각 전진기지 2 pad/1 tower, 양 진영 대칭, 세 접전지를 명시했다. | PASS |
| 3 | “자유로운”이 freeform terrain build로 scope 폭증한다 | `DISCOVERABLE_FIXED_PADS_IN_OPEN_TERRAIN__NOT_FREEFORM_TERRAIN_GRID`으로 고정했다. Cataclismo식 벽 조립은 REJECT다. | PASS |
| 4 | 이미지가 코드 구현/PASS로 오인된다 | actual `stage_run.gd`의 3 node 등록, home/tower/map consumer 부재를 재대조했다. v6는 generated planning exploration이며 runtime/human/player는 `NOT_RUN`이다. | PASS |
| 5 | reference 복제 또는 전술 바리케이드의 우발적 삭제가 생긴다 | Commander Quest/Thronefall은 전장 밀도·지형 판단 원칙만 ADAPT했고 source 표현은 복제하지 않는다. `TACTICAL_COMMAND_BARRICADE`는 out-of-scope retained다. | PASS |

## Decision quality

```text
ADOPT = OPEN_TERRAIN_COMBAT_READABILITY / TERRAIN_INFORMS_DEFENSE_CHOICE
ADAPT = THREE_FRONT_OCCUPATION_WITH_DISCOVERABLE_FIXED_PADS
REJECT = FENCED_OUTPOST_VISUALS / FIXED_FORWARD_BARRICADE / FREEFORM_WALL_OR_TERRAIN_GRID
NEXT_VALIDATION = USER_CONFIRM_V6_THEN_PHASE2_RED_TEST_AND_TARGET_RESOLUTION_RUNTIME_QA
NO_BASE_PROMOTION = PROJECT_SPECIFIC_THREE_FRONT_OCCUPATION_AND_FIXED_PAD_LAYOUT
```

이 검토는 planning canon의 일관성만 판정한다. 시각 방향 lock, runtime implementation, Human usability, Player Experience, asset rights는 아직 통과하지 않았다.

## Validation evidence ceiling

- 이 변경과 직접 연결된 문서/정본 검증 119건은 통과했다.
- 전체 Python discovery 556건은 이번 작업의 code 변경 없이 실행했으며, `numpy` 미설치로 3개 오류, `_base_recovery` checkout 부재로 1개 실패, 이미 추적된 Godot CSV import/translation 산출물로 1개 실패가 남았다. 이 결과는 열린 전장 구현 PASS가 아니며, 기존 local environment/repository hygiene gap을 성공으로 승격하지 않는다. 관련 follow-up은 current open Issue inventory를 fresh 확인한다.
- Hera live-editor 상태는 다른 프로젝트(`urban-legend`)만 연결되어 있었으므로 Omenward Scene/runtime은 실행하지 않았다.
