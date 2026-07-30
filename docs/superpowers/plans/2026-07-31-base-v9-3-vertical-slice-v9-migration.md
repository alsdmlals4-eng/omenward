# Base v9.3 + Vertical Slice v9 Migration Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Omenward의 제품 코어와 보호 경로를 변경하지 않고 Base v9.1 운영계약을 Base v9.3.0 + Vertical Slice v9 Application Binding으로 이관한다.

**Architecture:** `skills/PROJECT_BASE_ADAPTER.json`을 유일한 프로젝트 통합 권한으로 유지하고 Base v9.3 도구로 Snapshot·Health·Dashboard·compatibility view를 결정론적으로 재생성한다. 프로젝트 정본 진입점은 Full-System Vertical Slice와 제품 미구현 상태로 정렬하며, 프로젝트 전용 4개 Skill은 유지하고 공용 능력은 Base route로만 연결한다.

**Tech Stack:** GitHub, Markdown, JSON, Python 3, Base v9.3 project operating tools, Godot project metadata only. 제품 GDScript·Scene·Resource는 변경하지 않는다.

## Global Constraints

- 프로젝트명: 오멘워드(OMENWARD)
- 저장소: `alsdmlals4-eng/omenward`
- 기준 main: `774087dccc903bc9a8e2aec72eec2a2d13b216ce`
- 작업 Issue: `#115`
- Base version: `9.3.0`
- Base release commit: `30ca6c7b5f93521f0eb0eed42d01437cd43c50ae`
- Base evidence commit: `462a86db192d23d0f386281a1eb54b0a8cbad62e`
- Base Registry SHA-256: `9847bb2b225c776ad7916930f0f48c490bc2a898bea8e02ea1fdd0e6caac60c1`
- 주 플랫폼: PC
- 모바일: 후속 검토, 이번 범위 제외
- 제품 코드·Scene·데이터·에셋 변경 금지
- Google Sheet 쓰기 금지
- 생성물 수동 편집 금지
- 실제로 실행하지 않은 Runtime·device·accessibility·human 검증은 `NOT_RUN`

---

## File Structure

### 신규 감사·계획 문서

- `docs/operations/VERTICAL_SLICE_V9_APPLICATION.md`: 프로젝트 v9 Application Binding
- `docs/audits/OMENWARD_BASE_V9_3_APPLICATION_BINDING_PACKET_2026-07-31.md`: 기준선·traceability·propagation·finding·readiness
- `docs/audits/OMENWARD_BASE_V9_3_APPROVAL_BUNDLE_2026-07-31.md`: 승인 범위·명령·수용 기준·롤백
- `docs/superpowers/plans/2026-07-31-base-v9-3-vertical-slice-v9-migration.md`: 이 실행 계획

### 수정할 정본·진입점

- `AGENTS.md`
- `docs/BASE_RULES_VERSION.md`
- `docs/DOCUMENTATION_MAP.md`
- `docs/ACTIVE_CONTEXT.md`
- `docs/HANDOFF_CONTEXT.md`
- `docs/BASE_SHARED_SKILL_INTEGRATION.md`
- 필요한 README / START_HERE 소비자

### 수정할 기계 계약

- `skills/PROJECT_BASE_ADAPTER.json`
- `skills/SKILL_REGISTRY.json`
- 프로젝트 전용 4개 `SKILL.md`
- `skills/SHARED_EXECUTION_CONTRACT.md`
- `.agents/skills/omenward-workflow-router/SKILL.md`

### Base 도구가 생성할 파일

- `skills/PROJECT_SKILL_SNAPSHOT.json`
- `docs/PROJECT_OPERATING_HEALTH.json`
- `docs/PROJECT_OPERATING_DASHBOARD.html`
- `skills/BASE_V9_ADAPTER.json`
- `skills/PROJECT_BASE_SKILL_ADAPTER.json`
- 존재하는 경우 `skills/PROJECT_PATH_ADAPTER.json`

### 검증

- `tests/python/`의 adapter·skill·reference 관련 테스트
- `.github/workflows/validate-skill-system.yml`
- 프로젝트 adapter 검증 workflow

---

### Task 1: 기준선과 실패 조건 고정

