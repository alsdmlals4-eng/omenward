# 오멘워드 버티컬 슬라이스 위험 Stage·보스 행동 패키지 계약

- 결정 ID: `OMW-DEC-20260731-DANGER-BOSS-V1`
- 승인일: `2026-07-31`
- 상태: `USER_APPROVED_PLAN / EXACT_VALUES_PENDING`
- Work Mode: `PLAN / PLANNING_ONLY_PROFILE`
- 제품 구현 권한: `NONE`
- 선행 벤치마킹: `docs/benchmarks/OMENWARD_DANGER_STAGE_AND_BOSS_PACKAGE_BENCHMARK_2026-07-31.md`
- 역사 제안: `docs/design/proposals/2026-07-31-danger-stage-and-boss-package-proposal.md`

이 계약은 Stage 5·10·15·20의 역할, 공개 정보, 보스 아키타입과 행동 패키지 구조를 확정한다. 정확한 수량·Threat·HP·행동 간격·페이즈 임계점은 후속 시뮬레이션과 사람 플레이 승인 전까지 정본 수치가 아니다.

---

## 1. 공통 위험 Stage 계약

1. Stage 5·10·15는 4개 예약 공세 구간을 사용한다.
2. Stage 20은 5개 예약 공세 구간을 사용한다.
3. 모든 공세 구성·라인·수량·치명적 특수 행동은 준비 단계에서 공개한다.
4. 전투 HUD는 현재 위협과 다음 위협을 우선 표시한다.
5. 위험 Stage는 전술계획 정지를 허용하지 않는다.
6. 위험 Stage에서 새 핵심 시스템 튜토리얼을 추가하지 않는다.
7. 한 시점 핵심 위협 축은 최대 2개다.
8. 플레이어에게 동시에 요구하는 실시간 필수 조작 종류는 최대 2개다.
9. 주력 라인과 모든 예약 출격은 준비 checkpoint 생성 전에 확정한다.
10. 유료 재시도 시 주력 라인·공세·보스 행동·룰렛·미션의 동일 RNG 계보를 복원한다.
11. 일반 적은 공용 10개 아키타입을 사용한다.
12. 보스는 `공용 base_archetype_id + Rank + BossBehaviorPackage + BossPhaseProfile + 전용 Visual Set`으로 구성한다.
13. 일반 적 전용 능력치·스킬·AI 복사본을 만들지 않는다.
14. 숨은 증원, 숨은 승리 조건, 예고 없는 즉시 건물 삭제를 사용하지 않는다.

### 준비 화면 필수 정보

```text
주력 라인
보조 라인
구간별 출격 역할·수량·시각
치명적 특수 행동
보스 행동 패키지
관찰 가능한 위험 태그
```

### 전투 HUD 필수 정보

```text
현재 위협
다음 위협
행동 대상 라인
전조 남은 시간
보스 phase·공개 중첩
보관 병력·사용 가능한 실시간 명령
```

### 패배 귀인

패배 화면은 최대 세 개 원인을 표시한다.

1. 놓친 공개 위협.
2. 그 위협이 만든 직접 결과.
3. 재시도에서 바꿀 수 있는 준비 선택.

벨루는 정답을 강요하지 않고 관찰 가능한 인과만 설명한다.

---

## 2. Stage 5 — 첫 무정지 두 전선 시험

```yaml
danger_package_id: DNG-05-DUAL-LANE-EXECUTION
boss: none
primary_test: dual_lane_real_time_priority
target_duration: 90_to_120_seconds
new_tutorial: none
```

### 역할

Stage 1~4에서 학습한 징조·병영·룰렛·보관·배치·타워를 무정지 상태에서 연결하는 첫 통합 시험이다.

### 허용 병종

- 공통 보병.
- 방패병 또는 대검전사 중 하나.
- 궁병.

비행·암살·지원·공성은 사용하지 않는다.

### 4구간 구조

| 구간 | 주력 라인 | 보조 라인 | 시험 목적 |
|---|---|---|---|
| A | 보병 전열 | 없음 또는 비치명적 정찰 | 준비 선택 확인 |
| B | 전열 지속 | 궁병 견제 시작 | 두 위협 판독 |
| C | 엘리트 전열 1개체와 호위 | 궁병 증원 | 보관 병력 사용 압박 |
| D | 잔존 주력 재압박 | 보조 라인 마감 공세 | 우선순위 최종 확인 |

세 번째 라인은 안전하거나 비치명적 소수만 사용한다.

### 필수 실시간 조작

