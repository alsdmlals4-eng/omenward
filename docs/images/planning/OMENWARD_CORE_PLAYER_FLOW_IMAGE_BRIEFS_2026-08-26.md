# OMENWARD · Core Player Flow Image Brief 3-Pack

```yaml
work_package_id: OMW-VIS-BRIEF-20260826-CORE-PLAYER-FLOW-3PACK-01
status: USER_APPROVED_BRIEF_PACKAGE
approved_at: 2026-08-26
scope: PLANNING_AND_IMAGE_BRIEF_ONLY
product_code_mutation: NONE
godot_execution: NOT_IN_SCOPE
codex_execution: NOT_IN_SCOPE
image_generation: NOT_STARTED
human_visual_review: NOT_RUN
player_experience_validation: NOT_RUN
```

## 1. 목적

이 패키지는 새 gameplay 규칙을 만드는 Decision이 아니다. 이미 승인된 OMENWARD의 전장·Run Command·3×3 Roulette·COMMIT 계약을 **이미지 제작용 장면 지시문**으로 변환한다.

현재 사용자 작업 방향은 기획 + 이미지 작업이며 Godot/Codex 제품 구현은 이 work package에서 다루지 않는다.

### Current source canon

- `OMW-PLAN-20260825-FRONT-STATE-MINIMAP-SD-FANTASY-01`
- `OMW-PLAN-20260820-RUN-COMMAND-SHELL-01`
- `OMW-PLAN-20260820-ROULETTE-3X3-COMPONENT-01`
- `OMW-PLAN-20260820-LOWER-CONTROL-DECK-01`
- `OMW-PLAN-20260820-TEXT-UX-STATE-01`

이 문서는 과거 `OMENWARD_VISUAL_REQUIREMENT_INVENTORY_2026-08-20.md`의 Asset ID를 재사용한다. 과거 이미지/생성 이력은 삭제하지 않고 lineage로 보존한다.

## 2. 현재 3장 작업 순서

사용자가 승인한 현재 우선순위는 다음이다.

```text
1. OMW-VIS-003 · Main Battle / BATTLE Focus
2. OMW-VIS-001 · Run Command PREPARE / Roulette Manipulation
3. OMW-VIS-002 · COMMIT / Irreversible Front Assignment
```

이 순서는 **이미지 제작 순서만** 갱신한다. 기존 Asset ID의 의미 계보와 gameplay Decision은 변경하지 않는다.

## 3. 세트 구성 대안 검토

### A · Phase-separated 3-image set — APPROVED

각 장이 하나의 플레이어 질문을 명확히 소유한다.

- BATTLE: 지금 어느 전선이 위험하고 무엇이 벌어지고 있는가?
- PREPARE: 정지한 3×3 결과를 어떻게 조작할 것인가?
- COMMIT: 얻은 병력을 어느 전선에 비가역적으로 보낼 것인가?

장점:
- 한 장에 모든 UI를 몰아넣지 않아 현재 Focus가 명확하다.
- 실제 Run Command Screen의 지속 공간 맥락을 유지하면서 단계별 정보 우선순위를 검증할 수 있다.
- 세 장을 나란히 두면 `확률 설계 → 병력 획득 → 전선 배치 → 자동전투` 연결이 읽힌다.

### B · One panoramic full-flow image — REJECT

한 장에 PREPARE / COMMIT / BATTLE을 모두 넣으면 설명력은 높지만 실제 player-facing 화면처럼 보이지 않고 정보가 과밀해진다.

### C · Battle screen + detached component sheets — REJECT FOR FIRST PASS

병종/룰렛/UI 구성요소 검수에는 유리하지만 핵심 플레이 흐름과 감정 연결을 검증하기 어렵다. 3-Pack 승인 뒤 production component sheet 단계에서 사용한다.

---

# BRIEF 1 · OMW-VIS-003 · Main Battle / BATTLE Focus

## A. 검증 목적

대표 전투 화면 한 장만 보고 다음을 이해할 수 있어야 한다.

```text
- 상 / 중 / 하 세 전선이 동시에 진행된다.
- 세 전선의 현재 전투 상태가 서로 다르다.
- 각 전선 미니맵은 공간 맥락을 보조한다.
- 병종은 얼굴보다 역할 실루엣으로 읽힌다.
- 전투가 화면의 주 시각 질량이고 UI는 보조다.
- Omen Warden은 직접 싸우는 액션 영웅이 아니라 지휘관이다.
```

## B. 장면 상태

대표 BATTLE 순간은 세 전선을 의도적으로 서로 다른 상태로 만든다.

