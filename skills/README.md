# Omenward Skill System

이 디렉터리는 Base의 공용 작업 방법을 Omenward 책임 구조에 맞게 적용한 실행 패키지다.

## 시작

```powershell
$validatorBase = '<Base current validator checkout>'
$releasedBase = '<Base v9.4.4 exact checkout>'
python "$validatorBase/tools/check_approved_project_operating_contract.py" `
  --project-root . `
  --base-repository $releasedBase `
  --protected-base 9a67a267a69c80fba6f25d5a37e360a15dcc2419 `
  --approval docs/approvals/PROJECT_PROTECTED_CHANGE_APPROVAL_GLOBAL_ROSTER_AND_STRATEGIC_MAP_2026-08-30.json `
  --external-approval true `
  --check
python -m unittest tests.test_base_v944_reuse_first_adoption tests.python.test_project_base_adapter_freshness -v
```

The released Base v9.4.4 content and the current Base validator are intentionally separate: the former owns the semantic pin, while the latter verifies generated Git bytes safely across Windows line endings. An unreleased Base candidate is never adopted by this command.

현재 자동 라우팅 정본은 `.agents/skills/omenward-workflow-router/SKILL.md`이며, 이 Router는
`skills/PROJECT_BASE_ADAPTER.json`과 생성된 `skills/PROJECT_SKILL_SNAPSHOT.json`만 읽는다.
`docs/base/SKILL_REGISTRY.json`과 이 디렉터리의 과거 패키지는 명시적으로 열어 보는 호환·이력 자료이며 자동 선택 대상이 아니다.

## 활성 구조

- `SHARED_EXECUTION_CONTRACT.md`: 모든 Skill이 공유하는 우선순위·Work Mode·검증 계약
- `SKILL_REGISTRY.json`: Omenward 고유 활성 Skill 4개의 기계 판독 정본
- `PROJECT_BASE_ADAPTER.json`: Base v9.4.4 pin, explicit `omenward` identity, 공용·로컬 route, repository-only migration boundary, 보호 경로의 계약 정본
- `PROJECT_SKILL_SNAPSHOT.json`: 위 계약에서 생성된 효과 route view
- `foundation/`, 과거 `disciplines/`, `specialists/`: 레거시·호환 자료; 자동 발견 금지

`PROJECT_BASE_ADAPTER.json`은 schema v2다. Google Sheet는 `GOOGLE_SHEETS_LEGACY_MIGRATION_SOURCE`이며 current human authority가 아니다. Notion은 retired policy에 따라 routine read/write target이 아니다.

활성 Discipline:

- `discipline.omenward-core-design`
- `discipline.omenward-godot`
- `discipline.omenward-core-ux`
- `discipline.omenward-art-assets`

과거 11개 Discipline과 5개 Specialist 패키지는 `inactive` 역사 자료로 유지한다. Router는 이 패키지를 직접 선택하지 않으며, 레거시 ID는 Registry의 `aliases`와 `replaced_by`로 활성 Skill에 해석한다.

## 최적화 원칙

- 공통 규칙은 한 번만 정의한다.
- 개별 Skill은 고유 책임·입력·절차·출력만 가진다.
- `routing.always_on`은 비워 두고 trigger와 stage로만 선택한다.
- 한 작업의 주 책임 Discipline은 하나이며 지원 Discipline은 최대 하나다.
- REVIEW는 `foundation.validation-review`와 `specialist.canonical-freshness`를 추가한다.
- 비활성 Skill, 중복 ID, 고아 패키지, 잘못된 alias·dependency와 과도한 자동 선택은 CI에서 실패한다.
- 새 system/data/UI/visual/tool/workflow/test에는 current project consumer → approved project reference → Base reuse handoff/profile → targeted evidence 순서의 reuse-first preflight를 적용한다.
