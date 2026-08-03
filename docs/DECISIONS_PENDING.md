# 오멘워드 미확정 결정 목록

- 갱신일: 2026-08-03
- 현재 main: `RESOLVE_FROM_REPOSITORY_DEFAULT_BRANCH`
- 전체 시스템 정본: `docs/design/APPROVED_VERTICAL_SLICE_SYSTEM_CONTRACT_2026-07-27.md`
- Harness 정본: `docs/design/APPROVED_OMENWARD_DETERMINISTIC_SIMULATION_HARNESS_SCOPE_2026-08-03.md`
- 공통 전투 정본: `docs/design/APPROVED_OMENWARD_COMMON_COMBAT_SCHEMA_AND_RESOLUTION_ORDER_2026-08-03.md`
- 피해 의미 정본: `docs/design/APPROVED_OMENWARD_DAMAGE_PROTECTION_AND_STATUS_SEMANTICS_2026-08-03.md`
- 수치 기본값 정본: `docs/design/APPROVED_OMENWARD_MITIGATION_FORMULA_AND_PROTECTION_NUMERIC_DEFAULTS_2026-08-03.md`
- 상태: `PLANNING_ONLY / NUMERIC_DEFAULTS_APPROVED_NOT_IMPLEMENTED / PRODUCT_AND_TOOL_CODE_NOT_AUTHORIZED`
- 원칙: 체크되지 않은 값은 구현 사양이나 밸런스 결론으로 간주하지 않는다.

이미 승인된 구조와 수치를 다시 질문하지 않는다. 이 문서는 제품·Harness 구현 전에 남은 시간축·modifier·콘텐츠 값·통과선을 추적한다.

---

## 1. 해결된 주요 결정

### 1.1 제품·Vertical Slice

- [x] 20 Stage 전체 시스템 Vertical Slice.
- [x] 세 원형 릴·TokenSource·immutable SpinSnapshot.
- [x] 상·중·하 3전선·5구간·30개 건설 노드.
- [x] 금고·농장·타워·병영·지휘소.
- [x] 준비·전투·정산·정비시간과 checkpoint 방향.
- [x] 제품 코드는 별도 승인 전 변경하지 않음.

### 1.2 영웅·전설

- [x] 표준 영웅·해금 이름 지정 영웅·표준 전설의 스킬 계층.
- [x] `표준 영웅 < 해금 영웅 < 표준 전설` 파워 방향.
- [x] 전장 전체 영웅·전설 활성 합계 최대 1명.
- [x] 초기 5명과 고유 2스킬 개념.
- [x] 수동 발동·수동 타깃·마나·다중 charge 금지.
- [x] 공개 Trigger·same-lane Filter·Priority·stable tie-break·immutable commit.
- [x] active effect·미해결 commit의 Stage 이월 금지.
- [x] A/B/C 대표 encounter 검증 방향.

### 1.3 Deterministic Harness

- [x] headless pure-domain fixed-tick Harness 범위.
- [x] versioned fixture·ordered commands·named RNG·stable IDs.
- [x] ordered event·normalized state·metrics·fingerprint.
- [x] T0 schema / T1 replay / T2 invariants / T3 paired A/B/C.
- [x] headless·engine callback 자체는 결정론 보장이 아님.
- [x] T4 aggregate balance와 T5 product adapter를 후속 Gate로 분리.

### 1.4 Common Combat Schema

- [x] core-first 공통 Schema.
- [x] CombatRun/Lane/Combatant/Building/Objective.
- [x] DeploymentProvenance·OrderedCommand·Intent·Status·Effect.
- [x] quantized 2D 위치와 canonical ordering.
- [x] R00~R130 fixed phase order.
- [x] same snapshot commit·damage batch 뒤 death finalize.
- [x] post-death survivor objective.
- [x] hidden fallback retarget 금지.
- [x] 영웅·전설 공통 resolver extension seam.

### 1.5 Damage·Protection·Status Semantics

