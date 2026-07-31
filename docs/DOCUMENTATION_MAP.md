# 오멘워드 Documentation Map

- 갱신일: `2026-08-01`
- 현재 Work Mode: `PLAN / PLANNING_ONLY_PROFILE`
- 현재 제품: `LEGACY_PROTOTYPE`
- 최신 Vertical Slice: `NOT_IMPLEMENTED`
- 제품 코드·Codex·병합: `NOT_AUTHORIZED / BLOCKED`
- 이미지: `PREVIOUS_BATCH_REJECTED / NEW_GENERATION_BLOCKED`
- 활성 Base: `v9.1`
- Base v9.3: `MIGRATION_PLANNING_IN_PR_116 / NOT_ADOPTED`

이 문서는 질문별 책임 원본을 선택하는 권위 라우터다. 최신 사용자 지시와 현재 책임 원본을 우선하며 Legacy 구현·폐기 화면 보드·생성 실패 이미지를 활성 정본으로 사용하지 않는다.

## 1. 기본 읽기 순서

```text
최신 사용자 지시
→ AGENTS.md
→ BASE_RULES_VERSION.md
→ DOCUMENTATION_MAP.md
→ PROJECT_CORE.md
→ Project Understanding Gate
→ 질문 분야의 최신 APPROVED 계약
→ PROJECT_CANON_DECISION_LEDGER.md
→ DECISIONS_PENDING.md
→ CURRENT_IMPLEMENTATION_STATUS.md
→ 실제 Scene·Script·Resource·data·tests
→ 연결 Google Sheet
→ 시각 작업이면 Visual Reference Index와 실제 이미지
→ 사실표·충돌 원장·적대적 검토
```

## 2. 필수 작업 게이트

| 질문 | 책임 원본 | 권한 |
|---|---|---|
| 프로젝트 이해·누락 방지 | `operations/PROJECT_UNDERSTANDING_AND_OMISSION_PREVENTION_GATE_2026-08-01.md` | `CURRENT_MANDATORY_PREFLIGHT` |
| 종합 무결성·적대적 검토 | `reviews/OMENWARD_COMPREHENSIVE_PROJECT_INTEGRITY_REVIEW_2026-08-01.md` | `CURRENT_REVIEW_EVIDENCE` |
| 승인 결정 동기화 | `operations/CANON_SYNC_PROTOCOL_2026-07-31.md` | `CURRENT_PROJECT_WORK_RULE` |
| 새 시스템·핵심 규칙·UX | `operations/BENCHMARK_FIRST_PLANNING_RULE_2026-07-31.md` | `CURRENT_PROJECT_WORK_RULE` |

열린 P0는 이미지 생성·제품 구현·최종 기획 승격·Codex 인계를 차단한다. 열린 P1은 관련 영역 작업을 차단한다.

## 3. 현재 활성 책임 원본

