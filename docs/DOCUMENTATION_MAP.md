# 오멘워드 Documentation Map

- 갱신일: `2026-07-31`
- 현재 제품 단계: `PROTOTYPE_AND_VERTICAL_SLICE`
- 현재 Work Mode: `PLAN`
- 실행 프로필: `PLANNING_ONLY_PROFILE`
- 제품 코드 승인: `NO`
- Vertical Slice 구현: `NOT_STARTED`
- 사람 검증: `HUMAN_QA_NOT_RUN`
- 별도 Core PoC: `SKIPPED_BY_USER_DECISION`

이 문서는 질문별 책임 원본을 선택하는 권위 라우터다. 최신 사용자 지시와 현재 책임 원본을 우선하며 과거 V2 문서를 동시에 활성 정본으로 취급하지 않는다.

---

## 1. 기본 읽기 순서

```text
최신 사용자 지시
→ AGENTS.md
→ BASE_RULES_VERSION.md
→ DOCUMENTATION_MAP.md
→ PROJECT_CORE.md
→ 현재 질문의 분야별 APPROVED 계약
→ PROJECT_CANON_DECISION_LEDGER.md
→ DECISIONS_PENDING.md
→ CURRENT_IMPLEMENTATION_STATUS.md
→ ACTIVE_CONTEXT.md / HANDOFF_CONTEXT.md
→ 실제 코드·데이터·테스트
```

주요 승인 결정은 GitHub와 연결 Google Sheet에서 같은 결정 ID를 사용해야 한다.

---

## 2. 현재 활성 책임 원본

| 질문 | 책임 원본 | 권한 |
|---|---|---|
| 제품 정체성·현재 범위·불변 조건 | `PROJECT_CORE.md` | `CURRENT_CORE_AUTHORITY` |
| 전체 시스템 Vertical Slice 관계 | `design/APPROVED_VERTICAL_SLICE_SYSTEM_CONTRACT_2026-07-27.md` | `CURRENT_USER_APPROVED_PLAN` |
| 런 시간·피로도 | `design/APPROVED_VERTICAL_SLICE_RUN_DURATION_AND_FATIGUE_CONTRACT_2026-07-31.md` | `CURRENT_USER_APPROVED_PLAN` |
| 20 Stage·4막·첫 10분 | `design/APPROVED_VERTICAL_SLICE_20_STAGE_FOUR_ACT_AND_FIRST_10_MINUTES_CONTRACT_2026-07-31.md` | `CURRENT_USER_APPROVED_PLAN` |
| 콘텐츠 Manifest·미션 카드 풀 | `design/APPROVED_VERTICAL_SLICE_CONTENT_MANIFEST_AND_MISSION_CARD_POOL_2026-07-31.md` | `CURRENT_USER_APPROVED_PLAN` |
| 위험 Stage·보스 행동 패키지 | `design/APPROVED_VERTICAL_SLICE_DANGER_STAGE_AND_BOSS_PACKAGE_2026-07-31.md` | `CURRENT_USER_APPROVED_PLAN / EXACT_VALUES_PENDING` |
| 패배·영구재화 재시도 | `design/APPROVED_VERTICAL_SLICE_DEFEAT_AND_PAID_RETRY_PRINCIPLE_2026-07-31.md` | `CURRENT_USER_APPROVED_DETAIL / EXACT_COST_VALUES_PENDING` |
| 중간 이미지 점검 | `reviews/APPROVED_MIDPOINT_IMAGE_REVIEW_GATE_2026-07-31.md` | `CURRENT_USER_APPROVED_WORKFLOW / IMAGE_INPUT_PENDING` |
| 주요 결정 ID·GitHub/Sheet 위치 | `PROJECT_CANON_DECISION_LEDGER.md` | `CURRENT_DECISION_LEDGER` |
| Benchmark-First 기획 게이트 | `operations/BENCHMARK_FIRST_PLANNING_RULE_2026-07-31.md` | `CURRENT_PROJECT_WORK_RULE` |
| 즉시 기획 정본 동기화 | `operations/CANON_SYNC_PROTOCOL_2026-07-31.md` | `CURRENT_PROJECT_WORK_RULE` |
| 최신 적대적 검토 | `reviews/ADVERSARIAL_VERTICAL_SLICE_REVIEW_2026-07-27.md` | `CURRENT_REVIEW_EVIDENCE` |
| 구현·Legacy·미검증 경계 | `CURRENT_IMPLEMENTATION_STATUS.md` | `CURRENT_IMPLEMENTATION_AUTHORITY` |
| 후속 수치·콘텐츠 결정 | `DECISIONS_PENDING.md` | `PENDING_ONLY` |
| 구현·검증 순서 | `OMENWARD_ROADMAP.md` | `PLANNING_SEQUENCE / NEEDS_REFRESH` |
| 현재 작업 Context | `ACTIVE_CONTEXT.md` | `CURRENT_CONTEXT_PACK / NEEDS_REFRESH` |
| 새 작업자 인계 | `HANDOFF_CONTEXT.md` | `CURRENT_HANDOFF / NEEDS_REFRESH` |
| 통합 게임 설명 | `OMENWARD_GAME_DESIGN.md` | `CURRENT_DESIGN_SUMMARY / NEEDS_REFRESH` |

