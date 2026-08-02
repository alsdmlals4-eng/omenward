# OMENWARD 기획 정본 복구·총기획 재개 감사

```yaml
decision_id: OMW-DEC-20260802-CANON-RECOVERY-V1
approval: USER_APPROVED_2026-08-02_10:53_KST
status: CANON_RECOVERY_SYNCED / TOTAL_PLANNING_ACTIVE
work_mode: TOTAL_PLANNING
current_phase: GRILL_ME_DECISION_INTAKE
base_authority: v9.4.0_RELEASED
base_main_unreleased: OBSERVED_NOT_ADOPTED
project_repository: alsdmlals4-eng/omenward
baseline_main_commit: 9a39f6869f95ec4e6e1f6b96a6a2f896a22c5739
working_branch: gpt/omenward-canon-recovery-20260802
replacement_pr: 119
superseded_pr: 116_CLOSED_NOT_MERGED
sheet_sync: SYNCED
ci_validation: PROJECT_CORE_PASS / GDD_SHEET_PASS / BASE_ADOPTION_PASS
product_code_authority: NONE
primary_platform: PC
future_platform: MOBILE_CONSIDERATION_ONLY
runtime_validation: NOT_RUN
human_validation: NOT_RUN
simulation: NOT_RUN
```

## 1. 복구 결론

현재 `main`과 Base v9.4를 기준으로 승인 기획의 진입점·결정 원장·상태 문서·Sheet 계약을 복구했다. PR #116의 사용자 승인 결정은 계보로 보존했지만 Base v9.1→v9.3 전제, 오래된 HEAD, stale validator 상태와 거대 병합 범위는 현행 권위에서 제외했다.

```text
PR #116: CLOSED / NOT_MERGED / HISTORICAL_APPROVAL_EVIDENCE
PR #119: OPEN / DRAFT / CURRENT_RECOVERY_AUTHORITY
PRODUCT CODE: UNCHANGED
```

총기획은 다음 생명주기로 진행한다.

```text
검증된 기획 충돌 선택
→ Grill Me 1문항
→ 사용자 승인
→ GitHub 정본·Decision Ledger·Context 갱신
→ 동일 Decision ID Sheet 갱신
→ Commit·HEAD·Sheet 재조회
→ 다음 기획 충돌
```

## 2. 보호할 승인 강점

> 예고된 세 전선의 공세를 읽고, 건물과 영구 이동으로 세 물리 릴의 미래 구조를 설계한 뒤, 당첨 병력을 한 전선에 비가역 커밋해 전황을 뒤집는다.

- PC 주 플랫폼.
- 상·중·하 세 라인.
- 세 물리 원형 릴과 `TokenInstance`.
- TokenSource가 future reel structure에 관찰 가능한 영향을 줌.
- 가로 이동은 실행 즉시 영구 반영되고 undo가 없음.
- immutable `SpinSnapshot`과 명시적 확정 거래.
- 보관·판매·한 라인 배치, 배치 후 변경·회수·판매 없음.
- 본진 6노드/진영, 중간 거점 6곳×3노드, 접전지 0노드, 전체 30노드.
- 금고·농장·타워·병영·지휘소 5건물.
- 20 Stage·4막·위험 Stage 5/10/15/20·약 35분 목표.
- Stage 5 이후 MapRun당 최대 1회 paid Retry 원칙.
- 안내자 `벨루 / Belu`; 선택을 대신하지 않음.

## 3. 실제 구현 기준선

| 영역 | 현재 실제 구현 | 최신 승인 기획 |
|---|---|---|
| 룰렛 | 독립 가중치 9칸, `SPIN_COST=20` | 세 물리 릴·영구 이동·snapshot transaction |
| 건물 | 병영·타워·농장, 즉시 건설 | 5건물·시간·거래·TokenSource lifecycle |
| 전장 | Legacy outpost·capture_power | 30노드·고정시간 점령 |
| Retry | 무료 동일 Stage 재시작 | paid Retry·checkpoint·동일 RNG lineage |
| UI | Label/code-drawn graybox | Screen Board V2·벨루 runtime |

```text
LEGACY_PROVEN != LATEST_IMPLEMENTED != LATEST_PROVEN
```

## 4. 상세 수치 정책

사용자는 상세 데이터 수치를 GPT 권장안으로 진행하도록 승인했다. 이는 숫자를 무검증 제품값으로 확정한다는 의미가 아니다.

```text
LEGACY_H0 / HISTORICAL_ONLY
→ 기획 의미·제약식
→ RECOMMENDED_DEFAULT / TEST_VALUE
→ H0/H1/H2 simulation candidate
→ 꼬리 위험·지배 전략·softlock 검토
→ 사람 플레이 후보 축소
→ USER_APPROVED_VALUE
→ IMPLEMENTED_VALUE
→ VALIDATED_VALUE
```

## 5. 적대적 검토 Finding Ledger

