# 오멘워드 버티컬 슬라이스 런타임·피로도 계약

- 프로젝트: **오멘워드 / OMENWARD**
- 승인일: 2026-07-31
- 상태: `USER_APPROVED_PLANNING_DECISION / PLANNING_ONLY / PRODUCT_CODE_NOT_AUTHORIZED`
- 연결 Issue: `#115`
- 연결 Draft PR: `#116`
- 주 플랫폼: PC

이 문서는 20스테이지 Full-System Vertical Slice의 목표 플레이시간, 스테이지 시간 예산, 피로도 제한, 4막 진행 구조와 플레이테스트 통과 기준을 소유한다. 제품 코드·Google Sheet·활성 운영 계약을 변경하지 않으며, 후속 기획 통합과 검수의 입력으로 사용한다.

---

## 1. 승인된 핵심 결정

```yaml
run_duration:
  target: 35_minutes
  normal_range: 30_to_40_minutes
  first_run_max: 45_minutes
  stages: 20

platform:
  primary: PC
  mobile: future_feasibility_only

scope:
  full_system_connection: required
  unique_content_per_stage: not_required
  product_code_authorization: false
  codex_execution: blocked_until_planning_review_and_user_approval
```

판정:

- 반복 플레이는 `30~35분`에 수렴한다.
- 표준 플레이의 중앙 목표는 `약 35분`이다.
- 첫 플레이는 설명·탐색 비용을 포함해 `40~45분`까지 허용한다.
- `45분 초과`는 기본 목표가 아니라 피로도·과밀·동선 문제를 조사해야 하는 실패 신호다.
- 20스테이지는 유지하지만 20개의 독립 콘텐츠를 각각 제작하지 않는다.

---

## 2. 전체 시간 예산

| 구간 | 수량 | 스테이지당 목표 | 누적 목표 |
| --- | ---: | ---: | ---: |
| 일반 스테이지 | 16 | 55~70초 | 약 15~19분 |
| 위험 스테이지 | 3 | 90~120초 | 약 4.5~6분 |
| 최종 위험 스테이지 | 1 | 150~210초 | 약 2.5~3.5분 |
| 준비·정산·전환 | 전체 | 누적 관리 | 약 7~10분 |
| 전체 MapRun | 20 | - | 약 30~40분 |

스테이지 5·10·15는 위험 스테이지다. 스테이지 20은 위험과 최종 속성을 함께 가진다.

현재 문서의 `기준 일반 웨이브 길이 60초`는 이 목표와 양립하지 않으므로 `SUPERSEDED_TUNING_INPUT`으로 강등한다. 웨이브 수 구조는 유지할 수 있지만 웨이브 하나가 60초를 독점하는 방식은 사용하지 않는다.

---

## 3. 웨이브 시간 계약

### 일반 스테이지

```yaml
waves: 3
spawn_window_per_wave: 15_to_18_seconds
stage_total: 55_to_70_seconds
```

### 위험 스테이지

```yaml
waves: 4
spawn_window_per_wave: 18_to_22_seconds
stage_total: 90_to_120_seconds
planning_pause: disabled_after_start
new_tutorials: 0
```

### 최종 스테이지

```yaml
waves_or_phases: 5_waves_or_3_phases
stage_total: 150_to_210_seconds
new_major_systems: 0
purpose: integrated_mastery_test
```

규칙:

1. 예약된 웨이브 출현 시간표는 잔존 적 때문에 무기한 지연되지 않는다.
2. 이전 웨이브의 잔존 적은 다음 웨이브와 겹칠 수 있다.
3. 적 HP만 늘려 시간을 채우지 않는다.
4. 위험과 최종 스테이지의 난이도는 숨은 정보가 아니라 실행 압박·복합 위협·자원 선택에서 나온다.
5. 최종 스테이지는 새 시스템을 소개하지 않고 이전 19스테이지의 설계를 회수한다.

---

## 4. 4막 진행 구조

| 막 | 스테이지 | 플레이어 경험 | 핵심 검증 |
| --- | --- | --- | --- |
| 1막 — 이해 | 1~5 | 읽고 커밋한다 | 공세 읽기, 기본 룰렛, 보관·판매·비가역 배치 |
| 2막 — 설계 | 6~10 | 확률 구조를 만든다 | TokenSource, 영구 가로 이동, Tier 2, 중앙 경합 지역 |
| 3막 — 압박과 복구 | 11~15 | 잃고 다시 운영한다 | 점령, 수리, 철거, 식량, 복수 전선 기회비용 |
| 4막 — 설계 회수 | 16~20 | 내 구조로 전쟁을 끝낸다 | 대표 Tier 3, 복합 공세, 적 거점·본진, 최종 통합 시험 |

### 막별 위험 스테이지 역할

- **스테이지 5:** 전술계획 정지 없이 실행하는 차이를 안전하게 학습한다.
- **스테이지 10:** 건물과 TokenSource가 원하는 결과 확률에 실제 영향을 주는지 검증한다.
- **스테이지 15:** 수리·경제·복수 전선 압박 아래에서 무엇을 포기할지 결정한다.
- **스테이지 20:** 플레이어가 만든 릴·건물·배치 구조가 최종 결과의 주원인이 되게 한다.

---

## 5. 준비 단계 피로도 계약

```yaml
preparation:
  hard_time_limit: false
  normal_target: 15_to_25_seconds
  danger_target: 30_to_45_seconds
  final_target_max: 60_seconds

fatigue_budget:
  major_decisions_per_preparation: 2_to_3
  new_major_concepts_per_stage: 1
  new_major_concepts_danger_stage: 0
  act_breaks_after_stages: [5, 10, 15]
```

