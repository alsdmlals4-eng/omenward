# 오멘워드 기획 정본 결정 원장

```yaml
updated_at: 2026-08-04
status: CURRENT_DECISION_LEDGER / ACTIVE_PLANNING_BRANCH
current_planning_decision: OMW-DEC-20260804-PLANNING-COMBAT-HUD-REEL-AND-BUILD-UX-V1
current_process_policy: OMW-PROC-20260804-PLANNING-VISUALS-CODEX-IMPLEMENTATION-BOUNDARY-V1
work_mode: TOTAL_PLANNING
current_count: 9_OF_10
product_code_authority: NONE
image_production_authority: PAUSED_BY_USER
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
| 9 | `OMW-DEC-20260804-PLANNING-COMBAT-HUD-REEL-AND-BUILD-UX-V1` | HUD·룰렛 정보·골드/마석/병력 한도·Stage 종료 상인·6종 건물·벨루 | UI Scene·입력·데이터 구조는 Codex 결정 |

## 3. 비카운트 운영 정책

`OMW-PROC-20260804-PLANNING-VISUALS-CODEX-IMPLEMENTATION-BOUNDARY-V1`

```text
GPT / Work = core fun, content planning, player experience, visuals and art
Codex = implementation architecture and code
```

이는 Decision 수에 포함하지 않는 standing policy다.

## 4. Decision 9 핵심 정본

```text
BOTTOM_FUNCTIONS = ROULETTE / STORAGE / BUILD / TACTICAL_SKILL / BELU
SHOP_BUTTON = REMOVED
MAIN_HUD_RESOURCES = GOLD / MANA_STONE / DEPLOYED_TROOP_CAPACITY
MOVE_TICKET_DISPLAY = ROULETTE_PANEL_ONLY
MERCHANT = AFTER_STAGE_MAINTENANCE_ONLY
```

룰렛:

- 세 릴은 세 전선과 직접 대응하지 않는다.
- 토큰은 초당 공급되지 않고 활성 TokenSource가 세 릴에 결속한다.
- 릴 또는 행을 먼저 선택한 뒤 이동 방향을 미리보고 실행한다.
- 이동권은 룰렛 안에서 `보관 이동권 n/3`과 럭키 무료 이동으로 분리한다.
- 병종 Tier와 완성선 기반 보상 등급을 별도 정보로 설명한다.

건물:

```text
금고 / 농장 / 병영 / 방어탑 / 지휘소 / 마력탑
```

- 건물별 지속 유지비는 없다.
- 농장은 병력 한도를 확장한다.
- 지휘소는 현재 MapRun 전체 아군 배치 병력에 전역 오라를 제공한다.
- 같은 지휘소 계열은 최고 Tier만 적용하며 돌격·수비 계열은 공존할 수 있다.
- 마력탑은 전술스킬 자원인 마석 수급 또는 최대 보유량을 강화한다.
- 벨루는 우측 하단에서 상황과 선택 근거만 알려준다.

## 5. 충돌 대체 규칙

Decision 9는 다음 기존 표현을 대체한다.

```text
5종 기본 건물 목록
농장의 별도 초당 식량 자원 UI
지휘소 주변 반경 오라
평상시 상점 버튼
전투 중 상점 이동권 반복 구매
평상시 이동권 7/10 게이지
토큰 초당 공급량
독립 희귀도 확률표
건물별 지속 유지비
벨루 목록형 메뉴
```

## 6. 적대적 감사 계보

```text
OMW-AUD-208~289 = Decisions 1~6 and maintenance findings
OMW-AUD-290~299 = planning/implementation boundary and combat-space readability
OMW-AUD-300~313 = visual hierarchy, camera, information density and core-fun priority
OMW-AUD-314~330 = HUD, roulette, resources, merchant and building-role integrity
```

## 7. 현재 금지선

```text
CURRENT_PRODUCT = LEGACY_PROTOTYPE
PRODUCT_CODE = UNCHANGED
SIMULATION_TOOL_CODE = NOT_AUTHORIZED
IMAGE_PRODUCTION = PAUSED_BY_USER
BALANCE_CONCLUSION = FORBIDDEN
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
```

## 8. 다음 Decision

```text
10/10 OMW-DEC-20260804-PLANNING-ART-DIRECTION-AND-IMAGE-PROTOTYPE-BRIEF-V1
NEXT_PREFLIGHT = AT_10_OF_10
```
