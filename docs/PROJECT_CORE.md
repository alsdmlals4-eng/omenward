# 오멘워드 프로젝트 코어

- 공식명: **오멘워드 / OMENWARD**
- 갱신일: `2026-07-31`
- 기준 저장소: `alsdmlals4-eng/omenward`
- 작업 모드: `PLAN / PLANNING_ONLY_PROFILE`
- 전달 목표: `FULL_SYSTEM_VERTICAL_SLICE / MINIMUM_CONTENT_BREADTH`
- 코어 PoC: `SKIPPED_BY_USER_DECISION`
- 제품 코드: `NOT_AUTHORIZED`
- 구현 상태: `VERTICAL_SLICE_NOT_IMPLEMENTED`
- 사람 검증: `HUMAN_QA_NOT_RUN`

## 현재 권위 계약

1. 전체 시스템 관계: `docs/design/APPROVED_VERTICAL_SLICE_SYSTEM_CONTRACT_2026-07-27.md`
2. 런 시간·피로도: `docs/design/APPROVED_VERTICAL_SLICE_RUN_DURATION_AND_FATIGUE_CONTRACT_2026-07-31.md`
3. 20 Stage·첫 10분: `docs/design/APPROVED_VERTICAL_SLICE_20_STAGE_FOUR_ACT_AND_FIRST_10_MINUTES_CONTRACT_2026-07-31.md`
4. 콘텐츠 Manifest·미션 풀: `docs/design/APPROVED_VERTICAL_SLICE_CONTENT_MANIFEST_AND_MISSION_CARD_POOL_2026-07-31.md`
5. 패배·영구재화 재시도: `docs/design/APPROVED_VERTICAL_SLICE_DEFEAT_AND_PAID_RETRY_PRINCIPLE_2026-07-31.md`
6. Benchmark-First 원칙: `docs/operations/BENCHMARK_FIRST_PLANNING_RULE_2026-07-31.md`
7. 즉시 정본 동기화: `docs/operations/CANON_SYNC_PROTOCOL_2026-07-31.md`
8. 적대적 검토: `docs/reviews/ADVERSARIAL_VERTICAL_SLICE_REVIEW_2026-07-27.md`

현재 추가 승인 결정:

- `OMW-DEC-20260731-CONTENT-MANIFEST-V1`
- `OMW-DEC-20260731-CANON-SYNC-V1`
- `OMW-DEC-20260731-DEFEAT-RETRY-V1`

이 문서는 제품 정체성, 핵심 인과, 불변 조건, 현재 범위와 구현 게이트를 소유한다. 세부 규칙은 위 분야별 승인 계약이 소유한다. 충돌 시 **최신 사용자 지시 → 이 문서 → 최신 분야별 승인 계약 → 기존 승인 문서 → legacy evidence** 순으로 적용한다.

문서 승인, Sheet 동기화, 브랜치·PR 생성은 제품 구현을 의미하지 않는다. 자동 계약과 사람 플레이 증거 전에는 `CORE_LOCK`, `VERTICAL_SLICE_PROVEN`, `MVP_COMPLETE`를 사용하지 않는다.

---

## 1. 정체성

> **예고된 세 전선의 공세를 읽고, 제한된 건물로 세 원형 릴의 토큰 구조를 설계·영구 편집한 뒤, 당첨 병력을 어느 전선에 커밋할지 결정해 전황을 뒤집는 실시간 전략 오토배틀 게임.**

시장 차별화:

> **독립 3×3 슬롯으로 병력을 뽑는 게임이 아니라, 건물과 가로 이동으로 미래 룰렛 자체를 다시 쓰는 3전선 지휘 게임.**

짧은 문구:

> **건물로 룰렛을 만들고, 룰렛으로 전선을 지휘한다.**

---

## 2. 플레이어의 핵심 책임

