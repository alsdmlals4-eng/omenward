# OMENWARD · Lumern Shield Guard Runtime Asset Brief

```yaml
asset_brief_id: OMW-ASSET-BRIEF-20260826-LUMERN-SHIELD-GUARD-01
asset_family_id: ASSET-UNIT-LUMERN-SHIELD-GUARD
first_generation_target: ASSET-UNIT-LUMERN-SHIELD-GUARD-IDLE-V1
status: BRIEF_READY_IMAGE_NOT_STARTED
approved_production_policy: OMW-VIS-POLICY-20260826-RUNTIME-CONSUMER-ASSET-FIRST-01
current_visual_decision: OMW-PLAN-20260825-FRONT-STATE-MINIMAP-SD-FANTASY-01
primary_consumer: Battlefield UnitView / future sprite renderer
secondary_consumers:
  - Roulette unit-token Role-Anchor crop
  - Result / Storage unit presentation
  - COMMIT unit presentation
product_code_mutation: NONE
godot_execution: NOT_IN_SCOPE
codex_execution: NOT_IN_SCOPE
image_generation: NOT_STARTED
runtime_import_validation: NOT_RUN
human_asset_approval: NOT_RUN
final_frame_count: NOT_LOCKED
final_fps: NOT_LOCKED
skill_1_choreography: NOT_LOCKED
```

## 1. 목적

이 문서는 설명용 캐릭터 시트가 아니라 **실제 게임이 소비할 Lumern Shield Guard 이미지 자산**의 첫 제작 브리프다.

첫 생성물부터 실제 소비 가능성을 가져야 한다.

```text
FIRST OUTPUT
= one clean runtime-oriented IDLE sprite candidate
= transparent background
= battlefield unit source
= later token/storage/commit crop source
```

최종 자산 패밀리는 현재 `AnimationContract`의 상태를 따라 확장하지만, 첫 이미지 승인 전에 8개 상태를 한꺼번에 생성하지 않는다.

## 2. 근거 정본

### 현재 unit data

`data/units/shield_guard.tres` 기준:

```text
archetype_id = shield_guard
role = frontline
max_health = 180
armor = 24
magic_resistance = 16
move_speed = 1.0
attack_range = 1.0
counter_tags = ranged_defense
target_priority_tags = nearest
```

아트가 숫자를 직접 표현할 필요는 없지만 다음 시각 의미를 보호한다.

- 전열에서 버틴다.
- 원거리 압박을 받아내는 역할이 먼저 읽힌다.
- 빠른 공격수나 영웅이 아니라 **방어면을 제공하는 일반 전투 병종**이다.

### 현재 Visual Decision

```text
VISUAL_STYLE = FANTASY_MAGIC_SD_TACTICAL_PIXEL_ILLUSTRATION
UNIT_PROPORTION = 2.5_TO_3_HEAD_SD_TACTICAL_MINIATURE
PRIMARY_READ = ROLE_SILHOUETTE
ALLY = NAVY + IVORY + COOL_GRAY_METAL + RESTRAINED_GOLD
ALLY_SHAPES = ARCH + SHIELD + BANNER + RELIC + VERTICAL_LINES
```

### retained unit-production rules

기존 unit production guide에서 현재 Visual Decision과 충돌하지 않는 다음 규칙을 유지한다.

- 일반 인간형 전략 줌 표시 높이 `34~40px`는 **첫 제작 탐색 envelope**로 사용한다.
- core palette는 약 `6~10색`, 피부/금속/천 등을 포함한 전체 첫 제작 상한은 약 `18~24색`을 탐색 기준으로 둔다.
- 내부 픽셀 스케일에서 기본 1px 외곽선.
- 본체 2~4단 명암 + 제한된 material highlight.
- 자동 안티앨리어싱 금지.
- 최종 확대는 nearest-neighbor.

단, `34~40px`는 현재 Front-State 화면에서 아직 runtime 검증되지 않았으므로 **최종 런타임 크기 LOCK이 아니다.**

## 3. 실제 소비처

### Primary · Battlefield

현재 `UnitView`는 원/선/색으로 unit을 procedural graybox 렌더링한다. 이 자산 패밀리는 향후 실제 unit sprite renderer가 그 자리를 대체할 때 사용한다.

```text
Battlefield Unit
→ ASSET-UNIT-LUMERN-SHIELD-GUARD
```

