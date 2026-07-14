# Active Context

- Goal: Godot 기반 Phase 0 부트스트랩을 완료하고 3라인 전장·건설·룰렛의 수직 슬라이스 구현을 시작할 수 있게 한다.
- User value: 건설 조합이 룰렛 확률과 전선 운영으로 직접 연결되는 핵심 재미를 빠르게 검증한다.
- Decisions: Godot + GDScript, 3라인, 후방 6노드, 라인별 전방 3노드, 중앙 접전지, 건물 기반 토큰, 적 30초 전조 웨이브.
- Reference repositories: `alsdmlals4-eng/Base`의 spec-first 협업 규칙과 `alsdmlals4-eng/urban-legend`의 Godot 구조·검증 사례를 선별 적용한다.
- Scope: Phase 0 프로젝트 구조, 실행·headless 검증, 맵 단위와 기술 기준 확정.
- Excluded: 멀티플레이, 영구 성장, 완성형 아트, 전설·신화 최종 규칙, 수직 슬라이스 전체 구현.
- Files: `AGENTS.md`, `docs/DOCUMENTATION_MAP.md`, `docs/GODOT_PROJECT_STRUCTURE.md`, `docs/REFERENCE_REPOSITORIES.md`, `docs/goals/0001-engine-selection-and-bootstrap.md`.
- Risks: Godot minor 버전 미확정, 최대 동시 유닛 성능 목표 미확정, 룰렛 경제 기대값, 접전지 스노우볼, 전방 시설 파괴 연쇄 효과.
- Next verification: Goal 0001 기준으로 Godot 최소 프로젝트를 생성하고 에디터 실행 및 headless 검증을 통과한다.