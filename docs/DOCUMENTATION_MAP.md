# 오멘워드 Documentation Map

- 갱신일: `2026-08-01`
- 현재 제품 단계: `PROTOTYPE_AND_VERTICAL_SLICE`
- 현재 Work Mode: `PLAN`
- 실행 프로필: `PLANNING_ONLY_PROFILE`
- 제품 코드 승인: `NO`
- 최신 Vertical Slice 구현: `NOT_STARTED`
- 사람 검증: `HUMAN_QA_NOT_RUN`
- 이미지 생성: `PREVIOUS_BATCH_REJECTED / NEW_GENERATION_BLOCKED`
- 활성 Base: `V9_1`
- Base v9.3: `MIGRATION_PLANNING_IN_PR_116 / NOT_ADOPTED`

이 문서는 질문별 책임 원본을 선택하는 권위 라우터다. 최신 사용자 지시와 현재 책임 원본을 우선하며, Legacy 구현·폐기 화면 보드·생성 실패 이미지를 활성 정본으로 사용하지 않는다.

---

## 1. 기본 읽기 순서

```text
최신 사용자 지시
→ AGENTS.md
→ BASE_RULES_VERSION.md
→ DOCUMENTATION_MAP.md
→ PROJECT_CORE.md
→ PROJECT_UNDERSTANDING_AND_OMISSION_PREVENTION_GATE
→ 현재 질문의 분야별 APPROVED 계약
→ PROJECT_CANON_DECISION_LEDGER.md
→ DECISIONS_PENDING.md
→ CURRENT_IMPLEMENTATION_STATUS.md
→ 실제 Scene·Script·Resource·data·tests
→ 연결 Google Sheet
→ 시각 작업이면 docs/images/VISUAL_REFERENCE_INDEX.md와 실제 이미지
→ 사실표·충돌 원장·적대적 검토
```

주요 승인 결정은 GitHub와 연결 Google Sheet에서 같은 Decision ID를 사용한다.

---

## 2. 필수 작업 게이트

| 질문 | 책임 원본 | 권한 |
|---|---|---|
| 프로젝트 이해·누락 방지 | `operations/PROJECT_UNDERSTANDING_AND_OMISSION_PREVENTION_GATE_2026-08-01.md` | `CURRENT_MANDATORY_PREFLIGHT` |
| 종합 무결성·적대적 검토 | `reviews/OMENWARD_COMPREHENSIVE_PROJECT_INTEGRITY_REVIEW_2026-08-01.md` | `CURRENT_REVIEW_EVIDENCE` |
| 사용자 승인 결정 동기화 | `operations/CANON_SYNC_PROTOCOL_2026-07-31.md` | `CURRENT_PROJECT_WORK_RULE` |
| 새 시스템·핵심 규칙·UX 구조 | `operations/BENCHMARK_FIRST_PLANNING_RULE_2026-07-31.md` | `CURRENT_PROJECT_WORK_RULE` |

P0 Finding이 열려 있으면 이미지 생성, 제품 구현, 최종 기획 승격과 Codex 인계를 중단한다.

---

## 3. 현재 활성 책임 원본

