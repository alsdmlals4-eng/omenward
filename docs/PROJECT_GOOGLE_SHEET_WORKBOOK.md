# OMENWARD 프로젝트 Google Sheets Workbook

```yaml
project: omenward
spreadsheet_id: 1VLwRtXGDtyj0JFt98wdIOtG6Zqc3wtdfCzSF9Fo6lpw
spreadsheet_url: https://docs.google.com/spreadsheets/d/1VLwRtXGDtyj0JFt98wdIOtG6Zqc3wtdfCzSF9Fo6lpw/edit
workbook_role: USER_FACING_GDD_WORKSPACE
sheet_edit_policy: PROPOSED_SHEET_CHANGE
canonical_authority: GITHUB
current_sync_decision: OMW-DEC-20260802-GAMEPLAY-HERO-ABILITY-ACTIVATION-MODE-V1
current_operating_gate: OMW-OPS-20260802-PR121-TEN-DECISION-PREFLIGHT-V1
baseline_main_commit: 12012f88bc1dc1d9aaaa538b578be3893e4b1591
working_branch: gpt/omenward-gameplay-planning-20260802
active_base: 9.4.0
last_merged_pr: 120
current_pr: 121
sheet_status: PROJECT_SHEET_CONFIGURED / READBACK_PENDING / CI_PENDING
current_grill_me_count: 10
preflight: REQUIRED_IN_PROGRESS
merge_authorization: NOT_GRANTED
last_full_audit: 2026-08-02
```

Google Sheet는 사용자가 전체 GDD 흐름·결정·근거·작업 순서를 확인하고 수정하는 계획 작업면이다. 독립 정본이 아니며 GitHub 정본을 임의로 덮어쓰지 않는다.

## 1. 상태 축

```text
Decision ID
Canonical authority path
Baseline main commit
Active planning PR head
Implementation status
Automated validation status
Human validation status
Sheet read-back status
Grill Me approval count
Preflight status
Merge authorization
```

## 2. 주요 탭 역할

| 탭 | 역할 |
|---|---|
| `00_프로젝트_허브` | 현재 단계·Decision·main/PR SHA·preflight·카운터 |
| `01_작업순서` | 10번째 승인·preflight·병합 보류 순서 |
| `02_현재_확정결정` | 같은 Decision ID의 자동 발동 승인 내용 |
| `04_누락_충돌_감사` | 자동 판단·결정론·UI·preflight finding |
| `05_GDD_요약` | 최신 영웅 규칙·구현 경계·검증 상태 |
| `12_핵심루프` | 영웅 선택·배치·조건 조성·자동 전투 흐름 |
| `15_조작_게임규칙` | 수동 스킬 금지·trigger/priority/tie-break 규칙 |
| `40_핵심시스템_메인콘텐츠` | HeroAbilitySpec·결정론·저장 구조 |
| `41_성장_경제` | 영웅 해금이 조작 우위나 전역 강화가 되지 않는 경계 |
| `50_메인콘텐츠` | 자동 발동 조건·약점이 드러나는 encounter 구성 |
| `60_UX_UI_접근성` | 자동 표기·예고·대상·실패 원인·쿨다운 표시 |
| `99_변경이력` | GitHub path·HEAD·Sheet 범위·read-back·preflight 결과 |

## 3. 현재 동기화 Decision

Decision: `OMW-DEC-20260802-GAMEPLAY-HERO-ABILITY-ACTIVATION-MODE-V1`

```text
전투 상태 갱신
→ 공개 trigger_conditions 평가
→ 고정 ability_priority 평가
→ 공개 target_filter·target_priority·tie_break_rule 적용
→ 대상·비용·충전·쿨다운 재검증
→ 능력 자동 시작
→ 결과 상태 기록
```

- 이름 지정 영웅의 기본 공격과 전투 능력은 규칙 기반 자동 발동이다.
- 수동 스킬 버튼·수동 타깃 지정·수동 발동 보류는 금지한다.
- 플레이어는 영웅 선택·전선 배치·병력 조합·조건 조성으로 능력 고점을 만든다.
- trigger·능력 우선순위·대상 우선순위·동률 해소 규칙을 숨기지 않는다.
- 같은 tick에 여러 능력이 준비되면 고정 우선순위의 첫 합법 능력 하나만 시작한다.
- 동일 저장 상태·입력 순서에서는 같은 능력과 대상을 선택한다.
- 저장·Retry로 능력 또는 타깃을 다시 굴릴 수 없다.
- 자동 비효율은 공개된 조건·우선순위·명시적 약점에서 예측 가능해야 한다.
- 정확 능력·trigger·priority·tick·수치·UI는 별도 명세와 검증 전까지 pending이다.

## 4. 10건 preflight 상태

```text
CURRENT_GRILL_ME_COUNT = 10_OF_10
PREFLIGHT_TRIGGER = REACHED
PREFLIGHT = REQUIRED_IN_PROGRESS
MERGE_AUTHORIZATION = NOT_GRANTED
AUTO_MERGE = FORBIDDEN
```

