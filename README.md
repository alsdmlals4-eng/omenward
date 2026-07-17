# OMENWARD Prototype

**오멘워드**는 건물로 3×3 룰렛의 토큰과 확률을 설계하고, 베일의 징조로 예고된 공세에 맞서 상·중·하 세 전선을 지휘하는 판타지 전략 오토배틀 게임입니다.

> 현재 상태: **플레이 가능한 수직 슬라이스 구현 완료 / PR 검토·수동 QA 대기**
> 기본 언어는 GDScript이며 Godot 4.7.1 Standard, Compatibility renderer, 1920×1080 출력과 960×540 논리 해상도를 사용합니다.

## 핵심 문장

> **건물을 지어 룰렛 확률을 바꾸고, 당첨된 병력으로 예고된 위기를 뒤집는다.**

## 핵심 구조

- 좌우 대칭의 독립된 상·중·하 3라인과 라인별 성문.
- 중간거점 전방 2·후방 1 건설 노드와 점령에 따른 건설권·생산권 이전.
- 중앙 접전지 점령 수입과 성문 공성.
- 암살자를 안개 속 같은 라인 우회로로 보내 적 후열에 침투.
- 전장 전체를 기본 전략 화면에서 조망하며 미니맵은 사용하지 않음.
- 건물 개수가 룰렛 토큰과 확률을 바꾸고, Tier와 등급이 병종의 성장 방향을 결정.
- 활성 전투 시간 기준 60초 공세와 W5·W10·W15·W20 이정표.
- 벨루가 세계관, 튜토리얼, 공세 보고와 감정 반응을 담당.

## 공용 10병종 데이터

전투 규칙 기준 병종 데이터는 **공용 아키타입 10개만** 사용합니다.

```text
공용 UnitArchetypeProfile
+ TierProfile
+ RankProfile
+ owner_team_id
+ FactionVisualProfile
```

아군과 적군은 HP·공격·스킬·타기팅·애니메이션 상태와 판정 타이밍을 공유합니다. 차이는 소유 팀, 출격 방식, 스프라이트·초상화·아이콘·팔레트·표시명입니다.

- 별도 `EnemyUnitProfile`을 만들지 않습니다.
- 적 웨이브는 같은 `archetype_id`를 enemy 팀과 베일종 이미지로 출격시킵니다.
- 적군 전용 스탯·스킬·모션 상태 머신을 복제하지 않습니다.
- W15·W20 보스만 공용 아키타입 위에 보스 행동·페이즈 패키지를 추가합니다.

## 먼저 읽을 문서

작업 규칙은 [`AGENTS.md`](AGENTS.md), 세부 라우팅은 [`docs/DOCUMENTATION_MAP.md`](docs/DOCUMENTATION_MAP.md)에서 확인한다. 제품 방향과 현재 상태는 다음 다섯 활성 본책이 책임진다.

1. [게임 기획 본책](docs/planning/01_GAME_DESIGN.md)
2. [프로그래밍 기획·MVP 로드맵](docs/planning/02_PROGRAMMING_MVP_ROADMAP.md)
3. [아트 기획 본책](docs/planning/03_ART_DIRECTION.md)
4. [사운드 기획 본책](docs/planning/04_SOUND_DIRECTION.md)
5. [QA·PM 기획 본책](docs/planning/05_QA_PM_PLAN.md)

`docs/design/APPROVED_*.md`는 본책의 구체 수치·데이터 계약을 보존하는 상세 부록이다. 최신 공식 이미지는 [시각자료 인덱스](docs/images/VISUAL_REFERENCE_INDEX.md)와 `docs/images/current/`에서 확인한다.

## 현재 실행 순서

```text
Phase 0·3라인 핵심 수직 슬라이스 구현
→ headless 6종·editor import·runtime smoke 기준선 통과
→ [현재] 1920×1080·1280×720 수동 QA와 시각 프로브
→ 시뮬레이션·플레이테스트
→ 콘텐츠·아트·사운드 확장
```

수직 슬라이스는 튜토리얼 4웨이브, 일반 스테이지 W1~W20, 공용 병종 전투·점령·성문·건설·룰렛·배치·암살자 우회와 회색상자 UI를 구현합니다. 자동 검증은 [`docs/VERTICAL_SLICE_VALIDATION.md`](docs/VERTICAL_SLICE_VALIDATION.md)를 따릅니다.

검증 명령과 수동 QA는 [`docs/PHASE_0_VALIDATION.md`](docs/PHASE_0_VALIDATION.md)를 따른다.

## 현재 저장소 구조

```text
.
├─ project.godot
├─ AGENTS.md
├─ README.md
├─ scenes/
│  ├─ main/
│  ├─ battle/
│  ├─ buildings/
│  ├─ units/
│  ├─ roulette/
│  ├─ waves/
│  └─ ui/
├─ scripts/
│  ├─ core/
│  ├─ battle/
│  ├─ buildings/
│  ├─ units/
│  ├─ roulette/
│  ├─ waves/
│  └─ ui/
├─ data/
├─ resources/
├─ assets/
└─ tests/
```

실제 구조와 다음 기술 게이트는 [프로그래밍 본책](docs/planning/02_PROGRAMMING_MVP_ROADMAP.md)을 기준으로 갱신합니다.
