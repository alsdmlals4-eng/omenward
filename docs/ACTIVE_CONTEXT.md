# Active Context

```yaml
updated_at: 2026-08-02
project: OMENWARD / 오멘워드
work_mode: TOTAL_PLANNING
current_phase: CANON_RECOVERY_AND_ADVERSARIAL_PLANNING
current_recovery_decision: OMW-DEC-20260802-CANON-RECOVERY-V1
baseline_main_commit: 9a39f6869f95ec4e6e1f6b96a6a2f896a22c5739
working_branch: gpt/omenward-canon-recovery-20260802
active_base_version: 9.4.0
base_unreleased_main: OBSERVED_NOT_ADOPTED
current_product: LEGACY_PROTOTYPE
latest_planning: USER_APPROVED / NOT_IMPLEMENTED
product_code_authority: NONE
codex_execution: BLOCKED
primary_platform: PC
future_platform: MOBILE_CONSIDERATION_ONLY
sheet_sync: IN_PROGRESS
superseded_pr: 116
runtime_validation: NOT_RUN
human_validation: NOT_RUN
```

## 1. 현재 작업

현재는 제품 구현 단계가 아니다. PR #116에 누적된 승인 기획을 현재 `main`과 Base v9.4 기준으로 복구하고, GitHub와 Google Sheet를 같은 Decision ID로 동기화한 뒤 총기획을 재개한다.

```text
정본 복구
→ 적대적 검토 finding 확정
→ 안전한 누락·참조·상태 오류 보완
→ 중요한 기획 충돌만 Grill Me
→ 승인 즉시 GitHub·Sheet 동기화
→ 다음 기획 질문
```

## 2. 프로젝트 약속

> 공개된 세 전선의 공세를 읽고 건물과 TokenSource로 세 물리 릴의 미래 배열을 설계·영구 편집한 뒤, 얻은 병력을 한 전선에 비가역 커밋하고 결과 원인을 다음 설계에 반영한다.

핵심 문구:

> **건물로 룰렛을 만들고, 룰렛으로 전선을 지휘한다.**

## 3. 보호할 승인 결정

- 20 Stage·4막·약 35분 목표.
- 위험 Stage 5/10/15/20.
- 상·중·하 세 라인.
- 세 물리 원형 릴·TokenInstance·cursor·3×3 view.
- 가로 이동은 실행 즉시 future reel structure에 영구 반영, undo 없음.
- immutable SpinSnapshot과 명시적 한 번 확정.
- PendingReward 보관·판매·한 라인 비가역 배치.
- 본진 6노드/진영, 중간 거점 6곳×3노드, 접전지 0노드, 총 30노드.
- 금고·농장·타워·병영·지휘소.
- 고정시간 점령.
- Stage 5 이후 MapRun당 최대 1회 paid Retry 원칙.
- 정본 안내자 `벨루 / Belu`.
- PC-primary. 모바일은 후속 고려이며 현재 구현 범위 밖.

## 4. 실제 구현 경계

```text
CURRENT_LEGACY
- independent weighted 9-cell roulette / SPIN_COST=20
- barracks, tower, farm
- legacy outpost nodes and capture_power
- free same-stage retry
- Label/code-drawn graybox UI

LATEST_APPROVED_NOT_IMPLEMENTED
- three physical reels and permanent movement
- 30-node product topology
- five-building economy
- fixed-time capture
- profile/checkpoint/journal/backup
- paid Retry
- product Screen Board V2 and Belu runtime
```

`LEGACY_PROVEN != LATEST_IMPLEMENTED != LATEST_PROVEN`.

## 5. 현재 적대적 검토 결과

### MUST_FIX / AUTO_FIX

1. Base v9.1→v9.3 기록을 current Base v9.4로 복구.
2. PR #116을 현행 병합 단위가 아닌 역사·승계 근거로 전환.
3. Sheet의 오래된 PR HEAD와 `SYNCED_TO_PR_HEAD` 상태 수정.
4. Active Context·Handoff·Documentation Map·Workbook의 current routing 복구.
5. 시험값·legacy값·승인값·구현값·검증값 상태 분리.
6. 검증된 Sheet 열 밀림과 헤더 불일치 수정.

### USER_DECISION_REQUIRED

첫 질문:

```text
OMW-DEC-20260802-META-PROGRESSION-ROLE-V1
Profile 영구 성장은 무엇을 제공해야 하는가?
```

이 결정은 Retry 통화·시작 보관 용량·해금·반복 동기·난이도 공정성에 선행한다.

### RESEARCH_OR_TEST_REQUIRED

- 룰렛 통제감 사람 검증.
- 100K 경제·Retry·save simulation.
- save/retry fault injection.
- 일반/위험 Stage 인지 부하.
- 35분 런 피로도.
- 1080p·720p 가독성·접근성.

## 6. 상세 수치 처리

사용자가 상세 데이터 수치는 GPT 권장안으로 진행하도록 승인했다. 따라서 숫자는 다음 순서로 제시한다.

```text
기획 의미와 제약식
→ RECOMMENDED_DEFAULT / TEST_VALUE
→ 대안 범위
→ simulation·playtest
→ 사용자 승인값
→ 구현값
→ 검증값
```

과거 `20 gold spin`, `160 starting gold`, `70/50/40 refund` 등은 `LEGACY_H0 / HISTORICAL_ONLY`다.

## 7. 우선 읽기

1. `AGENTS.md`
2. `docs/BASE_RULES_VERSION.md`
3. `docs/DOCUMENTATION_MAP.md`
4. `docs/PROJECT_CORE.md`
5. `docs/PROJECT_CANON_DECISION_LEDGER.md`
6. `docs/audits/OMENWARD_CANON_RECOVERY_AND_TOTAL_PLANNING_RESTART_2026-08-02.md`
7. `docs/CURRENT_IMPLEMENTATION_STATUS.md`
8. `docs/HANDOFF_CONTEXT.md`
9. 현재 Grill Me Decision의 관련 정본·Sheet·실제 파일

## 8. 다음 작업

```text
GitHub 정본 복구 commit
→ Google Sheet same-Decision sync·read-back
→ 대체 Draft PR 생성
→ PR #116 superseded 처리
→ Grill Me #1: Profile 영구 성장 역할
```

```text
PRODUCT_CODE: UNCHANGED
CODEX: BLOCKED
PR_MERGE: NOT_REQUESTED
FIRST_GRILL_ME: WAITING_FOR_SYNC
```