- 10건 도달은 preflight 시작 트리거다.
- P0/P1 blocker가 있으면 병합하지 않는다.
- blocker 0이어도 사용자 명시적 병합 승인 전에는 Draft를 유지한다.
- preflight 결과는 GitHub review 문서와 Sheet 감사·변경이력에 함께 기록한다.

## 5. 동기화 후보

```text
PR #121 candidate head before Sheet synchronization:
d2789554e7199f0e84b27aabbfebda5f35a5d6f0

SHEET_BOUNDED_READBACK: PENDING
REQUIRED_CI_AT_CANDIDATE_HEAD: PENDING
PREFLIGHT_AT_CANDIDATE_HEAD: PENDING
```

동기화 예정 범위:

- `00_프로젝트_허브!E2:L2`
- `01_작업순서!A25:N26`
- `02_현재_확정결정!A34:M34`
- `04_누락_충돌_감사!A103:H111`
- `05_GDD_요약!D8:J8`
- `05_GDD_요약!B9:J9`
- `12_핵심루프!A11:J11`
- `15_조작_게임규칙!A14:J14`
- `40_핵심시스템_메인콘텐츠!A14:J14`
- `41_성장_경제!A24:I24`
- `50_메인콘텐츠!A21:J21`
- `60_UX_UI_접근성!A22:J22`
- `99_변경이력!A35:H36`

## 6. 기존 승인 연결

- 영웅 변환은 `1토큰 → 1유닛`이며 보너스 유닛과 릴 odds 변경이 없다.
- 전장 전체 active 이름 지정 영웅은 최대 1명이다.
- 영웅은 수동 퇴각·교대할 수 없고 생존 시 같은 인스턴스로 유지된다.
- 영웅의 장기 상태는 Stage를 넘어 유지하며 일시 전투 상태는 정산에서 제거한다.
- 사망은 회수 보상을 제공하지 않고 이름 지정 영웅 재출전에는 post-death token provenance가 필요하다.
- 이름 지정 영웅은 원본 병종과 유사한 평균 전투 예산의 조건부 고점형 전문화 sidegrade다.
- 자동 발동 편의성은 전투 예산 밖의 무료 전투력이나 수동 APM 우위가 아니다.
- 기본 Profile과 원본 영웅 등급 병종만으로 모든 콘텐츠 완료 가능성을 유지한다.

## 7. 권위 매핑

| 의미 | GitHub 책임 원본 |
|---|---|
| 제품 코어 | `docs/PROJECT_CORE.md` |
| 현재 승인 Decision | `docs/PROJECT_CANON_DECISION_LEDGER.md` |
| 영웅 전투 예산·전문화 | `docs/design/APPROVED_OMENWARD_HERO_POWER_BUDGET_AND_SIDEGRADE_2026-08-02.md` |
| 영웅 능력 자동 발동·결정론 | `docs/design/APPROVED_OMENWARD_HERO_ABILITY_ACTIVATION_MODE_2026-08-02.md` |
| Grill Me preflight 운영 | `docs/operations/GRILL_ME_MERGE_CADENCE_AND_PREFLIGHT_2026-08-02.md` |
| PR #121 preflight 결과 | `docs/reviews/OMENWARD_PR121_TEN_DECISION_PREMERGE_ADVERSARIAL_REVIEW_2026-08-02.md` |
| 현재 작업 | `docs/ACTIVE_CONTEXT.md` |
| 질문별 라우팅 | `docs/DOCUMENTATION_MAP.md` |

## 8. 금지

- 수동 스킬 버튼·수동 타깃 지정·영웅별 혼합 조작 방식.
- 숨은 trigger·숨은 능력 우선순위·숨은 대상 우선순위.
- 동률에서 비결정적 대상 선택.
- 저장·Retry로 더 좋은 능력이나 타깃을 재굴림.
- 자동 편의성과 무료 제어·지원·기동성을 함께 받아 순수 상위호환이 됨.
- 영웅 보유 자체가 전역 능력치·숨은 릴 odds·무료 병력을 제공.
- 10건 도달을 자동 병합 승인으로 해석.
- 승인 기획을 구현 완료·runtime 검증 완료로 표시.

## 9. 동기화 절차

```text
사용자 승인
→ GitHub 분야 정본·Ledger·Map·Context·운영 문서 갱신
→ candidate commit
→ Sheet 결정·분야·감사·변경이력 갱신
→ bounded read-back
→ candidate HEAD·CI 확인
→ 적대적 preflight
→ preflight review 문서 commit
→ final exact HEAD·CI·PR·review·changed-path 확인
→ Sheet final HEAD·preflight 상태 갱신
→ 사용자 명시 병합 승인 전 Draft 유지
```

`PARTIAL_SYNC_BLOCKED`, `SYNC_CONFLICT`, `OPEN_P0_OR_P1`이면 병합으로 진행하지 않는다.

## 10. 현재 상태

```text
SHEET_STATUS = READBACK_PENDING / CI_PENDING
BASELINE_MAIN = 12012f88bc1dc1d9aaaa538b578be3893e4b1591
GRILL_ME_COUNTER = 10_OF_10
PREFLIGHT = REQUIRED_IN_PROGRESS
MERGE_AUTHORIZATION = NOT_GRANTED
PRODUCT_CODE = UNCHANGED
```
