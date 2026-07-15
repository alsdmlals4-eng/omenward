# Goal 0002 — 핵심 수직 슬라이스

> 상태: **수직 슬라이스 Plan Mode 준비 완료 / Goal 0001 Phase 0 완료 및 별도 사용자 승인 전 구현 금지**

@Superpowers Use this repository's spec-first workflow.
Do not edit files immediately. First inspect the completed Godot project, current Issue, actual paths and verification commands, then submit a Plan Mode proposal using `docs/PROPOSAL_WORKFLOW.md`.

## Goal

한 개의 Godot 테스트 맵에서 오멘워드의 핵심 루프를 검증한다.

```text
베일의 징조 확인
→ 건설
→ 룰렛
→ 병력 배치
→ 3라인 교전
→ 중앙 접전지·중간거점 점령
→ 암살자 우회 침투
→ 라인별 성문 공성
```

## 선행 조건

- Issue #1의 Phase 0 Plan Mode 제안서 승인.
- 승인된 Phase 0 구현 완료.
- 실제 Godot stable 버전·폴더 구조·headless 실행 명령 확정.
- Issue #32에서 수직 슬라이스 Plan Mode 제안서 작성.

## 먼저 읽을 문서

- `AGENTS.md`
- `docs/DOCUMENTATION_MAP.md`
- `docs/DOCUMENT_LIFECYCLE.md`
- `docs/PROPOSAL_WORKFLOW.md`
- `docs/OMENWARD_GAME_DESIGN.md`
- `docs/design/APPROVED_PREPRODUCTION_POC_BASELINE_V1.md`
- `docs/design/APPROVED_BATTLEFIELD_TOPOLOGY_AND_SCALE_V1.md`
- `docs/design/APPROVED_UI_ART_AUDIO_POC_BIBLE_V1.md`
- `docs/design/APPROVED_PERFORMANCE_DATA_TEST_READINESS_POC_V1.md`
- `docs/GODOT_PROJECT_STRUCTURE.md`
- `docs/REFERENCE_REPOSITORIES.md`
- `docs/goals/0001-engine-selection-and-bootstrap.md`
- Issue #1·#21·#29·#30·#32

## 포함 범위

### 전장

- 좌우 대칭 본진 2개.
- 상·중·하 독립 3라인.
- 각 본진의 라인별 성문 3개.
- 각 진영·각 라인의 중간거점.
- 각 중간거점의 전방 건설 노드 2개와 후방 건설 노드 1개.
- 각 라인의 다른 길과 연결되지 않는 중앙 접전지.
- 일반 횡단로와 기본 라인 변경 없음.
- 기본 전략 줌에서 전장 전체 표시, 별도 미니맵 없음.

### 점령·건설·경제

- 중앙 접전지 점령.
- 중간거점 점령 상태와 건설권·기본 생산권 이전.
- 최소 전방 방어 건물 1종과 후방 경제 건물 1종.
- 건물과 최대 점유 영역이 도로를 침범하지 않는 검증.
- 기본 금화·식량·접전지 수입·거점 기본 생산.

### 병력·전투

- 검사 또는 방패병 더미 전열.
- 원거리 또는 지원형 더미 후열.
- 공성 역할 더미와 라인별 성문 피해.
- 암살자 더미의 선택·우회 이동·후열 출현.
- 암살자 적 후방 직접 생성 금지.

### 룰렛·공세

- 건물 토큰이 반영되는 최소 3×3 룰렛.
- 결과 보관과 라인 배치의 최소 흐름.
- 베일의 징조 뒤 지정 라인으로 진입하는 적 더미 웨이브.
- 디버그 표시: 라인 ID, 유닛 수, 포탑 사거리, 점령 상태, 성문 상태, 우회 상태.

## 승인된 초기값

### 중간거점

