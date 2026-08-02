# 오멘워드 기획 정본 결정 원장

```yaml
updated_at: 2026-08-02
status: CURRENT_DECISION_LEDGER / TOTAL_PLANNING
current_recovery_decision: OMW-DEC-20260802-CANON-RECOVERY-V1
canonical_baseline_main: 9a39f6869f95ec4e6e1f6b96a6a2f896a22c5739
active_base: 9.4.0
working_branch: gpt/omenward-canon-recovery-20260802
recovery_pr: 119
superseded_planning_pr: 116
product_code_authority: NONE
sheet_id: 1VLwRtXGDtyj0JFt98wdIOtG6Zqc3wtdfCzSF9Fo6lpw
sheet_sync: FIRST_READBACK_PASS / FINAL_EXACT_HEAD_WRITEBACK_FOLLOWS_THIS_COMMIT
```

이 문서는 **현재 승인 Decision과 상태**만 소유한다. 제품 정체성과 불변 조건은 `PROJECT_CORE.md`, 실제 구현은 `CURRENT_IMPLEMENTATION_STATUS.md`, 질문별 라우팅은 `DOCUMENTATION_MAP.md`가 소유한다.

## 1. 상태 용어

```text
USER_APPROVED_PLAN
!= PRODUCT_IMPLEMENTED
!= AUTOMATED_VALIDATED
!= HUMAN_VALIDATED
!= RELEASE_READY

RECOMMENDED_DEFAULT
!= USER_APPROVED_VALUE
!= IMPLEMENTED_VALUE
!= VALIDATED_VALUE
```

## 2. 현재 승인 Decision

| Decision ID | 상태 | 현재 결정 | 권위·계보 | 구현·검증 |
|---|---|---|---|---|
| `OMW-DEC-20260802-CANON-RECOVERY-V1` | `USER_APPROVED / CURRENT` | Base v9.4와 현재 main에서 깨끗한 정본 복구 PR을 만들고 PR #116은 역사 증거로 대체 | `docs/audits/OMENWARD_CANON_RECOVERY_AND_TOTAL_PLANNING_RESTART_2026-08-02.md`, PR #119 | 문서·Sheet만, 첫 read-back PASS, 제품 변경 없음 |
| `OMW-DEC-20260731-CONTENT-MANIFEST-V1` | `INHERITED_USER_APPROVED_PLAN` | 전장 1개·4막·Stage 20·일반 공세 8·위험 패키지 4·보스 패키지 3·미션 카드 12 | PR #116 승인 계보 | 미구현·미검증 |
| `OMW-DEC-20260731-DEFEAT-RETRY-V1` | `INHERITED_CURRENT_PRINCIPLE / EXACT_VALUES_PENDING` | Stage 5 이후 MapRun당 최대 1회 paid Retry와 동일 RNG lineage checkpoint 복원 | PR #116 승인 계보 | 미구현·fault test 미실행 |
| `OMW-DEC-20260731-DANGER-BOSS-V1` | `INHERITED_USER_APPROVED_PLAN` | 위험 Stage 5/10/15/20의 차별화된 공개 위협 패키지 | PR #116 승인 계보 | exact values·runtime 미실행 |
| `OMW-DEC-20260801-PROJECT-INTEGRITY-GATE-V1` | `INHERITED_CURRENT_CANON` | 건설 노드 1종, 본진 6/진영, 중간 거점 6곳×3, 접전지 0, 총 30 | PR #116 승인 계보 | 최신 제품 미구현 |
| `OMW-DEC-20260801-BELU-IDENTITY-V1` | `INHERITED_CURRENT_CANON` | 정본명 벨루, 율비는 역사 별칭; 벨루는 선택 근거를 설명하되 자동 결정하지 않음 | PR #116 승인 계보 | 제품 UI·대사 미구현 |
| `OMW-DEC-20260801-VISUAL-SCREEN-BOARD-V2` | `INHERITED_TEXT_SPEC / IMAGE_NOT_APPROVED` | 8개 독립 제품 화면과 정보 위계 방향 | PR #116 승인 계보 | 이미지·엔진 UI 미검증 |
| `OMW-DEC-20260801-ECONOMY-RETRY-SAVE-PLANNING-V1` | `INHERITED_STRUCTURE_CURRENT / VALUES_PENDING` | MapRun/Profile 경제 분리, Retry·checkpoint·Journal·Backup 구조 | PR #116 승인 계보 | simulator·schema·fault test 미실행 |
| `OMW-DEC-20260801-LATEST-CONTRACT-RED-TEST-V1` | `INHERITED_SPEC_WRITTEN_NOT_EXECUTED` | 최신 3릴·30노드·5건물·fixed capture·paid Retry의 Red test 책임 정의 | PR #116 승인 계보 | 실제 test files 없음 |
| `OMW-DEC-20260731-CANON-SYNC-V1` | `INHERITED_OPERATING_RULE` | 주요 승인 Decision은 GitHub와 Sheet에 같은 ID·commit으로 즉시 동기화 | PR #116 승인 계보 | 이번 복구에서 재적용 |

