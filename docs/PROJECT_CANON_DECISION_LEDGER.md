# 오멘워드 기획 정본 결정 원장

```yaml
updated_at: 2026-08-02
status: CURRENT_DECISION_LEDGER / TOTAL_PLANNING
current_recovery_decision: OMW-DEC-20260802-CANON-RECOVERY-V1
current_planning_decision: OMW-DEC-20260802-WORLD-RUN-MOTIVATION-V1
canonical_baseline_main: 9a39f6869f95ec4e6e1f6b96a6a2f896a22c5739
active_base: 9.4.0
working_branch: gpt/omenward-canon-recovery-20260802
recovery_pr: 119
superseded_planning_pr: 116
product_code_authority: NONE
sheet_id: 1VLwRtXGDtyj0JFt98wdIOtG6Zqc3wtdfCzSF9Fo6lpw
sheet_sync: WORLD_RUN_SYNC_IN_PROGRESS
ci_validation: PENDING_CURRENT_HEAD
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
| `OMW-DEC-20260802-WORLD-RUN-MOTIVATION-V1` | `USER_APPROVED / CURRENT / SYNC_IN_PROGRESS` | 각 MapRun은 징조로 감지된 별개의 실제 경계 공세이며, 징조는 제한된 예측 정보다. 승리는 한 균열·침공로 봉쇄, 패배는 전진 방어선 붕괴이며 시간 반복·가상 시뮬레이션이 아니다 | `design/APPROVED_OMENWARD_WORLD_RUN_MOTIVATION_2026-08-02.md` | 세계 상세·서사 콘텐츠·runtime·human 검증 미실행 |
| `OMW-DEC-20260802-META-PROGRESSION-ROLE-V1` | `USER_APPROVED / CURRENT / CONTENT_SYNCED` | 수평 해금·제한 편의를 주축으로 하고 한 런 1개·유한 랭크·초반 한정의 선택형 준비 보정으로 소규모 영구 전투력을 포함 | `design/APPROVED_OMENWARD_META_PROGRESSION_ROLE_2026-08-02.md` | exact values·simulation·runtime·human 검증 미실행 |
| `OMW-DEC-20260802-CANON-RECOVERY-V1` | `USER_APPROVED / SYNCED` | Base v9.4와 현재 main에서 깨끗한 정본 복구 PR을 만들고 PR #116은 역사 증거로 대체 | recovery audit, PR #119, connected Sheet | 문서·Sheet sync·CI Green, 제품 변경 없음 |
| `OMW-DEC-20260731-CONTENT-MANIFEST-V1` | `INHERITED_USER_APPROVED_PLAN` | 전장 1개·4막·Stage 20·일반 공세 8·위험 패키지 4·보스 패키지 3·미션 카드 12 | PR #116 승인 계보 | 미구현·미검증 |
| `OMW-DEC-20260731-DEFEAT-RETRY-V1` | `INHERITED_CURRENT_PRINCIPLE / EXACT_VALUES_PENDING` | Stage 5 이후 MapRun당 최대 1회 paid Retry와 동일 RNG lineage checkpoint 복원 | PR #116 승인 계보 | 미구현·fault test 미실행 |
| `OMW-DEC-20260731-DANGER-BOSS-V1` | `INHERITED_USER_APPROVED_PLAN` | 위험 Stage 5/10/15/20의 차별화된 공개 위협 패키지 | PR #116 승인 계보 | exact values·runtime 미실행 |
| `OMW-DEC-20260801-PROJECT-INTEGRITY-GATE-V1` | `INHERITED_CURRENT_CANON` | 건설 노드 1종, 본진 6/진영, 중간 거점 6곳×3, 접전지 0, 총 30 | PR #116 승인 계보 | 최신 제품 미구현 |
| `OMW-DEC-20260801-BELU-IDENTITY-V1` | `INHERITED_CURRENT_CANON` | 정본명 벨루, 율비는 역사 별칭; 벨루는 선택 근거를 설명하되 자동 결정하지 않음 | PR #116 승인 계보 | 제품 UI·대사 미구현 |
| `OMW-DEC-20260801-VISUAL-SCREEN-BOARD-V2` | `INHERITED_TEXT_SPEC / IMAGE_NOT_APPROVED` | 8개 독립 제품 화면과 정보 위계 방향 | PR #116 승인 계보 | 이미지·엔진 UI 미검증 |
| `OMW-DEC-20260801-ECONOMY-RETRY-SAVE-PLANNING-V1` | `INHERITED_STRUCTURE_CURRENT / VALUES_PENDING` | MapRun/Profile 경제 분리, Retry·checkpoint·Journal·Backup 구조 | PR #116 승인 계보 | simulator·schema·fault test 미실행 |
| `OMW-DEC-20260801-LATEST-CONTRACT-RED-TEST-V1` | `INHERITED_SPEC_WRITTEN_NOT_EXECUTED` | 최신 3릴·30노드·5건물·fixed capture·paid Retry의 Red test 책임 정의 | PR #116 승인 계보 | 실제 test files 없음 |
| `OMW-DEC-20260731-CANON-SYNC-V1` | `INHERITED_OPERATING_RULE` | 주요 승인 Decision은 GitHub와 Sheet에 같은 ID·commit으로 즉시 동기화 | PR #116 승인 계보 | recovery와 후속 Decision에서 재검증 |

## 3. 보호된 제품 기획

> 공개된 세 전선의 위험을 읽고 건물과 TokenSource로 세 물리 릴의 미래 배열을 설계·영구 편집한 뒤, 얻은 병력을 한 전선에 비가역 커밋하고 결과 원인을 다음 설계에 반영한다.

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

## 4. 세계·MapRun 반복 동기 정본

```text
징조 감지
→ 별개의 실제 경계 방어 작전
→ 4막·20 Stage 공세 고조
→ 균열/침공로 봉쇄 또는 전진 방어선 붕괴
→ 기록·교리·정산된 성과가 Profile로 귀환
```

- 같은 멸망의 날을 반복하지 않는다.
- 모든 전투가 가상 시뮬레이션이었다는 반전을 사용하지 않는다.
- 징조는 공세의 구조와 치명적 행동을 제한적으로 예고하지만 결과를 확정하지 않는다.
- Stage 20 승리는 해당 공세를 실제로 막은 결과이며, 다른 베일·침공로가 존재해 전쟁은 지속된다.
- 패배는 실제 피해와 철수로 남는다. paid Retry는 시간 되감기가 아니라 같은 공세의 비상 재투입이다.
- Profile은 실제 작전에서 축적된 교리·보급망·기록·준비 체계다.
- 벨루는 시간 루프 기억자가 아니라 공세를 관측·기록하고 인과를 설명하는 안내자다.
- 기존 `루메른 왕국·루미엔 영토·트리븐 전선·실베른 성채·베일런 황야·베일의 법칙·베일종` 명칭 계보는 보존하지만 최종 정의는 후속 세계관 Decision에서 재검증한다.

## 5. Profile 영구 성장 정본

```text
PRIMARY = 수평 해금 + 제한된 편의
SECONDARY = 선택형·상한형 준비 보정
FORBIDDEN = 무한 영구 능력치 누적
```

- 기본 Profile로 모든 콘텐츠 완료 가능.
- 수평 해금은 sidegrade이며 단순 상위 호환 금지.
- 시작 보관 편의는 hard cap을 가진다.
- 준비 보정은 한 MapRun에 하나만 장착한다.
- 준비 보정은 유한 랭크이고 시작·Act 1 중심이며 후반 복리로 확장하지 않는다.
- 유닛 전투 배율·생산량 전 구간 배율·릴 확률 조작·무한 prestige 누적을 금지한다.
- Retry는 spendable balance를 소비하고 준비 보정은 누적 정산 milestone으로 해금하는 것을 권장한다.
- 정확 효과량·milestone·비용은 시험값과 100K Profile trajectory 뒤 별도 승인한다.

## 6. 현재 실제 구현 경계

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

세계·MapRun 정본, Profile 영구 성장, 수평 해금, 준비 보정, paid Retry는 제품에 구현되지 않았다.

## 7. 상세 수치 정책

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

## 8. 적대적 검토 판정

### 해결된 핵심 충돌

- 반복 전투가 시간 루프인가 실제 전쟁인가: 별개의 실제 경계 공세로 확정.
- Stage 20 승리 뒤 반복의 의미: 한 균열·침공로는 봉쇄되지만 전쟁 전체는 지속.
- 징조가 선택을 무효화하는 문제: 공세 구조를 예고하지만 결과는 확정하지 않음.
- Profile 성장의 세계관 의미: 전술 교리·보급망·기록·준비 체계의 축적.
- 영구 성장 없음으로 반복 동기가 약해지는 위험: 수평 해금과 제한된 준비 보정으로 보완.
- 직접 능력치 누적으로 노가다가 정답이 되는 위험: 한 런 1개·유한 랭크·초반 한정으로 제한.

### RESEARCH_OR_TEST_REQUIRED

- 세계 규모·공세 빈도·한 작전의 인명·영토 지속 결과.
- `P0_BASE_PROFILE`, `P1_HORIZONTAL_ONLY`, `P2_HYBRID_MAX_CANDIDATE` 100K Profile trajectory 비교.
- 준비 보정별 지배 전략·후반 꼬리 seed·실패 귀인.
- 성장 체감과 노가다 강제감 사람 검증.
- 룰렛 통제감 사람 검증.
- save/retry fault injection.
- 일반/위험 Stage 인지 부하.
- 35분 런 피로도.

## 9. USER_DECISION_REQUIRED

| 순서 | Decision ID | 질문 | 상태 |
|---|---|---|---|
| 1 | `OMW-DEC-20260802-WORLD-VEIL-ONTOLOGY-V1` | 베일의 본질과 세계의 경계 상태 | `READY` |
| 2 | 오멘워드 조직·루메른 왕국·지휘관의 정치적 위치 | 세계 조직 결정 | `QUEUED` |
| 3 | 베일종·경계파쇄자의 발생·지성·목적 | 적대 존재 결정 | `QUEUED` |
| 4 | 징조·세 물리 릴·TokenSource의 세계 내 원리 | 시스템 세계관 연결 | `QUEUED` |
| 5 | `OMW-DEC-20260802-VS-CONTENT-BREADTH-V1` | 10병종·20전문화의 데모 대표 범위 | `QUEUED_AFTER_WORLD_CORE` |

## 10. 검증 기준

```text
RECOVERY_DECISION_ID_MATCH: PASS
BASE_V9_4_CURRENT: PASS
PR_116_CLOSED_NOT_MERGED: PASS
PR_119_CURRENT_DRAFT: PASS
PRODUCT_PATH_CHANGES: 0
WORLD_RUN_GITHUB_SYNC: IN_PROGRESS
WORLD_RUN_SHEET_READBACK: PENDING
EXACT_PR_HEAD: TRACK_IN_PR_AND_SHEET_AFTER_SYNC
RUNTIME/HUMAN/SIMULATION: NOT_RUN
```

## 11. 현재 다음 Gate

```text
Grill Me: OMW-DEC-20260802-WORLD-VEIL-ONTOLOGY-V1
```

```text
PRODUCT_CODE: NOT_AUTHORIZED
CODEX: BLOCKED
SIMULATION: NOT_RUN
RUNTIME: NOT_RUN
HUMAN_QA: NOT_RUN
MOBILE: FUTURE_CONSIDERATION_ONLY
```
