# Goal 0001 — Godot 프로젝트 부트스트랩 제안서

> 상태: **Codex Plan Mode 제안서 검토 대기 / 구현 금지**

@Superpowers Use this repository's spec-first workflow.
Use Codex Plan Mode for this pass.
Do not create or modify `project.godot`, Scene, script, Resource, data, asset, test, branch, commit, or pull request.
First inspect the repository and submit a proposal using `docs/PROPOSAL_WORKFLOW.md`.

## Goal

Godot + GDScript 기반 최소 실행 프로젝트를 어떤 버전·구조·검증 방식으로 부트스트랩할지 제안하고, 사용자가 검토할 수 있는 구현 계획을 작성한다.

이번 실행의 산출물은 **구현물이 아니라 제안서**다. 사용자가 제안서를 명시적으로 승인한 뒤 별도의 구현 실행으로 전환한다.

## 사용자 가치

Codex가 임의의 엔진 버전이나 폴더 구조를 먼저 고정하지 않고, 프로젝트의 실제 요구와 참고 저장소를 검토한 뒤 안전한 기술 기반을 합의한다.

## 먼저 읽을 문서

- `AGENTS.md`
- `docs/BASE_RULES_VERSION.md`
- `docs/DOCUMENTATION_MAP.md`
- `docs/PROPOSAL_WORKFLOW.md`
- `docs/GAME_DESIGN.md`
- `docs/GODOT_PROJECT_STRUCTURE.md`
- `docs/REFERENCE_REPOSITORIES.md`
- `docs/DECISIONS_PENDING.md`
- `docs/ROADMAP.md`
- `docs/ACTIVE_CONTEXT.md`
- GitHub Issue #1

참고 저장소는 필요한 파일만 읽는다.

- `alsdmlals4-eng/Base`: `AGENTS.md`, 작업 흐름·검증 관련 문서
- `alsdmlals4-eng/urban-legend`: `AGENTS.md`, `project.godot`, README의 폴더 구조, Godot UI·검증 관련 문서

## 승인된 결정

- 엔진: Godot
- 기본 언어: GDScript
- 공용 상태는 필요한 경우에만 AutoLoad 사용
- Godot 네이티브 Scene, Node, Resource, Signal, Control/Container/Theme 우선
- `.godot/` 및 로컬 생성물은 Git에서 제외
- 코드 작업 전 Codex Plan Mode 제안서와 사용자 승인 필수

## 제안서에서 검토할 결정

각 항목에 대해 **추천안, 이유, 대안의 장단점**을 제시한다.

- Godot 정확한 stable 버전: `urban-legend`와 동일한 4.7 stable 채택 여부
- Windows PC 우선 여부
- 기준 해상도와 16:9 정책
- 2D 또는 2.5D 카메라 방향
- 첫 프로토타입 최대 동시 유닛 수 목표와 성능 검증 방식
- 루트 폴더와 최소 Scene/스크립트/Data/Resource 구조
- AutoLoad를 처음부터 둘지, 첫 공유 상태가 생길 때 추가할지
- headless 검증 명령과 Windows 실행 파일 경로 처리
- 최소 메인 Scene이 보여줄 내용

## Plan Mode 포함 범위

- 현재 저장소 구조와 문서 간 불일치 확인
- Base와 urban-legend에서 적용 가능한 작업·Godot 구조 분석
- 정확한 예상 파일 목록과 각 파일의 책임 제안
- Godot Scene 트리, 상태 소유, Signal 연결의 최소 구조 제안
- 단계별 구현 순서 제안
- 검증 명령과 수동 확인 순서 제안
- 위험, 미확정 사항, 사용자 결정 요청 정리

## Plan Mode 제외 범위

- `project.godot` 생성·수정
- Scene, GDScript, Resource, 테스트 코드 생성·수정
- `.gitignore` 외 구현 파일 변경
- 외부 애드온·에셋·의존성 설치
- 구현 브랜치, 커밋, PR 생성
- 전투, 룰렛, 건설, 접전지, 웨이브 구현
- 승인되지 않은 기술 선택 확정

## 제안서 필수 내용

`docs/PROPOSAL_WORKFLOW.md` 형식을 사용하고 다음 내용을 구체적으로 포함한다.

- 확인한 실제 파일과 근거
- 추천 Godot 버전 및 대안
- 예상 Scene 트리
- 예상 파일 경로와 책임
- 상태 소유 및 AutoLoad 사용 여부
- 데이터/Resource 경계
- headless 및 에디터 검증 명령
- Phase 0 구현을 작은 커밋 또는 단계로 나눈 계획
- Goal 0002로 넘어가기 위한 종료 조건
- 사용자에게 필요한 결정 목록

## 이번 Goal 완료 기준

- [ ] 제안서가 코드 변경 없이 작성된다.
- [ ] 추천안과 선택하지 않은 대안의 이유가 명확하다.
- [ ] 예상 파일과 Scene/스크립트 책임이 실제 저장소 기준으로 제시된다.
- [ ] 검증 명령과 수동 확인 순서가 제시된다.
- [ ] 위험과 미확정 사항이 분리된다.
- [ ] 마지막 상태가 `제안서 검토 대기`로 표시된다.
- [ ] 사용자 승인 전 구현하지 않았음을 명시한다.

## 승인 후 예상 구현 범위

아래는 제안서 승인 후 별도 구현 실행에서만 수행한다.

- `project.godot`
- 최소 메인 Scene과 진입 스크립트
- 필요한 최소 `scenes/`, `scripts/`, `data/`, `resources/`, `tests/`, `assets/` 구조
- Godot용 `.gitignore` 최종 확인
- README 실행·headless 검증 방법
- 상태 소유와 데이터 위치의 최소 계약
- 최소 headless 파싱 또는 실행 검증
- Goal 0002의 실제 경로·검증 명령 갱신

## 제안서 제출 상태

```text
현재 상태: 제안서 검토 대기
사용자 승인 전 구현 금지
```
