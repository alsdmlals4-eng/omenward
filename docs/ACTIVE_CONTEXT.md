# Active Context

```yaml
updated_at: 2026-08-02
project: OMENWARD / 오멘워드
work_mode: TOTAL_PLANNING
current_phase: PR121_PREFLIGHT_CONTENT_PASS_MERGE_NOT_AUTHORIZED
current_recovery_decision: OMW-DEC-20260802-CANON-RECOVERY-V1
current_planning_decision: OMW-DEC-20260802-GAMEPLAY-HERO-ABILITY-ACTIVATION-MODE-V1
current_world_decision: OMW-DEC-20260802-WORLD-VEILSPECIES-PURPOSE-V1
current_meta_decision: OMW-DEC-20260802-GAMEPLAY-HERO-ABILITY-ACTIVATION-MODE-V1
current_operating_decision: OMW-DEC-20260802-GRILL-ME-MERGE-CADENCE-V1
current_branch: main
context_baseline_commit: a521cf744533139063a72ab358b4381d2aae6f0b
working_branch: gpt/omenward-gameplay-planning-20260802
active_base_version: 9.4.1
current_product: LEGACY_PROTOTYPE
latest_planning: USER_APPROVED / ACTIVE_BRANCH_SYNCED / NOT_IMPLEMENTED
product_code_authority: NONE
codex_execution: BLOCKED
primary_platform: PC
future_platform: MOBILE_CONSIDERATION_ONLY
last_merged_pr: 120
current_pr: 121
current_grill_me_count: 10
future_merge_cadence: 10
preflight: CONTENT_PASS / FINAL_EXACT_HEAD_REVALIDATION_REQUIRED_BEFORE_MERGE
preflight_report: docs/reviews/OMENWARD_PR121_TEN_DECISION_PREMERGE_ADVERSARIAL_REVIEW_2026-08-02.md
merge_authorization: NOT_GRANTED
runtime_validation: NOT_RUN
human_validation: NOT_RUN
simulation: NOT_RUN
```

`current_branch: main`과 `context_baseline_commit`은 병합 기준선이다. 승인 기획은 `working_branch`의 Draft PR #121에 있으며 현재 제품 구현 권한은 없다.

## 1. 현재 제품 방향

- 오멘워드는 건물과 TokenSource로 세 물리 릴을 설계하고 당첨 병력을 세 전선에 비가역 배치하는 전략 오토배틀이다.
- 공식 흐름은 `맵 → MapRun → Stage → Wave → Stage 정산 → 정비시간`이다.
- MapRun 목표는 20 Stage·4막·약 35분이며 위험 Stage는 5·10·15·20이다.
- 건설·업그레이드·수리, 룰렛, 보관함, 병력 배치는 Stage와 정비시간 모두 사용할 수 있다.
- 현재 제품은 Legacy 프로토타입이고 최신 승인 기획은 미구현이다.

> **건물로 룰렛을 만들고, 룰렛으로 전선을 지휘한다.**

## 2. 영웅 정본

```text
기존 UnitArchetype
→ 주점에서 복수 이름 지정 영웅 결정론적 해금·Profile 등록
→ 룰렛 동병종 [영웅] 등급 토큰
→ 원본 병종 유지 또는 해금 영웅 1명으로 1:1 변환
→ active 영웅이 없을 때 한 전선에 비가역 배치
→ 공개 규칙 기반 자동 능력 운용
```

- 세 전선 전체 active 이름 지정 영웅은 동시에 최대 1명이다.
- 수동 퇴각·교대·판매·재보관·전선 이동은 금지다.
- 생존 영웅은 같은 인스턴스로 Stage·Act·정비시간을 넘어 유지된다.
- HP·남은 쿨다운·충전·사용 횟수·고유 자원은 Stage 경계를 넘어 유지한다.
- 일시 버프·디버프·타깃·어그로·시전·투사체·장판·일시 소환물은 Stage 정산에서 제거한다.
- 정비시간에는 영웅 HP·쿨다운·충전·고유 자원 clock이 정지한다.
- 사망은 source token·재화·회수권·부활권·무료 재출전권·보장·pity를 제공하지 않는다.
- 이름 지정 영웅 재출전에는 사망 이후 새 동병종 `[영웅]` 룰렛 결과가 필요하다.
- 사망 전 보관 토큰은 원본 병종으로 사용할 수 있지만 이름 지정 영웅 재출전에는 사용할 수 없다.
- 새 적격 토큰은 최대 HP·준비된 스킬·기본 충전·초기 고유 자원의 새 인스턴스를 만든다.

## 3. 영웅 전투 예산·자동 능력

```text
원본 [영웅] 등급 병종
= 일관성 + 범용성 + 낮은 조건 의존도

이름 지정 영웅
= 유사 평균 총 전투 예산
+ 명확한 조건부 고점
+ 고유 전술 정체성
- 명시적 약점 또는 기회비용
```

- 모든 영웅은 고점 조건·고점 보상·실제 약점·원본 선택 사유·대응 압력을 가진다.
- DPS만 맞추고 제어·지원·기동성을 무료로 추가하는 우회는 금지다.

