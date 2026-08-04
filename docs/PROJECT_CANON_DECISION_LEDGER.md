# 오멘워드 기획 정본 결정 원장

```yaml
updated_at: 2026-08-04
status: CURRENT_DECISION_LEDGER / MAIN_CANONICAL
current_planning_decision: OMW-DEC-20260804-PLANNING-PIXEL-ILLUSTRATION-HYBRID-ART-DIRECTION-V1
current_sync: OMW-SYNC-20260804-POST-MERGE-PIXEL-ILLUSTRATION-HYBRID-CANON-V1
current_process_policy: OMW-PROC-20260804-PLANNING-VISUALS-CODEX-IMPLEMENTATION-BOUNDARY-V1
work_mode: TOTAL_PLANNING
last_merged_planning_pr: 133
last_merged_planning_commit: d8ce26ee3ee21dbab50839b7a1334116e147789e
current_count: 0_OF_10
product_code_authority: NONE
art_asset_production_authority: NONE
image_generation: STOPPED_BY_USER
```

## 1. 운영 원칙

- GitHub APPROVED 문서가 기획 정본이다.
- Google Sheet는 같은 Decision·Sync ID와 main/PR SHA로 동기화한다.
- GPT는 핵심 재미·콘텐츠·플레이어 경험·UX·이미지·아트 Brief를 소유한다.
- Codex는 자료구조·알고리즘·좌표·경로탐색·성능·코드·테스트 구현을 소유한다.
- 10개 승인 Decision마다 fresh preflight와 적대적 검토를 수행한다.
- 사용자 지시 전 제품 코드·실제 아트 자산·추가 이미지 생성을 시작하지 않는다.

## 2. main에 병합된 최근 10개 결정

| 순번 | Decision ID | 핵심 기획 정본 | 구현 경계 |
|---:|---|---|---|
| 1 | `OMW-DEC-20260803-VALIDATION-DETERMINISTIC-SIMULATION-HARNESS-SCOPE-V1` | 결과 재현·원인 복기 요구 | Harness 구조·Schema는 Codex 참고안 |
| 2 | `OMW-DEC-20260803-VALIDATION-COMMON-COMBAT-SCHEMA-AND-RESOLUTION-ORDER-V1` | 동일 조건 공정성·숨은 선공 금지 | phase·정렬·상태 구조는 Codex 참고안 |
| 3 | `OMW-DEC-20260803-VALIDATION-DAMAGE-PROTECTION-AND-STATUS-SEMANTICS-V1` | KINETIC/ARCANE·Barrier·Status 의미 | 내부 Resolver는 Codex 결정 |
| 4 | `OMW-DEC-20260803-VALIDATION-MITIGATION-FORMULA-AND-PROTECTION-NUMERIC-DEFAULTS-V1` | 방어 감소·Barrier·Status 기본값 | 내부 수학 표현은 Codex 결정 |
| 5 | `OMW-DEC-20260803-VALIDATION-FIXED-TICK-TIME-AND-ACTIVATION-DEFAULTS-V1` | 전투 템포·Spawn 선공/무적 금지 | Tick 구현은 Codex 참고안 |
| 6 | `OMW-DEC-20260803-VALIDATION-MODIFIER-STACKING-AND-EFFECT-PRECEDENCE-V1` | Buff 폭증 방지·효과 가독성 | Resolver·Snapshot 저장은 Codex 참고안 |
| 7 | `OMW-DEC-20260804-PLANNING-COMBAT-SPACE-ROUTE-AND-TARGETING-EXPERIENCE-V1` | 세 전선·명시적 Route·Targeting 경험 | 좌표·Pathfinding·충돌은 Codex 결정 |
| 8 | `OMW-DEC-20260804-PLANNING-BATTLEFIELD-VISUAL-HIERARCHY-AND-CAMERA-V1` | 고각도 3/4 카메라·전장 전체 가시성 | Camera transform·FOV는 Codex 결정 |
| 9 | `OMW-DEC-20260804-PLANNING-COMBAT-HUD-REEL-AND-BUILD-UX-V1` | HUD·룰렛·자원·상인·건물 6종·벨루 | UI Scene·입력·데이터 구조는 Codex 결정 |
| 10 | `OMW-DEC-20260804-PLANNING-PIXEL-ILLUSTRATION-HYBRID-ART-DIRECTION-V1` | 픽셀 가독성+동화풍 일러스트·아군/Veil·건물·벨루·자산 계보 | 실제 제작 규격·렌더링·애니메이션은 후속 승인 |

## 3. Decision 10 책임 원본

`design/APPROVED_OMENWARD_PIXEL_ILLUSTRATION_HYBRID_ART_DIRECTION_2026-08-04.md`

```text
STYLE = PIXEL_ILLUSTRATION_HYBRID
MOOD = FAIRYTALE_HOLY_FANTASY_VS_VEIL_GOTHIC
BATTLEFIELD = PIXEL_READABILITY + ILLUSTRATED_MATERIAL_AND_LIGHT
CLOSEUP_UI = ILLUSTRATION_FORWARD
```

룰렛 자산:

```text
금화 토큰 = 인게임 금화 이미지
병종 토큰 = 인게임 T1·T2 병종 이미지
T3 병종 토큰 = 금지
결과 보상 = 실제 지급 병종 이미지
별도 금화·병종 토큰 아이콘 제작 = 금지
```

## 4. Merge 증거

```text
SOURCE_PR = 133
SOURCE_HEAD = 48466c4f669e24e19e2c8be3f4c879bdbfda04a9
MERGED_MAIN = d8ce26ee3ee21dbab50839b7a1334116e147789e
CI = 842 / 558 / 539 PASS
BEHIND = 0
CHANGED_PATHS = 19 DOCS_ONLY
UNRESOLVED_THREADS = 0
OPEN_P0 = 0
OPEN_P1 = 0
MERGE_BLOCKER = 0
```

## 5. 비카운트 운영 정책·Sync

- `OMW-PROC-20260804-PLANNING-VISUALS-CODEX-IMPLEMENTATION-BOUNDARY-V1`
- `OMW-SYNC-20260804-POST-MERGE-PIXEL-ILLUSTRATION-HYBRID-CANON-V1`

정책·유지보수 Sync·HUD Amendment는 Decision 수에 포함하지 않는다.

## 6. 감사 계보

```text
OMW-AUD-208~289 = Decisions 1~6 and maintenance
OMW-AUD-290~299 = combat-space and planning-boundary audit
OMW-AUD-300~313 = battlefield visual hierarchy and camera audit
OMW-AUD-314~343 = HUD, roulette, resources, merchant, buildings and asset reuse
OMW-AUD-344~359 = pixel·illustration hybrid art-direction audit
```

## 7. 현재 금지선

```text
CURRENT_PRODUCT = LEGACY_PROTOTYPE
LATEST_PLANNING = MAIN_CANONICAL_NOT_IMPLEMENTED
PRODUCT_CODE = UNCHANGED
SIMULATION_TOOL_CODE = NOT_AUTHORIZED
ART_ASSET_PRODUCTION = NOT_AUTHORIZED
IMAGE_GENERATION = STOPPED_BY_USER
BALANCE_CONCLUSION = FORBIDDEN
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
```

## 8. 다음 운영 Gate

```text
CURRENT_COUNT_SINCE_MERGE = 0_OF_10
NEXT_PLANNING = CORE_FUN_AND_CONTENT_DEEPENING
NEXT_PREFLIGHT = AFTER_10_NEW_APPROVED_DECISIONS
NEXT_IMPLEMENTATION = SEPARATELY_AUTHORIZED_CODEX_HANDOFF
```
