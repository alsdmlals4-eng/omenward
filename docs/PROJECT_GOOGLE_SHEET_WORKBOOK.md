# [현행] OMENWARD 프로젝트 Google Sheets Workbook

```yaml
updated_at: 2026-08-05
spreadsheet_id: 1VLwRtXGDtyj0JFt98wdIOtG6Zqc3wtdfCzSF9Fo6lpw
spreadsheet_title: 오멘워드(OMENWARD)
workspace_role: USER_FACING_GDD_WORKSPACE
change_protocol: PROPOSED_SHEET_CHANGE
sheet_status: PROJECT_SHEET_CONFIGURED
current_decision: OMW-DEC-20260805-PLANNING-TROOP-ROLES-SYNERGIES-AND-COUNTERS-V1
current_process_policy: OMW-PROC-20260805-BENCHMARK-TDD-APPROVAL-BATCH-V1
current_main: RESOLVE_FROM_REPOSITORY_DEFAULT_BRANCH
current_grill_me_count: 4_OF_10
product_code_authority: NONE
art_asset_production_authority: NONE
image_generation: STOPPED_BY_USER
```

## 1. 역할

GitHub의 `[현행]` 책임 원본이 기획 정본이며 Sheet는 사용자 가시 GDD·근거·감사 Workspace다. 승인 변경은 같은 Decision ID와 exact PR HEAD로 반영한다.

## 2. 이번 Decision Sheet 계약

Decision:

`OMW-DEC-20260805-PLANNING-TROOP-ROLES-SYNERGIES-AND-COUNTERS-V1`

```text
ROSTER_BASELINE = 10
ROSTER_COUNT_IS_NOT_SACRED
ROSTER_MIN_MAX = NOT_PRESET
```

기준선:

```text
방패수호병 / 대검병 / 창병 / 궁수 / 마도사
사제 / 암살자 / 기병 / 비행병 / 거인
```

병종 수 증감은 역할 공백·중복·룰렛 학습량·보관함 복잡도·아트 제작비를 근거로 별도 승인한다.

## 3. 압력·시너지 Sheet 계약

| 압력 | 주 대응 | 보조 |
|---|---|---|
| MASS | 대검병·마도사 | 방패수호병 |
| ARMORED | 마도사·창병 | 거인 |
| FLYING | 궁수·비행병 | 요격탑·후속 전술 |
| INFILTRATION | 암살자·기병 | 후방 방패수호병 |
| SIEGE | 창병·기병/암살자 | 거인 역공 |

- 압력별 최소 두 병종 대응 경로와 건물·전술 대안을 둔다.
- 단일 하드키 병종은 금지한다.
- 시너지는 관찰 가능한 전장 행동 연결이다.
- 단순 병종 세트 보너스는 기본 문법으로 사용하지 않는다.
- 병종 하나가 다섯 압력 모두에서 최적이면 역할 또는 포기 비용을 재설계한다.

## 4. 병영·Tier·자산 Sheet 계약

```text
전열 병영 가중 = 방패수호병 / 대검병 / 창병 / 거인
기동 병영 가중 = 궁수 / 암살자 / 기병 / 비행병
공통 지원 = 마도사 / 사제
반대 계열 영구 삭제 = FORBIDDEN
```

```text
T1 병종 토큰 = 실제 T1 인게임 이미지
T2 병종 토큰 = 실제 T2 인게임 이미지
T3 병종 토큰 = FORBIDDEN
결과 Preview = 실제 지급 병종 이미지
```

정확한 가중치·승급 비용·체력·공격력·관통·회복·속도는 `PENDING_SIMULATION`이다.

## 5. 수명주기 Sheet 계약

```text
[현행] = CURRENT_AUTHORITY
[대체됨] = SUPERSEDED_HISTORY_ONLY
[보류] = HELD_NO_IMPLEMENTATION_INPUT
[폐기] = REJECTED_NO_USE
[증거] = EVIDENCE_ONLY
```