**Files:**
- Read: `AGENTS.md`
- Read: `docs/DOCUMENTATION_MAP.md`
- Read: `docs/PROJECT_CORE.md`
- Read: `docs/CURRENT_IMPLEMENTATION_STATUS.md`
- Read: `skills/PROJECT_BASE_ADAPTER.json`
- Read: `skills/PROJECT_SKILL_SNAPSHOT.json`
- Read: `skills/SKILL_REGISTRY.json`
- Read: `docs/audits/OMENWARD_BASE_V9_3_APPLICATION_BINDING_PACKET_2026-07-31.md`

**Interfaces:**
- Consumes: `main@774087d...`, Base v9.3 checkout, Issue #115
- Produces: 검증 가능한 baseline report와 보호 경로 diff 0 기준

- [ ] **Step 1: 저장소와 Base 기준선 확인**

```bash
git fetch origin
git rev-parse origin/main
git -C "$BASE_ROOT" rev-parse 30ca6c7b5f93521f0eb0eed42d01437cd43c50ae^{commit}
git -C "$BASE_ROOT" rev-parse 462a86db192d23d0f386281a1eb54b0a8cbad62e^{commit}
```

Expected:

```text
origin/main = 774087dccc903bc9a8e2aec72eec2a2d13b216ce
두 Base commit 모두 존재
```

- [ ] **Step 2: 보호 경로 기준 목록 저장**

```bash
git diff --name-only 774087dccc903bc9a8e2aec72eec2a2d13b216ce -- \
  data scripts scenes resources assets addons project.godot
```

Expected: 출력 없음.

- [ ] **Step 3: 현재 v9.1 검증을 실행해 baseline 증거 수집**

```bash
python "$BASE_ROOT/tools/check_project_operating_contract.py" \
  --project-root . \
  --base-repository "$BASE_ROOT" \
  --check
python -m unittest discover -s tests/python -v
```

Expected: 현재 입력에서 통과하거나, v9.3 checkout이 v9.1 adapter를 거부하는 정확한 실패 메시지를 기록한다. 실패를 임의 수정하지 않는다.

- [ ] **Step 4: 기준선 결과를 Issue #115 작업 로그에 기록**

기록 필드:

```text
project_main
base_release
base_evidence
current_adapter_version
protected_path_diff
static_test_result
blocked_reason
```

- [ ] **Step 5: Commit**

Task 1에서 문서 변경이 없으면 커밋하지 않는다.

---

### Task 2: Base v9.3 Adapter 이관

**Files:**
- Modify: `skills/PROJECT_BASE_ADAPTER.json`
- Generated later: `skills/PROJECT_SKILL_SNAPSHOT.json`
- Read: `docs/archive/base-v9-legacy-inputs/PROJECT_BASE_SKILL_ADAPTER.json`

**Interfaces:**
- Consumes: Base v9.3 lock, 기준 main의 archive protected policy, 프로젝트 Registry
- Produces: v9.3 canonical Adapter

- [ ] **Step 1: migration input이 기준 main에 존재하는지 확인**

```bash
git cat-file -e 774087dccc903bc9a8e2aec72eec2a2d13b216ce:docs/archive/base-v9-legacy-inputs/PROJECT_BASE_SKILL_ADAPTER.json
git show 774087dccc903bc9a8e2aec72eec2a2d13b216ce:docs/archive/base-v9-legacy-inputs/PROJECT_BASE_SKILL_ADAPTER.json | python -m json.tool > /dev/null
```

Expected: 두 명령 모두 성공.

- [ ] **Step 2: Base v9.3 Adapter 생성**

```bash
python "$BASE_ROOT/tools/migrate_project_operating_contract.py" \
  --project-root . \
  --base-repository "$BASE_ROOT" \
  --legacy-adapter docs/archive/base-v9-legacy-inputs/PROJECT_BASE_SKILL_ADAPTER.json \
  --output skills/PROJECT_BASE_ADAPTER.json \
  --base-version 9.3.0 \
  --release-commit 30ca6c7b5f93521f0eb0eed42d01437cd43c50ae \
  --release-evidence-commit 462a86db192d23d0f386281a1eb54b0a8cbad62e \
  --protected-baseline-commit 774087dccc903bc9a8e2aec72eec2a2d13b216ce \
  --protected-authority-kind REMOTE_TRACKING_REF \
  --protected-authority-ref refs/remotes/origin/main \
  --write
```

