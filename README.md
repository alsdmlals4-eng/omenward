# OMENWARD / 오멘워드

**오멘워드**는 예고된 세 전선 공세를 읽고, 건물로 세 원형 릴의 미래 결과를 설계한 뒤, 룰렛에서 얻은 병력을 한 전선에 비가역 배치해 전황을 뒤집는 판타지 전략 오토배틀 게임입니다.

> **건물로 룰렛을 만들고, 룰렛으로 전선을 지휘한다.**

```yaml
updated_at: 2026-08-05
current_main: RESOLVE_FROM_REPOSITORY_DEFAULT_BRANCH
work_mode: TOTAL_PLANNING
current_planning_decision: OMW-DEC-20260805-PLANNING-SIX-BUILDING-T2-T3-BRANCHES-AND-COUNTERS-V1
current_planning: SIX_BUILDING_T2_T3_BRANCHES_AND_COUNTERS / NOT_IMPLEMENTED
current_grill_me_count: 3_OF_10
product_code_authority: NONE
art_asset_production_authority: NONE
image_generation: STOPPED_BY_USER
human_validation: HUMAN_QA_NOT_RUN
```

## 핵심 루프

```text
Stage 압력·Wave 순서 확인
→ 건설·TokenSource 구성
→ 세 원형 릴 회전
→ 3×3 노출창에서 열·행 이동
→ 결과 확정
→ 보관·판매·한 전선 배치
→ 자동전투·점령·건물 운영
→ 결과 원인 복기
→ 다음 Stage 설계
```

세 원형 릴은 3×3 노출창의 세 열을 구성합니다.

## 현재 Stage 구조

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

압력은 `MASS / ARMORED / FLYING / INFILTRATION / SIEGE`로 구분합니다. Danger는 공개된 한 가지 규칙 변형만 사용하고, Boss는 HP만 늘리지 않고 Route·태세·목표·호위·집중 공격 기회를 바꿉니다. 치명적 압력과 필요한 대응은 Stage 시작 전에 공개합니다.

## 현재 건물 전문화

기본 건물 6종은 건물 인스턴스별로 다음 공통 문법을 사용합니다.

```text
T1
├─ T2 A → T3 A
└─ T2 B → T3 B
```

- 동일 인스턴스의 교차 분기와 양쪽 T3 완성은 금지합니다.
- 다른 인스턴스는 서로 다른 경로를 선택할 수 있습니다.
- 모든 분기는 `얻는 것`과 `포기하는 것`을 함께 표시합니다.
- T3는 단순 수치 증가가 아니라 결과 곡선·표적 우선순위·전선 교리·Route 대응·자원 사용 시점을 바꿉니다.
- 정확한 비용·배율·범위·쿨다운은 시뮬레이션 전 정본화하지 않습니다.

건물 경로:

```text
금고: 안정→비축 / 행운→징조 대박
농장: 징집→대규모 동원 / 예비→최후 예비대
병영: 전열→정예 전열 / 기동→징조 대응대
방어탑: 연사→요격 / 포격→파성
지휘소: 돌격→결전 전선 / 수비→종심 방어
마력탑: 유량→맥동 / 저장→징조 저장고
```

## 현재 핵심 규칙

- 상·중·하 세 전선과 보이는 주 경로·우회로·공중 Route.
- 골드, 마석, 배치 병력·병력 한도, 룰렛 이동권.
- 기본 건물 6종: 금고, 농장, 병영, 방어탑, 지휘소, 마력탑.
- 지휘소는 현재 MapRun 전체 아군 병력 오라.
- 상인은 Stage 종료 정비시간에만 방문.
- 룰렛 금화·병종 토큰은 인게임 금화·T1/T2 병종 이미지를 재사용.
- T3 병종 이미지는 룰렛 병종 토큰에 사용하지 않음.
- 최종 아트 방향은 픽셀 가독성과 동화풍 일러스트 재질을 결합한 하이브리드.

## 작업 운영 정책

`OMW-PROC-20260805-BENCHMARK-TDD-APPROVAL-BATCH-V1`

- 관련 벤치마크와 현업 비교를 거쳐 권장안을 제시합니다.
- 승인 10건을 최대 배치 크기로 사용합니다.
- 고위험 충돌·세션 종료·정본 영향이 큰 경우 조기 체크포인트를 허용합니다.
- 모든 변경은 `RED → GREEN → REFACTOR` 순서로 진행합니다.
- GitHub 파일 쓰기는 명시적 비기본 branch에서만 수행하고 main은 검증된 PR 병합으로만 변경합니다.

## 먼저 읽을 문서

1. [`AGENTS.md`](AGENTS.md)
2. [`docs/PROJECT_CORE.md`](docs/PROJECT_CORE.md)
3. [`docs/ACTIVE_CONTEXT.md`](docs/ACTIVE_CONTEXT.md)
4. [`docs/DOCUMENTATION_MAP.md`](docs/DOCUMENTATION_MAP.md)
5. [`docs/DOCUMENT_LIFECYCLE_REGISTRY.md`](docs/DOCUMENT_LIFECYCLE_REGISTRY.md)
6. [`docs/OMENWARD_GDD_CURRENT_CANON.md`](docs/OMENWARD_GDD_CURRENT_CANON.md)
7. [`docs/design/APPROVED_OMENWARD_STAGE_WAVE_DANGER_BOSS_PRESSURE_MATRIX_2026-08-04.md`](docs/design/APPROVED_OMENWARD_STAGE_WAVE_DANGER_BOSS_PRESSURE_MATRIX_2026-08-04.md)
8. [`docs/design/APPROVED_OMENWARD_SIX_BUILDING_T2_T3_BRANCHES_AND_COUNTERS_2026-08-05.md`](docs/design/APPROVED_OMENWARD_SIX_BUILDING_T2_T3_BRANCHES_AND_COUNTERS_2026-08-05.md)
9. [`docs/process/APPROVED_BENCHMARK_TDD_AND_APPROVAL_BATCH_POLICY_2026-08-05.md`](docs/process/APPROVED_BENCHMARK_TDD_AND_APPROVAL_BATCH_POLICY_2026-08-05.md)
10. [`docs/CURRENT_IMPLEMENTATION_STATUS.md`](docs/CURRENT_IMPLEMENTATION_STATUS.md)
11. [`docs/DECISIONS_PENDING.md`](docs/DECISIONS_PENDING.md)
12. [`docs/HANDOFF_CONTEXT.md`](docs/HANDOFF_CONTEXT.md)

`[대체됨]`, `[보류]`, `[폐기]` 문서는 신규 기획·Codex 구현·아트 제작 입력으로 사용하지 않습니다.

## 현재 단계

```text
[완료 1/10] 핵심 재미·콘텐츠 가드레일
→ [완료 2/10] Stage·Wave·Danger·Boss 압력 매트릭스
→ [완료 3/10] 건물 6종 T2/T3 분기·카운터
→ [다음 4/10] 병종 역할·시너지·카운터
→ 전술스킬·마석
→ Stage 종료 상인
→ 첫 10~15분 흐름
→ Hero·Legendary 재조정
→ Meta·Hub 재조정
```

제품 코드, 런타임, 실제 아트 자산은 별도 승인 전 변경하지 않습니다.
