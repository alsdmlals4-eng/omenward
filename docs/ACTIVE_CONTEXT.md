# Active Context

- Goal: 핵심 수직 슬라이스 코딩 전에 게임 규칙, 상태 전이, UI 계약, 데이터 경계, 약 3시간 프로토타입 캠페인, 절차적 생성기, 제약과 룰렛 계약을 최대한 확정한다.
- User value: Codex가 게임 기획을 임의 해석하거나 구현 중 큰 구조를 되돌리는 일을 줄이고, 승인된 계약을 기준으로 집중해서 코딩한다.
- Decisions: Godot + GDScript, Windows PC·마우스/키보드, 싱글플레이 PvE, 코드 작업 전 Plan Mode 제안서 필수, 3라인, 후방 6노드, 라인별 전방 3노드, 중앙 접전지, 건물 기반 토큰, 적 30초 전조 웨이브.
- Match structure: 정규 스테이지 평균 25~35분, 수직 슬라이스 10~15분, 첫 공개 프로토타입 총 약 3시간. 시작 상태·첫 60초·일시정지·2배속·승패·재도전은 `docs/design/APPROVED_MATCH_STRUCTURE.md`에서 관리한다.
- Campaign structure: 10~15분 수동 설계 튜토리얼 1개 뒤 정규 스테이지에서 난이도·맵·특수 적을 확장한다. 튜토리얼은 생성기 대상에서 제외한다.
- Stage generation direction: 정규 스테이지만 결정론적 시드, StageManifest, DifficultyProfile, Threat Budget과 Validator로 생성한다.
- Constraint direction: 튜토리얼 완료 후 정규 스테이지 준비 화면에서 공개형 제약을 선택한다. 기본 난이도와 제약은 별도 축이다.
- Roulette approved core: 기본 판정은 중앙 가로줄이며 아이템으로만 변경한다. 판정 줄 3개가 같은 심벌이어야 보상한다. 완성 줄 1/2/3~7/8개는 각각 1성 병사/엘리트/영웅/전설이다. 전설은 한 판당 1회이며 이후 9칸 동일은 영웅 2명이다.
- Roulette economy: 금화 완성 줄 1/2/3개 이상은 실제 회전 비용의 75%/200%/500%를 지급한다. 시장 특화 시 무한 경제 위험이 있어 구현 전에 별도 회전 제한 안전장치를 확정해야 한다.
- Lucky chance: 12% 시작, 실패당 +8%p, 6회 실패 뒤 다음 회전 확정. 행운 아이템이 초기 확률을 높인다. 자연 럭키 찬스와 여러 이동권을 같은 회전에 사용할 수 있고 이동 횟수 상한은 없다.
- Approved benchmark decisions: 수직 슬라이스 UX 6개, MVP 고정형 3티어, 일반 난이도 정확한 웨이브 수량 공개, 전방 생산시설은 합류 거리만 보상.
- Reference repositories: `alsdmlals4-eng/Base`의 spec-first 협업 규칙과 `alsdmlals4-eng/urban-legend`의 Godot 구조·검증 사례를 선별 적용한다.
- Current state: 룰렛 핵심 규칙은 `docs/design/APPROVED_ROULETTE_CORE_RULES.md`에 승인됐다. Issue #6은 줄 변경 아이템, 행운 아이템 수치, 대기칸, 전설 전투력과 금화 안전장치 검토를 위해 열려 있다.
- Design principle: 규칙·책임·상태·UI·실패 처리는 구현 전에 잠그고, 비용·시간·확률·능력치·거리 같은 수치는 데이터와 플레이테스트로 조정한다.
- Excluded now: `project.godot`, Scene, 코드, Resource, 테스트 생성·수정, 구현 브랜치·PR. 사용자 승인 전 Codex 구현 금지.
- Files: `docs/design/APPROVED_ROULETTE_CORE_RULES.md`, `docs/design/proposals/0004-roulette-resolution-bench-and-lucky-chance.md`, `docs/design/notes/roulette-proposal-review-questions.md`, `docs/DECISIONS_PENDING.md`.
- Risks: 금화 500%와 결정론적 금화 보드의 무한 경제, 이동권 다중 사용으로 보드 조작 가치가 지나치게 커질 가능성, 전설 희소성과 성능, 생성기 비대화, UI 정보 과밀, 다수 유닛 성능.
- Next verification: 금화 안전장치와 룰렛 세부 아이템·대기칸을 결정한 뒤 `건물·경제 → 전투 → 웨이브 → UI·데이터` 순서로 디자인 프리즈를 진행한다.