Expected: `Project adapter migrated`.

- [ ] **Step 3: 생성 Adapter의 release identity 확인**

```bash
python - <<'PY'
import json
from pathlib import Path
p = Path('skills/PROJECT_BASE_ADAPTER.json')
data = json.loads(p.read_text(encoding='utf-8'))
assert data['base_release']['version'] == '9.3.0'
assert data['base_release']['release_commit'] == '30ca6c7b5f93521f0eb0eed42d01437cd43c50ae'
assert data['base_release']['release_evidence_commit'] == '462a86db192d23d0f386281a1eb54b0a8cbad62e'
assert data['skill_registry']['base']['sha256'] == '9847bb2b225c776ad7916930f0f48c490bc2a898bea8e02ea1fdd0e6caac60c1'
assert data['gdd_sheet']['id'] == '1VLwRtXGDtyj0JFt98wdIOtG6Zqc3wtdfCzSF9Fo6lpw'
assert data['gdd_sheet']['write_policy'] == 'NO_AUTOMATIC_OVERWRITE'
print('adapter identity ok')
PY
```

Expected: `adapter identity ok`.

- [ ] **Step 4: 보호 경로 약화 여부 확인**

현재 v9.1 Adapter의 보호 경로보다 줄어든 항목이 있으면 중단한다. `resources/`는 실제 tracked 경로와 기존 정책 근거가 확인된 경우에만 추가한다.

- [ ] **Step 5: Commit**

```bash
git add skills/PROJECT_BASE_ADAPTER.json docs/PROJECT_OPERATING_HEALTH.json
git commit -m "chore: migrate Omenward adapter to Base v9.3"
```

---

### Task 3: Base shared route와 프로젝트 Skill ID 정합성 교정

**Files:**
- Modify: `skills/PROJECT_BASE_ADAPTER.json`
- Modify: `skills/SKILL_REGISTRY.json` only if ID/path metadata requires correction
- Modify: `skills/disciplines/governing-omenward-art-animation-and-assets/SKILL.md`
- Modify: `skills/disciplines/governing-omenward-core-design-and-data/SKILL.md`
- Modify: `skills/disciplines/evaluating-omenward-core-ux-and-playtests/SKILL.md`
- Modify: `skills/disciplines/planning-and-validating-omenward-godot-implementation/SKILL.md`
- Modify: `skills/SHARED_EXECUTION_CONTRACT.md`

**Interfaces:**
- Consumes: Base v9.3 Registry ACTIVE IDs, project Registry
- Produces: route-capable kebab-case IDs와 동적 stage routing

- [ ] **Step 1: Base ACTIVE route 확인**

아래 후보 각각이 Base v9.3 Registry에서 `ACTIVE`인지 검사한다.

```text
analyzing-and-refining-game-concepts
designing-vertical-slices
running-adversarial-review-and-refinement
auditing-and-refining-ui-art
identifying-project-core
establishing-project-core
synchronizing-local-and-github-state
maintaining-long-running-task-continuity
pruning-stale-and-nonfunctional-material
refactoring-with-contract-preservation
simplifying-skill-bodies
governing-game-user-research-coverage
```

Inactive·미등록 ID는 Adapter에 추가하지 않는다.

- [ ] **Step 2: 필요한 route를 `routing.base_routes`와 `shared_overrides`에 동일하게 추가**

각 route는 다음 shape을 사용한다.

```json
{
  "route_id": "designing-vertical-slices",
  "skill_id": "designing-vertical-slices",
  "status": "ACTIVE"
}
```

`shared_overrides`에는 route별 프로젝트 고유 override가 없으면 `{}`를 사용한다.

- [ ] **Step 3: 프로젝트 Skill 본문 ID를 Registry와 일치**

각 본문의 `Skill ID:`를 다음으로 교체한다.

```text
omenward-core-design
omenward-godot
omenward-core-ux
omenward-art-assets
```

Registry path와 status는 유지한다.

- [ ] **Step 4: Shared Execution Contract의 구형 ID 제거**

다음을 직접 호출하지 않는다.

```text
foundation.project-intake
foundation.validation-review
specialist.canonical-freshness
```

대신 다음 계약으로 교체한다.

