# OMENWARD 기획 정본 복구·총기획 재개 감사

```yaml
decision_id: OMW-DEC-20260802-CANON-RECOVERY-V1
approval: USER_APPROVED_2026-08-02_10:53_KST
status: CANON_RECOVERY_CURRENT / TOTAL_PLANNING_RESTART / SHEET_FIRST_READBACK_PASS
work_mode: TOTAL_PLANNING
current_phase: REVIEW_THEN_PLAN
base_authority: v9.4.0_RELEASED
base_main_unreleased: OBSERVED_NOT_ADOPTED
project_repository: alsdmlals4-eng/omenward
baseline_main_commit: 9a39f6869f95ec4e6e1f6b96a6a2f896a22c5739
working_branch: gpt/omenward-canon-recovery-20260802
replacement_pr: 119
superseded_pr: 116
product_code_authority: NONE
planning_and_documentation_authority: APPROVED
primary_platform: PC
future_platform: MOBILE_CONSIDERATION_ONLY
runtime_validation: NOT_RUN
human_validation: NOT_RUN
simulation: NOT_RUN
```

## 1. 복구 목적

현재 `main`과 Base v9.4를 기준으로 승인된 기획을 복구한다. PR #116에서 사용자 승인된 결정은 보존하지만, Base v9.1→v9.3 이관 전제·오래된 PR HEAD·stale validator·혼합된 Sheet 상태는 현행 권위로 가져오지 않는다.

총기획은 다음 생명주기로 진행한다.

```text
프로젝트 전체 감사
→ 승인 강점 보호
→ 충돌·누락·과설계·미검증 가정 공격
→ 비판의 사실성과 영향 재검증
→ 안전한 기획 오류·누락 자동 보완
→ 중요한 기획 선택만 Grill Me
→ 승인 즉시 GitHub·Sheet 동일 Decision ID 동기화
→ 다음 기획 질문
```

상세 데이터 수치는 다음 상태를 분리한다.

```text
LEGACY_H0 / HISTORICAL_ONLY
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
| Replacement PR | `#119`, Draft |
| Superseded planning PR | `#116`, 병합하지 않음 |
| Current product | Legacy prototype |
| Actual roulette | 독립 가중치 9칸, `SPIN_COST=20` |
| Actual buildings | 병영·타워·농장 3종, 즉시 건설 |
| Actual retry | 무료 동일 Stage 재시작 |
| Actual battlefield | Legacy 3라인·outpost·capture_power |
| Latest planned product | 세 물리 릴·30노드·5건물·고정시간 점령·paid Retry |
| Runtime/human proof | 최신 제품 기준 없음 |
| Connected Sheet | 25개 탭, 첫 bounded read-back 통과 |
| Protected paths | `scripts/`, `scenes/`, `data/`, `resources/`, `assets/`, `addons/`, `project.godot` |
| Rollback | Draft PR 폐기와 Sheet revision 복원 |

## 3. 보호할 승인 강점

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
- 안내자 정본명 `벨루 / Belu`; 선택을 대신하지 않음.
- 승인·구현·자동 검증·사람 검증 상태 분리.

## 4. PR #116 승계 판정

PR #116은 126개 commit과 52개 파일이 누적된 Base v9.3 기획 PR이며 현재 main보다 뒤처지고 병합 불가 상태였다. 따라서 PR 자체는 병합 단위로 사용하지 않는다.

### 승계하는 결정

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

### 승계하지 않는 상태

- Base v9.1이 현재라는 주장.
- Base v9.3이 다음 필수 migration이라는 주장.
- PR #116의 오래된 HEAD를 current Sheet HEAD로 사용하는 상태.
- stale validator의 구형 문자열 요구.
- PR #116 병합을 전제로 한 실행 순서.
- 미실행 simulator·Red test·runtime·human QA의 완료 표현.

## 5. 적대적 검토 Finding Ledger

