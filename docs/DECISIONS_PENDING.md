# 오멘워드 미확정 결정 목록

- 갱신일: 2026-08-03
- 현재 main: `RESOLVE_FROM_REPOSITORY_DEFAULT_BRANCH`
- 전체 시스템 정본: `docs/design/APPROVED_VERTICAL_SLICE_SYSTEM_CONTRACT_2026-07-27.md`
- 최신 영웅 정본: `docs/design/APPROVED_OMENWARD_HERO_UNIQUE_SKILL_2_TRIGGER_TARGET_AND_POWER_BUDGET_VALIDATION_2026-08-03.md`
- Harness 상위 정본: `docs/design/APPROVED_OMENWARD_DETERMINISTIC_SIMULATION_HARNESS_SCOPE_2026-08-03.md`
- 최신 검증 정본: `docs/design/APPROVED_OMENWARD_COMMON_COMBAT_SCHEMA_AND_RESOLUTION_ORDER_2026-08-03.md`
- 상태: `PLANNING_ONLY / COMMON_COMBAT_SCHEMA_APPROVED_NOT_IMPLEMENTED / PRODUCT_AND_TOOL_CODE_NOT_AUTHORIZED`
- 원칙: 체크되지 않은 값은 구현 사양이나 밸런스 결론으로 확정하지 않는다.

이미 승인된 구조를 다시 질문하지 않는다. 이 문서는 제품·Harness 구현 전에 실제 schema·수치·fixture·통과선을 고정해야 할 항목만 추적한다.

---

## 1. 해결된 주요 결정

### 1.1 전체 시스템

- [x] 20 Stage 전체 시스템 Vertical Slice.
- [x] 세 원형 릴·금고/병영 TokenSource·immutable SpinSnapshot.
- [x] 상·중·하 3전선과 5구간·30개 건설 노드.
- [x] 금고·농장·타워·병영·지휘소.
- [x] 보관·판매·식량·수리·건설 프로젝트 기본 계약.
- [x] 준비·전투·정산·정비시간과 versioned checkpoint 방향.
- [x] 제품 코드는 별도 승인 전 변경하지 않음.

### 1.2 영웅·전설

- [x] 표준 `[영웅]` = 강화 1스킬 + 표준 2스킬.
- [x] 해금 이름 지정 `[영웅]` = 강화 1스킬 + 고유 2스킬.
- [x] 표준 `[전설]` = 강화 1스킬 + 강화 표준 2스킬 + 표준 3스킬.
- [x] 향후 해금 이름 지정 `[전설]`은 고유 3스킬을 사용하되 상세는 후속 범위.
- [x] `표준 영웅 < 해금 영웅 < 표준 전설` 파워 방향.
- [x] 전장 전체 `[영웅]·[전설]` 활성 유닛 합계 최대 1명.
- [x] 초기 5명: 방패병·궁병·사제·마법사·암살자.
- [x] 고유 2스킬: 불퇴의 성벽·천공 소거·생명의 서약·메테오·그림자 분신.
- [x] 수동 발동·수동 타깃·마나·다중 charge 금지.
- [x] READY 최대 1회, 전투 clock만 timer 진행.
- [x] 공개 Trigger·same-lane Filter·Priority·stable tie-break·immutable commit Snapshot.
- [x] active effect·미해결 commit의 다음 Stage 이월 금지.
- [x] A/B/C 대표 encounter 파워 검증 방향.

### 1.3 Deterministic Simulation Harness 범위

- [x] headless 순수 도메인 fixed-tick Harness를 초기 기준으로 선택.
- [x] versioned fixture·ordered external commands·pure domain state transition.
- [x] named RNG streams와 seed/state/draw count 기록.
- [x] stable object ID·explicit sort key·양자화 위치 경계.
- [x] ordered event log·normalized final state·metrics·fingerprint 출력.
- [x] T0 schema / T1 replay / T2 invariants / T3 paired A/B/C 설계 범위.
- [x] headless 실행은 결정론 자체가 아니라는 경계.
- [x] raw JSON text·variable frame delta·wall clock·global RNG를 결정론 권위에서 제외.
- [x] T4 aggregate balance와 T5 product runtime adapter를 후속 Gate로 분리.

Harness scope 승인은 simulation tool 구현 또는 실행 승인이 아니다.

### 1.4 Common Combat Schema·Resolution Order

