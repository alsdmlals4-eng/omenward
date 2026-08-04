# [현행] OMENWARD 프로젝트 인수인계 컨텍스트

```yaml
updated_at: 2026-08-05
project: OMENWARD / 오멘워드
work_mode: TOTAL_PLANNING
phase: CORE_FUN_AND_CONTENT_DEEPENING
current_decision: OMW-DEC-20260805-PLANNING-SIX-BUILDING-T2-T3-BRANCHES-AND-COUNTERS-V1
current_process_policy: OMW-PROC-20260805-BENCHMARK-TDD-APPROVAL-BATCH-V1
current_main: RESOLVE_FROM_REPOSITORY_DEFAULT_BRANCH
current_grill_me_count: 3_OF_10
working_pr: 138
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
DOCUMENTATION_MAP.md
DOCUMENT_LIFECYCLE_REGISTRY.md
OMENWARD_GDD_CURRENT_CANON.md
design/APPROVED_OMENWARD_STAGE_WAVE_DANGER_BOSS_PRESSURE_MATRIX_2026-08-04.md
design/APPROVED_OMENWARD_SIX_BUILDING_T2_T3_BRANCHES_AND_COUNTERS_2026-08-05.md
process/APPROVED_BENCHMARK_TDD_AND_APPROVAL_BATCH_POLICY_2026-08-05.md
CURRENT_IMPLEMENTATION_STATUS.md
PROJECT_CANON_DECISION_LEDGER.md
DECISIONS_PENDING.md
```

대상 파일이 lifecycle registry에서 `[현행]`인지 확인한 뒤 사용한다.

## 2. 핵심 재미

> **건물로 룰렛을 만들고, 룰렛으로 전선을 지휘한다.**

```text
예고된 압력
→ 제작한 확률
→ 비가역 전선 커밋
→ 설명 가능한 결과·다음 설계
```

세 원형 릴은 3×3 노출창의 세 열이다.

## 3. 현재 Stage 구조

```text
MapRun = 20 Stage
Wave Beat = 3
Danger = 4 / 9 / 14 / 19
Boss = 5 / 10 / 15 / 20
압력 = MASS / ARMORED / FLYING / INFILTRATION / SIEGE
```

```text
1~5 압력 문해력
6~10 압력 조합
11~15 기회비용
16~20 종합 숙련
```

- Stage 시작 전에 압력·전선·Route·목표·치명 행동 공개.
- Danger는 한 공개 규칙 변형.
- Boss는 Route·태세·목표·호위·집중 공격 기회 변경.
- Stage 중 숨은 필수 카운터 변경 금지.
- 정확한 적 수·시간·Threat Budget은 시뮬레이션 전 미확정.

## 4. 현재 건물 전문화

```text
T1 → T2 A → T3 A
T1 → T2 B → T3 B
CROSS_BRANCH = FORBIDDEN
DUAL_T3 = FORBIDDEN
```

- 선택은 건물 인스턴스별.
- 다른 인스턴스는 다른 분기를 선택 가능.
- 모든 분기는 얻는 것과 포기하는 것을 함께 표시.
- T3는 결과 곡선·표적 우선순위·전선 교리·Route 대응·자원 사용 시점을 변경.
- 정확한 비용·배율·범위·쿨다운은 `PENDING_SIMULATION`.

| 건물 | A | B |
|---|---|---|
| 금고 | 안정→비축 | 행운→징조 대박 |
| 농장 | 징집→대규모 동원 | 예비→최후 예비대 |
| 병영 | 전열→정예 전열 | 기동→징조 대응대 |
| 방어탑 | 연사→요격 | 포격→파성 |
| 지휘소 | 돌격→결전 전선 | 수비→종심 방어 |
| 마력탑 | 유량→맥동 | 저장→징조 저장고 |

건물만으로 다섯 압력을 모두 해결하지 않는다. Decision 4 병종과 Decision 5 전술이 대응 공백을 채워야 한다.

## 5. 자원·HUD·자산

```text
자원 = 골드 / 마석 / 배치 병력·병력 한도 / 이동권
건물 = 금고 / 농장 / 병영 / 방어탑 / 지휘소 / 마력탑
하단 = [룰렛] [보관함] [건설] [전술스킬] [벨루]
상인 = Stage 종료 정비시간
STYLE = PIXEL_ILLUSTRATION_HYBRID
```

