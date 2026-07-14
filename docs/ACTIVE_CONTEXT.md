# Active Context

- Goal: 핵심 수직 슬라이스를 코딩하기 전에 게임 규칙, 상태 전이, UI 계약, 데이터 경계, 약 3시간 프로토타입 캠페인, 절차적 스테이지 생성기와 플레이어 선택형 제약 계약을 최대한 확정한다.
- User value: Codex가 게임 기획을 임의 해석하거나 구현 중 큰 구조를 되돌리는 일을 줄이고, 승인된 계약을 기준으로 집중해서 코딩한다.
- Decisions: Godot + GDScript, Windows PC·마우스/키보드, 싱글플레이 PvE, 코드 작업 전 Plan Mode 제안서 필수, 3라인, 후방 6노드, 라인별 전방 3노드, 중앙 접전지, 건물 기반 토큰, 적 30초 전조 웨이브.
- Match structure: 정규 스테이지 평균 25~35분, 수직 슬라이스 10~15분, 첫 공개 프로토타입 총 플레이 분량 약 3시간. 시작 상태·첫 60초·일시정지·2배속·승패·재도전은 `docs/design/APPROVED_MATCH_STRUCTURE.md`에 승인됐다.
- Campaign structure: 10~15분의 수동 설계 튜토리얼 1개에서 핵심 기능을 짧게 소개한다. 이후 정규 스테이지는 난이도 증가, 맵 변형과 특수 적 순차 등장으로 구성하며 `docs/design/APPROVED_PROTOTYPE_CAMPAIGN_STRUCTURE.md`에서 관리한다.
- Stage generation direction: 튜토리얼은 생성기 대상에서 제외한다. 정규 스테이지만 결정론적 시드, StageManifest, DifficultyProfile, Threat Budget과 Validator로 생성한다.
- Constraint direction: 튜토리얼 완료 후 정규 스테이지 준비 화면에서 공개형 제약을 선택해 난이도를 추가한다. 기본 난이도와 제약은 별도 축이며 세부안은 `docs/design/proposals/0003-constraint-system.md`에서 검토 중이다.
- Roulette proposal: `docs/design/proposals/0004-roulette-resolution-bench-and-lucky-chance.md`에서 회전 전 기준 줄 선택, 혼합 보상, 별·품질 분리, 결과 보관함, 금화 환급, 럭키 찬스 실패 누적과 이동권 계약을 검토 중이다.
- Approved benchmark decisions: 수직 슬라이스 UX 6개, MVP 고정형 3티어, 일반 난이도 정확한 웨이브 수량 공개, 럭키 찬스 실패 누적 보정, 전방 생산시설은 합류 거리만 보상.
- Reference repositories: `alsdmlals4-eng/Base`의 spec-first 협업 규칙과 `alsdmlals4-eng/urban-legend`의 Godot 구조·검증 사례를 선별 적용한다.
- Current state: 한 판 구조와 튜토리얼 우선 캠페인 구조는 승인됐다. 생성기·제약 세부안과 함께 룰렛 결과 및 예외 처리 제안서를 사용자와 조정한다.
- Design principle: 규칙·책임·상태·UI·실패 처리는 구현 전에 잠그고, 비용·시간·확률·능력치·거리 같은 수치는 데이터와 플레이테스트로 조정한다.
- Excluded now: `project.godot`, Scene, 코드, Resource, 테스트 생성·수정, 구현 브랜치·PR. 사용자 승인 전 Codex 구현 금지.
- Files: `docs/design/APPROVED_MATCH_STRUCTURE.md`, `docs/design/APPROVED_PROTOTYPE_CAMPAIGN_STRUCTURE.md`, `docs/design/proposals/0002-prototype-campaign-and-stage-generator.md`, `docs/design/proposals/0003-constraint-system.md`, `docs/design/proposals/0004-roulette-resolution-bench-and-lucky-chance.md`, `docs/DECISIONS_PENDING.md`, `docs/ROADMAP.md`.
- Risks: 생성기 자체 개발 비대화, 제약 조합 소프트락, 룰렛 금화 기대값, 결과 보관함과 대기칸 UI 과밀, 럭키 찬스 빈도, 접전지 스노우볼, 다수 유닛 성능.
- Next verification: 룰렛 제안서의 기준 줄, 혼합 보상, 별·품질, 결과 보관함, 금화 환급과 럭키 찬스 수치를 사용자 조정안으로 확정한 뒤 `건물·경제 → 전투 → 웨이브 → UI·데이터` 순서로 진행한다.