```text
TOP FRONT
= ALLY UNDER PRESSURE
= Veil armored / mass push
= 아군 방패/창 계열이 방어선 유지

MIDDLE FRONT
= ALLY ADVANTAGE / ACTIVE CLASH
= 아군 궁병/마법 병종이 전진 압박
= 현재 교전점이 적 방향으로 이동

BOTTOM FRONT
= SPECIAL THREAT
= Siege 또는 infiltration/air warning이 relevant
= 미니맵에서 route exception이 즉시 보임
```

세 전선이 모두 같은 전황이면 비교 판단을 검증할 수 없으므로 실패다.

## C. 화면 구성

### Battlefield

- 16:9 전략 화면.
- 화면 상단~중앙 대부분을 세 개의 **동시 Front-State View**가 차지한다.
- 세 전선은 수평 band로 명확히 나뉘지만 하나의 Ward Citadel 전쟁 공간처럼 시각 언어는 통일한다.
- 각 band는 `현재 아군 + 현재 위협 + 현재 교전점 + 전선 결과`가 보인다.
- 긴 수호성→적진 전체 도로를 한 번에 보여주는 과거 long-road 구성은 사용하지 않는다.

### Per-front minimap

각 Front-State 오른쪽 또는 명확한 동일 위치에 작은 contextual minimap 1개씩, 총 3개.

미니맵 내용:

```text
ALLY SIDE / ENEMY SIDE
CURRENT CLASH POSITION
STRONGHOLD / DEFENSE LINE
FRONT PROGRESS
RELEVANT ROUTE EXCEPTION
BOSS / SIEGE marker only when relevant
```

금지:
- 모든 병사 icon 복제
- 축소된 combat VFX
- 실제 전장의 작은 복사판

### Top HUD

상단 HUD는 짧고 한 줄 중심.

```text
Stage / Wave
Gold
Mana
Troop capacity
short Omen / threat summary
pause / speed / settings
```

### Lower Control Deck

BATTLE Focus이므로 Build / Roulette / COMMIT 조작을 펼치지 않는다.

허용:
- compact tactical quick access
- local mana cost
- cooldown / target-valid cue

전장이 확실히 가장 큰 시각 질량이어야 한다.

## D. Art direction

```text
VISUAL_STYLE = FANTASY_MAGIC_SD_TACTICAL_PIXEL_ILLUSTRATION
UNIT_RATIO = 2.5_TO_3_HEADS
ALLY = NAVY + IVORY + COOL_GRAY_METAL + RESTRAINED_GOLD
VEIL = BLACK_PURPLE + DARK_RED + CARAPACE_GRAY + LIMITED_RIFT_GLOW
```

- hard pixel edges / 명확한 도트 밀도.
- 병종은 방패, 창, 활, 지팡이, 날개, 대형 체급 같은 silhouette로 식별.
- 마법 VFX는 사건 순간에만 강하고 상시 bloom은 약하게.
- 전쟁 긴장감을 유지하고 모바일 치비의 과도한 귀여움은 피한다.

## E. 금지 요소

- 선택 전선 1개만 크게 확대하고 나머지 두 전선을 탭으로 숨김.
- 3개 미니맵 대신 하나의 전체 전략지도만 표시.
- 대형 Omen Warden 초상이 전투를 가림.
- 과도한 금장 모바일 왕국 UI.
- glassmorphism / glossy sci-fi HUD.
- 유닛보다 VFX가 더 크게 보이는 화면.

## F. 이미지 생성 프롬프트 초안

> 16:9 player-facing strategy autobattler game screen for OMENWARD. Show three simultaneous horizontal Front-State battle views, TOP MIDDLE BOTTOM, all visible at once. Each front has a small contextual minimap showing only progress, stronghold, current clash position and relevant route exceptions, never a duplicate miniature battlefield. Top front is under heavy Veil pressure, middle front is an allied advance, bottom front has a siege or infiltration exception. Fantasy magic SD tactical pixel illustration, 2.5–3 head miniature soldiers, crisp hard pixel edges, readable silhouettes, navy/ivory/cool-metal allied faction with restrained gold, black-purple/dark-red asymmetrical Veil creatures, restrained magical lighting. Battlefield dominates the screen; compact top HUD and a small battle-focused lower control deck. No casino imagery, no mobile kingdom gold clutter, no glassmorphism, no giant commander portrait, no long full-road composition, minimal readable UI labels only.

## G. 검수 체크리스트

