# [현행] 오멘워드 기획·운영 정본 결정 원장

```yaml
updated_at: 2026-08-08
status: CURRENT_DECISION_LEDGER
source_main_observed: 7b41923628b68c7c1477b286584973d8516eab6d
base_main_observed: fa69a77a14f923a756064f6ae151d34cadb374f7
current_process_decision: OMW-DEC-20260808-PROCESS-ACTIVATE-INTEGRATED-CONTRACT-V4-4-AND-RECONCILE-ENTRY-STATE-V1
active_contract: PROJECT_TOTAL_PLANNING_IMPLEMENTATION_AND_DELIVERY_INSTRUCTION_v4.4
onboarding_planning_status: APPROVED_10_OF_10_WITH_TOKEN_SOURCE_AMENDMENT
current_simulation_batch: APPROVED_4_OF_10_CONDITIONAL_FAIL
current_simulation_pr: 154
product_code_authority: NONE
entry_gate: BLOCK
image_generation: STOPPED / NOT_AUTHORIZED
```

이 문서는 현재 Decision의 색인과 충돌 해소 우선순위를 책임진다. 상세 설계 내용은 개별 승인 책임 원본에 남기고, 과거 버전의 이 원장에 있던 superseded 상세 문구는 Git history의 역사 증거로만 사용한다.

## 1. 현재 권위 우선순위

1. `docs/PROJECT_CORE.md`
2. `docs/DOCUMENT_LIFECYCLE_REGISTRY.md`
3. `docs/ONBOARDING_PLANNING_CURRENT_AUTHORITY.md`
4. `docs/DECISIONS_PENDING.md`
5. 현행 개별 승인 설계 문서
6. `docs/CURRENT_IMPLEMENTATION_STATUS.md`
7. 이 Decision 원장
8. 과거 PR·commit·Sheet 역사 행

Google Sheet는 동일 Decision ID와 exact branch/PR 상태를 기록하되, 제품 정본을 단독으로 대체하지 않는다.

## 2. 완료된 온보딩 기획

```text
OMW-DEC-20260806-PLANNING-PR142-LATEST-MAIN-INTEGRATION-V3
status = APPROVED_10_OF_10_WITH_TOKEN_SOURCE_AMENDMENT
latest_amendment = OMW-DEC-20260806-PLANNING-BARRACKS-AUTO-PRODUCTION-AND-TOKEN-SOURCE-AMENDMENT-V1
product_implementation = NOT_STARTED
```

현행 상세 우선순위는 `docs/ONBOARDING_PLANNING_CURRENT_AUTHORITY.md`가 소유한다. 특히 `SPECIAL_T1_TOKEN_SOURCE = NONE`은 superseded 역사 문구이며 구현 입력으로 사용할 수 없다.

## 3. 현재 병영 수치·시뮬레이션 배치

| 순서 | 상태 | Decision |
|---|---|---|
| 1/10 | 승인 / simulation contract only | `OMW-DEC-20260806-PLANNING-BARRACKS-ECONOMY-PRODUCTION-TOKEN-SOURCE-SIMULATION-CONTRACT-V1` |
| 2/10 | 승인 / input provenance | `OMW-DEC-20260806-PLANNING-BARRACKS-SIMULATION-INPUT-PROVENANCE-AND-ROULETTE-AXIS-CORRECTION-V1` |
| 3/10 | 승인 / smoke input only | `OMW-DEC-20260806-PLANNING-CURRENT-MAPRUN-ECONOMY-AND-PRESSURE-BASELINE-V1` |
| 4/10 | `CONDITIONAL_FAIL` | `OMW-DEC-20260806-PLANNING-BARRACKS-SMOKE-SWEEP-RESULTS-AND-IDENTIFIABILITY-GATE-V1` |

4/10의 현재 차단은 다음 두 핵심 finding을 포함한다.

```text
MODEL_IDENTIFIABILITY_FAIL
SPECIAL_TOKEN_SHARE_BURST_MAX = 0.50 > 0.45
```

