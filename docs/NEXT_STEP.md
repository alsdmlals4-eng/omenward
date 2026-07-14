# 다음 단계

엔진은 Godot, 기본 언어는 GDScript로 확정됐다.

다음 작업은 구현이 아니라 **Codex Plan Mode 제안서 검토**다.

Codex는 `docs/goals/0001-engine-selection-and-bootstrap.md`, GitHub Issue #1, `docs/PROPOSAL_WORKFLOW.md`를 기준으로 저장소를 읽기 전용으로 검토하고 다음을 제안한다.

- 정확한 Godot stable 버전
- Windows·해상도·2D/2.5D 기준
- 최소 Scene과 파일 구조
- 상태 소유 및 AutoLoad 정책
- 단계별 부트스트랩 구현 계획
- headless·에디터 검증 방법
- 위험과 사용자 결정 요청

사용자가 제안서를 명시적으로 승인하기 전에는 `project.godot`이나 게임 파일을 만들지 않는다.

제안서 승인 후 별도 구현 실행으로 Phase 0 부트스트랩을 진행하고, 실제 실행과 원격 push가 확인된 뒤 `docs/goals/0002-core-vertical-slice.md`를 구체화한다.
