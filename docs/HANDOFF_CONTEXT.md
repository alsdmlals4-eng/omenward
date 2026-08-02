# OMENWARD 프로젝트 인수인계 컨텍스트

```yaml
updated_at: 2026-08-02
project: OMENWARD / 오멘워드
work_mode: TOTAL_PLANNING
phase: PR121_PREFLIGHT_CONTENT_PASS_MERGE_NOT_AUTHORIZED
current_world_decision: OMW-DEC-20260802-WORLD-VEILSPECIES-PURPOSE-V1
current_meta_decision: OMW-DEC-20260802-GAMEPLAY-HERO-ABILITY-ACTIVATION-MODE-V1
current_operating_decision: OMW-DEC-20260802-GRILL-ME-MERGE-CADENCE-V1
baseline_main: a521cf744533139063a72ab358b4381d2aae6f0b
working_branch: gpt/omenward-gameplay-planning-20260802
current_pr: 121
last_merged_pr: 120
base: 9.4.1_RELEASED
current_product: LEGACY_PROTOTYPE
latest_planning: APPROVED_BRANCH_SYNCED_NOT_IMPLEMENTED
product_code_authority: NONE
codex: BLOCKED
current_grill_me_count: 10
preflight: CONTENT_PASS / FINAL_EXACT_HEAD_REVALIDATION_REQUIRED_BEFORE_MERGE
preflight_report: docs/reviews/OMENWARD_PR121_TEN_DECISION_PREMERGE_ADVERSARIAL_REVIEW_2026-08-02.md
merge_authorization: NOT_GRANTED
```

## 1. 현재 제품·진행 정본

- 오멘워드는 건물과 TokenSource로 세 물리 릴을 설계하고 당첨 병력을 세 전선에 비가역 배치하는 전략 오토배틀이다.
- 현재 제품은 Legacy 프로토타입이며 최신 승인 기획은 미구현이다.
- 공식 진행 계층은 `맵 → MapRun → Stage → Wave → Stage 정산 → 정비시간`이다.
- MapRun 목표는 20 Stage·4막·약 35분이며 위험 Stage는 5·10·15·20이다.
- 건설·업그레이드·수리, 룰렛, 보관함, 병력 배치는 Stage와 정비시간 모두 사용 가능하다.
- 세계관 노출은 `균열을 통해 넘어온 이계 생물종` 수준으로 제한한다.
- 메인 허브 보조 콘텐츠는 주점·허브 병영·연구다.

## 2. 영웅 전체 계약

```text
병종별 이름 지정 영웅 복수 해금·Profile 등록
→ 룰렛 동병종 [영웅] 등급 토큰
→ 원본 병종 또는 해금 영웅 선택
→ active slot 검사
→ 1토큰을 1유닛으로 변환·한 전선 비가역 배치
→ 공개 규칙 기반 자동 능력 운용
→ 생존 시 장기 상태 유지
→ 사망 시 무회수·slot clear
→ 사망 이후 새 적격 룰렛 결과로만 이름 지정 영웅 재출전
```

- 별도 pre-run 영웅 등록·계약은 없다.
- 세 전선 전체 active 이름 지정 영웅은 동시에 최대 1명이다.
- 수동 퇴각·교대·판매·재보관·전선 이동은 불가다.
- 생존 영웅의 HP·쿨다운·충전·사용 횟수·고유 자원은 Stage를 넘어 유지한다.
- 일시 전투 상태와 임시 파생 개체는 Stage 정산에서 제거한다.
- 정비시간에는 영웅 회복·쿨다운·충전·고유 자원 clock이 정지한다.
- 영웅 사망은 토큰·재화·회수권·부활권·보장·pity를 제공하지 않는다.
- 사망 전 보관 토큰은 원본 병종으로만 사용 가능하고 이름 지정 영웅 재출전 자격이 없다.
- 적격 재출전 토큰은 `created_sequence > previous_hero.ended_sequence`를 만족한다.
- 새 영웅은 최대 HP·쿨다운 0·기본 충전·초기 고유 자원의 새 인스턴스로 시작한다.

## 3. 영웅 전투 예산·자동 발동

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
- 순수 상위호환과 무료 제어·지원·기동성은 금지다.

```text
전투 상태 갱신
→ 공개 trigger
→ 고정 ability priority
→ 공개 target filter·priority·tie-break
→ 유효성 재검증
→ 자동 발동·상태 기록
```

- 모든 이름 지정 영웅 전투 능력은 규칙 기반 자동 발동이다.
- 수동 스킬 버튼·수동 타깃 지정·수동 발동 보류는 없다.
- 동일 저장 상태와 입력 순서에서는 같은 능력과 대상을 선택한다.
- 저장·Retry로 자동 판단을 재굴림할 수 없다.

## 4. current authority

- `docs/PROJECT_CORE.md`
- `docs/PROJECT_CANON_DECISION_LEDGER.md`
- `docs/DOCUMENTATION_MAP.md`
- `docs/ACTIVE_CONTEXT.md`
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

## 5. preflight 결과

후보 증거 HEAD `be552b54b96a029dfa042675ae002ad21b96af65`:

```text
CONTENT_PREFLIGHT = PASS
OPEN_P0 = 0
OPEN_P1 = 0
MERGE_BLOCKER = 0
PRODUCT_PATHS = 0
BEHIND_MAIN = 0
COMMENTS = 0
REVIEWS = 0
UNRESOLVED_THREADS = 0
Project Core run 615 = PASS
GDD Sheet run 332 = PASS
Base v9 run 308 = PASS
```

- latest main Base v9.4.1은 main→feature PR #124로 동기화했다.
- 누락됐던 Vertical Slice·적대적 review·Evidence Pilot 라우팅을 복원했다.
- 과거 `OPEN_P1` CI 행은 역사적 해결 상태로 전환했다.
- 제품 parser·simulation·fault test는 제품 구현 전 필수지만 문서-only 병합 blocker는 아니다.

## 6. 보호할 코어

- 세 물리 릴·비가역 가로 이동·SpinSnapshot.
- 보관·판매·한 전선 비가역 배치.
- 상·중·하 3전선·총 30개 노드.
- 금고·농장·타워·전장 병영·지휘소.
- fixed-time capture·paid Retry·벨루 비모달 안내자.
- 기본 Profile과 원본 병종 완주 가능.
- 무한 성장·숨은 odds·전역 multiplier·자동 플레이 금지.

## 7. 병합 상태

```text
CURRENT_COUNT = 10_OF_10
CONTENT_PREFLIGHT = PASS
FINAL_EXACT_HEAD_REVALIDATION = REQUIRED_BEFORE_MERGE
MERGE_AUTHORIZATION = NOT_GRANTED
DRAFT_MUST_REMAIN = TRUE
AUTO_MERGE = FORBIDDEN
```

최종 exact HEAD가 Green이어도 사용자의 별도 병합 승인 전에는 Ready 전환·병합을 수행하지 않는다.

## 8. 구현 경계

```text
CURRENT_PRODUCT = LEGACY_PROTOTYPE
LATEST_APPROVED = DOCUMENTED_NOT_IMPLEMENTED
PRODUCT_CODE = UNCHANGED
EXACT_VALUES = PENDING
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
```
