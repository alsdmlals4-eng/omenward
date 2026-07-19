# Goal 0002 — 핵심 수직 슬라이스

> 상태: **구현 완료 / PR 검토·수동 QA 대기**

@Superpowers Use this repository's spec-first workflow.
Do not edit files immediately. First inspect the completed Phase 0 project, current Issue, actual paths and verification commands, then submit a Plan Mode proposal using `docs/PROPOSAL_WORKFLOW.md`.

## Goal

한 개의 Godot 테스트 맵에서 오멘워드의 핵심 루프, 공용 병종 데이터와 최소 전투 연출을 검증한다.

```text
베일의 징조
→ 건설
→ 룰렛
→ 병력 배치
→ 3라인 교전
→ 중앙 접전지·중간거점 점령
→ 암살자 우회
→ 라인별 성문 공성
→ 스테이지 승리
```

## 선행 조건

- Issue #1 Phase 0 제안서 승인.
- 승인된 Phase 0 구현 완료.
- 실제 Godot 버전, 폴더, Resource와 headless 명령 확정.
- 공용 UnitArchetype·FactionVisual·AnimationContract 골격 존재.
- Issue #32에서 수직 슬라이스 Plan Mode 제안서 작성.

## 먼저 읽을 문서

1. `AGENTS.md`
2. `docs/BASE_RULES_VERSION.md`
3. `docs/HANDOFF_CONTEXT.md`
4. `docs/DOCUMENTATION_MAP.md`
5. `docs/PROPOSAL_WORKFLOW.md`
6. `docs/OMENWARD_GAME_DESIGN.md`
7. `docs/design/APPROVED_PREPRODUCTION_POC_BASELINE_V1.md`
8. `docs/design/APPROVED_SHARED_UNIT_ARCHETYPE_AND_FACTION_VISUAL_DATA_V1.md`
9. `docs/design/APPROVED_BATTLEFIELD_TOPOLOGY_AND_SCALE_V1.md`
10. `docs/design/APPROVED_UNIT_ANIMATION_AND_BATTLE_PRESENTATION_GUIDE_V1.md`
11. `docs/design/APPROVED_ART_DIRECTION_AND_PRODUCTION_GUIDE_V1.md`
12. `docs/design/APPROVED_UI_ART_AUDIO_POC_BIBLE_V1.md`
13. `docs/design/APPROVED_PERFORMANCE_DATA_TEST_READINESS_POC_V1.md`
14. `docs/GODOT_PROJECT_STRUCTURE.md`
15. `docs/REFERENCE_REPOSITORIES.md`
16. `docs/goals/0001-engine-selection-and-bootstrap.md`
17. Issue #1·#21·#29·#30·#32·#33
18. Phase 0 실제 파일과 검증 결과

## 포함 범위

### 전장

- 좌우 대칭 본진 2개.
- 상·중·하 독립 3라인.
- 각 본진의 라인별 성문 3개.
- 각 진영·각 라인의 중간거점.
- 각 중간거점 전방 2·후방 1 건설 노드.
- 각 라인의 독립 중앙 접전지.
- 일반 횡단로와 기본 라인 변경 없음.
- 기본 전략 줌에서 전체 전장 표시, 미니맵 없음.

### 점령·건설·경제

- 중앙 접전지 점령.
- 중간거점 중립화·점령·안정화와 건설권·생산권 이전.
- 최소 전방 방어 건물 1종, 후방 경제 건물 1종.
- 건물·최대 점유 영역의 도로 침범 검증.
- 기본 금화·식량·접전지·거점 수입.

### 공용 병종 데이터

전투 데이터는 공용 archetype만 사용한다.

```text
UnitArchetypeProfile
+ TierProfile
+ RankProfile
+ owner_team_id
+ FactionVisualProfile
```

- 대표 archetype 3~5종을 구현한다.
- 각 대표 archetype을 아군 Visual Set과 적군 Visual Set으로 각각 생성한다.
- 같은 archetype·Tier·Rank의 양 진영 유닛은 동일한 전투 결과를 낸다.
- 적군용 별도 UnitProfile·스탯·스킬·타기팅·AnimationContract를 만들지 않는다.
- 적 웨이브는 공용 `archetype_id`에 enemy 팀과 veil Visual Set을 지정한다.