| 질문 | 책임 원본 | 권한 |
|---|---|---|
| 제품 정체성·범위·불변 조건 | `PROJECT_CORE.md` | `CURRENT_CORE_AUTHORITY` |
| 전체 시스템 관계 | `design/APPROVED_VERTICAL_SLICE_SYSTEM_CONTRACT_2026-07-27.md` | `CURRENT_USER_APPROVED_PLAN` |
| 전장 토폴로지·건설 노드 | `design/APPROVED_BATTLEFIELD_TOPOLOGY_AND_CONSTRUCTION_NODE_INVARIANTS_2026-08-01.md` | `CURRENT_USER_CONFIRMED_CANON` |
| 룰렛 물리 구조·판정·이동 | `design/APPROVED_ROULETTE_CORE_RULES.md` | `CURRENT_APPROVED_DETAIL` |
| MapRun·Stage·접전지 | `design/APPROVED_MAPRUN_STAGE_WAVE_AND_MIDPOINT_CORE_V1.md` | `APPROVED_DETAIL / LATEST_OVERRIDES_APPLY` |
| 런 시간·피로도 | `design/APPROVED_VERTICAL_SLICE_RUN_DURATION_AND_FATIGUE_CONTRACT_2026-07-31.md` | `CURRENT_USER_APPROVED_PLAN` |
| 20 Stage·4막·첫 10분 | `design/APPROVED_VERTICAL_SLICE_20_STAGE_FOUR_ACT_AND_FIRST_10_MINUTES_CONTRACT_2026-07-31.md` | `CURRENT_USER_APPROVED_PLAN` |
| 콘텐츠 Manifest·미션 | `design/APPROVED_VERTICAL_SLICE_CONTENT_MANIFEST_AND_MISSION_CARD_POOL_2026-07-31.md` | `CURRENT_USER_APPROVED_PLAN` |
| 위험 Stage·보스 | `design/APPROVED_VERTICAL_SLICE_DANGER_STAGE_AND_BOSS_PACKAGE_2026-07-31.md` | `CURRENT_USER_APPROVED_PLAN / EXACT_VALUES_PENDING` |
| 패배·유료 재시도 | `design/APPROVED_VERTICAL_SLICE_DEFEAT_AND_PAID_RETRY_PRINCIPLE_2026-07-31.md` | `CURRENT_USER_APPROVED_DETAIL / EXACT_COSTS_PENDING` |
| 안내자 정체성·명칭 | `design/APPROVED_BELU_GUIDE_IDENTITY_AND_NAMING_CONTRACT_2026-08-01.md` | `CURRENT_USER_CONFIRMED_CANON` |
| Decision·GitHub/Sheet 위치 | `PROJECT_CANON_DECISION_LEDGER.md` | `CURRENT_DECISION_LEDGER` |
| 미확정 수치·콘텐츠 | `DECISIONS_PENDING.md` | `PENDING_ONLY` |
| 실제 구현·Legacy 경계 | `CURRENT_IMPLEMENTATION_STATUS.md` | `CURRENT_IMPLEMENTATION_AUTHORITY` |
| 연결 Google Sheet 계약 | `PROJECT_GOOGLE_SHEET_WORKBOOK.md` | `USER_FACING_GDD_WORKSPACE_CONTRACT` |

## 4. 벨루 명칭 라우팅

```text
CANONICAL_NAME_KO = 벨루
CANONICAL_NAME_EN = Belu
HISTORICAL_ALIAS = 율비
IDENTITY_RELATION = SAME_CHARACTER
```

- 신규 기획·UI·대사·에셋·데이터·파일명은 `벨루 / Belu / belu`를 사용한다.
- `율비`는 과거 `요정 율비 시안.png` 파일명과 변경 이력에서만 역사 별칭으로 보존한다.
- 안내자 역할·시각 승인 범위는 벨루 계약과 Visual Reference Index를 함께 읽는다.

## 5. 비주얼·화면 작업 라우팅

| 질문 | 책임 원본 | 현재 상태 |
|---|---|---|
| 시각자료 상태·참고/금지 요소 | `docs/images/VISUAL_REFERENCE_INDEX.md` | `CURRENT_VISUAL_REFERENCE_ROUTER` |
| 벨루 정체성·명칭 | `design/APPROVED_BELU_GUIDE_IDENTITY_AND_NAMING_CONTRACT_2026-08-01.md` | `RESOLVED / BELU_CANON` |
| 중간 이미지 점검 절차 | `reviews/APPROVED_MIDPOINT_IMAGE_REVIEW_GATE_2026-07-31.md` | `WORKFLOW_RETAINED / CURRENT_BATCH_REJECTED` |
| 과거 화면 보드 V1 | `design/OMENWARD_VISUAL_SITUATIONAL_INGAME_SCREEN_SPEC_BOARD_2026-07-31.md` | `REJECTED_EVIDENCE / DO_NOT_REUSE` |
| 새 화면 보드 V2 | 미작성 | `BLOCKED_PENDING_RED_TEST_SPEC_AND_BRIEF_APPROVAL` |

