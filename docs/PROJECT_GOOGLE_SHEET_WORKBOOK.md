# [현행] OMENWARD 프로젝트 Google Sheets Workbook

```yaml
updated_at: 2026-08-04
spreadsheet_id: 1VLwRtXGDtyj0JFt98wdIOtG6Zqc3wtdfCzSF9Fo6lpw
spreadsheet_title: 오멘워드(OMENWARD)
workspace_role: USER_FACING_GDD_WORKSPACE
change_protocol: PROPOSED_SHEET_CHANGE
sheet_status: PROJECT_SHEET_CONFIGURED
current_decision: OMW-DEC-20260804-PLANNING-CORE-FUN-AND-CONTENT-GUARDRAILS-V1
current_process_policy: OMW-PROC-20260804-DYNAMIC-CURRENT-MAIN-AND-DOCUMENT-LIFECYCLE-V1
current_main: RESOLVE_FROM_REPOSITORY_DEFAULT_BRANCH
current_grill_me_count: 1_OF_10
product_code_authority: NONE
art_asset_production_authority: NONE
image_generation: STOPPED_BY_USER
```

## 1. 역할

GitHub의 `[현행]` 책임 원본이 기획 정본이며 Sheet는 사용자 가시 GDD·근거·감사·이미지 계획 Workspace다. 승인 변경은 같은 Decision ID와 exact PR HEAD로 반영한다.

## 2. 이번 Decision Sheet 계약

Decision:

`OMW-DEC-20260804-PLANNING-CORE-FUN-AND-CONTENT-GUARDRAILS-V1`

```text
CORE_FUN = FORECAST_PRESSURE → BUILD_ODDS → IRREVERSIBLE_FRONT_COMMIT → EXPLAINABLE_RESULT
PRESSURE_TAGS = MASS / ARMORED / FLYING / INFILTRATION / SIEGE
RESOURCES = GOLD / MANA_STONE / DEPLOYED_TROOP_CAPACITY / MOVE_TICKET
BUILDINGS = VAULT / FARM / BARRACKS / DEFENSE_TOWER / COMMAND_POST / MANA_TOWER
```

룰렛·자산:

```text
THREE_CIRCULAR_REELS = THREE_COLUMNS_OF_3X3_VISIBLE_WINDOW
GOLD_TOKEN_ART = IN_GAME_GOLD_IMAGE
TROOP_TOKEN_ART = IN_GAME_T1_T2_TROOP_IMAGE
T3_TROOP_TOKEN = FORBIDDEN
RESULT_REWARD_ART = ACTUAL_REWARDED_TROOP_IMAGE
```

## 3. 문서 수명주기 Sheet 계약

```text
[현행] = CURRENT_AUTHORITY
[대체됨] = SUPERSEDED_HISTORY_ONLY
[보류] = HELD_NO_IMPLEMENTATION_INPUT
[폐기] = REJECTED_NO_USE
[증거] = EVIDENCE_ONLY
```

- 구형 master GDD는 `[대체됨]`.
- 첫 10분 구형 상세·Hero·Legendary·Meta·Hub는 `[보류]`.
- 식량 현행 자원·건물 5종·주변 지휘소·별도 룰렛 아이콘·T3 토큰은 `[폐기]`.

## 4. 탭별 반영

| 탭 | 반영 내용 |
|---|---|
| `00_프로젝트_허브` | Decision 1/10·exact PR HEAD·동적 main 정책 |
| `01_작업순서` | 핵심 재미 정본·구형 충돌 정리·다음 Stage 압력 |
| `02_현재_확정결정` | 핵심 재미·콘텐츠 가드레일 |
| `03_근거_라이브러리` | 구형 core/GDD/Hero/첫 10분 충돌 근거 |
| `04_누락_충돌_감사` | `OMW-AUD-360~375` |
| `05_GDD_요약` | 현행 자원·건물·핵심 루프·1/10 |
| `12_핵심루프` | 예고→확률 설계→커밋→복기 |
| `15_조작_게임규칙` | 세 릴과 3×3 관계·비가역 배치 |
| `40_핵심시스템_메인콘텐츠` | 압력 태그·건물 6종 역할 |
| `41_성장_경제` | 식량 폐기·현행 자원·상인 기회비용 |
| `50_메인콘텐츠` | Stage 압력 우선순위 |
| `60_UX_UI_접근성` | 결과 원인 설명·정보 공개 |
| `70_아트_오디오_에셋` | 시각 역할과 콘텐츠 기능 일치 |
| `71_이미지기획_생성목록` | 실제 제작 중단·구형 시안 비정본 |
| `99_변경이력` | 정본 충돌 해결·lifecycle 기록 |

## 5. Bounded Read-Back

쓰기 후 다음을 재조회한다.

- Decision ID와 exact PR HEAD.
- counter `1/10`.
- 핵심 재미 4축.
- MASS/ARMORED/FLYING/INFILTRATION/SIEGE.
- 골드·마석·병력 한도·이동권.
- 건물 6종·전역 지휘소.
- 세 릴과 3×3 관계.
- lifecycle `[대체됨]/[보류]/[폐기]`.
- 이미지 생성 중단·제품 코드 미변경.
- 감사 `OMW-AUD-360~375`.

일치 전에는 `READBACK_PASS`를 기록하지 않는다.

## 6. 필수 CI

```text
Validate Project Core Documentation
Validate Omenward GDD Sheet Adoption
Validate Base v9 adoption
```

모두 exact PR HEAD에서 `success`여야 한다.

## 7. 차단 검색

`04_누락_충돌_감사`의 실제 데이터 행에서 다음이 없어야 한다.

```text
OPEN_P0
OPEN_P1
MERGE_BLOCKER
```

## 8. 상태 경계

```text
PRODUCT_CODE = UNCHANGED
SIMULATION_TOOL_CODE = NOT_AUTHORIZED
ART_ASSET_PRODUCTION = NOT_AUTHORIZED
IMAGE_GENERATION = STOPPED_BY_USER
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
```
