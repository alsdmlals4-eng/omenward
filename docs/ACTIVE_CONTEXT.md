# Active Context

```yaml
updated_at: 2026-08-02
project: OMENWARD / 오멘워드
work_mode: TOTAL_PLANNING
current_phase: PR121_TEN_DECISION_ADVERSARIAL_PREFLIGHT
current_recovery_decision: OMW-DEC-20260802-CANON-RECOVERY-V1
current_planning_decision: OMW-DEC-20260802-GAMEPLAY-HERO-ABILITY-ACTIVATION-MODE-V1
current_world_decision: OMW-DEC-20260802-WORLD-VEILSPECIES-PURPOSE-V1
current_meta_decision: OMW-DEC-20260802-GAMEPLAY-HERO-ABILITY-ACTIVATION-MODE-V1
current_operating_decision: OMW-DEC-20260802-GRILL-ME-MERGE-CADENCE-V1
current_branch: main
context_baseline_commit: 12012f88bc1dc1d9aaaa538b578be3893e4b1591
working_branch: gpt/omenward-gameplay-planning-20260802
active_base_version: 9.4.0
current_product: LEGACY_PROTOTYPE
latest_planning: USER_APPROVED / ACTIVE_BRANCH_SYNCED / NOT_IMPLEMENTED
product_code_authority: NONE
codex_execution: BLOCKED
primary_platform: PC
future_platform: MOBILE_CONSIDERATION_ONLY
last_merged_pr: 120
last_main_commit: 12012f88bc1dc1d9aaaa538b578be3893e4b1591
current_grill_me_count: 10
future_merge_cadence: 10
preflight: REQUIRED_IN_PROGRESS
merge_authorization: NOT_GRANTED
runtime_validation: NOT_RUN
human_validation: NOT_RUN
simulation: NOT_RUN
```

`current_branch: main`과 `context_baseline_commit`은 현재 병합 기준선이다. 승인 Decision 작성과 preflight는 `working_branch`의 Draft PR #121에서 진행한다.

## 1. 현재 방향

- 게임플레이·콘텐츠 구조를 세계관 세부보다 우선한다.
- 현재 제품은 Legacy 프로토타입이며 최신 승인 기획은 미구현이다.
- 맵 선택으로 MapRun을 시작하고 RunState만 초기화한다.
- 한 MapRun은 현재 20 Stage 목표이며 각 Stage는 하나 이상의 맵 정의 Wave로 구성된다.
- Stage 정산 뒤 정비시간에서 전투·Wave를 멈추고 미션·선택지를 처리한다.
- 건설·업그레이드·수리, 룰렛, 보관함, 병력 배치는 Stage 전투 중과 정비시간 모두 사용 가능하다.
- 주점은 기존 병종에 연결된 복수 이름 지정 영웅을 결정론적으로 해금해 Profile 명부에 등록한다.
- 이름 지정 영웅은 룰렛이 직접 뽑지 않으며 동병종 `[영웅]` 등급 토큰을 선택적으로 변환한다.
- 세 전선 전체의 active 이름 지정 영웅은 동시에 최대 1명이다.
- 배치한 영웅은 수동 퇴각·교대·판매·재보관·전선 이동을 할 수 없다.
- 살아 있는 영웅은 같은 인스턴스로 Stage·Act·정비시간을 넘어 유지된다.
- 현재 HP·남은 쿨다운·충전·사용 횟수·고유 자원은 Stage 경계를 넘어 유지한다.
- 일시 버프·디버프·타깃·어그로·시전·투사체·장판·일시 소환물은 Stage 정산에서 제거한다.
- 정비시간에는 영웅 HP·쿨다운·충전·고유 자원 clock이 정지한다.
- 영웅 사망은 source token·재화·회수권·부활권·무료 재출전권을 제공하지 않는다.
- 이름 지정 영웅 재출전에는 사망 이후 룰렛에서 새로 확정된 동병종 `[영웅]` 등급 토큰이 필요하다.
- 사망 전 보관 토큰은 원본 영웅 등급 병종으로 사용할 수 있으나 이름 지정 영웅 재출전에는 사용할 수 없다.
- 새 적격 토큰은 최대 HP·준비된 스킬·기본 충전·초기 고유 자원의 완전한 새 인스턴스를 만든다.
- 이름 지정 영웅은 원본 영웅 등급 병종과 유사한 평균 총 전투 예산을 가진 조건부 고점형 전문화 sidegrade다.
- 모든 영웅은 고점 조건·고점 보상·명시적 약점·원본 선택 사유·대응 압력을 가진다.
- 모든 이름 지정 영웅 전투 능력은 공개된 규칙과 고정 우선순위에 따라 자동 발동한다.
- 수동 스킬 버튼·수동 타깃 지정·숨은 명령 큐는 없다.

