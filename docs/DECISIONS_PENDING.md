# [현행] 오멘워드 미확정 결정 목록

```yaml
updated_at: 2026-08-05
current_main: RESOLVE_FROM_REPOSITORY_DEFAULT_BRANCH
current_decision: OMW-DEC-20260805-PLANNING-SIX-BUILDING-T2-T3-BRANCHES-AND-COUNTERS-V1
current_process_policy: OMW-PROC-20260805-BENCHMARK-TDD-APPROVAL-BATCH-V1
lifecycle_policy: OMW-PROC-20260804-DYNAMIC-CURRENT-MAIN-AND-DOCUMENT-LIFECYCLE-V1
current_grill_me_count: 3_OF_10
product_code_authority: NONE
art_asset_production_authority: NONE
image_generation: STOPPED_BY_USER
```

- 전체 시스템 연결 기준선: `docs/design/APPROVED_VERTICAL_SLICE_SYSTEM_CONTRACT_2026-07-27.md`
- 현행 GDD: `docs/OMENWARD_GDD_CURRENT_CANON.md`
- Stage 압력 정본: `docs/design/APPROVED_OMENWARD_STAGE_WAVE_DANGER_BOSS_PRESSURE_MATRIX_2026-08-04.md`
- 건물 전문화 정본: `docs/design/APPROVED_OMENWARD_SIX_BUILDING_T2_T3_BRANCHES_AND_COUNTERS_2026-08-05.md`
- 문서 수명주기: `docs/DOCUMENT_LIFECYCLE_REGISTRY.md`

## 1. Decision 3/10으로 해결된 항목

- 기본 건물 6종이 모두 `T1 → 두 T2 중 하나 → 같은 경로 T3` 문법을 사용.
- 선택은 건물 인스턴스별이며 동일 인스턴스의 교차 분기·양쪽 T3를 금지.
- 다른 인스턴스는 다른 분기를 선택 가능.
- 철거는 인스턴스와 효과를 제거하며 재건은 새 선택. 정확한 환불·비용은 경제 결정으로 이관.
- 모든 분기에 `얻는 것`과 `포기하는 것`을 명시.
- T3는 수치만 올리지 않고 결과 곡선·표적 우선순위·전선 교리·Route 대응·자원 사용 시점을 변경.
- 금고: 안정/행운, 농장: 징집/예비, 병영: 전열/기동.
- 방어탑: 연사/포격, 지휘소: 돌격/수비, 마력탑: 유량/저장.
- 건물만으로 다섯 압력을 모두 해결하지 않고 병종·전술 결정에 의존.
- T3 병종 이미지는 룰렛 토큰에 사용하지 않음.
- 정확한 비용·배율·범위·쿨다운은 `PENDING_SIMULATION`.
- 벤치마킹·현업 비교·승인 10건 최대 배치·조기 체크포인트·TDD·명시적 branch 쓰기를 비카운터 운영 정책으로 확정.

## 2. 다음 Decision — 병종 역할·시너지·카운터 4/10

`OMW-DEC-20260805-PLANNING-TROOP-ROLES-SYNERGIES-AND-COUNTERS-V1`

다룰 내용:

- T1 공통 병종군과 T2 분기 병종의 전투 역할.
- 전열 병영과 기동 병영이 실제로 공급하는 병종 가족.
- Ground·Flying·우회 Route·후방 목표에 대한 공격 가능 Layer.
- `MASS / ARMORED / FLYING / INFILTRATION / SIEGE`별 병종 대응.
- 병종 간 시너지와 서로 대체할 수 없는 포기 비용.
- T3 전문화가 T2 병종 역할을 어떻게 강화하는지.
- 결과 Preview·보관함·배치 화면에서 역할과 한계를 어떻게 설명하는지.
- 건물·병종 사이의 역할 중복과 만능 조합 방지.

다루지 않을 내용:

- exact HP·Damage·공격속도·사거리·이동속도.
- 실제 데이터 Schema·Targeting 알고리즘·AnimationTree.
- T3 병종 룰렛 토큰.
- 제품 코드·Scene·Resource.

## 3. Decision 4/10이 반드시 답할 질문