### Secondary · Roulette / Result / Storage / COMMIT

현재 Token 계약은 별도 token-only 캐릭터 아트를 금지한다.

```text
Battlefield unit art
→ Role-Anchor crop
→ Roulette token
→ larger Result preview
→ Storage
→ COMMIT
```

따라서 이 unit source가 승인되면 방패 + 투구/상체가 남는 crop을 파생한다.

## 4. 제작 순서 대안

### A · Runtime idle first → state expansion — ADOPT

1. 실제 `idle` sprite candidate 1개 제작.
2. 작은 전략 줌과 token crop에서 검수.
3. 사용자 승인으로 base design lock.
4. 같은 디자인을 `deploy / move / attack_basic / skill_1 / hit_light / death / victory`로 확장.
5. Veil Shield Guard가 동일 frame/pivot/state 구조를 사용하도록 pair 제작.

장점:
- 첫 이미지부터 실제 game consumer가 있다.
- 생성형 이미지에서 흔한 캐릭터 drift를 가장 작은 범위에서 잡는다.
- 잘못된 디자인으로 전체 animation atlas를 생산하는 낭비를 막는다.

### B · 8-state full atlas one pass — REJECT FOR FIRST PASS

장점:
- 표면상 빠르게 한 병종이 완성된다.

거부 이유:
- 한 번에 많은 pose를 만들수록 얼굴/갑주/방패 형태 consistency가 무너질 위험이 높다.
- `skill_1` 정확 동작과 final frame count/FPS가 아직 정본으로 잠기지 않았다.
- 실패 시 전체 atlas를 버려야 한다.

### C · Turnaround / concept sheet first — REJECT AS PRODUCTION OUTPUT

장점:
- 디자인 설명은 쉽다.

거부 이유:
- 게임이 직접 소비하지 않는 설명용 sheet다.
- 현재 `NO_RUNTIME_CONSUMER = NO_IMAGE_PRODUCTION_TASK` 정책과 충돌한다.

필요한 디자인 판단은 문서에서 하고, 생성물은 runtime sprite부터 만든다.

## 5. 카메라 / 방향 대안

### A · 3/4 tactical top-down + canonical right-facing source — ADOPT

```text
VIEW = 3/4 tactical top-down
SOURCE_FACING = RIGHT
GROUND_CONTACT = VISIBLE
SHIELD_FACE = PARTIALLY_VISIBLE
```

- 세 전선의 좌우 진행 축에 잘 맞는다.
- 방패 면적과 SD 체형을 동시에 읽을 수 있다.
- 향후 Lumern/Veil pair에 동일 source direction과 frame arrangement를 적용하기 쉽다.

### B · Pure side-view — REJECT

실루엣은 단순하지만 OMENWARD의 tactical top-down world와 공간감이 약해진다.

### C · Four-direction / eight-direction set — DEFER

맵 이동 게임이라면 유용하지만 현재 세 전선 좌우 전투 소비처에 비해 제작량이 과도하다. 실제 runtime에서 방향 요구가 증명되기 전에는 만들지 않는다.

## 6. 실루엣 LOCK 후보

읽기 순서는 다음이다.

```text
1. OVERSIZED SHIELD FRONT SHAPE
2. LOW CENTER OF GRAVITY / DEFENSIVE POSTURE
3. SHORT ONE-HANDED WEAPON
4. HELMET + PRACTICAL PLATE/CLOTH BODY
5. LUMERN FACTION MATERIAL / COLOR
6. SMALL RELIC / RANK DETAIL
```

### Shield

- **몸 높이에 가까운 큰 전방 방어면**이 1순위 role anchor.
- 상단은 Lumern의 arch language가 느껴지는 완만한 곡선/아치 계열.
- 지나치게 넓은 원형 방패보다 세로 방향이 읽히는 방패를 우선한다.
- 방패 장식은 작은 Ward/omen 기하 문양 정도로 제한한다.
- 문양이 방패 실루엣보다 먼저 보이면 실패다.

탐색 비율:

```text
shield visible height ≈ 70~85% of character total visible height
shield mass = dominant front-side visual mass
```

정확 비율은 첫 candidate에서 검수 후 조정한다.

### Body / stance