- 식량·건물 유지비·토큰 초당 공급 없음.
- 금화·병종 토큰은 인게임 금화·T1/T2 병종 이미지를 재사용.
- T3 병종 이미지는 룰렛 토큰 금지.
- 실제 이미지·아트 제작은 중단 상태.

## 6. 작업 운영

```text
BENCHMARK_REQUIRED
INDUSTRY_COMPARISON_REQUIRED
MAX_APPROVAL_BATCH = 10
EARLY_CHECKPOINT = HIGH_RISK_CONFLICT / SESSION_END / LARGE_CANON_IMPACT
TDD = RED → GREEN → REFACTOR
GITHUB_WRITE = EXPLICIT_NON_DEFAULT_BRANCH_ONLY
```

- RED 증거: Project Core Documentation run 888.
- RED 원인: 건물 책임 원본·운영 정책·3/10 중앙 라우팅 부재.
- 복구 증거: accidental default-branch write는 PR #137로 제거했고 main 복구 SHA는 `a426aef7738a2d9aa8c40cf1eddbe97601e22f80`.
- current 작업은 PR #138의 명시적 branch에서 진행.

## 7. 문서 상태

```text
[현행] = 사용 허용
[대체됨] = 후속 정본 사용
[보류] = 재검증 전 사용 금지
[폐기] = 사용 금지
[증거] = 과거 사실만 허용
```

- `[대체됨]`: 구형 master GDD, 15 Wave Stage, 과거 상태 Sync.
- `[보류]`: 첫 10분·첫 4공세·Hero·Legendary·Meta·Hub·구형 구현 계획.
- `[폐기]`: 식량 핵심 자원, 건물 5종, 주변 지휘소, 별도 룰렛 아이콘, T3 룰렛 토큰, 동일 인스턴스 교차 분기·양쪽 T3.

## 8. 적대적 검토 결론

책임 원본:

`reviews/ADVERSARIAL_BUILDING_BRANCH_COUNTER_AND_OPPORTUNITY_COST_REVIEW_2026-08-05.md`

```text
CORE_FIT = STRONG
BRANCH_GRAMMAR = COHERENT
OPPORTUNITY_COST = EXPLICIT
PRESSURE_COVERAGE = STRUCTURALLY_VIABLE_WITH_DEPENDENCIES
PRODUCT_CODE = UNCHANGED
IMPLEMENTATION_READINESS = BLOCKED_BY_TROOP_AND_TACTICAL_DECISIONS
```

주요 위험:

- 한 분기의 지배적 선택화.
- 서로 다른 이름뿐인 거짓 선택.
- 6종×2분기의 정보 과밀.
- FLYING 실제 카운터 공백.
- 금고 이중 증폭·농장 한도 우회·지휘소 중첩·마석 무한 저장·철거 재분기 악용.

## 9. GPT·Codex 경계

```text
GPT / Work = 핵심 재미·콘텐츠·플레이어 규칙·UX·아트·검수 기준
Codex = 자료구조·알고리즘·좌표·경로탐색·Spawn·Targeting·성능·코드·테스트
```

정확한 비용·배율·Wave 시간·Threat Budget을 기획 추정치로 구현하지 않는다.

## 10. 현재 금지선과 다음 Gate

```text
CURRENT_PRODUCT = LEGACY_PROTOTYPE
LATEST_APPROVED = BUILDING_BRANCH_CANON_NOT_IMPLEMENTED
PRODUCT_CODE = UNCHANGED
SIMULATION_TOOL_CODE = NOT_AUTHORIZED
ART_ASSET_PRODUCTION = NOT_AUTHORIZED
IMAGE_GENERATION = STOPPED_BY_USER
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
CURRENT_COUNT = 3_OF_10
NEXT_DECISION = OMW-DEC-20260805-PLANNING-TROOP-ROLES-SYNERGIES-AND-COUNTERS-V1
THEN = OMW-DEC-20260805-PLANNING-TACTICAL-SKILLS-AND-MANA-STONE-V1
```
