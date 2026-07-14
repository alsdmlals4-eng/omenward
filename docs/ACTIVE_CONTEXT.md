# Active Context

- Goal: Codex Plan Mode에서 Godot Phase 0 부트스트랩 제안서를 검토하고, 사용자 승인 후에만 구현을 시작한다.
- User value: 엔진 버전·폴더·상태·검증 구조를 코드로 먼저 고정하지 않고 검토 가능한 계획으로 합의한다.
- Decisions: Godot + GDScript, 코드 작업 전 Plan Mode 제안서 필수, 3라인, 후방 6노드, 라인별 전방 3노드, 중앙 접전지, 건물 기반 토큰, 적 30초 전조 웨이브.
- Reference repositories: `alsdmlals4-eng/Base`의 spec-first 협업 규칙과 `alsdmlals4-eng/urban-legend`의 Godot 구조·검증 사례를 선별 적용한다.
- Current state: Issue #1과 Goal 0001은 `제안서 검토 대기` 상태이며 사용자 승인 전 구현이 금지된다.
- Proposal scope: Godot 버전, 플랫폼·해상도, 2D/2.5D, Scene/파일 구조, 상태 소유, 단계별 구현, headless 검증과 위험 제안.
- Excluded now: `project.godot`, Scene, 코드, Resource, 테스트 생성·수정, 구현 브랜치·커밋·PR.
- Files: `AGENTS.md`, `docs/PROPOSAL_WORKFLOW.md`, `docs/DOCUMENTATION_MAP.md`, `docs/GODOT_PROJECT_STRUCTURE.md`, `docs/REFERENCE_REPOSITORIES.md`, `docs/goals/0001-engine-selection-and-bootstrap.md`.
- Risks: Godot minor 버전 미확정, 최대 동시 유닛 성능 목표 미확정, 룰렛 경제 기대값, 접전지 스노우볼, 전방 시설 파괴 연쇄 효과.
- Next verification: Codex가 Plan Mode 제안서를 제출하고, 사용자가 수정 또는 승인한다. 승인 전에는 구현 검증을 시작하지 않는다.
