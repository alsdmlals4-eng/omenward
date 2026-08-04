# [현행] 오멘워드 현재 구현 상태

```yaml
updated_at: 2026-08-04
current_main: RESOLVE_FROM_REPOSITORY_DEFAULT_BRANCH
current_planning_decision: OMW-DEC-20260804-PLANNING-STAGE-WAVE-DANGER-BOSS-PRESSURE-MATRIX-V1
current_process_policy: OMW-PROC-20260804-DYNAMIC-CURRENT-MAIN-AND-DOCUMENT-LIFECYCLE-V1
work_mode: TOTAL_PLANNING / CORE_FUN_CONTENT
latest_planning: USER_APPROVED_ACTIVE_BRANCH_NOT_IMPLEMENTED
current_count: 2_OF_10
product_code_authority: NONE
art_asset_production_authority: NONE
image_generation: STOPPED_BY_USER
```

- 전체 시스템 연결 기준선: `docs/design/APPROVED_VERTICAL_SLICE_SYSTEM_CONTRACT_2026-07-27.md`
- 현행 GDD: `docs/OMENWARD_GDD_CURRENT_CANON.md`
- 핵심 재미 정본: `docs/design/APPROVED_OMENWARD_CORE_FUN_AND_CONTENT_GUARDRAILS_2026-08-04.md`
- Stage 압력 정본: `docs/design/APPROVED_OMENWARD_STAGE_WAVE_DANGER_BOSS_PRESSURE_MATRIX_2026-08-04.md`
- 문서 수명주기: `docs/DOCUMENT_LIFECYCLE_REGISTRY.md`
- 최신 버티컬 슬라이스 구현: `NOT_STARTED`

## 1. 정확한 상태 표기

```text
VERTICAL_SLICE_IMPLEMENTATION_NOT_STARTED
LATEST_AUTOMATED_CONTRACTS_NOT_RUN
HUMAN_QA_NOT_RUN
CORE_LOCK_NOT_ALLOWED
```

```text
CURRENT_PRODUCT = LEGACY_PROTOTYPE
LATEST_APPROVED_PLANNING = STAGE_PRESSURE_MATRIX_DOCUMENTED_NOT_IMPLEMENTED
PRODUCT_CODE = UNCHANGED
SIMULATION_TOOL_CODE = NOT_AUTHORIZED
ART_ASSET_PRODUCTION = NOT_AUTHORIZED
IMAGE_GENERATION = STOPPED_BY_USER
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
```

문서 계약·CI·병합은 최신 Vertical Slice·HUD·룰렛·아트·Stage 콘텐츠가 제품에 구현됐다는 뜻이 아니다.

## 2. Legacy 검증 증거

```text
LEGACY_C1_C2_C3_PROVEN
LEGACY_C1_ROULETTE_CORE_REMOTE_PROVEN
```

- C1 구현 검증 head: `19f1a4ff75ac393c09aff5d9c1154fed04ccc4f9`
- C1 최종 검증 run: `29926598807`

이 증거는 과거 Legacy C1 룰렛 계약의 원격 검증을 뜻한다. 최신 전체 시스템·20 Stage·HUD·아트·Stage 압력의 구현을 증명하지 않으며 **V2 구현 완료를 뜻하지 않는다**.

## 3. 현행 기획·구형 문서 경계

```text
[현행] = 신규 기획·구현 입력 허용
[대체됨] = 후속 문서 사용
[보류] = 재검증 전 구현 금지
[폐기] = 사용 금지
[증거] = 과거 사실만 증명
```

- `OMENWARD_GAME_DESIGN.md`는 `[대체됨]`이다.
- `APPROVED_15_WAVE_STAGE_CLOCK_AND_OVERTIME_V2.md`는 `[대체됨]`이다.
- `APPROVED_TUTORIAL_FIRST_FOUR_WAVES_BALANCE_V1.md`는 `[보류]`다.
- 구형 첫 10분·Hero·Legendary·Meta·Hub 문서군은 `[보류]`다.
- 식량 현행 자원·기본 건물 5종·주변 지휘소 오라·고정 60초 공세·별도 룰렛 아이콘은 `[폐기]`다.
- `APPROVED_VERTICAL_SLICE_SYSTEM_CONTRACT_2026-07-27.md`는 시스템 연결 계보만 부분 승계한다.

## 4. 현행 플레이어 규칙

```text
CORE = 예고된 압력 → 제작한 확률 → 비가역 전선 커밋 → 설명 가능한 결과
RESOURCES = GOLD / MANA_STONE / DEPLOYED_TROOP_CAPACITY / MOVE_TICKET
BUILDINGS = VAULT / FARM / BARRACKS / DEFENSE_TOWER / COMMAND_POST / MANA_TOWER
BOTTOM_FUNCTIONS = ROULETTE / STORAGE / BUILD / TACTICAL_SKILL / BELU
MERCHANT = AFTER_STAGE_MAINTENANCE_ONLY
```

- 세 원형 릴은 3×3 노출창의 세 열이다.
- 지휘소는 현재 MapRun 전체 아군 병력 오라다.
- 건물 지속 유지비·토큰 초당 공급은 없다.
- 식량은 현행 핵심 HUD 자원이 아니다.

