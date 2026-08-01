# 오멘워드 시각자료 인덱스

- 갱신일: `2026-08-01`
- 상태: `CURRENT_VISUAL_REFERENCE_ROUTER / SCREEN_BOARD_V2_TEXT_CURRENT / MIGRATION_GAPS_DECLARED`
- 화면 결정: `OMW-DEC-20260801-VISUAL-SCREEN-BOARD-V2`
- 안내자 계약: `docs/design/APPROVED_BELU_GUIDE_IDENTITY_AND_NAMING_CONTRACT_2026-08-01.md`
- 화면 정본: `docs/design/APPROVED_OMENWARD_VISUAL_SCREEN_BOARD_V2_TEXT_SPEC_2026-08-01.md`

이미지 파일만 보고 승인 범위를 추정하지 않는다. 각 자료의 참고·금지 범위와 현재 기획 계약을 함께 읽는다.

## 1. 우선순위

```text
최신 사용자 지시
→ CURRENT_USER_CONFIRMED_DIRECTION
→ 현재 APPROVED 기획·Screen Board V2
→ APPROVED_DIRECTION_REFERENCE
→ PARTIAL_REFERENCE
→ EXPLORATION
→ REJECTED_EVIDENCE / SUPERSEDED / ARCHIVE_SOURCE
```

시각자료의 수치·문구·맵 연결·노드 배치가 현재 기획서와 다르면 현재 기획서가 우선한다.

## 2. 현재 시각 방향

### VR-001 — 전장 UI·병종 월드 스프라이트 형식

- 상태: `APPROVED_DIRECTION_REFERENCE / MIGRATION_PENDING`
- 출처: 2026-07-16 사용자 제공 이미지
- 목표 경로: `docs/images/planning/canonical/omenward_battlefield_ui_and_unit_style_reference_v1.webp`

참고:

- 실제 전장에 삽입되는 소형 고해상도 픽셀 월드 스프라이트.
- 무기·자세·몸통 덩어리와 진영색에 의한 병종 식별.
- 2.5~3등신 전술 미니어처.

금지:

- 이미지의 임시 토폴로지·수치·문구를 제품 정본으로 복제.
- 큰 전신 비율을 전장에 그대로 사용.

### VR-002 — 10병종 × 등급 전개 도감표

- 상태: `SUPERSEDED_FOR_SPRITE_FORMAT / PARTIAL_REFERENCE / MIGRATION_PENDING`

참고:

- 방패·대검·암살·창·궁·기병·사제·마법·비행·거인 역할 구분.
- 등급 상승에 따른 제한적 실루엣 강화.

금지:

- 도감형 전신 비율·장식을 실제 전장 스프라이트나 수집형 영웅으로 사용.

### VR-003 — 아군 공용 병종·성장 표현

- 상태: `CURRENT_USER_CONFIRMED_DIRECTION / PARTIAL_REFERENCE / MIGRATION_PENDING`

참고:

- 백색·청색·금색 아군 언어.
- 작은 전장 크기에서 무기·자세로 역할을 구분.

금지:

- 모든 장식을 제품 애니메이션 수량으로 확정.
- 개별 유닛을 수집형 영웅으로 해석.

### VR-004 — 베일 진영 건축

- 상태: `CURRENT_USER_PROVIDED / PARTIAL_REFERENCE / MIGRATION_PENDING`

참고:

- 비대칭 갑각·가시·붉은 내부 발광·검보라 막 구조.
- 아군의 정돈된 백색 구조와 대비.

금지:

- 그림 속 구조물을 신규 건물 가족이나 노드로 자동 추가.

### VR-005 — 밝은 3전선 전투·병종 구성

- 상태: `CURRENT_USER_CONFIRMED_DIRECTION / APPROVED_DIRECTION_REFERENCE / MIGRATION_PENDING`

참고:

- 하나의 전장 안에서 상·중·하 세 라인을 동시에 읽는 방향.
- 백색·청색·금색 아군과 검보라·적색 베일의 대비.
- 밝은 회화·수채화 계열 환경과 소형 전술 유닛.

금지:

- 이미지의 거점·노드 수량을 제품 토폴로지로 복사.
- HUD 없는 콘셉트를 실제 제품 화면으로 표시.

### VR-006 — 초광각 3전선 배경

- 상태: `CURRENT_USER_PROVIDED / PARTIAL_REFERENCE / MIGRATION_PENDING`

참고:

- 한 전장의 좌우 진영 대비와 세 라인의 진행 방향.

금지:

- 16:9에 단순 축소.
- 중앙 접전지에 건설 노드 추가.

현재 토폴로지:

```text
본진 6노드/진영
중간 거점 3라인×2진영, 거점당 3노드
중앙 접전지 3곳, 노드 0
전체 건설 노드 30
```

### VR-007 — 안내자 벨루

- 상태: `CURRENT_USER_CONFIRMED_DIRECTION / BELU_CANON / PARTIAL_REFERENCE / MIGRATION_PENDING`
- 정본명: `벨루 / Belu`
- 역사 파일명·별칭: `요정 율비 시안.png / 율비`

참고:

- 백색·하늘색·금색 소형 안내자.
- 위험 경고·결과 반응·비모달 안내용 표정 구조.

금지:

- 신규 UI·대사·파일명에 `율비` 사용.
- 플레이어 대신 전술 결정을 수행.
- 정확한 픽셀 크기·프레임·색상값을 시안에서 자동 확정.

## 3. Screen Board V2 이미지 계획