- [ ] 1초 안에 전선이 정확히 3개임을 알 수 있다.
- [ ] 세 전선의 상태 차이를 색상 없이도 읽을 수 있다.
- [ ] 미니맵 3개가 각각 어떤 전선 소속인지 혼동되지 않는다.
- [ ] 미니맵이 두 번째 전장처럼 보이지 않는다.
- [ ] 방패/창/궁/마법/비행/거대 역할 실루엣이 최소한 일부 구분된다.
- [ ] Veil이 아군의 단순 색상 변경처럼 보이지 않는다.
- [ ] 전장 > HUD > Control Deck 시각 우선순위가 유지된다.
- [ ] Omen Warden이 직접 melee hero처럼 보이지 않는다.

---

# BRIEF 2 · OMW-VIS-001 · Run Command PREPARE / Roulette Manipulation

## A. 검증 목적

이 장면은 룰렛을 단순 랜덤 보상이나 카지노 UI가 아니라 **플레이어가 결과를 읽고 조작하는 전술 작업대**로 보여준다.

플레이어가 느껴야 하는 감정:

```text
내 준비가 확률을 만들었다
→ 결과가 정지했다
→ 거의 원하는 결과다
→ 내가 행/열을 조작할 수 있다
→ 결과를 확정하기 전에 판단한다
```

## B. 대표 상태

`PREPARE · Roulette STOPPED / MANIPULATE` 상태를 사용한다.

READY 상태보다 이 장면이 OMENWARD의 차별점인 **제한적 개입**을 더 잘 보여준다.

```text
natural stopped 3×3 board = visible
12 direct arrows = active
one row or column = hover/focus preview
center horizontal judging line = subtle persistent cue
move resource = local compact display
primary CTA = 결과 확정
Spin CTA = disabled / secondary state
```

## C. 화면 구성

### Persistent battlefield context

상단/중앙에는 현재 Visual Decision의 세 Front-State + 전선별 미니맵을 계속 보이게 한다.

- BATTLE 이미지보다 시각 디테일은 한 단계 낮춰도 된다.
- 전선 위치는 바뀌지 않는다.
- PREPARE로 들어왔다고 전장이 별도 전체화면으로 사라지지 않는다.

### Lower Control Deck · Roulette Focus

하단은 전체 높이의 약 28~32% exploration envelope.

```text
LEFT COMPACT
= Lucky Free Move / Stored Move Ticket

CENTER DOMINANT
= 3×3 actual-unit token board
= three column up arrows
= three column down arrows
= three row-left arrows
= three row-right arrows
= center judging-line cue

RIGHT ACTION
= local spin cost / compact result preview
= Result Confirm primary CTA
```

한 행 또는 열의 이동 preview를 ghost/snap 상태로 보여 이미지 한 장만으로도 “화살표를 누르면 이 줄이 이동한다”가 읽혀야 한다.

## D. Token visual language

- abstract weapon icon only가 아니라 실제 병종 SD art를 token 안에 사용.
- T1/T2/Tier 장식은 silhouette를 가리지 않는다.
- Gold token은 같은 tile grammar 안에서 큰 금화 silhouette.
- X는 명확한 non-reward state.
- 세 릴을 세 전선에 색으로 1:1 매핑하지 않는다.

## E. 금지 요소

- 1×N 슬롯머신 릴.
- cherries / 7 / jackpot / casino chip / lever / confetti.
- full-screen roulette modal로 전장을 완전히 숨김.
- Spin과 Result Confirm을 같은 버튼처럼 보이게 함.
- 12개 화살표의 대상/방향이 불명확함.
- 상단 Gold/Mana/Troop 수치를 하단에 다시 복제.
- 룰렛 규칙 텍스트가 전장보다 더 많은 면적을 차지.

## F. 이미지 생성 프롬프트 초안

> 16:9 OMENWARD Run Command PREPARE screen in Roulette STOPPED / MANIPULATE state. Keep the three battlefield Front-State views with one contextual minimap per front visible in the upper area so spatial context is never lost. The lower 28–32% is a compact tactical control deck. Center-dominant 3×3 board uses actual SD fantasy troop token art. Exactly twelve direct manipulation arrows: three column up, three column down, three row left, three row right. Show one row or column highlighted with a ghost movement preview, a subtle center-horizontal judging line, compact move resources on the left, compact result preview and one dominant Result Confirm action on the right. Fantasy magic SD tactical pixel illustration, crisp pixel edges, military omen sigils and ritual command-device language. No casino symbols, no slot-machine cabinet, no jackpot lights, no fake premium currency, no full-screen modal, minimal stable UI text.

