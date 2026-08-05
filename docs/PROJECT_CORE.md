# [현행] 오멘워드 프로젝트 코어

```yaml
project: OMENWARD / 오멘워드
updated_at: 2026-08-05
repository: alsdmlals4-eng/omenward
work_mode: PLANNING_ONLY_PROFILE
current_decision: OMW-DEC-20260805-PLANNING-TROOP-ROLES-SYNERGIES-AND-COUNTERS-V1
current_count: 4_OF_10
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
- 병종 역할: `docs/design/APPROVED_OMENWARD_TROOP_ROLES_SYNERGIES_AND_COUNTERS_2026-08-05.md`
- 병종 적대적 검토: `docs/reviews/ADVERSARIAL_TROOP_ROLE_SYNERGY_AND_COUNTER_REVIEW_2026-08-05.md`
- 문서 수명주기: `docs/DOCUMENT_LIFECYCLE_REGISTRY.md`

`APPROVED_VERTICAL_SLICE_SYSTEM_CONTRACT_2026-07-27.md`는 시스템 연결 계보를 보존한다. 최신 기획이 제품에 구현됐다는 뜻이 아니다.

## 1. 정체성·핵심 재미

> **건물로 룰렛을 만들고, 룰렛으로 전선을 지휘한다.**

```text
예고된 압력
→ 제작한 확률
→ 비가역 전선 커밋
→ 설명 가능한 결과와 다음 설계
```

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

식량은 현행 핵심 HUD 자원이 아니다. 건물별 지속 유지비와 토큰 초당 공급은 없다. 지휘소는 현재 MapRun 전체 아군 오라다.

## 5. 건물 전문화 코어

```text
T1 → T2 A → T3 A
T1 → T2 B → T3 B
CROSS_BRANCH: FORBIDDEN
DUAL_T3: FORBIDDEN
MAPRUN_PERMANENT_CHOICE
```

- 선택은 건물 인스턴스별이다.
- 모든 분기는 얻는 것과 포기하는 것을 함께 가진다.
- 정확한 비용·배율·범위·쿨다운은 `PENDING_SIMULATION`이다.

## 6. 병종 역할 코어

```text
ROSTER_BASELINE: 10
ROSTER_COUNT_IS_NOT_SACRED
ROSTER_MIN_MAX: NOT_PRESET
```

기준선:

```text
방패수호병 / 대검병 / 창병 / 궁수 / 마도사
사제 / 암살자 / 기병 / 비행병 / 거인
```

- 다섯 압력 각각에 최소 두 병종 대응 경로를 둔다.
- 병종 수는 역할 공백·중복·학습량·아트 비용을 근거로 별도 승인 후 증감할 수 있다.
- 시너지는 전장에서 관찰되는 행동 연결이며 단순 세트 보너스는 금지한다.
- 전열/기동 병영은 결과 가중을 바꾸되 반대 계열을 영구 삭제하지 않는다.
- 일반 병력의 자유 회수·Cross-lane 이동은 금지한다.
- T3는 룰렛 토큰으로 등장하지 않는다.
- 정확한 병종 수치·AI·가중치는 `PENDING_SIMULATION`이다.

## 7. Stage 콘텐츠 코어

```text
한 MapRun = 20 Stage
기본 Stage = 3 Wave Beat
Danger = 4 / 9 / 14 / 19
Boss = 5 / 10 / 15 / 20
압력 = MASS / ARMORED / FLYING / INFILTRATION / SIEGE
```

Danger는 공개된 한 규칙 변형만 사용한다. Boss는 Route·태세·목표·호위·집중 공격 기회를 바꾼다. Stage 시작 뒤 치명적 압력·Route·필요 Layer를 몰래 변경하지 않는다.

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

## 9. 문서·구현 경계

- `[현행]`만 신규 기획·구현 입력으로 사용.
- `[대체됨]`, `[보류]`, `[폐기]`는 구현 입력 금지.
- `[증거]`는 과거 사실만 증명.
- `data/units/*.tres`는 `LEGACY_PROTOTYPE_UNIT_DATA` 증거이며 최신 구현 입력이 아니다.
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

## 10. 현재 기획 순서

```text
[완료 1/10] 핵심 재미·콘텐츠 가드레일
→ [완료 2/10] Stage·Wave·Danger·Boss 압력 매트릭스
→ [완료 3/10] 건물 6종 T2/T3 분기·카운터
→ [현행 4/10] 병종 역할·시너지·카운터
→ [다음 5/10] 전술스킬·마석
→ [6/10] 상인
→ [7/10] 첫 10~15분
→ [8/10] Hero·Legendary
→ [9/10] Meta·Hub
→ [10/10] 종합 검토
```

완료 이력 보존:

```text
OMW-DEC-20260805-PLANNING-SIX-BUILDING-T2-T3-BRANCHES-AND-COUNTERS-V1
3_OF_10
```