1. **예측** — 다음 공세의 라인, 병종, 수량과 특수 행동을 읽는다.
2. **건설** — 금고·농장·타워·병영·지휘소의 제한된 노드를 배분한다.
3. **릴 설계** — TokenSource 결속 토큰과 영구 가로 이동으로 세 원형 릴을 바꾼다.
4. **결과 조작** — 멈춘 결과를 예측·조작하고 명시적으로 확정한다.
5. **전선 커밋** — 보관·판매·배치 중 하나를 선택하고 병력을 한 라인에 비가역적으로 투입한다.
6. **영토 운영** — 경합 지역과 중간 거점을 점령하고 건물·수리·업그레이드를 관리한다.
7. **장기 런 관리** — 20 Stage 동안 자원, HP, 영토, 릴과 checkpoint를 유지한다.
8. **선택 목표 관리** — 공개된 미션 보상과 기회비용을 비교해 수락하거나 거절한다.
9. **패배 비용 판단** — Stage 5 이후 패배 시 런 종료와 MapRun당 1회의 영구재화 재시도 사이에서 선택한다.

---

## 3. 핵심 루프

```text
Stage 준비
→ 공개 공세 확인
→ 해당 막의 미션 제시 시 선택 또는 거절
→ 건설·업그레이드·수리
→ 물리 룰렛 회전·영구 이동·확정
→ 보관·판매·라인 배치
→ 일반 또는 위험 전투
→ 중앙 경합 지역·중간 거점·본진 공방
→ 미션 판정·정산·checkpoint 저장
→ 다음 Stage 준비
```

첫 1막에는 미션 선택을 추가하지 않는다. 미션은 Stage 6·11·16 준비 단계에서만 제시하며 핵심 루프를 대체하는 별도 미니게임이 아니다.

본진 HP가 0이면 패배 화면으로 전환한다. Stage 5 이후이며 해당 MapRun에서 재시도를 사용하지 않았고 사용 가능한 영구재화가 충분할 때만 실패 Stage 준비 checkpoint 재시도를 선택할 수 있다. 그 외에는 MapRun을 종료한다.

---

## 4. 제품 코어

- 상·중·하 세 라인.
- 각 라인은 `아군 본진 → 아군 중간 거점 → 중앙 경합 지역 → 적 중간 거점 → 적 본진` 구조다.
- 기본·일반 난이도에서는 치명적 공세 정보를 숨기지 않는다.
- 금고와 병영은 물리 건설 노드에 결속된 TokenSource다.
- 금고는 `[금화]`, 병영은 병종 토큰을 세 릴에 하나씩 공급한다.
- 세 릴은 길이 3 이상의 원형 TokenInstance 배열이다.
- 가로 이동은 현재 보드와 미래 릴 배열을 동시에 영구 편집한다.
- 중앙 가로줄이 기본 보상 판정의 선행 조건이다.
- 보상은 멈춤, 조작, 예측, 명시적 확정과 결과 처리의 거래를 거친다.
- 병력은 보관하거나 판매할 수 있지만 배치 후 라인 변경·회수·판매가 불가능하다.
- 일반 Stage의 전술계획 정지와 위험 Stage의 실시간 실행이 대비된다.
- 자동전투는 영토, 건물, 본진 HP, Stage 승패와 다음 준비에 실제 영향을 준다.
- MapRun은 20 Stage이며 안전 경계 checkpoint 저장을 지원한다.
- 본진 HP 0은 기본적으로 MapRun 종료이며, Stage 5 이후 MapRun당 1회 영구재화 유료 재시도를 허용한다.
- 유료 재시도는 실패 Stage 준비 checkpoint와 동일 RNG 계보를 복원한다.
- 벨루는 자동 결정자가 아니라 상황 설명과 선택 근거를 제공한다.
- 미션은 공세 정보를 변경하지 않고 공개된 전술적 기회비용을 추가한다.

---

## 5. 버티컬 슬라이스 범위

```yaml
scope:
  core_poc: skipped
  run_duration:
    standard: 35_minutes
    normal_range: 30_to_40_minutes
    first_run_max: 45_minutes
  stages: 20
  acts:
    - 1_to_5
    - 6_to_10
    - 11_to_15
    - 16_to_20
  systems:
    roulette: included
    economy: included
    storage_selling_food: included
    tier_growth: included
    three_lane_battlefield: included
    capture_construction_repair: included
    missions: included
    meta_progression: included
    checkpoint_save: included
    paid_retry: included
    belu_ux: included
    art_audio_ui: included
```

콘텐츠는 모든 주요 시스템을 기능적으로 연결하되 고유 제작물 수를 통제한다. 가짜 UI나 문서만으로 시스템 연결을 대체하지 않는다.

### 5.1 콘텐츠 Manifest

