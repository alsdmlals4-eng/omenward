# 오멘워드 Documentation Map

```yaml
updated_at: 2026-08-02
work_mode: TOTAL_PLANNING
current_phase: WORLD_VEIL_ONTOLOGY_GRILL_ME_READY
current_recovery_decision: OMW-DEC-20260802-CANON-RECOVERY-V1
current_planning_decision: OMW-DEC-20260802-WORLD-RUN-MOTIVATION-V1
baseline_main: 9a39f6869f95ec4e6e1f6b96a6a2f896a22c5739
active_base: 9.4.0_RELEASED
current_product: LEGACY_PROTOTYPE
latest_planning: APPROVED_NOT_IMPLEMENTED
product_code_authority: NONE
recovery_pr: 119
superseded_pr: 116_CLOSED_NOT_MERGED
sheet_sync: CONTENT_READBACK_PASS / EXACT_HEAD_TRACKED_IN_SHEET_AND_PR
```

이 문서는 질문별 현행 책임 원본을 선택하는 라우터다. 한 질문에 하나의 현행 책임 원본만 둔다. PR #116은 역사적 승인 계보이며 현재 작업·병합 권위가 아니다.

## 1. 기본 읽기 순서

```text
최신 사용자 지시
→ AGENTS.md
→ BASE_RULES_VERSION.md
→ DOCUMENTATION_MAP.md
→ PROJECT_CORE.md
→ PROJECT_CANON_DECISION_LEDGER.md
→ APPROVED_OMENWARD_WORLD_RUN_MOTIVATION_2026-08-02.md
→ APPROVED_OMENWARD_META_PROGRESSION_ROLE_2026-08-02.md
→ CURRENT_IMPLEMENTATION_STATUS.md
→ ACTIVE_CONTEXT.md
→ HANDOFF_CONTEXT.md
→ 현재 질문의 분야별 책임 원본
→ 실제 code/data/Scene/Resource/tests
→ 연결 Google Sheet
```

## 2. 현재 책임 원본

| 질문 | 현행 책임 원본 | 권한 |
|---|---|---|
| 제품 정체성·플레이어 약속·불변 조건 | `PROJECT_CORE.md` | `CURRENT_CORE_AUTHORITY` |
| 승인 Decision·상태·대체 관계 | `PROJECT_CANON_DECISION_LEDGER.md` | `CURRENT_DECISION_AUTHORITY` |
| 세계·MapRun 반복·승패·징조 역할 | `design/APPROVED_OMENWARD_WORLD_RUN_MOTIVATION_2026-08-02.md` | `USER_APPROVED_WORLD_PRINCIPLE / WORLD_DETAIL_PENDING` |
| Profile 영구 성장 역할 | `design/APPROVED_OMENWARD_META_PROGRESSION_ROLE_2026-08-02.md` | `USER_APPROVED_PLAN / EXACT_VALUES_PENDING` |
| 정본 복구·적대적 finding | `audits/OMENWARD_CANON_RECOVERY_AND_TOTAL_PLANNING_RESTART_2026-08-02.md` | `CURRENT_RECOVERY_AUTHORITY` |
| 전체 Vertical Slice 시스템 관계 | `design/APPROVED_VERTICAL_SLICE_SYSTEM_CONTRACT_2026-07-27.md` | `APPROVED_SYSTEM_CONTRACT / LATER_DECISIONS_OVERRIDE` |
| 실제 구현·Legacy·미검증 경계 | `CURRENT_IMPLEMENTATION_STATUS.md` | `CURRENT_IMPLEMENTATION_AUTHORITY` |
| 현재 작업과 다음 Gate | `ACTIVE_CONTEXT.md` | `CURRENT_CONTEXT_PACK` |
| 새 작업자 인계 | `HANDOFF_CONTEXT.md` | `CURRENT_HANDOFF` |
| Google Sheet 역할·동기화 계약 | `PROJECT_GOOGLE_SHEET_WORKBOOK.md` | `CURRENT_SHEET_CONTRACT` |
| 미확정 수치·콘텐츠 | `DECISIONS_PENDING.md` | `PENDING_REFERENCE / LEDGER_OVERRIDES` |
| 통합 게임 설명 | `OMENWARD_GAME_DESIGN.md` | `REFERENCE_SUMMARY / CURRENT_DECISIONS_OVERRIDE` |

## 3. 현재 승인 기획 계보

