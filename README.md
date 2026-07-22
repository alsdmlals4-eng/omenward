# OMENWARD Prototype

**오멘워드**는 건물로 3×3 룰렛의 토큰과 확률을 설계하고, 베일의 징조로 예고된 공세에 맞서 상·중·하 세 전선을 지휘하는 판타지 전략 오토배틀 게임입니다.

> 현재 상태: **C1 룰렛 REMOTE_PROVEN / C2 전투 목적 루프 REMOTE_PROVEN / 사람 플레이 미완결**
> 프로젝트 코어: **CORE_CONFIRMED / CORE_LOCKED**
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
2. [`docs/PROJECT_CORE.md`](docs/PROJECT_CORE.md) — 제품 정체성, 핵심 선택, 불변 조건과 코어 검증 게이트
3. [`docs/CURRENT_IMPLEMENTATION_STATUS.md`](docs/CURRENT_IMPLEMENTATION_STATUS.md) — 실제 구현·부분 구현·미검증 증거 경계
4. [`docs/HANDOFF_CONTEXT.md`](docs/HANDOFF_CONTEXT.md) — 현재 방향, 불변 조건, 데이터 소유와 다음 작업
5. [`docs/DOCUMENTATION_MAP.md`](docs/DOCUMENTATION_MAP.md) — 작업별 책임 원본 라우터
6. [`docs/OMENWARD_GAME_DESIGN.md`](docs/OMENWARD_GAME_DESIGN.md) — 공식 전체 기획서
7. [`docs/design/APPROVED_PREPRODUCTION_POC_BASELINE_V1.md`](docs/design/APPROVED_PREPRODUCTION_POC_BASELINE_V1.md) — 승인 구조 통합 인덱스
8. [`docs/design/APPROVED_ROULETTE_CORE_RULES.md`](docs/design/APPROVED_ROULETTE_CORE_RULES.md) — 승인 룰렛 판정·등급·보상 계약
9. [`docs/OMENWARD_ROADMAP.md`](docs/OMENWARD_ROADMAP.md) — 현재 복구 순서와 단계별 완료 기준
10. [`docs/DECISIONS_PENDING.md`](docs/DECISIONS_PENDING.md) — 현재 결정 게이트와 PoC 조정 항목
11. [`docs/GODOT_PROJECT_STRUCTURE.md`](docs/GODOT_PROJECT_STRUCTURE.md) — 현재 Godot Scene·상태 소유·데이터 구조
12. [`docs/ACTIVE_CONTEXT.md`](docs/ACTIVE_CONTEXT.md) — 최신 작업 상태 캡슐

## 현재 개선 순서

```text
정본·프로젝트 코어 확정·잠금 완료
→ 승인 룰렛 핵심 계약 원격 검증 완료
→ C2 전투 목적 루프 원격 검증 완료
→ [다음 구현] C3 승인 코어 UX 6종
→ [결정 게이트] C1U 이동권·럭키·100,000시드
→ 10~15분 사람 플레이와 1080p·720p 가독성 검증
→ 밸런스 안정화
→ 콘텐츠·아트 확장
```

현재 저장소에는 원격 검증된 C1 룰렛 핵심 계약과 C2 전투 목적 루프가 존재한다. C2는 접전지·거점·성문·본진·자연 승패·경제를 연결했지만 공통 원격 검증은 완료됐고 사람 플레이는 남아 있다. 현재 판정은 `C1_ROULETTE_CORE_REMOTE_PROVEN`, `C2_BATTLE_OBJECTIVE_REMOTE_PROVEN`, `C2_BATTLE_OBJECTIVE_REMOTE_PROVEN`, `CORE_VERTICAL_SLICE_PARTIAL`, `CORE_LOOP_NOT_PROVEN`, `HUMAN_QA_NOT_RUN`이다.

세부 근거와 다음 게이트는 [`docs/CURRENT_IMPLEMENTATION_STATUS.md`](docs/CURRENT_IMPLEMENTATION_STATUS.md)를 따른다. C1 증거는 [`docs/C1_ROULETTE_RECOVERY_REPORT_2026-07-22.md`](docs/C1_ROULETTE_RECOVERY_REPORT_2026-07-22.md), C2 구현·감사는 [`docs/C2_BATTLE_OBJECTIVE_AUDIT_2026-07-22.md`](docs/C2_BATTLE_OBJECTIVE_AUDIT_2026-07-22.md), 자동·수동 검증은 [`docs/VERTICAL_SLICE_VALIDATION.md`](docs/VERTICAL_SLICE_VALIDATION.md)를 따른다.

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

현재 경로와 파일은 실제 저장소가 권위 원본이며, 구조 변경은 별도 승인·검증 PR에서 수행합니다.
