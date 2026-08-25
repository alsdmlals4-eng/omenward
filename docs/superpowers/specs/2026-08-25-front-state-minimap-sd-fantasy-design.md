# OMENWARD · Front-State Battlefield + Per-Front Minimap + Fantasy Magic SD Visual Design

```yaml
decision_id: OMW-PLAN-20260825-FRONT-STATE-MINIMAP-SD-FANTASY-01
status: USER_APPROVED_CURRENT
approved_at: 2026-08-25
planning_contract: PROJECT_TOTAL_PLANNING_IMPLEMENTATION_AND_DELIVERY_INSTRUCTION_v4.8
scope: BATTLEFIELD_PRESENTATION_VISUAL_STYLE_PLAYER_COMMANDER_IDENTITY
runtime_mutation: NONE
scene_mutation: NONE
product_data_mutation: NONE
image_generation: STOPPED_FOR_THIS_DECISION
human_runtime_validation: NOT_RUN
```

## 1. 결정 요약

OMENWARD의 기본 전장 표현은 더 이상 **수호성에서 적 진영까지 이어지는 긴 3개 길 전체**가 아니다. 상·중·하 **세 전선의 현재 교전 상황을 동시에 보여주는 3개 Front-State View**를 사용하고, 각 전선에 작은 미니맵을 붙여 공간 문맥을 보충한다.

```text
BATTLEFIELD_PRESENTATION = THREE_SIMULTANEOUS_FRONT_STATE_VIEWS
PER_FRONT_MINIMAP = REQUIRED
MINIMAP_IS_CONTEXT_NOT_SECOND_BATTLEFIELD = TRUE
UNIT_BY_UNIT_MINIMAP_REPLICATION = FORBIDDEN
LONG_FULL_ROAD_PRESENTATION = SUPERSEDED_AS_DEFAULT
```

그림체는 최신 `ANIME_PIXEL_ART + CLEAN_PIXEL_ART` 단순 조합을 폐기하고 기존 승인 계보의 판타지·마법·SD 방향을 하나로 통합한다.

```text
VISUAL_STYLE = FANTASY_MAGIC_SD_TACTICAL_PIXEL_ILLUSTRATION
UNIT_PROPORTION = 2.5_TO_3_HEAD_SD_TACTICAL_MINIATURE
MATERIAL_FINISH = HIGH_RES_PIXEL_TEXTURE_AND_RESTRAINED_LIGHTING
WORLD_TONE = FANTASY_WARD_CITADEL + MAGIC_WARFARE
```

플레이어 Omen Warden의 대표 실루엣은 **지휘관 외투/갑주 + 긴 지휘 깃발**이다. 직접 전투 영웅이 아니라 전조를 읽고 병력을 보내는 지휘자라는 역할이 먼저 읽혀야 한다.

## 2. 대체 관계

이 Decision은 다음 과거 표현을 부분 대체한다.

```text
SUPERSEDED:
- DEFAULT_CAMERA = FULL_THREE_LANE_VIEW 를 "긴 3개 전선 도로 전체 표시"로 해석하는 방식
- WIDE_COMBAT_ROADS 를 화면의 주 시각 문법으로 사용하는 방식
- NO_MINIMAP / 미니맵 기본 비요구
- CHARACTER_AND_UNIT_STYLE = ANIME_PIXEL_ART 단독 정의
- BATTLEFIELD_AND_BACKGROUND_STYLE = CLEAN_PIXEL_ART 단독 정의

RETAINED:
- 세 전선은 동시에 읽혀야 한다.
- 전장이 화면의 주 시각 질량이다.
- 하단 Control Deck은 보조다.
- 아군과 Veil의 진영 대비를 유지한다.
- 병종은 얼굴보다 역할 실루엣으로 먼저 읽힌다.
- 3×3 징조륜 / Focus-adaptive Control Deck / PREPARE→COMMIT→BATTLE→REVIEW는 유지한다.
- North Star v2.1의 진영 대비와 전장 우선 계층은 참고 가치가 있다.
```

## 3. 선택한 전장 구조

### A · 세 전선 상황창 + 각 전선 미니맵 — APPROVED