- [x] `KINETIC→ARMOR`, `ARCANE→RESISTANCE`.
- [x] channel·delivery tag·target profile 분리.
- [x] Damage/Restore/Protection/Status Intent 분리.
- [x] R80A~R80G 의미 barrier.
- [x] Barrier·HP-loss redirection·Health Floor 의미.
- [x] Restore는 negative damage가 아님.
- [x] Status family·stacking policy·expiry·dispel 의미.
- [x] true damage·execute·revive 현 Slice 금지.
- [x] Objective HP damage 기본 금지.

### 1.6 Mitigation·Protection Numeric Defaults

- [x] Armor·Resistance 공통 쌍곡선 공식.
- [x] effective defense `0~300` clamp.
- [x] 양수 정수 half-up 반올림.
- [x] 양수 유효 피해 최소 1.
- [x] Barrier per-application 20%·total 30%·3000ms.
- [x] Barrier excess 폐기·canonical consume order.
- [x] HP-loss redirection 30%·recipient 최대 1·무효 시 원대상 반환.
- [x] Health Floor 1 HP·instance당 1회·exclusive group.
- [x] `ADD_STACKS_CAPPED` 기본 cap 3.
- [x] DOT/HOT pulse 1000ms.
- [x] Control 단일 지속 최대 2000ms.
- [x] 동일 control group lockout 1000ms.
- [x] Barrier 조기 guard: uptime 40% 또는 흡수비 35% 초과.

Numeric Defaults 승인은 제품·Simulation tool 구현 또는 simulation 실행 승인이 아니다.

---

## 2. 현재 최우선 — Fixed Tick·Time·Activation Defaults

다음 Decision:

`OMW-DEC-20260803-VALIDATION-FIXED-TICK-TIME-AND-ACTIVATION-DEFAULTS-V1`

### 2.1 Fixed Tick

- [ ] reference tick rate와 tick duration.
- [ ] integer tick·milliseconds의 권위 관계.
- [ ] 3000/1000/2000/1000ms의 tick 변환 방식.
- [ ] half-tick·비정수 duration의 rounding 정책.
- [ ] simulation·runtime reference clock 일치 조건.

### 2.2 Spawn·Activation

- [ ] 배치·spawn의 `activation_tick` 즉시/다음 tick 정책.
- [ ] spawn 당일 movement·target·action 허용 범위.
- [ ] same-tick ProtectionIntent materialize 조건.
- [ ] 늦은 commit·Stage 종료 경계.
- [ ] timer가 maintenance에서 pause되는 정확 의미.

### 2.3 Timer·Pulse

- [ ] cooldown·warmup·duration·pulse의 `[start_tick,end_tick_exclusive)` 변환.
- [ ] DOT/HOT 첫 pulse와 마지막 pulse 경계.
- [ ] Control 종료와 1000ms lockout 시작 tick.
- [ ] Barrier expiry와 같은 tick damage의 선후.
- [ ] save/checkpoint 시 timer 잔여값 직렬화 단위.

---

## 3. 이후 미확정 결정

### 3.1 Modifier·Defense 확장

- [ ] source outgoing·target incoming modifier stacking.
- [ ] vulnerability·damage reduction category 우선순위.
- [ ] modifier cap·rounding 횟수.
- [ ] Armor/Resistance 감소·관통 지원 여부.
- [ ] immunity filter exact schema.
- [ ] critical·lifesteal·overheal conversion 지원 여부.

### 3.2 Common Schema 기술 기본값

- [ ] movement speed·range·position quantization scale.
- [ ] enum versioning과 unknown value 안전 처리.
- [ ] canonical serialization field order.
- [ ] fingerprint algorithm.
- [ ] reference engine build·reference CI environment.
- [ ] full snapshot checkpoint 간격·event log 보존.
- [ ] save round-trip·divergent tick 보고.
- [ ] fixture migration·authority commit pinning.
- [ ] holdout fixture 변경 승인.
- [ ] simulation tool GDScript·test 구현 패키지와 Red tests.