1. 보관 병력 추가 배치.
2. 타워 건설 또는 사전 시작한 건설 완료 확인.

수리·미션·보스 전용 버튼은 요구하지 않는다.

---

## 3. Stage 10 — 영웅급 지휘망 해체

```yaml
danger_package_id: DNG-10-COMMAND-NETWORK
boss_package_id: BSP-10-VEIL-HERALD
working_name: 베일 선도자
base_archetype_id: priest
rank: HEROIC
primary_test: command_network_dismantling
target_duration: 90_to_120_seconds
```

공용 사제 아키타입에 영웅 Rank와 지휘 행동 패키지를 결합한다.

### 행동 1 — 집결 명령

- 같은 라인의 공개된 호위 그룹을 강화한다.
- 대상 그룹과 발동 시각을 사전 공개한다.
- 제어·피격 경직으로 지연될 수 있으나 완전 취소 규칙은 후속 수치 검증 대상이다.

### 행동 2 — 전선 호명

- 준비 단계에서 지정한 보조 라인의 다음 예약 공세를 강화한다.
- 대상 라인은 전투 도중 변경하지 않는다.
- 숨은 병력을 생성하지 않고 공개된 예약 출격의 Rank 또는 간격만 조정한다.

### 행동 3 — 보호 대형

- 방패 호위가 살아 있는 동안 후열 위치를 유지하고 기본 표적 우선도를 낮춘다.
- 무적과 강제 타깃 해제는 사용하지 않는다.

### 대응 경로

- 이미 공개된 암살자·기병으로 지휘 적에 접근한다.
- 방패 호위를 먼저 파쇄한 뒤 원거리·마법·타워로 집중한다.
- 보조 라인은 타워와 소수 방어로 유지하고 주력 라인에 화력을 집중한다.

처치 순서 하나만 정답인 퍼즐로 만들지 않는다.

---

## 4. Stage 15 — 전설급 공성 돌파 보스

```yaml
danger_package_id: DNG-15-SIEGE-BREAKTHROUGH
boss_package_id: BSP-15-BOUNDARY-BREAKER
working_name: 경계파쇄자
base_archetype_id: giant
rank: LEGENDARY
primary_test: siege_breakthrough_and_density_control
target_duration: 90_to_120_seconds
```

공용 거인 아키타입에 전설 행동 패키지와 전용 Visual Set을 결합한다.

### 행동 1 — 파성 돌진

- 주력 라인의 다음 거점·건물 방향으로 긴 전조 후 돌진한다.
- 경로와 예상 충돌 대상을 표시한다.
- 종료 후 공개된 회복 창을 제공한다.
- 대형 저지와 제어가 거리·회복 창에 미치는 정확한 효과는 후속 수치 대상이다.

### 행동 2 — 대단절

- 현재 전열 주변 넓은 범위를 공격한다.
- 범위와 실행 시각을 표시한다.
- 밀집된 저내구 병력을 처벌하되 방패·거인·원거리 구성 등 복수 대응을 허용한다.

### 행동 3 — 진군 중첩

- 건물 또는 거점에 유효 피해를 줄 때 공개 중첩을 얻는다.
- 이동과 구조물 압박을 강화한다.
- 상한과 효과량은 후속 수치 대상이다.

### 전설 페이즈

공개 HP 임계점에서 새 규칙을 추가하지 않고 기존 행동의 우선순위와 간격만 강화한다.

### 대응 경로

- 창병·거인·방패 지연 전열과 원거리 화력으로 회복 창을 활용한다.
- 보조 라인은 타워로 유지하고 주력 화력을 집중한다.
- 일부 전진 거점·건물 손실을 감수하고 보관 병력을 본진 전 방어선에 추가 배치할 수 있다.

배치 완료 병력의 라인 이동·회수는 허용하지 않는다.

---

## 5. Stage 20 — 신화급 전체 인과 회수

```yaml
danger_package_id: DNG-20-FINAL-COMMAND
boss_package_id: BSP-20-MYTHIC-BOUNDARY-BREAKER
working_name: 절멸체 경계파쇄자
base_archetype_id: giant
rank: MYTHIC
primary_test: full_build_and_final_commit
target_duration: 150_to_210_seconds
```

Stage 10의 지휘 압박과 Stage 15의 공성 압박을 재조합한다. Stage 20에서 처음 보는 핵심 하위 시스템을 추가하지 않는다.

### Phase 1 — 전선 시험

- 공개된 주력 라인으로 보스가 출격한다.
- 나머지 두 라인은 서로 다른 시각에 호위 공세를 받는다.
- 파성 돌진과 대단절을 재사용한다.

