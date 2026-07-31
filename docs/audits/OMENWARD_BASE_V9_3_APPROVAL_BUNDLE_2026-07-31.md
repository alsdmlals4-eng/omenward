# OMENWARD Base v9.3 Approval Bundle + Change Plan

- 날짜: 2026-07-31
- Issue: `#115`
- 사용자 결정: **Base v9.3과 Vertical Slice v9 실행문을 기준으로 기획·검토 진행**
- 프로젝트: 오멘워드(OMENWARD)
- 주 플랫폼: PC
- 후속 플랫폼: 모바일 검토 예정, 현재 범위 제외
- 기준 main: `774087dccc903bc9a8e2aec72eec2a2d13b216ce`
- 현재 활성 단계: `PLAN / PLANNING_ONLY_PROFILE`
- Codex 실행 권한: `BLOCKED`
- 제품 코드 권한: `NONE`

## 1. 목적

오멘워드의 제품 코어와 프로젝트 전용 Skill을 보존하면서, 현재 Base v9.1 운영 계약을 Base v9.3.0과 Vertical Slice v9 단일 첨부 통합 실행 계약으로 이관하기 위한 **기획·검토·미래 실행 계획**을 정의한다.

현재 작업은 제품 기능 개발이나 운영체계 실제 이관이 아니다. 운영체계·정본 진입점·Skill routing·검증 계보의 변경은 전체 기획·적대적 검토·사용자 최종 승인 뒤 별도 실행 단계에서만 허용한다.

## 2. Work Mode와 실행 프로필

미래 승인 후의 단계 후보:

```text
PLAN
→ BUILD: 운영 문서·Adapter·생성 view·validator만
→ REVIEW: static·freshness·adversarial·PR gate
```

현재 활성 상태:

- 실행 프로필: `PLANNING_ONLY_PROFILE`
- 운영 이관 실행: `NOT_AUTHORIZED`
- 제품 코드 승인: `NO`
- Google Sheet 쓰기: `APPROVED_CANON_SYNC_ONLY`
- 보호 경로 변경: `NO`
- PR 병합: `NO`

## 3. 목표 사용자·플레이어 경험

운영체계 이관 자체가 플레이어 기능을 바꾸지는 않는다. 이관의 목적은 후속 Vertical Slice 기획·Codex 인계·검증에서 다음 플레이어 약속이 구형 문서나 잘못된 route에 의해 변질되지 않도록 하는 것이다.

> 예고된 세 전선의 공세를 읽고, 건물과 TokenSource로 미래 릴 구조를 설계한 뒤, 남은 무작위성을 감수해 결과를 한 전선에 비가역적으로 커밋하고 그 결과를 다음 설계에 사용한다.

## 4. 미래 실행 후보 범위

다음 경로는 현재 수정 권한이 아니라, 최종 승인 뒤 별도 실행 Issue·Plan에서 다시 검증할 후보 범위다.

### 4.1 Base binding

- `docs/BASE_RULES_VERSION.md`
- `skills/PROJECT_BASE_ADAPTER.json`
- `skills/PROJECT_SKILL_SNAPSHOT.json` — 생성물
- `.agents/skills/omenward-workflow-router/SKILL.md`
- `docs/PROJECT_OPERATING_HEALTH.json` — 생성·증거 갱신
- `docs/PROJECT_OPERATING_DASHBOARD.html` — 생성물
- v9 compatibility views — 생성물

### 4.2 정본 진입점

- `AGENTS.md`
- `docs/DOCUMENTATION_MAP.md`
- `docs/ACTIVE_CONTEXT.md`
- `docs/HANDOFF_CONTEXT.md`
- `docs/BASE_SHARED_SKILL_INTEGRATION.md`
- 필요한 README / START_HERE 소비자

### 4.3 Skill routing

- `skills/SKILL_REGISTRY.json`
- 프로젝트 전용 4개 `SKILL.md`
- `skills/SHARED_EXECUTION_CONTRACT.md`
- Skill validator와 Python tests