---

## 3. 현재 승인 결정 ID

| Decision ID | 결정 | 책임 원본 |
|---|---|---|
| `OMW-DEC-20260731-CONTENT-MANIFEST-V1` | 시스템 조합형 콘텐츠 Manifest와 12장 미션 풀 | `design/APPROVED_VERTICAL_SLICE_CONTENT_MANIFEST_AND_MISSION_CARD_POOL_2026-07-31.md` |
| `OMW-DEC-20260731-CANON-SYNC-V1` | 주요 승인 내용을 GitHub·Sheet에 같은 ID로 즉시 동기화 | `operations/CANON_SYNC_PROTOCOL_2026-07-31.md` |
| `OMW-DEC-20260731-DEFEAT-RETRY-V1` | 기본 패배 종료와 Stage 5 이후 MapRun당 1회 영구재화 재시도 | `design/APPROVED_VERTICAL_SLICE_DEFEAT_AND_PAID_RETRY_PRINCIPLE_2026-07-31.md` |
| `OMW-DEC-20260731-DANGER-BOSS-V1` | Stage 5·10·15·20 위험 공세와 3개 보스 행동 패키지 | `design/APPROVED_VERTICAL_SLICE_DANGER_STAGE_AND_BOSS_PACKAGE_2026-07-31.md` |
| `OMW-DEC-20260731-MID-IMAGE-REVIEW-V1` | 4개 필수 기준 화면과 6개 대표 이미지의 중간 점검 게이트 | `reviews/APPROVED_MIDPOINT_IMAGE_REVIEW_GATE_2026-07-31.md` |

이전 PR 번호형·Finding형 ID는 역사 계보로 보존한다. 2026-07-31 이후 새 주요 결정은 `OMW-DEC-YYYYMMDD-<SEMANTIC-SLUG>-V<REVISION>` 형식을 기본으로 사용한다.

---

## 4. 연구·벤치마킹 경계

| 주제 | 원본 | 권한 |
|---|---|---|
| 위험 Stage·보스 패키지 벤치마킹 | `benchmarks/OMENWARD_DANGER_STAGE_AND_BOSS_PACKAGE_BENCHMARK_2026-07-31.md` | `BENCHMARK_EVIDENCE / NOT_CANON_ALONE` |
| 패배·재시도·checkpoint·메타 경량 벤치마킹 | `benchmarks/OMENWARD_DEFEAT_RETRY_CHECKPOINT_META_BENCHMARK_2026-07-31.md` | `BENCHMARK_EVIDENCE / NOT_CANON_ALONE` |
| 콘텐츠 Manifest·미션 경량 벤치마킹 | `benchmarks/OMENWARD_CONTENT_MANIFEST_AND_MISSION_CARD_BENCHMARK_2026-07-31.md` | `BENCHMARK_EVIDENCE / NOT_CANON_ALONE` |
| 룰렛 통제감·인과 Pilot | `benchmarks/OMENWARD_ROULETTE_AGENCY_EVIDENCE_PACK_2026-07-29.md` | `PILOT_RECOMMENDATION / NOT_CANON` |
| 룰렛 사람 검증 Artifact | `superpowers/plans/2026-07-29-roulette-agency-validation-artifact.md` | `HUMAN_VALIDATION_INPUT / NOT_CANON` |
| 합성 테스터 구조 | `research/OMENWARD_SYNTHETIC_TESTER_STRUCTURE_ANALYSIS_2026-07-29.md` | `T6_AI_INFERENCE / NOT_CANON` |
| 합성 위험 판정 | `research/OMENWARD_ROULETTE_AGENCY_SYNTHETIC_TESTER_REPORT_2026-07-29.md` | `SYNTHETIC_RISK_REVIEW / HUMAN_NOT_RUN` |
| 합성 세션 결과 | `research/OMENWARD_ROULETTE_AGENCY_SYNTHETIC_SESSION_EXECUTION_2026-07-29.md` | `PROMISING_DIRECTION / T6_AI_INFERENCE` |
| 합성 검증 종료 | `research/OMENWARD_ROULETTE_AGENCY_SYNTHETIC_VALIDATION_CLOSURE_2026-07-29.md` | `RESEARCH_HANDOFF / NO_IMPLEMENTATION_AUTHORITY` |

벤치마킹·Pilot·합성 검토는 승인 계약의 근거가 될 수 있지만 그 자체로 제품 정본이나 구현 권한이 아니다.

---

## 5. 세부 규칙과 역사 계보

현재 분야별 APPROVED 계약과 충돌하지 않는 범위에서 다음을 세부 규칙·결정 계보·Legacy 회귀 근거로 읽는다.