| 질문 | 책임 원본 | 권한 |
|---|---|---|
| 제품 정체성·범위·불변 조건 | `PROJECT_CORE.md` | `CURRENT_CORE_AUTHORITY` |
| 전체 시스템 Vertical Slice 관계 | `design/APPROVED_VERTICAL_SLICE_SYSTEM_CONTRACT_2026-07-27.md` | `CURRENT_USER_APPROVED_PLAN` |
| 전장 토폴로지·건설 노드 | `design/APPROVED_BATTLEFIELD_TOPOLOGY_AND_CONSTRUCTION_NODE_INVARIANTS_2026-08-01.md` | `CURRENT_USER_CONFIRMED_CANON` |
| 룰렛 물리 구조·판정·이동 | `design/APPROVED_ROULETTE_CORE_RULES.md` | `CURRENT_APPROVED_DETAIL` |
| MapRun·Stage·Wave·접전지 | `design/APPROVED_MAPRUN_STAGE_WAVE_AND_MIDPOINT_CORE_V1.md` | `APPROVED_DETAIL / LATEST_OVERRIDES_APPLY` |
| 런 시간·피로도 | `design/APPROVED_VERTICAL_SLICE_RUN_DURATION_AND_FATIGUE_CONTRACT_2026-07-31.md` | `CURRENT_USER_APPROVED_PLAN` |
| 20 Stage·4막·첫 10분 | `design/APPROVED_VERTICAL_SLICE_20_STAGE_FOUR_ACT_AND_FIRST_10_MINUTES_CONTRACT_2026-07-31.md` | `CURRENT_USER_APPROVED_PLAN` |
| 콘텐츠 Manifest·미션 카드 풀 | `design/APPROVED_VERTICAL_SLICE_CONTENT_MANIFEST_AND_MISSION_CARD_POOL_2026-07-31.md` | `CURRENT_USER_APPROVED_PLAN` |
| 위험 Stage·보스 행동 | `design/APPROVED_VERTICAL_SLICE_DANGER_STAGE_AND_BOSS_PACKAGE_2026-07-31.md` | `CURRENT_USER_APPROVED_PLAN / EXACT_VALUES_PENDING` |
| 패배·유료 재시도 | `design/APPROVED_VERTICAL_SLICE_DEFEAT_AND_PAID_RETRY_PRINCIPLE_2026-07-31.md` | `CURRENT_USER_APPROVED_DETAIL / EXACT_COSTS_PENDING` |
| 주요 Decision ID·GitHub/Sheet 위치 | `PROJECT_CANON_DECISION_LEDGER.md` | `CURRENT_DECISION_LEDGER` |
| 미확정 수치·콘텐츠 | `DECISIONS_PENDING.md` | `PENDING_ONLY` |
| 구현·Legacy·미검증 경계 | `CURRENT_IMPLEMENTATION_STATUS.md` | `CURRENT_IMPLEMENTATION_AUTHORITY / NEEDS_REFRESH` |
| 연결 Google Sheet 계약 | `PROJECT_GOOGLE_SHEET_WORKBOOK.md` | `USER_FACING_GDD_WORKSPACE_CONTRACT` |

---

## 4. 비주얼·화면 작업 라우팅

| 질문 | 책임 원본 | 현재 상태 |
|---|---|---|
| 시각자료 상태·참고/금지 요소 | `docs/images/VISUAL_REFERENCE_INDEX.md` | `CURRENT_VISUAL_REFERENCE_ROUTER` |
| 중간 이미지 점검 절차 | `reviews/APPROVED_MIDPOINT_IMAGE_REVIEW_GATE_2026-07-31.md` | `WORKFLOW_RETAINED / CURRENT_BATCH_REJECTED / RESET_REQUIRED` |
| 2026-07-31 화면 명세 보드 | `design/OMENWARD_VISUAL_SITUATIONAL_INGAME_SCREEN_SPEC_BOARD_2026-07-31.md` | `REJECTED_EVIDENCE / DO_NOT_REUSE` |
| 새 화면 보드 | 미작성 | `BLOCKED_PENDING_FACT_MATRIX_AND_BRIEF_APPROVAL` |

정확한 시각자료 인덱스 경로는 `docs/images/VISUAL_REFERENCE_INDEX.md`다. 과거의 `images/VISUAL_REFERENCE_INDEX.md` 표기는 잘못된 경로다.

이미지 생성 전 읽기 순서:

```text
Project Understanding Gate
→ Battlefield Topology Contract
→ Roulette Core Rules
→ Current Implementation Status
→ docs/images/VISUAL_REFERENCE_INDEX.md
→ 사용자 제공 실제 이미지
→ 화면별 독립 브리프
→ 사용자 확인
→ 생성
→ Sheet 검수 로그
```

---

## 5. 현재 결정 ID

