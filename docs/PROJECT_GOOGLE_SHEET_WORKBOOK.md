# OMENWARD 프로젝트 Google Sheets Workbook

```yaml
updated_at: 2026-08-02
spreadsheet_id: 1VLwRtXGDtyj0JFt98wdIOtG6Zqc3wtdfCzSF9Fo6lpw
spreadsheet_title: 오멘워드(OMENWARD)
current_decision: OMW-DEC-20260802-GAMEPLAY-HERO-GRADE-SLOT-AND-UNLOCKED-SKILL-REPLACEMENT-V1
current_pr: 129
working_branch: gpt/omenward-hero-kit-planning-20260802
grill_me_count: 6_of_10
sheet_status: PROJECT_SHEET_CONFIGURED / SYNCED_TO_PR_129_HEAD / READBACK_PASS
workspace_mode: USER_FACING_GDD_WORKSPACE
change_protocol: PROPOSED_SHEET_CHANGE
exact_head_source: RESOLVE_FROM_PR_129_METADATA_AND_CONNECTED_SHEET
final_ci_source: RESOLVE_FROM_PR_129_BODY_AND_CONNECTED_SHEET
product_code_authority: NONE
```

## 1. 고정 Sheet 계약

```text
PROJECT_SHEET_CONFIGURED
USER_FACING_GDD_WORKSPACE
PROPOSED_SHEET_CHANGE
```

GitHub 기획 정본과 연결 Google Sheet는 같은 Decision ID와 같은 PR HEAD를 사용한다. `PROPOSED_SHEET_CHANGE`는 승인된 기획 변경을 같은 Decision ID로 기록하고 bounded read-back으로 검증하는 운영 계약이다.

Workbook 파일 자체에 현재 커밋 SHA를 고정하면 그 기록 커밋이 다시 HEAD를 이동시키므로, **최종 exact HEAD와 CI run은 Workbook 본문에 자기참조 방식으로 고정하지 않는다.** 실행 시점의 PR #129 메타데이터와 연결 Sheet `00_프로젝트_허브`, `02_현재_확정결정`, `05_GDD_요약`, `99_변경이력`에서 해석한다.

```text
USER_APPROVED_PLAN
!= PRODUCT_IMPLEMENTED
!= SIMULATION_VALIDATED
!= RUNTIME_VALIDATED
!= HUMAN_VALIDATED
```

## 2. 현행 Decision

```text
[영웅]·[전설] 등급 유닛은 표준/해금·병종·전선과 관계없이 전장 전체 최대 1명
해금 이름 지정 [영웅]은 표준 2스킬을 고유 2스킬로 교체
향후 해금 이름 지정 [전설]은 표준 3스킬을 고유 3스킬로 교체 / NOT_NOW
```

```text
STANDARD_HERO_POWER < UNLOCKED_NAMED_HERO_POWER < STANDARD_LEGENDARY_POWER
ACTIVE_UNIT_COUNT_WHERE_GRADE_IN(HERO, LEGENDARY) <= 1
NAMED_HERO_UNIQUE_SKILL_SLOT = 2
FUTURE_NAMED_LEGENDARY_UNIQUE_SKILL_SLOT = 3
```

## 3. 핵심 시스템·재미 연결

```text
예고된 공세
→ 건물·TokenSource로 릴 설계
→ 룰렛 조작·확정
→ 희귀 병력 획득
→ 세 전선 중 하나에 비가역 커밋
→ 전황 역전
→ 다음 설계
```

영웅 이상 전역 단일 슬롯은 최고 등급을 누적하는 것이 아니라 어느 전선에 최고 전력을 투입할지 판단하게 한다.

## 4. Sheet 반영·read-back 범위

- `00_프로젝트_허브!E2:L2`
- `01_작업순서!A33:N33`
- `02_현재_확정결정!A41:M41`
- `04_누락_충돌_감사!A153:H162`
- `05_GDD_요약!D8:J8`
- `05_GDD_요약!B9:J9`
- `12_핵심루프!A17:J17`
- `15_조작_게임규칙!A20:J20`
- `40_핵심시스템_메인콘텐츠!A20:J20`
- `41_성장_경제!A30:I30`
- `50_메인콘텐츠!A27:J27`
- `60_UX_UI_접근성!A28:J28`
- `70_아트_오디오_에셋!A11:J11`
- `99_변경이력!A43:H43`

쓰기 전 빈 행·서식을 확인하고, 쓰기 뒤 같은 범위를 읽어 다음을 확인한다.

```text
SAME_DECISION_ID = PASS
SHEET_BOUNDED_READBACK = PASS
EXACT_PR_HEAD_MATCH = PASS
HIGH_GRADE_CAP_1 = PRESENT
NAMED_HERO_UNIQUE_SKILL_2_REPLACEMENT = PRESENT
FUTURE_NAMED_LEGENDARY_SKILL_3_NOT_NOW = PRESENT
POWER_HIERARCHY = PRESENT
```

