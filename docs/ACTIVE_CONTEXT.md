# Active Context

- Goal: 핵심 수직 슬라이스를 코딩하기 전에 게임 규칙, 상태 전이, UI 계약, 데이터 경계, 약 3시간 프로토타입 캠페인, 절차적 스테이지 생성기와 플레이어 선택형 제약 계약을 최대한 확정한다.
- User value: Codex가 게임 기획을 임의 해석하거나 구현 중 큰 구조를 되돌리는 일을 줄이고, 승인된 계약을 기준으로 집중해서 코딩한다.
- Decisions: Godot + GDScript, Windows PC·마우스/키보드, 싱글플레이 PvE, 코드 작업 전 Plan Mode 제안서 필수, 3라인, 후방 6노드, 라인별 전방 3노드, 중앙 접전지, 건물 기반 토큰, 적 30초 전조 웨이브.
- Match structure: 정규 스테이지 평균 25~35분, 수직 슬라이스 10~15분, 첫 공개 프로토타입 총 플레이 분량 약 3시간. 시작 상태·첫 60초·일시정지·2배속·승패·재도전은 `docs/design/APPROVED_MATCH_STRUCTURE.md`에 승인됐다.
- Campaign structure: 수동 설계 튜토리얼 1개에서 모든 핵심 학습 전략을 진행한다. 이후 정규 스테이지는 난이도 증가, 맵 변형과 특수 적 순차 등장으로 구성하며 `docs/design/APPROVED_PROTOTYPE_CAMPAIGN_STRUCTURE.md`에서 관리한다.
- Stage generation direction: 튜토리얼은 생성기 대상에서 제외한다. 정규 스테이지만 결정론적 시드, StageManifest, DifficultyProfile, Threat Budget과 Validator로 생성한다.
- Constraint direction: 튜토리얼 완료 후 정규 스테이지 준비 화면에서 공개형 제약을 선택해 난이도를 추가한다. 기본 난이도와 제약은 별도 축이며 세부안은 `docs/design/proposals/0003-constraint-system.md`에서 검토 중이다.
- Approved benchmark decisions: 수직 슬라이스 UX 6개, MVP 고정형 3티어, 일반 난이도 정확한 웨이브 수량 공개, 럭키 찬스 실패 누적 보정, 전방 생산시설은 합류 거리만 보상.
- Reference repositories: `alsdmlals4-eng/Base`의 spec-first 협업 규칙과 `alsdmlals4-eng/urban-legend`의 Godot 구조·검증 사례를 선별 적용한다.
- Current state: 한 판 구조와 튜토리얼 우선 캠페인 구조는 승인됐다. Issue #4에서 생성기 세부 계약을, 별도 제약 제안서에서 점수·보상·조합 규칙을 검토한다.
- Design principle: 규칙·책임·상태·UI·실패 처리는 구현 전에 잠그고, 비용·시간·확률·능력치·거리 같은 수치는 데이터와 플레이테스트로 조정한다.
- Excluded now: `project.godot`, Scene, 코드, Resource, 테스트 생성·수정, 구현 브랜치·PR. 사용자 승인 전 Codex 구현 금지.
- Files: `docs/design/APPROVED_MATCH_STRUCTURE.md`, `docs/design/APPROVED_PROTOTYPE_CAMPAIGN_STRUCTURE.md`, `docs/design/proposals/0002-prototype-campaign-and-stage-generator.md`, `docs/design/proposals/0003-constraint-system.md`, `docs/DECISIONS_PENDING.md`, `docs/ROADMAP.md`.
- Risks: 튜토리얼에 모든 학습을 넣어 과밀해질 가능성, 생성기 자체 개발이 핵심 전투보다 앞서 비대해질 가능성, 제약 조합이 소프트락을 만들 가능성, 룰렛 경제 기대값, 접전지 스노우볼, UI 정보 과밀, 다수 유닛 성능.
- Next verification: 제약 시스템의 7개 핵심 결정을 사용자 조정안으로 확정하고, 생성기 세부안과 함께 디자인 프리즈에 반영한 뒤 `룰렛 → 건물·경제 → 전투 → 웨이브 → UI·데이터` 순서로 진행한다.
