# 오멘워드 Documentation Map

- 갱신일: `2026-08-01`
- Work Mode: `PLAN / PLANNING_ONLY_PROFILE`
- 현재 제품: `LEGACY_PROTOTYPE`
- 최신 Vertical Slice: `APPROVED / NOT_IMPLEMENTED`
- 제품 코드·Codex: `NOT_AUTHORIZED / BLOCKED`
- PR: `#116 DRAFT / OPEN / NOT_MERGED`
- 마지막 관찰 CI: `BASE_ADOPTION_PASS / PROJECT_CORE_FAIL / GDD_SHEET_FAIL`
- 화면: `SCREEN_BOARD_V2_TEXT_CURRENT / IMAGE_GENERATION_BLOCKED`
- 경제·Retry·저장: `STRUCTURE_CURRENT / EXACT_VALUES_PENDING / SIMULATION_NOT_RUN`
- 활성 Base: `v9.1`
- 권장 다음 Base: `v9.3 / SEPARATE_ATOMIC_MIGRATION`

이 문서는 질문별 책임 원본을 선택하는 권위 라우터다. Legacy 구현·폐기 화면·구형 수치·과거 실행 계획은 현재 제품 정본이 아니다.

## 1. 기본 읽기 순서

```text
최신 사용자 지시
→ AGENTS.md
→ BASE_RULES_VERSION.md
→ DOCUMENTATION_MAP.md
→ PROJECT_CORE.md
→ Project Understanding Gate
→ Base·프로젝트·Sheet 전수 감사
→ 질문 분야의 최신 APPROVED 계약
→ PROJECT_CANON_DECISION_LEDGER.md
→ DECISIONS_PENDING.md
→ CURRENT_IMPLEMENTATION_STATUS.md
→ 실제 Scene·Script·Resource·data·tests
→ 연결 Google Sheet
→ 적대적 검토
```

## 2. 필수 작업 게이트

| 질문 | 책임 원본 | 상태 |
|---|---|---|
| 프로젝트 이해·누락 방지 | `operations/PROJECT_UNDERSTANDING_AND_OMISSION_PREVENTION_GATE_2026-08-01.md` | `CURRENT_MANDATORY_PREFLIGHT` |
| Base·GitHub·Sheet 전체 상태 | `audits/OMENWARD_BASE_PROJECT_SHEET_REPOSITORY_WIDE_AUDIT_2026-08-01.md` | `SYNC_VERIFIED` |
| 승인 결정 동기화 | `operations/CANON_SYNC_PROTOCOL_2026-07-31.md` | `CURRENT_PROJECT_WORK_RULE` |
| 최신 구현 전 Red 계약 | `testing/LATEST_VERTICAL_SLICE_RED_TEST_SPEC_2026-08-01.md` | `SPEC_WRITTEN_NOT_EXECUTED` |
| 경제·Retry·저장 Red 확장 | `testing/OMENWARD_ECONOMY_RETRY_SAVE_RED_TEST_EXTENSION_2026-08-01.md` | `TEST_FILES_NOT_CREATED` |
| Legacy 테스트 마이그레이션 | `testing/LEGACY_TEST_PRESERVE_REPLACE_RETIRE_MATRIX_2026-08-01.md` | `CURRENT_MIGRATION_TEST_AUTHORITY` |
| Base v9.3 프로젝트 적용 | `operations/VERTICAL_SLICE_V9_APPLICATION.md` | `MIGRATION_NOT_EXECUTED` |

## 3. 현재 활성 책임 원본