- 약 `2.5~3등신`.
- 발을 넓게 벌리지 않고 짧고 안정적인 보폭.
- 상체는 방패 뒤에서 약간 앞으로 숙여진 낮은 중심.
- 영웅식 contrapposto, 긴 망토, 과도한 장식 자세 금지.
- 얼굴보다 방패와 몸의 무게중심이 먼저 읽혀야 한다.

### Helmet / armor

- practical cool-gray plate + navy cloth + ivory underlayer.
- 투구는 얼굴을 완전히 주인공처럼 드러내지 않는다.
- 작은 cloth tab / short coat는 허용하지만 긴 영웅 망토는 사용하지 않는다.
- armor silhouette는 비교적 대칭적이고 disciplined.

## 7. 한손 무기 선택 대안

현재 source는 Shield Guard의 basic attack을 **방패 옆 짧은 찌르기/베기**로 설명하지만 정확 weapon name은 현행 unit data에 잠겨 있지 않다.

### A · Short straight sword — FIRST IMAGE CANDIDATE

장점:
- 짧은 찌르기와 베기 둘 다 자연스럽다.
- Spear Guard와 silhouette를 침범하지 않는다.
- 큰 방패 뒤에 부분적으로 숨겨도 weapon read가 가능하다.

### B · Short spear — REJECT FOR FIRST CANDIDATE

방패병 archetype에는 자연스럽지만 Spear Guard의 가장 중요한 long-weapon silhouette와 혼동될 위험이 있다.

### C · Mace — REJECT FOR FIRST CANDIDATE

방어병 무게감은 좋지만 현재 animation language의 `찌르기/베기`와 맞지 않는다.

따라서 첫 이미지 후보는 **짧고 곧은 한손검**을 사용한다.

```text
SHORT_SWORD = PRODUCTION_CANDIDATE
SHORT_SWORD_CANON_LOCK = ONLY_AFTER_USER_IMAGE_APPROVAL
```

## 8. Lumern palette / material

우선순위:

```text
COOL_GRAY_METAL
→ NAVY CLOTH
→ IVORY CLOTH / SHIELD FIELD
→ DARK NEUTRAL OUTLINE
→ RESTRAINED GOLD ACCENT
```

가이드:
- 금색은 shield rim 전체를 화려하게 덮기보다 작은 ward fitting / buckle / relic point에 제한.
- 실용 판금의 면 분할을 2~4 tone으로 단순화.
- 금속 highlight는 한 방향 광원으로 제한.
- 파란색만 칠한 일반 기사처럼 보이지 않도록 arch/shield/vertical construction language를 함께 사용.

## 9. 첫 runtime idle 자산의 기술 envelope

### Output semantics

```text
TARGET = isolated single unit sprite
BACKGROUND = transparent
BAKED_TEXT = NONE
BAKED_UI_FRAME = NONE
BAKED_GROUND_SHADOW = NONE
SOURCE_FACING = RIGHT
POSE = combat-ready idle
```

바닥 그림자는 향후 world shadow/shared effect가 소유한다. terrain에 종속되는 shadow를 unit texture에 bake하지 않는다.

### Display-scale exploration

```text
INTERNAL_REFERENCE = 960x540
NORMAL_HUMANOID_DISPLAY_HEIGHT_START = 34~40px
TOKEN_TILE_REFERENCE = 32~34px
TOKEN_SAFE_ART_REFERENCE = 26~29px
```

첫 candidate는 다음 두 소비 상황을 모두 고려한다.

1. Battlefield에서는 34~40px 전후의 작은 크기에서도 shield role이 읽혀야 한다.
2. Token crop에서는 상체 + 방패가 26~29px safe art에 들어가도 Shield Guard임을 알아볼 수 있어야 한다.

### AI generation boundary

생성형 원본은 곧바로 `RUNTIME_READY`가 아니다.

```text
AI_GENERATED_CANDIDATE
→ silhouette / design review
→ pixel-grid cleanup
→ transparent PNG cleanup
→ palette / edge cleanup
→ nearest-neighbor size validation
→ USER APPROVAL
→ RUNTIME_ASSET_CANDIDATE
```

혼합 픽셀 크기, soft anti-aliasing, semi-transparent fuzzy edge가 남으면 runtime candidate로 승격하지 않는다.

## 10. 현재 AnimationContract 확장 계획

현재 code/data가 직접 요구하는 상태명:

```text
deploy
idle
move
attack_basic
skill_1
hit_light
death
victory
```