```text
- 요청과 stage에 맞는 route를 PROJECT_SKILL_SNAPSHOT.effective_routes에서 선택한다.
- REVIEW에는 reviewing-and-validating-project-changes와 auditing-canonical-reference-freshness를 필요 시 추가한다.
- repository-wide audit에는 running-adversarial-review-and-refinement를 선택한다.
- 프로젝트 local route와 Base route가 같은 책임이면 local route가 우선한다.
```

- [ ] **Step 5: Project Registry hash를 Adapter에 갱신**

Registry를 수정한 경우 raw bytes SHA-256을 계산해 Adapter의 `skill_registry.project.sha256`과 일치시킨다. 생성기 실행 전 불일치를 허용하지 않는다.

- [ ] **Step 6: Commit**

```bash
git add skills/PROJECT_BASE_ADAPTER.json skills/SKILL_REGISTRY.json skills/SHARED_EXECUTION_CONTRACT.md skills/disciplines
git commit -m "refactor: align Omenward skill routes with Base v9.3"
```

---

### Task 4: 생성 operating artifacts 재생성

**Files:**
- Generated: `skills/PROJECT_SKILL_SNAPSHOT.json`
- Generated: `docs/PROJECT_OPERATING_HEALTH.json`
- Generated: `docs/PROJECT_OPERATING_DASHBOARD.html`
- Generated: compatibility views
- Modify: `.agents/skills/omenward-workflow-router/SKILL.md`

**Interfaces:**
- Consumes: canonical Adapter, project/Base Registries
- Produces: deterministic effective routes와 operating views

- [ ] **Step 1: artifacts 생성**

```bash
python "$BASE_ROOT/tools/build_project_operating_artifacts.py" \
  --project-root . \
  --base-repository "$BASE_ROOT" \
  --write
```

Expected: `Project operating generated artifacts written: N changed`.

- [ ] **Step 2: Router 설명을 v9.3으로 갱신**

Router 본문은 thin router로 유지한다. Base shared Skill 본문을 복사하지 않는다. 설명은 `verified Base v9.3 operating contracts`를 명시한다.

- [ ] **Step 3: Snapshot route 검증**

```bash
python - <<'PY'
import json
s = json.load(open('skills/PROJECT_SKILL_SNAPSHOT.json', encoding='utf-8'))
for route in ['designing-vertical-slices','running-adversarial-review-and-refinement']:
    assert s['effective_routes'][route]['source'] == 'BASE_SHARED'
for route in ['omenward-core-design','omenward-godot','omenward-core-ux','omenward-art-assets']:
    assert s['effective_routes'][route]['source'] == 'PROJECT_LOCAL'
print('route resolution ok')
PY
```

Expected: `route resolution ok`.

- [ ] **Step 4: 생성물 check**

```bash
python "$BASE_ROOT/tools/build_project_operating_artifacts.py" \
  --project-root . \
  --base-repository "$BASE_ROOT" \
  --check
```

Expected: `Project operating generated artifacts are current`.

- [ ] **Step 5: Commit**

```bash
git add skills/PROJECT_SKILL_SNAPSHOT.json docs/PROJECT_OPERATING_HEALTH.json docs/PROJECT_OPERATING_DASHBOARD.html skills/BASE_V9_ADAPTER.json skills/PROJECT_BASE_SKILL_ADAPTER.json skills/PROJECT_PATH_ADAPTER.json .agents/skills/omenward-workflow-router/SKILL.md
git commit -m "chore: regenerate Base v9.3 operating artifacts"
```

존재하지 않는 optional path는 `git add` 목록에서 제외한다.

---

### Task 5: 정본 진입점과 현재 Gate 정렬

**Files:**
- Modify: `AGENTS.md`
- Modify: `docs/BASE_RULES_VERSION.md`
- Modify: `docs/DOCUMENTATION_MAP.md`
- Modify: `docs/ACTIVE_CONTEXT.md`
- Modify: `docs/HANDOFF_CONTEXT.md`
- Modify: `docs/BASE_SHARED_SKILL_INTEGRATION.md`
- Modify: 필요한 README / START_HERE 소비자

**Interfaces:**
- Consumes: Project Core, Vertical Slice v9 Application, Issue #115
- Produces: 동일한 읽기 순서·다음 Gate·미검증 상태

