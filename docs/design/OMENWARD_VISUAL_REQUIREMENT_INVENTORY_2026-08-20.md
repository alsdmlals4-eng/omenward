# OMENWARD Visual Requirement Inventory · 2026-08-20

```yaml
status: ON_HOLD_PENDING_USER_REFERENCE_FILES
inventory_id: OMW-VISINV-20260820-01
planning_contract: PROJECT_TOTAL_PLANNING_IMPLEMENTATION_AND_DELIVERY_INSTRUCTION_v4.7
source_decisions:
  - OMW-PLAN-20260820-WORLD-ROLE-01
  - OMW-PLAN-20260820-MAPRUN-WORLD-01
  - OMW-PLAN-20260820-PRESSURE-LANGUAGE-01
  - OMW-PLAN-20260820-MOBILIZATION-REGISTRY-01
  - OMW-PLAN-20260820-FIRST5-FTUE-01
  - OMW-PLAN-20260820-RUN-COMMAND-SHELL-01
first_generation_decision: OMW-PLAN-20260820-VISUAL-NORTH-STAR-01
first_generation_option: OPTION_A_APPROVED
visual_asset_generated: true
visual_asset_approved: false
generated_candidate_disposition: REJECTED_NOT_CANON
visual_generation_paused: true
pause_reason: USER_WILL_PROVIDE_LOCAL_MOCKUP_REFERENCE_FILES
runtime_mutation: NONE
```

이 문서는 구현용 자산 승인이 아니라 **어떤 시각 자료가 먼저 있어야 기획·UX·전장·세계관을 검증할 수 있는지**를 정리한 Inventory다.

2026-08-20 첫 North Star A안 생성 시도는 사용자가 요구한 **더 강한 도트·픽셀감이 실질적으로 반영되지 않았다고 판단하여 미승인/비정본 처리**한다. 해당 결과는 Visual Bible, Asset Library, 구현 reference로 승격하지 않는다.

현재 이미지 관련 작업은 사용자가 집에 보유한 기존 시안/레퍼런스 파일을 제공할 때까지 보류한다. 파일을 받기 전에는 새 이미지 생성·수정·대체 시안을 진행하지 않는다.

## 1. 기존 시각 불변 조건

기존 승인 아트/UI 계약을 유지한다.

```text
STYLE = 클린 전술 픽셀 + 미니어처 치비 픽셀 + 제한된 고급 조명
OUTPUT_REFERENCE = 1920x1080 16:9
INTERNAL_PIXEL_REFERENCE = 960x540 candidate / integer upscale
FULL_BATTLEFIELD = 양측 본진 + 세 라인 전체를 기본 전략 줌에서 확인
MINIMAP = NONE
AI_GENERATED_LOOK_REDUCTION = REQUIRED
STYLE_CONSISTENCY_AND_READABILITY = REQUIRED
WORLD_CORE_SYSTEM_FIT = REQUIRED
```

추가 보호:

- 전장 정보는 가능한 한 실제 월드 위치에 붙인다.
- 색상만으로 진영·병종·Pressure를 구분하지 않는다.
- 카지노·슬롯머신·잭팟·칩·레버 문법을 Omen Wheel의 핵심 시각 언어로 쓰지 않는다.
- 금장·광택·발광을 모든 UI와 일반 유닛에 상시 사용하지 않는다.
- 픽셀 그리드 위에 매끈한 생성형 명암만 얹은 형태를 피한다.
- 최종 자산은 1280x720 축소에서도 핵심 전선·병종·위협을 읽을 수 있어야 한다.
- 사용자가 제공할 기존 시안의 **도트 밀도, 픽셀 경계, 색군, UI 프레임, 전장 배치**를 먼저 분석한 뒤 현재 규칙과 충돌 여부를 판단한다.

## 2. Visual Requirement Inventory

### P0 · Core-experience North Star

| Asset ID | 시각 자료 | 검증 목적 | 상태 |
|---|---|---|---|
| `OMW-VIS-001` | Run Command Screen · PREPARE North Star | 세계·3전선·Forecast·건물·동원 인장·Omen Wheel·정보 계층을 한 장에서 검증 | OPTION A APPROVED / GENERATION PAUSED |
| `OMW-VIS-002` | COMMIT Focus Mode | 획득 병력과 세 전선의 공간적 비가역 배치 가독성 | DEFERRED AFTER 001 |
| `OMW-VIS-003` | BATTLE Focus Mode | 세 라인 전황·병종 실루엣·Signature·마력 전술의 전투 중 가독성 | DEFERRED AFTER 002 |
| `OMW-VIS-004` | REVIEW Focus Mode | Forecast→준비→배치→사건→대응→결과 인과 설명 | DEFERRED AFTER 003 |
| `OMW-VIS-005` | Ward Citadel / 3-lane battlefield clean plate | UI 없는 전장 구조·건물 위치·게이트·중간거점·접전지·우회로 기본 시각 | DEFERRED |

