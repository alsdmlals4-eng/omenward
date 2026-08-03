# OMENWARD 프로젝트 인수인계 컨텍스트

```yaml
updated_at: 2026-08-04
project: OMENWARD / 오멘워드
work_mode: TOTAL_PLANNING
phase: COMBAT_HUD_ROULETTE_RESOURCE_MERCHANT_BUILDING_ROSTER_APPROVED
current_validation_decision: OMW-DEC-20260804-PLANNING-COMBAT-HUD-REEL-AND-BUILD-UX-V1
current_process_policy: OMW-PROC-20260804-PLANNING-VISUALS-CODEX-IMPLEMENTATION-BOUNDARY-V1
working_branch: gpt/omenward-simulation-harness-planning-20260803
current_grill_me_count: 9_OF_10
product_code_authority: NONE
image_production_authority: PAUSED_BY_USER
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
design/APPROVED_OMENWARD_COMBAT_HUD_ROULETTE_RESOURCE_MERCHANT_AND_BUILDING_ROSTER_2026-08-04.md
```

전체 시스템 제품 범위는 `design/APPROVED_VERTICAL_SLICE_SYSTEM_CONTRACT_2026-07-27.md`가 소유한다. Decision 9와 충돌하는 HUD·자원·상인·건물 조항은 최신 Decision 9 정본이 우선한다.

## 2. 제품 코어

```text
예고된 세 전선 공세
→ 제한된 건물·TokenSource로 세 원형 릴 설계
→ SpinSnapshot 이동·결과 확정
→ 보관·판매·한 전선 비가역 배치
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

## 4. 승인된 전투 공간·카메라

```text
THREE_FRONTS = TOP / MID / BOTTOM
VISIBLE_MAIN_ROUTE_PER_FRONT
VISIBLE_BYPASS_AND_AIR_ROUTES
CAMERA = PC 16:9 HIGH_ANGLE_THREE_QUARTER_STRATEGY
THREE_FRONTS_VISIBLE = REQUIRED
FORCED_CAMERA_MOVEMENT = MINIMIZED
```

- Ground는 전열·후열·혼잡을 형성한다.
- Flying은 Ground 혼잡을 넘지만 전선·Target 규칙을 무시하지 않는다.
- 침투 병력은 순간이동이 아니라 보이는 우회로를 사용한다.
- Boss·Danger 연출은 다른 전선을 숨기지 않는다.

## 5. 승인된 HUD·룰렛·자원

평상시 하단:

```text
[룰렛] [보관함] [건설] [전술스킬] [벨루]
```

- 상시 상점 버튼은 없다.
- 벨루는 우측 하단 초상과 짧은 상황 대사로 사용한다.
- 평상시 자원은 골드·마석·배치 병력/병력 한도다.
- 이동권은 룰렛 안에서만 `보관 이동권 n/3`과 럭키 무료 이동으로 표시한다.
- 건물별 지속 유지비와 토큰 초당 공급 표시는 없다.
- 병종 Tier와 완성선 기반 보상 등급을 분리한다.

룰렛 이동:

```text
릴 선택 → 위/아래 미리보기 → 세로 이동 실행
행 선택 → 왼쪽/오른쪽 미리보기 → 가로 이동 실행
```

## 6. 승인된 상인·건물 6종

```text
Stage 정산
→ 정비시간
→ 유한 재고 상인 거래
→ 미션·선택지
→ 다음 Stage
```

기본 건물:

| 건물 | 역할 |
|---|---|
| 금고 | 골드 수입 + 금화 TokenSource |
| 농장 | 병력 한도 확장 |
| 병영 | 병종 TokenSource·Tier 성장 |
| 방어탑 | 전선 직접 공격 |
| 지휘소 | 현재 MapRun 전체 아군 병력 오라 |
| 마력탑 | 마석 수급·최대 보유량 강화 |

- 같은 지휘소 계열은 최고 Tier만 적용한다.
- 돌격 지휘소와 수비 지휘소는 함께 활성화할 수 있다.
- 마력탑은 전술스킬을 자동 사용하지 않는다.

## 7. 이미지 상태

```text
IMAGE_GENERATION = PAUSED_BY_USER
EXISTING_GENERATED_IMAGES = CONCEPT_REFERENCE_ONLY / NOT_CANON
```

10/10에서는 추가 이미지를 만들지 않고 아트 방향과 최종 Brief를 텍스트로 확정한다.

## 8. 적대적 감사

```text
OMW-AUD-208~289 = 기존 검증·수치·전투 감사
OMW-AUD-290~299 = 기술 과잉 정본화·Route·Targeting·이미지 가독성 감사
OMW-AUD-300~313 = 카메라·시각 계층·정보 밀도·핵심 재미 우선순위 감사
OMW-AUD-314~330 = HUD·룰렛·자원·상인·건물 역할 감사
```

## 9. 현재 금지선

```text
CURRENT_PRODUCT = LEGACY_PROTOTYPE
LATEST_APPROVED = COMBAT_HUD_ROULETTE_RESOURCE_MERCHANT_BUILDING_ROSTER_DOCUMENTED_NOT_IMPLEMENTED
PRODUCT_CODE = UNCHANGED
SIMULATION_TOOL_CODE = NOT_AUTHORIZED
IMAGE_ANIMATION_HX = PAUSED_BY_USER
BALANCE_CONCLUSION = FORBIDDEN
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
```

## 10. 다음 작업

```text
10/10 아트 방향·최종 이미지 Brief
→ preflight·적대적 검토
→ merge readiness
→ 핵심 재미·콘텐츠 기획 심화
→ Codex 구현 계약
```

다음 Decision:

`OMW-DEC-20260804-PLANNING-ART-DIRECTION-AND-IMAGE-PROTOTYPE-BRIEF-V1`