- [ ] **Step 1: 공통 읽기 순서를 다음으로 통일**

```text
최신 사용자 지시
→ AGENTS.md
→ docs/BASE_RULES_VERSION.md
→ docs/DOCUMENTATION_MAP.md
→ docs/operations/VERTICAL_SLICE_V9_APPLICATION.md
→ docs/PROJECT_CORE.md
→ 최신 Vertical Slice 시스템 계약
→ docs/CURRENT_IMPLEMENTATION_STATUS.md
→ docs/ACTIVE_CONTEXT.md
→ docs/HANDOFF_CONTEXT.md
→ 현재 Issue·PR·실제 파일
```

- [ ] **Step 2: Base Rules Version을 v9.3으로 갱신**

release/evidence/hash를 정확히 기록하고 v9.1은 이전 채택 이력으로만 남긴다.

- [ ] **Step 3: Context/Handoff의 stale next work 제거**

활성 문서에서 다음을 제거하거나 legacy 판정한다.

```text
CORE_POC 가설 재선택
3스테이지 최소 Slice
v6 planning intake를 현재 다음 작업으로 표시
```

다음 상태를 공통으로 기록한다.

```text
CURRENT_WORK: BASE_V9_3_OPERATING_MIGRATION
PRODUCT_CODE_AUTHORIZED: NO
FULL_SYSTEM_VERTICAL_SLICE: USER_APPROVED_PLAN
VERTICAL_SLICE_IMPLEMENTATION: NOT_STARTED
NEXT_GATE: COMPLETE_OPERATING_MIGRATION_AND_CLOSE_P1_FINDINGS
```

- [ ] **Step 4: Documentation Map에 신규 산출물 연결**

Application, Audit Packet, Approval Bundle, Plan을 현재 운영 이관 책임 문서로 등록한다.

- [ ] **Step 5: stale term scan**

```bash
git grep -n -E 'Base v9\.1|CORE_POC|3스테이지|foundation\.project-intake|foundation\.validation-review|specialist\.canonical-freshness' -- \
  AGENTS.md README.md docs skills .agents tests .github
```

각 결과를 `CURRENT`, `ALLOWED_LEGACY`, `MUST_FIX`로 판정한다. Archive와 migration traceability의 의도적 기록은 삭제하지 않는다.

- [ ] **Step 6: Commit**

```bash
git add AGENTS.md README.md docs .agents
git commit -m "docs: align Omenward entrypoints with Vertical Slice v9"
```

---

### Task 6: Validator·reference freshness·보호 경로 검증

**Files:**
- Modify only if required: `tests/python/*`
- Modify only if required: `.github/workflows/*`
- Read: all changed operating files

**Interfaces:**
- Consumes: Tasks 2–5 outputs
- Produces: static integrity evidence

- [ ] **Step 1: Base project contract check**

```bash
python "$BASE_ROOT/tools/check_project_operating_contract.py" \
  --project-root . \
  --base-repository "$BASE_ROOT" \
  --check
```

Expected: 성공.

- [ ] **Step 2: 프로젝트 전체 Python tests**

```bash
python tools/check_archive_governance.py
python tools/validate_skill_system.py
python -m unittest discover -s tests/python -v
```

Expected: 모두 성공.

- [ ] **Step 3: 생성물 deterministic check**

```bash
python "$BASE_ROOT/tools/build_project_operating_artifacts.py" \
  --project-root . \
  --base-repository "$BASE_ROOT" \
  --check
git status --short
```

Expected: 생성기 재실행 뒤 새 변경 없음.

- [ ] **Step 4: 보호 경로 diff 검사**

```bash
git diff --name-only 774087dccc903bc9a8e2aec72eec2a2d13b216ce -- \
  data scripts scenes resources assets addons project.godot
```

Expected: 출력 없음. 하나라도 나오면 P0/P1로 중단한다.

- [ ] **Step 5: 문서 링크·route·hash 검사**

- 등록 경로 존재
- Adapter project Registry hash 일치
- Snapshot source Registry hash 일치
- v9.3 Base Registry hash 일치
- Router가 Snapshot만 소비
- Sheet ID 유지

- [ ] **Step 6: 필요한 테스트 수정 Commit**

