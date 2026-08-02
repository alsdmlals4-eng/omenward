# OMENWARD 기획 정본 복구·총기획 재개 감사

```yaml
decision_id: OMW-DEC-20260802-CANON-RECOVERY-V1
approval: USER_APPROVED_2026-08-02_10:53_KST
status: CANON_RECOVERY_CURRENT / TOTAL_PLANNING_RESTART / SHEET_SYNC_PENDING
work_mode: TOTAL_PLANNING
current_phase: REVIEW_THEN_PLAN
base_repository: alsdmlals4-eng/Base
base_authority: v9.4.0_RELEASED
base_main_unreleased: OBSERVED_NOT_ADOPTED
project_repository: alsdmlals4-eng/omenward
baseline_main_commit: 9a39f6869f95ec4e6e1f6b96a6a2f896a22c5739
working_branch: gpt/omenward-canon-recovery-20260802
superseded_pr: 116
product_code_authority: NONE
planning_and_documentation_authority: APPROVED
primary_platform: PC
future_platform: MOBILE_CONSIDERATION_ONLY
runtime_validation: NOT_RUN
human_validation: NOT_RUN
simulation: NOT_RUN
```

## 1. 목적

현재 `main`의 Base v9.4 운영 계약을 기준으로 OMENWARD의 승인된 기획을 복구한다. PR #116의 유효한 사용자 승인 결정은 보존하되, Base v9.1→v9.3 이관 전제, 오래된 PR HEAD, stale validator, Sheet 상태 혼합은 현행 권위로 가져오지 않는다.

이 작업 뒤 총기획은 다음 규칙으로 진행한다.

```text
프로젝트 전체 감사
→ 보호 강점 고정
→ 충돌·누락·과설계·미검증 가정 공격
→ 비판의 사실성과 영향 재검증
→ 안전한 기획 오류·누락 자동 보완
→ 중요한 기획 선택만 Grill Me
→ 승인 즉시 GitHub·Sheet 같은 Decision ID 동기화
→ 다음 기획 질문
```

상세 데이터 수치는 AI 권장안을 초기 시험값으로 제시할 수 있지만 다음 상태를 분리한다.

```text
RECOMMENDED_DEFAULT
TEST_VALUE
SIMULATION_CANDIDATE
USER_APPROVED_VALUE
IMPLEMENTED_VALUE
VALIDATED_VALUE
```

## 2. Baseline Recovery Record

| 항목 | 복구 결과 |
|---|---|
| Base released authority | v9.4.0 |
| Base unreleased main | v9.5 maintenance candidate, 미채택 |
| Project main | `9a39f6869f95ec4e6e1f6b96a6a2f896a22c5739` |
| Current product | Legacy prototype |
| Latest planning | PR #116의 승인 결정 계보, main 미병합 |
| Actual roulette | 독립 가중치 9칸, `SPIN_COST=20` |
| Actual buildings | 병영·타워·농장 3종, 즉시 건설 |
| Actual retry | 무료 동일 Stage 재시작 |
| Actual battlefield | Legacy 3라인·outpost·capture_power 기반 |
| Latest planned product | 세 물리 릴·30노드·5건물·고정시간 점령·paid Retry |
| Runtime/human proof | 최신 제품 기준 없음 |
| Connected Sheet | 25개 탭, PR #116의 과거 HEAD와 Base v9.1 기록 포함 |
| Protected paths | `scripts/`, `scenes/`, `data/`, `resources/`, `assets/`, `addons/`, `project.godot` |
| Rollback | Draft PR 폐기와 Sheet revision 복원 |

## 3. 보호할 승인 강점

### 프로젝트 정체성

> 예고된 세 전선의 공세를 읽고, 건물과 영구 이동으로 세 물리 릴의 미래 구조를 설계한 뒤, 당첨 병력을 한 전선에 비가역 커밋해 전황을 뒤집는다.

### 보호 불변 조건

- PC 주 플랫폼.
- 상·중·하 세 라인.
- 세 물리 원형 릴과 `TokenInstance`.
- 건물과 TokenSource가 future reel structure에 관찰 가능한 영향을 줌.
- 가로 이동은 실행 즉시 영구 반영되고 undo가 없음.
- 보상은 immutable `SpinSnapshot`과 명시적 확정 거래를 사용.
- 배치 후 라인 변경·회수·판매 없음.
- 본진 6노드/진영, 중간 거점 6곳×3노드, 접전지 0노드, 전체 30노드.
- 금고·농장·타워·병영·지휘소 5건물.
- 20 Stage·4막·위험 Stage 5/10/15/20·목표 런타임 약 35분.
- Stage 5 이후 MapRun당 최대 1회 paid Retry 원칙.
- 안내자 정본명 `벨루 / Belu`; 플레이어 결정을 대신하지 않음.
- 승인 문서와 실제 구현·검증 상태를 분리.

## 4. PR #116 승계 판정