프로젝트 전용 4개 route는 유지한다.

```text
omenward-core-design
omenward-godot
omenward-core-ux
omenward-art-assets
```

Base v9.3 공용 route는 trigger 기반 최소 집합으로 확장한다. 기존 10개 외에 우선 다음 route를 검토·추가한다.

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

실제 추가는 Base v9.3 Registry에서 `ACTIVE`임을 검증한 ID만 허용한다. 같은 책임이 Omenward local route에 있으면 프로젝트 route를 우선하고 Base 본문을 복제하지 않는다.

## 5. 제외·보호 범위

다음은 현재 기획 PR에서 변경하지 않는다.

```text
scripts/
scenes/
data/
resources/
assets/
addons/
project.godot
skills/ active adapter or generated runtime artifacts
```

추가 제외:

- 게임 Runtime 규칙·밸런스·제품 데이터·자산 구현
- 제품 저장 migration과 Runtime behavior
- 모바일 UI·입력·성능·배포 계약
- 실제 사람·기기·접근성 검증 완료 판정
- 승인되지 않은 가설·수치의 Google Sheet 기록

Google Sheet 쓰기는 `OMW-DEC-20260731-CANON-SYNC-V1`에 따라 사용자 승인된 기획 정본을 같은 Decision ID로 동기화하는 범위에만 허용한다.

`resources/`가 실제 Adapter 보호 정책에 빠져 있다면, 추측 추가하지 않고 tracked 경로와 기존 정책 소스를 확인해 별도 Finding으로 처리한다.

## 6. 미래 실행 원칙

다음 원칙은 최종 실행 승인 뒤에만 적용한다.

1. `skills/PROJECT_BASE_ADAPTER.json`만 프로젝트 통합 권한으로 편집한다.
2. Snapshot·Health·Dashboard·compatibility view는 Base 도구로 생성한다.
3. 생성물을 수동 패치하지 않는다.
4. v9.3 release/evidence pin과 Registry raw SHA-256이 lock과 일치해야 한다.
5. Context와 Handoff는 같은 다음 Gate를 반환해야 한다.
6. CORE_POC와 3스테이지는 활성 권한에서 제거하고 필요한 이력 문서에서만 legacy로 보존한다.
7. Skill ID는 Registry의 `omenward-*`를 정식 기계 ID로 유지하는 방향을 기본값으로 한다.
8. 테스트·Runtime·사람 검증을 실행하지 않았으면 `NOT_RUN`으로 남긴다.
9. 승인 결정 Sheet 동기화와 제품 데이터 Sheet 입력을 구분한다.
10. 승인 정본 동기화는 같은 Decision ID, GitHub authority commit, Sheet 범위, PR merge state를 기록한다.

## 7. 미래 실행 수용 기준

### Static integrity

- [ ] Base v9.3 release/evidence/hash 일치
- [ ] Adapter schema 통과
- [ ] Snapshot deterministic regeneration 통과
- [ ] Router가 유효한 effective route만 선택
- [ ] local/base duplicate ownership 없음
- [ ] orphan path·duplicate ID·alias cycle 없음
- [ ] 생성물 drift 없음
- [ ] 보호 경로 diff 0건

### Canon consistency

- [ ] AGENTS·Documentation Map·Application·Project Core·Context·Handoff 읽기 순서 일치
- [ ] 활성 CORE_POC·3스테이지 stale reference 0건
- [ ] `V2_IMPLEMENTED`, `CORE_LOCK`, `VERTICAL_SLICE_PROVEN` 근거 없는 상승 0건
- [ ] 제품 코드 미승인 상태 유지

### Evidence and review

- [ ] 관련 Python tests 통과
- [ ] Base project operating contract check 통과
- [ ] reference freshness 검사 통과
- [ ] repository-wide adversarial review 완료
- [ ] 미해결 P0/P1 없음
- [ ] GitHub PR checks 통과 또는 실행 불가 근거 명시