```text
┌────────────────────────────────────────────┐
│ 상단 전선 · CURRENT CLASH          [MINIMAP] │
│ 현재 병력 / 위협 / 교전 상태                  │
├────────────────────────────────────────────┤
│ 중앙 전선 · CURRENT CLASH          [MINIMAP] │
│ 현재 병력 / 위협 / 교전 상태                  │
├────────────────────────────────────────────┤
│ 하단 전선 · CURRENT CLASH          [MINIMAP] │
│ 현재 병력 / 위협 / 교전 상태                  │
└────────────────────────────────────────────┘
┌────────────────────────────────────────────┐
│ 현재 Focus의 compact Control Deck            │
└────────────────────────────────────────────┘
```

핵심은 **길의 길이**가 아니라 **현재 전선 상태**다. 플레이어가 한눈에 비교해야 하는 정보는 세 전선의 전투 압력, 병종 조합, 거점 위험, 위협 Signature, 전선 밀림/전진 상태다.

### 전선별 미니맵

각 전선 미니맵은 상세 전투를 복제하지 않는다. 다음만 보여준다.

```text
- 아군 방향 / 적 방향
- 현재 교전 위치
- 주요 거점 또는 방어선
- 우회 / 침투 / 공중 Route 징후
- Boss / Siege / 핵심 위협 위치가 relevant할 때
- 전선 우세·균형·열세의 공간적 맥락
```

미니맵에서 개별 병사를 모두 표시하거나 전체 전투 VFX를 축소 복제하지 않는다.

## 4. 비교한 대안

### B · 선택 전선 1개 확대 + 나머지 2개 미니맵/탭 — REJECT

장점:
- 선택 전선의 전술 디테일이 강하다.
- 큰 VFX와 병종 애니메이션을 보여주기 쉽다.

단점:
- 세 전선 동시 판단이 약해진다.
- 오토배틀러의 병렬 전선 운영 감각이 줄어든다.

세 전선 동시 비교가 제품 정체성에 더 중요하므로 채택하지 않는다.

### C · 전체 전략 지도 + 선택 전선 팝업 — REJECT

장점:
- 영지/전략 게임 느낌이 강하다.
- 전체 작전 상황은 쉽게 전달한다.

단점:
- 전투 관전성과 병종 조합 판독이 약해진다.
- 전투가 지도 아이콘 사건처럼 축소될 위험이 있다.

OMENWARD는 영지 지도 자체보다 **병력을 보내고 자동전투 결과를 읽는 경험**이 핵심이므로 채택하지 않는다.

## 5. 그림체 정본

### 캐릭터 / 병종

```text
UNIT_STYLE = SD_TACTICAL_PIXEL_ILLUSTRATION
BODY_RATIO = 2.5_TO_3_HEADS
PRIMARY_READ = ROLE_SILHOUETTE
SECONDARY_READ = FACTION + TIER + MAGIC_CUE
```

- 귀여움만을 목적으로 한 모바일 치비는 피한다.
- 작은 체형에서도 방패·창·활·지팡이·날개·갑주·체급이 크게 읽힌다.
- 상위 Tier는 체형을 무작정 키우기보다 장비, 자세, 실루엣 부속, 짧은 VFX로 위계를 올린다.
- 픽셀 그리드와 외곽선을 유지하면서 재질과 제한된 조명으로 판타지 고급감을 만든다.

### 아군 수호성 / Omen Warden 진영

```text
PALETTE = NAVY + IVORY + COOL_GRAY_METAL + RESTRAINED_GOLD
SHAPE_LANGUAGE = ARCH + SHIELD + BANNER + RELIC + VERTICAL_LINES
MAGIC_LANGUAGE = OMEN_SIGIL + SANCTIFIED_LIGHT + ARCANE_GEOMETRY
```

세계는 단순 중세 군대가 아니라 **마법 문명을 가진 수호성 전쟁 판타지**로 보인다. 지휘소, 마력탑, 징조륜, 성물, 전조 표식에 마법이 분명하게 존재한다.

### Veil 측

```text
PALETTE = BLACK_PURPLE + DARK_RED + CARAPACE_GRAY + LIMITED_RIFT_GLOW
SHAPE_LANGUAGE = ASYMMETRIC_RIFT + CARAPACE + SPIKE + VOID_APERTURE
```

Veil은 단일 종족처럼 획일화하지 않되 아군과 다른 형태 문법으로 즉시 구분한다.

### 마법 연출

