# [현행] 오멘워드 프로젝트 코어

```yaml
project: OMENWARD / 오멘워드
updated_at: 2026-08-05
repository: alsdmlals4-eng/omenward
work_mode: PLANNING_ONLY_PROFILE
current_decision: OMW-DEC-20260805-PLANNING-SIX-BUILDING-T2-T3-BRANCHES-AND-COUNTERS-V1
current_count: 3_OF_10
process_policy: OMW-PROC-20260805-BENCHMARK-TDD-APPROVAL-BATCH-V1
제품 코드: `NOT_AUTHORIZED`
implementation: VERTICAL_SLICE_NOT_IMPLEMENTED
legacy_evidence: LEGACY_C1_C2_C3_PROVEN
human_validation: HUMAN_QA_NOT_RUN
```

현행 책임 원본:

- 전체 시스템 연결 계보: `docs/design/APPROVED_VERTICAL_SLICE_SYSTEM_CONTRACT_2026-07-27.md`
- 현행 GDD: `docs/OMENWARD_GDD_CURRENT_CANON.md`
- 핵심 재미: `docs/design/APPROVED_OMENWARD_CORE_FUN_AND_CONTENT_GUARDRAILS_2026-08-04.md`
- Stage 압력: `docs/design/APPROVED_OMENWARD_STAGE_WAVE_DANGER_BOSS_PRESSURE_MATRIX_2026-08-04.md`
- 건물 전문화: `docs/design/APPROVED_OMENWARD_SIX_BUILDING_T2_T3_BRANCHES_AND_COUNTERS_2026-08-05.md`
- 문서 수명주기: `docs/DOCUMENT_LIFECYCLE_REGISTRY.md`

`APPROVED_VERTICAL_SLICE_SYSTEM_CONTRACT_2026-07-27.md`는 시스템 연결 계보를 보존한다. 식량·건물 5종·주변 지휘소·구형 Stage 시계는 후속 현행 정본이 대체한다.

## 1. 정체성·핵심 재미

> **건물로 룰렛을 만들고, 룰렛으로 전선을 지휘한다.**

```text
예고된 압력
→ 제작한 확률
→ 비가역 전선 커밋
→ 설명 가능한 결과와 다음 설계
```

1. 다음 공세의 전선·Route·특수 행동을 읽는다.
2. 건물과 TokenSource로 미래 릴을 설계한다.
3. 3×3 노출창에서 제한된 이동권을 사용한다.
4. 보관·판매·한 전선 배치 중 선택한다.
5. 결과를 복기해 다음 Stage의 건물·릴·배치를 수정한다.

새 시스템은 공세 예측, 릴 설계, 결과 처리, 전선 결과, 복기 중 최소 두 축을 바꿔야 한다. 숫자만 증가시키는 기능은 추가하지 않는다.

## 2. 핵심 루프

```text
Stage 압력·Wave 순서 확인
→ 건설·TokenSource 구성
→ 룰렛 회전·열/행 이동
→ 보상 확정
→ 보관·판매·한 전선 비가역 배치
→ 자동전투·점령·건물 운영
→ 결과 원인 복기
→ 정비·상인·다음 Stage 설계
```

세 원형 릴은 3×3 노출창의 세 열이다.

## 3. 전장·룰렛 불변 조건

- 상·중·하 세 전선과 보이는 주 경로·우회로·공중 Route.
- 일반 병력의 자유로운 전선 횡단 없음.
- Cross-lane 효과는 명시적 능력·건물만 허용하고 사전 표시.
- 열 상하 이동과 행 좌우 순환 이동.
- 멈춘 결과는 immutable `SpinSnapshot`에서 판정.
- 보상은 명시적 확정 한 번에만 지급.

```text
금화 토큰 = 인게임 금화 이미지
병종 토큰 = 인게임 T1·T2 병종 이미지
T3 병종 토큰 = 금지
결과 보상 = 실제 지급 병종 이미지
```

좌표·경로탐색·충돌·성능·자료구조는 Codex가 소유한다.

## 4. 현행 자원·건물

```text
현행 자원 집합 = 골드 / 마석 / 배치 병력·병력 한도 / 이동권
현행 건물 집합 = 금고 / 농장 / 병영 / 방어탑 / 지휘소 / 마력탑
```

| 건물 | 기본 역할 |
|---|---|
| 금고 | 골드·금화 TokenSource |
| 농장 | 병력 한도 |
| 병영 | 병종 TokenSource·Tier 성장 |
| 방어탑 | 특정 전선 직접 방어 |
| 지휘소 | 현재 MapRun 전체 아군 오라 |
| 마력탑 | 마석 수급·보유량 지원 |

식량은 현행 핵심 HUD 자원이 아니다. 건물별 지속 유지비와 토큰 초당 공급은 없다. 지휘소는 주변 범위 오라가 아니다.

## 5. 건물 전문화 코어

```text
T1 → T2 A → T3 A
T1 → T2 B → T3 B
CROSS_BRANCH: FORBIDDEN
DUAL_T3: FORBIDDEN
MAPRUN_PERMANENT_CHOICE
```