| Decision ID | 결정 | 책임 원본 |
|---|---|---|
| `OMW-DEC-20260731-CONTENT-MANIFEST-V1` | 시스템 조합형 콘텐츠 Manifest와 12장 미션 풀 | 콘텐츠 Manifest 계약 |
| `OMW-DEC-20260731-CANON-SYNC-V1` | GitHub·Sheet 즉시 정본 동기화 | Canon Sync Protocol |
| `OMW-DEC-20260731-DEFEAT-RETRY-V1` | Stage 5 이후 MapRun당 1회 영구재화 재시도 | 패배·재시도 계약 |
| `OMW-DEC-20260731-DANGER-BOSS-V1` | Stage 5·10·15·20 위험 공세·보스 패키지 | 위험 Stage 계약 |
| `OMW-DEC-20260731-MID-IMAGE-REVIEW-V1` | 중간 이미지 검수 절차 | 현재 배치 폐기·게이트 재설정 |
| `OMW-DEC-20260731-VISUAL-SCREEN-BOARD-V1` | 과거 화면 보드 | `REJECTED_EVIDENCE` |
| `OMW-DEC-20260801-PROJECT-INTEGRITY-GATE-V1` | 사실표·충돌 원장·누락 방지·전장 노드 불변 계약 | 2026-08-01 게이트·검토·토폴로지 문서 |

---

## 6. 상태 판정 규칙

```text
CURRENT_CANON != CURRENT_IMPLEMENTATION
LEGACY_PROVEN != LATEST_PROVEN
USER_APPROVED_PLAN != PRODUCT_CODE_AUTHORIZED
TEXT_WIREFRAME != VALID_VISUAL_SPEC
GENERATED_IMAGE != APPROVED_ASSET
REJECTED_EVIDENCE != NOT_CREATED
MIGRATION_PLANNED != MIGRATION_ADOPTED
SYNCED_TO_PR_HEAD != SYNCED_TO_MAIN
```

- 활성 Base는 `BASE_RULES_VERSION.md`가 소유한다.
- PR #116의 Base v9.3 문서는 마이그레이션 계획이며 활성 Adapter 전환이나 채택 완료가 아니다.
- 최신 구현 상태는 실제 Scene·Script·Resource·tests와 fresh 실행 증거가 소유한다.

---

## 7. Legacy 해석

현재 실행되는 C1·C2·C3는 보존 가능한 seam을 가진 Legacy 증거다.

| Legacy | 보존 후보 | 최신 교체 필요 |
|---|---|---|
| C1 룰렛 | 중앙 판정·완성선·금화 resolver | 독립 9칸 → 세 물리 릴·SpinSnapshot·이동 |
| C2 전장 | 3라인·구조물 피해·승패 | capture_power·구형 outpost lifecycle·본진 노드 부재 |
| C3 UX | snapshot→HUD·원인 보고 | 기술 Label HUD·구형 확률/시간 의미 |
| Retry | 개발용 Stage restart seam | 제품 영구재화 1회 Retry와 분리 |

Legacy 기능이 실행된다는 사실을 최신 Vertical Slice 구현 완료로 표시하지 않는다.

---

## 8. 다음 작업 라우팅

| 작업 | 먼저 읽을 책임 원본 |
|---|---|
| 전장·노드 기획 | Project Understanding Gate → Battlefield Topology Contract → 전체 시스템 계약 → 실제 BattleSimulator/BuildingService |
| 룰렛 기획 | Project Understanding Gate → Roulette Core Rules → 실제 RouletteService/tests |
| UI·화면·이미지 | Project Understanding Gate → Topology → Roulette → Visual Reference Index → 사용자 이미지 → 독립 브리프 |
| 패배·checkpoint·메타 | Project Understanding Gate → 패배·재시도 계약 → 저장 계보 → Pending |
| 콘텐츠·위험 Stage | Benchmark-First → 20 Stage 계약 → 콘텐츠 Manifest → 위험 Stage 계약 |
| Codex 구현 인계 | 사실표·충돌 원장 PASS → 사용자 승인 Plan → Red tests → 별도 실행 Issue |
| REVIEW | 영향 범위 지도 → 공격 → Finding → 수정 → GitHub·Sheet·실제 파일 재조회 |

현재 새 이미지 생성, 제품 코드 변경, Codex 실행과 PR 병합은 승인되지 않았다.