### Sheet boundary

- [ ] 승인 정본 동기화 외 제품 데이터 변경 0건
- [ ] Draft PR SHA에는 `SYNCED_TO_PR_HEAD / NOT_MERGED` 사용
- [ ] 병합 후 main SHA 재조회 전 `SYNCED_TO_MAIN` 표기 금지
- [ ] 승인되지 않은 수치·Threat·보상량 기록 0건

## 8. 미래 검증 명령 계약

다음 명령은 현재 실행 지시가 아니다. 별도 사용자 최종 승인과 Codex 실행 Issue가 생성된 뒤 사용하는 미래 검증 계약이다.

Base checkout 경로를 `$BASE_ROOT`, 프로젝트 checkout을 현재 디렉터리로 가정한다.

### Adapter 이관

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

실행 전에 `origin/main`이 정확히 기준 commit을 가리키는지 확인한다. 입력 archive가 기준 commit에 없거나 `/protected_paths` 추출이 실패하면 중단한다.

### 생성물

```bash
python "$BASE_ROOT/tools/build_project_operating_artifacts.py" \
  --project-root . \
  --base-repository "$BASE_ROOT" \
  --write
```

### 검증

```bash
python "$BASE_ROOT/tools/check_project_operating_contract.py" \
  --project-root . \
  --base-repository "$BASE_ROOT" \
  --check

python "$BASE_ROOT/tools/build_project_operating_artifacts.py" \
  --project-root . \
  --base-repository "$BASE_ROOT" \
  --check

python tools/check_archive_governance.py
python tools/validate_skill_system.py
python -m unittest discover -s tests/python -v
```

GitHub PR에서는 workflow가 PR base SHA를 `--protected-base`로 주입하는 기존 계약을 유지한다.

## 9. 롤백

- 기준점: `774087dccc903bc9a8e2aec72eec2a2d13b216ce`
- 생성물 실패 시 일부 파일만 보존하지 않고 Adapter 수정 후 전체 재생성한다.
- 제품 보호 경로가 변경되면 해당 커밋을 되돌리고 운영 문서 변경과 분리한다.
- v9.1 파일은 Git 이력으로 복구할 수 있으며 활성 경로에 중복 정본을 만들지 않는다.

## 10. Codex 실행 게이트

현재 Codex Goal은 발행하지 않는다.

Codex 실행은 다음을 모두 만족한 뒤 별도 Issue·Plan에서만 허용한다.

1. 전체 기획 정본 완성.
2. 최신 독립·적대적 검토 완료.
3. 미해결 P0/P1 없음.
4. 사용자 최종 실행 승인.
5. 실행 대상 경로와 보호 경로 재확인.
6. 승인된 GitHub main·Sheet 상태 동기화.

향후 Codex Goal 문구는 위 게이트를 통과한 별도 실행 문서에서 생성하며, 이 Approval Bundle 자체는 실행 명령이 아니다.

## 11. 현재 상태 표현

Draft PR 상태:

```text
BASE_V9_3_APPLICATION: PLANNING_PROPOSAL
OPERATING_MIGRATION: NOT_STARTED
PRODUCT_BUILD: NOT_AUTHORIZED
CANON_SHEET_SYNC: APPROVED_CANON_ONLY / SYNCED_TO_PR_HEAD
PRODUCT_DATA_SHEET_WRITE: NOT_AUTHORIZED
CODEX_EXECUTION: BLOCKED
PR_MERGE: NOT_AUTHORIZED
```

최종 승인·실행·검증·병합 뒤에만:

```text
BASE_V9_3_APPLICATION: CURRENT
OPERATING_MIGRATION: VERIFIED
PRODUCT_BUILD: SEPARATE_AUTHORIZATION_REQUIRED
CANON_SHEET_SYNC: SYNCED_TO_MAIN
```
