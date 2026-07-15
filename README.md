# OMENWARD Prototype

**오멘워드**는 건물로 3×3 룰렛의 토큰과 확률을 설계하고, 베일의 징조로 예고된 괴물 공세에 맞서 상·중·하 세 전선을 지휘하는 판타지 전략 오토배틀 게임입니다.

> 현재 상태: **프리프로덕션 디자인 프리즈 / Godot 엔진 확정 / Phase 0 부트스트랩 준비**  
> 기본 구현 언어는 GDScript이며 정확한 Godot stable 버전과 목표 해상도는 Phase 0에서 확정합니다.

## 핵심 문장

> **건물을 지어 룰렛 확률을 바꾸고, 당첨된 병력으로 예고된 위기를 뒤집는다.**

## 세계관

플레이어는 루메른 왕국 트리븐 전선의 **실베른 성채**에 부임한 지휘관입니다. 정체불명의 **베일의 법칙**에 따라 베일런 황야에서 넘어오는 베일종을 세 라인에서 막아냅니다.

작은 감시 정령 **벨루**가 세계관 설명, 적 공세 보고, 튜토리얼과 전술 선택지 안내를 담당합니다.

## 핵심 특징

- 완공된 건물이 3×3 룰렛의 토큰 수와 확률을 결정
- 룰렛 완성 줄로 일반·엘리트·영웅·전설 병력 획득
- 획득한 유닛을 대기칸에 보관한 뒤 원하는 라인에 배치
- 베일의 징조가 적 라인·병종·수량을 약 30초 전에 공개
- 적이 접근해도 계속되는 건설과 간발의 차이로 완공되는 포탑
- 병영 Tier에 따른 병종 분기·패시브 강화와 룰렛 등급별 스킬 성장
- 좌우 대칭 독립 3라인과 라인별 성문 공방
- 중간거점을 점령해 건설권과 기본 자원 생산권 탈취
- 상·중·하 중앙 접전지를 점령해 지속 금화 획득
- 암살자를 안개 속 우회로로 보내 같은 라인의 적 후열 침투
- 전장 전체를 기본 화면에서 조망하며 별도 미니맵은 사용하지 않음
- 시장·병영·포탑·용병 중심의 다양한 빌드
- 바리케이드·화살비·역병·강화지대 전술 명령
- 지상·비행 레이어와 대공 대응
- 일시정지 중 룰렛·건설·배치·전술 명령을 모두 수행하는 계획 모드

## 먼저 읽을 문서

1. [`AGENTS.md`](AGENTS.md) — Codex와 공동 작업자의 작업 규칙
2. [`docs/ACTIVE_CONTEXT.md`](docs/ACTIVE_CONTEXT.md) — 현재 승인 상태와 다음 검증
3. [`docs/OMENWARD_GAME_DESIGN.md`](docs/OMENWARD_GAME_DESIGN.md) — 현재 공식 게임 기획서
4. [`docs/DOCUMENTATION_MAP.md`](docs/DOCUMENTATION_MAP.md) — 작업별 책임 문서 라우터
5. [`docs/DOCUMENT_LIFECYCLE.md`](docs/DOCUMENT_LIFECYCLE.md) — 최신본 유지·중복 제거·아카이브 규칙
6. [`docs/design/APPROVED_BATTLEFIELD_TOPOLOGY_AND_SCALE_V1.md`](docs/design/APPROVED_BATTLEFIELD_TOPOLOGY_AND_SCALE_V1.md) — 전장·성문·중간거점·암살자 우회로 기준
7. [`docs/design/APPROVED_OMENWARD_WORLD_AND_NAMING.md`](docs/design/APPROVED_OMENWARD_WORLD_AND_NAMING.md) — 공식명·세계관·명칭 계약
8. [`docs/design/APPROVED_BELLU_MASCOT_AND_GUIDE_CONTRACT.md`](docs/design/APPROVED_BELLU_MASCOT_AND_GUIDE_CONTRACT.md) — 벨루 캐릭터·UI·오디오 계약
9. [`docs/design/APPROVED_BELLU_SINGLE_GUIDE_AND_FIRST_10_MINUTE_FLOW.md`](docs/design/APPROVED_BELLU_SINGLE_GUIDE_AND_FIRST_10_MINUTE_FLOW.md) — 첫 10분 흐름
10. [`docs/OMENWARD_ROADMAP.md`](docs/OMENWARD_ROADMAP.md) — 단계별 개발 순서
11. [`docs/DECISIONS_PENDING.md`](docs/DECISIONS_PENDING.md) — 구현 전 확정할 항목
12. [`docs/GODOT_PROJECT_STRUCTURE.md`](docs/GODOT_PROJECT_STRUCTURE.md) — Godot 구조와 상태 소유 원칙

## 이름 마이그레이션

```text
Roulettebound → 오멘워드 / OMENWARD
율비 → 벨루
경계의 율 → 베일의 법칙
은종성채·실버벨 배스천 → 실베른 성채
삼문경계·쓰리게이트 프론트 → 트리븐 전선
무명야·베일와일즈 → 베일런 황야
```

저장소명과 내부 코드명 `roulettebound-prototype`은 구현 마이그레이션 계획이 승인될 때까지 유지합니다.

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
│  └─ ui/
├─ scripts/
│  ├─ core/
│  ├─ battle/
│  ├─ buildings/
│  ├─ roulette/
│  ├─ waves/
│  └─ ui/
├─ data/
├─ resources/
└─ tests/
```