```yaml
battlefield:
  unique: 1
  act_states: 4
stage_content:
  manifests: 20
  standard_assault_templates: 8
  danger_packages: 4
  boss_behavior_packages: 3
units:
  tier_1: 1
  tier_2: 10
  tier_3: 20
  shared_combat_archetypes: 10
missions:
  cards: 12
  categories:
    frontline: 4
    design: 4
    constraint: 4
```

20개 Stage는 20개의 독립 맵·적 데이터·규칙 세트가 아니다. 한 전장과 공용 아키타입을 라인, Rank, 공세 패키지, 영토 상태와 미션 조건으로 조합한다.

### 5.2 미션 코어

- Stage 6·11·16 준비 단계에서 제시.
- 서로 다른 카테고리 2장 중 1장 선택 또는 모두 거절.
- 동시에 활성 미션 하나.
- 같은 MapRun에서 같은 카드 반복 금지.
- 목표, 판정 시점, 실패 조건과 정확한 보상을 사전 공개.
- 보상 종류는 골드, 사용 가능한 식량, 추가 무료 회전만 사용.
- 시간제 미션, 숨은 보상, 실패 직접 페널티, 전용 화폐·상점·성장 트리를 사용하지 않는다.

### 5.3 패배·재시도 코어

```yaml
paid_retry:
  available_from_stage: 5
  maximum_per_maprun: 1
  restore_point: failed_stage_preparation_checkpoint
  same_rng_lineage: true
  current_run_pending_currency_usable: false
  exact_costs: pending_simulation
```

- Stage 1~4에서는 유료 재시도를 제공하지 않는다.
- 비용은 Stage 5~10 / 11~15 / 16~20의 세 등급이며 후반일수록 높다.
- 현재 런의 미정산 영구재화, 골드, 식량, 무료 회전은 비용으로 사용할 수 없다.
- 개발 무료 재시도는 제품 메타 보상·업적·공식 기록과 분리한다.

---

## 6. 주요 불변 조건

1. 일반 유닛은 세 라인 사이를 자유롭게 횡단하지 않는다.
2. 호위병의 보호 오라는 실제 거리만 사용하므로 라인 경계를 넘을 수 있다.
3. 기본·일반 난이도에서는 라인, 병종, 정확한 수량과 치명적 특수 행동을 사전에 공개한다.
4. 금고·병영 선택은 live 릴의 토큰·출처·인접 순서에 관찰 가능한 영향을 준다.
5. 중앙 가로줄이 동일 비-X 심벌 세 개가 아니면 다른 완성선을 무시한다.
6. 등급은 동일 심벌 완성선 수로 계산한다.
7. 가로 이동은 TokenInstance와 출처를 이동시키며 실행 즉시 확정되고 되돌릴 수 없다.
8. 멈춘 보드의 보상은 immutable SpinSnapshot에서만 계산한다.
9. source 파괴·점령·BLOCKED는 live 릴만 바꾸고 기존 snapshot과 PendingReward를 바꾸지 않는다.
10. 보상은 명시적 확정 한 번에만 생성·지급한다.
11. 보관 중 병력은 식량을 사용하지 않고, 배치 후 라인 변경·회수·판매가 불가능하다.
12. 식량 한도 감소는 기존 병력을 제거·약화하지 않고 신규 배치만 차단한다.
13. 중앙 경합 지역과 중간 거점의 점령속도는 유닛 수·Tier·등급에 영향받지 않는다.
14. 후방 거점을 잃어도 이미 전진한 병력은 후퇴·약화·소멸하지 않는다.
15. 건물 HP와 건설·업그레이드 진행도는 별도다.
16. HP 0 건물은 완전히 제거되고 노드는 즉시 EMPTY가 된다. 잔해와 재건은 없다.
17. 한 건물에는 수리 작업 하나만 붙일 수 있고, 여러 건물은 동시에 수리할 수 있다.
18. 수리는 실제 회복 HP만큼 골드를 실시간 소비하며 지갑은 음수가 되지 않는다.
19. 미션은 베일의 징조와 실제 공세를 거짓으로 만들거나 숨은 적을 추가하지 않는다.
20. 미션을 거절하거나 실패해도 직접 디버프·본진 피해·자원 강제 차감이 없다.
21. 일반 적군 전용 전투 스탯·스킬·AI 복사본을 만들지 않는다.
22. 제품 구현은 별도 계획 승인 전 시작하지 않는다.
23. 문서·Sheet 반영만으로 구현·검증·잠금을 주장하지 않는다.
24. 주요 승인 결정은 같은 결정 ID로 GitHub 권위 문서와 연결 Sheet에 동기화한다.
25. 유료 재시도는 Stage 5 이후 MapRun당 최대 1회다.
26. 유료 재시도는 실패 Stage 준비 checkpoint와 동일 RNG·공세·미션 계보를 복원한다.
27. 현재 런 미정산 영구재화는 재시도 비용으로 사용할 수 없다.
28. 영구재화 차감과 checkpoint 복원은 멱등성을 가진 원자 거래다.
29. 개발 무료 재시도 결과는 정상 제품 보상·업적·공식 기록에 반영하지 않는다.

