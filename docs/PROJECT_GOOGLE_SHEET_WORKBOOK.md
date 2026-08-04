# [현행] OMENWARD 프로젝트 Google Sheets Workbook

```yaml
updated_at: 2026-08-05
spreadsheet_id: 1VLwRtXGDtyj0JFt98wdIOtG6Zqc3wtdfCzSF9Fo6lpw
spreadsheet_title: 오멘워드(OMENWARD)
workspace_role: USER_FACING_GDD_WORKSPACE
change_protocol: PROPOSED_SHEET_CHANGE
sheet_status: PROJECT_SHEET_CONFIGURED
current_decision: OMW-DEC-20260805-PLANNING-SIX-BUILDING-T2-T3-BRANCHES-AND-COUNTERS-V1
current_process_policy: OMW-PROC-20260805-BENCHMARK-TDD-APPROVAL-BATCH-V1
current_main: RESOLVE_FROM_REPOSITORY_DEFAULT_BRANCH
current_grill_me_count: 3_OF_10
product_code_authority: NONE
art_asset_production_authority: NONE
image_generation: STOPPED_BY_USER
```

## 1. 역할

GitHub의 `[현행]` 책임 원본이 기획 정본이며 Sheet는 사용자 가시 GDD·근거·감사·이미지 계획 Workspace다. 승인 변경은 같은 Decision ID와 exact PR HEAD로 반영한다.

## 2. 이번 Decision Sheet 계약

Decision:

`OMW-DEC-20260805-PLANNING-SIX-BUILDING-T2-T3-BRANCHES-AND-COUNTERS-V1`

공통 분기:

```text
T1 → T2 A → T3 A
T1 → T2 B → T3 B
CROSS_BRANCH = FORBIDDEN
DUAL_T3 = FORBIDDEN
MAPRUN_PERMANENT_CHOICE
```

건물:

```text
금고 = 안정→비축 / 행운→징조 대박
농장 = 징집→대규모 동원 / 예비→최후 예비대
병영 = 전열→정예 전열 / 기동→징조 대응대
방어탑 = 연사→요격 / 포격→파성
지휘소 = 돌격→결전 전선 / 수비→종심 방어
마력탑 = 유량→맥동 / 저장→징조 저장고
```

## 3. 압력·포기 비용 Sheet 계약

- 각 T2는 `얻는 것`, `포기하는 것`, `유리한 압력`, `핵심 루프 영향`, `T3 예고`를 가진다.
- 단일 건물 분기가 `MASS / ARMORED / FLYING / INFILTRATION / SIEGE`를 모두 해결하지 않는다.
- 건물은 준비 경로를 제공하고 병종·전술 Decision이 실제 카운터를 완성한다.
- `FLYING` 실제 병종·전술 대응은 4/10·5/10 전까지 blocker다.
- 정확한 비용·배율·범위·쿨다운·환불값은 `PENDING_SIMULATION`이다.
- T3 병종 이미지는 룰렛 토큰에 사용하지 않는다.

## 4. 운영 정책 Sheet 계약

```text
BENCHMARK_REQUIRED
INDUSTRY_COMPARISON_REQUIRED
MAX_APPROVAL_BATCH = 10
EARLY_CHECKPOINT = HIGH_RISK_CONFLICT / SESSION_END / LARGE_CANON_IMPACT
TDD = RED → GREEN → REFACTOR
EXPLICIT_BRANCH_REQUIRED_FOR_GITHUB_MUTATION
DIRECT_MAIN_WRITE = FORBIDDEN
```

- 공식 벤치마크·현업 비교에서 채택·비채택 원칙을 분리한다.
- 승인 10건은 최대 배치 크기이며 조기 체크포인트가 카운터를 임의 초기화하지 않는다.
- RED 실패·GREEN·REFACTOR 검증을 변경 이력에 기록한다.
- GitHub 파일 쓰기는 명시적 비기본 branch에서만 수행한다.

## 5. 수명주기 Sheet 계약

```text
[현행] = CURRENT_AUTHORITY
[대체됨] = SUPERSEDED_HISTORY_ONLY
[보류] = HELD_NO_IMPLEMENTATION_INPUT
[폐기] = REJECTED_NO_USE
[증거] = EVIDENCE_ONLY
```

- 기존 HUD·기본 건물 문서는 기본 역할 권위로 유지하고 새 건물 정본이 T2/T3 분기를 확장한다.
- 동일 인스턴스 교차 분기·양쪽 T3·만능 건물·T3 룰렛 토큰은 `[폐기]`다.
- 구형 첫 10분·Hero·Meta는 `[보류]`를 유지한다.

## 6. 탭별 반영

| 탭 | 반영 내용 |
|---|---|
| `00_프로젝트_허브` | Decision 3/10·exact PR HEAD·다음 병종 Gate |
| `01_작업순서` | 건물 분기 정본·TDD·다음 작업 |
| `02_현재_확정결정` | 공통 분기·인스턴스 선택·수치 경계 |
| `03_근거_라이브러리` | 공식 벤치마크·Stage 압력·기본 건물 역할 |
| `04_누락_충돌_감사` | `OMW-AUD-398~419` |
| `05_GDD_요약` | 건물 경로·포기 비용·3/10 |
| `12_핵심루프` | Stage 예고→건물 전문화→룰렛/전선 커밋 |
| `15_조작_게임규칙` | 업그레이드 카드·교차 분기 금지·Stage 전 선택 |
| `40_핵심시스템_메인콘텐츠` | 6종×2 분기와 압력 준비 경로 |
| `41_성장_경제` | 철거·환불·비축·저장 exact 수치 보류 |
| `50_메인콘텐츠` | 건물·Stage 압력 의존성 |
| `60_UX_UI_접근성` | 얻는 것·포기하는 것·T3 예고 비교 UX |
| `70_아트_오디오_에셋` | T1 실루엣 유지·분기 장치 차별화·실제 제작 중단 |
| `71_이미지기획_생성목록` | 건물 분기 Brief만 기록·추가 이미지 보류 |
| `99_변경이력` | Decision·정책·RED/GREEN·lifecycle 기록 |

## 7. Bounded Read-Back

쓰기 후 다음을 재조회한다.

- Decision ID와 exact PR HEAD.
- counter `3/10`.
- 건물 6종과 12개 T2·12개 T3 경로.
- `CROSS_BRANCH / DUAL_T3 = FORBIDDEN`.
- 얻는 것·포기하는 것·압력 적합성.
- 운영 정책과 RED run 888.
- lifecycle `[현행]/[대체됨]/[보류]/[폐기]`.
- 제품 코드·아트 자산 미변경.
- 감사 `OMW-AUD-398~419`.

일치 전에는 `READBACK_PASS`를 기록하지 않는다.

## 8. 필수 CI·차단 검색

```text
Validate Project Core Documentation
Validate Omenward GDD Sheet Adoption
Validate Base v9 adoption
```

모두 exact PR HEAD에서 success여야 한다.

`04_누락_충돌_감사` 실제 데이터 행에 다음이 없어야 한다.

```text
OPEN_P0
OPEN_P1
MERGE_BLOCKER
```

## 9. 상태 경계

```text
PRODUCT_CODE = UNCHANGED
SIMULATION_TOOL_CODE = NOT_AUTHORIZED
ART_ASSET_PRODUCTION = NOT_AUTHORIZED
IMAGE_GENERATION = STOPPED_BY_USER
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
```