| 질문 | 책임 원본 | 권한 |
|---|---|---|
| 제품 정체성·범위·불변 조건 | `PROJECT_CORE.md` | `CURRENT_CORE_AUTHORITY` |
| 전체 시스템 관계 | `design/APPROVED_VERTICAL_SLICE_SYSTEM_CONTRACT_2026-07-27.md` | `CURRENT_USER_APPROVED_PLAN` |
| 전장 토폴로지·건설 노드 | `design/APPROVED_BATTLEFIELD_TOPOLOGY_AND_CONSTRUCTION_NODE_INVARIANTS_2026-08-01.md` | `CURRENT_CANON` |
| 세 물리 릴·판정·이동 | `design/APPROVED_ROULETTE_CORE_RULES.md` | `CURRENT_APPROVED_DETAIL` |
| 런·Stage·콘텐츠 | 2026-07-31 관련 APPROVED 계약 | `CURRENT_USER_APPROVED_PLAN` |
| 위험 Stage·보스 | `design/APPROVED_VERTICAL_SLICE_DANGER_STAGE_AND_BOSS_PACKAGE_2026-07-31.md` | `EXACT_VALUES_PENDING` |
| 제품 Retry 상위 원칙 | `design/APPROVED_VERTICAL_SLICE_DEFEAT_AND_PAID_RETRY_PRINCIPLE_2026-07-31.md` | `CURRENT_APPROVED_DETAIL / EXACT_COSTS_PENDING` |
| 경제·Retry·save/checkpoint 구조 | `design/APPROVED_OMENWARD_ECONOMY_RETRY_SAVE_CHECKPOINT_PLANNING_CONTRACT_2026-08-01.md` | `STRUCTURE_CURRENT / EXACT_VALUES_PENDING` |
| 경제 Parameter ID·상태 | `design/OMENWARD_ECONOMY_RETRY_SAVE_PARAMETER_REGISTRY_V1.json` | `MACHINE_READABLE_CURRENT / NULL_NOT_APPROVED` |
| 100K 시뮬레이션 | `testing/OMENWARD_ECONOMY_META_RETRY_100K_SIMULATION_CONTRACT_2026-08-01.md` | `CONTRACT_CURRENT / NOT_RUN` |
| 안내자 벨루 | `design/APPROVED_BELU_GUIDE_IDENTITY_AND_NAMING_CONTRACT_2026-08-01.md` | `CURRENT_CANON` |
| 화면 구조·정보 위계 | `design/APPROVED_OMENWARD_VISUAL_SCREEN_BOARD_V2_TEXT_SPEC_2026-08-01.md` | `TEXT_SPEC_CURRENT / SYNC_VERIFIED` |
| 개별 화면 브리프 | `design/screen-briefs/OMENWARD_SCREEN_BRIEF_OM_IMG_011...018_2026-08-01.md` | `TEXT_BRIEF_CURRENT` |
| 시각자료 상태 | `images/VISUAL_REFERENCE_INDEX.md` | `MIGRATION_PENDING` |
| 최신 Red 테스트 | `testing/LATEST_VERTICAL_SLICE_RED_TEST_SPEC_2026-08-01.md` | `TEST_FILES_NOT_CREATED` |
| 전체 감사·다음 순서 | `audits/OMENWARD_BASE_PROJECT_SHEET_REPOSITORY_WIDE_AUDIT_2026-08-01.md` | `CURRENT_REPOSITORY_WIDE_AUDIT` |
| 현재 상태 압축 | `ACTIVE_CONTEXT.md` | `CURRENT_ACTIVE_CONTEXT` |
| Decision·GitHub/Sheet 위치 | `PROJECT_CANON_DECISION_LEDGER.md` | `CURRENT_DECISION_LEDGER` |
| 미확정 수치·콘텐츠 | `DECISIONS_PENDING.md` | `PENDING_ONLY` |
| 실제 구현·Legacy 경계 | `CURRENT_IMPLEMENTATION_STATUS.md` | `CURRENT_IMPLEMENTATION_AUTHORITY` |
| 연결 Google Sheet | `PROJECT_GOOGLE_SHEET_WORKBOOK.md` | `USER_FACING_GDD_WORKSPACE_CONTRACT` |

## 4. 경제·Retry·저장 라우팅

```text
APPROVED_STRUCTURE
- MapRun 경제와 Profile 경제 분리
- Act 단위 비감소 유료 회전가 구조
- 무료 회전 금화는 현재 Act 유료 회전 reference cost 사용
- 이동 비용 n×P
- 보관 식량 0 / 배치 시 식량 예약
- 제한된 profile 시작 보관 용량 tier
- Stage 5+ MapRun당 1회 paid Retry
- T1<T2<T3
- 동일 seed·manifest·RNG lineage checkpoint 복원
- ProfileSave / RunCheckpoint / Settings / Journal / Backup 분리
- 안정 planning 경계 checkpoint·원자 save·복구

PENDING_EXACT_VALUES
- 시작 자원·수입·금고·접전지 수입
- 회전 base·Act multiplier·이동 P
- 판매가·보관 용량·unlock 비용
- 5건물 비용·시간·HP·수리·철거·환불률
- 영구재화명·획득 공식·Retry T1/T2/T3
- save schema 번호·checksum·backup 수·migration 범위
```

