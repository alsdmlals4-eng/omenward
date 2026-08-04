# [현행] 오멘워드 기획 정본 결정 원장

```yaml
updated_at: 2026-08-04
status: CURRENT_DECISION_LEDGER / ACTIVE_PLANNING_BRANCH
current_planning_decision: OMW-DEC-20260804-PLANNING-STAGE-WAVE-DANGER-BOSS-PRESSURE-MATRIX-V1
current_process_policy: OMW-PROC-20260804-DYNAMIC-CURRENT-MAIN-AND-DOCUMENT-LIFECYCLE-V1
current_main: RESOLVE_FROM_REPOSITORY_DEFAULT_BRANCH
work_mode: TOTAL_PLANNING
last_merged_planning_pr: 135
last_merged_planning_commit: 8a56d9b9d0b7b1bec3702644305d000670f6aea7
current_count: 2_OF_10
product_code_authority: NONE
art_asset_production_authority: NONE
image_generation: STOPPED_BY_USER
```

## 1. 운영 원칙

- `PROJECT_CORE.md`가 제품 정체성과 핵심 불변을 소유한다.
- `DOCUMENTATION_MAP.md`와 `DOCUMENT_LIFECYCLE_REGISTRY.md`가 현재 권위와 구형 문서 상태를 소유한다.
- `current_main`과 `context_baseline_commit`은 저장소 기본 브랜치에서 동적으로 해석한다.
- Google Sheet는 같은 Decision ID와 exact PR HEAD로 동기화한다.
- GPT는 핵심 재미·콘텐츠·플레이어 경험·UX·아트 방향을 소유한다.
- Codex는 자료구조·알고리즘·좌표·경로탐색·성능·코드·테스트 구현을 소유한다.
- 10개 승인 Decision마다 fresh preflight와 적대적 검토를 수행한다.

## 2. 직전 병합 Planning Stack

PR #133~#135를 통해 이전 10개 결정과 새 Batch 1/10이 main에 반영됐다.

| 구간 | 핵심 |
|---|---|
| 이전 1~6 | 전투 공정성·Damage·Status·Modifier 의미 |
| 이전 7 | 세 전선·Route·Targeting 경험 |
| 이전 8 | 전장 시각 계층·카메라 |
| 이전 9 | HUD·룰렛·자원·상인·건물 6종 |
| 이전 10 | 픽셀·일러스트 하이브리드 아트 |
| 새 Batch 1 | 핵심 재미·콘텐츠 가드레일·문서 lifecycle |

## 3. 새 Planning Batch — Decision 1/10

### `OMW-DEC-20260804-PLANNING-CORE-FUN-AND-CONTENT-GUARDRAILS-V1`

책임 원본:

`design/APPROVED_OMENWARD_CORE_FUN_AND_CONTENT_GUARDRAILS_2026-08-04.md`

핵심:

```text
예고된 압력
→ 제작한 확률
→ 비가역 전선 커밋
→ 설명 가능한 결과·다음 설계
```

압력 분류:

```text
MASS / ARMORED / FLYING / INFILTRATION / SIEGE
```

## 4. 새 Planning Batch — Decision 2/10

### `OMW-DEC-20260804-PLANNING-STAGE-WAVE-DANGER-BOSS-PRESSURE-MATRIX-V1`

책임 원본:

`design/APPROVED_OMENWARD_STAGE_WAVE_DANGER_BOSS_PRESSURE_MATRIX_2026-08-04.md`

구조:

```text
MapRun = 20 Stage
Stage당 3 Wave Beat 기준선
Danger = 4 / 9 / 14 / 19
Boss = 5 / 10 / 15 / 20
```

네 막:

```text
1~5 압력 문해력
6~10 압력 조합
11~15 기회비용
16~20 종합 숙련
```

공정성:

- Stage 시작 전 주·보조 압력, 전선, Route, 목표, 치명적 행동 공개.
- Danger는 공개된 한 가지 규칙 변형.
- Boss는 Route·태세·목표·호위·집중 공격 기회를 변경.
- 압력 역할은 고정하고 적 패키지·전선·Route는 맵별 작성 변형.
- Stage 시작 뒤 필요한 카운터를 숨은 무작위로 변경하지 않음.
- 정확한 시간·Threat Budget·적 수치는 시뮬레이션 전 미확정.