### 대표 역할

- 전열: 방패병 또는 검사형.
- 원거리: 궁병.
- 침투: 암살자.
- 지원: 사제.
- 공성: 거인 또는 대형 더미.

모든 역할을 동시에 완성할 필요는 없지만, 최소한 전열·원거리와 암살자 또는 공성 중 하나를 포함한다.

### 최소 애니메이션·연출

```text
deploy
idle
move
attack_basic
skill_1 또는 역할 특수 행동
hit_light
death
capture 또는 점령 대기
victory
```

- 암살자: `bypass_enter`, `bypass_exit`.
- 거인·공성: `structure_attack`.
- 공격은 준비→판정→회복.
- 접촉·투사체 발사와 실제 판정 오차 한 프레임 이내.
- 이동 위치는 코드가 소유하고 루트 모션을 사용하지 않는다.
- 같은 archetype의 양 진영 이미지 시트는 상태·프레임·피벗·이벤트를 공유한다.
- 같은 병종 다수의 루프는 결정론적 프레임 오프셋을 사용한다.
- 웨이브 정리는 짧은 무기 정리만, 최종 승리에만 2.5~4초 시퀀스.

### 룰렛·공세

- 완공 건물 토큰이 반영되는 최소 3×3 룰렛.
- 결과 보관과 라인 배치.
- 룰렛 결과는 공용 archetype ID와 Rank를 생성.
- 베일의 징조 뒤 공용 archetype 기반 최소 적 웨이브.
- 디버그 표시: 라인, 팀, archetype, Visual Set, Unit 수, 사거리, 점령, 성문, 우회, 애니메이션 상태와 판정 이벤트.

## 승인된 초기값

### 중간거점

```text
neutralize_seconds_at_power_1 = 10.0
capture_seconds_at_power_1 = 10.0
max_effective_capture_power = 2.0
progress_hold_after_exit = 3.0
progress_revert_rate = 10% / sec
stabilization_seconds = 5.0
owned_income = gold +2 / 30 sec
```

- 방패·수호형 1.25.
- 일반 근접·기병 1.0.
- 원거리·지원·거인 0.5.
- 암살자·비행·순수 공성 0.
- 점령 시도 중 생산·건설·업그레이드 정지.
- 중립화 시 기존 건물 비활성.
- 점령 완료 시 기존 건물 폐허화, 환불 없음.
- 안정화 후 새 소유자의 건설·생산 활성.

### 성문

```text
max_hp = 5000
armor = 80
magic_resistance = 80
normal_structure_damage_multiplier = 0.40
siege_structure_damage_multiplier = 2.00
fixed_structure_damage_multiplier = 0.50
collapse_duration = 2.0 sec
```

- 같은 팀 통과, 적 차단.
- 군중제어·밀쳐내기·비율 피해 면역.
- 폐허 충돌 없음.
- 수직 슬라이스에서 수리·재건 없음.

### 암살자

```text
entry_windup = 1.0 sec
travel_duration = 9.0 sec
defender_warning_before_arrival = 2.5 sec
arrival_recovery = 0.6 sec
exit_offset = enemy midpoint toward base 120 units
exit_zone_size = 160 × 120 units
blocked_fallback_radius = 80 units
capture_power = 0
```

- 진입 확정 뒤 취소·후퇴 불가.
- 우회 중 전투·점령·피격·버프 없음.
- 경로는 선택·배치 중에만 표시.
- 탐지 전용 건물 제외.

### 일반 인간형 모션 첫 가설

```text
idle = 4~6 frames
move = 6~8 frames
attack_basic = 6~10 frames
skill_1 = 8~14 frames
hit_light = 2~3 frames
death = 6~10 frames
victory = 8~14 frames
stage_victory_sequence = 2.5~4.0 sec
```

