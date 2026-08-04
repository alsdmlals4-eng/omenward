# [현행] OMENWARD 건물 분기·카운터·포기 비용 적대적 검토

```yaml
review_id: OMW-REV-20260805-BUILDING-BRANCH-COUNTER-OPPORTUNITY-COST-V1
decision_id: OMW-DEC-20260805-PLANNING-SIX-BUILDING-T2-T3-BRANCHES-AND-COUNTERS-V1
status: PASS / REQUIRED_CANON_FIXES_APPLIED
review_scope: BUILDING_BRANCHES / COUNTERS / OPPORTUNITY_COST / UX / PROCESS / PR_PREFLIGHT
product_code_authority: NONE
simulation: NOT_RUN
human_validation: NOT_RUN
```

## 1. 결론

`건물 인스턴스별 T1 → 두 T2 중 하나 → 같은 경로 T3` 구조는 오멘워드의 핵심 재미와 맞는다.

```text
예고된 Stage 압력
→ 건물 전문화로 미래 룰렛·전선 대응 설계
→ 다른 강점을 포기하고 한 경로에 커밋
→ 결과를 복기해 다음 건물·병종·전술 설계
```

강점:

- 건물이 단순 수치 생산기가 아니라 다음 Stage를 준비하는 선택이 된다.
- 두 경로와 포기 비용을 플레이어에게 명시한다.
- 동일 건물 여러 인스턴스로 서로 다른 전략을 구성할 수 있다.
- 건물만으로 모든 압력을 해결하지 않고 병종·전술 결정에 의존한다.
- T3가 룰렛 자산 규칙과 비가역 전선 원칙을 침범하지 않는다.

현재 한계:

- 병종 역할과 전술스킬이 미확정이므로 `FLYING`, `ARMORED`, `SIEGE` 대응은 아직 완결되지 않았다.
- 정확한 비용·배율·한도·쿨다운·범위는 시뮬레이션 전 확정할 수 없다.
- 첫 5 Stage에서 선택이 실제로 강제되지 않는지는 사람 플레이 검증이 필요하다.

```text
CORE_FIT = STRONG
BRANCH_GRAMMAR = COHERENT
OPPORTUNITY_COST = EXPLICIT
PRESSURE_COVERAGE = STRUCTURALLY_VIABLE_WITH_DEPENDENCIES
DOCUMENT_PR_MERGE_READINESS = PASS
PRODUCT_CODE = UNCHANGED
IMPLEMENTATION_READINESS = BLOCKED_BY_TROOP_AND_TACTICAL_DECISIONS
```

## 2. P0 정본·핵심 재미 공격

### OMW-AUD-398 — 분기 선택 범위 모호성

- 위험: 한 건물 선택이 같은 종류 전체를 잠그거나 한 인스턴스에서 양쪽 경로를 얻을 수 있다.
- 조치: 선택은 건물 인스턴스별이다. 같은 인스턴스의 `CROSS_BRANCH`와 `DUAL_T3`는 금지하고 다른 인스턴스는 다른 경로를 선택할 수 있다.

### OMW-AUD-399 — 철거·재건 무료 재전문화

- 위험: Stage 예고 뒤 저비용 철거·재건으로 카운터를 무제한 교체하면 전문화 커밋이 사라진다.
- 조치: 철거는 인스턴스와 효과를 제거한다. 재건은 새 선택이지만 환불·재건 비용·정비시간 제약은 경제 Decision에서 악용 불가능하게 설계한다.
- 잔여 상태: 경제 Gate 의존.

### OMW-AUD-400 — DOMINANT_BRANCH_RISK

- 공격: 한 분기가 자원·화력·안정성을 동시에 제공하면 다른 분기는 장식이 된다.
- 조치: 모든 분기에 얻는 것과 포기하는 것을 함께 명시하고 서로 다른 압력·운영 시점에서 강점이 나타나게 한다.
- 재검증: 압력 구성과 무관하게 한 분기 선택률이 지속적으로 압도하면 비용·등장 시점·효과를 재설계한다.

### OMW-AUD-401 — FALSE_CHOICE_RISK

- 공격: 이름만 다르고 실제 결과가 같은 수치 선택이 될 수 있다.
- 조치: T3는 결과 곡선, 표적 우선순위, 전선 교리, Route 대응 또는 자원 사용 시점 중 하나를 실제로 바꾼다. 순수 수치 증가는 승인 조건을 충족하지 않는다.

