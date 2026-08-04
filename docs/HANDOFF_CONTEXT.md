# OMENWARD 프로젝트 인수인계 컨텍스트

```yaml
updated_at: 2026-08-04
project: OMENWARD / 오멘워드
work_mode: TOTAL_PLANNING
phase: POST_MERGE_CANON_SYNC / CORE_FUN_CONTENT_DEEPENING
current_decision: OMW-DEC-20260804-PLANNING-PIXEL-ILLUSTRATION-HYBRID-ART-DIRECTION-V1
current_sync: OMW-SYNC-20260804-POST-MERGE-PIXEL-ILLUSTRATION-HYBRID-CANON-V1
current_process_policy: OMW-PROC-20260804-PLANNING-VISUALS-CODEX-IMPLEMENTATION-BOUNDARY-V1
current_main: d8ce26ee3ee21dbab50839b7a1334116e147789e
last_merged_planning_pr: 133
current_grill_me_count: 0_OF_10
product_code_authority: NONE
art_asset_production_authority: NONE
image_generation: STOPPED_BY_USER
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
process/POST_MERGE_PIXEL_ILLUSTRATION_HYBRID_CANON_SYNC_2026-08-04.md
design/APPROVED_OMENWARD_PIXEL_ILLUSTRATION_HYBRID_ART_DIRECTION_2026-08-04.md
design/APPROVED_OMENWARD_HUD_ROULETTE_LAYOUT_AND_BATTLEFIELD_VIEW_AMENDMENT_2026-08-04.md
design/APPROVED_OMENWARD_COMBAT_HUD_ROULETTE_RESOURCE_MERCHANT_AND_BUILDING_ROSTER_2026-08-04.md
design/APPROVED_OMENWARD_BATTLEFIELD_VISUAL_HIERARCHY_AND_CAMERA_2026-08-04.md
design/APPROVED_OMENWARD_COMBAT_SPACE_ROUTE_AND_TARGETING_EXPERIENCE_2026-08-04.md
```

전체 시스템 제품 범위는 `design/APPROVED_VERTICAL_SLICE_SYSTEM_CONTRACT_2026-07-27.md`가 소유한다. 최신 Decision과 충돌하는 HUD·자원·건물·시각 조항은 Decision 9·10과 HUD Amendment가 우선한다.

## 2. 제품 코어

```text
예고된 세 전선 공세
→ 제한된 건물·TokenSource로 세 원형 릴 설계
→ 릴·행 이동과 회전 결과 확정
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

기술 구현 논의가 핵심 재미·콘텐츠·이미지 논의를 밀어내면 범위를 교정한다. 과거 문서의 `30 TPS`, R00~R130, 정수 좌표·시간, basis point, Schema·정렬 키는 Codex 참고안이며 구현 구속력이 없다.

## 4. 승인된 HUD·룰렛·자원

```text
평상시 하단 = [룰렛] [보관함] [건설] [전술스킬] [벨루]
핵심 자원 = 골드 / 마석 / 배치 병력·병력 한도
이동권 = 룰렛 내부 n/3 + 럭키 무료 이동
상인 = Stage 종료 정비시간
```

룰렛 작업대:

```text
좌측 = 이동권·럭키·병종 Tier·완성선 보상 등급
중앙 = 3×3 룰렛·열 상하·행 좌우 화살표
우측 = 회전 비용·룰렛 돌리기·결과 Preview·결과 확정·벨루
```

기본 건물은 금고·농장·병영·방어탑·지휘소·마력탑이다. 지휘소는 현재 MapRun 전체 아군 오라다.

## 5. 승인된 아트 방향

```text
STYLE = PIXEL_ILLUSTRATION_HYBRID
MOOD = FAIRYTALE_HOLY_FANTASY_VS_VEIL_GOTHIC
BATTLEFIELD = PIXEL_READABILITY + ILLUSTRATED_MATERIAL_AND_LIGHT
CLOSEUP_UI = ILLUSTRATION_FORWARD
```

- 전장에서는 먼 거리 실루엣·진영·길·노드 판독이 우선이다.
- 보상·도감·벨루에서는 일러스트의 동화 감성과 재질·표정을 강화한다.
- 아군은 상아·청색·절제된 금색, Veil은 흑색·심자색·적자색이다.
- Veil은 아군 자산 재도색이 아니라 비대칭·가시·유기 고딕 형태를 사용한다.
- T1→T2→T3는 장비·자세·실루엣·역할 판타지로 성장한다.
- 영웅·전설은 기본 병종 계보를 유지한다.
- 벨루는 일러스트 우선 SD 컷아웃이다.

## 6. 룰렛 자산 재사용 — 변경 금지

```text
금화 토큰 = 인게임 금화 이미지
병종 토큰 = 인게임 T1·T2 병종 이미지
T3 병종 토큰 = 금지
결과 보상 = 실제 지급 병종 이미지
별도 금화·병종 토큰 아이콘 제작 = 금지
```

토큰 → 결과 카드 → 보관함 → 배치 카드 → 전장 병종은 같은 디자인 계보를 사용한다.

## 7. 이미지 상태

```text
IMAGE_GENERATION = STOPPED_BY_USER
EXISTING_GENERATED_IMAGES = SELECTION_EVIDENCE_AND_LAYOUT_REFERENCE_ONLY / NOT_CANON_ASSETS
ART_ASSET_PRODUCTION = NOT_AUTHORIZED
```

비교 이미지에서 사용자가 선택한 것은 스타일 4의 방향이며, 이미지 파일 자체가 최종 자산은 아니다.

## 8. 병합·검증 상태

```text
PR_133 = MERGED
SOURCE_HEAD = 48466c4f669e24e19e2c8be3f4c879bdbfda04a9
MAIN = d8ce26ee3ee21dbab50839b7a1334116e147789e
CI = 842 / 558 / 539 PASS
DOCS_ONLY_PATHS = 19
UNRESOLVED_THREADS = 0
BLOCKERS = 0
```

## 9. 현재 금지선

```text
CURRENT_PRODUCT = LEGACY_PROTOTYPE
LATEST_APPROVED = PIXEL_ILLUSTRATION_HYBRID_ART_DIRECTION_MAIN_CANON_NOT_IMPLEMENTED
PRODUCT_CODE = UNCHANGED
SIMULATION_TOOL_CODE = NOT_AUTHORIZED
ART_ASSET_PRODUCTION = NOT_AUTHORIZED
IMAGE_GENERATION = STOPPED_BY_USER
BALANCE_CONCLUSION = FORBIDDEN
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
```

## 10. 다음 작업

```text
CURRENT_COUNT = 0/10
NEXT = 핵심 재미·콘텐츠 심화
1 = Stage·Wave·Danger·Boss 콘텐츠 압력
2 = 건물 6종 T2/T3 분기·카운터
3 = 전술스킬·마석·Stage 종료 상인
4 = 병종·영웅·전설 시너지·획득 경험
5 = 첫 10~15분 플레이 검증 시나리오
```
