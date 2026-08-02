# OMENWARD 프로젝트 Google Sheets Workbook

```yaml
project: omenward
spreadsheet_id: 1VLwRtXGDtyj0JFt98wdIOtG6Zqc3wtdfCzSF9Fo6lpw
spreadsheet_url: https://docs.google.com/spreadsheets/d/1VLwRtXGDtyj0JFt98wdIOtG6Zqc3wtdfCzSF9Fo6lpw/edit
workbook_role: USER_FACING_GDD_WORKSPACE
sheet_edit_policy: PROPOSED_SHEET_CHANGE
canonical_authority: GITHUB
current_sync_decision: OMW-DEC-20260802-GAMEPLAY-HERO-POWER-BUDGET-AND-SIDEGRADE-V1
baseline_main_commit: 12012f88bc1dc1d9aaaa538b578be3893e4b1591
working_branch: gpt/omenward-gameplay-planning-20260802
active_base: 9.4.0
last_merged_pr: 120
superseded_pr: 116_CLOSED_NOT_MERGED
sheet_status: PROJECT_SHEET_CONFIGURED / READBACK_PENDING / CI_PENDING
current_grill_me_count: 9
next_decision: OMW-DEC-20260802-GAMEPLAY-HERO-ABILITY-ACTIVATION-MODE-V1
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
```

## 2. 주요 탭 역할

| 탭 | 역할 |
|---|---|
| `00_프로젝트_허브` | 현재 단계·Decision·main/PR SHA·다음 Gate·카운터 |
| `01_작업순서` | 승인·선행/후속·병합 단계 |
| `02_현재_확정결정` | 같은 Decision ID의 승인 내용 |
| `04_누락_충돌_감사` | 적대적 finding·해결·검증·merge blocker |
| `05_GDD_요약` | 최신 게임플레이·Meta·구현 요약 |
| `12_핵심루프` | 영웅 토큰 선택과 원본·영웅 전문화 판단 흐름 |
| `15_조작_게임규칙` | 전투 예산·고점 조건·약점·상위호환 금지 규칙 |
| `40_핵심시스템_메인콘텐츠` | HeroPowerBudgetProfile·다축 비교·검증 구조 |
| `41_성장_경제` | 영웅 해금을 순수 강화가 아닌 전문화 선택지로 관리 |
| `50_메인콘텐츠` | 맵·전선·적 조합별 영웅 조건부 고점 콘텐츠 |
| `60_UX_UI_접근성` | 원본 안정성·영웅 고점 조건·명시적 약점 비교 표시 |
| `99_변경이력` | GitHub path·HEAD·Sheet 범위·read-back·merge 결과 |

## 3. 현재 동기화 Decision

Decision: `OMW-DEC-20260802-GAMEPLAY-HERO-POWER-BUDGET-AND-SIDEGRADE-V1`

```text
Original Hero-grade archetype unit
= consistency + broad applicability + low setup requirement

Named Hero
= comparable average total combat budget
+ explicit conditional peak
+ unique tactical identity
- explicit weakness or opportunity cost
```

- 이름 지정 영웅은 원본 `[영웅]` 등급 병종의 순수 상위호환이 아니다.
- 대표 전투 상황 전체의 평균 총 전투 예산은 원본과 유사하게 유지한다.
- 영웅은 명확한 조건을 충족했을 때 원본보다 분명한 전술적 고점을 제공한다.
- 조건 불충족 시 안정성·범용성·지속력·대응 폭 중 하나 이상이 원본보다 낮아야 한다.
- 모든 영웅은 전술 정체성·고점 조건·고점 보상·명시적 약점·원본 병종 선택 사유·대응 압력을 정의한다.
- 피해·생존·사거리·제어·지원이 동시에 우세하고 실질적 약점이 없는 설계를 금지한다.
- DPS만 맞추고 제어·지원·기동성을 무료로 추가하는 우회도 금지한다.
- 같은 병종의 복수 영웅은 서로 다른 선택 조건과 약점을 가져야 한다.
- 원본 영웅 등급 병종은 높은 일관성·넓은 범용성·낮은 조건 의존도를 고유 장점으로 유지한다.
- 정확 전투 예산식·가중치·허용 편차·영웅별 수치는 simulation 전까지 pending이다.

## 4. 동기화 후보

```text
PR #121 candidate head before Sheet synchronization:
97454815fad711813fde41cd4f4eba9d56536945

SHEET_BOUNDED_READBACK: PENDING
REQUIRED_CI_AT_CANDIDATE_HEAD: PENDING
```

동기화 예정 범위:

- `00_프로젝트_허브!E2:L2`
- `01_작업순서!A24:N24`
- `02_현재_확정결정!A33:M33`
- `04_누락_충돌_감사!A97:H102`
- `05_GDD_요약!D8:J8`
- `05_GDD_요약!B9:J9`
- `12_핵심루프!A10:J10`
- `15_조작_게임규칙!A13:J13`
- `40_핵심시스템_메인콘텐츠!A13:J13`
- `41_성장_경제!A23:I23`
- `50_메인콘텐츠!A20:J20`
- `60_UX_UI_접근성!A21:J21`
- `99_변경이력!A34:H34`