- 마법은 세계의 상시 존재감으로 사용한다.
- 전투 가독성을 가리는 상시 bloom/섬광은 금지한다.
- Omen, Mana, Signature, Hero/Legendary/Boss 사건에서만 강도를 올린다.

## 6. 지휘관 시각 정체성

```text
COMMANDER_SILHOUETTE = LONG_COMMAND_FLAG + COMMAND_COAT/ARMOR + HIGH_GROUND_POSTURE
PLAYER_FANTASY = READ_OMEN -> PREPARE_DOMAIN -> SEND_TROOPS -> COMMIT_FRONTS -> OBSERVE_AUTOBATTLE
DIRECT_HERO_MELEE_FANTASY = FORBIDDEN_AS_PRIMARY
```

- 긴 지휘 깃발은 단순 장식이 아니라 플레이어 역할을 즉시 설명하는 Role Anchor다.
- 지휘관은 전선 상황창을 가리는 대형 상시 초상/캐릭터가 아니다.
- PREPARE/COMMIT 또는 수호성 지휘 공간에서 존재감을 주고 BATTLE에서는 전선 읽기를 우선한다.

## 7. 기존 North Star v2.1 처리

```text
NORTH_STAR_V2_1_OVERALL = REFERENCE_ONLY_AFTER_2026_08_25
RETAIN = BATTLEFIELD_PRIMARY_HIERARCHY
RETAIN = ALLY_VS_VEIL_FACTION_CONTRAST
RETAIN = COMPACT_LOWER_CONTROL_DECK_DIRECTION
SUPERSEDE = LONG_ROAD_FULL_THREE_LANE_COMPOSITION
SUPERSEDE = NO_MINIMAP
SUPERSEDE = ANIME_PIXEL_ONLY_CHARACTER_DIRECTION
```

기존 시안은 전장 우선 계층과 진영 대비 참고로 남긴다. 새 전장 레이아웃이나 최종 그림체의 정본으로 사용하지 않는다.

## 8. UX / 정보 계약

세 전선 각각이 한 화면에서 최소 다음 질문에 답해야 한다.

```text
1. 지금 어느 전선이 가장 위험한가?
2. 어떤 병종/위협이 현재 충돌하고 있는가?
3. 전선이 어디까지 밀렸거나 전진했는가?
4. 우회/침투/공성/Boss 같은 공간적 예외가 있는가?
5. 내가 COMMIT한 병력이 어떤 결과를 만들고 있는가?
```

전선 상황창은 1·2·5를 담당하고, 전선별 미니맵은 3·4를 담당한다.

## 9. 해상도 / 가독성 검증 계약

실제 구현 전 다음을 검증해야 한다.

```text
960x540   = 세 전선 상황 + 미니맵 3개 + 현재 Focus CTA 식별 가능
1280x720  = 병종 역할과 전선 위험 비교 가능
1920x1080 = 재질/마법 디테일이 정보 계층을 침범하지 않음
```

검증 전 상태:

```text
GODOT_RUNTIME = NOT_RUN
UI_RUNTIME = NOT_RUN
HUMAN_USABILITY = NOT_RUN
PLAYER_EXPERIENCE = NOT_RUN
MINIMAP_READABILITY = NOT_RUN
SD_UNIT_RUNTIME_READABILITY = NOT_RUN
```

## 10. 위험과 완화

| 위험 | 영향 | 완화 |
|---|---|---|
| 전선 3개 + 미니맵 3개로 정보 과밀 | 작은 해상도에서 혼잡 | 미니맵은 route/progress/context만 표시하고 유닛 복제 금지 |
| 전선 전체 길이를 숨겨 공간감 상실 | 전황 변화가 단절되어 보임 | 미니맵이 front progress/stronghold/route를 책임 |
| SD가 너무 귀여워 전쟁 긴장 약화 | 세계 톤 붕괴 | 장비/자세/재질/Veil 형태를 전술적으로 유지 |
| 판타지 마법 VFX가 병종을 가림 | 오토배틀 가독성 저하 | 상시 저강도, 사건 순간만 고강도 |
| 지휘관이 영웅 액션 주인공처럼 보임 | 플레이어 역할 왜곡 | 깃발/지휘 위치 중심, 직접 전투 비중 최소화 |

## 11. 5회 전체 적대적 검토

