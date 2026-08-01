# 오멘워드 기획 정본 결정 원장

- 갱신일: `2026-08-01`
- 상태: `CURRENT_DECISION_LEDGER / PLANNING_ONLY`
- 동기화 프로토콜: `docs/operations/CANON_SYNC_PROTOCOL_2026-07-31.md`
- 연결 Sheet ID: `1VLwRtXGDtyj0JFt98wdIOtG6Zqc3wtdfCzSF9Fo6lpw`
- 제품 코드·Codex·병합: `NONE / BLOCKED / NOT_AUTHORIZED`

## 1. 현재 결정 요약

| Decision ID | 상태 | 요약 |
|---|---|---|
| `OMW-DEC-20260731-CONTENT-MANIFEST-V1` | `USER_APPROVED_PLAN` | 전장 1·4막·Stage 20·공세 8·위험 4·보스 3·미션 12 |
| `OMW-DEC-20260731-DEFEAT-RETRY-V1` | `CURRENT_PRINCIPLE / EXACT_COSTS_PENDING` | Stage 5 이후 MapRun당 최대 1회 제품 유료 Retry |
| `OMW-DEC-20260731-VISUAL-SCREEN-BOARD-V1` | `REJECTED_EVIDENCE` | 과거 잘못된 화면 보드 재사용 금지 |
| `OMW-DEC-20260801-PROJECT-INTEGRITY-GATE-V1` | `CURRENT_CANON` | 전장 `6/3/0=30` |
| `OMW-DEC-20260801-BELU-IDENTITY-V1` | `CURRENT_CANON` | 정본명 벨루, 율비는 역사 별칭 |
| `OMW-DEC-20260801-LATEST-CONTRACT-RED-TEST-V1` | `SPEC_WRITTEN_NOT_EXECUTED` | 최신 Red 명세·Legacy 테스트 판정 |
| `OMW-DEC-20260801-BASE-PROJECT-SHEET-AUDIT-V1` | `SYNC_VERIFIED` | Base·GitHub·25개 Sheet·CI 전수 감사 |
| `OMW-DEC-20260801-VISUAL-SCREEN-BOARD-V2` | `TEXT_SPEC_CURRENT / SYNC_VERIFIED / IMAGE_NOT_GENERATED` | 8개 독립 화면·공통 시각·정보 위계 |
| `OMW-DEC-20260801-ECONOMY-RETRY-SAVE-PLANNING-V1` | `STRUCTURE_CURRENT / EXACT_VALUES_PENDING / SIMULATION_NOT_RUN` | 경제 Parameter·Retry 거래·save/checkpoint·100K simulation |

## 2. 경제·Retry·save/checkpoint 결정

```yaml
decision_id: OMW-DEC-20260801-ECONOMY-RETRY-SAVE-PLANNING-V1
status: RECOMMENDED_DEFAULT_APPROVED / STRUCTURE_CURRENT / EXACT_VALUES_PENDING / PLANNING_ONLY
authority_commit: 74aec3c86c03088f334af5fe9b4a7a12ab2dcdfd
authority_path: docs/design/APPROVED_OMENWARD_ECONOMY_RETRY_SAVE_CHECKPOINT_PLANNING_CONTRACT_2026-08-01.md
parameter_registry_commit: 6f26fa32f86e2c11c4210f5fa44e223064b3e6c5
parameter_registry_path: docs/design/OMENWARD_ECONOMY_RETRY_SAVE_PARAMETER_REGISTRY_V1.json
simulation_contract_commit: fca381b74520319ee118572be13ec99e82622e0f
simulation_contract_path: docs/testing/OMENWARD_ECONOMY_META_RETRY_100K_SIMULATION_CONTRACT_2026-08-01.md
red_extension_commit: afde3b6455a9d95b87dd63c1a1c2b63c6e63d907
red_extension_path: docs/testing/OMENWARD_ECONOMY_RETRY_SAVE_RED_TEST_EXTENSION_2026-08-01.md
product_code: UNCHANGED
simulator: NOT_CREATED
simulation: NOT_RUN
exact_values: NOT_APPROVED
sheet_sync_status: PENDING
```

