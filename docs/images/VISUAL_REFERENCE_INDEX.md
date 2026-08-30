# 오멘워드 시각자료 인덱스

- 갱신일: 2026-08-30
- 상태: **HISTORICAL_VISUAL_LINEAGE_INDEX / current router는 별도 owner**
- 책임 범위: 사용자가 제공한 이미지, 탐색 시안, 비교표와 도구 산출물의 상태·용도·금지 해석

이 문서는 대화에 있던 이미지를 문서에서 누락하거나, 오래된 시안을 최신 승인안으로 오인하는 일을 방지한다. 이미지 자체보다 이 인덱스의 **상태와 해석 규칙**을 먼저 확인한다.

## 0. 현행 override · 2026-08-28

이 파일의 2026-07~08-26 항목은 **시각 계보/자산 provenance 참고**이며 current visual router가 아니다. 현행 전장·그림체·지도 topology는 다음 repository owner가 소유한다.

- `docs/superpowers/specs/2026-08-28-storybook-sd-three-front-strategic-map-design.md`
- `docs/design/APPROVED_OMENWARD_OPEN_BATTLEFIELD_TOWER_ONLY_FORWARD_LAYOUT_2026-08-28.md`
- `docs/images/planning/OMENWARD_PROJECT_CORE_SCENE_VISUAL_BOARD_2026-08-28.md`
- `docs/images/approved/OMENWARD_STORYBOOK_SD_SHIELD_GUARD_TRUE_ALPHA_PAIR_V1.md`
- `docs/migrations/OMENWARD_NOTION_CURRENT_CONTENT_TO_REPOSITORY_MIGRATION_2026-08-28.md`

```text
CURRENT_VISUAL_STYLE = STORYBOOK_WATERCOLOR_SD_TACTICAL_ILLUSTRATION
CURRENT_MAP_TOPOLOGY = ONE_WARD_CITADEL_ROOT__THREE_SHARED_FRONTS__ONE_VEIL_CITADEL_ROOT
PER_FRONT_MINIMAP = ABSORBED_INTO_PRIMARY_STRATEGIC_MAP
CURRENT_V6_BOARD = USER_CONFIRMED_PLANNING_LOCK__OPEN_BATTLEFIELD_NO_BARRICADE__NOT_RUNTIME_ASSET
```

따라서 아래 `MIGRATION_PENDING`, 옛 `ANIME_PIXEL_ART + CLEAN_PIXEL_ART`, 전선별 미니맵, 병렬 세 도로, Notion에만 남은 과거 생성 queue는 신규 구현·자산 제작의 입력으로 사용하지 않는다.

## 1. 우선순위

```text
최신 사용자 지시
→ docs/CURRENT_CONFIRMED_DECISIONS.md + docs/ACTIVE_CONTEXT.md
→ current visual Decision/spec/asset owner
→ 이 인덱스의 lineage 상태
→ 관련 APPROVED 기획서
→ PARTIAL_REFERENCE 자료
→ EXPLORATION·SUPERSEDED 자료
```

이미지의 화면 안 문구·수치·맵 연결·병종 이름이 현재 책임 기획서와 다르면 기획서가 우선한다. 다만 사용자가 특정 이미지의 형식을 최신 기준으로 다시 지정한 경우 해당 형식 결정은 이 인덱스에 반영하고 이후 작업에 적용한다.

## 2. 현재 승인 runtime pair

### OMW-IMG-20260830-STORYBOOK-SD-SHIELD-GUARD-PAIR-V1 — Storybook SD Shield Guard pair

- 상태: **USER_APPROVED / CANON_REGISTERED / IMPLEMENTED / RUNTIME_NOT_RUN**
- 정본 기록: `docs/images/approved/OMENWARD_STORYBOOK_SD_SHIELD_GUARD_TRUE_ALPHA_PAIR_V1.md`
- Lumern runtime derivative: `assets/art/units/lumern_shield_guard_storybook_idle_v1.png`
- Veil runtime derivative: `assets/art/units/veil_shield_guard_storybook_idle_v1.png`
- 사용처: `data/bootstrap_catalog.tres`의 Shield Guard faction profile 및 Run Command token.
- 유지할 것: 2.5–3등신 전술 미니어처, Lumern의 ivory/navy/gold, Veil의 charcoal/violet, 방패 우선 실루엣, 양 진영의 서로 마주 보는 전진 방향.
- 범위 밖: 이 pair 외의 source-sheet cell, animation atlas, live runtime/readability, release rights. 이들은 이 record의 PASS가 아니다.

## 3. Historical visual lineage

### ASSET-UNIT-VEIL-SHIELD-GUARD-IDLE-V1 — Veil Shield Guard runtime source candidate

