# [현행] 오멘워드 GDD 정본 요약

```yaml
updated_at: 2026-08-05
status: CURRENT_GDD_CANON / PLANNING_ONLY / NOT_IMPLEMENTED
current_main: RESOLVE_FROM_REPOSITORY_DEFAULT_BRANCH
current_decision: OMW-DEC-20260805-PLANNING-SIX-BUILDING-T2-T3-BRANCHES-AND-COUNTERS-V1
current_count: 3_OF_10
vertical_slice_baseline: docs/design/APPROVED_VERTICAL_SLICE_SYSTEM_CONTRACT_2026-07-27.md
product_code_authority: NONE
art_asset_production_authority: NONE
simulation: NOT_RUN
runtime: NOT_RUN
human_validation: NOT_RUN
```

`APPROVED_VERTICAL_SLICE_SYSTEM_CONTRACT_2026-07-27.md`는 시스템 연결 계보다. 식량·건물 5종·주변 지휘소·구형 Stage 시계는 후속 현행 정본이 대체한다.

## 1. 제품 한 문장

> **예고된 세 전선의 공세를 읽고, 제한된 건물로 세 원형 릴의 미래 결과를 설계한 뒤, 룰렛에서 얻은 병력을 한 전선에 비가역 배치해 전황을 뒤집는 전략 오토배틀 게임.**

> **건물로 룰렛을 만들고, 룰렛으로 전선을 지휘한다.**

## 2. 핵심 재미와 루프

```text
예고된 압력
→ 제작한 확률
→ 비가역 전선 커밋
→ 설명 가능한 결과와 다음 설계
```

```text
Stage 압력·Wave 순서 확인
→ 건설·업그레이드·수리와 TokenSource 구성
→ 세 원형 릴 회전
→ 3×3 노출창에서 열·행 이동
→ 보상 확정
→ 보관·판매·한 전선 배치
→ 자동전투·점령·건물 운영
→ 결과 원인 복기
→ Stage 정비·상인
→ 다음 Stage 설계
```

세 원형 릴은 3×3 노출창의 세 열이다.

## 3. 전장·룰렛

- 상·중·하 세 전선과 아군 본진→중간 거점→접전→적 거점→적 본진 구조.
- 주 경로·우회로·공중 Route를 화면에서 구분.
- 일반 병력의 자유로운 전선 횡단 없음.
- Cross-lane 효과는 명시적 능력·건물만 허용하고 사전 표시.
- 열 상하 이동과 행 좌우 순환 이동.
- 이동권은 룰렛 패널 안에서 표시하고 럭키 무료 이동과 구분.
- 보상 등급은 동일 심벌 완성선 수로 결정.
- 멈춘 결과는 immutable `SpinSnapshot`에서 계산하고 한 번만 지급.

```text
금화 토큰 = 인게임 금화 이미지
병종 토큰 = 인게임 T1·T2 병종 이미지
T3 병종 토큰 = 금지
결과 보상 = 실제 지급 병종 이미지
```

## 4. 자원·HUD·기본 건물

| 자원 | 역할 |
|---|---|
| 골드 | 건설·업그레이드·수리·룰렛·상인 |
| 마석 | 전술스킬 |
| 배치 병력·병력 한도 | 전장 병력 규모 |
| 이동권 | 현재 결과와 미래 릴 조작 |

식량은 현행 핵심 HUD 자원이 아니다.

| 건물 | 기본 역할 |
|---|---|
| 금고 | 골드·금화 TokenSource |
| 농장 | 병력 한도 |
| 병영 | 병종 TokenSource·Tier 성장 |
| 방어탑 | 선택 전선 직접 방어 |
| 지휘소 | 현재 MapRun 전체 아군 병력 오라 |
| 마력탑 | 마석 수급·보유량 지원 |

- 건물별 지속 유지비 없음.
- 토큰 초당 공급 없음.
- 평상시 하단은 `[룰렛] [보관함] [건설] [전술스킬] [벨루]`.
- 상인은 Stage 종료 정비시간에 방문.
- 벨루는 설명만 제공하고 결정을 대신하지 않음.

## 5. 건물 T2/T3 전문화 — Decision 3/10

책임 원본:

`docs/design/APPROVED_OMENWARD_SIX_BUILDING_T2_T3_BRANCHES_AND_COUNTERS_2026-08-05.md`

```text
T1 → T2 A → T3 A
T1 → T2 B → T3 B
CROSS_BRANCH = FORBIDDEN
DUAL_T3 = FORBIDDEN
```

- 선택은 건물 인스턴스별이며 다른 인스턴스는 다른 경로를 선택할 수 있다.
- 모든 T2는 `얻는 것`과 `포기하는 것`을 함께 가진다.
- 모든 T3는 결과 곡선·표적 우선순위·전선 교리·Route 대응·자원 사용 시점을 바꾼다.
- 한 분기가 다섯 압력 모두의 최적해가 되어서는 안 된다.
- 철거는 인스턴스와 효과를 제거하며 재건은 새 선택이다. 정확한 환불·비용은 경제 결정이 소유한다.
- 정확한 비용·배율·범위·쿨다운은 시뮬레이션 전 미확정이다.