## 5. 현행 Stage 콘텐츠

```text
MAPRUN_STAGE_COUNT = 20
BASELINE_WAVE_BEATS = 3
DANGER_STAGES = 4 / 9 / 14 / 19
BOSS_STAGES = 5 / 10 / 15 / 20
PRESSURES = MASS / ARMORED / FLYING / INFILTRATION / SIEGE
```

- Stage 1~5: 압력 문해력.
- Stage 6~10: 압력 조합.
- Stage 11~15: 기회비용.
- Stage 16~20: 종합 숙련.
- Danger는 공개된 한 가지 규칙 변형을 사용한다.
- Boss는 Route·태세·목표·호위·집중 공격 기회를 바꾼다.
- Stage 시작 뒤 필요한 카운터를 숨은 무작위로 변경하지 않는다.
- 정확한 시간·Threat Budget·적 수치는 `NOT_RUN / NOT_APPROVED_NUMERIC`이다.

## 6. 현행 시각·자산 규칙

```text
STYLE = PIXEL_ILLUSTRATION_HYBRID
BATTLEFIELD = PIXEL_READABILITY + ILLUSTRATED_MATERIAL_AND_LIGHT
CLOSEUP_UI = ILLUSTRATION_FORWARD
GOLD_TOKEN_ART = IN_GAME_GOLD_IMAGE
TROOP_TOKEN_ART = IN_GAME_T1_T2_TROOP_IMAGE
T3_TROOP_TOKEN = FORBIDDEN
RESULT_REWARD_ART = ACTUAL_REWARDED_TROOP_IMAGE
```

## 7. 구현 상태 행렬

| 영역 | 기획 상태 | 제품 구현 | 자동 검증 | 사람 검증 |
|---|---|---|---|---|
| 전체 시스템 Vertical Slice | 연결 기준선·후속 정본 존재 | `NOT_STARTED` | `NOT_RUN_LATEST` | `NOT_RUN` |
| 핵심 재미·콘텐츠 가드레일 | 사용자 승인 1/10 | `NOT_STARTED` | `DOCUMENT_CI_ONLY` | `NOT_RUN` |
| Stage 압력 매트릭스 | 사용자 승인 2/10 | `NOT_STARTED` | `DOCUMENT_CI_ONLY` | `NOT_RUN` |
| 건물 6종 T2/T3 | `PENDING_3_OF_10` | `NOT_STARTED` | `NOT_RUN` | `NOT_RUN` |
| 병종·시너지·카운터 | `PENDING_4_OF_10` | `NOT_STARTED` | `NOT_RUN` | `NOT_RUN` |
| 전술스킬·상인 | `PENDING_5_TO_6` | `NOT_STARTED` | `NOT_RUN` | `NOT_RUN` |
| 전투 공간·HUD·아트 | main 정본 | `NOT_STARTED` | `NOT_RUN` | `NOT_RUN` |
| Hero·Legendary family | `[보류]` | `NOT_STARTED` | `NOT_RUN` | `NOT_RUN` |
| Meta·Hub | `[보류]` | `NOT_STARTED` | `NOT_RUN` | `NOT_RUN` |
| 실제 이미지·Animation·VFX | 사용자 중단 | `NOT_AUTHORIZED` | `N/A` | `NOT_RUN` |
| Codex 구현 계약 | 별도 승인 필요 | `BLOCKED` | `NOT_RUN` | `NOT_RUN` |

## 8. 이번 정본 검증 목표

- PROJECT_CORE·GDD·Map·Lifecycle이 같은 20 Stage 구조를 말한다.
- 구형 `15웨이브=1스테이지` 문서에 `[대체됨]`이 표시된다.
- 구형 첫 4공세 밸런스에 `[보류]`가 표시된다.
- Stage 시작 뒤 치명적 압력·Route를 숨은 무작위로 변경하지 않는다.
- Danger와 Boss가 단순 수치 증가로 수렴하지 않는다.
- 제품 경로 변경은 0이다.

## 9. CI 호환 marker

```text
CURRENT_VERTICAL_SLICE_AUTHORITY = design/APPROVED_VERTICAL_SLICE_SYSTEM_CONTRACT_2026-07-27.md
CURRENT_ADVERSARIAL_REVIEW_LINEAGE = reviews/ADVERSARIAL_VERTICAL_SLICE_REVIEW_2026-07-27.md
ROULETTE_AGENCY_EVIDENCE = benchmarks/OMENWARD_ROULETTE_AGENCY_EVIDENCE_PACK_2026-07-29.md
PILOT_RECOMMENDATION / NOT_CANON
```

## 10. 다음 작업

```text
CURRENT_GRILL_ME_COUNT = 2/10
NEXT_PLANNING = SIX_BUILDING_T2_T3_BRANCHES_AND_COUNTERS
THEN = TROOP_ROLES_SYNERGIES_AND_COUNTERS
CODEX_IMPLEMENTATION_PLAN = BLOCKED_UNTIL_SEPARATE_HANDOFF
PRODUCT_CODE_AUTHORITY = NONE
```