## G. 검수 체크리스트

- [ ] 3×3이 화면의 현재 작업 중심으로 즉시 보인다.
- [ ] 화살표가 정확히 12개이고 각 대상/방향을 설명 없이 추정할 수 있다.
- [ ] preview와 실행 완료 상태가 시각적으로 다르다.
- [ ] 중앙 가로줄이 기준선으로 약하게 읽힌다.
- [ ] Spin과 Result Confirm의 역할 차이가 보인다.
- [ ] 전장 3개 + 미니맵 3개가 여전히 공간 맥락으로 남아 있다.
- [ ] 카지노/가챠 인상이 없다.
- [ ] 병종 token이 추상 아이콘보다 실제 병력 획득 감각을 준다.

---

# BRIEF 3 · OMW-VIS-002 · COMMIT / Irreversible Front Assignment

## A. 검증 목적

룰렛 결과를 얻는 것보다 **어느 전선에 보내는가**가 별도 전략 결정임을 한 장에서 보여준다.

플레이어 질문:

> 지금 얻은 병력을 어느 전선에 되돌릴 수 없게 투입할 것인가?

## B. 대표 상태

`COMMIT · PENDING assignment` 상태.

아직 실제 deployed truth가 아니다.

```text
newly acquired troop(s)
+ stored troop(s)
→ one or more pending front assignments
→ COMMIT 내부에서는 수정 가능
→ final primary CTA = 배치 확정 · 전투 시작
→ confirm 이후에만 irreversible deployment
```

## C. 화면 구성

### Three Front-State views remain spatial anchors

상·중·하 전선은 PREPARE/BATTLE과 동일한 화면 위치를 유지한다.

각 전선이 다른 판단 이유를 제공해야 한다.

예:

```text
TOP = 병력이 부족하지만 현재 방어는 유지
MIDDLE = 현재 우세, 추가 투입 시 돌파 가능
BOTTOM = Siege warning 때문에 즉시 보강 필요
```

미니맵은 각 전선의 progress / stronghold / route exception을 보조한다.

### Pending assignment visualization

하단 또는 전장 연결부에서 얻은 병력을 보여준다.

권장 시각:
- 새 획득 병력은 강조된 actual-unit card/token.
- 현재 선택 병력에서 대상 Front-State로 가는 얇은 command line / banner cue / ghost placement cue.
- PENDING 상태는 deployed 병사와 시각적으로 구분.
- assignment를 바꿀 수 있다는 점이 보이되 최종 확정 경계는 강하게 표시.

### Primary CTA

```text
배치 확정 · 전투 시작
```

옆에 상시 경고 의미를 짧게 보인다.

```text
확정 후 회수·판매·전선 이동 불가
```

긴 modal은 사용하지 않는다.

## D. 지휘관 역할 표현

세 장 중 Omen Warden의 존재감을 가장 자연스럽게 넣을 수 있는 화면이다.

허용:
- 화면 측면/하단의 command dais 또는 높은 지휘 위치.
- 긴 지휘 깃발 + command coat/armor.
- 병력을 전선으로 지시하는 silhouette.

금지:
- 전선 한가운데서 검을 들고 적을 직접 베는 모습.
- 병력보다 큰 영웅 portrait가 배치 판단 공간을 압도.

## E. 금지 요소

- Top/Middle/Bottom 추상 버튼 3개만 두고 실제 전장과 연결하지 않음.
- 획득 token과 전선이 자동 1:1로 매핑되어 보임.
- pending 선택 순간 병력이 이미 전투 중인 것처럼 표현.
- 병력 하나마다 대형 confirmation modal.
- 비가역 경고를 숨김.
- 모든 전선이 동일한 상태라 선택 이유가 없음.

## F. 이미지 생성 프롬프트 초안

> 16:9 OMENWARD COMMIT Focus player-facing strategy screen. Keep three simultaneous TOP MIDDLE BOTTOM Front-State battlefield views in fixed spatial positions, each with a small contextual minimap. Show different strategic needs: top is stable but thinly defended, middle is pushing forward, bottom has an urgent siege warning. In the compact lower control deck show newly acquired and stored actual SD troop tokens. One selected troop has a clear pending assignment cue toward a visible battlefield front, using a restrained command line/banner/ghost-placement visual. Pending assignment must look editable and not yet deployed. One dominant primary action reads conceptually “Confirm Deployment · Start Battle” with a short irreversible warning: after confirmation troops cannot be recalled, sold, or moved to another front. Include the Omen Warden as a small commanding silhouette with a long command flag, never as a melee hero. Fantasy magic SD tactical pixel illustration, crisp pixels, battlefield-primary composition, no casino imagery, no oversized modal, no abstract three-button-only lane selector.