## 5. Sheet 핵심 불변식

```text
HIGH_GRADE_ACTIVE_CAP = 1
COUNTED_GRADES = HERO | LEGENDARY
COUNTED_VARIANTS = STANDARD | UNLOCKED_NAMED
SCOPE = ALL_THREE_LANES
LIMIT_APPLIES_TO = BATTLEFIELD_DEPLOYMENT
TOKEN_ACQUISITION_WHEN_SLOT_FULL = ALLOWED
STORE_OR_SELL_WHEN_SLOT_FULL = ALLOWED
AUTO_DELETE_OR_AUTO_REPLACE = FORBIDDEN
```

```text
STANDARD_HERO = UPGRADED_SKILL_1 + STANDARD_SKILL_2
UNLOCKED_NAMED_HERO = UPGRADED_SKILL_1 + UNIQUE_SKILL_2
STANDARD_LEGENDARY = UPGRADED_SKILL_1 + UPGRADED_STANDARD_SKILL_2 + STANDARD_SKILL_3
FUTURE_UNLOCKED_NAMED_LEGENDARY = UPGRADED_SKILL_1 + UPGRADED_STANDARD_SKILL_2 + UNIQUE_SKILL_3
```

## 6. 적대적 검토 기록

- OMW-AUD-153: named-only 제한과 최신 전 등급 제한 충돌.
- OMW-AUD-154: 고유 스킬 추가가 전설 계층 침범.
- OMW-AUD-155: 전설 잭팟의 즉시 배치 불가 좌절.
- OMW-AUD-156: 영웅 결과 빈도·장기 슬롯 점유·보관함 압력.
- OMW-AUD-157: 해금 후 표준 영웅 완전 대체는 의도된 수직 성장.
- OMW-AUD-158: 고유 2스킬이 표준 전설 전체 키트를 넘는 위험.
- OMW-AUD-159: 단일 고등급 슬롯이 세 전선 다양성을 축소할 위험.
- OMW-AUD-160: 수동 교체가 비가역 커밋 훼손.
- OMW-AUD-161: 미래 해금 전설 범위 폭증.
- OMW-AUD-162: cooldown 완료 즉시 낭비 발동.

## 7. 자동 발동

```text
COOLDOWN
→ READY_WAITING_FOR_VALID_CONDITION
→ trigger·target·priority·tie-break
→ CAST_COMMIT
→ effect·VFX/SFX·log
→ COOLDOWN
```

유효 조건이 없으면 준비 상태를 유지한다.

## 8. exact-head 검증 절차

```text
1. PR #129 actual head 조회
2. latest main 대비 compare에서 behind 0 확인
3. changed paths가 docs-only이고 product paths 0인지 확인
4. actual head의 필수 CI 3개 Green 확인
5. comments·reviews·unresolved threads 확인
6. Sheet OPEN_P0·OPEN_P1·MERGE_BLOCKER 검색
7. Sheet의 exact SHA·CI run·status를 actual head에 맞춰 기록
8. bounded read-back으로 SHA와 status 확인
9. PR 설명에 동일 증거 기록
```

최종 증거는 PR #129 설명과 연결 Sheet가 소유한다. Workbook은 검증 방법과 반영 범위만 소유한다.

## 9. 실패·교정 계보

첫 후보에서 GDD Sheet CI가 실패한 원인은 설계 내용이 아니라 Workbook의 고정 표식 `PROJECT_SHEET_CONFIGURED` 누락이었다. 테스트 계약을 확인해 다음 표식을 복원했다.

```text
PROJECT_SHEET_CONFIGURED
USER_FACING_GDD_WORKSPACE
PROPOSED_SHEET_CHANGE
```

후속 exact-head 검증에서는 이 표식과 실제 Sheet 동기화를 모두 확인한다.

## 10. 구현 경계

```text
CURRENT_PRODUCT = LEGACY_PROTOTYPE
PRODUCT_CODE = UNCHANGED
EXACT_UNIQUE_SKILL_2 = PENDING
FUTURE_NAMED_LEGENDARY = NOT_NOW
EXACT_VALUES = PENDING
ASSETS = NOT_CREATED
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
```

## 11. 최종 검증 체크리스트

- [ ] PR actual HEAD와 Sheet SHA 동일.
- [ ] 같은 Decision ID.
- [ ] bounded read-back PASS.
- [ ] 필수 CI 3개 actual HEAD Green.
- [ ] latest main 대비 behind 0.
- [ ] changed paths docs-only.
- [ ] 제품 경로 0.
- [ ] comments·reviews·unresolved threads 0 또는 해결.
- [ ] Sheet `OPEN_P0`, `OPEN_P1`, `MERGE_BLOCKER` 0.
- [ ] PR #129 Draft 유지, 카운터 6/10.

## 12. 다음 Gate

```text
OMW-DEC-20260802-GAMEPLAY-HERO-FIRST-FIVE-UNIQUE-SKILL-2-CONCEPTS-V1
```
