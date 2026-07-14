# Roulettebound Prototype

건물로 룰렛의 토큰 풀을 설계하고, 상·중·하 3개 전선을 실시간으로 운영하는 판타지 전략 오토배틀 프로토타입입니다.

> 현재 상태: **Godot 엔진 확정 / Phase 0 부트스트랩 준비**  
> 기본 구현 언어는 GDScript이며, 정확한 Godot minor 버전과 목표 플랫폼·해상도는 Phase 0에서 확정합니다.

## 핵심 특징

- 완공된 건물이 3×3 룰렛의 토큰 수와 확률을 결정
- 룰렛으로 획득한 유닛을 대기칸에 보관한 뒤 원하는 라인에 배치
- 상·중·하 중앙 접전지를 점령하면 지속 금화 획득
- 안전하지만 제한된 후방 노드와 위험한 전방 거점 노드의 경쟁
- 농장, 시장, 병종별 훈련시설, 포탑의 실시간 건설·업그레이드
- 적은 룰렛 대신 건물 기반 정기 웨이브를 사용하며 출격 30초 전에 구성과 공격 라인을 예고
- 병종 상성, 후방 침투, 스킬북·장비를 이용한 한 게임 단위 빌드 구성

## 먼저 읽을 문서

1. [`AGENTS.md`](AGENTS.md) — Codex와 공동 작업자의 작업 규칙
2. [`docs/DOCUMENTATION_MAP.md`](docs/DOCUMENTATION_MAP.md) — 작업별 문서 라우터
3. [`docs/GAME_DESIGN.md`](docs/GAME_DESIGN.md) — 현재 게임 기획서
4. [`docs/GODOT_PROJECT_STRUCTURE.md`](docs/GODOT_PROJECT_STRUCTURE.md) — Godot 구조와 상태 소유 원칙
5. [`docs/REFERENCE_REPOSITORIES.md`](docs/REFERENCE_REPOSITORIES.md) — Base·urban-legend 채택/제외 기준
6. [`docs/ROADMAP.md`](docs/ROADMAP.md) — 단계별 개발 순서
7. [`docs/DECISIONS_PENDING.md`](docs/DECISIONS_PENDING.md) — 구현 전 확정할 항목

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
├─ tests/
├─ assets/
└─ docs/
   ├─ GAME_DESIGN.md
   ├─ GODOT_PROJECT_STRUCTURE.md
   ├─ REFERENCE_REPOSITORIES.md
   ├─ ROADMAP.md
   ├─ DECISIONS_PENDING.md
   ├─ goals/
   └─ ai/
```

실제 폴더는 Phase 0 Goal에서 최소 프로젝트를 생성하며 확정합니다.

## Codex 작업 방식

- 모든 구현은 승인된 GitHub Issue 또는 `docs/goals/`의 Goal을 기준으로 진행합니다.
- Codex는 파일을 수정하기 전에 목표, 범위, 제외 범위, 예상 파일, 위험, 완료 기준, 검증 방법을 먼저 요약합니다.
- 구현 결과는 별도 브랜치와 Pull Request로 제출합니다.
- 이 대화에서 확정된 기획과 규칙은 관련 문서에 바로 반영해 `main`에 push합니다.
- 벤치마킹 대상의 코드, 명칭, UI, 아트 자산을 복제하지 않습니다.

권장 브랜치 이름:

```text
codex/issue-<번호>-<짧은-설명>
```

## 구조 참고

- [`alsdmlals4-eng/Base`](https://github.com/alsdmlals4-eng/Base): spec-first, Issue/Goal, 검증과 Compound 작업 규칙
- [`alsdmlals4-eng/urban-legend`](https://github.com/alsdmlals4-eng/urban-legend): Godot 장면·스크립트 분리, AutoLoad, 데이터 기반 구조, 네이티브 UI와 headless 검증 사례

참고 저장소는 구조와 작업 방법을 분석하는 용도입니다. 프로젝트별 게임 코드와 데이터를 직접 복사하거나 자동 동기화하지 않습니다.

## 게임성 참고 방향

- Slotbound: 슬롯과 오토배틀의 결합 방식 참고
- Commander Quest: 실시간 배치, 건설 노드, 전장 가독성 참고
- Desert Strike 계열: 생산시설과 장기 경제 선택 참고
- Mechabellum: 병종 상성 및 후방 특수 배치 참고

참고 대상은 게임성 분석용입니다. 자산·코드·고유 명칭·레이아웃을 그대로 복제하지 않습니다.