첫 제작은 `idle`만 한다.

### 상태별 identity

| State | Shield Guard motion identity | 현재 제작 상태 |
|---|---|---|
| `idle` | 낮은 중심, shield front 고정, 호흡/미세 체중 이동 | **FIRST** |
| `move` | 짧은 보폭, 방패 방향 안정, 몸이 shield를 따라 전진 | AFTER_IDLE_APPROVAL |
| `attack_basic` | shield 옆에서 짧은 one-hand stab/slash | AFTER_IDLE_APPROVAL |
| `skill_1` | exact gameplay choreography 미확정 | BLOCKED_UNTIL_SKILL_FRESH_READ |
| `hit_light` | 매우 짧은 반동; 과장 경직 금지 | AFTER_IDLE_APPROVAL |
| `death` | 공격/충돌 제거가 읽히는 낮은 붕괴 | AFTER_IDLE_APPROVAL |
| `deploy` | 전선 배치/증원 도착을 읽히게 하는 짧은 진입 | AFTER_IDLE_APPROVAL |
| `victory` | shield를 세우고 weapon으로 한 번 두드리는 계보 | AFTER_IDLE_APPROVAL |

과거 animation guide의 일반 인간형 frame budget은 참고값이다.

```text
idle 4~6
move 6~8
attack_basic 6~10
skill_1 8~14
hit_light 2~3
death 6~10
deploy 6~10
victory 8~14
```

정확 frame count/FPS는 PoC/runtime 검증 전 `NOT_LOCKED`다.

현재 code `AnimationContract`에 없는 `hit_heavy / controlled / capture / defeat` 등 과거 조건부 상태는 이번 생산 범위에 자동 추가하지 않는다.

## 11. Veil pair compatibility

다음 자산 `ASSET-UNIT-VEIL-SHIELD-GUARD`는 단순 recolor가 아니지만 같은 gameplay archetype이다.

따라서 Lumern source부터 다음을 pair-safe하게 만든다.

```text
same state order
same future frame counts per state
same canvas envelope
same ground-contact pivot logic
same attack direction
same impact-event timing contract
same mirror convention
```

Veil에서는 shield 기능을 갑각판/방어기관으로 번역할 수 있지만 gameplay timing을 바꾸지 않는다.

## 12. 금지 요소

- mobile kingdom hero처럼 과도한 금장/왕관/보석.
- 긴 cape / halo / giant shoulder armor가 shield role보다 먼저 읽힘.
- 방패가 작은 buckler 수준으로 축소됨.
- 얼굴/머리카락이 Shield Guard의 1순위 identifier가 됨.
- pure blue recolor만으로 Lumern identity를 만듦.
- painterly blur / soft brush / smooth anime rendering.
- inconsistent pixel density.
- baked floor/background/scenery.
- token frame나 UI 장식을 unit sprite에 포함.
- text/name/number를 sprite에 bake.
- 한 장에 여러 pose를 넣어 설명용 sheet로 만드는 것.

## 13. 첫 이미지 생성 프롬프트 초안

아래는 실제 생성 시 사용할 source prompt의 의미 계약이다. 이미지 생성은 아직 실행하지 않는다.

> Single isolated runtime game unit sprite candidate for OMENWARD: Lumern Shield Guard, fantasy magic SD tactical pixel illustration, 2.5 to 3 heads tall, three-quarter tactical top-down view, canonical right-facing combat-ready idle pose. The primary silhouette is an oversized body-height arched shield held forward, low stable center of gravity, practical cool-gray plate armor, navy cloth, ivory underlayer, very restrained gold ward fittings, compact helmet and short coat, short straight one-handed sword partially visible beside the shield. Crisp hard pixel edges, handcrafted pixel clusters, restrained material lighting from upper left, shield and posture readable before face or decoration. Transparent background only, one character only, no ground shadow, no text, no UI frame, no scenery, no cape, no crown, no heroic aura, no casino motifs, no smooth anti-aliased painterly shading.

## 14. 첫 candidate 검수 체크리스트

### Runtime consumer
- [ ] 한 명의 isolated unit만 존재한다.
- [ ] 투명 배경이다.
- [ ] UI/문구/설명 요소가 없다.
- [ ] Battlefield unit source로 crop 가능한 형태다.