## 2. 프로젝트 약속

> 공개된 세 전선의 공세를 읽고 건물과 TokenSource로 세 물리 릴의 미래 배열을 설계·영구 편집한 뒤, 얻은 병력을 한 전선에 비가역 커밋하고 결과 원인을 다음 설계에 반영한다.

> **건물로 룰렛을 만들고, 룰렛으로 전선을 지휘한다.**

## 3. MapRun 흐름

```text
맵 선택
→ MapRun 생성·RunState 초기화
→ Stage
→ Wave 1...N
   ↔ 건설·업그레이드·수리
   ↔ 룰렛 조작과 병력 확보
   ↔ 보관함 관리
   ↔ 병력 배치
→ Stage 정산·checkpoint
→ 정비시간: 전투·Wave 정지, 미션·선택지 처리
→ 다음 Stage
```

- 공식 계층은 `맵 → MapRun → Stage → Wave`다.
- `라운드`는 별도 상태가 아니며 공식 용어는 `Wave / 웨이브`다.
- Wave 사이에는 기본 정비시간이 없고 Stage 종료 뒤 한 번만 발생한다.
- 위험 Stage 5·10·15·20에도 Stage 경계 정비시간은 존재한다.
- 영웅 외 일반 경제·건설·수리 clock matrix는 아직 pending이다.

## 4. 영웅 능력 자동 발동 계약

```text
전투 상태 갱신
→ 공개된 trigger_conditions 평가
→ 고정 ability_priority 평가
→ 공개된 target_filter·target_priority·tie_break_rule 적용
→ 대상·비용·충전·쿨다운 재검증
→ 능력 자동 시작
→ 결과 상태 기록
```

- 기본 공격과 고유 전투 능력 모두 `AUTOMATIC_RULE_BASED`다.
- 같은 tick에 여러 능력이 준비되면 고정 우선순위의 첫 합법 능력 하나만 시작한다.
- 대상 동률은 거리·전선 진행도·생성 순서·고정 ID 같은 결정론적 기준으로 해소한다.
- 조건·능력 우선순위·대상 우선순위·고점 조건·약점은 사용자에게 공개한다.
- 저장·불러오기·Retry로 더 좋은 능력이나 타깃을 다시 굴릴 수 없다.
- 자동 발동의 비효율은 숨은 오작동이 아니라 공개된 규칙과 약점으로 예측 가능해야 한다.

## 5. 보호할 제품 코어

- PC-primary, 20 Stage·4막·약 35분 목표.
- 위험 Stage 5·10·15·20.
- 상·중·하 세 전선.
- 세 물리 원형 릴·TokenInstance·cursor·3×3 view.
- 가로 이동은 future reel structure를 영구 변경하며 undo가 없다.
- immutable SpinSnapshot과 명시적 한 번 확정.
- PendingReward 보관·판매·한 전선 비가역 배치.
- 총 30개 건설 노드.
- MapRun 건물: 금고·농장·타워·전장 병영·지휘소.
- 고정시간 점령·paid Retry 원칙·벨루 비모달 안내자.
- 기본 Profile과 원본 병종만으로 모든 콘텐츠 완료 가능.
- 무한 능력치 성장·숨은 릴 확률·전역 multiplier·자동 플레이 금지.