- [x] 영웅 우선이 아닌 core-first 공통 Schema.
- [x] `CombatRunState`, `LaneState`, `CombatantState`, `BuildingState`, `ObjectiveState`.
- [x] `DeploymentProvenance`, `OrderedCommand`, `ActionIntent`, `EffectIntent`.
- [x] `StatusInstance`, `PendingCommit`, `ActiveEffect`, `RngStreamState`.
- [x] 전장 유닛의 `SpinSnapshot·TokenSource·lane commit→deployment_id` provenance.
- [x] `TOP=0`, `MID=1`, `BOTTOM=2` canonical lane order.
- [x] 실제 거리 기반 cross-lane 효과를 위한 quantized 2D `position_q`.
- [x] Dictionary·SceneTree traversal을 resolution order 권위에서 제외.
- [x] R00~R130 fixed-tick phase order.
- [x] movement 뒤 same snapshot targeting·action commit.
- [x] 동일 tick damage/effect batch 뒤 death·destruction finalize.
- [x] post-death 생존자만 objective 계산.
- [x] commit 뒤 hidden fallback retarget 금지.
- [x] R120 phase 뒤 canonical fingerprint 생성.
- [x] 영웅·전설은 공통 resolver extension seam만 사용.

Common Schema 승인은 GDScript·fixture·test·simulation 구현 승인이 아니다.

---

## 2. 현재 최우선 — Damage·Protection·Status Semantics

다음 Decision:

`OMW-DEC-20260803-VALIDATION-DAMAGE-PROTECTION-AND-STATUS-SEMANTICS-V1`

### 2.1 피해 분류

- [ ] 기본 공격·스킬·광역·지속·환경·재전달 피해 taxonomy.
- [ ] 물리·마법 또는 대체 damage channel 구조.
- [ ] 절대 피해·처형·최소 피해 지원 여부.
- [ ] friendly fire·self damage·building/objective damage 경계.
- [ ] raw damage와 resolved HP loss의 event 분리.

### 2.2 방어·보호

- [ ] armor·resistance 공식 형태와 상·하한.
- [ ] 피해 감소·barrier·absorption·damage sharing 적용 순서.
- [ ] 방벽 budget과 target별/전체 공유 방식.
- [ ] health-floor가 damage clamp인지 status인지.
- [ ] 보호 효과 중첩·동일 category 우선순위.

### 2.3 회복·상태·죽음

- [ ] restore/heal과 health-floor의 구분.
- [ ] overheal·revive 지원 여부와 금지 기본값.
- [ ] buff·debuff·crowd-control·immunity taxonomy.
- [ ] status stacking·refresh·replace·exclusive group.
- [ ] start/end tick exclusive semantics와 dispel/cleanup.
- [ ] post-hit trigger·on-death trigger·owner removal 순서.

### 2.4 전투 대상 범위

- [ ] 유닛·건물·목표의 targetable channel.
- [ ] flying·ground·structure·objective filter.
- [ ] 공격 불가·면역·무효 target event.
- [ ] cross-lane scope와 거리 계산.

---

## 3. 이후 미확정 결정

### 3.1 Common Schema 기술 기본값

- [ ] fixed tick duration과 시간 단위.
- [ ] spawn `activation_tick` 즉시/다음 tick 정책.
- [ ] movement speed·range·position quantization scale.
- [ ] enum versioning과 unknown value 안전 처리.
- [ ] canonical serialization field order.
- [ ] fingerprint algorithm.
- [ ] reference engine build·reference CI environment.
- [ ] full snapshot checkpoint 간격과 event log 보존 정책.
- [ ] save round-trip fixture와 divergent tick 보고 형식.
- [ ] fixture migration·authority commit pinning.
- [ ] holdout fixture 관리와 변경 승인 절차.
- [ ] simulation tool GDScript·test 구현 패키지와 Red tests.

### 3.2 AI·Trigger 공통 의미

- [ ] `role`, `threat`, `frontline`, `backline`, `cluster`, `flying`, `high_value` exact schema.
- [ ] target filter·priority score 세부 계산.
- [ ] trigger 평가 주기와 stability window exact 값.
- [ ] target snapshot과 position snapshot의 효과별 정책.
- [ ] 분신 proxy owner link·독립 AI 금지 직렬화.

### 3.3 영웅 Exact 값

- [ ] 다섯 고유 2스킬 Trigger 임계치.
- [ ] Trigger stability window와 평가 주기.
- [ ] initial warmup과 스킬별 cooldown.
- [ ] 방벽 흡수량·지속시간·전열 압력 공식.
- [ ] 천공 소거 비행 위협도·대상 수·대상별 피해.
- [ ] 생명의 서약 Trigger·유효 하한·지속시간.
- [ ] 메테오 군집 반경·최소 적중 수·낙하 지연·피해·경고시간.
- [ ] 그림자 분신 지속시간·복제 피해율·owner link 세부.

### 3.4 A/B/C Acceptance

