# OMENWARD 작업 시작

## 목적

오멘워드는 건물 구성과 룰렛 확률 변화, 공용 10병종 획득, 독립 3라인 배치, 거점·성문 공방을 연결하는 싱글플레이 PvE 전략 오토배틀이다.

## 10분 콜드 스타트

1. `AGENTS.md`와 이 문서에서 우선순위·보호 범위·Base 기준을 확인한다.
2. `ACTIVE_CONTEXT.md`에서 현재 단계·다음 작업·미검증을 확인한다.
3. `DOCUMENTATION_MAP.md`와 `DESIGN_DOCUMENT_REGISTRY.json`에서 질문의 단일 책임 원본을 찾는다.
4. `SKILL_REGISTRY.json`에서 Work Mode와 trigger가 맞는 최소 Skill을 자동 선택한다.
5. `DEVELOPMENT_GATES.md`, 승인 Issue/Plan, 실제 코드·Scene·데이터·테스트를 대조한다.
6. 변경 뒤 정본·참조·발행·Context·Learning을 갱신한다.

## Current baseline

- Base main: `ee265576da7f67d3278f8099dd97d4e714ef0651`
- Omenward integration branch: `codex/omenward-active`
- Base PR #18 `d2457e75a856260d309203e20262f2a2142d2dd6` Productivity 연결: 비정본 legacy extension
- 현재 범위: 운영체계·문서·Skill·검증 정합성. 게임 규칙·콘텐츠 재설계는 범위 밖.

## Automatic routing

```text
요청
→ PLAN / BUILD / REVIEW 판정
→ Foundation 최대 3개
→ 주 책임 분야 Skill 최대 1개
→ 필요 시 Specialist
→ 실행·검증
→ 사용 이유·결과·미검증 보고
```

사용자가 Skill 이름을 직접 고를 필요가 없다. 전체 `skills/`를 기본 로드하지 않는다.

## Selected disciplines

| 번호 | 분야 | 책임 본책 | 진입 Skill |
|---:|---|---|---|
| 01 | 설정·내러티브 | `../01_설정_내러티브/01_설정_내러티브_본책.md` | `omenward-narrative` |
| 02 | 게임 디자인 | `../02_게임_디자인/02_게임_디자인_본책.md` | `omenward-game-design` |
| 03 | UX·UI·접근성 | `../03_UX_UI_접근성/03_UX_UI_접근성_본책.md` | `omenward-ux-ui-accessibility` |
| 04 | 개발·엔지니어링 | `../04_개발_엔지니어링/04_개발_엔지니어링_본책.md` | `omenward-engineering` |
| 05 | 테크니컬 아트·콘텐츠 파이프라인 | `../05_테크니컬아트_콘텐츠_파이프라인/05_테크니컬아트_콘텐츠_파이프라인_본책.md` | `omenward-technical-art-pipeline` |
| 06 | 아트 | `../06_아트/06_아트_본책.md` | `omenward-art` |
| 07 | 사운드 | `../07_사운드/07_사운드_본책.md` | `omenward-audio` |
| 08 | QA | `../08_QA/08_QA_본책.md` | `omenward-qa` |
| 09 | 프로덕션·PM | `../09_프로덕션_PM/09_프로덕션_PM_본책.md` | `omenward-production-pm` |
| 10 | 분석·유저리서치 | `../10_분석_유저리서치/10_분석_유저리서치_본책.md` | `omenward-analytics-user-research` |
| 11 | 통합검수 | `../11_통합검수/11_통합검수_본책.md` | `omenward-integration-review` |

## Protection and next work

- 기존 승인 문서·자산·수치·코드·저장 형식을 보존한다.
- 충돌을 해결할 근거가 없으면 삭제·추정하지 않고 `[확인 필요]`로 남긴다.
- 다음 제품 변경은 최신 Issue 또는 승인된 직접 요청 계약으로 시작한다.
- 구조·Skill·Base 갱신은 `managing-game-project-operating-system`과 `auditing-canonical-reference-freshness`를 함께 사용한다.

## Validation path

```text
Python contract tests
→ active Markdown links
→ Registry/Schema/package integrity
→ publication regeneration and clean diff
→ Godot editor import
→ headless 6종
→ runtime smoke
→ 필요한 사람 QA
```