## 6. 실제 구현 경계

```text
CURRENT_LEGACY
- independent weighted 9-cell roulette
- barracks/tower/farm
- legacy outpost/capture_power
- free same-stage retry

LATEST_APPROVED_NOT_IMPLEMENTED
- Map→MapRun→Stage/Wave→settlement→Maintenance lifecycle
- Stage-runtime build/upgrade/repair, Roulette, storage and deployment
- three physical reels and permanent movement
- 30-node topology and five MapRun buildings
- fixed-time capture·Profile save·paid Retry
- Tavern/Barracks/Research auxiliary hub
- multi-Hero-per-archetype deterministic roster
- stored Hero-grade token conversion and irreversible deployment
- one active named Hero across all lanes
- no manual Hero exit; persistent Stage/Act instance and long-term state
- no death recovery reward; post-death matching Hero-grade result required
- conditional-peak specialized Hero sidegrades
- deterministic rule-based automatic Hero ability activation
```

`APPROVED_PLAN != IMPLEMENTED != VALIDATED`.

## 7. current authority

- `docs/PROJECT_CORE.md`
- `docs/PROJECT_CANON_DECISION_LEDGER.md`
- `docs/DOCUMENTATION_MAP.md`
- `docs/design/APPROVED_OMENWARD_MAPRUN_STAGE_WAVE_MAINTENANCE_2026-08-02.md`
- `docs/design/APPROVED_OMENWARD_HERO_UNLOCK_REGISTRATION_2026-08-02.md`
- `docs/design/APPROVED_OMENWARD_HERO_TOKEN_CONVERSION_AND_DEPLOYMENT_2026-08-02.md`
- `docs/design/APPROVED_OMENWARD_HERO_SINGLE_ACTIVE_AND_REPEAT_DEPLOYMENT_2026-08-02.md`
- `docs/design/APPROVED_OMENWARD_HERO_EXIT_AND_REPLACEMENT_2026-08-02.md`
- `docs/design/APPROVED_OMENWARD_HERO_STAGE_STATE_PERSISTENCE_2026-08-02.md`
- `docs/design/APPROVED_OMENWARD_HERO_REDEPLOYMENT_INITIAL_STATE_2026-08-02.md`
- `docs/design/APPROVED_OMENWARD_HERO_POWER_BUDGET_AND_SIDEGRADE_2026-08-02.md`
- `docs/design/APPROVED_OMENWARD_HERO_ABILITY_ACTIVATION_MODE_2026-08-02.md`
- `docs/design/APPROVED_OMENWARD_VEILSPECIES_GAMEPLAY_SCOPE_2026-08-02.md`
- `docs/operations/GRILL_ME_MERGE_CADENCE_AND_PREFLIGHT_2026-08-02.md`

## 8. Grill Me·병합 상태

```text
CURRENT_COUNT = 10_OF_10
PREFLIGHT_TRIGGER = REACHED
PREFLIGHT = REQUIRED_IN_PROGRESS
MERGE_AUTHORIZATION = NOT_GRANTED
AUTO_MERGE = FORBIDDEN
```

- 10번째 승인은 preflight 실행 트리거이지 병합 명령이 아니다.
- P0/P1 blocker가 있으면 병합할 수 없다.
- blocker가 없어도 사용자의 명시적 병합 승인 전에는 Draft PR을 병합하지 않는다.

## 9. 현재 Gate

```text
OMW-OPS-20260802-PR121-TEN-DECISION-PREFLIGHT-V1
= GitHub authority·Sheet·PR·CI·review·changed paths·P0/P1를 적대적으로 검증
```

## 10. 경계

```text
PRODUCT_CODE: UNCHANGED
CODEX: BLOCKED
EXACT_VALUES: PENDING
CURRENT_MERGE_PENDING: PREFLIGHT_ONLY
MERGE_AUTHORIZATION: NOT_GRANTED
RUNTIME/HUMAN/SIMULATION: NOT_RUN
```