`null` Registry 값은 구현 default가 아니다. 과거 160골드·20회전가·70/50/40 환급 등은 `LEGACY_CANDIDATE_H0 / HISTORICAL_ONLY`다.

## 5. Screen Board V2 라우팅

```text
OM-IMG-011 메인·런 진입
OM-IMG-012 Stage 준비·공세·건설
OM-IMG-013 세 물리 릴 설계
OM-IMG-014 PendingReward·보관·판매·배치
OM-IMG-015 일반 세 라인 전투
OM-IMG-016 Stage 15 경계파쇄자
OM-IMG-017 Stage 정산·인과 복기
OM-IMG-018 패배·제품 유료 Retry
```

이미지 생성은 시각자료 바이너리 이관·Index 재검증 전 차단한다.

## 6. Base·역사 라우팅

```text
CURRENT_PROJECT_BASE=v9.1
NEXT_RECOMMENDED_BASE=v9.3
BASE_RELEASED != PROJECT_ADOPTED
```

- Base v9.3은 별도 원자 migration package에서만 적용한다.
- PR #92/#97·F-30·C1/C2/C3 proof·과거 경제 수치는 역사 계보다.
- V1과 OM-IMG-005~010은 `REJECTED_EVIDENCE / DO_NOT_REUSE`다.

## 7. 현재 Decision

| Decision ID | 결정 | 상태 |
|---|---|---|
| `OMW-DEC-20260801-PROJECT-INTEGRITY-GATE-V1` | 사실표·6/3/0=30 | `CURRENT_CANON` |
| `OMW-DEC-20260801-BELU-IDENTITY-V1` | 벨루 명칭 | `CURRENT_CANON` |
| `OMW-DEC-20260801-LATEST-CONTRACT-RED-TEST-V1` | Red 명세·Legacy 판정 | `SPEC_WRITTEN_NOT_EXECUTED` |
| `OMW-DEC-20260801-BASE-PROJECT-SHEET-AUDIT-V1` | Base·GitHub·Sheet 감사 | `SYNC_VERIFIED` |
| `OMW-DEC-20260801-VISUAL-SCREEN-BOARD-V2` | 8개 화면 계약 | `TEXT_SPEC_CURRENT / SYNC_VERIFIED / IMAGE_NOT_GENERATED` |
| `OMW-DEC-20260801-ECONOMY-RETRY-SAVE-PLANNING-V1` | 경제 Parameter·Retry 거래·save/checkpoint·100K simulation | `STRUCTURE_CURRENT / EXACT_VALUES_PENDING / NOT_RUN` |

## 8. 상태 판정

```text
CURRENT_CANON != CURRENT_IMPLEMENTATION
STRUCTURE_CURRENT != EXACT_VALUES_APPROVED
SIMULATION_CONTRACT_WRITTEN != SIMULATION_RUN
TEXT_SPEC_CURRENT != IMAGE_GENERATED
RED_SPEC_WRITTEN != RED_TESTS_CREATED
CI_PARTIAL_FAILURE != VALIDATED
```

## 9. 다음 작업

```text
경제·Retry·save 계약 GitHub·Sheet read-back
→ 100K simulator Work Order·Candidate H0/H1/H2
→ 시각자료 바이너리 이관·Visual Index 재검증
→ OM-IMG-013 독립 이미지 중간 검수
→ 최신 Red test Work Order·expected-failure package
→ Base v9.3 원자 migration package
→ validator Green
→ 사용자 승인 Codex 제품 구현 Plan
```

제품 코드 변경, Codex 실행, 시뮬레이션 실행, 이미지 생성, PR ready/merge는 현재 범위에 포함되지 않는다.