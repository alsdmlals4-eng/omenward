# 다음 단계

엔진은 Godot, 기본 언어는 GDScript로 확정됐다.

현재 다음 작업은 구현이 아니라 두 제안서의 검토다.

## 1. 핵심 게임 벤치마킹 제안서

`docs/benchmarks/0001-core-game-benchmark-proposal.md`를 검토해 다음을 결정한다.

- 수직 슬라이스 필수 UX 6개 채택 여부
- 건물 티어 고정 성장 또는 선택형 분기
- 적 웨이브 수량 정확 공개 또는 범위 공개
- 럭키 찬스 실패 누적 보정 여부
- 전방 생산시설 추가 생산 보너스 여부

사용자 승인 전에는 후보를 `GAME_DESIGN.md`의 확정 규칙으로 옮기지 않는다.

## 2. Godot Phase 0 Plan Mode 제안서

Codex는 `docs/goals/0001-engine-selection-and-bootstrap.md`, GitHub Issue #1, `docs/PROPOSAL_WORKFLOW.md`를 기준으로 저장소를 읽기 전용으로 검토하고 다음을 제안한다.

- 정확한 Godot stable 버전
- Windows·해상도·2D/2.5D 기준
- 최소 Scene과 파일 구조
- 상태 소유 및 AutoLoad 정책
- 단계별 부트스트랩 구현 계획
- headless·에디터 검증 방법
- 위험과 사용자 결정 요청

사용자가 제안서를 명시적으로 승인하기 전에는 `project.godot`이나 게임 파일을 만들지 않는다.

두 제안서에서 승인된 내용만 후속 Goal과 구현 Issue에 반영한다.