| Image ID | 화면 | 브리프 | 현재 상태 |
|---|---|---|---|
| `OM-IMG-011` | 메인·런 진입 | `screen-briefs/OMENWARD_SCREEN_BRIEF_OM_IMG_011_RUN_ENTRY_2026-08-01.md` | `TEXT_BRIEF_CURRENT / IMAGE_NOT_GENERATED` |
| `OM-IMG-012` | Stage 준비·공세·건설 | `screen-briefs/OMENWARD_SCREEN_BRIEF_OM_IMG_012_STAGE_PREPARATION_2026-08-01.md` | `TEXT_BRIEF_CURRENT / IMAGE_NOT_GENERATED` |
| `OM-IMG-013` | 세 물리 릴 설계 | `screen-briefs/OMENWARD_SCREEN_BRIEF_OM_IMG_013_PHYSICAL_REELS_2026-08-01.md` | `FOUNDATION_1 / IMAGE_NOT_GENERATED` |
| `OM-IMG-014` | PendingReward·보관·판매·배치 | `screen-briefs/OMENWARD_SCREEN_BRIEF_OM_IMG_014_PENDING_REWARD_DEPLOYMENT_2026-08-01.md` | `TEXT_BRIEF_CURRENT / IMAGE_NOT_GENERATED` |
| `OM-IMG-015` | 일반 세 라인 전투 | `screen-briefs/OMENWARD_SCREEN_BRIEF_OM_IMG_015_STANDARD_BATTLE_2026-08-01.md` | `FOUNDATION_2 / IMAGE_NOT_GENERATED` |
| `OM-IMG-016` | Stage 15 경계파쇄자 | `screen-briefs/OMENWARD_SCREEN_BRIEF_OM_IMG_016_BOUNDARY_BREAKER_2026-08-01.md` | `DEPENDS_ON_015 / IMAGE_NOT_GENERATED` |
| `OM-IMG-017` | Stage 정산·인과 복기 | `screen-briefs/OMENWARD_SCREEN_BRIEF_OM_IMG_017_SETTLEMENT_CAUSAL_RECAP_2026-08-01.md` | `TEXT_BRIEF_CURRENT / IMAGE_NOT_GENERATED` |
| `OM-IMG-018` | 패배·제품 유료 Retry | `screen-briefs/OMENWARD_SCREEN_BRIEF_OM_IMG_018_DEFEAT_PAID_RETRY_2026-08-01.md` | `TEXT_BRIEF_CURRENT / IMAGE_NOT_GENERATED` |

생성 순서:

```text
013 → 015 → 012 → 014 → 016 → 017 → 018 → 011 → 8패널 통합 보드
```

통합 보드는 독립 이미지 검수 전 생성하지 않는다.

## 4. 생성 실패·폐기 자료

### VR-008 — 2026-07-31~08-01 화면 보드 실패 묶음

- 상태: `REJECTED_EVIDENCE / DO_NOT_REUSE / CONVERSATION_ONLY`
- 관련 ID: `OM-IMG-005~010`

폐기 사유:

- 일반 다크 판타지 RPG·수집형 영웅·장비 인벤토리로 변질.
- 세 물리 릴을 독립 원형 판 또는 임의 9칸으로 표현.
- 하나의 전장·세 라인·30노드 구조를 오해.
- 기술 상태·범례·보고서 텍스트를 이미지에 과다 삽입.

재사용 금지:

- UI 프레임, 영웅 파티, 장비 인벤토리, 룰렛·전선·노드 배치.

## 5. 기타 누락 자료

| 자료 | 상태 |
|---|---|
| 스타일 후보 6안 비교표 | `MIGRATION_PENDING` |
| image-gen-1/3/4/5 | `MIGRATION_PENDING / PARTIAL_REFERENCE` |
| 어두운 전투의 전술 지도 | `MIGRATION_PENDING / PARTIAL_REFERENCE` |
| 중세 판타지 전장의 전투 중 | `MIGRATION_PENDING / PARTIAL_REFERENCE` |
| 전략적 전투의 시작 | `MIGRATION_PENDING / PARTIAL_REFERENCE` |
| 오멘워드 유닛 도감 | `VR-002 계열 / 형식 폐기` |
| battle_map_tool.html·사용법 | `MIGRATION_PENDING` |
| 룰렛바운드 GDD v0.7 | `ARCHIVE_SOURCE` |

## 6. 이미지 작업 전 Gate

```text
SCREEN_BOARD_V2_TEXT_SPEC: CURRENT
INDEPENDENT_SCREEN_BRIEFS: CURRENT
VISUAL_REFERENCE_BINARY_MIGRATION: PENDING
VISUAL_REFERENCE_INDEX_REVERIFICATION: PENDING
FOUNDATION_IMAGE_013: NOT_GENERATED
FOUNDATION_IMAGE_015: NOT_GENERATED
IMAGE_GENERATION: BLOCKED
```

바이너리 이관 전에는 대화 첨부를 저장소 자산으로 간주하지 않는다.

## 7. 검수 질문

- 최신 사용자 제공 이미지가 저장 가능한 경로와 ID로 등록됐는가.
- 참고·금지 범위를 설명할 수 있는가.
- 전장 노드가 `6/3/0`, 전체 30으로 표현되는가.
- 룰렛이 세 물리 릴·3×3 노출 보드로 표현되는가.
- 하나의 전장과 세 라인이 동시에 읽히는가.
- OM-IMG-005~010과 V1을 재사용하지 않는가.
- 벨루 명칭이 통일됐는가.
- 미확정 수치·재화명·병종명이 마스킹됐는가.

하나라도 답할 수 없으면 이미지 생성과 화면 자산 승격을 중단한다.