### OMW-AUD-402 — 단일 만능 건물

- 위험: 하나의 업그레이드만 반복하면 Stage 예고·룰렛·병종·전술 선택이 무의미해진다.
- 조치: 단일 만능 분기를 금지하고 압력별 대응을 여러 건물·병종·전술에 분산한다.

### OMW-AUD-403 — HIDDEN_COUNTER_CHANGE

- 위험: Stage 중 대상·전선·공격 Layer를 숨겨서 바꾸면 비가역 배치가 함정이 된다.
- 조치: 요격 우선순위, 결전 전선, 후방 우선순위, 마석 Pulse와 예약 상태는 Stage 시작 전에 공개한다.

## 3. P1 구조·복잡성 공격

### OMW-AUD-404 — COMPLEXITY_BUDGET_RISK

- 공격: 6종×2분기×T3를 한 화면에 모두 설명하면 정비시간이 백과사전이 된다.
- 조치: 한 건물에는 T2 카드 두 장만 표시하고 `얻는 것 / 포기하는 것 / 유리한 압력 / 핵심 루프 영향 / T3 예고`만 고정 노출한다.
- 현재 범위에서 추가 예외 분기와 교차 전문화는 폐기한다.

### OMW-AUD-405 — 첫 5 Stage 강제 정답

- 공격: 압력 학습 순서 때문에 특정 초기 건물이 자동 정답이 될 수 있다.
- 조치: 기본 병종·전선 배치·룰렛 준비를 포함해 최소 두 대응 경로를 제공한다. 가격·해금 시점은 첫 10~15분 Decision과 시뮬레이션에서 검증한다.

### OMW-AUD-406 — PRESSURE_COVERAGE_GAP

- 가장 큰 공백: `FLYING`은 건물만으로 실제 카운터가 완성되지 않는다.
- 조치: 기동 병영과 명시적 대공 요격 포대는 준비 경로만 정의한다. 실제 대공 병종·전술이 4/10·5/10에서 승인되기 전 구현 준비 완료로 판정하지 않는다.

### OMW-AUD-407 — 다중 인스턴스의 포기 비용 약화

- 공격: 슬롯이 충분하면 A/B를 모두 세워 사실상 모든 장점을 얻을 수 있다.
- 판정: 다중 인스턴스 자체는 허용한다. 건설 슬롯·골드·업그레이드 시간·다른 건물 기회비용이 실제 제한이어야 한다.
- 잔여 상태: 경제·맵 시뮬레이션 의존.

### OMW-AUD-408 — 기능명이 최종 세계관 명칭으로 고정

- 조치: 현재 이름은 기능 식별용 기획명이다. 최종 명칭은 역할과 포기 비용을 보존한 채 아트·콘텐츠 제작 전 재검토할 수 있다.

## 4. 건물별 악용 공격

### OMW-AUD-409 — 금고 이중 증폭

- 공격: 금화 TokenSource 강화와 완성선 배율을 같은 결과에 중첩해 경제가 폭발할 수 있다.
- 조치: 안정 계열은 바닥값·예산 보호, 행운 계열은 공개 고완성선 상한만 소유한다. 같은 효과의 이중 적용과 Stage 반복 발동을 금지한다.

### OMW-AUD-410 — 비축 예산 오용

- 조치: 비축 예산은 다음 정비시간 건설 목적에 한정한다. 상인 구매·반복 룰렛·이자 생성으로 전환하지 않는다. 정확 범위는 경제 Decision에서 검증한다.

### OMW-AUD-411 — 농장 한도 우회

- 공격: 예비 슬롯을 누적해 하드 캡을 영구 초과할 수 있다.
- 조치: 한 Stage의 제한된 배치 창이며 종료 뒤 정상 한도 계약으로 돌아간다. 기존 병력 제거는 금지하고 신규 배치만 통제한다.

### OMW-AUD-412 — 병영의 병종 정본 선점

- 공격: 전열·기동 분기에서 로스터·Layer·수치까지 정하면 Decision 4/10이 형식화된다.
- 조치: 병영은 TokenSource 역할 범위만 정한다. 병종 가족·시너지·표적·공격 Layer·수치는 병종 정본이 소유한다.