```bash
git add tests .github tools
git commit -m "test: validate Base v9.3 project operating contract"
```

테스트 수정이 없으면 커밋하지 않는다.

---

### Task 7: 독립 적대적 검토와 PR Gate

**Files:**
- Create: `docs/reviews/2026-07-31-base-v9-3-operating-migration-review.md`
- Update: Issue #115 작업 로그

**Interfaces:**
- Consumes: 전체 diff와 validation logs
- Produces: merge 가능 여부

- [ ] **Step 1: repository-wide attack**

검토 관점:

```text
정본 중복
stale prompt/route
untouched consumer
generated drift
보호 경로 침범
Sheet 권한 혼동
근거 없는 maturity 상승
프로젝트 전용 책임의 Base 침범
Base shared body 복제
```

- [ ] **Step 2: Finding 재검증**

각 Finding을 다음 중 하나로 판정한다.

```text
MUST_FIX
SHOULD_FIX
USER_DECISION_REQUIRED
DEFER
REJECTED_CRITIQUE
BLOCKED_UNVERIFIED
ALLOWED_LEGACY
```

- [ ] **Step 3: P0/P1 최소 수정 후 전체 회귀 재실행**

수정이 있으면 관련 Task의 검증 명령을 다시 실행한다.

- [ ] **Step 4: Review 문서 작성**

필수 내용:

- 기준 branch/commit
- 변경 파일
- 보호 경로 diff
- 실행한 검사와 결과
- 미실행 Runtime/device/accessibility/human
- Sheet 변경 0건
- P0/P1 상태
- rollback
- merge verdict

- [ ] **Step 5: Commit**

```bash
git add docs/reviews/2026-07-31-base-v9-3-operating-migration-review.md
git commit -m "docs: review Base v9.3 operating migration"
```

---

### Task 8: PR·병합 후 동기화 경계

**Files:**
- GitHub PR
- No Sheet write in this Task

**Interfaces:**
- Consumes: verified branch HEAD
- Produces: merged-main follow-up contract

- [ ] **Step 1: PR 설명에 증거 연결**

PR 본문에 다음을 포함한다.

- Closes #115
- Base v9.3 pins/hash
- 신규 감사·Application·Plan
- 변경/제외 범위
- 보호 경로 diff 0
- 테스트 결과
- 미실행 Gate
- Sheet read-only

- [ ] **Step 2: required checks와 review thread 확인**

미해결 P0/P1, 실패 check, unresolved review가 있으면 병합하지 않는다.

- [ ] **Step 3: 병합 후 새 main 재조회**

```bash
git fetch origin
git rev-parse origin/main
```

새 main에서 Adapter/Snapshot/Router/Health를 다시 읽고 정합성을 확인한다.

- [ ] **Step 4: Sheet 후속 작업 분리**

이 PR에서는 Sheet를 쓰지 않는다. 새 main SHA가 확인된 후 별도 동기화 작업에서 정확한 탭과 range를 다시 읽고 다음 최소 범위만 검토한다.

```text
00_프로젝트_허브
01_작업순서
04_누락_충돌_감사
05_GDD_요약
99_변경이력
```

- [ ] **Step 5: 최종 상태**

```text
BASE_V9_3_APPLICATION: CURRENT
OPERATING_MIGRATION: VERIFIED
PRODUCT_BUILD: NOT_AUTHORIZED
VERTICAL_SLICE_IMPLEMENTATION: NOT_STARTED
SHEET_SYNC: FOLLOWUP_REQUIRED
MOBILE: DEFERRED
```

---

## Plan Self-Review

- Spec coverage: Application Binding, six audit outputs, Adapter/Snapshot/Router, canon alignment, Skill routing, validation, adversarial review, merge and Sheet boundary를 모두 Task에 연결했다.
- Placeholder scan: 실행값은 Issue #115, 정확한 SHA, 파일 경로와 명령으로 고정했다.
- Scope check: 제품 구현·Sheet 쓰기·모바일 구현은 명시적으로 제외했다.
- Type/ID consistency: 프로젝트 기계 ID는 `omenward-*`, Base route는 v9.3 Registry의 kebab-case ID를 사용한다.
- Rollback: 기준 main과 생성물 전체 재생성 원칙을 기록했다.
