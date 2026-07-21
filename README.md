# Omenward

Omenward는 3레인 배치·룰렛·병종 획득·거점 공방을 연결한 싱글플레이 PvE 전략 오토배틀 프로토타입이다.

## Start and current state

- 시작: [`START_HERE.md`]([기획서]/00_프로젝트_허브/START_HERE.md)
- 현재 상태: [`ACTIVE_CONTEXT.md`]([기획서]/00_프로젝트_허브/ACTIVE_CONTEXT.md)
- 책임 원본·Skill·검증: [`DOCUMENTATION_MAP.md`]([기획서]/00_프로젝트_허브/DOCUMENTATION_MAP.md)
- Base 기준: `alsdmlals4-eng/Base@ee265576da7f67d3278f8099dd97d4e714ef0651`
- Base 동기화 감사: [`BASE_SYNC_AUDIT_2026-07-21.md`](docs/base/BASE_SYNC_AUDIT_2026-07-21.md)
- PR 작업 브랜치: `codex/omenward-active`

Base PR #18 `d2457e75a856260d309203e20262f2a2142d2dd6`의 Productivity 연결은 현재 Base main의 정본이 아니므로 비정본 legacy extension으로만 보존한다.

## Operating model

```text
요청
→ PLAN / BUILD / REVIEW
→ trigger 기반 Foundation·Specialist·분야 Skill 자동 선택
→ 승인 계약
→ 최소 구현
→ 정본·참조·정적·런타임·회귀·발행 검증
→ Active Context·Learning·PR 증거
```

- 전체 Skill을 기본 로드하지 않는다.
- Foundation Skill 최대 3개, 주 책임 분야 Skill 최대 1개.
- 사용자가 Skill 이름을 지정하지 않아도 자동 라우팅한다.
- 24개 활성 Skill 패키지와 Registry 경로는 1:1이어야 한다.
- 실행하지 않은 검증은 `NOT_RUN` 또는 `[미검증]`.

## Selected disciplines

Omenward에서는 아래 11개 분야가 모두 실제 책임을 가지므로 전부 선택돼 있다.

| 분야 | 본책 |
|---|---|
| 설정·내러티브 | [`01_설정_내러티브_본책.md`]([기획서]/01_설정_내러티브/01_설정_내러티브_본책.md) |
| 게임 디자인 | [`02_게임_디자인_본책.md`]([기획서]/02_게임_디자인/02_게임_디자인_본책.md) |
| UX·UI·접근성 | [`03_UX_UI_접근성_본책.md`]([기획서]/03_UX_UI_접근성/03_UX_UI_접근성_본책.md) |
| 개발·엔지니어링 | [`04_개발_엔지니어링_본책.md`]([기획서]/04_개발_엔지니어링/04_개발_엔지니어링_본책.md) |
| 테크니컬 아트·콘텐츠 파이프라인 | [`05_테크니컬아트_콘텐츠_파이프라인_본책.md`]([기획서]/05_테크니컬아트_콘텐츠_파이프라인/05_테크니컬아트_콘텐츠_파이프라인_본책.md) |
| 아트 | [`06_아트_본책.md`]([기획서]/06_아트/06_아트_본책.md) |
| 사운드 | [`07_사운드_본책.md`]([기획서]/07_사운드/07_사운드_본책.md) |
| QA | [`08_QA_본책.md`]([기획서]/08_QA/08_QA_본책.md) |
| 프로덕션·PM | [`09_프로덕션_PM_본책.md`]([기획서]/09_프로덕션_PM/09_프로덕션_PM_본책.md) |
| 분석·유저리서치 | [`10_분석_유저리서치_본책.md`]([기획서]/10_분석_유저리서치/10_분석_유저리서치_본책.md) |
| 통합검수 | [`11_통합검수_본책.md`]([기획서]/11_통합검수/11_통합검수_본책.md) |

## Validation

- Python contract·Schema·Skill package integrity
- active Markdown links
- Skill Map and design-document publication regeneration
- Godot editor import → headless 6종 → runtime smoke
- 1920×1080·1280×720 사람 플레이/시각 QA는 별도 증거 필요
- 승인 전장 시안·표시·저장 계약 보존
