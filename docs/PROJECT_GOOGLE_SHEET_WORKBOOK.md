# OMENWARD 프로젝트 Google Sheets Workbook

```yaml
updated_at: 2026-08-04
spreadsheet_id: 1VLwRtXGDtyj0JFt98wdIOtG6Zqc3wtdfCzSF9Fo6lpw
spreadsheet_title: 오멘워드(OMENWARD)
workspace_role: USER_FACING_GDD_WORKSPACE
change_protocol: PROPOSED_SHEET_CHANGE
sheet_status: PROJECT_SHEET_CONFIGURED
current_decision: OMW-DEC-20260804-PLANNING-PIXEL-ILLUSTRATION-HYBRID-ART-DIRECTION-V1
current_process_policy: OMW-PROC-20260804-PLANNING-VISUALS-CODEX-IMPLEMENTATION-BOUNDARY-V1
current_grill_me_count: 10_OF_10
product_code_authority: NONE
art_asset_production_authority: NONE
image_generation: STOPPED_BY_USER
```

## 1. 역할

GitHub APPROVED 문서가 기획 정본이며 Sheet는 사용자 가시 GDD·근거·감사·이미지 계획 Workspace다. 승인 변경은 같은 Decision ID와 exact PR HEAD로 기록한다.

## 2. Decision 10 Sheet 동기화 계약

Decision ID:

`OMW-DEC-20260804-PLANNING-PIXEL-ILLUSTRATION-HYBRID-ART-DIRECTION-V1`

반영 내용:

```text
STYLE = PIXEL_ILLUSTRATION_HYBRID
MOOD = FAIRYTALE_HOLY_FANTASY_VS_VEIL_GOTHIC
BATTLEFIELD = PIXEL_READABILITY + ILLUSTRATED_MATERIAL_AND_LIGHT
CLOSEUP_UI = ILLUSTRATION_FORWARD
ALLY = IVORY / BLUE / RESTRAINED_GOLD
VEIL = CHARCOAL / DEEP_PURPLE / CRIMSON / ASYMMETRIC_GOTHIC
```

룰렛 자산:

```text
GOLD_TOKEN_ART = IN_GAME_GOLD_IMAGE
TROOP_TOKEN_ART = IN_GAME_T1_T2_TROOP_IMAGE
T3_TROOP_TOKEN = FORBIDDEN
RESULT_REWARD_ART = ACTUAL_REWARDED_TROOP_IMAGE
SEPARATE_GOLD_OR_TROOP_TOKEN_ICON_PRODUCTION = FORBIDDEN
```

## 3. 탭별 반영 의미

| 탭 | 반영 내용 |
|---|---|
| `00_프로젝트_허브` | 10/10·Decision·PR HEAD·preflight 상태 |
| `01_작업순서` | Decision 10 완료와 preflight 단계 |
| `02_현재_확정결정` | 픽셀·일러스트 하이브리드 최종 아트 정본 |
| `03_근거_라이브러리` | 사용자 제공 병종 이미지·스타일 비교 선택·기존 전장/HUD 근거 |
| `04_누락_충돌_감사` | `OMW-AUD-344~359` |
| `05_GDD_요약` | 최종 아트 방향과 10/10 상태 |
| `12_핵심루프` | 전장 가독성과 룰렛·보상 자산 계보가 핵심 루프를 지원하는 방식 |
| `40_핵심시스템_메인콘텐츠` | 병종 Tier·등급·Veil·건물 6종 시각 문법 |
| `50_메인콘텐츠` | 전장·병종·건물·영웅·전설 콘텐츠 표현 |
| `60_UX_UI_접근성` | 픽셀 가독성·일러스트 근접 정보·UI 장식 제한 |
| `70_아트_오디오_에셋` | 최종 색·재질·실루엣·VFX·벨루·자산 우선순위 |
| `71_이미지기획_생성목록` | 스타일 4 선택 기록·비교 이미지는 비정본·추가 생성 중단 |
| `99_변경이력` | Decision·HEAD·10/10·CI·preflight 기록 |

## 4. Bounded Read-Back

쓰기 후 다음을 다시 읽는다.

- Decision ID와 exact PR HEAD.
- `10/10` 상태.
- 픽셀·일러스트 하이브리드 표현.
- 아군·Veil 색·형태 문법.
- T1·T2 토큰 재사용과 T3 토큰 금지.
- 실제 지급 병종 결과 이미지.
- 건물 6종 실루엣과 벨루 일러스트 우선.
- 이미지 생성 중단·비정본 참고 이미지 상태.
- 감사 `OMW-AUD-344~359` 연속성.
- CI와 blocker 상태.

일치 전에는 `READBACK_PASS`를 기록하지 않는다.

## 5. 필수 CI

```text
Validate Project Core Documentation
Validate Omenward GDD Sheet Adoption
Validate Base v9 adoption
```

모두 PR exact HEAD에서 `success`여야 한다.

## 6. Blocker 검색

`04_누락_충돌_감사`에서 다음 실제 데이터 행을 검색한다.

```text
OPEN_P0
OPEN_P1
MERGE_BLOCKER
```

헤더 외 일치 행이 없어야 한다.

## 7. 상태 표기

```text
SHEET_SYNC = SYNCED_TO_PR_HEAD_AFTER_WRITE_AND_READBACK
PRODUCT_CODE = UNCHANGED
SIMULATION_TOOL_CODE = NOT_AUTHORIZED
ART_ASSET_PRODUCTION = NOT_AUTHORIZED
IMAGE_GENERATION = STOPPED_BY_USER
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
```

## 8. 운영 Gate

```text
GRILL_ME_COUNT = 10/10
NEXT_PREFLIGHT = NOW
MERGE = ONLY_AFTER_FRESH_GREEN_AND_ZERO_BLOCKERS
```