| ID | 유형 | 검증된 문제 | 영향 | 분류 | 판정 |
|---|---|---|---|---|---|
| OMW-F-001 | STALE_REFERENCE | PR·Sheet는 Base v9.1→v9.3을 현행으로 기록했지만 main은 v9.4 | 잘못된 기준선 | AUTO_FIX_ELIGIBLE | FIXED_IN_PR_119 |
| OMW-F-002 | DUPLICATE_ACTIVE_SOURCE | main과 PR #116이 서로 다른 상태·다음 작업을 주장 | 콜드 스타트 실패 | AUTO_FIX_ELIGIBLE | FIXED_IN_PR_119 |
| OMW-F-003 | MISSING_SYNC | Sheet current PR HEAD가 실제 작업보다 오래됨 | 허위 `SYNCED` | AUTO_FIX_ELIGIBLE | FIRST_READBACK_PASS |
| OMW-F-004 | PRODUCTION_RISK | 20 Stage·모든 시스템·표현·저장·메타를 첫 데모에 포함 | 제작·검증량 폭증 | RESEARCH_OR_TEST_REQUIRED | TEST_IN_VERTICAL_SLICE |
| OMW-F-005 | UNPROVEN_ASSUMPTION | 릴 구조 설계가 실제 통제감·재미·실패 귀인을 만든다는 가설 | 코어 재미 미검증 | RESEARCH_OR_TEST_REQUIRED | HUMAN_TEST_REQUIRED |
| OMW-F-006 | UNDERDESIGN | Profile 영구 성장 역할 미확정 | Retry·해금·난이도·반복 동기 충돌 | USER_DECISION_REQUIRED | GRILL_ME_1 |
| OMW-F-007 | UNDERDESIGN | 세계·세력·플레이어 동기가 20 Stage 반복과 약하게 연결됨 | 콘텐츠 정체성 약화 | USER_DECISION_REQUIRED | GRILL_ME_QUEUE |
| OMW-F-008 | PLAYER_EXPERIENCE_RISK | 일반 정지/위험 실시간 전환의 인지 부하 미검증 | 위험 Stage 과부하 | RESEARCH_OR_TEST_REQUIRED | PROTOTYPE_TEST |
| OMW-F-009 | ACCESSIBILITY_RISK | 공세·릴·건물·3라인 동시 정보의 대체 채널 미검증 | 가독성 실패 | RESEARCH_OR_TEST_REQUIRED | UX_TEST |
| OMW-F-010 | MISSING_CANON | 상세 수치 상태가 legacy·candidate·pending으로 분산 | 시험값 오인 | AUTO_FIX_ELIGIBLE | FIXED_POLICY |
| OMW-F-011 | CANON_IMPLEMENTATION_GAP | 최신 기획과 Legacy 코드 차이가 큼 | migration 위험 | AUTO_FIX_ELIGIBLE | DECLARED |
| OMW-F-012 | DATA_COMPATIBILITY_RISK | Save/Checkpoint/Journal/Backup schema·migration 미정 | 저장 손상·Retry 중복 | RESEARCH_OR_TEST_REQUIRED | FAULT_TEST_REQUIRED |
| OMW-F-013 | OVERDESIGN | 10병종·20전문화 전체 상세가 코어 검증보다 앞설 수 있음 | 제작량이 학습을 압도 | USER_DECISION_REQUIRED_OR_TEST | LATER_GRILL_ME |
| OMW-F-014 | MISSING_CONSUMER | PR #116 승인 결정이 main Context·Handoff·Workbook에 없음 | 다음 작업자 오도 | AUTO_FIX_ELIGIBLE | FIXED_IN_PR_119 |
| OMW-F-015 | DERIVATIVE_STALE | Screen Board·Visual Index·이미지 상태 분리 | 잘못된 이미지 재사용 | AUTO_FIX_AND_REVIEW | SHOULD_FIX_LATER |

## 6. Attack → Validate Critique

### “기획 문서가 많으므로 방향은 충분히 명확하다”

문서량은 많지만 영구 성장, 반복 동기, 대표 콘텐츠 폭, 위험 Stage 조작 부담은 닫히지 않았다. `VALID_FINDING`이다.

### “PR #116을 병합하면 해결된다”

