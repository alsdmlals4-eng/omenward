# 오멘워드 현재 구현 상태

- 갱신일: 2026-08-04
- 전체 시스템 정본: `docs/design/APPROVED_VERTICAL_SLICE_SYSTEM_CONTRACT_2026-07-27.md`
- 작업 모드: `TOTAL_PLANNING / CORE_FUN_CONTENT_VISUAL_PROFILE`
- 최신 기획 상태: `USER_APPROVED_ACTIVE_BRANCH_NOT_IMPLEMENTED`
- 현재 Decision: `OMW-DEC-20260804-PLANNING-BATTLEFIELD-VISUAL-HIERARCHY-AND-CAMERA-V1`
- 운영 정책: `OMW-PROC-20260804-PLANNING-VISUALS-CODEX-IMPLEMENTATION-BOUNDARY-V1`
- 제품 코드 승인: `NOT_AUTHORIZED`
- 이미지 제작 승인: `NOT_AUTHORIZED_UNTIL_10_OF_10_PREFLIGHT`

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
LATEST_APPROVED_PLANNING = BATTLEFIELD_VISUAL_HIERARCHY_CAMERA_DOCUMENTED_NOT_IMPLEMENTED
PRODUCT_CODE = UNCHANGED
SIMULATION_TOOL_CODE = NOT_AUTHORIZED
IMAGE_PRODUCTION = NOT_AUTHORIZED
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
```

문서 계약과 CI 통과는 최신 Vertical Slice·전투 시스템·카메라·이미지가 구현됐다는 뜻이 아니다.

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
```

### P7 플레이어 시각 규칙

```text
CAMERA = PC 16:9 HIGH_ANGLE_THREE_QUARTER_STRATEGY
THREE_FRONTS_VISIBLE = REQUIRED
FORCED_CAMERA_MOVEMENT = MINIMIZED
FRONT_FLOW_BEFORE_UNIT_DETAIL = REQUIRED
```

- 전투 공간 약 70~75%, 하단 HUD 약 25~30%를 기획 목표로 한다.
- 위험·우회·거점 변화가 개별 피해 숫자보다 먼저 보인다.
- 모든 체력바·Status·Target 선은 상시 노출하지 않는다.
- Boss·Danger 연출은 다른 전선을 숨기지 않는다.

## 5. 구현 상태 행렬

| 영역 | 기획 상태 | 제품 구현 | 자동 검증 | 사람 검증 |
|---|---|---|---|---|
| 20 Stage 전체 시스템 Vertical Slice | 승인 정본 존재 | `NOT_STARTED` | `NOT_RUN_LATEST` | `NOT_RUN` |
| 결정론·공통 전투 참고 계약 | 플레이어 결과 요구 승인 | `NOT_STARTED` | `NOT_RUN` | `NOT_RUN` |
| Damage·Protection·Status | 플레이어 의미 승인 | `NOT_STARTED` | `NOT_RUN` | `NOT_RUN` |
| 방어·Barrier·Modifier | 기획 기본값 승인 | `NOT_STARTED` | `NOT_RUN` | `NOT_RUN` |
| 전투 공간·Route·Targeting | 플레이 경험 승인 | `NOT_STARTED` | `NOT_RUN` | `NOT_RUN` |
| 전장 시각 계층·카메라 | 플레이 경험 승인 | `NOT_STARTED` | `NOT_RUN` | `NOT_RUN` |
| HUD·룰렛·건설 UX | 미확정 9/10 | `BLOCKED` | `NOT_RUN` | `NOT_RUN` |
| 아트·이미지 Prototype Brief | 미확정 10/10 | `BLOCKED` | `NOT_RUN` | `NOT_RUN` |
| 실제 이미지·Animation·HX | 후속 Gate | `NOT_STARTED` | `N/A` | `NOT_RUN` |
| 핵심 재미·콘텐츠 심화 | Visual preflight 이후 계속 | `N/A` | `NOT_RUN` | `NOT_RUN` |
| Codex 구현 계약 | Planning preflight 이후 | `BLOCKED` | `NOT_RUN` | `NOT_RUN` |

## 6. Decision 8 이미지 검수 목표

- 정지 화면에서 세 전선의 우세·열세를 비교할 수 있다.
- 양측 본진·거점·건물·주요 교전 위치가 동시에 식별된다.
- Ground 전열·후열, Flying, 우회 침투가 서로 다른 층으로 읽힌다.
- 위험 경고를 보고 어느 전선과 위치가 문제인지 즉시 찾을 수 있다.
- 영웅·Boss 연출 중에도 다른 전선 위험을 놓치지 않는다.
- 화면의 화려함보다 룰렛 배치 결과와 전선 판단이 먼저 보인다.

## 7. CI 호환 회귀 기록

`OMW-AUD-261`에서 중앙 문서 간소화로 Legacy C1·Vertical Slice 상태·Review·Pilot 라우팅 marker가 누락되어 CI가 실패했다. 복구 후 non-counter 유지보수로 기록했다.

```text
CURRENT_IMPLEMENTATION_STATUS restore commit = 1cca3bdb4a278aa741e4112a5c16970472daa9bb
DOCUMENTATION_MAP restore commit = 601be3bb5a885b8ada966621b994973accf17577
```

## 8. 남은 차단 요인

```text
COMBAT_HUD_REEL_BUILD_UX = PENDING_USER_DECISION
ART_DIRECTION_IMAGE_PROTOTYPE_BRIEF = PENDING_USER_DECISION
IMAGE_PRODUCTION = BLOCKED_UNTIL_10_OF_10_PREFLIGHT
CORE_FUN_AND_CONTENT_DEEPENING = CONTINUES_AFTER_VISUAL_PREFLIGHT
CODEX_IMPLEMENTATION_PLAN = BLOCKED_UNTIL_PLANNING_HANDOFF
PRODUCT_CODE_AUTHORITY = NONE
```

## 9. 다음 Gate

```text
GRILL_ME_COUNT = 8/10
NEXT_DECISION = OMW-DEC-20260804-PLANNING-COMBAT-HUD-REEL-AND-BUILD-UX-V1
NEXT_PREFLIGHT = AT_10_OF_10
```