### Loop 1
- 전체 범위 재검토: 세 전선 동시성, 오토배틀러 정체성, Run Command 흐름, UI 밀도, 장기 구현 비용.
- Finding: `전선 상황만`이 선택 전선 1개만 보인다는 의미로 오해될 수 있음.
- 수정: **상·중·하 세 Front-State View 동시 표시**를 명시적 불변식으로 고정.
- 대안 재검색: B/C보다 A가 세 전선 판단을 가장 잘 보존.
- 장기 적합성: PASS.

### Loop 2
- 전체 범위 재검토.
- Finding: 미니맵이 작은 두 번째 전장처럼 복제될 위험.
- 수정: `MINIMAP_IS_CONTEXT_NOT_SECOND_BATTLEFIELD`, 개별 병사/VFX 복제 금지.
- 대안 재검색: 단일 전체 미니맵보다 per-front가 전선 비교와 직접 연결됨.
- 장기 적합성: PASS.

### Loop 3
- 전체 범위 재검토.
- Finding: 최신 `Anime Pixel + Clean Pixel` 문구와 기존 `SD + fantasy + magic` 승인 계보가 충돌.
- 수정: 통합 정본 `FANTASY_MAGIC_SD_TACTICAL_PIXEL_ILLUSTRATION`을 정의하고 과거 두 단독 스타일 표현을 부분 대체.
- 대안 재검색: 완전 풀 일러스트/비픽셀 전환은 전투 가독성과 기존 자산 계보를 훼손하므로 기각.
- 장기 적합성: PASS.

### Loop 4
- 전체 범위 재검토.
- Finding: 큰 깃발 지휘관이 전장을 가리거나 액션 영웅처럼 보일 위험.
- 수정: Commander는 Role Anchor로 유지하되 BATTLE 전선 패널을 침범하지 않고 PREPARE/COMMIT/수호성 지휘 맥락에서 우선 노출.
- 대안 재검색: 지휘관 제거는 플레이어 역할 판타지를 약화하므로 기각.
- 장기 적합성: PASS.

### Loop 5
- 전체 범위 재검토: 960×540, 하단 Focus UI, 룰렛, COMMIT, 전선 미니맵, SD 병종, VFX.
- Finding: P0/P1 blocking finding 없음. 실제 가독성은 runtime/human 증거가 없어 PASS로 승격할 수 없음.
- 수정: 구현/사용성 증거를 `NOT_RUN`으로 유지하고 해상도 검증 계약을 명시.
- 대안 재검색: A 유지.
- 장기 적합성: PASS.

```text
ADVERSARIAL_FULL_LOOP_COUNT = 5
CLEAN_REVIEW_EXIT = PLANNING_LEVEL_ONLY
RUNTIME_AND_HUMAN_EVIDENCE = NOT_RUN
```

## 12. 승인 이미지 및 closeout

현재 사용자 승인 visual reference:

```text
IMAGE_ID = OM-IMG-023
IMAGE_STATUS = USER_APPROVED_CURRENT
FULL_RESOLUTION = 1536x1024 PNG
FULL_RESOLUTION_OWNER = GOOGLE_DRIVE_FILE_ID_1-JRf4q95wZm51DsEYPH_-hnH_GLEIAQ5
NOTION_HOME_INLINE_PREVIEW = SERVER_READBACK_PASS
NOTION_VISUAL_BIBLE_INLINE_PREVIEW = SERVER_READBACK_PASS
```

Repository asset record:
`docs/images/planning/canonical/OMENWARD_APPROVED_FRONT_STATE_VISUAL_2026-08-25.md`

New-chat handoff:
`docs/handoffs/2026-08-25-front-state-visual-approved-closeout.md`

이미지 승인만으로 Godot runtime, minimap/SD readability, human usability, player experience, rights review를 PASS로 승격하지 않는다.

## 13. 다음 단계

```text
PROJECT_STATE = PAUSED_QUEUED
CURRENT_NEXT = USER_EXPLICIT_REACTIVATION
IMAGE_GENERATION = STOPPED_AFTER_APPROVED_CLOSEOUT
```

- 새 이미지를 자동 생성하지 않는다.
- Godot/runtime 구현을 자동 재개하지 않는다.
- 다음 세션은 승인 asset `OM-IMG-023`을 실제로 다시 읽고 시작한다.
- 과거 visual 문서의 충돌 문구는 이 Decision의 supersession 경계를 따른다.