```text
전투 상태 갱신
→ 공개 trigger 평가
→ 고정 ability priority 평가
→ 공개 target filter·priority·tie-break 적용
→ 유효성 재검증
→ 자동 발동
→ 결과 상태 기록
```

- 기본 공격과 이름 지정 영웅 전투 능력은 모두 `AUTOMATIC_RULE_BASED`다.
- 수동 스킬 버튼·수동 타깃 지정·숨은 명령 큐는 없다.
- 조건·능력 우선순위·대상 우선순위·동률 해소 규칙을 공개한다.
- 동일 저장 상태와 입력 순서에서는 같은 능력과 대상을 선택한다.
- 저장·Retry로 자동 판단을 재굴림할 수 없다.

## 4. 보호할 제품 코어

- 세 물리 원형 릴·TokenInstance·cursor·3×3 view.
- 가로 이동은 미래 릴 구조를 영구 편집하며 undo가 없다.
- immutable SpinSnapshot과 명시적 한 번 확정.
- PendingReward 보관·판매·한 전선 비가역 배치.
- 상·중·하 3전선, 총 30개 건설 노드.
- MapRun 건물: 금고·농장·타워·전장 병영·지휘소.
- 고정시간 점령·paid Retry 원칙·벨루 비모달 안내자.
- 기본 Profile과 원본 병종으로 모든 콘텐츠 완료 가능.
- 무한 성장·숨은 릴 확률·전역 multiplier·자동 플레이 금지.

## 5. 실제 구현 경계

```text
CURRENT_LEGACY
- independent weighted 9-cell roulette
- barracks/tower/farm
- legacy outpost/capture_power
- free same-stage retry

LATEST_APPROVED_NOT_IMPLEMENTED
- MapRun Stage/Wave/Maintenance lifecycle
- physical reels and permanent movement
- 30-node topology and five buildings
- paid Retry and Profile save
- Tavern/Barracks/Research hub
- full Hero lifecycle, sidegrade budget and automatic abilities
```

`APPROVED_PLAN != IMPLEMENTED != VALIDATED`.

## 6. current authority

- `docs/PROJECT_CORE.md`
- `docs/PROJECT_CANON_DECISION_LEDGER.md`
- `docs/DOCUMENTATION_MAP.md`
- `docs/design/APPROVED_VERTICAL_SLICE_SYSTEM_CONTRACT_2026-07-27.md`
- `docs/reviews/ADVERSARIAL_VERTICAL_SLICE_REVIEW_2026-07-27.md`
- `docs/benchmarks/OMENWARD_ROULETTE_AGENCY_EVIDENCE_PACK_2026-07-29.md` — `PILOT_RECOMMENDATION / NOT_CANON`
- `docs/design/APPROVED_OMENWARD_MAPRUN_STAGE_WAVE_MAINTENANCE_2026-08-02.md`
- `docs/design/APPROVED_OMENWARD_HERO_UNLOCK_REGISTRATION_2026-08-02.md`
- `docs/design/APPROVED_OMENWARD_HERO_TOKEN_CONVERSION_AND_DEPLOYMENT_2026-08-02.md`
- `docs/design/APPROVED_OMENWARD_HERO_SINGLE_ACTIVE_AND_REPEAT_DEPLOYMENT_2026-08-02.md`
- `docs/design/APPROVED_OMENWARD_HERO_EXIT_AND_REPLACEMENT_2026-08-02.md`
- `docs/design/APPROVED_OMENWARD_HERO_STAGE_STATE_PERSISTENCE_2026-08-02.md`
- `docs/design/APPROVED_OMENWARD_HERO_REDEPLOYMENT_INITIAL_STATE_2026-08-02.md`
- `docs/design/APPROVED_OMENWARD_HERO_POWER_BUDGET_AND_SIDEGRADE_2026-08-02.md`
- `docs/design/APPROVED_OMENWARD_HERO_ABILITY_ACTIVATION_MODE_2026-08-02.md`
- `docs/reviews/OMENWARD_PR121_TEN_DECISION_PREMERGE_ADVERSARIAL_REVIEW_2026-08-02.md`

## 7. preflight·병합 상태

```text
CURRENT_COUNT = 10_OF_10
CONTENT_PREFLIGHT = PASS
OPEN_P0 = 0
OPEN_P1 = 0
MERGE_BLOCKER = 0
FINAL_EXACT_HEAD_REVALIDATION = REQUIRED_BEFORE_MERGE
MERGE_AUTHORIZATION = NOT_GRANTED
DRAFT_MUST_REMAIN = TRUE
AUTO_MERGE = FORBIDDEN
```

## 8. 다음 Gate

```text
USER_EXPLICIT_MERGE_DECISION_AFTER_FINAL_EXACT_HEAD_VERIFICATION
```

## 9. 경계

```text
PRODUCT_CODE: UNCHANGED
CODEX: BLOCKED
EXACT_VALUES: PENDING
MERGE_AUTHORIZATION: NOT_GRANTED
RUNTIME/HUMAN/SIMULATION: NOT_RUN
```
