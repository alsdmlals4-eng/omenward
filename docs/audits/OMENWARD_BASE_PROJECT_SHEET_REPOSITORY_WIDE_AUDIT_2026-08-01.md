# 오멘워드 Base·프로젝트·Google Sheet 전수 감사

- 결정 ID: `OMW-DEC-20260801-BASE-PROJECT-SHEET-AUDIT-V1`
- 작성일: `2026-08-01`
- Work Mode: `PLAN → REVIEW → BUILD(DOCS/CANON ONLY) → REVIEW`
- 상태: `CURRENT_REPOSITORY_WIDE_AUDIT / RECOMMENDED_DECISIONS_APPROVED`
- 제품 코드: `UNCHANGED / NOT_AUTHORIZED`
- Codex: `NOT_RUN / BLOCKED`
- PR 병합: `NOT_AUTHORIZED`
- Runtime·사람 검증: `NOT_RUN`

이 문서는 Base 현행 운영 구조, Omenward GitHub 실제 상태, 연결 Google Sheet 25개 탭과 PR 검증 상태를 하나의 기준선에서 대조한 감사 원본이다. 승인된 권장안은 이 Decision ID로 정본·Sheet에 동기화한다.

## 1. 감사 범위

### Base

- `START_HERE.md`
- `AGENTS.md`
- `docs/OPERATING_MODEL.md`
- `docs/WORK_MODE_AND_SKILL_ROUTING.md`
- `docs/DOCUMENTATION_MAP.md`
- `docs/BASE_RULES_VERSION.md`
- `base-v9.3.lock.json`
- `skills/SKILL_REGISTRY.json`
- `docs/generated/BASE_ACTIVE_SKILLS.md`
- 프로젝트 Adapter·승인 결정·Sheet·기획 순서 정책
- 현재 작업에 trigger가 일치하는 운영·적대적 검토 Skill

### Omenward GitHub

- PR `#116`, 변경 파일, 검토, review thread, workflow run
- `AGENTS.md`, `PROJECT_CORE`, `DOCUMENTATION_MAP`, `DECISIONS_PENDING`
- `ACTIVE_CONTEXT`, `HANDOFF_CONTEXT`, `CURRENT_IMPLEMENTATION_STATUS`
- Base Adapter·프로젝트 Skill Registry
- 실제 `project.godot`, Main Scene, StageRun, Roulette, Building, Battle, HUD
- Headless·Python 테스트 구조와 CI validator
- Base v9.3 Application·Approval Bundle·구형 실행 계획

### Google Sheet

Spreadsheet ID: `1VLwRtXGDtyj0JFt98wdIOtG6Zqc3wtdfCzSF9Fo6lpw`

- 25개 탭 metadata와 실제 셀
- 현재 결정·감사·GDD·시스템·경제·UX·아트·이미지·플레이테스트·로드맵·변경이력
- GitHub Decision ID·Commit·상태와의 의미 일치

## 2. Base 현행 구조 분석

### 2.1 권위 계층

```text
최신 사용자 지시
→ 프로젝트 AGENTS·보안·엔진·데이터 규칙
→ 프로젝트 승인 결정·분야 정본·실제 파일
→ 프로젝트에 고정된 Base Adapter
→ Base 원격 운영 계약
→ 외부 사례·과거 대화·추정
```

`Base를 전부 살핀다`는 전체 파일·전체 Skill을 무차별 로드한다는 뜻이 아니다. `START_HERE → OPERATING_MODEL → WORK_MODE_AND_SKILL_ROUTING → DOCUMENTATION_MAP → SKILL_REGISTRY`로 현재 요청에 필요한 책임 원본과 소비자를 선별한다.

### 2.2 Work Mode·Skill 구조

- Work Mode는 `PLAN / BUILD / REVIEW` 중 한 시점에 하나가 주 상태다.
- Skill은 trigger·입력·출력·실패·검증 경계를 가진 책임 계약이다.
- Skill Mode는 Skill 내부 절차다.
- Registry는 `automatic-trigger-match`, `load_all_skills=false`, 주 책임 분야 최대 1개를 강제한다.
- L1 이상은 실행 이유·수행 내용·증거·미검증을 보고한다.

현재 요청에 실제 적용한 최소 Skill 책임:

| 책임 | Skill·Mode |
|---|---|
| 요청·범위·순서 | `managing-project-intake-and-work-contract`: route, contract, decompose-and-sequence, execution-report |
| 기존 프로젝트 운영 감사 | `managing-game-project-operating-system`: audit, verify |
| 저장소 전체 공격 검토 | `running-adversarial-review-and-refinement`: repository-wide-audit, attack, validate-critique, decision-report |
| 정본·Sheet 즉시 동기화 | `managing-design-documents`: update, canonical-integration |
| 변경 전파 확인 | `auditing-canonical-reference-freshness`: reference-freshness |
| 실제 변경 증거 | `reviewing-and-validating-project-changes`: contract-check, static-validation, evidence-report |