## 3. 보호된 제품 기획

### 플레이어 약속

> 공개된 세 전선의 위험을 읽고 건물과 TokenSource로 세 물리 릴의 미래 배열을 설계·영구 편집한 뒤, 얻은 병력을 한 전선에 비가역 커밋하고 결과 원인을 다음 설계에 반영한다.

### 승인된 구조

- PC-primary.
- 20 Stage, 4막, 약 35분 목표.
- 위험 Stage 5/10/15/20.
- 세 물리 릴, TokenInstance, cursor, 3×3 view.
- immutable SpinSnapshot과 명시적 한 번 확정.
- 보관·판매·한 라인 배치, 배치 뒤 변경 불가.
- 상·중·하 3라인과 고정시간 점령.
- 30개 건설 노드.
- 금고·농장·타워·병영·지휘소.
- 벨루 안내자.

## 4. 현재 실제 구현 경계

```text
CURRENT_PRODUCT = LEGACY_PROTOTYPE

- independent weighted 9-cell roulette
- SPIN_COST=20 legacy value
- barracks/tower/farm only
- legacy outpost node IDs
- capture_power aggregation
- free same-stage restart
- Label/code-drawn graybox UI

LATEST_APPROVED_PRODUCT = NOT_IMPLEMENTED
```

제품 코드가 최신 정본과 다른 것은 migration 대상이라는 뜻이며, 문서만으로 구현 완료를 주장하지 않는다.

## 5. 상세 수치 정책

```text
기획 철학·플레이어 결과 확정
→ 제약식·상대 관계 확정
→ RECOMMENDED_DEFAULT 후보 작성
→ H0/H1/H2 동일 seed simulation
→ 꼬리 위험·지배 전략·softlock 검토
→ 사람 플레이 후보 축소
→ 사용자 승인
→ 구현값·검증값 분리 기록
```

과거 코드와 문서의 `20 gold spin`, `160 starting gold`, `70/50/40 refund` 등은 `LEGACY_H0 / HISTORICAL_ONLY`이며 현재 제품값이 아니다.

## 6. 현재 Finding 분류

### AUTO_FIX_ELIGIBLE

- Base v9.4·main 기준선 동기화: PR #119에 반영.
- PR #116 대체 관계: final Sheet sync 뒤 close.
- Active Context·Handoff·Documentation Map·Workbook: PR #119에 반영.
- Sheet PR HEAD·Base SHA·authority 의미: 첫 read-back PASS.
- `03`, `40`, `90`의 검증된 열·schema 오류: 첫 read-back PASS.
- 수치 상태 레이블: current policy로 반영.

### USER_DECISION_REQUIRED

| 순서 | Decision ID | 질문 | 상태 |
|---|---|---|---|
| 1 | `OMW-DEC-20260802-META-PROGRESSION-ROLE-V1` | Profile 영구 성장의 역할 | `READY_AFTER_FINAL_SYNC` |
| 2 | `OMW-DEC-20260802-WORLD-RUN-MOTIVATION-V1` | 20 Stage 반복과 세계·플레이어 동기의 연결 | `QUEUED` |
| 3 | `OMW-DEC-20260802-VS-CONTENT-BREADTH-V1` | 10병종·20전문화의 데모 대표 범위 | `QUEUED` |

### RESEARCH_OR_TEST_REQUIRED

- 룰렛 통제감 사람 검증.
- 100K economy/retry/save simulation.
- save/retry fault injection.
- 일반/위험 Stage 인지 부하.
- 35분 런 피로도.
- 1080p·720p 가독성·접근성.

## 7. Sheet 첫 read-back

```text
DECISION_ID_MATCH: PASS
BASE_V9_4_CURRENT: PASS
PR_116_HISTORICAL_BOUNDARY: PASS
APPROVAL_IMPLEMENTATION_VALIDATION_AXES: PASS
03_EVIDENCE_ALIGNMENT: PASS
40_SYSTEM_ID_ALIGNMENT: PASS
90_MILESTONE_SCHEMA_ALIGNMENT: PASS
60_UX_SCHEMA_CRITIQUE: REJECTED / NO_ERROR_FOUND
FIRST_BOUNDED_READBACK: PASS
```

이 파일을 갱신한 최종 PR HEAD를 Sheet에 다시 기록하고 재조회한 뒤 `SYNCED`로 닫는다.

## 8. 현재 다음 Gate

```text
FINAL_EXACT_HEAD_SHEET_WRITEBACK_AND_READBACK
→ CLOSE_PR_116_AS_SUPERSEDED
→ FIRST_GRILL_ME_META_PROGRESSION_ROLE
→ APPROVED_DECISION_IMMEDIATE_SYNC
→ NEXT_VALIDATED_PLANNING_CONFLICT
```

```text
PRODUCT_CODE: NOT_AUTHORIZED
CODEX: BLOCKED
SIMULATION: NOT_RUN
RUNTIME: NOT_RUN
HUMAN_QA: NOT_RUN
MOBILE: FUTURE_CONSIDERATION_ONLY
```
