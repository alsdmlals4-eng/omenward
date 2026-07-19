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

1. [`AGENTS.md`](AGENTS.md) — 작업 규칙과 승인 게이트
2. [`docs/HANDOFF_CONTEXT.md`](docs/HANDOFF_CONTEXT.md) — 현재 방향, 불변 조건, 데이터 소유와 다음 작업
3. [`docs/DOCUMENTATION_MAP.md`](docs/DOCUMENTATION_MAP.md) — 작업별 책임 원본 라우터
4. [`docs/OMENWARD_GAME_DESIGN.md`](docs/OMENWARD_GAME_DESIGN.md) — 공식 전체 기획서 v0.19
5. [`docs/design/APPROVED_PREPRODUCTION_POC_BASELINE_V1.md`](docs/design/APPROVED_PREPRODUCTION_POC_BASELINE_V1.md) — 승인 구조 통합 인덱스
6. [`docs/design/APPROVED_SHARED_UNIT_ARCHETYPE_AND_FACTION_VISUAL_DATA_V1.md`](docs/design/APPROVED_SHARED_UNIT_ARCHETYPE_AND_FACTION_VISUAL_DATA_V1.md) — 공용 병종·진영 이미지 데이터 계약
7. [`docs/design/APPROVED_BATTLEFIELD_TOPOLOGY_AND_SCALE_V1.md`](docs/design/APPROVED_BATTLEFIELD_TOPOLOGY_AND_SCALE_V1.md) — 전장·성문·거점·우회로
8. [`docs/design/APPROVED_UNIT_ANIMATION_AND_BATTLE_PRESENTATION_GUIDE_V1.md`](docs/design/APPROVED_UNIT_ANIMATION_AND_BATTLE_PRESENTATION_GUIDE_V1.md) — 이동·공격·피격·승리 연출
9. [`docs/OMENWARD_ROADMAP.md`](docs/OMENWARD_ROADMAP.md) — 승인 게이트와 단계별 완료 기준
10. [`docs/DECISIONS_PENDING.md`](docs/DECISIONS_PENDING.md) — 구현 전·PoC 후 결정 항목
11. [`docs/GODOT_PROJECT_STRUCTURE.md`](docs/GODOT_PROJECT_STRUCTURE.md) — 예정 기술 구조와 상태 소유
12. [`docs/ACTIVE_CONTEXT.md`](docs/ACTIVE_CONTEXT.md) — 최신 작업 상태 캡슐

## 현재 실행 순서

```text
Issue #1 Phase 0 Plan Mode
→ 사용자 승인
→ Godot 기술 기반 구현
→ Issue #32 수직 슬라이스 Plan Mode
→ 사용자 승인
→ 3라인 핵심 수직 슬라이스
→ 시뮬레이션·플레이테스트
```

수직 슬라이스는 튜토리얼 4웨이브, 일반 스테이지 W1~W20, 공용 병종 전투·점령·성문·건설·룰렛·배치·암살자 우회와 회색상자 UI를 구현합니다. 자동 검증은 [`docs/VERTICAL_SLICE_VALIDATION.md`](docs/VERTICAL_SLICE_VALIDATION.md)를 따릅니다.

검증 명령과 수동 QA는 [`docs/PHASE_0_VALIDATION.md`](docs/PHASE_0_VALIDATION.md)를 따른다.

## 예정 저장소 구조

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

정확한 경로와 파일은 Phase 0 Plan Mode 승인 후 확정합니다.