원칙:

1. 무제한 준비 시간은 접근성과 전략 검토를 위해 유지한다.
2. 정상 흐름은 추천 작업, 변경점 요약, 즉시 시작 경로를 통해 목표시간에 수렴해야 한다.
3. 한 준비 단계가 건설·수리·업그레이드·미션·룰렛·보관함을 모두 동등하게 압박하지 않는다.
4. 플레이어가 처리할 주요 질문은 최대 2~3개다.
5. 위험 스테이지에서는 신규 시스템 튜토리얼을 제공하지 않는다.
6. 장시간 준비가 필요했다면 단순히 플레이어 숙련 부족으로 처리하지 않고 정보 구조·동선·의사결정 과밀을 조사한다.

대표 의사결정:

```text
1. 어느 전선에 대응할 것인가
2. 어떤 건물·릴 구조를 바꿀 것인가
3. 결과를 보관·판매·배치할 것인가
```

---

## 6. 막 사이 호흡 구간

스테이지 5·10·15 종료 뒤 선택적 정리 구간을 제공한다.

- 목표 길이: `20~40초`
- 강제 컷신: 사용하지 않음
- 전선 소유권·본진·건물 피해 변화 요약
- 릴 배열과 TokenSource 변화 요약
- 주요 병력 손실과 획득 요약
- 벨루의 짧은 상황 보고
- checkpoint 저장 완료 표시
- 즉시 다음 준비로 넘어가는 입력 제공

이 구간은 콘텐츠 감상보다 인지 정리와 손 피로 완화를 우선한다.

---

## 7. UX·접근성 영향

항상 모든 정보를 같은 강도로 보여주지 않는다.

```text
1단계 — 즉시 위험
라인 위협·본진·거점·남은 시간

2단계 — 현재 선택
룰렛 결과·배치 대상·건물 작업

3단계 — 분석 정보
TokenSource·가능 결과·과거 결과·벨루 팁
```

추가 원칙:

- 위험 스테이지에서 분석 패널이 전장 위험을 가리지 않는다.
- 준비 화면과 전투 화면의 주요 입력 구조를 과도하게 다르게 만들지 않는다.
- 색상만으로 위험·출처·커밋 상태를 전달하지 않는다.
- 첫 플레이의 설명 시간과 반복 플레이의 조작 시간을 별도 측정한다.

---

## 8. 플레이테스트 통과 기준

### 시간

- 반복 플레이 중앙값: `30~35분`
- 전체 정상 범위: 참가자의 다수가 `30~40분`
- 첫 플레이: `45분 이하`
- 일반 스테이지 중앙값: `70초 이하`
- 위험 스테이지: `120초 이하`
- 최종 스테이지: `210초 이하`
- 일반 준비 중앙값: `25초 이하`

### 피로도·이해도

- 스테이지 10 전후에 플레이어가 건물·TokenSource·릴 결과의 인과를 설명할 수 있다.
- 위험 스테이지 종료 후 다음 행동을 파악하지 못하는 상태가 반복되지 않는다.
- 한 준비 화면에서 세 가지를 넘는 주요 결정을 동시에 처리한다고 느끼는 참가자가 다수면 실패다.
- 20스테이지 종료 전에 반복적으로 `남은 시간이 너무 길다`고 보고하면 시간 구조를 재조정한다.
- 막 사이 정리 구간이 흐름을 끊는지, 피로를 낮추는지 별도 측정한다.

### 실패 신호

```text
RUN_OVER_45_MINUTES
NORMAL_STAGE_OVER_90_SECONDS_REPEATED
DANGER_STAGE_OVER_120_SECONDS
PREPARATION_MEDIAN_OVER_30_SECONDS
DECISION_OVERLOAD_REPORTED
PLAYER_CANNOT_EXPLAIN_CAUSE_CHAIN_BY_STAGE_10
```

실패 신호는 적 수치만 낮추는 방식으로 처리하지 않는다. 스테이지 목표, 정보량, 입력 동선, 웨이브 겹침, 경제 압박을 함께 진단한다.

---

## 9. 후속 기획 전파 대상

이 결정은 전체 기획 검수 후 다음 정본에 통합한다.

- `docs/PROJECT_CORE.md`
- `docs/OMENWARD_GAME_DESIGN.md`
- `docs/design/APPROVED_VERTICAL_SLICE_SYSTEM_CONTRACT_2026-07-27.md`
- `docs/DECISIONS_PENDING.md`
- `docs/DEVELOPMENT_ROADMAP.md`
- Google Sheet의 `20_코어경험_데모목표`, `30_데모범위_품질기준_제작기반`, `50_메인콘텐츠`, `80_데모_버티컬슬라이스_플레이테스트`

현재는 기획·검수 브랜치이므로 활성 정본과 Google Sheet에 즉시 쓰지 않는다. 전체 기획 검수와 사용자 승인 후 정확한 범위로 전파한다.

---

## 10. 현재 상태

```text
RUN_DURATION_CONTRACT: USER_APPROVED
TARGET_DURATION: 35_MINUTES
NORMAL_RANGE: 30_TO_40_MINUTES
FIRST_RUN_MAX: 45_MINUTES
TWENTY_STAGE_STRUCTURE: RETAINED
FATIGUE_BUDGET: APPROVED
PRODUCT_IMPLEMENTATION: NOT_AUTHORIZED
CODEX_EXECUTION: BLOCKED
SHEET_WRITE: BLOCKED_UNTIL_PLANNING_SYNC_APPROVAL
```