### 2.3 Base release와 프로젝트 채택 분리

Base v9.3 자체는 released lock을 보유한다.

```text
version: 9.3.0
release: 30ca6c7b5f93521f0eb0eed42d01437cd43c50ae
evidence: 462a86db192d23d0f386281a1eb54b0a8cbad62e
registry_sha256: 9847bb2b225c776ad7916930f0f48c490bc2a898bea8e02ea1fdd0e6caac60c1
```

그러나 Omenward의 활성 Adapter는 Base v9.1이다.

```text
active_version: 9.1.0
release: 3c158f52cfdad889970aef4d6ce6650a6fea0645
evidence: dd20ad3852e264d7e337e34d2cb963f71053a6cb
```

**결정:** Base v9.3은 다음 운영 마이그레이션 목표로 유지하되, 현재 문서 PR에서 Adapter·Snapshot·Router·validator를 부분 수정하지 않는다. 별도 원자 마이그레이션 패키지에서 release/evidence pin, Registry hash, protected baseline, routes, generated views, validators를 함께 검증한다.

## 3. 프로젝트 실제 진행 상태

### 3.1 승인된 제품 구조

- PC 우선, 16:9.
- 35분 표준 MapRun, 20 Stage, 4막.
- 하나의 전장과 `top/middle/bottom` 3라인.
- 건설 노드 한 종류.
- 본진 6노드/진영, 중간 거점 6곳×3노드, 접전지 3곳×0노드, 전체 30노드.
- 왼쪽·중앙·오른쪽 세 물리 릴, TokenInstance, cursor, 3×3 노출 보드.
- 건물 TokenSource가 동일 출처 토큰을 세 릴에 하나씩 공급.
- 세로 cursor 이동과 영구 가로 TokenInstance 교환.
- immutable SpinSnapshot·명시적 확정·PendingReward.
- 보관·판매·한 라인 비가역 배치.
- 고정시간 점령.
- 금고·농장·타워·병영·지휘소 5개 건물 가족.
- Stage 5 이후 MapRun당 최대 1회 제품 유료 재시도.
- 안내자 정본명 `벨루 / Belu`; `율비`는 역사 별칭.

### 3.2 실제 Legacy 구현

실제 Godot 파일은 다음을 구현한다.

- Main Scene이 `Battlefield + StageHud + StageSelect`를 직접 조립.
- 3라인·양 진영 outpost·clash·gate·base simulation seam.
- 독립 가중치로 9칸 board를 생성하는 Legacy Roulette.
- 중앙줄 판정·8개 완성선·금화·등급 resolver.
- 병영·타워·농장 3건물.
- `front_a/front_b/rear` 3노드/outpost.
- `capture_power` 합산 점령.
- pending reward와 한 라인 배치 seam.
- 패배 후 동일 Stage 무료 restart.
- Label 중심 기술 HUD와 원인 보고 seam.

```text
LEGACY_PROVEN
!= LATEST_VERTICAL_SLICE_IMPLEMENTED
!= LATEST_VERTICAL_SLICE_PROVEN
```

### 3.3 최신 테스트 상태

- 최신 Red 테스트 **명세와 Legacy 판정표는 작성됨**.
- `tests/headless/latest/**`, `tests/python/latest/**`는 미작성.
- expected Red 실행 증거 없음.
- 제품 코드 구현 없음.
- Runtime·접근성·성능·사람 QA 미실행.

## 4. Google Sheet 25개 탭 감사

### 4.1 양호한 범위

- `02_현재_확정결정`은 역사 결정과 현재 결정을 대부분 분리한다.
- `04_누락_충돌_감사`는 이미지 실패·전장 토폴로지·Legacy 경계를 보존한다.
- `60/70/71/72`는 폐기 이미지와 벨루의 현재 방향을 비교적 정확히 기록한다.
- `80`은 실제 테스트가 대부분 `NOT_RUN`임을 숨기지 않는다.
- `99`는 Decision ID와 PR head 동기화 이력을 보존한다.

### 4.2 정정이 필요한 의미 drift

