# Active Context

- Goal: 핵심 수직 슬라이스를 코딩하기 전에 게임 규칙, 상태 전이, UI 계약, 데이터 경계와 검증 시나리오를 최대한 확정한다.
- User value: Codex가 게임 기획을 임의 해석하거나 구현 중 큰 구조를 되돌리는 일을 줄이고, 승인된 계약을 기준으로 집중해서 코딩한다.
- Decisions: Godot + GDScript, 코드 작업 전 Plan Mode 제안서 필수, 3라인, 후방 6노드, 라인별 전방 3노드, 중앙 접전지, 건물 기반 토큰, 적 30초 전조 웨이브.
- Approved benchmark decisions: 수직 슬라이스 UX 6개, MVP 고정형 3티어, 일반 난이도 정확한 웨이브 수량 공개, 럭키 찬스 실패 누적 보정, 전방 생산시설은 합류 거리만 보상.
- Reference repositories: `alsdmlals4-eng/Base`의 spec-first 협업 규칙과 `alsdmlals4-eng/urban-legend`의 Godot 구조·검증 사례를 선별 적용한다.
- Current state: 벤치마킹 적용안은 승인되어 `docs/design/APPROVED_BENCHMARK_DECISIONS.md`에 확정됐다. 구현 전 `docs/design/DESIGN_FREEZE_CHECKLIST.md`를 영역별로 검토한다.
- Design principle: 규칙·책임·상태·UI·실패 처리는 구현 전에 잠그고, 비용·시간·확률·능력치·거리 같은 수치는 데이터와 플레이테스트로 조정한다.
- Excluded now: `project.godot`, Scene, 코드, Resource, 테스트 생성·수정, 구현 브랜치·PR. 사용자 승인 전 Codex 구현 금지.
- Files: `docs/GAME_DESIGN.md`, `docs/design/APPROVED_BENCHMARK_DECISIONS.md`, `docs/design/DESIGN_FREEZE_CHECKLIST.md`, `docs/DECISIONS_PENDING.md`, `docs/benchmarks/`.
- Risks: 과도한 사전 기획으로 실제 손맛 검증이 늦어질 수 있음, 룰렛 경제 기대값, 접전지 스노우볼, UI 정보 과밀, 전방 시설 파괴 연쇄 효과, 다수 유닛 성능.
- Next verification: 디자인 프리즈 체크리스트를 한 번에 모두 결정하지 않고 `한 판 구조 → 룰렛 → 건물·경제 → 전투 → 웨이브 → UI·데이터` 순서로 제안서화하고 사용자 승인을 받는다.
