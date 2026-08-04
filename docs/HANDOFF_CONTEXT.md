# [현행] OMENWARD 프로젝트 인수인계 컨텍스트

```yaml
updated_at: 2026-08-04
project: OMENWARD / 오멘워드
work_mode: TOTAL_PLANNING
phase: CORE_FUN_AND_CONTENT_DEEPENING
current_decision: OMW-DEC-20260804-PLANNING-STAGE-WAVE-DANGER-BOSS-PRESSURE-MATRIX-V1
current_process_policy: OMW-PROC-20260804-DYNAMIC-CURRENT-MAIN-AND-DOCUMENT-LIFECYCLE-V1
current_main: RESOLVE_FROM_REPOSITORY_DEFAULT_BRANCH
current_grill_me_count: 2_OF_10
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
CURRENT_IMPLEMENTATION_STATUS.md
PROJECT_CANON_DECISION_LEDGER.md
DECISIONS_PENDING.md
```

작업 주제의 파일이 lifecycle registry에서 `[현행]`인지 확인한 뒤 사용한다.

## 2. 핵심 재미

> **건물로 룰렛을 만들고, 룰렛으로 전선을 지휘한다.**

```text
예고된 압력
→ 제작한 확률
→ 비가역 전선 커밋
→ 설명 가능한 결과·다음 설계
```

세 원형 릴은 3×3 노출창의 세 열을 구성한다.

## 3. 현행 Stage 구조

```text
한 MapRun = 20 Stage
기본 Stage = 3 Wave Beat
Danger = Stage 4 / 9 / 14 / 19
Boss = Stage 5 / 10 / 15 / 20
```

네 막:

```text
Stage 1~5   = 압력 문해력
Stage 6~10  = 압력 조합
Stage 11~15 = 기회비용
Stage 16~20 = 종합 숙련
```

압력:

```text
MASS / ARMORED / FLYING / INFILTRATION / SIEGE
```

Wave Beat:

```text
Normal = Probe → Complication → Commitment Test
Danger = Distortion Introduction → Overlap → Consequence
Boss = Approach → Boss Entry → Finale
```

## 4. Stage 공정성 약속

- Stage 시작 전에 주·보조 압력, 전선, Route, 예상 목표, 치명적 행동을 공개한다.
- Danger는 한 가지 공개 규칙 변형만 사용한다.
- Boss는 HP만 늘리지 않고 Route·태세·목표·호위·집중 공격 기회를 바꾼다.
- Stage 시작 뒤 필요한 카운터·치명적 Route를 숨은 무작위로 바꾸지 않는다.
- 압력 역할·학습 목표는 고정하고 적 패키지·전선·Route는 맵별 작성 변형으로 둔다.
- 정확한 적 수·등장 시각·Threat Budget은 시뮬레이션 전 고정하지 않는다.

## 5. 현행 자원·건물·HUD

```text
자원 = 골드 / 마석 / 배치 병력·병력 한도 / 이동권
건물 = 금고 / 농장 / 병영 / 방어탑 / 지휘소 / 마력탑
하단 = [룰렛] [보관함] [건설] [전술스킬] [벨루]
상인 = Stage 종료 정비시간
지휘소 = 현재 MapRun 전체 아군 병력 오라
```

- 식량은 현행 핵심 HUD 자원이 아니다.
- 건물 지속 유지비 없음.
- 토큰 초당 공급 없음.
- T3 병종 이미지는 룰렛 토큰 금지.

## 6. 전장·룰렛

- 상·중·하 세 전선과 보이는 주·우회·공중 Route.
- Ground·Flying·침투 역할을 화면에서 구분.
- 기본 Target은 같은 전선/Route.
- Cross-lane은 명시적 능력·건물만 허용하고 사전 표시.
- 룰렛 이동권은 패널 내부 `n/3`.
- 금화·병종 토큰은 인게임 금화·T1/T2 병종 이미지를 재사용.

## 7. 문서 상태

```text
[현행] = 사용 허용
[대체됨] = 후속 정본 사용
[보류] = 재검증 전 사용 금지
[폐기] = 사용 금지
[증거] = 과거 사실만 허용
```

### [대체됨]

- `OMENWARD_GAME_DESIGN.md`.
- `APPROVED_15_WAVE_STAGE_CLOCK_AND_OVERTIME_V2.md`.
- 구형 Dopamine/첫 10분 원칙 문서.
- 과거 post-merge 상태 문서.

### [보류]

- 구형 첫 10분 상세 흐름.
- `APPROVED_TUTORIAL_FIRST_FOUR_WAVES_BALANCE_V1.md`.
- Hero·Legendary family.
- Meta·Hub.
- 구형 구현 계획.

### [폐기]

- 식량 현행 HUD 자원.
- 건물 5종.
- 주변 범위 지휘소 오라.
- `15웨이브=1스테이지`·고정 60초 공세.
- Danger의 핵심 기능·치명적 정보 차단.
- 전투 중 숨은 필수 카운터 변경.
- 별도 룰렛 금화·병종 아이콘.
- T3 병종 룰렛 토큰.

## 8. 적대적 검토

책임 원본:

`reviews/ADVERSARIAL_STAGE_PRESSURE_REPLAYABILITY_AND_FAIRNESS_REVIEW_2026-08-04.md`

핵심 결론:

```text
CORE_FIT = STRONG
CONTENT_PROGRESSION = COHERENT
REPLAYABILITY = VIABLE_WITH_AUTHORED_VARIANTS
FAIRNESS = PASS_IF_FULL_OMEN_DISCLOSURE_IS_PRESERVED
IMPLEMENTATION_READINESS = BLOCKED_BY_BUILDING_AND_TROOP_COUNTER_DECISIONS
```

## 9. GPT·Codex 경계

```text
GPT / Work = 핵심 재미·콘텐츠·플레이어 규칙·UX·아트·검수 기준
Codex = 좌표·자료구조·알고리즘·경로탐색·Spawn 데이터 구조·성능·코드·테스트
```

정확한 Wave 시간·수량·Threat Budget을 기획 추정치로 구현하지 않는다.

## 10. 현재 금지선

```text
CURRENT_PRODUCT = LEGACY_PROTOTYPE
LATEST_APPROVED = STAGE_PRESSURE_MATRIX_NOT_IMPLEMENTED
PRODUCT_CODE = UNCHANGED
SIMULATION_TOOL_CODE = NOT_AUTHORIZED
ART_ASSET_PRODUCTION = NOT_AUTHORIZED
IMAGE_GENERATION = STOPPED_BY_USER
BALANCE_CONCLUSION = FORBIDDEN
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
```

## 11. 다음 작업

```text
1/10 완료 = 핵심 재미·콘텐츠 가드레일
2/10 완료 = Stage·Wave·Danger·Boss 압력 매트릭스
3/10 다음 = 건물 6종 T2/T3 분기·카운터
4/10 = 병종 역할·시너지·카운터
5/10 = 전술스킬·마석
```
