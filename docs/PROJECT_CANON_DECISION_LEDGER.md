# [현행] 오멘워드 기획 정본 결정 원장

```yaml
updated_at: 2026-08-04
status: CURRENT_DECISION_LEDGER / ACTIVE_PLANNING_BRANCH
current_planning_decision: OMW-DEC-20260804-PLANNING-CORE-FUN-AND-CONTENT-GUARDRAILS-V1
current_process_policy: OMW-PROC-20260804-DYNAMIC-CURRENT-MAIN-AND-DOCUMENT-LIFECYCLE-V1
current_main: RESOLVE_FROM_REPOSITORY_DEFAULT_BRANCH
work_mode: TOTAL_PLANNING
last_merged_planning_pr: 134
last_merged_planning_commit: 3dc91102607b2e3d184897fb1fd7531f8a3327b3
current_count: 1_OF_10
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

PR #133과 #134를 통해 다음 10개 기획 결정과 post-merge 상태가 main에 반영됐다.

| 순번 | Decision ID | 핵심 정본 |
|---:|---|---|
| 1 | `OMW-DEC-20260803-VALIDATION-DETERMINISTIC-SIMULATION-HARNESS-SCOPE-V1` | 결과 재현·원인 복기 요구 |
| 2 | `OMW-DEC-20260803-VALIDATION-COMMON-COMBAT-SCHEMA-AND-RESOLUTION-ORDER-V1` | 동일 조건 공정성·숨은 선공 금지 |
| 3 | `OMW-DEC-20260803-VALIDATION-DAMAGE-PROTECTION-AND-STATUS-SEMANTICS-V1` | Damage·Barrier·Status 의미 |
| 4 | `OMW-DEC-20260803-VALIDATION-MITIGATION-FORMULA-AND-PROTECTION-NUMERIC-DEFAULTS-V1` | 방어·Barrier·Status 기획 기본값 |
| 5 | `OMW-DEC-20260803-VALIDATION-FIXED-TICK-TIME-AND-ACTIVATION-DEFAULTS-V1` | 전투 템포·Spawn 가독성 의도 |
| 6 | `OMW-DEC-20260803-VALIDATION-MODIFIER-STACKING-AND-EFFECT-PRECEDENCE-V1` | Modifier 폭증 방지·효과 가독성 |
| 7 | `OMW-DEC-20260804-PLANNING-COMBAT-SPACE-ROUTE-AND-TARGETING-EXPERIENCE-V1` | 세 전선·Route·Targeting 경험 |
| 8 | `OMW-DEC-20260804-PLANNING-BATTLEFIELD-VISUAL-HIERARCHY-AND-CAMERA-V1` | 전장 시각 계층·카메라 |
| 9 | `OMW-DEC-20260804-PLANNING-COMBAT-HUD-REEL-AND-BUILD-UX-V1` | HUD·룰렛·자원·상인·건물 6종 |
| 10 | `OMW-DEC-20260804-PLANNING-PIXEL-ILLUSTRATION-HYBRID-ART-DIRECTION-V1` | 픽셀·일러스트 하이브리드 아트·자산 계보 |

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

콘텐츠 압력 분류:

```text
MASS / ARMORED / FLYING / INFILTRATION / SIEGE
```

이 Decision은 정확한 Stage 수치·건물 분기·병종·전술스킬을 고정하지 않는다. 후속 콘텐츠 Decision이 소유한다.

## 4. 현행 자원·건물·룰렛

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

## 5. 문서 수명주기 Decision

정책:

`OMW-PROC-20260804-DYNAMIC-CURRENT-MAIN-AND-DOCUMENT-LIFECYCLE-V1`

```text
[현행] = 신규 기획·구현 사용 허용
[대체됨] = 후속 정본이 권위 승계
[보류] = 최신 정본과 재검증 전 사용 금지
[폐기] = 사용 금지
[증거] = 과거 사실 증명만 허용
```

세부 파일 상태는 `DOCUMENT_LIFECYCLE_REGISTRY.md`가 소유한다.

## 6. 적대적 감사 계보

```text
OMW-AUD-208~289 = 전투 결정·유지보수
OMW-AUD-290~299 = 전투 공간·기획 경계
OMW-AUD-300~313 = 전장 시각 계층
OMW-AUD-314~343 = HUD·룰렛·자원·건물·자산 재사용
OMW-AUD-344~359 = 픽셀·일러스트 하이브리드 아트
OMW-AUD-360~375 = 핵심 재미·정본·구형 문서 충돌
```

## 7. 현재 보류·폐기

- 첫 10분 구형 상세 흐름: `[보류]`.
- Hero·Legendary family: `[보류]`.
- Meta·Hub: `[보류]`.
- 식량 현행 HUD 자원: `[폐기]`.
- 기본 건물 5종: `[폐기]`.
- 주변 범위 지휘소 오라: `[폐기]`.
- 별도 룰렛 금화·병종 아이콘: `[폐기]`.
- T3 병종 룰렛 토큰: `[폐기]`.

## 8. 현재 금지선

```text
CURRENT_PRODUCT = LEGACY_PROTOTYPE
LATEST_PLANNING = CORE_FUN_AND_CONTENT_GUARDRAILS_NOT_IMPLEMENTED
PRODUCT_CODE = UNCHANGED
SIMULATION_TOOL_CODE = NOT_AUTHORIZED
ART_ASSET_PRODUCTION = NOT_AUTHORIZED
IMAGE_GENERATION = STOPPED_BY_USER
BALANCE_CONCLUSION = FORBIDDEN
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
```

## 9. 다음 Gate

```text
CURRENT_COUNT = 1/10
NEXT_DECISION = STAGE_WAVE_DANGER_BOSS_PRESSURE_MATRIX
NEXT_AFTER = SIX_BUILDING_T2_T3_BRANCHES_AND_COUNTERS
```