### P0 · Core mechanic visual language

| Asset ID | 시각 자료 | 검증 목적 |
|---|---|---|
| `OMW-VIS-006` | Triple Omen Wheels focus close-up | 세 릴=중앙 삼중 동원 장치, 세 전선과 1:1 비대응, 도박 비주얼 회피 |
| `OMW-VIS-007` | Omen Signature icon sheet | MASS / ARMORED / FLYING / INFILTRATION / SIEGE를 형태로 구분 |
| `OMW-VIS-008` | Mobilization Seal / TokenSource feedback | 건물 건설→자동생산 + 동원 인장 등록이라는 두 출력 구분 |

### P1 · Production readability

| Asset ID | 시각 자료 | 검증 목적 |
|---|---|---|
| `OMW-VIS-009` | 7 building family silhouette board | 금고/농장/일반병영/특수병영/방어탑/지휘소/마력탑 식별과 Tier 성장 |
| `OMW-VIS-010` | 10 troop archetype silhouette lineup | 34~56px 전략 줌에서 역할 실루엣 검증, Giant는 별도 크기 위계 |
| `OMW-VIS-011` | Ally vs Veil faction visual pair board | 같은 역할의 양 진영 Visual Set이 색만이 아니라 형태 언어로 구분되는지 검증 |
| `OMW-VIS-012` | Stage 1 FTUE build-group cue sheet | 생존 기반 / 군사 기반 / 지휘 기반 3묶음의 단계적 강조 |

### P2 · Content expansion

- Elite / Hero / Legendary / Mythic boss hierarchy board
- Merchant / reward / growth surface
- Special Barracks T1 assigned-corps reveal and T2 specialization
- assassin bypass omen/fog warning
- gate damage / siege warning / capture state VFX
- biome / Ward Citadel expansion kit

## 3. 첫 생성 후보 · OMW-PLAN-20260820-VISUAL-NORTH-STAR-01

### A · 승인 — `OMW-VIS-001 Stage 2 PREPARE · Omen Wheels Focus`

한 장에서 가장 많은 핵심 가설을 검증한다.

Scene intent:

```text
Stage 2 PREPARE
→ 세 전선 전체와 양측 거점이 보이는 전략 줌
→ 상단에 3-lane Forecast/Omen Signature 요약
→ 아군 Ward Citadel과 현재 건물 상태
→ 선택한 T2 후보의 현재→변경 후 동원 방향 preview
→ 세 Omen Wheels가 PREPARE focus layer로 열림
→ Wheel은 전선별 릴이 아니라 중앙 삼중 동원 장치로 표현
```

검증 가능한 질문:

1. 한눈에 세 전선을 읽을 수 있는가?
2. Forecast가 전장을 가리지 않고 전선별로 연결되는가?
3. 건물→TokenSource/동원 인장→Wheel의 인과가 보이는가?
4. Omen Wheel이 카지노보다 군사/징조 장치로 읽히는가?
5. Pixel battlefield와 UI가 같은 작품처럼 보이는가?
6. 항상 표시 / 현재 Focus / 상세 정보의 위계가 읽히는가?
7. 1280x720 축소에서도 무엇을 해야 하는지 남는가?

첫 생성 시도 결과:

```text
RESULT = REJECTED_NOT_CANON
USER_FEEDBACK = stronger dot + pixel feeling was requested but the visible result was effectively unchanged
PROMOTION = FORBIDDEN
RETRY_NOW = FORBIDDEN_UNTIL_USER_REFERENCE_FILES
```

### B · `OMW-VIS-003 BATTLE Focus North Star`

장점:
- 3전선 전황과 10병종 실루엣, 적/아군 진영 구분을 가장 잘 검증한다.
- 전술 개입과 자동전투 가독성을 직접 볼 수 있다.

약점:
- OMENWARD만의 건물→확률→Omen Wheel 정체성이 거의 보이지 않는다.
- 첫 대표 이미지로 쓰면 일반 3라인 오토배틀러처럼 보일 위험이 있다.

### C · `OMW-VIS-006 Triple Omen Wheels / Command Sanctum`

장점:
- 프로젝트 고유 메커니즘과 `Omen Warden` 세계관을 가장 강하게 보여준다.
- 도박 문법을 제거한 룰렛의 형태 언어를 집중 검증할 수 있다.

약점:
- 전장·배치·자동전투가 보이지 않아 게임 전체 North Star가 되기 어렵다.
- 메타 장치나 별도 미니게임처럼 오해될 위험이 있다.

## 4. 사용자 시안 수신 후 재개 절차