PR #116은 126개 commit과 52개 파일이 누적된 Base v9.3 기획 PR이며 현재 main보다 뒤처지고 병합 불가 상태였다. 따라서 PR 자체는 병합 단위로 사용하지 않는다.

### 승계

- 20 Stage·4막·35분 피로도 원칙.
- 콘텐츠 Manifest와 미션 카드 구조.
- 위험 Stage·보스 패키지 방향.
- 패배·paid Retry 원칙.
- 전장 6/3/0=30 불변 조건.
- 벨루 정체성.
- Screen Board V2 텍스트 구조.
- 경제·Retry·save/checkpoint 구조와 Parameter Registry 경계.
- 최신 계약 Red test 책임과 Legacy 테스트 분류.
- 즉시 Decision sync 원칙.

### 승계하지 않음

- Base v9.1이 현재라는 상태.
- Base v9.3이 다음 필수 migration이라는 상태.
- PR #116의 오래된 HEAD를 Sheet current head로 사용하는 상태.
- 실패한 stale validator의 구형 문자열 요구.
- PR #116 병합을 전제로 한 실행 순서.
- 미실행 simulator·Red test·runtime·human QA를 완료로 보는 표현.

## 5. 적대적 검토 Finding Ledger

| ID | 유형 | 검증된 문제 | 영향 | 분류 | 판정 |
|---|---|---|---|---|---|
| OMW-F-001 | STALE_REFERENCE | Sheet·PR #116은 Base v9.1→v9.3을 현행으로 기록하지만 main은 v9.4 | 모든 후속 작업의 잘못된 기준선 | AUTO_FIX_ELIGIBLE | MUST_FIX |
| OMW-F-002 | DUPLICATE_ACTIVE_SOURCE | main 정본과 PR #116 정본이 서로 다른 다음 작업·상태를 주장 | 콜드 스타트 실패·중복 기획 | AUTO_FIX_ELIGIBLE | MUST_FIX |
| OMW-F-003 | MISSING_SYNC | Sheet current PR HEAD가 실제 #116 HEAD보다 오래됨 | `SYNCED_TO_PR_HEAD` 허위 상태 | AUTO_FIX_ELIGIBLE | MUST_FIX |
| OMW-F-004 | PRODUCTION_RISK | 20 Stage·모든 시스템·UI·아트·오디오·저장·메타를 첫 완성형 데모에 포함 | 제작량과 검증량 폭증 | RESEARCH_OR_TEST_REQUIRED | TEST_IN_VERTICAL_SLICE |
| OMW-F-005 | UNPROVEN_ASSUMPTION | 룰렛 구조 설계가 실제 통제감·재미·실패 귀인을 만든다는 가설 | 코어 재미 미검증 | RESEARCH_OR_TEST_REQUIRED | HUMAN_TEST_REQUIRED |
| OMW-F-006 | UNDERDESIGN | 영구 성장의 역할이 정해지지 않았지만 Profile 경제·Retry 통화·시작 보관 해금이 예정됨 | 장기 동기·난이도·공정성 충돌 | USER_DECISION_REQUIRED | GRILL_ME_1 |
| OMW-F-007 | UNDERDESIGN | 월드·세력·플레이어 동기가 20 Stage 반복 구조와 시스템에 충분히 연결되지 않음 | 콘텐츠 정체성과 반복 정당화 약화 | USER_DECISION_REQUIRED | GRILL_ME_QUEUE |
| OMW-F-008 | PLAYER_EXPERIENCE_RISK | 일반 Stage 정지와 위험 Stage 실시간 전환의 정보량·조작 부담 검증 없음 | 위험 Stage에서 과부하 가능 | RESEARCH_OR_TEST_REQUIRED | PROTOTYPE_TEST |
| OMW-F-009 | ACCESSIBILITY_RISK | 정확 공세·릴·건물·3라인 상태를 동시에 읽어야 하나 대체 채널·색각·입력 우선순위가 미확정 | 가독성·접근성 실패 | RESEARCH_OR_TEST_REQUIRED | UX_TEST |
| OMW-F-010 | MISSING_CANON | 상세 수치의 상태 체계가 문서마다 legacy·candidate·pending으로 분산 | 시험값의 제품값 오인 | AUTO_FIX_ELIGIBLE | MUST_FIX |
| OMW-F-011 | CANON_IMPLEMENTATION_GAP | 최신 기획과 실제 Legacy 코드의 차이가 큼 | 구현 계획의 대규모 migration 위험 | AUTO_FIX_ELIGIBLE | DECLARE_ONLY |
| OMW-F-012 | DATA_COMPATIBILITY_RISK | ProfileSave·RunCheckpoint·Journal·Backup 구조는 있으나 실제 schema·migration 범위 미정 | 저장 손상·Retry 중복 위험 | RESEARCH_OR_TEST_REQUIRED | CONTRACT_AND_FAULT_TEST |
| OMW-F-013 | OVERDESIGN | Tier 2 10병종·Tier 3 20전문화의 전체 상세 구현이 코어 검증보다 앞설 수 있음 | 콘텐츠 제작이 코어 학습을 압도 | USER_DECISION_REQUIRED_OR_SLICE_TEST | LATER_GRILL_ME |
| OMW-F-014 | MISSING_CONSUMER | PR #116의 신규 결정이 main의 Active Context·Handoff·Workbook 계약에 반영되지 않음 | 다음 작업자 오도 | AUTO_FIX_ELIGIBLE | MUST_FIX |
| OMW-F-015 | DERIVATIVE_STALE | Screen Board·Visual Index·Sheet 이미지 상태가 실제 승인 자산과 분리 | 잘못된 이미지 재사용 가능 | AUTO_FIX_ELIGIBLE_AND_REVIEW | SHOULD_FIX |