```text
neutralize_seconds_at_power_1 = 10.0
capture_seconds_at_power_1 = 10.0
max_effective_capture_power = 2.0
progress_hold_after_exit = 3.0
progress_revert_rate = 10% / 초
stabilization_seconds = 5.0
owned_income = 금화 +2 / 30초
```

- 방패·수호형 1.25.
- 일반 근접·기병 1.0.
- 원거리·지원·거인 0.5.
- 암살자·비행·순수 공성 병기 0.
- 점령 시도 중 생산·신규 건설·업그레이드 정지.
- 중립화 시 기존 건물 비활성.
- 점령 완료 시 기존 건물 폐허화, 환불 없음.
- 5초 안정화 후 새 소유자의 건설과 생산 활성.

### 성문

```text
max_hp = 5000
armor = 80
magic_resistance = 80
normal_structure_damage_multiplier = 0.40
siege_structure_damage_multiplier = 2.00
fixed_structure_damage_multiplier = 0.50
collapse_duration = 2.0초
```

- 아군 통과, 적 차단.
- 군중제어·밀치기·비율 피해 면역.
- 폐허 충돌 없음.
- 수직 슬라이스에서 수리·재건 없음.

### 암살자 우회로

```text
entry_windup = 1.0초
travel_duration = 9.0초
defender_warning_before_arrival = 2.5초
arrival_recovery = 0.6초
exit_offset = 적 중간거점에서 본진 방향 120 units
exit_zone_size = 160 × 120 units
blocked_fallback_radius = 80 units
capture_power = 0
```

- 진입 확정 뒤 취소·후퇴 불가.
- 우회 중 전투·점령·피격·버프 없음.
- 우회 경로는 선택·배치 중에만 표시.
- 탐지 전용 건물은 제외.

## 프로젝트 불변 조건

- 기본 포탑 한 기가 중간거점과 중앙 접전지 사이 전체를 단독으로 덮지 않는다.
- 완공된 건물 개수가 룰렛 토큰 수를 결정한다.
- 적은 플레이어와 같은 룰렛을 돌리지 않고 전조가 있는 웨이브를 생산한다.
- 상·중·하 일반 이동 그래프는 서로 연결되지 않는다.
- 중간거점은 전방 2·후방 1 노드를 유지한다.
- 점령된 중간거점의 건설권과 생산권은 점령 진영으로 이전된다.
- 암살자는 같은 라인의 우회로를 사용하며 적 후방 직접 생성은 금지한다.
- 미니맵은 구현하지 않는다.
- 모든 밸런스 값은 데이터 책임 원본에서 읽는다.

## 제외 범위

- 최종 UI·아트·오디오.
- 플레이어 10병종 전체와 모든 등급 스킬.
- 전체 1~20웨이브.
- 모든 Tier 3 분기.
- 암살자 탐지 건물과 추가 대응 체계.
- 성문 수리·재건.
- 최종 룰렛 확률표.
- 저장·불러오기, 멀티플레이.
- C#, GDExtension, 외부 ECS.

## 완료 기준

- 미니맵 없이 세 라인의 성문·거점·접전지 상태를 파악한다.
- 일반 유닛이 다른 라인으로 이탈하지 않는다.
- 건물이 도로를 막지 않는다.
- 중간거점 점령 전후 생산·건설권이 정확히 전환된다.
- 기존 건물이 중립화 시 비활성되고 점령 완료 시 폐허화된다.
- 성문 세 개의 HP와 파괴 상태가 독립적으로 동작한다.
- 공성 태그가 일반 병력보다 성문에 유의미하게 강하다.
- 암살자 선택 전에는 우회로가 보이지 않는다.
- 암살자가 1초 진입 후 9초 이동을 거쳐 적 후열에 나타난다.
- 수비 측에 도착 2.5초 전 경고가 표시된다.
- 동일 시드와 입력 로그로 핵심 결과를 재현한다.

세부 파일 경로와 Scene 구조는 Goal 0001에서 실제 Godot 기반이 생성된 뒤 Issue #32의 Plan Mode 제안서에서 확정한다.
