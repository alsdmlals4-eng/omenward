# OMENWARD 프로젝트 인수인계 컨텍스트

```yaml
updated_at: 2026-08-04
project: OMENWARD / 오멘워드
work_mode: TOTAL_PLANNING
phase: COMBAT_SPACE_ROUTE_AND_TARGETING_EXPERIENCE_APPROVED
current_validation_decision: OMW-DEC-20260804-PLANNING-COMBAT-SPACE-ROUTE-AND-TARGETING-EXPERIENCE-V1
current_process_policy: OMW-PROC-20260804-PLANNING-VISUALS-CODEX-IMPLEMENTATION-BOUNDARY-V1
working_branch: gpt/omenward-simulation-harness-planning-20260803
current_grill_me_count: 7_OF_10
product_code_authority: NONE
image_production_authority: NONE
simulation: NOT_RUN
runtime: NOT_RUN
human_qa: NOT_RUN
```

## 1. 먼저 읽을 문서

```text
PROJECT_CORE.md
ACTIVE_CONTEXT.md
CURRENT_IMPLEMENTATION_STATUS.md
DOCUMENTATION_MAP.md
PROJECT_CANON_DECISION_LEDGER.md
DECISIONS_PENDING.md
process/APPROVED_PLANNING_VISUALS_AND_CODEX_IMPLEMENTATION_BOUNDARY_2026-08-04.md
design/APPROVED_OMENWARD_COMBAT_SPACE_ROUTE_AND_TARGETING_EXPERIENCE_2026-08-04.md
```

전체 시스템 제품 범위는 `design/APPROVED_VERTICAL_SLICE_SYSTEM_CONTRACT_2026-07-27.md`가 소유한다.

## 2. 제품 코어

```text
예고된 세 전선 공세
→ 제한된 건물·TokenSource로 세 원형 릴 설계
→ SpinSnapshot 결과
→ 비가역 전선 배치
→ 자동전투·점령·건물 운영
→ 결과 원인 복기
→ 다음 Stage 설계
```

## 3. 가장 중요한 운영 수정

```text
GPT / Work
= 기획·플레이어 규칙·콘텐츠·UX·아트 방향·이미지 Brief·검수 기준

Codex
= 자료구조·알고리즘·좌표·경로탐색·물리·성능·코드·테스트 구현
```

과거 문서의 `30 TPS`, R00~R130, 정수 좌표·시간, basis point, Schema·정렬 키는 Codex 참고안이며 구현 구속력이 없다. 플레이어가 보는 공정성·전투 템포·피해 의미·가독성·밸런스 목표는 유지한다.

## 4. 현재 승인된 전투 공간 기획

```text
THREE_FRONTS = TOP / MID / BOTTOM
VISIBLE_MAIN_ROUTE_PER_FRONT
VISIBLE_BYPASS_AND_AIR_ROUTES
DEFAULT_TARGET = nearest valid on same front/route
CROSS_LANE = explicit and telegraphed only
HIDDEN_AUTO_LANE_CHANGE = FORBIDDEN
```

- Ground는 전열·후열·혼잡을 형성한다.
- Flying은 Ground 혼잡을 넘지만 전선·Target 규칙을 무시하지 않는다.
- 침투 병력은 순간이동이 아니라 보이는 우회로를 사용한다.
- Target 변경은 플레이어가 이해 가능한 이유를 가진다.

## 5. 이미지 요구

후속 Prototype은 최소 다음 4종이다.

```text
1. 세 전선 전체 구도
2. 주 경로·우회로·공중 경로 Overlay
3. 전열·후열·Flying·Target 확대
4. Cross-lane 공격·지원 범위
```

분위기만 좋은 Concept Art가 아니라 실제 GDD를 설명하는 이미지여야 한다.

## 6. 적대적 감사

```text
OMW-AUD-208~289 = 기존 검증·수치·전투 감사
OMW-AUD-290~299 = 기술 과잉 정본화·Route·Targeting·이미지 가독성 감사
```

Decision 7 주요 위험:

- GPT가 구현 세부까지 고정.
- 자동 길찾기가 배치 의도를 변경.
- 우회 병력이 순간이동처럼 보임.
- Flying이 전역 예외가 됨.
- Cross-lane 공격이 화면 밖에서 발생.
- Target 선·범위 표시가 화면을 덮음.
- Concept Art와 실제 규칙 불일치.

## 7. 현재 금지선

```text
CURRENT_PRODUCT = LEGACY_PROTOTYPE
LATEST_APPROVED = COMBAT_SPACE_ROUTE_TARGETING_EXPERIENCE_DOCUMENTED_NOT_IMPLEMENTED
PRODUCT_CODE = UNCHANGED
SIMULATION_TOOL_CODE = NOT_AUTHORIZED
IMAGE_ANIMATION_HX = NOT_AUTHORIZED_UNTIL_10_OF_10_PREFLIGHT
BALANCE_CONCLUSION = FORBIDDEN
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
```

## 8. 다음 작업

```text
8/10 전장 시각 계층·카메라·정보 밀도
9/10 전투 HUD·룰렛·건설·전술 UX
10/10 아트 방향·이미지 Prototype Brief
→ preflight·적대적 검토
→ 이미지 제작
→ Codex 구현 계약
```

다음 Decision:

`OMW-DEC-20260804-PLANNING-BATTLEFIELD-VISUAL-HIERARCHY-AND-CAMERA-V1`
