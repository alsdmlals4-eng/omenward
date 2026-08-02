# OMENWARD 프로젝트 인수인계 컨텍스트

```yaml
updated_at: 2026-08-02
project: OMENWARD / 오멘워드
work_mode: TOTAL_PLANNING
phase: PR121_TEN_DECISION_ADVERSARIAL_PREFLIGHT
current_world_decision: OMW-DEC-20260802-WORLD-VEILSPECIES-PURPOSE-V1
current_meta_decision: OMW-DEC-20260802-GAMEPLAY-HERO-ABILITY-ACTIVATION-MODE-V1
current_operating_decision: OMW-DEC-20260802-GRILL-ME-MERGE-CADENCE-V1
baseline_main: 12012f88bc1dc1d9aaaa538b578be3893e4b1591
working_branch: gpt/omenward-gameplay-planning-20260802
current_pr: 121
last_merged_pr: 120
base: 9.4.0_RELEASED
current_product: LEGACY_PROTOTYPE
latest_planning: APPROVED_BRANCH_SYNCED_NOT_IMPLEMENTED
product_code_authority: NONE
codex: BLOCKED
current_grill_me_count: 10
preflight: REQUIRED_IN_PROGRESS
merge_authorization: NOT_GRANTED
```

## 1. 현재 정본

- 오멘워드는 건물과 TokenSource로 세 물리 릴을 설계하고 당첨 병력을 세 전선에 비가역 배치하는 전략 오토배틀이다.
- 현재 제품은 Legacy 프로토타입이며 최신 승인 기획은 미구현이다.
- 공식 진행 계층은 `맵 → MapRun → Stage → Wave → Stage 정산 → 정비시간`이다.
- MapRun 목표는 20 Stage이며 위험 Stage는 5·10·15·20이다.
- 건설·업그레이드·수리, 룰렛, 보관함, 병력 배치는 Stage 전투 중과 정비시간 모두 사용 가능하다.
- 세계관 노출은 `균열을 통해 넘어온 이계 생물종` 수준으로 제한한다.
- 메인 허브 보조 콘텐츠는 주점·허브 병영·연구다.

## 2. 영웅 전체 계약

```text
병종별 이름 지정 영웅 후보 복수 가능
→ 주점에서 결정론적 영구 해금·Profile 명부 등록
→ 룰렛에서 동병종 [영웅] 등급 토큰 획득
→ 보관함에서 원본 병종 유지 또는 해금 영웅 선택
→ active hero가 없으면 1토큰을 1영웅으로 변환
→ 한 전선에 비가역 배치
→ 자동 전투 능력 운용
→ 생존 시 Stage·Act·정비시간을 넘어 같은 인스턴스 유지
→ 사망 시 슬롯 해제·회수 보상 없음
→ 사망 이후 새 동병종 [영웅] 룰렛 결과로만 이름 지정 영웅 재출전
```

- 같은 병종에 여러 영웅을 해금할 수 있다.
- 별도 pre-run 영웅 등록·계약 단계는 없다.
- 세 전선 전체의 이름 지정 active 영웅은 동시에 최대 1명이다.
- 수동 퇴각·교대·판매·재보관·전선 이동은 불가다.
- 살아 있는 영웅의 HP·남은 쿨다운·충전·사용 횟수·고유 자원은 Stage 경계를 넘어 유지한다.
- 일시 버프·디버프·타깃·어그로·시전·투사체·장판·일시 소환물은 Stage 정산에서 제거한다.
- 정비시간에는 영웅 회복·쿨다운·충전·고유 자원 clock이 정지한다.
- 영웅 사망은 source token·재화·회수권·부활권·무료 재배치권·보장·pity를 제공하지 않는다.
- 사망 전 보관 토큰은 원본 영웅 등급 병종으로 사용할 수 있지만 이름 지정 영웅 재출전 자격은 없다.
- 재출전 적격 토큰은 `token.created_sequence > previous_hero.ended_sequence`를 만족해야 한다.
- 새 적격 인스턴스는 최대 HP·쿨다운 0·기본 충전·초기 고유 자원으로 시작하며 이전 상태를 승계하지 않는다.

## 3. 전투 예산·능력 발동

```text
원본 [영웅] 등급 병종
= 높은 일관성 + 넓은 범용성 + 낮은 조건 의존도

이름 지정 영웅
= 유사한 평균 총 전투 예산
+ 명확한 조건부 고점
+ 고유 전술 정체성
- 명시적 약점 또는 기회비용
```