## G. 검수 체크리스트

- [ ] 세 전선의 상황 차이가 실제 선택 이유로 보인다.
- [ ] 획득 병력과 보관 병력이 전선 공간과 연결된다.
- [ ] PENDING과 실제 deployed 상태를 혼동하지 않는다.
- [ ] 최종 확정이 비가역 경계임을 읽을 수 있다.
- [ ] 세 릴 / 세 token / 세 전선이 자동 1:1로 보이지 않는다.
- [ ] CTA가 하나의 주요 행동으로 보인다.
- [ ] Omen Warden이 지휘관으로 읽힌다.
- [ ] 하단 UI가 전장을 압도하지 않는다.

---

## 4. 3장 공통 제작 규칙

### 화면 일관성

세 장은 서로 다른 게임처럼 보이면 실패다.

공통 유지:

```text
same Front-State positions
same minimap grammar
same top HUD hierarchy
same lower deck shell
same faction palette / material language
same SD unit proportions
same pixel density family
```

Focus에 따라 **내용 우선순위만** 바뀐다.

### Text generation guardrail

생성 이미지 안의 문구는 최소화한다.

허용 예:
- TOP / MID / BOT 또는 짧은 전선명
- Stage / Wave
- PENDING
- Confirm / Battle 같은 매우 짧은 placeholder

최종 한국어 UI copy를 생성 이미지에서 정확히 재현하는 것을 승인 조건으로 삼지 않는다. 의미 구조와 위치 관계를 먼저 검수한다.

### Visual approval ceiling

```text
IMAGE_BRIEF = APPROVED
IMAGE_GENERATION = NOT_STARTED
GENERATED_CANDIDATE = NONE
USER_IMAGE_APPROVAL = NOT_RUN
RUNTIME_READABILITY = NOT_RUN
HUMAN_USABILITY = NOT_RUN
PLAYER_EXPERIENCE = NOT_RUN
```

이미지 생성은 이 브리프 승인만으로 자동 실행하지 않는다. 실제 생성은 사용자의 명시적 `1번 생성`, `OMW-VIS-003부터 그려줘` 같은 요청을 받은 뒤 **한 장씩** 수행한다.

## 5. 생성 후 승인 흐름

```text
ONE BRIEF
→ ONE generated candidate
→ source/brief checklist review
→ user APPROVE / REVISE / REJECT
→ approved candidate만 현재 Visual lineage에 등록
→ 다음 이미지로 이동
```

한 번에 여러 후보를 생성해 승인 기준을 흐리지 않는다.

## 6. 5회 적대적 브리프 검토

### Loop 1 · Canon / lineage
Finding: 과거 Inventory의 `NO_MINIMAP`, long-road 기본 구도와 현재 Visual Decision이 충돌한다.
Correction: 이 3-Pack은 2026-08-25 Decision을 우선하며 per-front minimap과 Front-State 구조를 모든 장에 강제한다.

### Loop 2 · Core loop identity
Finding: BATTLE만 먼저 만들면 일반 3-lane autobattler처럼 보일 위험이 있다.
Correction: 3-Pack에 PREPARE 3×3 manipulation과 COMMIT을 반드시 포함해 OMENWARD의 `확률 → 선택 → 배치 → 자동전투` 정체성을 보존한다.

### Loop 3 · Information density
Finding: 세 Front-State + 미니맵 3개 + lower deck가 작은 화면에서 과밀해질 수 있다.
Correction: 미니맵은 context-only, lower deck는 one active work surface, 생성 텍스트 최소화, 전장-primary를 공통 guardrail로 고정한다.

### Loop 4 · Player role / emotional read
Finding: SD 캐릭터와 지휘관이 캐릭터 수집 RPG처럼 보일 수 있다.
Correction: role silhouette 우선, Omen Warden은 command flag와 high-ground posture로 표현하고 melee hero fantasy를 금지한다.

### Loop 5 · Generation readiness
Finding: 프롬프트가 art style만 설명하고 실제 gameplay state 차이를 놓치면 예쁜 컨셉아트로 퇴행할 수 있다.
Correction: 각 브리프에 구체적인 phase state, 전선 상태 차이, UI action, 금지 요소, pass checklist를 포함한다.

```text
BRIEF_REVIEW = CLEAN_5_OF_5
BLOCKING_FINDINGS = 0
IMAGE_GENERATION = NOT_STARTED
```
