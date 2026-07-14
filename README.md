# Roulettebound Prototype

건물로 룰렛의 토큰 풀을 설계하고, 상·중·하 3개 전선을 실시간으로 운영하는 판타지 전략 오토배틀 프로토타입입니다.

> 현재 상태: **기획 확정 및 기술 기반 결정 전**  
> 구현 엔진과 대상 플랫폼은 아직 확정되지 않았습니다. Codex는 관련 Issue/Goal 승인 전 임의로 엔진 프로젝트를 생성하지 않습니다.

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
2. [`docs/GAME_DESIGN.md`](docs/GAME_DESIGN.md) — 현재 게임 기획서
3. [`docs/ROADMAP.md`](docs/ROADMAP.md) — 단계별 개발 순서
4. [`docs/DECISIONS_PENDING.md`](docs/DECISIONS_PENDING.md) — 구현 전 확정할 항목
5. [`docs/BASE_RULES_VERSION.md`](docs/BASE_RULES_VERSION.md) — 공용 Base 규칙 기준 버전

원본 DOCX 기획서는 [`docs/GAME_DESIGN_v0.7.docx`](docs/GAME_DESIGN_v0.7.docx)에 보관합니다.

## 저장소 구조

```text
.
├─ AGENTS.md
├─ README.md
├─ docs/
│  ├─ GAME_DESIGN.md
│  ├─ GAME_DESIGN_v0.7.docx
│  ├─ ROADMAP.md
│  ├─ DECISIONS_PENDING.md
│  ├─ ACTIVE_CONTEXT.md
│  ├─ BASE_RULES_VERSION.md
│  ├─ goals/
│  ├─ ai/
│  └─ images/
├─ src/                 # 엔진 결정 후 실제 프로젝트 구조로 교체
├─ tests/               # 검증 체계 결정 후 구성
└─ .github/
   ├─ ISSUE_TEMPLATE/
   └─ PULL_REQUEST_TEMPLATE.md
```

## Codex 작업 방식

- 모든 구현은 승인된 GitHub Issue 또는 `docs/goals/`의 Goal을 기준으로 진행합니다.
- Codex는 파일을 수정하기 전에 목표, 범위, 제외 범위, 예상 파일, 위험, 완료 기준, 검증 방법을 먼저 요약합니다.
- 구현 결과는 별도 브랜치와 Pull Request로 제출합니다.
- 벤치마킹 대상의 코드, 명칭, UI, 아트 자산을 복제하지 않습니다.

권장 브랜치 이름:

```text
codex/issue-<번호>-<짧은-설명>
```

## 참고 방향

- Slotbound: 슬롯과 오토배틀의 결합 방식 참고
- Commander Quest: 실시간 배치, 건설 노드, 전장 가독성 참고
- Desert Strike 계열: 생산시설과 장기 경제 선택 참고
- Mechabellum: 병종 상성 및 후방 특수 배치 참고

참고 대상은 게임성 분석용입니다. 자산·코드·고유 명칭·레이아웃을 그대로 복제하지 않습니다.