### 승인된 구조

```text
MapRun 경제와 Profile 경제 분리
Act 단위 비감소 유료 회전가
무료 회전 금화 = 현재 Act 유료 회전 reference cost 기준
n번째 이동 비용 = n×P
보관 병력 식량 0 / 배치 시 식량 예약
제한된 profile 시작 보관 용량 tier / 런 내 무제한 확장 금지
Stage 5+ MapRun당 1회 paid Retry
Stage 5~10=T1 / 11~15=T2 / 16~20=T3 / 0<T1<T2<T3
동일 seed·공세·미션·룰렛 RNG lineage 복원
ProfileSave / RunCheckpoint / SettingsSave / Journal / Backup 분리
안정 planning 경계 checkpoint·원자 save·last-known-good 복구
```

### 미확정 값

- 시작 골드·식량·무료 회전.
- 기본·접전지·금고 수입.
- 회전 base·Act multiplier·이동 P.
- 판매가·보관 용량·unlock 비용.
- 5건물 비용·시간·HP·Tier·수리·철거·환불률.
- 영구재화명·획득 공식·Retry T1/T2/T3.
- save schema 번호·checksum·backup 수·migration 범위.

과거 160골드·20회전가·70/50/40 환급 등은 `LEGACY_CANDIDATE_H0 / HISTORICAL_ONLY`이며 제품값이 아니다.

## 3. Screen Board V2 결정

```yaml
decision_id: OMW-DEC-20260801-VISUAL-SCREEN-BOARD-V2
status: TEXT_SPEC_CURRENT / SYNC_VERIFIED / IMAGE_NOT_GENERATED
authority_commit: 116f24bb3cbaf00b7de88ba71e77c2223d166928
verification_commit: 46744f3ff3a3ce0bdb9552759d3ed6000fbdb238
image_ids: [OM-IMG-011, OM-IMG-012, OM-IMG-013, OM-IMG-014, OM-IMG-015, OM-IMG-016, OM-IMG-017, OM-IMG-018]
visual_reference_binary_migration: PENDING
image_generation: BLOCKED
```

## 4. Red·감사 상태

```yaml
latest_red:
  authority_commit: 1aba7e9f5e3fbc4e93d0291a4a06f204d196ab7e
  test_files: NOT_CREATED
  expected_red: NOT_RUN
base_project_sheet_audit:
  authority_commit: 6882777ac42d30a8d25e621b98f9731fbe8537be
  verification_commit: e46ed794bcb5e90924362464bc3abff92deb86d1
  status: SYNC_VERIFIED
last_observed_ci:
  base_v9_adoption: PASS
  project_core_documentation: FAIL
  gdd_sheet_adoption: FAIL
```

## 5. 현재 상태

```text
CURRENT_PRODUCT: LEGACY_PROTOTYPE
LATEST_VERTICAL_SLICE: APPROVED_NOT_IMPLEMENTED
ECONOMY_RETRY_SAVE_STRUCTURE: CURRENT
EXACT_BALANCE_VALUES: NOT_APPROVED
100K_SIMULATOR_AND_RUN: NOT_CREATED / NOT_RUN
SCREEN_BOARD_V2: TEXT_CURRENT / IMAGE_NOT_GENERATED
LATEST_RED_TEST_FILES: NOT_CREATED
PRODUCT_CODE: NOT_AUTHORIZED
CODEX: BLOCKED
RUNTIME_AND_HUMAN_QA: NOT_RUN
PR_READY: NO
PR_MERGE: BLOCKED
```

## 6. 다음 작업

```text
경제·Retry·save 계약 Sheet 동기화·read-back
→ 100K simulator Work Order·Candidate H0/H1/H2
→ 시각자료 바이너리 이관·Visual Index 재검증
→ OM-IMG-013 독립 이미지 중간 검수
→ 최신 Red test Work Order·expected-failure package
→ Base v9.3 원자 migration package
→ validator Green
→ 사용자 승인 Codex 제품 구현 Plan
```

계약 작성, 시뮬레이션 실행, exact value 승인, 제품 구현은 서로 다른 상태다.