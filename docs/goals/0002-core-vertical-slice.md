# Goal 0002 — 핵심 수직 슬라이스

> 상태: Godot Goal 0001 완료 후 구체화

@Superpowers Use this repository's spec-first workflow.
Do not edit files immediately. First inspect the completed Godot project, current Issue, actual paths and verification commands, then summarize scope, risks, completion criteria, and verification.

## Goal

한 개의 Godot 테스트 맵에서 3라인 이동, 건설 노드, 중앙 접전지, 기본 건물, 더미 룰렛, 적 전조 웨이브가 연결된 플레이 가능한 수직 슬라이스를 만든다.

## 먼저 읽을 문서

- `AGENTS.md`
- `docs/DOCUMENTATION_MAP.md`
- `docs/GAME_DESIGN.md`
- `docs/GODOT_PROJECT_STRUCTURE.md`
- `docs/REFERENCE_REPOSITORIES.md`
- `docs/goals/0001-engine-selection-and-bootstrap.md`
- 현재 Phase 0 구현 Issue와 PR 결과

## 초기 포함 범위

- 본진 2개
- 3개 라인과 충분한 이동 거리
- 플레이어 후방 6노드와 라인별 전방 3노드
- 라인별 접전지
- 검사 더미 유닛
- 농장, 시장, 검사 훈련소, 기본 포탑
- 기본 금화와 식량
- 건물 토큰이 반영되는 최소 3×3 룰렛
- 30초 뒤 상단으로 오는 적 검사 웨이브 전조
- 디버그 표시로 라인 id, 유닛 수, 포탑 사거리, 접전지 거리를 확인할 수 있는 기능

## 프로젝트 불변 조건

- 기본 포탑은 중앙 접전지에 닿지 않는다.
- 건물 티어가 아니라 완공된 건물 개수가 룰렛 토큰 수를 결정한다.
- 적은 룰렛을 돌리지 않고 전조가 있는 웨이브를 생산한다.
- 밸런스 수치는 코드에 흩어놓지 않고 한 책임 원본에서 읽는다.

## 제외 범위

- 최종 UI/아트
- 4병종 상성 완성
- 스킬북과 장비
- 럭키 찬스
- 저장/불러오기
- 멀티플레이
- C#, GDExtension, 외부 ECS

세부 완료 기준, 파일 범위와 성능 목표는 Goal 0001에서 실제 생성된 Godot 경로와 검증 명령을 확인한 뒤 갱신한다.