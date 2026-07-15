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

Codex가 임의의 엔진 버전이나 폴더 구조를 먼저 고정하지 않고, 오멘워드의 실제 전장·룰렛·건설·데이터·성능 요구와 참고 저장소를 검토한 뒤 안전한 기술 기반을 합의한다.

## 먼저 읽을 문서

- `AGENTS.md`
- `docs/BASE_RULES_VERSION.md`
- `docs/DOCUMENTATION_MAP.md`
- `docs/DOCUMENT_LIFECYCLE.md`
- `docs/PROPOSAL_WORKFLOW.md`
- `docs/OMENWARD_GAME_DESIGN.md`
- `docs/design/APPROVED_PREPRODUCTION_POC_BASELINE_V1.md`
- `docs/design/APPROVED_BATTLEFIELD_TOPOLOGY_AND_SCALE_V1.md`
- `docs/design/APPROVED_PERFORMANCE_DATA_TEST_READINESS_POC_V1.md`
- `docs/GODOT_PROJECT_STRUCTURE.md`
- `docs/REFERENCE_REPOSITORIES.md`
- `docs/DECISIONS_PENDING.md`
- `docs/OMENWARD_ROADMAP.md`
- `docs/ACTIVE_CONTEXT.md`
- GitHub Issue #1

참고 저장소는 필요한 파일만 읽는다.

- `alsdmlals4-eng/Base`: `AGENTS.md`, 작업 흐름·검증 관련 문서
- `alsdmlals4-eng/urban-legend`: `AGENTS.md`, `project.godot`, README의 폴더 구조, Godot UI·검증 관련 문서

## 승인된 결정

- 프로젝트명: 오멘워드 / OMENWARD
- 엔진: Godot
- 기본 언어: GDScript
- 플랫폼: Windows PC / 마우스·키보드 / 싱글플레이 PvE
- 공용 상태는 필요한 경우에만 AutoLoad 사용
- Godot 네이티브 Scene, Node, Resource, Signal, Control/Container/Theme 우선
- `.godot/` 및 로컬 생성물은 Git에서 제외
- 코드 작업 전 Codex Plan Mode 제안서와 사용자 승인 필수
- 전장은 좌우 대칭 독립 3라인이며 라인별 성문·중간거점·중앙 접전지를 가진다.
- 중간거점은 전방 2·후방 1 건설 노드를 가지며 점령 시 건설권과 기본 생산권이 이전된다.
- 암살자는 같은 라인의 안개 우회로를 사용하며 적 후방에 직접 생성하지 않는다.
- 기본 전략 화면에서 전장 전체를 표시하며 별도 미니맵은 사용하지 않는다.

## 제안서에서 검토할 결정

각 항목에 대해 **추천안, 이유, 대안의 장단점**을 제시한다.

- 정확한 Godot stable 버전
- 기준 출력 1920×1080과 내부 논리 해상도·stretch 정책
- 2D 픽셀 Camera2D와 확대·이동·픽셀 스냅 정책
- 첫 프로토타입 최대 동시 유닛·투사체·VFX 목표와 성능 검증 방식
- 루트 폴더와 최소 Scene·Script·Resource·Data·Test 구조
- 전장 라인·성문·중간거점·접전지·우회로 데이터 소유 구조
- AutoLoad를 처음부터 둘지 첫 공유 상태가 생길 때 추가할지
- 결정론적 난수·전투 시간·계획 모드 시간 소유 구조
- headless 검증 명령과 Windows 실행 파일 경로 처리
- 최소 메인 Scene이 보여줄 내용

## Plan Mode 포함 범위

- 현재 저장소 구조와 문서 간 불일치 확인
- Base와 urban-legend에서 적용 가능한 작업·Godot 구조 분석
- 정확한 예상 파일 목록과 각 파일의 책임 제안
- Godot Scene 트리, 상태 소유, Signal 연결의 최소 구조 제안
- 데이터·Resource 경계와 검증 가능한 seam 제안
- 단계별 구현 순서 제안
- 검증 명령과 수동 확인 순서 제안
- 위험, 미확정 사항, 사용자 결정 요청 정리

## Plan Mode 제외 범위

- `project.godot` 생성·수정
- Scene, GDScript, Resource, 테스트 코드 생성·수정
- 외부 애드온·에셋·의존성 설치
- 구현 브랜치, 커밋, PR 생성
- 전투, 룰렛, 건설, 거점, 성문, 우회로, 웨이브 구현
- 승인되지 않은 기술 선택 확정

## 제안서 필수 내용

`docs/PROPOSAL_WORKFLOW.md` 형식을 사용하고 다음 내용을 구체적으로 포함한다.

- 확인한 실제 파일과 근거
- 추천 Godot 버전 및 대안
- 예상 Scene 트리
- 예상 파일 경로와 책임
- 상태 소유 및 AutoLoad 사용 여부
- 데이터/Resource 경계
- 전장 구조 데이터 표현 방식
- headless 및 에디터 검증 명령
- Phase 0 구현을 작은 커밋 또는 단계로 나눈 계획
- Goal 0002로 넘어가기 위한 종료 조건
- 사용자에게 필요한 결정 목록

## 이번 Goal 완료 기준

- [ ] 제안서가 코드 변경 없이 작성된다.
- [ ] 추천안과 선택하지 않은 대안의 이유가 명확하다.
- [ ] 예상 파일과 Scene·Script·Resource 책임이 실제 저장소 기준으로 제시된다.
- [ ] 최신 오멘워드 전장·UI·성능 계약을 반영한다.
- [ ] 검증 명령과 수동 확인 순서가 제시된다.
- [ ] 위험과 미확정 사항이 분리된다.
- [ ] 마지막 상태가 `제안서 검토 대기`로 표시된다.
- [ ] 사용자 승인 전 구현하지 않았음을 명시한다.

## 승인 후 예상 구현 범위

아래는 제안서 승인 후 별도 구현 실행에서만 수행한다.

- `project.godot`
- 최소 메인 Scene과 진입 Script
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