## 5. 기존 승인 연결

- 영웅 변환은 `1토큰 → 1유닛`이며 보너스 유닛과 릴 odds 변경이 없다.
- 전장 전체 이름 지정 active 영웅은 최대 1명이다.
- 영웅은 수동 퇴각·교대할 수 없고 Stage·Act·정비시간에 동일 인스턴스로 유지된다.
- 생존 인스턴스의 HP·쿨다운·충전·고유 자원은 Stage 경계를 넘어 유지하고 일시 전투 상태는 제거한다.
- 사망한 인스턴스는 회수 보상을 제공하지 않으며 이름 지정 영웅 재출전에는 post-death token provenance가 필요하다.
- 영웅 해금은 모든 런에 적용되는 전역 강화가 아니라 조건부 전문화 후보를 Profile 명부에 추가한다.
- 기본 Profile과 원본 영웅 등급 병종만으로도 모든 콘텐츠 완료 가능성을 유지한다.

## 6. 동기화 절차

```text
사용자 승인
→ GitHub 분야 정본·관련 계약·Ledger·Map·Context 갱신
→ candidate commit
→ Sheet 결정·분야·감사·변경이력 갱신
→ bounded read-back
→ candidate HEAD·CI 확인
→ Workbook closure commit
→ final exact HEAD·CI·PR·review·changed-path 확인
→ 승인 10건 또는 사용자 지시 시 preflight·merge
→ main·Sheet 재검증
```

`PARTIAL_SYNC_BLOCKED`, `SYNC_CONFLICT`, `OPEN_P0_OR_P1`이면 다음 중요 Decision 또는 병합으로 진행하지 않는다.

## 7. 권위 매핑

| 의미 | GitHub 책임 원본 |
|---|---|
| 제품 코어 | `docs/PROJECT_CORE.md` |
| 현재 승인 Decision | `docs/PROJECT_CANON_DECISION_LEDGER.md` |
| 영웅 토큰 변환·배치 | `docs/design/APPROVED_OMENWARD_HERO_TOKEN_CONVERSION_AND_DEPLOYMENT_2026-08-02.md` |
| 영웅 단일 활성·반복 출전 | `docs/design/APPROVED_OMENWARD_HERO_SINGLE_ACTIVE_AND_REPEAT_DEPLOYMENT_2026-08-02.md` |
| 영웅 퇴각·교대·active 종료 | `docs/design/APPROVED_OMENWARD_HERO_EXIT_AND_REPLACEMENT_2026-08-02.md` |
| 영웅 Stage 상태 지속 | `docs/design/APPROVED_OMENWARD_HERO_STAGE_STATE_PERSISTENCE_2026-08-02.md` |
| 영웅 사망 무회수·post-death 결과·새 인스턴스 | `docs/design/APPROVED_OMENWARD_HERO_REDEPLOYMENT_INITIAL_STATE_2026-08-02.md` |
| 영웅 전투 예산·조건부 고점·전문화·약점 | `docs/design/APPROVED_OMENWARD_HERO_POWER_BUDGET_AND_SIDEGRADE_2026-08-02.md` |
| 현재 작업 | `docs/ACTIVE_CONTEXT.md` |
| 질문별 라우팅 | `docs/DOCUMENTATION_MAP.md` |

## 8. 금지

- 이름 지정 영웅을 원본 영웅 등급 병종의 무조건적 상위호환으로 설계.
- 피해·생존·사거리·제어·지원이 동시에 우세하고 약점이 없음.
- 명목상 조건이 대부분 자동 충족되어 사실상 상시 고점으로 작동.
- DPS만 같추고 제어·지원·기동성·유틸리티를 무료로 추가.
- 영웅 해금 뒤 원본 영웅 등급 병종의 합리적 선택 상황을 제거.
- 같은 병종의 한 영웅을 다른 영웅의 수치 상위 버전으로 제작.
- 약점을 설명문에만 적고 전투 규칙·수치·대응 관계에 반영하지 않음.
- 영웅 보유 자체가 전역 능력치·숨은 릴 확률·무료 병력을 제공.
- 승인 기획을 구현 완료·runtime 검증 완료로 표시.

## 9. 현재 상태

```text
SHEET_STATUS = READBACK_PENDING / CI_PENDING
BASELINE_MAIN = 12012f88bc1dc1d9aaaa538b578be3893e4b1591
GRILL_ME_COUNTER = 9_OF_10
NEXT_DECISION = OMW-DEC-20260802-GAMEPLAY-HERO-ABILITY-ACTIVATION-MODE-V1
PRODUCT_CODE = UNCHANGED
```