| ID | 유형 | 검증된 문제 | 분류 | 현재 판정 |
|---|---|---|---|---|
| OMW-F-001 | STALE_REFERENCE | Base v9.1→v9.3 기록과 current v9.4 충돌 | AUTO_FIX | FIXED_SYNCED |
| OMW-F-002 | DUPLICATE_ACTIVE_SOURCE | main과 PR #116이 다른 다음 작업 주장 | AUTO_FIX | FIXED_SYNCED |
| OMW-F-003 | MISSING_SYNC | Sheet PR HEAD·상태 drift | AUTO_FIX | FIXED_READBACK_PASS |
| OMW-F-004 | PRODUCTION_RISK | 20 Stage 완성형 데모 제작·검증량 | TEST_REQUIRED | SCOPE_PRESERVED / TEST_IN_SLICE |
| OMW-F-005 | UNPROVEN_ASSUMPTION | 릴 설계가 실제 통제감·재미를 만든다는 가설 | TEST_REQUIRED | HUMAN_TEST_REQUIRED |
| OMW-F-006 | UNDERDESIGN | Profile 영구 성장 역할 미확정 | USER_DECISION | GRILL_ME_1_READY |
| OMW-F-007 | UNDERDESIGN | 세계·세력·플레이어 동기와 20 Stage 반복 연결 부족 | USER_DECISION | QUEUED |
| OMW-F-008 | PLAYER_EXPERIENCE_RISK | 일반 정지/위험 실시간 전환 인지 부하 | TEST_REQUIRED | PROTOTYPE_TEST |
| OMW-F-009 | ACCESSIBILITY_RISK | 공세·릴·건물·3라인 동시 정보 대체 채널 미검증 | TEST_REQUIRED | UX_TEST |
| OMW-F-010 | MISSING_CANON | 상세 수치 상태 분산 | AUTO_FIX | FIXED_POLICY |
| OMW-F-011 | CANON_IMPLEMENTATION_GAP | 최신 기획과 Legacy 코드 격차 | AUTO_FIX | DECLARED |
| OMW-F-012 | DATA_COMPATIBILITY_RISK | save schema·migration·fault handling 미정 | TEST_REQUIRED | CONTRACT_AND_FAULT_TEST |
| OMW-F-013 | OVERDESIGN | 10병종·20전문화가 코어 검증보다 앞설 가능성 | USER_DECISION/TEST | LATER_GRILL_ME |
| OMW-F-014 | MISSING_CONSUMER | 승인 결정의 Context·Handoff·Workbook 미반영 | AUTO_FIX | FIXED_SYNCED |
| OMW-F-015 | DERIVATIVE_STALE | Visual Index·이미지 상태 분리 | AUTO_FIX/REVIEW | SHOULD_FIX_LATER |

## 6. 비판 재검증

- “문서가 많으므로 결정이 완결됐다”는 비판은 유효하지 않다. 영구 성장·반복 동기·대표 콘텐츠 폭이 미확정이다.
- “PR #116을 병합하면 된다”는 대안은 오래된 Base 전제와 scope drift 때문에 기각했다.
- “20 Stage를 즉시 축소해야 한다”는 비판은 승인된 방향을 침해하므로 기각했다. 대표 콘텐츠 수·제작 순서는 후속 결정과 테스트로 다룬다.
- “상세 수치를 GPT가 정하므로 방향 질문도 필요 없다”는 주장은 기각했다. 숫자는 기획 철학에 종속된다.
- `60_UX_UI_접근성` schema 오류 주장은 bounded 재조회에서 10열 일치가 확인돼 기각했다.

## 7. Recovery 증거

```text
SAME_DECISION_ID: PASS
BASE_V9_4_CURRENT: PASS
PR_116_CLOSED_NOT_MERGED: PASS
PR_119_DRAFT_MERGEABLE: PASS
CHANGED_FILES: 7 DOCS_ONLY
PRODUCT_PATH_CHANGES: 0
SHEET_SCHEMA_FIXES: READBACK_PASS
PROJECT_CORE_DOCUMENTATION_CI: PASS
GDD_SHEET_ADOPTION_CI: PASS
BASE_V9_ADOPTION_CI: PASS
REVIEW_THREADS: 0
RUNTIME/HUMAN/SIMULATION: NOT_RUN
```

## 8. Grill Me 큐

1. `OMW-DEC-20260802-META-PROGRESSION-ROLE-V1` — Profile 영구 성장의 역할.
2. `OMW-DEC-20260802-WORLD-RUN-MOTIVATION-V1` — 20 Stage 반복과 세계·플레이어 동기의 연결.
3. `OMW-DEC-20260802-VS-CONTENT-BREADTH-V1` — 10병종·20전문화의 데모 대표 범위.

## 9. 현재 Gate

```text
RECOVERY_AND_SYNC: PASS
FIRST_GRILL_ME: READY
PRODUCT_CODE: UNCHANGED
CODEX: BLOCKED
PR_MERGE: NOT_REQUESTED
```
