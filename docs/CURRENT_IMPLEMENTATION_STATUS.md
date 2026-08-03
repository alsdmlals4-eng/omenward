# 오멘워드 현재 구현 상태

- 갱신일: 2026-08-04
- 전체 시스템 정본: `docs/design/APPROVED_VERTICAL_SLICE_SYSTEM_CONTRACT_2026-07-27.md`
- 최신 Decision 9 정본: `docs/design/APPROVED_OMENWARD_COMBAT_HUD_ROULETTE_RESOURCE_MERCHANT_AND_BUILDING_ROSTER_2026-08-04.md`
- 작업 모드: `TOTAL_PLANNING / CORE_FUN_CONTENT_VISUAL_PROFILE`
- 최신 기획 상태: `USER_APPROVED_ACTIVE_BRANCH_NOT_IMPLEMENTED`
- 현재 Decision: `OMW-DEC-20260804-PLANNING-COMBAT-HUD-REEL-AND-BUILD-UX-V1`
- 운영 정책: `OMW-PROC-20260804-PLANNING-VISUALS-CODEX-IMPLEMENTATION-BOUNDARY-V1`
- 제품 코드 승인: `NOT_AUTHORIZED`
- 이미지 제작 상태: `PAUSED_BY_USER`

## 1. 정확한 상태 표기

```text
최신 버티컬 슬라이스 구현: `NOT_STARTED`
VERTICAL_SLICE_IMPLEMENTATION_NOT_STARTED
LATEST_AUTOMATED_CONTRACTS_NOT_RUN
HUMAN_QA_NOT_RUN
CORE_LOCK_NOT_ALLOWED
```

```text
CURRENT_PRODUCT = LEGACY_PROTOTYPE
LATEST_APPROVED_PLANNING = COMBAT_HUD_ROULETTE_RESOURCE_MERCHANT_BUILDING_ROSTER_DOCUMENTED_NOT_IMPLEMENTED
PRODUCT_CODE = UNCHANGED
SIMULATION_TOOL_CODE = NOT_AUTHORIZED
IMAGE_PRODUCTION = PAUSED_BY_USER
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
```

문서 계약과 CI 통과는 최신 Vertical Slice·전투 시스템·HUD·자원·건물·상인이 구현됐다는 뜻이 아니다.

## 2. Legacy 검증 증거

```text
LEGACY_C1_C2_C3_PROVEN
LEGACY_C1_ROULETTE_CORE_REMOTE_PROVEN
```

- C1 구현 검증 head: `19f1a4ff75ac393c09aff5d9c1154fed04ccc4f9`
- C1 최종 검증 run: `29926598807`

이 증거는 과거 Legacy C1 룰렛 계약의 원격 검증을 뜻한다. 최신 V2 전체 시스템, 20 Stage Vertical Slice, 현재 Planning Stack 구현을 증명하지 않으며 **V2 구현 완료를 뜻하지 않는다**.

## 3. 현행 작업 권한

```text
GPT / Work
= 핵심 재미·플레이 동기·콘텐츠 기획·플레이어 규칙·UX·이미지·아트 방향·검수 기준

Codex
= 자료구조·알고리즘·좌표·경로탐색·물리·성능·코드·테스트 구현
```

GPT 작업은 핵심 재미→콘텐츠 구조→UX·이미지·아트 순서로 진행한다. 기존 1~6 Decision의 기술 세부는 `CODEX_REFERENCE_RECOMMENDATION / NOT_BINDING_IMPLEMENTATION`이다. 플레이어에게 보이는 규칙·밸런스 의도·가독성 목표는 계속 승인 상태다.

## 4. 승인 Planning Stack

```text
P0 결과 재현·원인 복기 요구
P1 공통 전투 공정성·숨은 선공 금지
P2 Damage·Protection·Status 의미
P3 방어·Barrier·Status 기획 기본값
P4 전투 템포·Spawn 가독성 의도
P5 Modifier 폭증 방지·효과 가독성
P6 세 전선·Route·Targeting 경험
P7 전장 시각 계층·카메라·정보 밀도
P8 HUD·룰렛 정보·자원·상인·건물 역할
```

### P8 플레이어 UX·콘텐츠 규칙

```text
BOTTOM_FUNCTIONS = ROULETTE / STORAGE / BUILD / TACTICAL_SKILL / BELU
MAIN_HUD_RESOURCES = GOLD / MANA_STONE / DEPLOYED_TROOP_CAPACITY
MOVE_TICKET = ROULETTE_PANEL_ONLY / STORED_CAP_3
MERCHANT = AFTER_STAGE_MAINTENANCE_ONLY
BUILDINGS = VAULT / FARM / BARRACKS / DEFENSE_TOWER / COMMAND_POST / MANA_TOWER
```

