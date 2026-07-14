# Documentation Map

이 문서는 Codex와 공동 작업자가 현재 작업에 필요한 문서만 읽도록 안내하는 라우터다. 모든 문서를 매번 읽지 않는다.

## 기본 읽기 순서

`최신 사용자 지시 → AGENTS.md → BASE_RULES_VERSION.md → DOCUMENTATION_MAP.md → PROPOSAL_WORKFLOW.md → GAME_DESIGN.md → 조건부 문서 → Issue/Goal → 승인된 제안서 → 대상 파일 → ACTIVE_CONTEXT.md`

## 조건부 라우팅

| 작업 조건 | 추가로 읽을 문서 |
|---|---|
| Codex Plan Mode 검토 또는 구현 전 제안서 | `PROPOSAL_WORKFLOW.md`, 현재 Issue/Goal |
| Godot 프로젝트 생성, Scene·Node·AutoLoad·데이터 구조 | `GODOT_PROJECT_STRUCTURE.md` |
| Base 또는 urban-legend 구조 참고 | `REFERENCE_REPOSITORIES.md` |
| 게임 규칙·룰렛·건물·접전지·웨이브 변경 | `GAME_DESIGN.md` |
| 단계와 우선순위 변경 | `ROADMAP.md`, `ACTIVE_CONTEXT.md` |
| 미확정 수치나 정책을 결정 | `DECISIONS_PENDING.md` |
| 실제 구현 시작 | 사용자 승인된 제안서, 현재 GitHub Issue와 대응 Goal |
| 외부 게임·도구·저장소 벤치마킹 | `docs/ai/BENCHMARKING_REFERENCE_GUIDE.md`가 존재하면 읽고, 없으면 Issue에 적용/제외 결론을 기록 |
| 외부 AI·스킬·코드 위임 | `docs/ai/`의 관련 규칙과 `AGENTS.md`의 보안·검증 원칙 |
| 작업 종료와 인수인계 | `ACTIVE_CONTEXT.md`, PR 템플릿, 완료 보고 형식 |

분기 조건이 없으면 해당 문서를 읽지 않는다. 복합 작업은 실제 영향이 있는 갈래만 추가한다.

## 책임 원본

- 우선순위, Godot 불변 조건, GitHub 반영 방식, Plan Mode 승인 게이트, 완료 보고: `AGENTS.md`
- 제안서 형식과 승인 기준: `PROPOSAL_WORKFLOW.md`
- 게임의 현재 규칙과 플레이어 경험: `GAME_DESIGN.md`
- Godot 폴더·상태·Scene·UI 계약: `GODOT_PROJECT_STRUCTURE.md`
- Base·urban-legend 채택 및 제외 기준: `REFERENCE_REPOSITORIES.md`
- 개발 순서: `ROADMAP.md`
- 미확정 항목: `DECISIONS_PENDING.md`
- 현재 작업 상태: `ACTIVE_CONTEXT.md`
- 현재 검토·구현 범위와 완료 기준: 최신 Issue/Goal 및 승인된 제안서
- 공용 규칙 기준 커밋: `BASE_RULES_VERSION.md`

다른 문서가 같은 내용을 반복하면 위 책임 원본을 링크하고 작업별 차이만 기록한다.

## 참고 저장소 경계

- Base 원격은 공용 규칙의 기준 확인, 동기화, 승격 후보 검토 때 사용한다.
- urban-legend 원격은 Godot 구조·검증 사례가 현재 작업과 직접 관련될 때 필요한 파일만 확인한다.
- 외부 저장소 변경을 이 프로젝트에 자동 병합하지 않는다. 채택할 구조는 제안서, Issue/Goal과 프로젝트 문서에서 명시적으로 승인한다.