---

## 7. 건물 코어

| 건물 | 역할 | 성장 |
|---|---|---|
| 금고 | 골드/초 + 금화 토큰 | 선형 T1→T3 |
| 농장 | 식량 생산·한도 | 선형 T1→T3 |
| 타워 | 방어 공격 | T2 연사/포격 분기, T3 계열 강화 |
| 병영 | 병종 토큰 | T2 10병종, T3 각 2전문화 |
| 지휘소 | 범위형 전장 버프 | T2 돌격/수비 분기, T3 계열 강화 |

- 타워만 기본 직접 공격 가능한 건물이다.
- 금고·농장·타워·지휘소는 호환 점령 이전 대상이다.
- 병영은 적 점령 시 BLOCKED다.
- 보관과 판매는 별도 건물이 아니라 플레이어 공통 런 시스템이다.

---

## 8. 전장·병종 코어

### 전장

- 진영당 본진 건설 노드 6개.
- 전체 중간 거점 6개, 거점당 건설 노드 3개.
- 중앙 경합 지역 3개.
- 전체 건설 노드 30개.
- 중앙 경합 지역 소유는 전역 골드/초 보너스를 제공한다.
- 중앙 경합 지역을 점령해야 적 중간 거점으로 진격한다.
- 적 중간 거점을 점령해야 적 본진으로 진격한다.
- 점령 완료 순간 소유권, 수입, 건설 권리와 건물 효과를 원자적으로 이전한다.

### 병종

- Tier 1은 공통 보병.
- Tier 2는 방패, 대검, 암살, 창, 궁, 기병, 사제, 마법, 비행, 거인 10종.
- Tier 3는 각 Tier 2에서 두 전문화, 총 20종.
- Tier 3는 단순 상위호환이 아니라 역할 사이드그레이드다.
- 방패병 계열은 일반 적의 높은 기본 표적 우선도를 가진다.
- 철벽수호병은 정지시간으로 0~3단계 개인 방어를 쌓는다.
- 호위병은 반경 2.5D 내 유효 아군의 직접·광역 최종 HP 손실 25%를 분담한다.

나머지 Tier 3 상세 능력과 정확한 전투 수치는 후속 설계 항목이다.

---

## 9. 시간·저장 코어

- 표준 런 35분, 정상 30~40분, 첫 플레이 최대 45분.
- 위험 Stage는 5·10·15, 최종 위험 Stage는 20.
- 일반 전술계획 정지는 전투, 점령, 회복, 수리와 경제를 모두 정지한다.
- 위험 Stage는 전술계획 정지를 허용하지 않는다.
- Stage 준비와 정산 완료는 versioned checkpoint 안전 경계다.
- 활성 전투 임의 프레임 저장은 버티컬 슬라이스 범위가 아니다.
- checkpoint 실패는 이전 정상본을 파괴하지 않는다.
- 유료 재시도는 실패 Stage 준비 checkpoint를 복원한다.
- 같은 seed·공세·룰렛·미션 계보를 유지하고 준비 선택만 다시 수행한다.
- 재시도 transaction 실패는 영구재화를 손실시키지 않는다.

---

## 10. 기존 구현 증거의 지위

현재 main의 C1·C2·C3는 legacy 설계 기준 증거다.

```text
LEGACY_C1_ROULETTE_CORE_REMOTE_PROVEN
LEGACY_C2_BATTLE_OBJECTIVE_REMOTE_PROVEN
LEGACY_C3_AUTOMATED_CONTRACTS_PROVEN
```