- 선택은 건물 인스턴스별이다. 다른 인스턴스는 다른 경로를 고를 수 있다.
- 철거는 해당 인스턴스와 효과를 제거하고 재건은 새 선택이다. 정확한 환불·비용은 경제 결정이 소유한다.
- 모든 분기는 `얻는 것`과 `포기하는 것`을 함께 가진다.
- 모든 T3는 결과 곡선·표적 우선순위·전선 교리·Route 대응·자원 사용 시점 중 하나를 바꾼다.
- 한 분기가 다섯 압력 모두의 최적해가 되어서는 안 된다.
- 정확한 비용·배율·범위·쿨다운은 `PENDING_SIMULATION`이다.

```text
금고 = 안정→비축 / 행운→징조 대박
농장 = 징집→대규모 동원 / 예비→최후 예비대
병영 = 전열→정예 전열 / 기동→징조 대응대
방어탑 = 연사→요격 / 포격→파성
지휘소 = 돌격→결전 전선 / 수비→종심 방어
마력탑 = 유량→맥동 / 저장→징조 저장고
```

제품 구현은 병종 역할·전술스킬 정본과 압력 대응 재검증 전 시작하지 않는다.

## 6. Stage 콘텐츠 코어

```text
한 MapRun = 20 Stage
기본 Stage = 3 Wave Beat
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

Danger는 공개된 한 규칙 변형만 사용한다. Boss는 Route·태세·목표·호위·집중 공격 기회를 바꾼다. Stage 시작 뒤 치명적 압력·Route·필요 Layer를 몰래 변경하지 않는다. 각 압력에는 건물·병종·전술·룰렛 준비 전체에서 최소 두 대응 경로가 필요하다.

구형 `15웨이브=1스테이지`는 `[대체됨]`이다. 정확한 적 수·시간·Threat Budget은 시뮬레이션 전 고정하지 않는다.

## 7. HUD·아트

```text
[룰렛] [보관함] [건설] [전술스킬] [벨루]
```

- 자원은 골드·마석·배치 병력/한도, 이동권은 룰렛 패널 안에서 표시.
- 상인은 Stage 종료 정비시간에 등장.
- 벨루는 설명만 제공하고 결정을 대신하지 않음.

```text
STYLE = PIXEL_ILLUSTRATION_HYBRID
ALLY = IVORY / BLUE / RESTRAINED_GOLD
VEIL = CHARCOAL / DEEP_PURPLE / CRIMSON / ASYMMETRIC_GOTHIC
```

전장에서는 실루엣·전선·노드 판독이 우선이며 실제 아트 제작은 별도 승인 전 시작하지 않는다.

## 8. 작업 운영 코어

```text
BENCHMARK_REQUIRED
INDUSTRY_COMPARISON_REQUIRED
MAX_APPROVAL_BATCH: 10
EARLY_CHECKPOINT_ON_HIGH_RISK_CONFLICT
EARLY_CHECKPOINT_ON_SESSION_END
EARLY_CHECKPOINT_ON_LARGE_CANON_IMPACT
TDD_MANDATORY
RED → GREEN → REFACTOR
EXPLICIT_BRANCH_REQUIRED_FOR_GITHUB_MUTATION
DIRECT_MAIN_WRITE: FORBIDDEN
```

관련 벤치마크와 현업 관행을 비교하고 채택·비채택 이유를 기록한다. 승인 10건은 최대 배치 크기이며 고위험 충돌·세션 종료·대규모 정본 영향 시 조기 체크포인트를 허용한다. GitHub 파일 쓰기는 명시적 비기본 branch에서만 수행하고 main은 검증된 PR 병합으로 변경한다.

## 9. 문서·구현 경계

- `[현행]`만 신규 기획·구현 입력으로 사용.
- `[대체됨]`, `[보류]`, `[폐기]`는 구현 입력 금지.
- `[증거]`는 과거 사실만 증명.
- `current_main`과 `context_baseline_commit`은 기본 브랜치에서 동적으로 해석.
- 문서 승인·CI·병합은 제품 구현 완료가 아니다.

```text
VERTICAL_SLICE_NOT_IMPLEMENTED
VERTICAL_SLICE_IMPLEMENTATION_NOT_STARTED
LATEST_AUTOMATED_CONTRACTS_NOT_RUN
LEGACY_C1_C2_C3_PROVEN
LEGACY_C1_ROULETTE_CORE_REMOTE_PROVEN
HUMAN_QA_NOT_RUN
CORE_LOCK_NOT_ALLOWED
```

## 10. 다음 기획 순서

```text
[완료 1/10] 핵심 재미·콘텐츠 가드레일
→ [완료 2/10] Stage·Wave·Danger·Boss 압력 매트릭스
→ [완료 3/10] 건물 6종 T2/T3 분기·카운터
→ [다음 4/10] 병종 역할·시너지·카운터
→ [5/10] 전술스킬·마석
→ [6/10] Stage 종료 상인
→ [7/10] 첫 10~15분 흐름
→ [8/10] Hero·Legendary 재조정
→ [9/10] Meta·Hub 재조정
→ [10/10] 전체 Run 콘텐츠·UX·아트 종합 검토
```
