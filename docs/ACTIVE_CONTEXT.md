# Active Context

```yaml
updated_at: 2026-08-02
project: OMENWARD / 오멘워드
work_mode: TOTAL_PLANNING
current_phase: WORLD_RUN_MOTIVATION_GRILL_ME_READY
current_recovery_decision: OMW-DEC-20260802-CANON-RECOVERY-V1
current_planning_decision: OMW-DEC-20260802-META-PROGRESSION-ROLE-V1
current_branch: main
context_baseline_commit: 9a39f6869f95ec4e6e1f6b96a6a2f896a22c5739
working_branch: gpt/omenward-canon-recovery-20260802
active_base_version: 9.4.0
base_unreleased_main: OBSERVED_NOT_ADOPTED
current_product: LEGACY_PROTOTYPE
latest_planning: USER_APPROVED / NOT_IMPLEMENTED
product_code_authority: NONE
codex_execution: BLOCKED
primary_platform: PC
future_platform: MOBILE_CONSIDERATION_ONLY
sheet_sync: CONTENT_READBACK_PASS / EXACT_HEAD_TRACKED_IN_SHEET_AND_PR
superseded_pr: 116
recovery_pr: 119
ci_validation: META_DECISION_CONTENT_HEAD_2DA4E1BE_3_GREEN / FINAL_PR_HEAD_GATED
runtime_validation: NOT_RUN
human_validation: NOT_RUN
simulation: NOT_RUN
```

`current_branch: main`과 `context_baseline_commit`은 현재 정본 기준선을 뜻한다. 실제 쓰기 작업은 `working_branch`에서 수행하며 main 직접 변경을 의미하지 않는다.

## 1. 현재 작업

첫 Grill Me Decision이 사용자 승인되고 GitHub·Sheet 내용 재조회까지 통과했다.

```text
OMW-DEC-20260802-META-PROGRESSION-ROLE-V1
= A 권장안 + B의 제한된 성장 체감 반영
```

현재 다음 작업은 두 번째 중요 충돌인 세계·세력·플레이어 동기와 20 Stage 반복 구조를 결정하는 것이다.

## 2. 프로젝트 약속

> 공개된 세 전선의 공세를 읽고 건물과 TokenSource로 세 물리 릴의 미래 배열을 설계·영구 편집한 뒤, 얻은 병력을 한 전선에 비가역 커밋하고 결과 원인을 다음 설계에 반영한다.

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

## 4. 승인된 Profile 영구 성장 역할

정본: `design/APPROVED_OMENWARD_META_PROGRESSION_ROLE_2026-08-02.md`

```text
PRIMARY = 수평 해금 + 제한된 편의
SECONDARY = 선택형·상한형 소규모 준비 보정
FORBIDDEN = 무한 영구 능력치 누적
```

- 기본 Profile로 전체 콘텐츠 완료 가능.
- 수평 해금은 sidegrade이며 단순 상위 호환 금지.
- 시작 보관 편의는 hard cap을 가진다.
- 준비 보정은 한 MapRun에 하나만 선택한다.
- 준비 보정은 유한 랭크·시작/Act 1 중심이며 후반 복리로 확장하지 않는다.
- 직접 유닛 전투 배율, 전 구간 생산 배율, 릴 확률 조작, 무한 prestige 누적은 금지한다.
- Retry는 정산 잔액을 소비하고 준비 보정은 누적 Profile milestone으로 해금하는 구조를 권장한다.
- 정확 효과량·milestone·비용은 아직 제품값이 아니다.

## 5. 실제 구현 경계

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
- horizontal meta unlocks and selectable readiness perk
- product Screen Board V2 and Belu runtime
```

`LEGACY_PROVEN != LATEST_IMPLEMENTED != LATEST_PROVEN`.

## 6. 적대적 검토 결과

### 해결된 중요 충돌

1. 수평 성장만으로 성장 체감이 약할 수 있음 → 제한된 선택형 준비 보정 추가.
2. 직접 능력치 누적이 노가다 정답이 될 수 있음 → 한 런 1개·유한 랭크·초반 한정.
3. Retry와 전투력 구매가 같은 지갑에서 충돌 → 준비 보정은 누적 milestone, Retry는 spendable balance.
4. 수평 해금이 숨은 상위 호환이 될 수 있음 → 비용·조건·채택률·공세별 성능 검증.

### RESEARCH_OR_TEST_REQUIRED

- `P0_BASE_PROFILE`, `P1_HORIZONTAL_ONLY`, `P2_HYBRID_MAX_CANDIDATE` 100K 비교.
- Profile별 full-run 승률·Act 1 clear rate·실패 seed·지배 전략.
- 성장 체감·노가다 강제감·실패 귀인 사람 검증.
- 룰렛 통제감 사람 검증.
- save/retry fault injection.
- 일반/위험 Stage 인지 부하.
- 35분 런 피로도.
- 1080p·720p 가독성·접근성.

## 7. 상세 수치 처리

```text
기획 의미와 제약식
→ RECOMMENDED_DEFAULT / TEST_VALUE
→ 대안 범위
→ simulation·playtest
→ 사용자 승인값
→ 구현값
→ 검증값
```

현재 Meta 시험 가드레일은 제품 확정값이 아니다.

- 최고/기본 Profile full-run 승률 차이 상한 후보: 5 percentage points.
- Act 1 clear-rate 차이 후보: 3~8 percentage points.
- 준비 보정 후보군: 3개.
- 한 런 장착: 1개.
- 준비 보정별 랭크 후보: 2단계.

과거 `20 gold spin`, `160 starting gold`, `70/50/40 refund` 등은 `LEGACY_H0 / HISTORICAL_ONLY`다.

## 8. 우선 읽기

1. `AGENTS.md`
2. `docs/BASE_RULES_VERSION.md`
3. `docs/DOCUMENTATION_MAP.md`
4. `docs/PROJECT_CORE.md`
5. `docs/PROJECT_CANON_DECISION_LEDGER.md`
6. `docs/design/APPROVED_OMENWARD_META_PROGRESSION_ROLE_2026-08-02.md`
7. `docs/CURRENT_IMPLEMENTATION_STATUS.md`
8. `docs/HANDOFF_CONTEXT.md`
9. 현재 Grill Me Decision의 관련 정본·Sheet·실제 파일

## 9. 다음 작업

```text
Grill Me #2: OMW-DEC-20260802-WORLD-RUN-MOTIVATION-V1
```

```text
PRODUCT_CODE: UNCHANGED
CODEX: BLOCKED
PR_MERGE: NOT_REQUESTED
NEXT_GRILL_ME: READY
```