| ID | Finding | 판정 |
|---|---|---|
| `AUD-SHEET-001` | `00`의 `Base SHA` 칸에 프로젝트 권위 commit이 기록됨 | `SCHEMA_SEMANTIC_CONFLICT` |
| `AUD-SHEET-002` | `01`에 이미 병합된 Sheet 설치가 GitHub 반영 대기로 남음 | `STALE_STATUS` |
| `AUD-SHEET-003` | `05`가 PR #92/#97 exact refund와 구형 단계 정보를 CURRENT처럼 요약 | `HISTORICAL_CURRENT_DRIFT` |
| `AUD-SHEET-004` | `10`이 16:9와 해상도를 후보로 표기 | `STALE_CONFIRMED_BASELINE` |
| `AUD-SHEET-005` | `12/15`의 `수정·리셋` 문구가 릴 이동 undo까지 허용하는 것처럼 읽힘 | `AMBIGUOUS_IRREVERSIBILITY` |
| `AUD-SHEET-006` | `14/40/41/50`이 역사 PR #92/#97을 현재 exact 수치 권위로 표시 | `AUTHORITY_ROUTING_DRIFT` |
| `AUD-SHEET-007` | 여러 분야 탭이 승인·구현·검증 상태를 한 단어 `APPROVED`에 혼합 | `STATUS_AXIS_COLLAPSE` |

### 4.3 정정 원칙

- `Base SHA`는 활성 Omenward Base release pin만 기록한다.
- 프로젝트 권위 commit과 현재 PR head는 별도 필드로 분리한다.
- PR #92/#97과 F-30 exact 값은 삭제하지 않고 `HISTORICAL_APPROVED_SOURCE / LATEST_OVERRIDES_APPLY`로 보존한다.
- 최신 책임 원본·Decision ID가 있는 분야는 bare `PR #97`, `Slice 정본` 대신 현재 경로를 연결한다.
- 구조 승인, 구현 상태, 검증 상태를 분리한다.
- `수정 가능`은 배치 대상 선택·확정 전 review를 뜻하며, 이동권 소비 뒤 릴 편집 undo/reset을 뜻하지 않는다.

## 5. 적대적 검토 Finding

### P1 — Active Context·Handoff가 현재 상태를 복원하지 못함

증거:

- 2026-07-27 갱신 상태.
- `V6_PLANNING_INTAKE`, `3스테이지`, `CORE_POC`, Issue #69를 다음 작업으로 표시.
- 20 Stage·30노드·5건물·벨루·유료 Retry·최신 Red 명세를 복원하지 못함.

영향:

- 새 작업자가 구형 기획을 현재 목표로 오인.
- validator와 사람 작업 모두 stale entrypoint를 소비.

권장 조치: 현재 감사와 Decision Ledger를 압축한 Active Context·Handoff로 교체.

### P1 — PR #116 필수 검증 실패

현재 head에서 확인한 workflow:

```text
Validate Base v9 adoption: SUCCESS
Validate Project Core Documentation: FAILURE
Validate Omenward GDD Sheet Adoption: FAILURE
```

세부:

- Project Core workflow는 `validate_project_core_docs.py` 단계에서 실패.
- GDD workflow는 `test_bca_visual_sheet_adoption.py`에서 실패.
- GDD test는 오래된 Base SHA와 C1 증거 문자열을 직접 고정한다.

영향:

- PR을 ready/merge 가능한 상태로 승격할 수 없음.
- 현재 문서와 validator가 서로 다른 시대의 계약을 주장.

권장 조치: 이번 감사에서는 실패를 명시하고 merge를 차단한다. validator 갱신은 별도 non-product verification package에서 최신 정본·Legacy 보존을 함께 검사하도록 교체한다.

### P1 — Base v9.3 실행 계획의 권한 오독 위험

과거 계획은 agentic execution header와 Adapter·validator 수정 명령을 포함한다. Approval Bundle은 이를 미래 실행 후보로 제한하지만, 계획 단독 소비 시 실행 가능한 작업지시로 오인될 수 있다.

권장 조치:

- 기존 계획은 `HISTORICAL_EXECUTION_CANDIDATE / DO_NOT_EXECUTE_CURRENTLY`로 라우팅.
- 현재 권위는 이 감사, Application Contract, Approval Bundle, 제품 코드 차단 Gate가 소유.
- 실제 v9.3 Adapter 이관은 별도 Issue·Branch·검증 패키지로 재작성.

### P1 — Sheet 상태 의미 혼합

`Base SHA`, PR authority commit, Sheet sync가 한 행에 혼합돼 Base 채택 상태와 기획 동기화 상태를 구분하기 어렵다.

권장 조치: 활성 Base pin, 권위 commit, PR head, Sheet sync를 각각 독립 필드로 유지.

### P2 — 분야 책임 경로가 과거 PR 별칭에 의존

