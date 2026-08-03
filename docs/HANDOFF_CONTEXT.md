# OMENWARD 프로젝트 인수인계 컨텍스트

```yaml
updated_at: 2026-08-04
project: OMENWARD / 오멘워드
work_mode: TOTAL_PLANNING
phase: BATTLEFIELD_VISUAL_HIERARCHY_AND_CAMERA_APPROVED
current_validation_decision: OMW-DEC-20260804-PLANNING-BATTLEFIELD-VISUAL-HIERARCHY-AND-CAMERA-V1
current_process_policy: OMW-PROC-20260804-PLANNING-VISUALS-CODEX-IMPLEMENTATION-BOUNDARY-V1
working_branch: gpt/omenward-simulation-harness-planning-20260803
current_grill_me_count: 8_OF_10
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
design/APPROVED_OMENWARD_BATTLEFIELD_VISUAL_HIERARCHY_AND_CAMERA_2026-08-04.md
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

## 3. GPT 역할 — 반드시 유지

```text
GPT / Work
= 핵심 재미·플레이 동기·콘텐츠 기획·플레이어 규칙·UX·이미지·아트 방향·검수 기준

Codex
= 자료구조·알고리즘·좌표·경로탐색·물리·성능·코드·테스트 구현
```

GPT 작업 우선순위:

```text
핵심 재미
→ 콘텐츠 구조와 역할
→ UX·이미지·아트
→ 구현 결과 조건
```

기술 구현 논의가 핵심 재미·콘텐츠·이미지 논의를 밀어내면 즉시 범위를 교정한다. 과거 문서의 `30 TPS`, R00~R130, 정수 좌표·시간, basis point, Schema·정렬 키는 Codex 참고안이며 구현 구속력이 없다.

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

## 5. 현재 승인된 카메라·시각 계층

```text
CAMERA = PC 16:9 HIGH_ANGLE_THREE_QUARTER_STRATEGY
THREE_FRONTS_VISIBLE = REQUIRED
BATTLEFIELD_SHARE = ABOUT_70_TO_75_PERCENT
BOTTOM_HUD_SHARE = ABOUT_25_TO_30_PERCENT
FORCED_CAMERA_MOVEMENT = MINIMIZED
```

정보 우선순위:

```text
전선 우세·열세
→ 우회·침투·공중 위협
→ 본진·거점·건물 상태
→ 영웅·전설·핵심 병종 역할
→ 개별 피해·세부 Status
```

- Boss·Danger 연출은 다른 전선을 숨기지 않는다.
- 모든 체력바·Status·Target 선을 상시 표시하지 않는다.
- 주 경로·우회로·공중 Route는 별도 시각 언어를 가진다.
- 화면의 화려함보다 룰렛 배치 결과와 전선 판단이 먼저 보인다.

## 6. 이미지 요구

후속 Prototype은 최소 다음 4종이다.

```text
1. 기본 고각도 3/4 전략 화면
2. 위험 전선·우회 위협 화면
3. 전열·후열·Flying·영웅 교전 확대
4. Danger/Boss 긴장 화면
```

분위기만 좋은 Concept Art가 아니라 핵심 재미와 실제 GDD를 설명하는 이미지여야 한다.

## 7. 적대적 감사

```text
OMW-AUD-208~289 = 기존 검증·수치·전투 감사
OMW-AUD-290~299 = 기술 과잉 정본화·Route·Targeting·이미지 가독성 감사
OMW-AUD-300~313 = 카메라·시각 계층·정보 밀도·핵심 재미 우선순위 감사
```

Decision 8 주요 위험:

- 낮은 카메라로 세 전선을 놓침.
- 완전 탑다운으로 전장 존재감 소실.
- 강제 카메라 이동이 판단권을 빼앗음.
- 모든 체력바·Status·Target 선이 화면을 덮음.
- Boss 연출이 다른 전선 위험을 숨김.
- Concept Art와 실제 인게임 구도가 불일치.
- 기술 논의가 핵심 재미·콘텐츠 기획을 대체.

## 8. 현재 금지선

```text
CURRENT_PRODUCT = LEGACY_PROTOTYPE
LATEST_APPROVED = BATTLEFIELD_VISUAL_HIERARCHY_CAMERA_DOCUMENTED_NOT_IMPLEMENTED
PRODUCT_CODE = UNCHANGED
SIMULATION_TOOL_CODE = NOT_AUTHORIZED
IMAGE_ANIMATION_HX = NOT_AUTHORIZED_UNTIL_10_OF_10_PREFLIGHT
BALANCE_CONCLUSION = FORBIDDEN
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
```

## 9. 다음 작업

```text
9/10 전투 HUD·룰렛·건설·전술 UX
10/10 아트 방향·이미지 Prototype Brief
→ preflight·적대적 검토
→ 이미지 제작
→ 핵심 재미·콘텐츠 기획 심화
→ Codex 구현 계약
```

다음 Decision:

`OMW-DEC-20260804-PLANNING-COMBAT-HUD-REEL-AND-BUILD-UX-V1`
