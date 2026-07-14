# Active Context

- Goal: 핵심 수직 슬라이스를 코딩하기 전에 게임 규칙, 상태 전이, UI 계약, 데이터 경계, 약 3시간 프로토타입 캠페인과 절차적 스테이지 생성기 계약을 최대한 확정한다.
- User value: Codex가 게임 기획을 임의 해석하거나 구현 중 큰 구조를 되돌리는 일을 줄이고, 승인된 계약을 기준으로 집중해서 코딩한다.
- Decisions: Godot + GDScript, Windows PC·마우스/키보드, 싱글플레이 PvE, 코드 작업 전 Plan Mode 제안서 필수, 3라인, 후방 6노드, 라인별 전방 3노드, 중앙 접전지, 건물 기반 토큰, 적 30초 전조 웨이브.
- Match structure: 정규 스테이지 평균 25~35분, 수직 슬라이스 10~15분, 첫 공개 프로토타입 총 플레이 분량 약 3시간. 시작 상태·첫 60초·일시정지·2배속·승패·재도전은 `docs/design/APPROVED_MATCH_STRUCTURE.md`에 승인됐다.
- Stage generation direction: 첫 프로토타입에 절차적 스테이지 생성기를 포함한다. 현재 `docs/design/proposals/0002-prototype-campaign-and-stage-generator.md`에서 6개 안팎의 선형 캠페인, 결정론적 시드, StageManifest, DifficultyProfile, Threat Budget과 Validator를 검토 중이다.
- Approved benchmark decisions: 수직 슬라이스 UX 6개, MVP 고정형 3티어, 일반 난이도 정확한 웨이브 수량 공개, 럭키 찬스 실패 누적 보정, 전방 생산시설은 합류 거리만 보상.
- Reference repositories: `alsdmlals4-eng/Base`의 spec-first 협업 규칙과 `alsdmlals4-eng/urban-legend`의 Godot 구조·검증 사례를 선별 적용한다.
- Current state: 한 판 구조는 승인됐다. Issue #4에서 3시간 캠페인과 절차적 생성기 세부안을 조정한 뒤 룰렛·대기칸 영역으로 진행한다.
- Design principle: 규칙·책임·상태·UI·실패 처리는 구현 전에 잠그고, 비용·시간·확률·능력치·거리 같은 수치는 데이터와 플레이테스트로 조정한다.
- Excluded now: `project.godot`, Scene, 코드, Resource, 테스트 생성·수정, 구현 브랜치·PR. 사용자 승인 전 Codex 구현 금지.
- Files: `docs/design/APPROVED_MATCH_STRUCTURE.md`, `docs/design/proposals/0002-prototype-campaign-and-stage-generator.md`, `docs/design/DESIGN_FREEZE_CHECKLIST.md`, `docs/DECISIONS_PENDING.md`, `docs/ROADMAP.md`.
- Risks: 생성 규칙이 너무 자유로워 불공정 스테이지가 나올 가능성, 생성기 자체 개발이 핵심 전투보다 앞서 비대해질 가능성, 룰렛 경제 기대값, 접전지 스노우볼, UI 정보 과밀, 다수 유닛 성능.
- Next verification: 절차적 생성기의 7개 핵심 결정을 사용자 조정안으로 확정하고, 이후 `룰렛 → 건물·경제 → 전투 → 웨이브 → UI·데이터` 순서로 디자인 프리즈를 진행한다.