이 Decision은 건물·병종의 실제 카운터 목록을 고정하지 않는다. 3/10·4/10 Decision이 최소 두 대응 경로를 채운다.

## 5. 현행 자원·건물·룰렛

```text
자원 = 골드 / 마석 / 배치 병력·병력 한도 / 이동권
건물 = 금고 / 농장 / 병영 / 방어탑 / 지휘소 / 마력탑
지휘소 = 현재 MapRun 전체 아군 병력 오라
룰렛 = 세 원형 릴이 3×3 노출창의 세 열을 구성
```

자산:

```text
금화 토큰 = 인게임 금화 이미지
병종 토큰 = 인게임 T1·T2 병종 이미지
T3 병종 토큰 = 금지
결과 보상 = 실제 지급 병종 이미지
```

## 6. 문서 수명주기

정책:

`OMW-PROC-20260804-DYNAMIC-CURRENT-MAIN-AND-DOCUMENT-LIFECYCLE-V1`

```text
[현행] = 신규 기획·구현 사용 허용
[대체됨] = 후속 정본이 권위 승계
[보류] = 최신 정본과 재검증 전 사용 금지
[폐기] = 사용 금지
[증거] = 과거 사실 증명만 허용
```

Stage 관련:

- `APPROVED_15_WAVE_STAGE_CLOCK_AND_OVERTIME_V2.md`: `[대체됨]`.
- `APPROVED_TUTORIAL_FIRST_FOUR_WAVES_BALANCE_V1.md`: `[보류]`.
- Vertical Slice 2026-07-27: 전체 연결 계보만 부분 승계.

세부 파일 상태는 `DOCUMENT_LIFECYCLE_REGISTRY.md`가 소유한다.

## 7. 적대적 감사 계보

```text
OMW-AUD-208~289 = 전투 결정·유지보수
OMW-AUD-290~299 = 전투 공간·기획 경계
OMW-AUD-300~313 = 전장 시각 계층
OMW-AUD-314~343 = HUD·룰렛·자원·건물·자산 재사용
OMW-AUD-344~359 = 픽셀·일러스트 하이브리드 아트
OMW-AUD-360~375 = 핵심 재미·정본·구형 문서 충돌
OMW-AUD-376~397 = Stage 압력·공정성·리플레이성·구형 Stage 충돌
```

## 8. 현재 보류·폐기

- 첫 10~15분 구형 상세 흐름: `[보류]`.
- 구형 첫 4공세 수치·식량·자동생산: `[보류]`.
- Hero·Legendary family: `[보류]`.
- Meta·Hub: `[보류]`.
- 식량 현행 HUD 자원: `[폐기]`.
- 기본 건물 5종: `[폐기]`.
- 주변 범위 지휘소 오라: `[폐기]`.
- `15웨이브=1스테이지`와 고정 60초 공세: `[폐기]`.
- Danger에서 정보·핵심 기능 차단: `[폐기]`.
- 별도 룰렛 금화·병종 아이콘: `[폐기]`.
- T3 병종 룰렛 토큰: `[폐기]`.

## 9. 현재 금지선

```text
CURRENT_PRODUCT = LEGACY_PROTOTYPE
LATEST_PLANNING = STAGE_PRESSURE_MATRIX_NOT_IMPLEMENTED
PRODUCT_CODE = UNCHANGED
SIMULATION_TOOL_CODE = NOT_AUTHORIZED
ART_ASSET_PRODUCTION = NOT_AUTHORIZED
IMAGE_GENERATION = STOPPED_BY_USER
BALANCE_CONCLUSION = FORBIDDEN
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
```

## 10. 다음 Gate

```text
CURRENT_COUNT = 2/10
NEXT_DECISION = SIX_BUILDING_T2_T3_BRANCHES_AND_COUNTERS
NEXT_AFTER = TROOP_ROLES_SYNERGIES_AND_COUNTERS
```