- 상태: **USER_APPROVED_CURRENT_VISUAL_ASSET / NOT_IMPLEMENTATION_READY**
- 승인 기록: `docs/images/approved/OMENWARD_ASSET_UNIT_VEIL_SHIELD_GUARD_IDLE_V1_APPROVAL_2026-08-26.md`
- 프로젝트 로컬 원본: `.asset-vault/library/characters/enemies/OMENWARD_ASSET_UNIT_VEIL_SHIELD_GUARD_IDLE_V1.png`
- Notion 승인 기록: `25 · Approved Asset · Veil Shield Guard Idle V1`
- 사용할 것: Shield Guard 역할을 읽게 하는 넓은 전면 갑각 방패, Veil의 black-purple/dark-red/carapace-gray 언어, 우향 3/4 전술 소스 포즈.
- 사용하지 않을 것: 보스 체급, 창·긴 뿔·대검 실루엣, 과도한 rift glow와 가시, 이 후보만으로 runtime scale·pivot·atlas·상업 출시 권리를 확정하는 해석.

이 자산은 프로젝트 asset lineage 승인본이며 Godot import 또는 runtime 검증본이 아니다. Pair의 animation production boundary는 `docs/images/planning/OMENWARD_UNIT_ANIMATION_PRODUCTION_CONTRACT_2026-08-26.md`가 소유한다. Mass unit animation atlas는 cleaned-pair geometry/timing addendum 전까지 금지다.

### VR-001 — 전장 UI·병종 월드 스프라이트 형식

- 상태: **APPROVED_DIRECTION_REFERENCE / MIGRATION_PENDING**
- 원본: 2026-07-16 대화에서 사용자가 다시 제공한 첫 번째 이미지
- 목표 저장 경로: `docs/images/planning/canonical/omenward_battlefield_ui_and_unit_style_reference_v1.webp`
- 현재 주의: 방향과 해석은 승인됐으나 위 최종 바이너리 경로의 존재가 아직 확인되지 않았다. 실제 이동 완료 전에는 이미지 저장 완료로 보고하지 않는다.
- 연결 기획서:
  - `docs/design/APPROVED_UNIT_VISUAL_FORMAT_AND_REFERENCE_USE_V1.md`
  - `docs/design/APPROVED_ART_DIRECTION_AND_PRODUCTION_GUIDE_V1.md`
  - `docs/design/APPROVED_UI_ART_AUDIO_POC_BIBLE_V1.md`

참고할 것:

- 병종 이미지는 도감용 전신 일러스트가 아니라 **실제 전장에 삽입되는 소형 고해상도 픽셀 스프라이트 형식**으로 제작한다.
- 작은 크기에서도 무기, 자세, 몸통 덩어리와 진영색으로 병종을 읽을 수 있어야 한다.
- 2.5~3등신 안팎의 전술 미니어처 비율, 선명한 외곽선, 제한된 재질 디테일과 방향성 있는 공격 포즈를 사용한다.
- 아군과 적군은 같은 공용 병종·애니메이션 계약을 사용하되 실루엣 소재와 팔레트를 다르게 만든다.
- 전장·HUD·건설 패널·벨루 영역이 한 화면에서 동시에 읽히는 정보 밀도와 계층을 참고한다.

참고하지 않을 것:

- 이미지 안의 본진·요새·점령지 배치와 연결을 현재 전장 토폴로지로 복사하지 않는다.
- 이미지의 금화·식량·웨이브·체력·비용 수치를 기획 수치로 사용하지 않는다.
- 이미지 안의 임시 세력명, 건물명, 병종 아이콘 배열과 한글 문구를 확정 텍스트로 사용하지 않는다.
- 미니맵처럼 보이는 좌하단 전장 요약은 현재 기획의 `미니맵 없음` 규칙을 대체하지 않는다.

### VR-002 — 10병종 × 등급 전개 도감표

- 상태: **SUPERSEDED_FOR_SPRITE_FORMAT / PARTIAL_REFERENCE / MIGRATION_PENDING**
- 원본: 2026-07-16 대화에서 제공된 두 번째 이미지
- 보존 목적: 병종 10종과 일반·엘리트·영웅·전설의 전개 관계를 한눈에 검토한 과거 시안
- 현재 주의: 이미지 형식은 교체됐으며, 원본 바이너리의 공식 저장 경로도 아직 확정되지 않았다.

계속 참고할 것:

- 방패병·대검전사·암살자·창병·궁병·기병·사제·마법사·비행병·거인의 10병종 구분.
- 같은 병종 안에서 일반→엘리트→영웅→전설로 위계가 증가해야 한다는 비교 구조.
- 등급이 올라갈수록 무기, 자세, 실루엣 부속과 제한적 효과가 강화되는 방향.

더 이상 참고하지 않을 것:

