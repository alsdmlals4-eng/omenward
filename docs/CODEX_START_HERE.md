# Codex 시작 안내

Codex는 구현 전에 다음 순서로 문서를 읽는다.

1. `AGENTS.md`
2. `docs/BASE_RULES_VERSION.md`
3. `docs/DOCUMENTATION_MAP.md`
4. `docs/GAME_DESIGN.md`
5. 현재 GitHub Issue 또는 `docs/goals/` Goal
6. `docs/GODOT_PROJECT_STRUCTURE.md`
7. `docs/REFERENCE_REPOSITORIES.md`
8. `docs/DECISIONS_PENDING.md`
9. 관련 실제 파일과 테스트
10. `docs/ACTIVE_CONTEXT.md`

엔진은 Godot, 기본 언어는 GDScript로 확정됐다.

첫 구현 작업은 `docs/goals/0001-engine-selection-and-bootstrap.md`다. 이 Goal은 엔진 비교가 아니라 Godot 최소 프로젝트, 폴더 구조, 실행 명령과 headless 검증을 만드는 작업이다.

`Base`와 `urban-legend`는 구조와 작업 방식의 참고 자료다. 코드를 바로 복사하지 말고 `docs/REFERENCE_REPOSITORIES.md`의 채택·제외 기준을 따른다.

구현 작업은 별도 `codex/issue-<번호>-<설명>` 브랜치와 Pull Request로 제출한다. 완료 보고 전에 실제 검증 결과와 원격 push 여부를 확인한다.