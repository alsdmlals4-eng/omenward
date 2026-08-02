# OMENWARD 프로젝트 인수인계 컨텍스트

```yaml
updated_at: 2026-08-02
project: OMENWARD / 오멘워드
work_mode: TOTAL_PLANNING
phase: GAMEPLAY_HERO_REDEPLOYMENT_GRILL_ME_READY
current_world_decision: OMW-DEC-20260802-WORLD-VEILSPECIES-PURPOSE-V1
current_meta_decision: OMW-DEC-20260802-GAMEPLAY-HERO-STAGE-STATE-PERSISTENCE-V1
current_operating_decision: OMW-DEC-20260802-GRILL-ME-MERGE-CADENCE-V1
baseline_main: 12012f88bc1dc1d9aaaa538b578be3893e4b1591
working_branch: gpt/omenward-gameplay-planning-20260802
last_merged_pr: 120
superseded_pr: 116_CLOSED_NOT_MERGED
base: 9.4.0_RELEASED
current_product: LEGACY_PROTOTYPE
latest_planning: APPROVED_BRANCH_SYNCED_NOT_IMPLEMENTED
product_code_authority: NONE
codex: BLOCKED
current_grill_me_count: 7
future_merge_cadence: 10
```

## 1. 현재 정본

- 오멘워드는 건물과 TokenSource로 세 물리 릴을 설계하고 당첨 병력을 세 전선에 비가역 배치하는 전략 오토배틀이다.
- 현재 제품은 Legacy 프로토타입이고 최신 기획은 미구현이다.
- 플레이어는 맵을 선택해 하나의 MapRun을 시작하고 RunState를 초기화한다.
- 현재 MapRun 목표는 20 Stage이며 각 Stage는 선택 맵이 정의한 하나 이상의 Wave로 구성된다.
- Stage 정산 뒤 정비시간에 전투·Wave 진행을 멈추고 미션·선택지를 처리한다.
- 건설·업그레이드·수리, 룰렛, 보관함, 병력 배치는 Stage 전투 중에도 사용할 수 있다.
- 세계관은 `균열을 통해 넘어온 이계 생물종` 정도로만 사용자에게 제시한다.
- 적은 군집·돌격·원거리·방호·교란·공성 역할로 제작하며 경계파쇄자는 균열을 고정·확장하는 보스급 생물이다.
- 메인 허브 보조 콘텐츠는 주점·허브 병영·연구다.
- 영웅은 기존 병종에 고정 연결되며 같은 병종에 여러 영웅을 해금할 수 있다.
- 주점 해금은 Profile 영웅 명부 등록이며 별도 pre-run 영웅 편성은 없다.
- 룰렛의 동병종 `[영웅]` 등급 토큰을 보관한 뒤 원본 유지 또는 해금 영웅 변환을 선택한다.
- 세 전선을 합쳐 출전 중인 이름 지정 영웅은 동시에 최대 1명이다.
- 배치한 영웅은 수동 퇴각·교대할 수 없고 Stage·Act·정비시간에도 살아 있는 동일 인스턴스로 유지된다.
- 살아 있는 영웅의 현재 HP·남은 쿨다운·충전·사용 횟수·고유 자원은 Stage를 넘어 유지한다.
- 일시 버프·디버프·타깃·어그로·시전·투사체·장판·일시 소환물은 Stage 정산에서 제거한다.
- 정비시간에는 영웅 회복·쿨다운·충전·고유 자원 clock이 정지한다.

