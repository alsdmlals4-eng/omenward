# Active Context

- Goal: Godot Phase 0 부트스트랩과 핵심 게임 벤치마킹을 각각 제안서로 검토하고, 사용자 승인 후에만 기획 확정 또는 구현을 시작한다.
- User value: 엔진 구조와 게임 UX를 코드로 먼저 고정하지 않고, 실제 참고작의 반응·장단점과 검증 가능한 계획을 바탕으로 합의한다.
- Decisions: Godot + GDScript, 코드 작업 전 Plan Mode 제안서 필수, 3라인, 후방 6노드, 라인별 전방 3노드, 중앙 접전지, 건물 기반 토큰, 적 30초 전조 웨이브.
- Reference repositories: `alsdmlals4-eng/Base`의 spec-first 협업 규칙과 `alsdmlals4-eng/urban-legend`의 Godot 구조·검증 사례를 선별 적용한다.
- Current state: Issue #1과 Goal 0001은 Godot 부트스트랩 제안서 검토 대기다. `docs/benchmarks/0001-core-game-benchmark-proposal.md`는 게임성 적용 후보 검토 대기다.
- Benchmark findings: 단순한 표면과 깊은 인과, 확률 설계 가시화, 적 의도 전조, 패배 원인 설명, 제한된 건설 공간이 반복적으로 좋은 반응을 얻었다. 장르 혼합 과부하, 통제 불가능한 RNG, 불명확한 전투 결과는 주요 위험이다.
- Proposal scope: Godot 버전·구조·검증 제안과, 수직 슬라이스 UX 6개 및 이후 실험 후보의 승인 여부.
- Excluded now: `project.godot`, Scene, 코드, Resource, 테스트 생성·수정, 벤치마킹 후보의 `GAME_DESIGN.md` 자동 확정, 구현 브랜치·PR.
- Files: `AGENTS.md`, `docs/PROPOSAL_WORKFLOW.md`, `docs/DOCUMENTATION_MAP.md`, `docs/benchmarks/`, `docs/GODOT_PROJECT_STRUCTURE.md`, `docs/REFERENCE_REPOSITORIES.md`, `docs/goals/0001-engine-selection-and-bootstrap.md`.
- Risks: Godot minor 버전 미확정, 최대 동시 유닛 성능 목표 미확정, 룰렛 경제 기대값, 접전지 스노우볼, UI 정보 과밀, 전방 시설 파괴 연쇄 효과.
- Next verification: 사용자가 벤치마킹 제안서의 A/B/C 후보를 검토하고, 승인된 항목만 게임 기획서와 후속 Codex Plan Mode 제안서에 반영한다. 승인 전 구현 검증을 시작하지 않는다.