| 영역 | 세부 원본·계보 |
|---|---|
| V2 통합 결정 계보 | `design/APPROVED_CORE_V2_INTEGRATED_DECISION_LEDGER_2026-07-25.md` |
| 과거 V2 통합 명세 | `design/APPROVED_CORE_V2_INTEGRATED_SPEC.md` |
| 룰렛·이동·snapshot | `design/APPROVED_ROULETTE_CORE_RULES.md` |
| MapRun·Stage·Wave·거점 계보 | `design/APPROVED_MAPRUN_STAGE_WAVE_AND_MIDPOINT_CORE_V1.md` |
| 전설 배치 제한 계보 | `design/APPROVED_V2_LEGENDARY_DEPLOYMENT_LIMIT_2026-07-26.md` |
| 전술계획 건물 작업 | `design/APPROVED_V2_TACTICAL_PLANNING_BUILDING_WORK_CONSOLIDATED_2026-07-26.md` |
| F-30 동일시각 처리 | `design/APPROVED_V2_CONSTRUCTION_REPAIR_SAME_TIMESTAMP_ORDER_2026-07-27.md` |
| Legacy C1·C2·C3 증거 | `CURRENT_IMPLEMENTATION_STATUS.md`와 실제 run·test 증거 |

충돌 우선순위:

```text
최신 사용자 지시
→ PROJECT_CORE.md
→ 현재 질문의 최신 분야별 APPROVED 계약
→ PROJECT_CANON_DECISION_LEDGER.md
→ 기존 승인 문서
→ 과거 V2 계획·검토
→ Legacy 구현 증거
```

---

## 6. 상태 판정 규칙

```text
USER_APPROVED_PLAN
!= PRODUCT_CODE_AUTHORIZED
!= VERTICAL_SLICE_IMPLEMENTED
!= VERTICAL_SLICE_PROVEN
!= CORE_LOCK

USER_APPROVED_DETAIL
!= EXACT_COST_VALUES_APPROVED
!= META_CURRENCY_NAME_APPROVED
!= SAVE_SCHEMA_IMPLEMENTED

BENCHMARK_COMPLETE
!= DESIGN_APPROVED
!= IMPLEMENTATION_AUTHORIZED

MIDPOINT_IMAGE_REVIEW_GATE_APPROVED
!= ACTUAL_IMAGE_PROVIDED
!= IMAGE_REVIEW_RUN
!= PRODUCT_ASSET_APPROVED

CANON_SYNC_AUTHORIZED
!= PRODUCT_CODE_AUTHORIZED
!= PR_MERGE_AUTHORIZED

SYNCED_TO_PR_HEAD
!= SYNCED_TO_MAIN
```

Google Sheet에 Draft PR head를 기록할 때는 `NOT_MERGED`를 함께 표시한다. PR 병합 뒤 main SHA로 재동기화하기 전에는 `SYNCED_TO_MAIN`을 사용하지 않는다.

---

## 7. 다음 작업 라우팅

| 작업 | 먼저 읽을 책임 원본 |
|---|---|
| 새 시스템·핵심 규칙·콘텐츠 구조·UX 흐름 | Benchmark-First 원칙 → 관련 기존 정본 → 벤치마킹 근거 |
| 승인 결정 동기화 | Canon Sync Protocol → Project Core → 분야별 APPROVED 계약 → 결정 원장·Sheet |
| 콘텐츠 Manifest·미션 | 콘텐츠 Manifest 계약 → 20 Stage 계약 → 전체 시스템 계약 |
| 위험 Stage·보스 편성 | 위험 Stage·보스 계약 → 20 Stage 계약 → 콘텐츠 Manifest 계약 → 공용 적 아키타입 문서 |
| 중간 이미지 점검 | 중간 이미지 점검 게이트 → `71_이미지기획_생성목록` → `72_이미지검수_승인로그` → 실제 이미지·화면 근거 |
| 패배·checkpoint·메타 | 패배·유료 재시도 계약 → 전체 시스템 계약 → 저장 계약 계보 → Pending |
| 경제·100,000 seed 시뮬레이션 | 콘텐츠 Manifest 계약 → 룰렛·경제 세부 정본 → 별도 검증 계획 |
| UI·접근성·정보 위계 | 중간 이미지 점검 게이트 → 20 Stage 계약 → UX Evidence → `discipline.omenward-core-ux` |
| 아트·애니메이션 | 중간 이미지 점검 게이트 → 콘텐츠 Manifest 계약 → 관련 `APPROVED_ART_*` → `images/VISUAL_REFERENCE_INDEX.md` |
| Codex 구현 인계 | 전체 기획·적대적 검토·사용자 최종 승인 후 별도 실행 Issue·Plan |
| REVIEW | 영향 범위 지도 → 공격 → Finding 판정 → 수정 → 회귀 재검사 |

최종 구현·검증 상태는 항상 `CURRENT_IMPLEMENTATION_STATUS.md`와 실제 실행 증거가 소유한다.