## 2. MapRun·Stage·Wave·정비시간 계약

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
→ 정비시간: 전투·Wave 일시정지, 미션·선택지 처리
→ 다음 Stage
```

- 공식 계층은 `맵 → MapRun → Stage → Wave`다.
- `라운드`는 별도 상태가 아니며 공식 용어는 `Wave / 웨이브`다.
- Wave 사이에는 기본 정비시간이 없고 Stage 종료 뒤 한 번만 발생한다.
- 위험 Stage에서도 Stage 경계 정비시간은 존재한다.
- 네 가지 운영 기능은 정비시간 전용이 아니며 Stage 진행 중에도 실시간 사용 가능하다.
- 영웅 clock 외 일반 경제·건설·수리 clock matrix는 pending이다.
- MapRun 초기화는 RunState만 초기화하며 Profile 영구 해금은 유지한다.

## 3. 영웅 계약

```text
병종별 영웅 후보 복수 가능
→ 주점에서 영구 해금·명부 등록
→ 동병종 [영웅] 등급 토큰을 룰렛에서 획득
→ 보관함에서 원본 또는 해금 영웅 선택
→ active hero가 없으면 1토큰을 1영웅으로 치환
→ 한 전선에 비가역 배치
→ 살아 있는 동안 Stage·Act·정비시간을 넘어 유지
→ Stage 정산에서 장기 상태 저장·전투 잔여물 제거
→ 사망·완전 제거 또는 MapRun 종료 시 슬롯 해제
```

- 다른 병종 영웅은 후보가 아니다.
- 해금 영웅은 릴 확률·전역 능력치·과거 결과를 바꾸지 않는다.
- 영웅 변환은 보너스 병력을 추가하지 않는다.
- 변환하지 않은 원본 영웅 등급 병종도 정상 배치 가능하다.
- active hero가 있으면 새 토큰은 보관하거나 원본 병종으로 배치한다.
- 서로 다른 영웅도 동시에 둘 이상 출전할 수 없다.
- 같은 영웅은 이전 인스턴스가 사망·완전 제거된 뒤 새 영웅 등급 토큰으로 다시 배치할 수 있다.
- 수동 퇴각·교대·판매·재보관·전선 이동은 불가다.
- Stage·Act 전환과 정비시간만으로 영웅을 귀환시키거나 무료 교체하지 않는다.
- 배치 확정 전에는 취소·후보 변경 가능, 확정 뒤 되돌릴 수 없다.
- 현재 HP·남은 쿨다운·충전·사용 횟수·고유 자원은 Stage를 넘어 현재 값 그대로 유지한다.
- 일시 버프·디버프·타깃·어그로·시전 상태는 Stage 정산에서 초기화한다.
- 투사체·장판·일시 소환물은 Stage 정산에서 제거한다.
- 정비시간에는 영웅 회복·쿨다운·충전·고유 자원 clock이 정지한다.
- 사망 후 새 토큰으로 출전하는 새 영웅 인스턴스의 초기 상태는 pending이다.

## 4. 보호할 코어

- PC-primary.
- 20 Stage·4막·약 35분.
- Stage별 맵 정의 Wave 구성과 Stage 종료 뒤 정비시간.
- 위험 Stage 5·10·15·20.
- 세 물리 릴·비가역 가로 이동·SpinSnapshot.
- 보관·판매·한 라인 비가역 배치.
- Stage 중 건설·업그레이드·수리·룰렛·보관함·병력 배치 가능.
- 전장 3라인, 건설 노드 1종, 전체 30개.
- MapRun 건물 5종: 금고·농장·타워·전장 병영·지휘소.
- fixed-time capture·paid Retry 원칙·벨루 비모달 안내자.
- 기본 Profile로 모든 콘텐츠 완료 가능.

## 5. 보조 허브 경계

```text
메인 1순위 = 이어하기·새 작전
보조 시설 = 주점·병영·연구
노드 = 유한·비용/선행/결과 공개
```

- 주점: 병종별 복수 영웅 후보 해금·명부 관리.
- 보관함: 영웅 등급 토큰의 원본 유지 또는 동병종 해금 영웅 변환.
- 전장: 이름 지정 영웅 active slot 1개를 세 전선이 공유.
- 영웅은 수동 퇴각·교대할 수 없으며 사망·MapRun 종료로만 active 상태를 종료한다.
- 허브 병영: 병사·병종·전문화·교리 sidegrade.
- 연구: 대체 건물·TokenSource·미션·정보·편의 sidegrade.
- 금지: 랜덤 유료 영입, 중복 합성, 무한 레벨, 전 구간 배율, 숨은 릴 확률, 자동 플레이.

## 6. current authority

- `docs/PROJECT_CORE.md`
- `docs/PROJECT_CANON_DECISION_LEDGER.md`
- `docs/DOCUMENTATION_MAP.md`
- `docs/design/APPROVED_OMENWARD_MAPRUN_STAGE_WAVE_MAINTENANCE_2026-08-02.md`
- `docs/design/APPROVED_OMENWARD_HERO_UNLOCK_REGISTRATION_2026-08-02.md`
- `docs/design/APPROVED_OMENWARD_HERO_TOKEN_CONVERSION_AND_DEPLOYMENT_2026-08-02.md`
- `docs/design/APPROVED_OMENWARD_HERO_SINGLE_ACTIVE_AND_REPEAT_DEPLOYMENT_2026-08-02.md`
- `docs/design/APPROVED_OMENWARD_HERO_EXIT_AND_REPLACEMENT_2026-08-02.md`
- `docs/design/APPROVED_OMENWARD_HERO_STAGE_STATE_PERSISTENCE_2026-08-02.md`
- `docs/design/APPROVED_OMENWARD_VEILSPECIES_GAMEPLAY_SCOPE_2026-08-02.md`
- `docs/design/APPROVED_OMENWARD_AUXILIARY_HUB_PROGRESSION_2026-08-02.md`
- `docs/design/APPROVED_OMENWARD_META_PROGRESSION_ROLE_2026-08-02.md`
- `docs/design/APPROVED_OMENWARD_VISUAL_SCREEN_BOARD_V2_TEXT_SPEC_2026-08-01.md`
- `docs/operations/GRILL_ME_MERGE_CADENCE_AND_PREFLIGHT_2026-08-02.md`

## 7. 실제 구현 경계

```text
CURRENT_PRODUCT
- independent weighted 9-cell roulette
- barracks/tower/farm
- legacy outpost/capture_power
- free same-stage retry