이미지 생성 전 순서:

```text
Project Understanding Gate
→ Battlefield Topology Contract
→ Roulette Core Rules
→ Belu Identity Contract
→ Current Implementation Status
→ Visual Reference Index
→ 사용자 제공 실제 이미지
→ 화면별 독립 브리프
→ 사용자 확인
→ 생성
→ 검수 로그·Sheet 동기화
```

## 6. 현재 Decision ID

| Decision ID | 결정 | 상태 |
|---|---|---|
| `OMW-DEC-20260731-CONTENT-MANIFEST-V1` | 콘텐츠 Manifest·미션 풀 | `USER_APPROVED_PLAN` |
| `OMW-DEC-20260731-CANON-SYNC-V1` | GitHub·Sheet 정본 동기화 | `CURRENT_WORK_RULE` |
| `OMW-DEC-20260731-DEFEAT-RETRY-V1` | 유료 재시도 | `USER_APPROVED_DETAIL` |
| `OMW-DEC-20260731-DANGER-BOSS-V1` | 위험 Stage·보스 | `USER_APPROVED_PLAN` |
| `OMW-DEC-20260731-MID-IMAGE-REVIEW-V1` | 이미지 검수 절차 | `WORKFLOW_RETAINED / BATCH_REJECTED` |
| `OMW-DEC-20260731-VISUAL-SCREEN-BOARD-V1` | 과거 화면 보드 | `REJECTED_EVIDENCE` |
| `OMW-DEC-20260801-PROJECT-INTEGRITY-GATE-V1` | 사실표·충돌 원장·6/3/0=30 | `CURRENT_WORK_RULE` |
| `OMW-DEC-20260801-BELU-IDENTITY-V1` | 벨루·율비 동일 인물, 벨루 통일 | `CURRENT_USER_CONFIRMED_CANON` |

## 7. 상태 판정 규칙

```text
CURRENT_CANON != CURRENT_IMPLEMENTATION
LEGACY_PROVEN != LATEST_PROVEN
USER_APPROVED_PLAN != PRODUCT_CODE_AUTHORIZED
GENERATED_IMAGE != APPROVED_ASSET
REJECTED_EVIDENCE != NOT_CREATED
MIGRATION_PLANNED != MIGRATION_ADOPTED
SYNCED_TO_PR_HEAD != SYNCED_TO_MAIN
HISTORICAL_ALIAS != CURRENT_CANONICAL_NAME
```

## 8. Legacy 해석

| Legacy | 보존 후보 | 최신 교체 필요 |
|---|---|---|
| C1 룰렛 | 중앙 판정·완성선·금화 resolver | 독립 9칸 → 세 물리 릴·snapshot·이동 |
| C2 전장 | 3라인·구조물 피해·승패 | capture_power·본진 노드 부재·30노드 미구현 |
| C3 UX | snapshot→HUD·원인 보고 | 기술 Label HUD·제품 화면 부재 |
| Retry | 개발용 Stage restart seam | 제품 유료 1회 Retry와 분리 |

## 9. 다음 작업 라우팅

| 순서 | 작업 | 선행 책임 원본 |
|---:|---|---|
| 1 | 최신 계약 Red 테스트 명세 | Project Core → Integrity Gate → 실제 Legacy tests |
| 2 | 화면 명세 보드 V2 | 승인 Red 테스트 명세 → Topology → Roulette → Belu → Visual Index |
| 3 | 대표 화면 중간 검수 | 화면별 독립 브리프 → 사용자 확인 |
| 4 | 경제·Retry 비용·저장 schema | Benchmark-First → Pending → 시뮬레이션 계획 |
| 5 | Codex 구현 Plan | 열린 관련 P1 해소 → 사용자 최종 승인 → Red tests |

현재 제품 코드 변경, Codex 실행, 새 이미지 생성과 PR 병합은 승인되지 않았다.
