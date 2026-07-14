# Goal 0001 — 엔진 선정과 프로젝트 부트스트랩

> 상태: 사용자 승인 전 / 탐색 작업

@Superpowers Use this repository's spec-first workflow.
Do not create an engine project until the user approves the recommendation.

## Goal

`docs/GAME_DESIGN.md`의 3라인 실시간 오토배틀, 다수 유닛, 노드 건설, 데이터 기반 룰렛을 구현하기 적합한 엔진을 비교하고 한 가지를 추천한다.

## 먼저 읽을 문서

- `AGENTS.md`
- `docs/GAME_DESIGN.md`
- `docs/DECISIONS_PENDING.md`
- `docs/ROADMAP.md`
- `docs/BASE_RULES_VERSION.md`

## Scope

- Godot와 Unity를 최소 비교
- 2D 다수 유닛, 경로 이동, UI, 데이터 리소스, 헤드리스 테스트, Codex 편집성을 평가
- 목표 Windows MVP를 가정한 추천안 작성
- 선택 후 생성될 예상 폴더 구조와 검증 명령 제안

## Excluded

- 엔진 프로젝트 생성
- 에셋 설치
- 게임 시스템 구현
- 유료 플러그인 선택

## Completion

- 비교 기준과 근거가 문서화된다.
- 추천 엔진 1개와 선택하지 않은 대안의 이유가 명확하다.
- 사용자 승인에 필요한 질문이 5개 이하로 정리된다.
- 승인 전 저장소에 엔진 산출물이 추가되지 않는다.

## Verification

- 추천 기능이 해당 엔진의 공식 기능으로 가능한지 확인한다.
- 요구되는 추가 플러그인과 라이선스를 구분한다.

## Report

- 추천 결과
- 비교표
- 예상 위험
- 사용자 결정 필요 항목
- 다음 Goal 초안
