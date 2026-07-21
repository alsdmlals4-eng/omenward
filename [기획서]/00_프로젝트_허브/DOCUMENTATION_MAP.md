# OMENWARD Documentation Map

질문마다 아래의 현행 책임 원본 하나를 먼저 읽고, 필요한 최소 Skill과 실제 파일·테스트를 연결한다.

## Project operations

| 질문 | 책임 원본 | 자동 진입 Skill |
|---|---|---|
| 어디서 시작하고 현재 무엇을 해야 하는가 | `START_HERE.md`, `ACTIVE_CONTEXT.md` | `maintaining-project-context-and-handoff` |
| 요청의 범위·승인·순서는 무엇인가 | 승인 Issue/직접 요청, `AI_WORKFLOW.md` | `managing-project-intake-and-work-contract` |
| Base 기준과 차이는 무엇인가 | `BASE_RULES_VERSION.md`, `docs/base/BASE_SYNC_AUDIT_2026-07-21.md` | `managing-game-project-operating-system` |
| 문서·Skill·발행 구조가 건강한가 | Registry·Development Gates·Manifest | `managing-game-project-operating-system: verify` |
| 오래된 경로·ID·Schema·생성물이 남았는가 | `LEGACY_SKILL_ALIASES.md`, `LEGACY_ARTIFACT_RECONCILIATION.md` | `auditing-canonical-reference-freshness` |
| 변경이 계약과 실행 증거를 만족하는가 | `SKILL_EXECUTION_REPORT.md`, 테스트·PR | `reviewing-and-validating-project-changes` |
| 프로젝트 교훈을 Base에 올릴 것인가 | Learning Log·증거 | `managing-base-change-proposals` |

## Design and product

| 질문 | 책임 본책 | 주 분야 Skill | 필요 시 Specialist |
|---|---|---|---|
| 세계관·명칭·벨루 | 01 설정·내러티브 | `omenward-narrative` | `analyzing-and-refining-game-concepts` |
| 룰렛·전장·병종·경제 | 02 게임 디자인 | `omenward-game-design` | `analyzing-and-refining-game-concepts`, `designing-vertical-slices` |
| HUD·입력·튜토리얼·접근성 | 03 UX·UI·접근성 | `omenward-ux-ui-accessibility` | `auditing-and-refining-ui-art` |
| 코드·Scene·Resource·저장·성능 | 04 개발·엔지니어링 | `omenward-engineering` | `reviewing-and-validating-project-changes` |
| import·애니메이션·콘텐츠 파이프라인 | 05 테크니컬 아트 | `omenward-technical-art-pipeline` | `designing-vertical-slices` |
| 아트 방향·시안·스프라이트 | 06 아트 | `omenward-art` | `designing-art-prompts-and-technique-cards`, `auditing-and-refining-ui-art` |
| 음악·효과음·믹싱 | 07 사운드 | `omenward-audio` | `designing-vertical-slices` |
| 재현·회귀·플레이 검증 | 08 QA | `omenward-qa` | `reviewing-and-validating-project-changes` |
| Roadmap·Issue·위험·Handoff | 09 프로덕션·PM | `omenward-production-pm` | `managing-project-intake-and-work-contract` |
| 벤치마크·반응·텔레메트리·실험 | 10 분석·유저리서치 | `omenward-analytics-user-research` | `analyzing-and-refining-game-concepts` |
| 마이그레이션·릴리스·보존·콜드 스타트 | 11 통합검수 | `omenward-integration-review` | `auditing-canonical-reference-freshness` |

## Registries and generated publications

- `DESIGN_DOCUMENT_REGISTRY.json`: 질문·문서 ID·정본·발행 정책
- `SKILL_REGISTRY.json`: 자동 routing·Work Mode·Skill·Learning
- `ASSET_REGISTRY.json`: 승인 자산·경로·해시·상태
- `PROJECT_SKILL_MAP.md/.pdf/.assets`와 Manifest: Registry의 읽기 전용 파생본
- 각 본책 PDF와 Publication Manifest: Markdown 책임 원본의 읽기 전용 파생본

## Lifecycle boundaries

- `[백업]`: 복구·역사
- `[보류]`: 미승인·재개 대기
- `legacy_extensions`: 현재 정본이 아니지만 삭제하지 않은 호환 정보
- 활성 구현은 등록된 정본·Registry·승인 계약만 사용