```text
USER_LOCAL_REFERENCE_FILES
→ 파일 자체를 요청 근거로 검토
→ 현재 A안 구조와 공통점/충돌점 비교
→ 도트 크기 / 픽셀 밀도 / 팔레트 / 윤곽 / UI 프레임 / 전장 구성 / 룰렛 형태 언어 추출
→ 재사용 가능한 요소와 프로젝트 전용 요소 분리
→ 필요한 경우 A안 구성 가이드 수정
→ 사용자 명시 요청 후 이미지 생성/편집 재개
→ 정확히 한 장씩 결과 승인
→ 승인 결과만 Notion Visual Bible + Asset Library + Flow에 등록
```

사용자 파일에 없는 요소는 임의로 그 파일의 특징이라고 가정하지 않는다. 기존 시안과 현재 정본이 충돌하면 충돌을 먼저 보고하고 결정한다.

## 5. 권장 A의 화면 구성 가이드

```text
TOP STRIP
→ Stage / Wave / 핵심 자원
→ Lane A/B/C Forecast chips: primary + secondary Signature + intensity

CENTER WORLD
→ 한 화면 전체 3 horizontal lanes
→ friendly Ward Citadel / three gates / outposts / central clashes / enemy side
→ 건물과 병력은 전장 위에 직접 배치

PREPARE FOCUS LAYER
→ selected building / T2 candidate
→ before → after mobilization tendency
→ compact Triple Omen Wheels / 3x3 exposure
→ one dominant action: confirm upgrade or mobilize/spin depending exact state

ON-DEMAND ONLY
→ exact Token Ledger
→ raw weights/internal IDs
→ raw target/cause debug text
```

정확한 패널 위치·카메라 투영·아이콘 형태는 사용자 시안 검토 후 조정할 CHANGEABLE 항목이다.

## 6. Art / UI generation guardrails

### Pixel / rendering

- crisp hard pixel edges, nearest-neighbor feeling
- 1px outer silhouette logic at internal pixel scale
- 2~4 tone body shading + restrained highlight
- no painterly blur / no soft AI airbrush
- no mixed pixel density inside the same asset family
- atmospheric light only where it improves hierarchy
- **user-requested stronger dot/pixel impression must be visibly distinguishable, not merely stated in the prompt**

### Friendly faction

- vertical lines, arches, shields, bells, cloth banners
- blue-gray / navy / ivory / warm metal accent
- disciplined geometry and relatively symmetrical military structures

### Enemy / Veil

- asymmetric cracks, carapace, void holes, controlled internal glow
- dark violet / dark red / shell gray
- do not make enemy merely a recolored ally

### Omen Wheel

ADOPT:
- war seals, engraved sigils, military registry marks, omen geometry
- metal/stone/ritual-command construction
- three related circles feeding one result/exposure logic

AVOID:
- cherries, 7s, casino chip shapes, lever, jackpot lights
- giant slot-machine cabinet
- celebratory gambling confetti

### UI

- compact framed panels with clear negative space
- world-first: the battlefield remains the largest visual mass
- Signature uses icon shape + label/intensity, not color alone
- no mobile-kingdom-game oversized gold frames
- no glassmorphism or excessive glossy gradients
- generated text should be minimal; use short stable labels/icons to avoid fake UI noise

## 7. Benchmark disposition

`Mechabellum — ADAPT`
- use the principle that preparation/formation must remain spatially legible before automated combat.
- do not copy its mech UI, exact deployment grid, or competitive HUD.

`Thronefall — ADAPT`
- use the principle of keeping base defense visually readable with low interface clutter.
- do not copy its low-poly art style or day/night structure.

`Against the Storm — ADAPT`
- use explicit building output identity and readable production/state communication.
- avoid importing its settlement-management density into the core battle screen.

`The King is Watching — ADAPT`
- use the principle that economy/production and army preparation live in one coherent operating context.
- do not copy gaze mechanics or its exact pixel UI.

## 8. Generation / approval pipeline

```text
Visual Requirement Inventory
→ Option A approved
→ first generated candidate rejected as NOT_CANON
→ image work PAUSED
→ user supplies local mockup/reference files
→ source-grounded review
→ user explicitly resumes generation/editing
→ generate/edit EXACTLY ONE image
→ user reviews image
→ APPROVE / REVISE / REJECT
→ approved image only: Notion Visual Bible + Asset Library + relevant Flow surface
→ structure/layer/reusable component classification
→ next visual one at a time
```

## 9. Revisit conditions

Reopen the first North Star selection if:

- user-provided mockups establish a stronger existing layout that outperforms A;
- PREPARE screen cannot keep the three-lane battlefield readable while Omen Wheel focus is open;
- generated screen reads as generic mobile castle defense or casino roulette;
- pixel UI and battlefield art look like separate visual systems;
- 1280x720 downscale loses Forecast or lane identity;
- the first image cannot communicate `forecast → build/probability design → later lane commitment` without explanatory prose.
