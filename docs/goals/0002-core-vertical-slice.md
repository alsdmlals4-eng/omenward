# Goal 0002 — 핵심 수직 슬라이스

> 상태: **Goal 0001 구현 완료 및 별도 Plan Mode 제안서 승인 후 구체화**

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
→ 암살자 우회 침투 또는 성문 공성
```

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
- 현재 Phase 0 구현 Issue·승인 제안서·PR 결과

## 초기 포함 범위

### 전장

- 좌우 대칭 본진 2개.
- 상·중·하 독립 3라인.
- 각 본진의 라인별 성문 3개.
- 각 진영·각 라인의 중간거점.
- 각 중간거점의 전방 건설 노드 2개와 후방 건설 노드 1개.
- 각 라인의 다른 길과 연결되지 않는 중앙 접전지.
- 일반 횡단로와 기본 라인 변경 없음.
- 주 도로와 성문·중간거점 전방의 넓은 전투 공간.
- 기본 전략 줌에서 전장 전체 표시, 별도 미니맵 없음.

### 점령·건설·경제

- 중앙 접전지 점령.
- 중간거점 점령 상태와 건설권·기본 생산권 이전.
- 최소 한 종류의 전방 건물과 후방 경제 건물.
- 건물과 최대 점유 영역이 도로를 침범하지 않는 검증.
- 기본 금화·식량·접전지 수입·거점 기본 생산.

### 병력·전투

- 검사 또는 방패병 더미 전열.
- 원거리 또는 지원형 더미 후열.
- 공성 역할 더미와 라인별 성문 피해.
- 암살자 더미를 아군 측에 배치하면 같은 라인의 안개 우회로로 이동.
- 암살자는 적 후방에 직접 생성하지 않음.
- 우회로는 암살자 선택·배치 중에만 표시.

### 룰렛·공세

- 건물 토큰이 반영되는 최소 3×3 룰렛.
- 결과 보관과 라인 배치의 최소 흐름.
- 베일의 징조 뒤 지정 라인으로 진입하는 적 더미 웨이브.
- 디버그 표시로 라인 ID, 유닛 수, 포탑 사거리, 점령 상태, 성문 상태, 우회 경로 상태를 확인.

## 프로젝트 불변 조건

- 기본 포탑 한 기가 중간거점과 중앙 접전지 사이 전체를 단독으로 덮지 않는다.
- 건물 Tier가 아니라 완공된 건물 개수가 룰렛 토큰 수를 결정한다.
- 적은 플레이어와 같은 룰렛을 돌리지 않고 전조가 있는 웨이브를 생산한다.
- 상·중·하 라인의 일반 이동 그래프는 서로 연결되지 않는다.
- 각 중간거점은 전방 2·후방 1 노드를 유지한다.
- 점령된 중간거점의 건설권과 기본 생산권은 점령 진영으로 이전된다.
- 암살자는 같은 라인의 우회로를 사용하며 적 후방 직접 생성은 금지한다.
- 우회로는 평상시 안개로 가린다.
- 미니맵은 구현하지 않는다.
- 밸런스 수치는 코드에 흩어놓지 않고 데이터 책임 원본에서 읽는다.

## 제외 범위

- 최종 UI·아트·오디오.
- 플레이어 10병종 전체와 모든 등급 스킬.
- 전체 1~20웨이브.
- 모든 Tier 3 분기.
- 최종 암살자 탐지·대응 체계.
- 최종 성문 재건 규칙.
- 럭키 찬스와 최종 확률표.
- 저장·불러오기.
- 멀티플레이.
- C#, GDExtension, 외부 ECS.

## 완료 기준 초안

- 기본 전략 화면에서 미니맵 없이 세 라인의 성문·거점·접전지 상태를 파악할 수 있다.
- 일반 유닛이 다른 라인으로 이탈하지 않는다.
- 건물이 도로를 막지 않는다.
- 중간거점 점령 전후 건설권과 생산권이 전환된다.
- 암살자 선택 전에는 우회로가 보이지 않고, 선택·배치 중에는 출발 라인과 도착 후열을 확인할 수 있다.
- 암살자가 우회 시간을 거쳐 적 후열에 도착한다.
- 성문 세 개의 내구도와 파괴 상태가 독립적으로 동작한다.
- 동일 시드와 입력 로그로 핵심 결과를 재현할 수 있다.

세부 완료 기준, 파일 범위, 초기 수치와 성능 목표는 Goal 0001에서 실제 생성된 Godot 경로와 검증 명령을 확인한 뒤 Plan Mode 제안서에서 확정한다.
