# [현행] 오멘워드 기획 정본 결정 원장

```yaml
updated_at: 2026-08-05
status: CURRENT_DECISION_LEDGER / ACTIVE_PLANNING_BRANCH
current_planning_decision: OMW-DEC-20260805-PLANNING-TACTICAL-SKILLS-AND-MANA-V1
current_process_policy: OMW-PROC-20260805-BENCHMARK-TDD-APPROVAL-BATCH-V1
lifecycle_policy: OMW-PROC-20260804-DYNAMIC-CURRENT-MAIN-AND-DOCUMENT-LIFECYCLE-V1
current_main: RESOLVE_FROM_REPOSITORY_DEFAULT_BRANCH
work_mode: TOTAL_PLANNING
last_merged_planning_pr: 139
last_merged_planning_commit: 554ad7ccb4d3a4aa5f98941ce20f546ed3e01d90
current_working_pr: 140
current_count: 5_OF_10
product_code_authority: NONE
image_generation: STOPPED_BY_USER
```

## 1. 운영 원칙

- `PROJECT_CORE.md`가 제품 정체성과 핵심 불변을 소유한다.
- `DOCUMENTATION_MAP.md`와 `DOCUMENT_LIFECYCLE_REGISTRY.md`가 현재 권위를 소유한다.
- `current_main`은 저장소 기본 브랜치에서 동적으로 해석한다.
- Google Sheet는 같은 Decision ID와 exact PR HEAD로 동기화한다.
- 벤치마크·현업 비교·채택·비채택 이유를 기록한다.
- 승인 10건은 최대 배치 크기이며 고위험 충돌·세션 종료·대규모 영향 시 조기 체크포인트를 허용한다.
- 모든 행동 변경은 `RED → GREEN → REFACTOR`로 진행한다.
- main은 검증된 PR 병합으로만 변경한다.

## 2. Planning Batch

| 순서 | 상태 | Decision |
|---|---|---|
| 1/10 | 완료 | `OMW-DEC-20260804-PLANNING-CORE-FUN-AND-CONTENT-GUARDRAILS-V1` |
| 2/10 | 완료 | `OMW-DEC-20260804-PLANNING-STAGE-WAVE-DANGER-BOSS-PRESSURE-MATRIX-V1` |
| 3/10 | 완료 | `OMW-DEC-20260805-PLANNING-SIX-BUILDING-T2-T3-BRANCHES-AND-COUNTERS-V1` |
| 4/10 | 완료 | `OMW-DEC-20260805-PLANNING-TROOP-ROLES-SYNERGIES-AND-COUNTERS-V1` |
| 5/10 | 현행 | `OMW-DEC-20260805-PLANNING-TACTICAL-SKILLS-AND-MANA-V1` |
| 6/10 | 다음 | `OMW-DEC-20260805-PLANNING-STAGE-END-MERCHANT-V1` |

## 3. Decision 5/10 — 전술스킬·마력

책임 원본:

- `design/APPROVED_OMENWARD_TACTICAL_SKILLS_AND_MANA_2026-08-05.md`
- `reviews/ADVERSARIAL_TACTICAL_SKILLS_MANA_AND_RESEARCH_REVIEW_2026-08-05.md`
- `superpowers/specs/2026-08-05-tactical-skills-and-mana-design.md`
- `superpowers/plans/2026-08-05-tactical-skills-and-mana.md`

```text
마력탑 최대 활성 수 = 1
마력탑 T1 → T2 → T3
분기 = FORBIDDEN
동시 연구 = 1
연구 = 골드 + 시간
시전 = 마력
전술 = T1 4 / T2 3 / T3 3
Stage 전 편성 = 없음
자동 시전 = 금지
Reset = NEW_MAPRUN
```

전술 목록:

```text
T1 = 속박진 / 수호장 / 집중 명령 / 충격파
T2 = 폭풍 억제 / 파쇄 명령 / 봉쇄 결계
T3 = 결전의 깃발 / 성역 / 시간 왜곡
```

결정:

- 마력탑 Tier 상승은 수급량과 연구 가능한 전술 Tier를 높인다.
- 연구 완료 전술은 현재 MapRun 동안 해금된다.
- 유효한 시전 확정 시에만 마력을 소비한다.
- 전술은 병종·건물의 지속 역할을 대체하지 않는다.
- 과거 마력탑 두 분기와 구형 자원명은 구현 입력으로 사용하지 않는다.
- 정확 수치는 `PENDING_SIMULATION`이다.

## 4. TDD·적대적 감사

```text
RED_RUN = Project Core Documentation 954
RED_RESULT = FAILURE_AS_EXPECTED
RED_EXISTING_CONTRACTS = 45 PASS
OMW-AUD-444~467 = REQUIRED_FIXES_APPLIED
GREEN_CANDIDATE_HEAD = 917445ba9b09260da1f2b7bafb0bbf2f809a834b
PROJECT_CORE_RUN = 976 / SUCCESS
GDD_SHEET_RUN = 682 / SUCCESS
OMENWARD_CORE_RUN = 150 / SUCCESS
BASE_V9_RUN = 665 / SUCCESS
SHEET_CANDIDATE_READBACK = PASS
REFACTOR = COMPLETE
PRODUCT_CODE = UNCHANGED
```

final exact-head·merge 증거는 PR #140과 Sheet 현재 상태 셀이 소유한다.

## 5. 감사 계보

```text
OMW-AUD-360~375 = 핵심 재미·정본 충돌
OMW-AUD-376~397 = Stage 압력
OMW-AUD-398~419 = 건물 분기
OMW-AUD-420~443 = 병종 역할
OMW-AUD-444~467 = 전술스킬·마력·연구
```

## 6. 수명주기

- `[현행]`: 5/10 책임 원본·Spec·Plan·Review.
- `[대체됨]`: 과거 마력탑 유량/저장 분기와 구형 자원명.
- `[보류]`: 첫 10분·Hero·Legendary·Meta·Hub.
- `[폐기]`: 자동 시전·Stage 전 편성·복수 마력탑·병렬 연구·T3 전면 복구.
- `[증거]`: 과거 PR·CI·Sheet·Legacy Prototype.

## 7. 제품 경계

```text
CURRENT_PRODUCT = LEGACY_PROTOTYPE
LATEST_PLANNING = TACTICAL_MANA_CANON_NOT_IMPLEMENTED
PRODUCT_CODE = UNCHANGED
DATA_MIGRATION = NOT_AUTHORIZED
EXACT_NUMERICS = PENDING_SIMULATION
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
```

## 8. 완료 이력

```text
OMW-DEC-20260805-PLANNING-SIX-BUILDING-T2-T3-BRANCHES-AND-COUNTERS-V1
3_OF_10
OMW-DEC-20260805-PLANNING-TROOP-ROLES-SYNERGIES-AND-COUNTERS-V1
4_OF_10
LEGACY_C1_C2_C3_PROVEN
```