- [ ] family별 fixture·seed·난이도·배치 표본 수.
- [ ] B>A 의도 상황 통과선.
- [ ] C>B 전체 대표 family 합산 통과선.
- [ ] 허용오차·신뢰구간·재실행 기준.
- [ ] no-cast·precheck 실패·late commit 취소율 허용 범위.
- [ ] 특정 해금 영웅의 전 encounter 필수 선택화 stop-ship.
- [ ] 다른 두 전선 기여도 하한.
- [ ] placeholder parameter set 결과의 `EXPLORATORY_ONLY` 표시.

### 3.5 룰렛·경제

- [ ] 유료 회전 기본 비용과 Stage별 변화.
- [ ] 무료 회전 금화 보상 기준가.
- [ ] 초기 릴 X·고정 토큰 구성.
- [ ] 이동 기본가격 `P`와 세션 `nP`.
- [ ] 등급별 판매가·보관함 확장 비용과 상한.
- [ ] 금고 Tier·중앙 경합 지역 골드/초.
- [ ] 100,000-seed 목표 기대값·허용 범위.

### 3.6 건물·수리·점령

- [ ] 5개 건물 기본 비용·시간·HP와 Tier 값.
- [ ] 연사/포격 타워와 돌격/수비 지휘소 exact 값.
- [ ] 철거 시간·환불률.
- [ ] 수리 HPS·HP당 비용·자동 재개 UX.
- [ ] 점령 유예·회복속도·반경.
- [ ] 거점·본진 능력치와 실제 node/anchor 배치.

### 3.7 병종·전투 콘텐츠

- [ ] 전체 10병종 표준 능력치.
- [ ] 나머지 Tier 3 전문화 능력.
- [ ] 일반~전설 스킬 강화 exact 값.
- [ ] 비행 충돌·고도·수평거리 규칙.
- [ ] 타워와 유닛 target score 통합.
- [ ] 20 Stage 적 구성·보스·미션·난이도·세션 길이.

### 3.8 저장·메타·UX

- [ ] save schema version·migration·checksum·atomic replace·backup.
- [ ] checkpoint 직렬화 field와 중간 사건 ID.
- [ ] timer·READY·RNG·commit·resolved 상태 저장.
- [ ] 메타 재화·영구 성장·respec·반복 clear 점감.
- [ ] 영웅 상태 HUD와 paused/waiting/cancel 이유 표시.
- [ ] provenance 기반 결과 복기 UX.
- [ ] 1920×1080·1280×720 가독성.

---

## 4. 검증 전 보류

- [ ] 금화 TokenSource 포함 100,000-seed 경제 분포.
- [ ] 금고 회수기간·무한 증식 여부.
- [ ] 다중 수리 골드 압박.
- [ ] 타워·지휘소가 유닛 조합을 대체하는지.
- [ ] 20 Stage checkpoint 왕복·손상 복구.
- [ ] 표준 영웅·해금 영웅·표준 전설 A/B/C 결과.
- [ ] 방벽 상시 유지, 비행 공세 삭제, 서약 광역 무적 체감.
- [ ] 메테오 회피 불가·전설 초과, 분신 독립 AI 확장.
- [ ] 다른 두 전선 운영의 결정성.
- [ ] Harness와 실제 Scene 결과 분기.
- [ ] reference CI replay bit parity.

---

## 5. Legacy evidence로만 남는 값

현재 정본이 아님:

- 독립 9칸 가중 추첨.
- `capture_power` 합산.
- 구형 중간거점 상태기와 10초+10초 점령.
- 작업자 임금·글로벌 수리 예산.
- 파괴 건물 재건.
- 3 Stage 최소 Slice.
- 스테이지당 전설 1회.
- 이름 지정 영웅만 1명 제한.
- 해금 영웅 패시브/active 선택과 3번째 추가 스킬.
- 강제 상쇄 sidegrade.
- 공개 12% 럭키와 이동 되돌리기.

---

## 6. 현재 우선순위

```text
P0 = deterministic Harness 범위·입출력·재현성 — APPROVED_CONCEPT / NOT_IMPLEMENTED
P1 = common combat schema·resolution order — APPROVED_CONCEPT / NOT_IMPLEMENTED
P2 = damage·protection·status semantics — CURRENT_NEXT_GATE
P3 = 다섯 해금 영웅 exact Trigger·timer·효과값
P4 = A/B/C sample·tolerance·stop-ship
P5 = roulette/economy 100,000-seed simulation
P6 = checkpoint/save schema
P7 = Harness 및 첫 제품 구현 패키지·Red tests·회귀·롤백
```

제품 코드·simulation tool 코드·Scene·Resource·test 변경은 별도 사용자 승인 전 금지한다.