## 6. 적대적 Attack → Validate Critique

### 공격 A — “기획이 많으므로 제품 방향이 충분히 명확하다”

- 사실 근거: 시스템 문서는 풍부하다.
- 반증: 영구 성장, 상세 콘텐츠 제작량, 위험 Stage 조작 부담, 세계·반복 동기는 결정되지 않았다.
- 판정: `REJECTED_CRITIQUE`가 아니라 `VALID_FINDING`; 문서량과 결정 완결성은 다르다.

### 공격 B — “PR #116을 병합하면 모든 정본 문제가 해결된다”

- 사실 근거: 많은 승인 문서가 #116에 있다.
- 반증: Base 전제가 오래됐고, scope drift·merge conflict·stale validator·Sheet head drift가 존재한다.
- 판정: `MUST_FIX`; 깨끗한 current-main recovery가 더 안전하다.

### 공격 C — “20 Stage 완성형 데모는 무조건 과도하므로 축소해야 한다”

- 사실 근거: 제작·검증 범위가 매우 크다.
- 반증: 사용자가 이미 20 Stage와 완성형 데모 방향을 승인했다. 시스템 종류의 완결성과 콘텐츠 양의 최소화로 해결할 여지가 있다.
- 판정: 강제 축소 비판은 `REJECTED_CRITIQUE`; 다만 제작량·대표 콘텐츠 수는 테스트와 후속 결정이 필요하다.

### 공격 D — “상세 수치는 AI가 정하면 기획 질문이 필요 없다”

- 사실 근거: 많은 값은 시뮬레이션으로 후보를 좁힐 수 있다.
- 반증: 수치는 영구 성장의 철학, 실패 비용, 보상 의미 같은 기획 방향에 종속된다.
- 판정: 값 자체는 권장안·시험값으로 처리하되 방향 결정을 AI가 대신하지 않는다.

## 7. 개선 분류

### AUTO_FIX_ELIGIBLE

- Base v9.4·main 기준선 복구.
- PR #116의 대체 관계 기록.
- GitHub·Sheet HEAD·Decision·상태 축 분리.
- Active Context·Handoff·Documentation Map·Workbook 라우팅 갱신.
- 상세 수치 상태 레이블 통일.
- 실제 구현과 최신 기획의 간극 명시.
- Sheet의 검증된 열 밀림·헤더 불일치 수정.

### USER_DECISION_REQUIRED

1. Profile 영구 성장의 역할.
2. 세계·세력·플레이어 동기와 20 Stage 반복의 연결 방식.
3. 10병종·20전문화의 Vertical Slice 대표 콘텐츠 범위.
4. 필요 시 룰렛 설계와 전장 지휘의 우선순위 조정.

### RESEARCH_OR_TEST_REQUIRED

- 100K 경제·Retry·save simulation.
- 룰렛 통제감 사람 검증.
- 일반/위험 Stage 인지 부하 검증.
- 1080p·720p 정보 가독성·접근성.
- save/retry transaction fault injection.
- 실제 35분 런 피로도와 Stage당 결정 수.

## 8. 첫 Grill Me 후보

```yaml
decision_id: OMW-DEC-20260802-META-PROGRESSION-ROLE-V1
finding: OMW-F-006
question: 실패와 완주 뒤 Profile 영구 성장은 어떤 역할을 가져야 하는가?
status: READY_AFTER_CANON_AND_SHEET_SYNC
```

이 질문은 Retry 통화, 시작 보관 용량, 해금, 난이도, 반복 동기와 직접 연결된다. 상세 숫자보다 먼저 결정해야 한다.

## 9. 현재 Gate

```text
CANON_RECOVERY_BRANCH: CREATED
RECOVERY_PLAN: WRITTEN
GITHUB_CANON_UPDATE: IN_PROGRESS
SHEET_SYNC: PENDING
PR_REPLACEMENT: PENDING
PRODUCT_CODE: UNCHANGED
CODEX: BLOCKED
FIRST_GRILL_ME: BLOCKED_UNTIL_SYNC
```