정확한 FPS, 프레임, 이벤트, 흔들림은 실제 모션 테스트로 조정한다.

## 프로젝트 불변 조건

- 기본 포탑 한 기가 중간거점과 중앙 접전지 사이 전체를 단독으로 덮지 않는다.
- 완공된 건물 개수가 룰렛 토큰 수를 결정한다.
- 적은 플레이어 룰렛을 돌리지 않고 웨이브로 출격한다.
- 상·중·하 일반 이동 그래프는 연결되지 않는다.
- 중간거점은 전방 2·후방 1 노드를 유지한다.
- 점령된 중간거점의 건설권·생산권은 점령 팀으로 이전된다.
- 암살자는 같은 라인 우회로를 사용하고 후방 직접 생성은 금지한다.
- 미니맵을 구현하지 않는다.
- 공용 UnitArchetype 수는 10개다.
- 적군용 별도 UnitProfile·Scene·전투 데이터·AnimationContract를 만들지 않는다.
- `visual_faction_id`는 능력치와 판정을 변경하지 않는다.
- 모든 밸런스와 애니메이션 이벤트는 책임 데이터에서 읽는다.
- 다수 전투에서 매 타격마다 큰 히트 스톱·화면 흔들림을 사용하지 않는다.

## 제외 범위

- 최종 UI·아트·오디오.
- 공용 10병종 전체와 모든 등급 스킬.
- 별도 적군 10병종 데이터·모션 제작.
- 전체 W1~20.
- 모든 Tier 3.
- 전체 양 진영 Visual Set 완성.
- 암살자 탐지 건물.
- 성문 수리·재건.
- 최종 룰렛 확률.
- 저장·불러오기, 멀티플레이.
- C#, GDExtension, 외부 ECS.

## 완료 기준

### 공용 데이터

- UnitArchetypeProfile이 정확히 10개 확장 구조를 따른다.
- 수직 슬라이스 대표 archetype에 아군·적군 Visual Set이 존재한다.
- 같은 archetype·Tier·Rank의 양 진영 전투 수치와 결과가 동일하다.
- `visual_faction_id`만 변경해 같은 Unit Scene에서 이미지가 바뀐다.
- 적군 전용 스탯·스킬·타기팅·AnimationContract 복사본이 없다.
- 웨이브가 공용 archetype ID를 참조한다.

### 전장

- 미니맵 없이 세 라인의 성문·거점·접전지 상태를 파악한다.
- 일반 유닛이 다른 라인으로 이탈하지 않는다.
- 건물이 도로를 막지 않는다.
- 중간거점 점령 전후 생산·건설권이 정확히 전환된다.
- 기존 건물이 중립화 시 비활성, 적 점령 완료 시 폐허화된다.
- 성문 세 개의 HP와 파괴 상태가 독립적으로 동작한다.
- 공성 태그가 일반 병력보다 성문에 유의미하게 강하다.
- 암살자 선택 전 우회로가 보이지 않는다.
- 암살자가 1초 진입 후 9초 이동을 거쳐 적 후열에 나타난다.
- 수비 측에 2.5초 전 경고가 표시된다.

### 모션·가독성

- 0.85배 줌에서 이동·공격으로 대표 역할과 진영을 구분한다.
- 양 진영 Visual Set의 상태·프레임·피벗·이벤트가 일치한다.
- 판정과 접촉·발사 이벤트 오차가 한 프레임 이내다.
- 가벼운 연속 피격이 공격 모션을 계속 끊지 않는다.
- 같은 병종 다수가 완전히 동일한 루프로 움직이지 않지만 동일 시드에서 재현된다.
- 성문 붕괴와 스테이지 승리가 승인 시간 안에 완료된다.

### 결정론·성능

- 동일 시드와 입력 로그로 핵심 결과를 재현한다.
- 정상 객체 목표에서 목표 프레임을 검증한다.
- 누락·중복·잘못된 참조가 실행 전에 검출된다.

세부 파일 경로와 Scene 구조는 Phase 0 구현 뒤 Issue #32 제안서에서 확정한다.
