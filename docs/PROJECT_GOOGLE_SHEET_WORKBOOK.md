# [현행] OMENWARD 프로젝트 Google Sheets Workbook

```yaml
updated_at: 2026-08-04
spreadsheet_id: 1VLwRtXGDtyj0JFt98wdIOtG6Zqc3wtdfCzSF9Fo6lpw
spreadsheet_title: 오멘워드(OMENWARD)
workspace_role: USER_FACING_GDD_WORKSPACE
change_protocol: PROPOSED_SHEET_CHANGE
sheet_status: PROJECT_SHEET_CONFIGURED
current_decision: OMW-DEC-20260804-PLANNING-STAGE-WAVE-DANGER-BOSS-PRESSURE-MATRIX-V1
current_process_policy: OMW-PROC-20260804-DYNAMIC-CURRENT-MAIN-AND-DOCUMENT-LIFECYCLE-V1
current_main: RESOLVE_FROM_REPOSITORY_DEFAULT_BRANCH
current_grill_me_count: 2_OF_10
product_code_authority: NONE
art_asset_production_authority: NONE
image_generation: STOPPED_BY_USER
```

## 1. 역할

GitHub의 `[현행]` 책임 원본이 기획 정본이며 Sheet는 사용자 가시 GDD·근거·감사·이미지 계획 Workspace다. 승인 변경은 같은 Decision ID와 exact PR HEAD로 반영한다.

## 2. 이번 Decision Sheet 계약

Decision:

`OMW-DEC-20260804-PLANNING-STAGE-WAVE-DANGER-BOSS-PRESSURE-MATRIX-V1`

```text
MAPRUN_STAGE_COUNT = 20
BASELINE_WAVE_BEATS = 3
DANGER_STAGES = 4 / 9 / 14 / 19
BOSS_STAGES = 5 / 10 / 15 / 20
PRESSURES = MASS / ARMORED / FLYING / INFILTRATION / SIEGE
```

네 막:

```text
1~5 압력 문해력
6~10 압력 조합
11~15 기회비용
16~20 종합 숙련
```

Wave 문법:

```text
NORMAL = PROBE → COMPLICATION → COMMITMENT_TEST
DANGER = DISTORTION_INTRODUCTION → OVERLAP → CONSEQUENCE
BOSS = APPROACH → BOSS_ENTRY → FINALE
```

## 3. 공정성·변형 Sheet 계약

- Stage 시작 전 압력·전선·Route·예상 목표·치명적 행동 공개.
- Danger는 한 가지 전역 규칙 변형만 사용.
- Boss는 Route·태세·목표·호위·집중 공격 기회를 변경.
- Stage 시작 뒤 필수 카운터를 숨은 무작위로 변경하지 않음.
- 압력 역할·학습 목표는 고정.
- 적 패키지·전선·Route는 맵별 작성 변형.
- exact 시간·수량·Threat Budget은 `PENDING_SIMULATION`.

## 4. 문서 수명주기 Sheet 계약

```text
[현행] = CURRENT_AUTHORITY
[대체됨] = SUPERSEDED_HISTORY_ONLY
[보류] = HELD_NO_IMPLEMENTATION_INPUT
[폐기] = REJECTED_NO_USE
[증거] = EVIDENCE_ONLY
```

Stage 관련:

- `APPROVED_15_WAVE_STAGE_CLOCK_AND_OVERTIME_V2.md`: `[대체됨]`.
- `APPROVED_TUTORIAL_FIRST_FOUR_WAVES_BALANCE_V1.md`: `[보류]`.
- Vertical Slice 2026-07-27: 시스템 연결 계보만 부분 승계.
- `15웨이브=1스테이지`, 고정 60초 공세, Danger 정보 차단, 숨은 필수 카운터 변경: `[폐기]`.

## 5. 탭별 반영

| 탭 | 반영 내용 |
|---|---|
| `00_프로젝트_허브` | Decision 2/10·exact PR HEAD·20 Stage 상태 |
| `01_작업순서` | Stage 압력 정본·구형 Stage 충돌·다음 건물 분기 |
| `02_현재_확정결정` | 4막×5 Stage·Danger/Boss 위치·공정성 |
| `03_근거_라이브러리` | 기존 MapRun·구형 15 Wave·첫 4공세·리플레이 대안 |
| `04_누락_충돌_감사` | `OMW-AUD-376~397` |
| `05_GDD_요약` | 20 Stage·3 Wave Beat·2/10 |
| `12_핵심루프` | 압력 예고→릴 설계→커밋→Stage 복기 |
| `15_조작_게임규칙` | Danger/Boss 정보 공개와 비가역 배치 공정성 |
| `40_핵심시스템_메인콘텐츠` | 다섯 압력·Normal/Danger/Boss 문법 |
| `41_성장_경제` | Stage 정비·Boss 재조정 기회·exact 보상 보류 |
| `50_메인콘텐츠` | 20 Stage 전체 매트릭스 |
| `60_UX_UI_접근성` | Omen 정보·주 전선·Route·목표 판독 |
| `70_아트_오디오_에셋` | 압력·Danger·Boss 시각 역할·실제 제작 중단 |
| `71_이미지기획_생성목록` | 역할 확정 전 추가 이미지 제작 보류 |
| `99_변경이력` | Decision·lifecycle·적대적 검토 기록 |

## 6. Bounded Read-Back

쓰기 후 다음을 재조회한다.

- Decision ID와 exact PR HEAD.
- counter `2/10`.
- 20 Stage와 3 Wave Beat.
- Danger `4/9/14/19`, Boss `5/10/15/20`.
- 네 막과 다섯 압력.
- Danger 한 규칙·Boss 선택 구조.
- Stage 시작 전 치명적 정보 공개.
- lifecycle `[대체됨]/[보류]/[폐기]`.
- 이미지 생성 중단·제품 코드 미변경.
- 감사 `OMW-AUD-376~397`.

일치 전에는 `READBACK_PASS`를 기록하지 않는다.

## 7. 필수 CI

```text
Validate Project Core Documentation
Validate Omenward GDD Sheet Adoption
Validate Base v9 adoption
```

모두 exact PR HEAD에서 `success`여야 한다.

## 8. 차단 검색

`04_누락_충돌_감사`의 실제 데이터 행에서 다음이 없어야 한다.

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
