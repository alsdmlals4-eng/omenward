# OMENWARD Base Shared Skill 맞춤형 통합

```yaml
updated_at: 2026-09-01
canonical_machine_owner: skills/PROJECT_BASE_ADAPTER.json
generated_route_owner: skills/PROJECT_SKILL_SNAPSHOT.json
adapter_schema: PROJECT_BASE_ADAPTER_V2
released_semantic_contract: Base v9.4.4
release_payload: 210ec78292fa12ed7563ba743b322dd36103ae4a
release_evidence: bb61e68dc3028421b60c11b87ba2abd297ee6f78
release_finalization: 5adc196c0185951f50e49ab5e51586eff8d60886
current_validator_reference: 19355b7ef065a21d0f2b685c7d9be64a4a3970f8
unreleased_v9_5_policy_adoption: NONE
project_identity: omenward
```

## 1. 목적과 현재 결론

OMENWARD는 Base를 공용 운영 체계로 사용하되, 현재 제품의 single-front, repository-only canon, user-approved asset lifecycle, Godot protection boundary를 Base의 generic example로 치환하지 않는다.

이번 갱신은 다음을 고정한다.

| 항목 | 채택 | 제외 / 보류 |
| --- | --- | --- |
| Released reuse-first contract | Base **v9.4.4** pin | v9.4.3의 이전 pin 유지 |
| Adapter data shape | v2 + explicit `project_id: omenward` | path/repository 이름으로 identity 추론 |
| Base current | Git-canonical evidence validator reference | unreleased v9.5 policy/product adoption |
| Knowledge reuse | preflight + handoff only | Base module의 자동 설치 또는 runtime 연결 |
| Human authority | repository owner | Notion/Google Sheet의 current workspace 복귀 |

## 2. Source of truth와 생성물

```text
skills/PROJECT_BASE_ADAPTER.json
    ├── skills/PROJECT_SKILL_SNAPSHOT.json         generated route view
    ├── skills/BASE_V9_ADAPTER.json                generated compatibility view
    ├── skills/PROJECT_BASE_SKILL_ADAPTER.json     generated compatibility view
    ├── .agents/skills/omenward-workflow-router/SKILL.md
    └── docs/PROJECT_OPERATING_DASHBOARD.html
```

`PROJECT_BASE_ADAPTER.json`만 사람이 수정하는 machine canon이다. 나머지는 Base generator가 만드는 파생물이며, 직접 수정하지 않는다. legacy input 원본은 `docs/archive/base-v9-legacy-inputs/`에 보존하지만 current route가 아니다.

현재 adapter v2의 의미:

```text
PROJECT_IDENTITY = omenward
GDD_SHEET_ROLE = GOOGLE_SHEETS_LEGACY_MIGRATION_SOURCE
GDD_SHEET_STATE = STALE / MIGRATION_COMPATIBILITY_SURFACE
CURRENT_HUMAN_AUTHORITY = REPOSITORY_ONLY
NOTION = RETIRED__NO_FUTURE_READ_OR_WRITE
```

이는 historical Sheet/Notion 증거를 삭제하거나 무효화하지 않는다. repository-only policy의 현재 의미를 정확히 표현할 뿐이다.

## 3. Base v9.4.4와 current validator의 역할 분리

Base v9.4.4 released lock은 current semantic contract다. exact identity는 adapter와 `base-v9.4.4.lock.json`으로 검증한다.

```text
released content / lock / registry  → Base at 5adc196... (v9.4.4 finalization)
validator program                  → Base at 19355b7... (Git-canonical EOL handling)
v9.5 candidate policy              → NOT ADOPTED
```

분리는 의도적이다. frozen v9.4.4 validator는 Windows working-tree raw bytes가 LF checkout과 달라질 때 generated evidence를 false mismatch로 판단할 수 있다. current validator reference는 Git canonical bytes를 사용한다. 반면 release registry, lock, Skill contract는 exact v9.4.4 worktree에서 읽으므로 최신 candidate 정책이 프로젝트 규칙으로 유입되지 않는다.