- 해당 도감표의 큰 전신 캐릭터 비율과 렌더링 밀도를 실제 전장 스프라이트 형식으로 사용하지 않는다.
- 병종 이미지 제작 형식은 VR-001의 실제 전장 삽입형 픽셀 스프라이트로 변경됐다.
- 도감표에 보이는 등급별 체형 변화, 장식량과 개별 캐릭터 디자인을 그대로 복제하지 않는다.

## 4. 확인된 누락 자료 감사

File Library와 이전 산출물에서 다음 오멘워드 관련 자료가 확인됐다. 현재 활성 책임 문서에 모두 포함된 것은 아니므로 이전 작업자가 존재 여부를 다시 추정하지 않게 목록을 남긴다.

| 자료 | 분류 | 현재 처리 | 목표 위치·조치 |
|---|---|---|---|
| `스타일 후보 6안 비교표.png` | 아트 스타일 비교 | **MIGRATION_PENDING** | `docs/images/planning/research/`로 이동하고 평가 기준·채택/기각 이유 기록 |
| `image-gen-1.png`, `image-gen-3.png`, `image-gen-4.png`, `image-gen-5.png` | 스테이지·환경 탐색 | **MIGRATION_PENDING / PARTIAL_REFERENCE** | 환경 콘셉트 묶음으로 분류하고 각 이미지의 채택·제외 요소 기록 |
| `어두운 전투의 전술 지도.png` | UI·전술 화면 탐색 | **MIGRATION_PENDING / PARTIAL_REFERENCE** | UI 참고 묶음으로 이동, 미니맵·임시 문구는 제외 |
| `중세 판타지 전장의 전투 중.png` | 전장 배치 탐색 | **MIGRATION_PENDING / PARTIAL_REFERENCE** | 전장 토폴로지와 충돌하는 부분을 명시 |
| `전략적 전투의 시작.png` | 전장·하단 UI 탐색 | **MIGRATION_PENDING / PARTIAL_REFERENCE** | UI·카메라·정보 밀도 참고로 분류 |
| `오멘워드 유닛 도감.png` | 과거 병종 도감 | **VR-002와 동일 계열 / 형식 폐기** | 병종·등급 관계만 보존 |
| `battle_map_tool.html` | 전장 설계 도구 | **MIGRATION_PENDING** | `tools/battle_map/` 또는 승인된 도구 경로에 HTML·사용법·버전 기록 |
| `전장_맵_툴_사용법.txt` | 도구 사용법 | **MIGRATION_PENDING** | 맵 툴과 함께 보존 |
| `룰렛바운드_게임기획서_v0.7.docx` | 레거시 GDD | **ARCHIVE_SOURCE** | 최신 GDD와 충돌하지 않게 `archive/` 또는 변경 이력 인덱스로만 보존 |
| `붙여넣은 텍스트 (1).txt` | 게임 제작 방법 메모 | **BASE_CANDIDATE** | 프로젝트 사양이 아니라 Base 공용 기획 방법 자료로 정리 |

`urban-legend`의 저승역 UI·캐릭터 아트 제안서는 다른 프로젝트 자료다. 오멘워드의 파일 누락 감사 대상이나 활성 아트 기준에 포함하지 않는다. 범용 방법만 Base에서 별도로 추출할 수 있다.

## 5. 시각자료 유입 규칙

앞으로 사용자가 이미지·영상 프레임·도표·UI 시안을 제공하면 작업 종료 전에 다음을 수행한다.

1. 저장 가능한 원본 또는 변환본을 프로젝트 경로에 배치한다.
2. 이 인덱스에 ID, 날짜, 상태, 원본 출처와 경로를 기록한다.
3. `참고할 것`, `참고하지 않을 것`, `현재 기획과 달라진 것`을 적는다.
4. 연결되는 APPROVED 기획서와 Work Order에서 읽도록 라우팅한다.
5. 기존 이미지가 교체되면 삭제하지 않고 `SUPERSEDED` 또는 `ARCHIVE_SOURCE`로 상태를 낮춘다.
6. 바이너리 이동을 완료하지 못했으면 반드시 `MIGRATION_PENDING`으로 표시하며 완료했다고 보고하지 않는다.

## 6. Codex·작업자 검수 질문

시각 작업 또는 UI·전장·병종 구현 전 다음을 답할 수 있어야 한다.

- 현재 병종 월드 스프라이트 형식의 승인 기준 이미지는 무엇인가.
- 도감표를 실제 전장 스프라이트 형식으로 사용해도 되는가.
- 참고 이미지의 어떤 요소가 승인됐고 어떤 요소가 임시인가.
- 이미지의 맵 구조가 현재의 단일 Ward root → 세 shared front → 단일 Veil root 토폴로지와 충돌하지 않는가.
- 사용하려는 이미지가 저장소에 있으며 이 인덱스에 상태가 기록됐는가.

답을 확인할 수 없으면 임의로 이미지를 선택하거나 생성하지 않고 이 인덱스와 관련 책임 문서를 먼저 갱신한다.
