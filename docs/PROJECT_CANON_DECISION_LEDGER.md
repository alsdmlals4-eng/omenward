# 오멘워드 기획 정본 결정 원장

```yaml
updated_at: 2026-08-04
status: CURRENT_DECISION_LEDGER / ACTIVE_PLANNING_BRANCH
current_planning_decision: OMW-DEC-20260804-PLANNING-BATTLEFIELD-VISUAL-HIERARCHY-AND-CAMERA-V1
current_process_policy: OMW-PROC-20260804-PLANNING-VISUALS-CODEX-IMPLEMENTATION-BOUNDARY-V1
work_mode: TOTAL_PLANNING
current_count: 8_OF_10
product_code_authority: NONE
image_production_authority: NONE
```

## 1. 운영 원칙

- GitHub APPROVED 문서가 기획 정본이다.
- Google Sheet는 사용자 가시 GDD이며 같은 Decision ID와 exact PR HEAD로 동기화한다.
- GPT는 핵심 재미·콘텐츠 기획·플레이어 경험·UX·이미지·아트 Brief를 소유한다.
- Codex는 자료구조·알고리즘·좌표·경로탐색·성능·코드·테스트 구현을 소유한다.
- GPT는 기술 세부보다 핵심 재미와 콘텐츠 구조를 먼저 검토한다.
- Codex 구현이 핵심 재미·콘텐츠 역할·플레이어 경험을 바꾸면 Grill Me로 되돌린다.
- 10개 승인 Decision마다 preflight·적대적 검토를 수행한다.

## 2. 현재 승인 결정

| 순번 | Decision ID | 기획 정본 | 구현 세부 상태 |
|---:|---|---|---|
| 1 | `OMW-DEC-20260803-VALIDATION-DETERMINISTIC-SIMULATION-HARNESS-SCOPE-V1` | 결과 재현·원인 복기 요구 | Harness 구조·Schema는 Codex 참고안 |
| 2 | `OMW-DEC-20260803-VALIDATION-COMMON-COMBAT-SCHEMA-AND-RESOLUTION-ORDER-V1` | 동일 조건 공정성·숨은 선공 금지 | phase·정렬·상태 구조는 Codex 참고안 |
| 3 | `OMW-DEC-20260803-VALIDATION-DAMAGE-PROTECTION-AND-STATUS-SEMANTICS-V1` | KINETIC/ARCANE·Barrier·Status 의미 | 내부 Resolver는 Codex 결정 |
| 4 | `OMW-DEC-20260803-VALIDATION-MITIGATION-FORMULA-AND-PROTECTION-NUMERIC-DEFAULTS-V1` | 방어 감소 곡선·Barrier·Status 기획 기본값 | 정수식·표현 방식은 Codex 결정 |
| 5 | `OMW-DEC-20260803-VALIDATION-FIXED-TICK-TIME-AND-ACTIVATION-DEFAULTS-V1` | 전투 템포·Spawn 선공/무적 금지 | 30 TPS·Tick 저장은 Codex 참고안 |
| 6 | `OMW-DEC-20260803-VALIDATION-MODIFIER-STACKING-AND-EFFECT-PRECEDENCE-V1` | Buff 폭증 방지·효과 가독성 | basis point·phase·Snapshot 저장은 Codex 참고안 |
| 7 | `OMW-DEC-20260804-PLANNING-COMBAT-SPACE-ROUTE-AND-TARGETING-EXPERIENCE-V1` | 세 전선·명시적 Route·Targeting·이미지 요구 | 좌표·Pathfinding·충돌은 Codex 결정 |
| 8 | `OMW-DEC-20260804-PLANNING-BATTLEFIELD-VISUAL-HIERARCHY-AND-CAMERA-V1` | 고각도 3/4 카메라·정보 우선순위·전장 가독성 | Camera transform·FOV·Occlusion은 Codex 결정 |

## 3. 비카운트 운영 정책

`OMW-PROC-20260804-PLANNING-VISUALS-CODEX-IMPLEMENTATION-BOUNDARY-V1`

```text
GPT / Work = core fun, content planning, player experience, visuals and art
Codex = implementation architecture and code
```

이는 Decision 수에 포함하지 않는 standing policy다.

## 4. Decision 8 핵심 정본

```text
CAMERA = PC 16:9 HIGH_ANGLE_THREE_QUARTER_STRATEGY
THREE_FRONTS_VISIBLE = REQUIRED
BATTLEFIELD_SHARE = ABOUT_70_TO_75_PERCENT
BOTTOM_HUD_SHARE = ABOUT_25_TO_30_PERCENT
FORCED_CAMERA_MOVEMENT = MINIMIZED
```

정보 순서:

```text
전선 흐름
→ 우회·침투·공중 위협
→ 본진·거점·건물 상태
→ 영웅·전설·핵심 병종 역할
→ 개별 피해·세부 Status
```

- 모든 체력바·Status·Target 선을 상시 표시하지 않는다.
- Boss·Danger 연출은 다른 전선을 숨기지 않는다.
- 주 경로·우회로·공중 Route는 별도 시각 언어를 사용한다.
- 화면의 화려함보다 룰렛 배치 결과와 전선 판단이 먼저 보인다.

## 5. 적대적 감사 계보

```text
OMW-AUD-208~289 = Decisions 1~6 and maintenance findings
OMW-AUD-290~299 = planning/implementation boundary and combat-space readability
OMW-AUD-300~313 = visual hierarchy, camera, information density and core-fun priority
```

## 6. 현재 금지선

```text
CURRENT_PRODUCT = LEGACY_PROTOTYPE
PRODUCT_CODE = UNCHANGED
SIMULATION_TOOL_CODE = NOT_AUTHORIZED
IMAGE_PRODUCTION = NOT_AUTHORIZED_UNTIL_10_OF_10_PREFLIGHT
BALANCE_CONCLUSION = FORBIDDEN
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
```

## 7. 다음 Decision

```text
9/10 OMW-DEC-20260804-PLANNING-COMBAT-HUD-REEL-AND-BUILD-UX-V1
10/10 OMW-DEC-20260804-PLANNING-ART-DIRECTION-AND-IMAGE-PROTOTYPE-BRIEF-V1
NEXT_PREFLIGHT = AT_10_OF_10
```