## 4. 맞춤 route와 reuse-first order

Router는 먼저 project-local route를 확인한 뒤 필요한 Base shared route만 연다.

```text
project-local: omenward-core-design / omenward-core-ux / omenward-godot / omenward-art-assets
Base shared: intake, game operating system, design docs, freshness, validation,
             legacy governance, context/handoff, Base-change proposal, cost, worktree routes
```

새 system/data/UI/visual/tool/workflow/test가 scope에 들어오면 다음 preflight 순서를 따른다.

1. current project decision, implementation, consumer, approved asset/reference를 읽는다.
2. Base `PROJECT_WORK_REUSE_HANDOFF.json`과 OMENWARD profile을 확인한다.
3. 기존 project/Base 자료로 부족한 부분만 targeted benchmark 또는 primary source로 조사한다.
4. `REUSE / ADAPT / EXTRACT_PROJECT_ONLY_MODULE / NO_REUSE` 중 하나를 선택하고 consumer, provenance, rollback을 기록한다.
5. implementation 뒤 `REUSE_LEARNING_HANDOFF_REQUIRED`를 처리한다.

새 consumer가 없는 mechanical documentation/adapter regeneration은 `NOT_APPLICABLE`로 끝낼 수 있다. 이 작업은 new runtime module, asset, dependency, Godot scene을 추가하지 않았다.

## 5. Operating contract commands

PowerShell에서 current validator source와 exact released Base content를 분리해 사용한다.

```powershell
$validatorBase = 'C:\Users\user\Documents\GitHub\Base'
$releasedBase = '<Base v9.4.4 exact worktree>'
$project = '<OMENWARD worktree>'
$python = "$validatorBase\.venv\Scripts\python.exe"

& $python "$validatorBase\tools\check_approved_project_operating_contract.py" `
  --project-root $project `
  --base-repository $releasedBase `
  --protected-base 9a67a267a69c80fba6f25d5a37e360a15dcc2419 `
  --approval docs\approvals\PROJECT_PROTECTED_CHANGE_APPROVAL_GLOBAL_ROSTER_AND_STRATEGIC_MAP_2026-08-30.json `
  --external-approval true `
  --check
```

The adapter retains the original approved protected baseline because the approved game implementation remains part of the working history. Therefore adapter CI always runs the exact approval manifest route; it fails if the detected protected paths differ from that manifest. A future baseline migration is a separate approval/review task, not an automatic switch to the ordinary checker. CI never silently bypasses the protected-path rule.

## 6. Project-specific adaptations

| Base principle | OMENWARD adaptation | Why |
| --- | --- | --- |
| Fresh-read current authority | Decision/Active Context + actual Godot consumer first | product topology and runtime evidence move faster than global templates |
| Reuse-first | consumer-first art/system screening | prevents unbound modules or decorative visual candidates |
| Generated operating views | LF-tracked derived files | prevents Windows EOL from creating phantom drift |
| Protected path validation | exact user approval manifest when protected diff exists | preserves approved game implementation without weakening the gate |
| Human canon | repository-only docs | Notion is retired; Sheet is historical compatibility only |
| Runtime evidence | machine/runtime/human/release gates separate | technical smoke does not imply player or release acceptance |

## 7. What this does not claim

- No v9.5 policy, Tool Hub deployment, or Base current candidate has been adopted.
- No Base reusable module has become a new OMENWARD runtime dependency.
- No Godot code, scene, data, save format, approved asset bytes, game balance, or product decision changed.
- No player/human/device/accessibility/release evidence was executed by this contract-only update.

## 8. Future Base promotion

The evidence-byte/EOL repair is already handled by the current validator reference. It is not a new OMENWARD-specific Base promotion request. Future project-specific findings must stay in project owners until repeated cross-project evidence justifies a separately reviewed Base proposal.