10,000 decision sweep, 50,000 confirmation sweep, 최종 수치 확정, 제품 구현은 이 차단이 해소되기 전 진행하지 않는다.

## 4. 현재 운영·도구 Decision

```text
OMW-DEC-20260806-TOOLS-HIGODOT-GUT-AUTHORITY-AND-WORK-ENTRY-GATE-V1
OMW-DEC-20260806-TOOLS-GUT-9-7-1-VENDOR-MANIFEST-RECONCILIATION-V1
OMW-DEC-20260807-PROCESS-ACTIONS-BUDGET-LOCAL-EXACT-HEAD-FALLBACK-V1
OMW-DEC-20260807-PROCESS-BASE-REPOSITORY-SKILL-MAP-AND-LOCAL-VERIFICATION-PACK-V1
OMW-DEC-20260807-PROCESS-PUBLIC-REPOSITORY-STANDARD-HOSTED-ACTIONS-V1
OMW-DEC-20260807-DOCS-C1-REMOTE-PROVEN-AUTHORITY-RESTORATION-V1
OMW-DEC-20260807-TESTS-CURRENT-CANON-LIFECYCLE-RECONCILIATION-V1
OMW-DEC-20260808-PROCESS-ACTIVATE-INTEGRATED-CONTRACT-V4-4-AND-RECONCILE-ENTRY-STATE-V1
```

v4.3 활성화 Decision은 역사 비교 전용이다. 현재 계약은 v4.4다.

## 5. 2026-08-08 repository drift 판정

Sheet의 마지막 정본 기준 이후 actual `main`에는 다음 direct-main 변경이 존재한다.

- `37f13c2ba4b76d59a300ce08d15c2dd4ab784ce6`: Hera Agent Godot 파일 유입.
- `7b41923628b68c7c1477b286584973d8516eab6d`: `.asset-vault/` ignore 추가.

두 변경은 저장소에 존재하는 사실은 인정하지만, 대응 Decision linkage가 현 원장·Sheet에서 발견되지 않았으므로 이 Decision이 소급 승인하지 않는다.

Hera 판정:

```text
FILES_PRESENT = TRUE
PROJECT_GODOT_EDITOR_PLUGIN_ENABLED = FALSE
ADOPTION = NOT_VERIFIED_INSTALLED_UNUSED
ROLE_IF_ADOPTED = LIVE_QA_AND_OBSERVABILITY_ONLY
PERSISTENT_SOURCE_MUTATION = FORBIDDEN
NEXT = EXISTING_SOLUTION_FIRST_DISPOSITION
```

## 6. Entry Gate

```text
ENTRY_GATE = BLOCK
```

현재 blocking reasons:

- PR #154 conditional fail / unmerged
- PR #155 GUT adoption spec not merged
- PR #159 Base recovery incomplete
- HiGodot exact source/version unverified
- Hera direct-main import disposition not closed
- local Godot / shared audio vault `BLOCKED_UNVERIFIED`
- historical secret scan unproven accepted risk

금지:

```text
PRODUCT_IMPLEMENTATION
GODOT_AUTHORING_MUTATION
FORMAL_GUT_EXECUTION
HERA_LIVE_QA_COMPLETION_CLAIM
IMAGE_GENERATION
AUDIO_ASSET_IMPORT
LOCAL_OR_RUNTIME_COMPLETION_CLAIM
```

## 7. 다음 작업

1. PR #159 Base recovery의 남은 unread/partial surface를 0으로 축소.
2. PR #154 4/10 conditional fail의 capability proxy / multi-special token burst remediation.
3. PR #155 GUT adoption spec을 현재 v4.4 역할 계약에 맞춰 재검토.
4. Hera direct-main 유입을 `REUSE / ABSORB / REFACTOR / ARCHIVE` 중 하나로 명시 판정.

제품 구현은 Entry Gate가 PASS로 재판정될 때까지 시작하지 않는다.