LATEST_APPROVED_NOT_IMPLEMENTED
- map selection→MapRun reset→Stage/Wave→settlement→maintenance lifecycle
- Stage-runtime build/upgrade/repair, roulette, storage and deployment
- physical reels and permanent movement
- 30-node topology and five buildings
- paid Retry and Profile save
- minimal extradimensional-creature gameplay scope
- Tavern/Barracks/Research permanent-node hub
- multi-hero-per-unit unlock roster
- stored Hero-grade token conversion and irreversible deployment
- one active Hero across all lanes; repeat deployment after slot clears
- no manual Hero retreat or replacement; same instance persists across Stage, Act and MaintenancePhase
- persistent Hero HP/cooldowns/charges/unique resources across Stage boundaries
- transient Hero combat state cleared and Hero clocks paused during MaintenancePhase
```

## 8. Grill Me 운영

- 현재 승인 카운터는 `7/10`이다.
- 10번째 승인 시 병합 preflight를 실행한다.
- blocker가 있으면 병합하지 않는다.

## 9. 다음 Gate

```text
OMW-DEC-20260802-GAMEPLAY-HERO-REDEPLOYMENT-INITIAL-STATE-V1
= 영웅 사망 뒤 새 영웅 등급 토큰으로 같은 영웅 또는 다른 영웅을 재배치할 때 새 인스턴스의 HP·쿨다운·충전·고유 자원은 어떤 초기값으로 시작하는가
```

```text
EXACT_VALUES: PENDING
SIMULATION: NOT_RUN
RUNTIME: NOT_RUN
HUMAN_QA: NOT_RUN
PRODUCT_CODE: UNCHANGED
```