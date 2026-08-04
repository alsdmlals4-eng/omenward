# [현행] 오멘워드 GDD 정본 요약

```yaml
updated_at: 2026-08-05
status: CURRENT_GDD_CANON / PLANNING_ONLY / NOT_IMPLEMENTED
current_main: RESOLVE_FROM_REPOSITORY_DEFAULT_BRANCH
current_decision: OMW-DEC-20260805-PLANNING-TROOP-ROLES-SYNERGIES-AND-COUNTERS-V1
current_count: 4_OF_10
vertical_slice_baseline: docs/design/APPROVED_VERTICAL_SLICE_SYSTEM_CONTRACT_2026-07-27.md
product_code_authority: NONE
art_asset_production_authority: NONE
simulation: NOT_RUN
runtime: NOT_RUN
human_validation: NOT_RUN
```

`APPROVED_VERTICAL_SLICE_SYSTEM_CONTRACT_2026-07-27.md`는 시스템 연결 계보다. 최신 기획이 제품에 구현됐다는 뜻이 아니다.

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

## 3. 전장·룰렛

- 상·중·하 세 전선과 아군 본진→중간 거점→접전→적 거점→적 본진 구조.
- 주 경로·우회로·공중 Route를 화면에서 구분.
- 일반 병력의 자유로운 전선 횡단 없음.
- Cross-lane 효과는 명시적 능력·건물만 허용하고 사전 표시.
- 세 원형 릴은 3×3 노출창의 세 열.
- 보상은 immutable `SpinSnapshot`에서 한 번만 지급.

```text
금화 토큰 = 인게임 금화 이미지
병종 토큰 = 인게임 T1·T2 병종 이미지
T3 병종 토큰 = 금지
결과 보상 = 실제 지급 병종 이미지
```

## 4. 자원·기본 건물

```text
자원 = 골드 / 마석 / 배치 병력·병력 한도 / 이동권
건물 = 금고 / 농장 / 병영 / 방어탑 / 지휘소 / 마력탑
```

- 식량은 현행 핵심 HUD 자원이 아니다.
- 지휘소는 현재 MapRun 전체 아군 오라.
- 토큰 초당 공급과 건물별 지속 유지비는 없다.
- 상인은 Stage 종료 정비시간에 등장한다.

## 5. 건물 전문화 — 완료 3/10

책임 원본: `docs/design/APPROVED_OMENWARD_SIX_BUILDING_T2_T3_BRANCHES_AND_COUNTERS_2026-08-05.md`

```text
T1 → T2 A → T3 A
T1 → T2 B → T3 B
CROSS_BRANCH = FORBIDDEN
DUAL_T3 = FORBIDDEN
```

- 선택은 건물 인스턴스별이다.
- 모든 분기는 얻는 것과 포기하는 것을 함께 가진다.
- 정확한 비용·배율·범위·쿨다운은 시뮬레이션 전 미확정이다.

완료 이력:

```text
OMW-DEC-20260805-PLANNING-SIX-BUILDING-T2-T3-BRANCHES-AND-COUNTERS-V1
3_OF_10
```

## 6. 병종 역할·시너지·카운터 — 현행 4/10

책임 원본: `docs/design/APPROVED_OMENWARD_TROOP_ROLES_SYNERGIES_AND_COUNTERS_2026-08-05.md`

```text
ROSTER_BASELINE: 10
ROSTER_COUNT_IS_NOT_SACRED
ROSTER_MIN_MAX: NOT_PRESET
```

| 병종 | 핵심 역할 | 주 압력 |
|---|---|---|
| 방패수호병 | 전선 고정·후열 보호 | MASS·INFILTRATION |
| 대검병 | 근접 광역·밀집 해체 | MASS |
| 창병 | 대형·돌진·공성 차단 | SIEGE·ARMORED |
| 궁수 | 공중 억제·원거리 견제 | FLYING |
| 마도사 | 장갑 약화·제한 광역 | ARMORED·MASS |
| 사제 | 유지력·보호·회복 | 장기 복합 압력 |
| 암살자 | 우회 Route 추적·후열 제거 | INFILTRATION·SIEGE |
| 기병 | 공개 Route 신속 대응 | INFILTRATION·SIEGE |
| 비행병 | 공중 우세·후방 급습 | FLYING·SIEGE |
| 거인 | 장갑 돌파·승리 전선 구조물 파괴 | ARMORED·SIEGE |

