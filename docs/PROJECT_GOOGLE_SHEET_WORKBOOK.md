# OMENWARD 프로젝트 Google Sheets Workbook

```yaml
updated_at: 2026-08-04
spreadsheet_id: 1VLwRtXGDtyj0JFt98wdIOtG6Zqc3wtdfCzSF9Fo6lpw
spreadsheet_title: 오멘워드(OMENWARD)
workspace_role: USER_FACING_GDD_WORKSPACE
change_protocol: PROPOSED_SHEET_CHANGE
sheet_status: PROJECT_SHEET_CONFIGURED
current_decision: OMW-DEC-20260804-PLANNING-PIXEL-ILLUSTRATION-HYBRID-ART-DIRECTION-V1
current_sync: OMW-SYNC-20260804-POST-MERGE-PIXEL-ILLUSTRATION-HYBRID-CANON-V1
current_process_policy: OMW-PROC-20260804-PLANNING-VISUALS-CODEX-IMPLEMENTATION-BOUNDARY-V1
current_main: d8ce26ee3ee21dbab50839b7a1334116e147789e
last_merged_planning_pr: 133
current_grill_me_count: 0_OF_10
product_code_authority: NONE
art_asset_production_authority: NONE
image_generation: STOPPED_BY_USER
```

## 1. 역할

GitHub APPROVED 문서가 기획 정본이며 Sheet는 사용자 가시 GDD·근거·감사·이미지 계획 Workspace다. 승인 변경은 같은 Decision·Sync ID와 main/PR SHA로 기록한다.

## 2. 현재 main 정본

Decision:

`OMW-DEC-20260804-PLANNING-PIXEL-ILLUSTRATION-HYBRID-ART-DIRECTION-V1`

Post-merge Sync:

`OMW-SYNC-20260804-POST-MERGE-PIXEL-ILLUSTRATION-HYBRID-CANON-V1`

```text
MAIN = d8ce26ee3ee21dbab50839b7a1334116e147789e
SOURCE_PR = 133
SOURCE_HEAD = 48466c4f669e24e19e2c8be3f4c879bdbfda04a9
PREFLIGHT_CI = 842 / 558 / 539 PASS
CURRENT_COUNT = 0/10
```

## 3. 최종 아트 방향 Sheet 계약

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

## 4. Post-merge Sheet 반영

| 탭 | 반영 내용 |
|---|---|
| `00_프로젝트_허브` | PR #133 merged·main SHA·counter 0/10 |
| `01_작업순서` | 10/10 완료·merge 증거·다음 콘텐츠 기획 |
| `02_현재_확정결정` | Decision 10 main canonical 상태 |
| `03_근거_라이브러리` | Post-merge Sync 근거 |
| `04_누락_충돌_감사` | 감사 `OMW-AUD-344~359` 유지·blocker 0 |
| `05_GDD_요약` | main canon·다음 핵심 재미/콘텐츠 작업 |
| `70_아트_오디오_에셋` | 최종 스타일·자산 경계 유지 |
| `71_이미지기획_생성목록` | 비교 이미지는 비정본·추가 생성 중단 |
| `99_변경이력` | merge·post-merge Sync 기록 |

## 5. Bounded Read-Back

쓰기 후 다음을 다시 읽는다.

- Decision·Sync ID.
- main merge SHA.
- PR #133 merged 상태.
- current counter `0/10`.
- 픽셀·일러스트 하이브리드.
- T1·T2 토큰 재사용과 T3 토큰 금지.
- 실제 지급 병종 결과 이미지.
- 이미지 생성 중단·비정본 참고 이미지 상태.
- 제품 코드·실제 자산 미변경.

일치 전에는 `READBACK_PASS`를 기록하지 않는다.

## 6. 필수 CI

```text
Validate Project Core Documentation
Validate Omenward GDD Sheet Adoption
Validate Base v9 adoption
```

Post-merge Sync PR exact HEAD에서도 모두 `success`여야 한다.

## 7. 상태 표기

```text
SHEET_SYNC = MAIN_MERGE_AND_POST_MERGE_SYNC
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
LAST_MERGED_COUNT = 10/10
CURRENT_COUNT = 0/10
NEXT_PLANNING = CORE_FUN_AND_CONTENT_DEEPENING
NEXT_PREFLIGHT = AFTER_10_NEW_APPROVED_DECISIONS
```