| 건물 | A 경로 | B 경로 | 선택 의미 |
|---|---|---|---|
| 금고 | 안정→비축 | 행운→징조 대박 | 예산 안정 vs 고완성선 상한 |
| 농장 | 징집→대규모 동원 | 예비→최후 예비대 | 최대 규모 vs 배치 여유 |
| 병영 | 전열→정예 전열 | 기동→징조 대응대 | 정면 역할 vs Route·Layer 대응 |
| 방어탑 | 연사→요격 | 포격→파성 | 다수·빠른 위협 vs 장갑·공성 |
| 지휘소 | 돌격→결전 전선 | 수비→종심 방어 | 집중 돌파 vs 분산 방어 |
| 마력탑 | 유량→맥동 | 저장→징조 저장고 | 잦은 사용 vs Danger·Boss 대비 |

## 6. Stage·Wave·압력

```text
한 MapRun = 20 Stage
기본 Stage = 3 Wave Beat
Danger = 4 / 9 / 14 / 19
Boss = 5 / 10 / 15 / 20
```

```text
1~5 압력 문해력
6~10 압력 조합
11~15 기회비용
16~20 종합 숙련
```

```text
MASS / ARMORED / FLYING / INFILTRATION / SIEGE
```

- Normal: `Probe → Complication → Commitment Test`.
- Danger: 공개된 한 규칙 변형만 사용.
- Boss: Route·태세·목표·호위·집중 공격 기회를 변경.
- Stage 시작 뒤 치명적 요구 카운터를 숨은 무작위로 변경하지 않음.
- 압력 역할·학습 목표는 고정하고 적 패키지·전선·Route는 맵별 작성 변형.
- 각 압력에는 건물·병종·전술·룰렛 준비 전체에서 최소 두 대응 경로가 필요.
- 정확한 시간·적 수·Threat Budget은 시뮬레이션 전 미확정.

구형 `15웨이브=1스테이지`는 `[대체됨]`, 구형 첫 4공세는 `[보류]`다.

## 7. 압력별 건물 준비 경로

| 압력 | 현행 건물 준비 | 후속 필요 |
|---|---|---|
| MASS | 징집 농장·연사탑·수비 지휘소·유량 마력탑 | 광역·다중 표적 병종·전술 |
| ARMORED | 행운 금고·전열 병영·포격탑·돌격 지휘소·저장 마력탑 | 관통·집중 병종·전술 |
| FLYING | 기동 병영·명시적 대공 요격·저장 마력탑 | 실제 대공 병종·전술 |
| INFILTRATION | 농장 예비·기동 병영·요격·수비 지휘소·유량 마력탑 | 후방·Route 병종·전술 |
| SIEGE | 예비 농장·전열 병영·포격탑·돌격 지휘소·저장 마력탑 | 공성 차단 병종·전술 |

건물만으로 하드카운터를 완성하지 않는다. 제품 구현은 Decision 4/10 병종과 5/10 전술 뒤 재검증한다.

## 8. 아트 방향

```text
STYLE = PIXEL_ILLUSTRATION_HYBRID
BATTLEFIELD = PIXEL_READABILITY + ILLUSTRATED_MATERIAL_AND_LIGHT
CLOSEUP_UI = ILLUSTRATION_FORWARD
ALLY = IVORY / BLUE / RESTRAINED_GOLD
VEIL = CHARCOAL / DEEP_PURPLE / CRIMSON / ASYMMETRIC_GOTHIC
```

전장에서는 실루엣·전선·노드 판독이 우선이다. 건물 분기는 색만 바꾸지 않고 상단 장치·무기·배너·마력 구조로 구분하되 T1 실루엣을 유지한다. 실제 자산 제작은 별도 승인 전 시작하지 않는다.

## 9. 작업 운영 정책

```text
BENCHMARK_REQUIRED
INDUSTRY_COMPARISON_REQUIRED
MAX_APPROVAL_BATCH = 10
EARLY_CHECKPOINT = 고위험 충돌 / 세션 종료 / 대규모 정본 영향
TDD = RED → GREEN → REFACTOR
GITHUB_WRITE = EXPLICIT_NON_DEFAULT_BRANCH_ONLY
```

관련 공식 벤치마크와 현업 관행을 비교하고 프로젝트에 맞는 원칙만 승계한다. 이번 Decision의 RED 증거는 Project Core Documentation run 888이다.

## 10. 문서·제품 경계

- `[현행]`만 신규 기획·구현 입력으로 사용.
- `[대체됨]`, `[보류]`, `[폐기]`는 구현 입력 금지.
- 문서 승인과 CI는 제품 구현 완료가 아님.

```text
CURRENT_PRODUCT = LEGACY_PROTOTYPE
LATEST_PLANNING = MAIN_CANON_TARGET / NOT_IMPLEMENTED
PRODUCT_CODE = UNCHANGED
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
```

## 11. 다음 기획 순서

```text
[완료 1/10] 핵심 재미·콘텐츠 가드레일
→ [완료 2/10] Stage 압력 매트릭스
→ [완료 3/10] 건물 T2/T3 분기·카운터
→ [다음 4/10] 병종 역할·시너지·카운터
→ [5/10] 전술스킬·마석
→ [6/10] Stage 종료 상인
→ [7/10] 첫 10~15분 흐름
→ [8/10] Hero·Legendary
→ [9/10] Meta·Hub
→ [10/10] 전체 Run 콘텐츠·UX·아트 종합 검토
```