보존 가능한 기반:

- 중앙 판정, 완성선, 등급, 금화 75/200/500% resolver.
- 결정론과 RNG stream 개념.
- 공용 병종 데이터와 진영 Visual 분리.
- 3라인 전투 기반.
- 원인 보고와 snapshot→HUD 경계.

대체 대상:

- 독립 9칸 추첨.
- `capture_power` 합산 점령.
- 구형 중간거점 상태기.
- 스테이지당 전설 제한.
- 구형 공개 럭키.
- 이동 되돌리기·확정 시 소비.
- 단일 StageRun 중심 수명주기.
- 작업자 임금·글로벌 수리 예산·재건 계약.
- 3스테이지 최소 슬라이스 범위.

---

## 11. 검증 게이트

### C0 — 정본 일치

- PROJECT_CORE, 분야별 승인 계약, 결정 원장, GDD Sheet, pending와 구현 상태가 같은 목표를 말한다.
- 같은 결정 ID의 의미·상태·경로가 GitHub와 Sheet에서 일치한다.
- 기존 구현 증거와 최신 설계 미구현 상태를 섞지 않는다.

### C1 — 물리 룰렛·토큰 생명주기

- TokenSource 결속 슬롯, X 복원, source lifecycle 멱등성.
- 가로·세로 이동과 immutable snapshot.
- 중앙 판정, 완성선, 등급과 금화 resolver.

### C2 — 결과·보관·배치·미션

- 판매·보관·배치 원자성.
- 식량 반환과 신규 배치 차단.
- 미션 후보 필터, 중복 금지, 공개 보상과 허용 보상 종류.

### C3 — 전장·건설·수리

- 5구간 라인과 점령 경로.
- 30개 노드와 점령 권리.
- 건물 이전·BLOCKED·파괴·철거·업그레이드 거래.
- 피해→파괴→수리 순서와 지갑 하한.

### C4 — 전투 AI·공용 콘텐츠

- 공용 10개 아키타입과 적 전용 데이터 복제 금지.
- 방패병 우선도와 전문 프로필.
- 호위병 분담, 철벽 단계와 재배치 초기화.

### C5 — MapRun·저장·Manifest

- 20 Stage 상태 연속성.
- 8개 일반 공세 템플릿과 4개 위험 패키지 참조 무결성.
- 준비·일반·위험 시간 행렬.
- checkpoint 원자 저장과 schema 오류 처리.
- MapRun당 1회 유료 재시도 상한과 Stage 1~4 차단.
- 동일 RNG 계보 복원, 영구재화 원자 차감, 복원 실패 롤백.
- 개발 재시도의 메타·업적·공식 기록 차단.

### C6 — 분포·사람 플레이

- 100,000 seed 경제·룰렛·판매·비축·수리·미션 보상·재시도 비용 시뮬레이션.
- 1080p·720p 정보 가독성.
- 첫 플레이에서 건설→릴 변화→결과→배치→전선 변화 인과 설명.
- 미션 목표·실패·보상을 선택 전에 이해하고 거절 가능성을 인지.
- 재시도 비용·복원 범위·동일 seed를 선택 전에 이해.
- 벨루 조언이 자동 결정이나 입력 방해를 만들지 않음.

---

## 12. 현재 판정

```text
LATEST_USER_DESIGN_INTEGRATED
+ CONTENT_MANIFEST_APPROVED
+ MISSION_POOL_STRUCTURE_APPROVED
+ DEFEAT_AND_PAID_RETRY_DETAIL_APPROVED
+ BENCHMARK_FIRST_RULE_APPROVED
+ CANON_SYNC_PROTOCOL_APPROVED
+ DOCUMENT_AND_SHEET_SYNC_REQUIRED
+ PRODUCT_CODE_NOT_CHANGED
+ VERTICAL_SLICE_NOT_IMPLEMENTED
+ AUTOMATED_CONTRACTS_NOT_RUN
+ HUMAN_QA_NOT_RUN
+ CORE_LOCK_NOT_ALLOWED
```

다음 기획 게이트는 위험 Stage·보스 상세 편성, 영구재화 명칭·획득량·재시도 비용 시뮬레이션 목표, 저장 schema, UX 정보 예산과 대표 에셋 Manifest다. 제품 구현은 별도 계획 승인 전 시작하지 않는다.