### Role readability
- [ ] 색을 빼도 Shield Guard로 읽힌다.
- [ ] 1순위 mass가 큰 방패다.
- [ ] 낮고 안정적인 frontline stance다.
- [ ] short sword가 Spear/Greatsword role을 침범하지 않는다.

### Faction readability
- [ ] Navy/Ivory/Cool Gray/Gold가 restrained hierarchy로 사용된다.
- [ ] vertical/arch/shield/relic 형태가 최소 하나 이상 읽힌다.
- [ ] 일반 등급인데 영웅처럼 과장되지 않는다.

### Pixel quality
- [ ] hard pixel edge가 보인다.
- [ ] 동일 자산 안에서 pixel density가 일관된다.
- [ ] soft AI airbrush / blur가 없다.
- [ ] material shading이 silhouette를 덮지 않는다.

### Small-scale
- [ ] 약 34~40px 표시 크기 탐색에서 shield role이 남는다.
- [ ] 32~34px token tile용 상체 crop이 가능하다.
- [ ] shield + helmet/upper body가 26~29px safe art에서 구분 가능하다.

### Pair compatibility
- [ ] 향후 Veil Shield Guard와 같은 canvas/pivot/state layout을 쓰는 데 무리가 없다.
- [ ] right-facing source orientation이 명확하다.
- [ ] weapon/shield가 frame edge에 과도하게 붙지 않는다.

## 15. 5회 전체 적대적 검토

### Loop 1 · 실제 소비처
- 질문: 이 이미지는 설명 자료인가 실제 게임 자산인가?
- 검토: Battlefield unit source + Token/Storage/COMMIT 파생 소비처가 존재한다.
- Finding: turnaround sheet를 별도 생성하면 정책 위반.
- 수정: 첫 생성물을 `idle runtime sprite`로 제한.
- 결과: PASS.

### Loop 2 · 역할 오독
- 질문: 작은 화면에서 일반 기사/검사로 보일 수 있는가?
- Finding: 검과 갑주 디테일이 커지면 shield role이 약해질 수 있다.
- 수정: oversized body-height shield를 1순위 mass로 고정, short sword는 secondary.
- 결과: PASS.

### Loop 3 · 진영 오독
- 질문: 단순 파란색 기사로 보일 수 있는가?
- Finding: palette만으로 Lumern을 정의하면 faction contract 위반.
- 수정: arch/vertical/shield/relic construction language를 palette와 함께 요구.
- 결과: PASS.

### Loop 4 · animation lock 과잉
- 질문: 아직 정본이 없는 `skill_1`과 frame/FPS를 임의로 만들고 있는가?
- Finding: 과거 guide에는 frame budget이 있지만 exact 수치는 PoC 대상이다.
- 수정: 상태명만 현재 contract로 보호하고 exact frame/FPS/skill choreography는 `NOT_LOCKED`.
- 결과: PASS.

### Loop 5 · 생성형 결과의 runtime 오인
- 질문: image generator output을 곧바로 게임 파일로 승인할 위험이 있는가?
- Finding: soft edge/mixed pixel density가 남을 수 있다.
- 수정: `AI_GENERATED_CANDIDATE != RUNTIME_READY`; pixel cleanup + transparent export + user approval을 별도 Gate로 고정.
- 결과: PASS.

```text
ADVERSARIAL_REVIEW = CLEAN_5_OF_5
BLOCKING_FINDINGS = 0
```

## 16. 현재 상태 / 다음 행동

```text
BRIEF = READY
IMAGE_GENERATION = GENERATED_AND_USER_APPROVED
FIRST_TARGET = ASSET-UNIT-LUMERN-SHIELD-GUARD-IDLE-V1
FIRST_TARGET_USER_APPROVAL = APPROVED
PIXEL_CLEANUP = NOT_RUN
RUNTIME_IMPORT = NOT_RUN
GODOT_CODEX = OUT_OF_CURRENT_SCOPE
APPROVAL_RECORD = docs/images/approved/OMENWARD_ASSET_UNIT_LUMERN_SHIELD_GUARD_IDLE_V1_APPROVAL_2026-08-26.md
NEXT_AFTER_APPROVAL = UNIT_ANIMATION_PRODUCTION_CONTRACT
```

사용자가 실제 이미지 생성을 명시하면 **Lumern Shield Guard idle 1개만** 생성한다. 승인 전에는 Veil pair나 다른 상태로 진행하지 않는다.