- 건물별 지속 유지비는 없다.
- 토큰은 초당 공급되지 않는다.
- 보상 등급은 완성선 수로 결정한다.
- 지휘소는 현재 MapRun 전체 아군 병력 오라다.
- 벨루는 우측 하단에서 상황과 선택 근거만 제공한다.

## 5. 구현 상태 행렬

| 영역 | 기획 상태 | 제품 구현 | 자동 검증 | 사람 검증 |
|---|---|---|---|---|
| 20 Stage 전체 시스템 Vertical Slice | 승인 정본 존재 | `NOT_STARTED` | `NOT_RUN_LATEST` | `NOT_RUN` |
| 결정론·공통 전투 참고 계약 | 플레이어 결과 요구 승인 | `NOT_STARTED` | `NOT_RUN` | `NOT_RUN` |
| Damage·Protection·Status | 플레이어 의미 승인 | `NOT_STARTED` | `NOT_RUN` | `NOT_RUN` |
| 방어·Barrier·Modifier | 기획 기본값 승인 | `NOT_STARTED` | `NOT_RUN` | `NOT_RUN` |
| 전투 공간·Route·Targeting | 플레이 경험 승인 | `NOT_STARTED` | `NOT_RUN` | `NOT_RUN` |
| 전장 시각 계층·카메라 | 플레이 경험 승인 | `NOT_STARTED` | `NOT_RUN` | `NOT_RUN` |
| HUD·룰렛·자원·상인·건물 6종 | 사용자 승인 9/10 | `NOT_STARTED` | `NOT_RUN` | `NOT_RUN` |
| 아트·최종 이미지 Brief | 미확정 10/10 | `BLOCKED` | `NOT_RUN` | `NOT_RUN` |
| 실제 이미지·Animation·HX | 사용자 중단 | `PAUSED` | `N/A` | `NOT_RUN` |
| 핵심 재미·콘텐츠 심화 | Visual preflight 이후 계속 | `N/A` | `NOT_RUN` | `NOT_RUN` |
| Codex 구현 계약 | Planning preflight 이후 | `BLOCKED` | `NOT_RUN` | `NOT_RUN` |

## 6. Decision 9 구현 검수 목표

- 평상시 HUD에 상점·이동권 대형 게이지·중복 식량 카운터가 없다.
- 이동권은 룰렛 안에서 보관형 n/3과 럭키 무료 이동으로 구분된다.
- 룰렛은 릴 또는 행을 선택한 뒤 방향 미리보기와 실행을 제공한다.
- TokenSource가 초당 생산이 아니라 현재 릴 구성에 결속된다는 점을 이해할 수 있다.
- 병종 Tier와 완성선 기반 보상 등급을 혼동하지 않는다.
- Stage 종료 정비시간에 상인이 등장하고 상시 상점은 없다.
- 건물 카드에 지속 유지비가 없다.
- 지휘소는 전역 아군 오라로, 마력탑은 마석 지원 건물로 읽힌다.
- 벨루는 전장을 가리지 않고 우측 하단에서 짧은 상황 조언을 제공한다.

## 7. CI 호환 회귀 기록

`OMW-AUD-261`에서 중앙 문서 간소화로 Legacy C1·Vertical Slice 상태·Review·Pilot 라우팅 marker가 누락되어 CI가 실패했다. 복구 후 non-counter 유지보수로 기록했다.

```text
CURRENT_IMPLEMENTATION_STATUS restore commit = 1cca3bdb4a278aa741e4112a5c16970472daa9bb
DOCUMENTATION_MAP restore commit = 601be3bb5a885b8ada966621b994973accf17577
```

## 8. 남은 차단 요인

```text
ART_DIRECTION_IMAGE_PROTOTYPE_BRIEF = PENDING_USER_DECISION
IMAGE_PRODUCTION = PAUSED_BY_USER
CORE_FUN_AND_CONTENT_DEEPENING = CONTINUES_AFTER_VISUAL_PREFLIGHT
CODEX_IMPLEMENTATION_PLAN = BLOCKED_UNTIL_PLANNING_HANDOFF
PRODUCT_CODE_AUTHORITY = NONE
```

## 9. 다음 Gate

```text
GRILL_ME_COUNT = 9/10
NEXT_DECISION = OMW-DEC-20260804-PLANNING-ART-DIRECTION-AND-IMAGE-PROTOTYPE-BRIEF-V1
NEXT_PREFLIGHT = AT_10_OF_10
```