### 3.3 AI·Trigger 의미

- [ ] role·threat·frontline·backline·cluster·flying·high_value exact schema.
- [ ] target filter·priority score 계산.
- [ ] trigger 평가 주기·stability window.
- [ ] target snapshot·position snapshot 효과별 정책.
- [ ] 분신 proxy owner link·직렬화.

### 3.4 영웅 Exact 값

- [ ] 다섯 고유 2스킬 Trigger 임계치.
- [ ] initial warmup·cooldown.
- [ ] 방벽 budget·지속·전열 압력 공식.
- [ ] 천공 소거 대상·피해.
- [ ] 생명의 서약 Trigger·Floor·지속.
- [ ] 메테오 반경·지연·피해·경고.
- [ ] 그림자 분신 지속·복제율·owner link.

### 3.5 A/B/C Acceptance

- [ ] family별 fixture·seed·표본 수.
- [ ] B>A 의도 상황 통과선.
- [ ] C>B 대표 family 합산 통과선.
- [ ] 허용오차·신뢰구간·재실행 기준.
- [ ] no-cast·precheck 실패·late commit 취소율.
- [ ] 전 encounter 필수 선택화 stop-ship.
- [ ] 다른 두 전선 기여도 하한.
- [ ] Barrier overcentralization guard의 최종 판정법.

### 3.6 룰렛·경제

- [ ] 회전 비용·무료 회전 보상·초기 릴 구성.
- [ ] 이동 가격·판매가·보관함 비용.
- [ ] 금고 Tier·중앙 경합 수입.
- [ ] 100,000-seed 목표 기대값·허용 범위.

### 3.7 건물·수리·점령

- [ ] 5개 건물 비용·시간·HP·Tier.
- [ ] 타워·지휘소 분기 exact 값.
- [ ] 철거 시간·환불률.
- [ ] 수리 HPS·비용·자동 재개 UX.
- [ ] 점령 유예·회복속도·반경.
- [ ] 거점·본진 능력치와 node 배치.

### 3.8 병종·전투 콘텐츠

- [ ] 10병종 능력치.
- [ ] Tier 3 전문화.
- [ ] 등급별 스킬 강화 exact 값.
- [ ] 비행 충돌·고도·수평거리.
- [ ] 타워·유닛 target score.
- [ ] 20 Stage 적·보스·미션·난이도·세션 길이.

### 3.9 저장·메타·UX

- [ ] save schema·migration·checksum·atomic replace·backup.
- [ ] checkpoint field·RNG·timer·commit 상태.
- [ ] 메타 재화·영구 성장·respec·점감.
- [ ] 영웅 상태 HUD·cancel 이유.
- [ ] provenance 기반 결과 복기 UX.
- [ ] 1920×1080·1280×720 가독성.

---

## 4. 검증 전 보류

- [ ] 100,000-seed 경제 분포.
- [ ] 금고 회수기간·무한 증식.
- [ ] 다중 수리 골드 압박.
- [ ] 타워·지휘소의 유닛 대체 여부.
- [ ] 20 Stage checkpoint 왕복·손상 복구.
- [ ] A/B/C 결과와 신뢰구간.
- [ ] Barrier uptime 40%·흡수비 35% guard.
- [ ] 방벽 상시 유지·비행 공세 삭제·서약 과보호.
- [ ] 메테오 회피 불가·전설 초과·분신 독립 AI.
- [ ] 다른 두 전선 운영의 결정성.
- [ ] Harness와 실제 Scene 결과 분기.
- [ ] reference CI replay parity.

---

## 5. 구현 경계

```text
GRILL_ME_COUNT = 4/10
PRODUCT_CODE = NOT_AUTHORIZED
SIMULATION_TOOL_CODE = NOT_AUTHORIZED
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
NEXT_PREFLIGHT = AT_10_OF_10
```
