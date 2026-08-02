# OMENWARD 프로젝트 Google Sheets Workbook

```yaml
updated_at: 2026-08-02
spreadsheet_id: 1VLwRtXGDtyj0JFt98wdIOtG6Zqc3wtdfCzSF9Fo6lpw
spreadsheet_title: 오멘워드(OMENWARD)
current_decision: OMW-DEC-20260802-GAMEPLAY-HERO-GRADE-SLOT-AND-UNLOCKED-SKILL-REPLACEMENT-V1
current_pr: 129
working_branch: gpt/omenward-hero-kit-planning-20260802
grill_me_count: 6_of_10
sheet_status: SYNC_IN_PROGRESS
product_code_authority: NONE
```

## 1. 동기화 목적

GitHub 기획 정본과 연결 Google Sheet가 같은 Decision ID·같은 PR head·같은 상태 언어를 사용하도록 유지한다.

```text
USER_APPROVED_PLAN
!= PRODUCT_IMPLEMENTED
!= SIMULATION_VALIDATED
!= RUNTIME_VALIDATED
!= HUMAN_VALIDATED
```

## 2. 현행 Decision 요약

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

## 4. Sheet 반영 범위

이번 Decision에서 다음 범위를 사용한다.

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

쓰기 전 다음 빈 행과 기존 서식을 bounded read로 확인한다. 쓰기 뒤 같은 범위를 다시 읽어 값·Decision ID·PR SHA를 검증한다.

## 5. Sheet에 기록할 핵심 불변식

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

Sheet 감사 탭에 다음을 기록한다.

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

## 7. 자동 발동 Sheet 표현

```text
COOLDOWN
→ READY_WAITING_FOR_VALID_CONDITION
→ trigger·target·priority·tie-break
→ CAST_COMMIT
→ effect·VFX/SFX·log
→ COOLDOWN
```

유효 조건이 없으면 준비 상태를 유지한다.

## 8. 구현·검증 경계

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

## 9. 최종 검증 체크리스트

- [ ] GitHub와 Sheet에 같은 Decision ID.
- [ ] Sheet에 exact PR head SHA.
- [ ] bounded read-back PASS.
- [ ] 필수 CI 3개 exact HEAD Green.
- [ ] latest main 대비 behind 0.
- [ ] changed paths가 문서 전용.
- [ ] 제품 경로 0.
- [ ] PR comments·reviews·unresolved threads 0 또는 해결.
- [ ] Sheet `OPEN_P0`, `OPEN_P1`, `MERGE_BLOCKER` 0.
- [ ] PR #129 Draft 유지, 카운터 6/10.

## 10. 다음 Gate

```text
OMW-DEC-20260802-GAMEPLAY-HERO-FIRST-FIVE-UNIQUE-SKILL-2-CONCEPTS-V1
```