### Phase 2 — 구조 시험

- 공개 임계점에서 진군 중첩과 구조물 우선 행동을 강화한다.
- 보조 라인에는 공성 또는 후열 압박 중 하나만 추가한다.
- Stage 10의 전선 호명 원리를 재사용해 강화 라인을 사전 공개한다.

### Phase 3 — 최종 커밋 시험

- 마지막 예약 공세의 전체 구성과 출격 시각을 진입 전에 공개한다.
- 미공개 추가 증원은 없다.
- 보스는 방어 안정성을 일부 잃고 공격 간격이 짧아진다.
- 플레이어는 남은 보관 병력·골드·수리·무료 회전 결과를 어느 전선에 커밋할지 결정한다.
- 보스와 예약된 치명적 호위를 제거하고 본진이 생존해야 승리한다.

### 최종전 금지 규칙

- 보스 라인 순간이동.
- 예약되지 않은 무한 증원.
- 무조건 제어 면역.
- 기존 규칙을 무효화하는 Phase 전환.
- 숨은 건물 삭제 또는 숨은 승리 조건.

---

## 6. 데이터 계약

```text
DangerStagePackage
- danger_package_id
- stage_id
- primary_test_id
- primary_lane_id
- secondary_lane_ids[]
- assault_segment_ids[]
- boss_package_id?
- concurrent_threat_axis_limit = 2
- real_time_operation_type_limit = 2
- telegraph_profile_id
- failure_attribution_profile_id
- checkpoint_restore_policy_id
```

```text
BossBehaviorPackage
- package_id
- base_archetype_id
- allowed_rank
- action_ids[]
- phase_profile_id
- target_priority_override_id?
- control_resistance_profile_id
- structure_pressure_profile_id?
- telegraph_profile_id
- failure_attribution_tags[]
```

```text
BossPhaseProfile
- phase_id
- entry_condition
- enabled_action_ids[]
- action_interval_profile
- spawn_schedule_modifier_id?
- target_priority_modifier_id?
- presentation_event_id
```

보스 패키지는 공용 아키타입의 HP·공격력·스킬 전체 복사본을 저장하지 않는다. 보스 배율과 특수 행동은 독립 modifier·action 참조로 관리한다.

---

## 7. 검증 계약

### 자동 검증

- 위험 Stage의 전술계획 정지 진입 0회.
- 위험 Stage 신규 튜토리얼 이벤트 0개.
- 동시 핵심 위협 축 최대 2.
- 제품 실시간 필수 조작 종류 최대 2.
- 모든 치명적 행동에 유효한 telegraph event 존재.
- 일반 적은 공용 10개 archetype ID만 참조.
- 보스 패키지는 공용 아키타입 원본을 변경하지 않음.
- 재시도 전후 주력 라인·spawn schedule·boss phase seed 일치.
- 숨은 증원·숨은 승리 조건 0.
- Stage 5 보스 참조 없음.
- Stage 20 예약되지 않은 무한 증원 없음.

### 사람 플레이 검증

- 시작 전에 주력·보조 라인과 핵심 위험을 설명할 수 있음.
- 패배 후 놓친 공개 위협을 한 문장으로 설명할 수 있음.
- Stage 5·10·15·20의 판단 차이를 구분할 수 있음.
- 대응 방법이 하나뿐이라고 느끼지 않음.
- 1280×720에서 현재 행동·다음 공세·라인 정보가 겹치지 않음.
- 보스가 HP 증가만으로 길어진다고 느끼지 않음.

---

## 8. 미확정 수치

- 각 구간의 정확한 archetype·Tier·Rank·count.
- 출격 시각과 구간 간격.
- Stage 10 지휘 버프 수치·범위·간격.
- Stage 15 돌진 거리·회복 창·대단절 범위·진군 상한.
- Stage 20 Phase 임계점·최종 상태 배율.
- 각 Stage Threat 예산.
- 건강한 빌드 제거율·본진 HP 잔존 목표.
- 난이도별 변형 규칙.

이 값은 병종·건물·경제 기준값, 100,000-seed 시뮬레이션과 사람 플레이 전에는 구현 수치로 확정하지 않는다.

---

## 9. 상태 경계

```text
USER_APPROVED_PLAN
!= EXACT_STAGE_VALUES_APPROVED
!= BOSS_BALANCE_PROVEN
!= HUMAN_PLAYTEST_PASSED
!= PRODUCT_CODE_AUTHORIZED
```