- 20 Stage·4막·위험 Stage 5/10/15/20.
- 콘텐츠 Manifest·미션 카드·보스 패키지.
- 세 물리 릴·비가역 전선 커밋.
- 전장 6/3/0=30과 5건물.
- 패배·paid Retry·checkpoint 구조.
- 벨루 정체성.
- 경제·save·Journal·Backup 구조.
- 수평 해금 중심 + 선택형·상한형 준비 보정.
- 별개의 실제 경계 공세 + 징조의 제한된 예측 정보.
- 즉시 GitHub·Sheet Decision sync.

## 4. 세계관 라우팅

### 확정

- 각 MapRun은 별개의 실제 경계 공세다.
- 징조는 다가올 공세를 제한적으로 예고한다.
- 승리는 하나의 균열·침공로 봉쇄다.
- 패배는 실제 전진 방어선 붕괴다.
- Profile은 작전 교리·보급망·기록·준비 체계의 축적이다.
- 벨루는 시간 루프 기억자가 아니라 관측·기록·인과 안내자다.

### 기존 명칭 계보·재검증 필요

- 루메른 왕국.
- 루미엔 영토.
- 트리븐 전선.
- 실베른 성채.
- 베일런 황야.
- 베일의 법칙.
- 베일의 징조.
- 베일종.

### 다음 결정

```text
OMW-DEC-20260802-WORLD-VEIL-ONTOLOGY-V1
= 베일의 본질과 세계의 경계 상태
```

이 결정 전에는 베일을 다른 차원·마법 장벽·신적 존재·생명체 군집 중 하나로 임의 확정하지 않는다.

## 5. 분야별 라우팅

| 분야 | 먼저 읽을 원본 | 보조·검증 |
|---|---|---|
| 핵심 컨셉·뾰족한 재미 | `PROJECT_CORE.md`, Decision Ledger | 룰렛 agency Evidence·사람 검증 |
| 세계·MapRun·징조·승패 | World Run Motivation | 기존 Game Design 명칭 계보·Sheet `11_세계관` |
| 베일·왕국·조직·적·지리 | 후속 세계관 Decision | 기존 명칭은 자동 확정 금지 |
| 벨루 | Belu identity + World Run Motivation | Sheet `13_주요인물` |
| Profile 영구 성장 | Meta Progression Role | Sheet `41_성장_경제`, P0/P1/P2 simulation |
| 룰렛·TokenSource·이동 | `design/APPROVED_ROULETTE_CORE_RULES.md` | Legacy roulette code·latest Red spec |
| 전장·노드·점령 | Project Core, 30-node Decision | Legacy battle code·tests |
| 경제·Retry·저장 | Meta Role, Decision Ledger | simulator/fault test NOT_RUN |
| 콘텐츠·위험 Stage·미션 | Decision Ledger | exact values pending |
| UX·UI·접근성 | Screen Board V2 inherited Decision | runtime·해상도 검증 NOT_RUN |
| 구현 인계 | Planning and Review Complete 이후 새 Plan | Codex BLOCKED |

## 6. 실제 구현 경계

```text
CURRENT_PRODUCT
- independent weighted 9-cell roulette
- barracks/tower/farm
- legacy outpost/capture_power
- free same-stage retry

LATEST_APPROVED_NOT_IMPLEMENTED
- physical reels and permanent move
- 30-node topology
- five buildings
- fixed-time capture
- paid Retry and profile save
- horizontal unlocks and readiness perk
- real-incursion world/run principle
```

## 7. 상태·수치 경계

```text
APPROVED_PLAN != IMPLEMENTED != VALIDATED
RECOMMENDED_DEFAULT != PRODUCT_VALUE
WORLD_PRINCIPLE_APPROVED != WORLD_DETAIL_APPROVED
```

## 8. Grill Me 규칙

- 자료에서 확인 가능한 사실은 묻지 않는다.
- 이미 승인된 결정은 재질문하지 않는다.
- 세계관은 존재론 → 조직 → 적 → 시스템 원리 → 지리 → 인물 순으로 확정한다.
- 프로젝트 방향을 바꾸는 핵심 충돌만 한 번에 하나씩 질문한다.
- 답변 후 GitHub·Sheet가 같은 Decision ID로 동기화되기 전 다음 질문으로 넘어가지 않는다.

## 9. 현재 다음 Gate

```text
Grill Me: OMW-DEC-20260802-WORLD-VEIL-ONTOLOGY-V1
```

```text
PRODUCT_CODE: UNCHANGED
CODEX: BLOCKED
WORLD_DETAIL: PENDING
RUNTIME/HUMAN/SIMULATION: NOT_RUN
```
