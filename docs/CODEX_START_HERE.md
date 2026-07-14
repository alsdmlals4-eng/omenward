# Codex 시작 안내

Codex는 다음 순서로 문서를 읽는다.

1. `AGENTS.md`
2. `docs/BASE_RULES_VERSION.md`
3. `docs/DOCUMENTATION_MAP.md`
4. `docs/PROPOSAL_WORKFLOW.md`
5. `docs/GAME_DESIGN.md`
6. 현재 GitHub Issue 또는 `docs/goals/` Goal
7. `docs/GODOT_PROJECT_STRUCTURE.md`
8. `docs/REFERENCE_REPOSITORIES.md`
9. `docs/DECISIONS_PENDING.md`
10. 관련 실제 파일과 테스트
11. `docs/ACTIVE_CONTEXT.md`

엔진은 Godot, 기본 언어는 GDScript로 확정됐다.

## 첫 실행: Plan Mode 제안서

첫 Codex 실행은 `docs/goals/0001-engine-selection-and-bootstrap.md`와 Issue #1을 기준으로 **Plan Mode에서만** 진행한다.

- 저장소와 참고 문서를 읽는다.
- `docs/PROPOSAL_WORKFLOW.md` 형식으로 Godot 부트스트랩 제안서를 작성한다.
- 정확한 버전, Scene 구조, 예상 파일, 상태 소유, 단계별 구현, 검증과 위험을 제안한다.
- 사용자 승인 전에는 `project.godot`, Scene, 스크립트, Resource, 데이터 또는 테스트를 만들거나 수정하지 않는다.
- 구현 브랜치, 커밋, Pull Request도 만들지 않는다.

`Base`와 `urban-legend`는 구조와 작업 방식의 참고 자료다. 코드를 바로 복사하지 말고 `docs/REFERENCE_REPOSITORIES.md`의 채택·제외 기준을 따른다.

## 승인 후 구현

사용자가 제안서를 명시적으로 승인한 뒤에만 별도 구현 실행을 시작한다.

- 승인된 제안서와 Issue/Goal의 범위를 다시 확인한다.
- `codex/issue-<번호>-<설명>` 브랜치를 사용한다.
- 구현, 검증, 커밋과 Pull Request를 진행한다.
- 완료 보고 전에 실제 검증 결과와 원격 push 여부를 확인한다.
- 승인 범위를 바꿔야 하면 구현을 멈추고 제안서 수정안으로 돌아간다.