규칙:

- 다섯 압력 각각에 최소 두 병종 대응 경로를 둔다.
- 단일 하드키 병종은 금지한다.
- 시너지는 관찰 가능한 전장 행동이며 단순 세트 보너스는 금지한다.
- 전열/기동 병영은 후보 가중을 바꾸되 반대 계열을 영구 삭제하지 않는다.
- 병종 수 증감은 역할 공백·중복·룰렛 학습량·아트 비용을 근거로 별도 승인한다.
- T3 병종은 룰렛 토큰으로 등장하지 않는다.
- 정확한 수치·AI·가중치는 `PENDING_SIMULATION`이다.

## 7. 압력별 병종 대응

| 압력 | 주 대응 | 보조 |
|---|---|---|
| MASS | 대검병·마도사 | 방패수호병 |
| ARMORED | 마도사·창병 | 거인 |
| FLYING | 궁수·비행병 | 요격탑·후속 전술 |
| INFILTRATION | 암살자·기병 | 후방 방패수호병 |
| SIEGE | 창병·기병/암살자 | 거인 역공 |

병종 대응은 건물·전술 대응을 대체하지 않는다.

## 8. Stage·Wave·압력

```text
한 MapRun = 20 Stage
기본 Stage = 3 Wave Beat
Danger = 4 / 9 / 14 / 19
Boss = 5 / 10 / 15 / 20
압력 = MASS / ARMORED / FLYING / INFILTRATION / SIEGE
```

- Danger는 공개된 한 규칙 변형만 사용.
- Boss는 Route·태세·목표·호위·집중 공격 기회를 변경.
- Stage 시작 뒤 치명적 요구 카운터를 숨은 무작위로 변경하지 않음.
- 정확한 시간·적 수·Threat Budget은 시뮬레이션 전 미확정.

## 9. 아트 방향

```text
STYLE = PIXEL_ILLUSTRATION_HYBRID
BATTLEFIELD = PIXEL_READABILITY + ILLUSTRATED_MATERIAL_AND_LIGHT
CLOSEUP_UI = ILLUSTRATION_FORWARD
ALLY = IVORY / BLUE / RESTRAINED_GOLD
VEIL = CHARCOAL / DEEP_PURPLE / CRIMSON / ASYMMETRIC_GOTHIC
```

전장에서는 실루엣·전선·노드 판독이 우선이다. 실제 자산 제작은 별도 승인 전 시작하지 않는다.

## 10. 작업 운영 정책

```text
BENCHMARK_REQUIRED
INDUSTRY_COMPARISON_REQUIRED
MAX_APPROVAL_BATCH = 10
EARLY_CHECKPOINT = 고위험 충돌 / 세션 종료 / 대규모 정본 영향
TDD = RED → GREEN → REFACTOR
GITHUB_WRITE = EXPLICIT_NON_DEFAULT_BRANCH_ONLY
```

## 11. 문서·제품 경계

```text
CURRENT_PRODUCT = LEGACY_PROTOTYPE
LATEST_PLANNING = MAIN_CANON_TARGET / NOT_IMPLEMENTED
PRODUCT_CODE = UNCHANGED
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
```

`data/units/*.tres`는 Legacy Prototype 증거이며 최신 구현 입력이 아니다.

## 12. 다음 기획 순서

```text
[완료 1/10] 핵심 재미·콘텐츠 가드레일
→ [완료 2/10] Stage 압력 매트릭스
→ [완료 3/10] 건물 T2/T3 분기·카운터
→ [현행 4/10] 병종 역할·시너지·카운터
→ [다음 5/10] 전술스킬·마석
→ [6/10] Stage 종료 상인
→ [7/10] 첫 10~15분 흐름
→ [8/10] Hero·Legendary
→ [9/10] Meta·Hub
→ [10/10] 전체 Run 콘텐츠·UX·아트 종합 검토
```