승인 문서는 많지만 오래된 Base 전제, scope drift, merge conflict, stale validator와 Sheet drift가 존재한다. `MUST_FIX`이며 PR #119 대체가 타당하다.

### “20 Stage 데모는 무조건 축소해야 한다”

제작 위험은 크지만 20 Stage와 완성형 데모 방향은 승인돼 있다. 강제 축소는 `REJECTED_CRITIQUE`; 대표 콘텐츠 수와 제작 순서는 후속 결정·테스트 대상으로 둔다.

### “상세 수치는 GPT 권장안이면 즉시 확정해도 된다”

숫자는 권장·시험값으로 제시할 수 있으나, 영구 성장 철학과 실패 비용·보상 의미에 종속된다. 사용자 방향 결정을 AI가 대신하지 않는다.

### “60_UX_UI_접근성 탭도 schema 오류다”

bounded 재조회 결과 헤더 10열과 데이터 10열이 일치했다. 이 비판은 `REJECTED_CRITIQUE`다.

## 7. 첫 Sheet 동기화 결과

Decision: `OMW-DEC-20260802-CANON-RECOVERY-V1`

첫 쓰기·재조회 범위:

- `00_프로젝트_허브!A1:L2`
- `01_작업순서!A1:N9`
- `02_현재_확정결정!A17:M18`
- `03_근거_라이브러리!A1:I11`
- `04_누락_충돌_감사!A22:H28`
- `40_핵심시스템_메인콘텐츠!A1:K8`
- `90_본제작_출시_사업!A1:H8`
- `99_변경이력!A17:H18`

```text
SAME_DECISION_ID: PASS
BASE_V9_4_CURRENT: PASS
PR_116_HISTORICAL_BOUNDARY: PASS
APPROVAL_IMPLEMENTATION_VALIDATION_SEPARATION: PASS
03_EVIDENCE_COLUMN_ALIGNMENT: PASS
40_SYSTEM_ID_ALIGNMENT: PASS
90_MILESTONE_SCHEMA_ALIGNMENT: PASS
FIRST_BOUNDED_READBACK: PASS
FINAL_PR_HEAD_WRITEBACK: PENDING_AFTER_THIS_COMMIT
```

## 8. 개선 분류

### AUTO_FIX_ELIGIBLE

- Base v9.4·main 기준선 복구.
- PR #116 대체 관계.
- GitHub·Sheet HEAD·Decision·상태 축 분리.
- Active Context·Handoff·Documentation Map·Workbook 라우팅.
- 상세 수치 상태 레이블.
- 실제 구현과 최신 기획 간극.
- 검증된 Sheet 열 밀림·schema 오류.

### USER_DECISION_REQUIRED

1. Profile 영구 성장의 역할.
2. 세계·세력·플레이어 동기와 20 Stage 반복의 연결.
3. 10병종·20전문화의 데모 대표 범위.

### RESEARCH_OR_TEST_REQUIRED

- 룰렛 통제감 사람 검증.
- 100K 경제·Retry·save simulation.
- save/retry fault injection.
- 일반/위험 Stage 인지 부하.
- 35분 런 피로도.
- 1080p·720p 가독성·접근성.

## 9. 첫 Grill Me

```yaml
decision_id: OMW-DEC-20260802-META-PROGRESSION-ROLE-V1
finding: OMW-F-006
question: 실패와 완주 뒤 Profile 영구 성장은 어떤 역할을 가져야 하는가?
status: READY_AFTER_FINAL_SYNC
```

이 결정은 Retry 통화, 시작 보관 용량, 해금, 난이도 공정성과 반복 동기에 선행한다.

## 10. 현재 Gate

```text
RECOVERY_PLAN: WRITTEN
GITHUB_CANON: UPDATED_IN_PR_119
SHEET_FIRST_READBACK: PASS
FINAL_EXACT_HEAD_WRITEBACK: PENDING_AFTER_THIS_COMMIT
PR_116_SUPERSESSION: PENDING_FINAL_SYNC
PRODUCT_CODE: UNCHANGED
CODEX: BLOCKED
FIRST_GRILL_ME: READY_AFTER_FINAL_SYNC
```