```text
[증거] data/units/*.tres
status = LEGACY_PROTOTYPE_UNIT_DATA
IMPLEMENTATION_INPUT_FORBIDDEN
```

구형 병종 `.tres`는 과거 프로토타입 존재만 증명하며 Decision 5/10·수치 시뮬레이션·Codex 구현 계획 전 신규 구현 입력으로 사용하지 않는다.

## 6. 운영 정책 Sheet 계약

```text
BENCHMARK_REQUIRED
INDUSTRY_COMPARISON_REQUIRED
MAX_APPROVAL_BATCH = 10
EARLY_CHECKPOINT = HIGH_RISK_CONFLICT / SESSION_END / LARGE_CANON_IMPACT
TDD = RED → GREEN → REFACTOR
EXPLICIT_BRANCH_REQUIRED_FOR_GITHUB_MUTATION
DIRECT_MAIN_WRITE = FORBIDDEN
```

- 4/10 RED는 Project Core Documentation run 922다.
- GREEN·REFACTOR run 번호와 exact head는 최종 PR 검증 뒤 기록한다.

## 7. 탭별 반영

| 탭 | 반영 내용 |
|---|---|
| `00_프로젝트_허브` | Decision 4/10·exact PR HEAD·다음 전술 Gate |
| `01_작업순서` | 병종 정본·TDD·다음 작업 |
| `02_현재_확정결정` | 10종 기준선·비고정 수량·수치 경계 |
| `03_근거_라이브러리` | 공식 벤치마크·Stage·건물·Legacy 프로토타입 근거 |
| `04_누락_충돌_감사` | `OMW-AUD-420~443` |
| `05_GDD_요약` | 역할·압력·시너지·4/10 |
| `12_핵심루프` | 공세→병영/룰렛→비가역 배치→행동 시너지 복기 |
| `15_조작_게임규칙` | Layer·Route·배치 후 이동 금지·병종 정보 공개 |
| `40_핵심시스템_메인콘텐츠` | 10종 기준선·병영 가중·압력 대응 |
| `50_메인콘텐츠` | Stage 압력×병종 역할 의존성 |
| `99_변경이력` | Decision·RED/GREEN·lifecycle·PR 기록 |

## 8. Bounded Read-Back

쓰기 후 다음을 재조회한다.

- Decision ID와 exact PR HEAD.
- counter `4/10`.
- 10종 기준선과 `ROSTER_COUNT_IS_NOT_SACRED / ROSTER_MIN_MAX_NOT_PRESET`.
- 다섯 압력과 최소 두 병종 경로.
- 행동 기반 시너지와 단순 세트 보너스 금지.
- 병영 가중과 반대 계열 영구 삭제 금지.
- T1/T2 실제 자산 재사용과 T3 토큰 금지.
- lifecycle `LEGACY_PROTOTYPE_UNIT_DATA / IMPLEMENTATION_INPUT_FORBIDDEN`.
- 감사 `OMW-AUD-420~443`.
- 다음 Decision `OMW-DEC-20260805-PLANNING-TACTICAL-SKILLS-AND-MANA-V1`.
- 제품 코드·데이터·아트 자산 미변경.

일치 전에는 `READBACK_PASS`를 기록하지 않는다.

## 9. 필수 CI·차단 검색

```text
Validate Project Core Documentation
Validate Omenward GDD Sheet Adoption
Validate Omenward Core
Validate Base v9 adoption
```

모두 exact PR HEAD에서 success여야 한다.

`04_누락_충돌_감사` 실제 데이터 행에 다음이 없어야 한다.

```text
OPEN_P0
OPEN_P1
MERGE_BLOCKER
```

## 10. 상태 경계

```text
PRODUCT_CODE = UNCHANGED
DATA_MIGRATION = NOT_AUTHORIZED
SIMULATION_TOOL_CODE = NOT_AUTHORIZED
ART_ASSET_PRODUCTION = NOT_AUTHORIZED
IMAGE_GENERATION = STOPPED_BY_USER
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
```