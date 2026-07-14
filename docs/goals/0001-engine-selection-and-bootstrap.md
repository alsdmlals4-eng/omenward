# Goal 0001 — Godot 프로젝트 부트스트랩

> 상태: 엔진 승인 완료 / 구현 대기

@Superpowers Use this repository's spec-first workflow.
Do not edit files immediately. First inspect the repository and summarize the approved decisions, remaining questions, scope, risks, completion criteria, and verification commands.

## Goal

Godot + GDScript 기반의 최소 실행 프로젝트와 검증 루프를 만들어 이후 `Goal 0002 — 핵심 수직 슬라이스`를 안전하게 시작할 수 있게 한다.

## 사용자 가치

Codex와 공동 작업자가 같은 엔진 버전, 폴더 구조, 실행 명령과 검증 기준을 사용해 기능 구현보다 환경 차이 해결에 시간을 낭비하지 않는다.

## 먼저 읽을 문서

- `AGENTS.md`
- `docs/BASE_RULES_VERSION.md`
- `docs/DOCUMENTATION_MAP.md`
- `docs/GAME_DESIGN.md`
- `docs/GODOT_PROJECT_STRUCTURE.md`
- `docs/REFERENCE_REPOSITORIES.md`
- `docs/DECISIONS_PENDING.md`
- `docs/ROADMAP.md`
- `docs/ACTIVE_CONTEXT.md`

참고 저장소를 확인해야 할 때는 다음 범위만 읽는다.

- `alsdmlals4-eng/Base`: `AGENTS.md`, 작업 흐름·검증 관련 문서
- `alsdmlals4-eng/urban-legend`: `AGENTS.md`, `project.godot`, README의 폴더 구조, Godot UI·검증 관련 문서

## 승인된 결정

- 엔진: Godot
- 기본 언어: GDScript
- 공용 상태는 필요한 경우에만 AutoLoad 사용
- Godot 네이티브 Scene, Node, Resource, Signal, Control/Container/Theme 우선
- `.godot/` 및 로컬 생성물은 Git에서 제외

## 구현 전 사용자 확인이 필요한 항목

작업 시작 보고에서 아래 항목을 추천안과 함께 제시하고, 이미 Issue에서 확정됐다면 반복 질문하지 않는다.

- Godot 정확한 minor 버전: urban-legend와 동일한 4.7 stable 사용 여부
- Windows PC 우선 여부
- 기준 해상도와 16:9 정책
- 2D 또는 2.5D 카메라 방향
- 첫 프로토타입 최대 동시 유닛 수 목표

## Scope

- `project.godot` 생성
- 최소 메인 Scene과 진입 스크립트 생성
- `scenes/`, `scripts/`, `data/`, `resources/`, `tests/`, `assets/` 기본 구조 생성
- Godot용 `.gitignore` 확정
- README에 에디터 실행과 headless 검증 명령 추가
- 상태 소유, Scene 의존성, 데이터 파일 위치의 최소 계약 문서화
- 최소 headless 파싱 또는 실행 검증 구성

## Excluded

- 전투, 룰렛, 건설, 접전지, 웨이브 시스템 구현
- 외부 애드온 설치
- 유료 에셋 또는 플러그인 선택
- C#, GDExtension, ECS 도입
- 완성형 UI 및 아트
- 저장/불러오기

## 예상 구조

```text
project.godot
scenes/
  main/
scripts/
  core/
data/
resources/
tests/
assets/
docs/
```

필요하지 않은 빈 계층을 과도하게 만들지 않는다. 첫 실제 기능이 생길 때 하위 폴더를 확장한다.

## Completion

- [ ] 저장소 루트의 `project.godot`을 Godot 에디터에서 열 수 있다.
- [ ] 실행하면 최소 메인 Scene이 오류 없이 표시된다.
- [ ] Godot 정확한 버전과 실행 방법이 README에 기록된다.
- [ ] headless 검증 명령이 성공하고 종료 코드 0을 반환한다.
- [ ] `.godot/` 및 로컬 import 캐시가 추적되지 않는다.
- [ ] Scene, 스크립트, 데이터와 AutoLoad 상태 소유 기준이 문서화된다.
- [ ] Goal 0002가 실제 생성 경로와 검증 명령을 참조하도록 갱신된다.

## Verification

최종 명령은 확정한 Godot 실행 파일명에 맞춘다. 최소 검증 예시는 다음과 같다.

```bash
godot --headless --path . --editor --quit
```

추가로 수행한다.

- `git diff --check`
- 에디터에서 프로젝트 열기
- 메인 Scene 실행
- Git 상태에서 `.godot/` 미추적 확인

## Report

- 확정한 Godot 버전과 이유
- 생성·수정 파일과 역할
- 실행한 명령과 실제 결과
- 에디터 수동 확인 결과
- 미검증 항목과 남은 위험
- Goal 0002 시작 전 필요한 후속 결정
- Base 승격 후보