- 영웅은 원본 병종의 순수 상위호환이 아니다.
- 모든 영웅은 고점 조건·고점 보상·명시적 약점·원본 선택 사유·대응 압력을 가진다.
- DPS만 원본과 맞추고 제어·지원·기동성을 무료로 추가하는 설계는 금지다.
- 같은 병종의 복수 영웅은 서로 다른 전술 질문에 답해야 한다.

```text
전투 상태 갱신
→ 공개 trigger 평가
→ 고정 ability priority 평가
→ 공개 target filter·priority·tie-break 적용
→ 유효성 재검증
→ 능력 자동 발동
→ 결과 상태 기록
```

- 기본 공격과 이름 지정 영웅 전투 능력은 모두 규칙 기반 자동 발동이다.
- 수동 스킬 버튼·수동 타깃 지정·수동 발동 보류는 없다.
- trigger·능력 우선순위·대상 우선순위·동률 해소 규칙을 숨기지 않는다.
- 동일 저장 상태와 입력 순서에서는 같은 능력과 대상을 선택한다.
- 저장·Retry로 능력 또는 타깃을 다시 굴리지 않는다.
- 비효율적 자동 발동은 공개된 조건과 약점에서 예측 가능해야 한다.

## 4. 보호할 코어

- PC-primary, 20 Stage·4막·약 35분.
- 세 물리 릴·TokenInstance·cursor·3×3 view.
- 가로 이동은 미래 릴 구조를 영구 편집하며 undo가 없다.
- immutable SpinSnapshot·명시적 한 번 확정.
- PendingReward 보관·판매·한 전선 비가역 배치.
- 상·중·하 3전선, 총 30개 건설 노드.
- MapRun 건물 5종: 금고·농장·타워·전장 병영·지휘소.
- 고정시간 점령·paid Retry 원칙·벨루 비모달 안내자.
- 기본 Profile과 원본 병종으로 모든 콘텐츠 완료 가능.
- 무한 성장·숨은 릴 odds·전역 multiplier·자동 플레이 금지.

## 5. current authority

- `docs/PROJECT_CORE.md`
- `docs/PROJECT_CANON_DECISION_LEDGER.md`
- `docs/DOCUMENTATION_MAP.md`
- `docs/ACTIVE_CONTEXT.md`
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
- preflight 완료 후 생성될 `docs/reviews/OMENWARD_PR121_TEN_DECISION_PREMERGE_ADVERSARIAL_REVIEW_2026-08-02.md`.

## 6. 실제 구현 경계

```text
CURRENT_PRODUCT
- independent weighted 9-cell roulette
- barracks/tower/farm
- legacy outpost/capture_power
- free same-stage retry

LATEST_APPROVED_NOT_IMPLEMENTED
- MapRun Stage/Wave/Maintenance lifecycle
- Stage-runtime build/upgrade/repair, Roulette, storage and deployment
- physical reels and permanent movement
- 30-node topology and five buildings
- paid Retry and Profile save
- Tavern/Barracks/Research hub
- multi-Hero-per-archetype roster and token conversion
- single active Hero, persistent lifecycle and post-death provenance
- conditional-peak specialized Hero sidegrades
- deterministic automatic Hero ability activation
```

## 7. Grill Me·preflight 운영

```text
CURRENT_COUNT = 10_OF_10
PREFLIGHT_TRIGGER = REACHED
PREFLIGHT = REQUIRED_IN_PROGRESS
MERGE_AUTHORIZATION = NOT_GRANTED
AUTO_MERGE = FORBIDDEN
```

- 이번 10건은 PR #121의 현재 묶음이다.
- preflight에서 blocker 0이면 병합 가능 상태일 수 있으나 사용자의 명시적 병합 승인 전에는 Draft를 유지한다.
- 제품 구현·Ready 전환·병합은 자동으로 수행하지 않는다.

## 8. 다음 Gate

```text
OMW-OPS-20260802-PR121-TEN-DECISION-PREFLIGHT-V1
= GitHub·Sheet·PR·CI·review·authority·P0/P1 전수 검증
```

```text
EXACT_VALUES: PENDING
SIMULATION: NOT_RUN
RUNTIME: NOT_RUN
HUMAN_QA: NOT_RUN
PRODUCT_CODE: UNCHANGED
```