1. `FLYING`에 최소 두 실제 병종 대응 경로가 있는가.
2. `ARMORED`와 `SIEGE` 대응이 같은 단일 병종으로 수렴하지 않는가.
3. `MASS` 대응이 방어탑만의 역할이 되지 않는가.
4. `INFILTRATION` 대응이 배치 뒤 자유 전선 이동을 요구하지 않는가.
5. T1과 T2 병종이 모두 사용할 이유가 있으며 T2가 단순 상위호환이 아닌가.
6. 전열/기동 병영 분기가 실제 룰렛 결과와 전선 커밋을 다르게 만드는가.
7. 병종 역할이 전술스킬과 건물 전문화를 무효화하지 않는가.
8. 병종 토큰은 인게임 T1/T2 이미지를 재사용하며 T3 전문화는 Preview·배치 정보로 표현되는가.

## 4. 후속 Planning Batch

```text
[완료] 1/10 핵심 재미·콘텐츠 가드레일
[완료] 2/10 Stage·Wave·Danger·Boss 압력 매트릭스
[완료] 3/10 건물 6종 T2/T3 분기·카운터
[다음] 4/10 T1/T2/T3 병종 역할·시너지·카운터
5/10 전술스킬·마석 획득/소비
6/10 Stage 종료 상인 재고·가격·이벤트
7/10 최신 첫 10~15분 흐름·벨루
8/10 Hero·Legendary family 재조정
9/10 Meta·Hub 재조정
10/10 통합 플레이 시나리오·구현 handoff readiness
```

승인 10건은 최대 배치 크기다. P0/P1 정본 충돌·세션 종료·대규모 정본 영향이 있으면 조기 체크포인트를 허용한다.

## 5. 계속 미확정인 수치·경제

- 건물 건설·업그레이드·철거 환불·재건 비용.
- 건물 T2/T3 해금 Stage와 업그레이드 시간.
- 금고 바닥값·대박 조건·비축 상한.
- 농장 한도·예비 슬롯.
- 방어탑 범위·재장전·관통·공격 Layer.
- 지휘소 교리 효과와 중첩 수치.
- 마력탑 Pulse·저장·예약량.
- Stage Wave 길이·Spawn Group·Threat Budget.
- Danger·Boss 보상.

병종·전술 대응과 경제 시뮬레이션 근거가 생긴 뒤 확정한다.

## 6. [보류]

- 구형 첫 10분 타임라인과 첫 4공세 수치.
- 식량·병영 자동생산·바리케이드 기반 튜토리얼.
- Hero·Legendary 문서군.
- Meta Profile·주점·허브 병영·연구.
- 과거 V2 구현 계획.

상세 목록은 `DOCUMENT_LIFECYCLE_REGISTRY.md`가 소유한다.

## 7. [폐기]

- 식량 핵심 HUD 자원.
- 기본 건물 5종과 주변 범위 지휘소.
- `15웨이브=1스테이지`·고정 60초 공세.
- Danger에서 핵심 기능·치명적 정보 제거.
- Stage 중 숨은 필수 카운터 변경.
- 룰렛 전용 금화·병종 상징 아이콘과 T3 병종 룰렛 토큰.
- 동일 건물 인스턴스의 교차 분기·양쪽 T3.
- 건물 하나로 다섯 압력 모두 해결.

## 8. 실제 아트 제작 전 결정

- T1/T2 병종 실루엣·무기·공격 Layer.
- 건물 T2/T3의 상단 장치·무기·배너·마력 구조 차이.
- 압력별 적 실루엣·Route 아이콘.
- Boss VFX 화면 점유 제한.

사용자 별도 지시 전 실제 제작하지 않는다.

## 9. Codex 구현 결정

```text
building and troop data schema
upgrade state ownership and persistence
demolition/rebuild migration
targeting search and distance implementation
stage/wave scheduling
pathfinding, avoidance and collision
performance and automated test architecture
```

플레이어 경험·콘텐츠 역할을 바꾸는 선택은 기획 Gate로 되돌린다.

## 10. 계속 금지되는 항목

```text
PRODUCT_CODE = UNCHANGED
SIMULATION_TOOL_CODE = NOT_AUTHORIZED
ART_ASSET_PRODUCTION = NOT_AUTHORIZED
IMAGE_GENERATION = STOPPED_BY_USER
BALANCE_CONCLUSION = FORBIDDEN
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
```

## 11. Merge Cadence

```text
CURRENT_COUNT = 3_OF_10
MAX_APPROVAL_BATCH = 10
EARLY_CHECKPOINT = HIGH_RISK_CONFLICT / SESSION_END / LARGE_CANON_IMPACT
CURRENT_PR = FRESH_PREFLIGHT_REQUIRED_AFTER_GREEN
```