### OMW-AUD-413 — T3 룰렛 토큰 회귀

- 조치: 룰렛은 T2 병종 이미지를 유지한다. T3 효과는 결과 Preview·보관함·배치 설명에서 표현하며 `T3_ROULETTE_TOKEN`은 금지한다.

### OMW-AUD-414 — 숨은 대공 능력

- 조치: 대공 가능 여부는 업그레이드 카드·사거리 표시·시각 장치·실제 공격 Layer가 모두 일치해야 한다.

### OMW-AUD-415 — 전 Route 자동 요격

- 공격: 누수·비행·침투를 동시에 최우선 처리하면 만능 방어탑이 된다.
- 조치: Stage 시작 전에 요격 교리 하나만 선택하고 사거리·Route 제한을 유지한다.

### OMW-AUD-416 — 지휘소 무한 중첩

- 조치: 같은 계열은 활성 건물 중 최고 Tier 하나만 적용한다. 돌격·수비는 별도 인스턴스로 공존할 수 있으나 슬롯·경제 기회비용을 부담한다.

### OMW-AUD-417 — 결전 전선 과잉 처벌

- 조치: 결전 전선은 집중 강점을 주지만 다른 전선에 전역 페널티를 부과하지 않는다. 지정은 Stage 시작 전에 공개하고 중간 변경을 금지한다.

### OMW-AUD-418 — 마석 자동화·무한 축적

- 공격: 자동 전술 사용, 무제한 저장, 예약 마석 이중 사용이 생길 수 있다.
- 조치: 마력탑은 수급 시점과 저장 한도만 바꾸며 스킬을 자동 사용하지 않는다. 예약 자원은 잠긴 동안 일반 Wave에서 소비할 수 없다.

### OMW-AUD-419 — 수치·제품 구현 조기 확정

- 공격: 역할 문서를 실제 배율·범위·쿨다운·환불값으로 오해해 바로 구현할 수 있다.
- 조치: 모든 정확 수치는 `PENDING_SIMULATION`. 제품 코드는 병종·전술 Decision, 압력 대응 재검증, 별도 구현 계획과 Red 테스트 승인 뒤에만 시작한다.

## 5. 벤치마킹 적합성

### 채택

- 전문화가 즉시 읽히는 소수 분기.
- 선택한 강점과 포기한 대안의 동시 표시.
- 모든 건물에 같은 2갈래 문법을 적용해 비교 비용 제한.
- T1 실루엣을 유지한 단계적 외형 변화.

### 비채택

- 같은 종류 모든 건물을 잠그는 전역 단일 선택.
- 건물마다 별도 재화·메뉴·미니게임을 추가하는 방식.
- 유명 게임의 수치·타워 경로·Landmark 구조를 그대로 복제하는 방식.

## 6. PR 검수 결과

- [x] 설계 Spec·현재 책임 원본·운영 정책·적대적 검토 연결.
- [x] 중앙 라우터가 같은 Decision ID와 `3_OF_10` 사용.
- [x] Google Sheet가 같은 Decision ID·exact HEAD·감사 `398~419` 기록.
- [x] RED run 888의 예상 실패와 GREEN 문서 검증 확인.
- [x] 제품 코드·Scene·Resource·게임 데이터 변경 0.
- [x] 리뷰 0·미해결 Thread 0.
- [x] Sheet `OPEN_P0 / OPEN_P1 / MERGE_BLOCKER` 0.
- [x] 문서 수명주기와 구형 규칙 금지선 연결.

검수 시점 Green 증거:

```text
Validate Project Core Documentation = PASS
Validate Omenward GDD Sheet Adoption = PASS
Validate Omenward Core = PASS
Validate Base v9 adoption = PASS
```

최종 PR head에서도 같은 검증을 다시 실행한다.

## 7. 다음 Gate

```text
OMW-DEC-20260805-PLANNING-TROOP-ROLES-SYNERGIES-AND-COUNTERS-V1
→ OMW-DEC-20260805-PLANNING-TACTICAL-SKILLS-AND-MANA-STONE-V1
→ 건물·병종·전술 압력 대응 재검증
```

Hero·Meta·제품 구현은 위 기본 Run 콘텐츠가 연결되기 전 재개하지 않는다.