삭제할 문제는 아니지만, 화면 V2·수치 계약·Codex 인계에서 과거 PR 번호가 현재 권위처럼 소비될 수 있다.

권장 조치: 분야 탭과 Documentation Map에 최신 책임 원본 경로를 우선하고 과거 PR은 lineage로 유지.

### P2 — 정확 수치·save schema·경제 시뮬레이션 미확정

구조는 승인됐으나 다음은 pending이다.

- 회전·이동·건설·업그레이드·수리·철거 실제 수치.
- 영구재화 명칭·획득·Retry 비용.
- save/checkpoint schema와 transaction journal.
- 100,000 seed 경제·룰렛·미션 분포.
- 병종·건물·위험 Stage exact values.

임의 숫자로 닫지 않는다.

## 6. 승인된 권장 결정

사용자의 `권장안 일괄 승인` 지시에 따라 다음을 확정한다.

### 6.1 Base 채택

```text
CURRENT_PROJECT_BASE: v9.1
NEXT_RECOMMENDED_BASE: v9.3
V9_3_ADAPTER_MIGRATION: SEPARATE_ATOMIC_PACKAGE_REQUIRED
CURRENT_PR_PARTIAL_ADAPTER_EDIT: FORBIDDEN
```

### 6.2 PR #116

```text
PR_STATE: DRAFT / OPEN / NOT_MERGED
PURPOSE: PLANNING_CANON_AND_AUDIT
PRODUCT_CODE: UNCHANGED
READY_FOR_REVIEW: NO
MERGE: BLOCKED_BY_FAILED_CHECKS_AND_P1
```

### 6.3 과거 건물 수치

```text
PR92_EXACT_REFUNDS: HISTORICAL_APPROVED_SOURCE
F30_ORDER: LEGACY_PROVEN_TECHNICAL_CONTRACT
LATEST_BUILDING_EXACT_VALUES: PENDING
```

과거 값을 삭제하지 않으며 최신 수치의 자동 승계도 하지 않는다.

### 6.4 화면·이미지

- 기존 Screen Board V1과 OM-IMG-005~010은 폐기 증거.
- 다음 산출물은 이미지가 아니라 **화면별 독립 브리프와 Screen Board V2 텍스트 명세**다.
- 기본 전투·Stage 준비·정산 화면의 구조가 먼저 승인된 뒤 파생 위험·Retry 화면을 작성한다.

### 6.5 다음 작업 순서

```text
1. Active Context·Handoff·Sheet 의미 drift 정정
2. PR body·Decision Ledger·Documentation Map 동기화
3. Screen Board V2 독립 화면 브리프·텍스트 명세
4. 경제·Retry 비용·save/checkpoint Approval Bundle과 시뮬레이션 계약
5. 실제 최신 Red test Work Order·expected-failure package
6. 별도 Base v9.3 Adapter 원자 마이그레이션 package
7. 사용자 승인 Codex 제품 구현 Plan
8. Codex Build → 자동·Runtime·사람 검증
```

Screen Board V2와 Red test package는 병렬 구현하지 않는다. 화면 명세는 최신 계약을 읽는 시각 소비자이고, Red package는 구현 전 실패 계약이므로 둘 다 현재 감사·정본 정정 완료 뒤 진행한다.

## 7. 완료·미완료 경계

```text
BASE_STRUCTURE_ANALYSIS: COMPLETE
PROJECT_GITHUB_AUDIT: COMPLETE
GOOGLE_SHEET_25_TAB_AUDIT: COMPLETE
ADVERSARIAL_REVIEW: COMPLETE
RECOMMENDED_DECISIONS: APPROVED
CANON_PROPAGATION: IN_PROGRESS_UNTIL_READBACK
SHEET_PROPAGATION: IN_PROGRESS_UNTIL_READBACK
LATEST_RED_SPEC: WRITTEN_NOT_EXECUTED
LATEST_IMPLEMENTATION: NOT_STARTED
CI: PARTIAL_FAILURE
RUNTIME: NOT_RUN
HUMAN_QA: NOT_RUN
CODEX: BLOCKED
MERGE: BLOCKED
```

## 8. 검증 기준

이 결정은 다음을 재조회해 닫는다.

- Decision ID와 감사 문서 경로.
- Active Context·Handoff의 현재 단계·다음 순서.
- Documentation Map·Decision Ledger·Pending.
- Sheet `00/01/02/04/05/10/12/15/40/41/50/99`.
- PR body·head·Draft·merge state.
- workflow conclusion은 수정하지 않았으므로 실패 상태 그대로 기록.

`CANON_PROPAGATION_COMPLETE`는 문서·Sheet read-back이 일치할 때만 사용한다.