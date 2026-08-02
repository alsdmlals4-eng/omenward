# OMENWARD 프로젝트 Google Sheets Workbook

```yaml
updated_at: 2026-08-03
spreadsheet_id: 1VLwRtXGDtyj0JFt98wdIOtG6Zqc3wtdfCzSF9Fo6lpw
spreadsheet_title: 오멘워드(OMENWARD)
current_decision: OMW-DEC-20260803-GAMEPLAY-HERO-FIRST-FIVE-UNIQUE-SKILL-2-CONCEPTS-V1
current_process_policy: OMW-PROC-20260803-GRILL-ME-BENCHMARK-PRODUCTION-COMPARISON-V1
current_pr: 129
working_branch: gpt/omenward-hero-kit-planning-20260802
grill_me_count: 7_of_10
sheet_status: PROJECT_SHEET_CONFIGURED / SYNC_IN_PROGRESS
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

Workbook 파일 자체에 현재 커밋 SHA를 고정하면 그 기록 커밋이 다시 HEAD를 이동시키므로, 최종 exact HEAD와 CI run은 Workbook 본문에 자기참조 방식으로 고정하지 않는다. 실행 시점의 PR #129 메타데이터와 연결 Sheet `00_프로젝트_허브`, `02_현재_확정결정`, `05_GDD_요약`, `99_변경이력`에서 해석한다.

```text
USER_APPROVED_PLAN
!= PRODUCT_IMPLEMENTED
!= SIMULATION_VALIDATED
!= RUNTIME_VALIDATED
!= HUMAN_VALIDATED
```

## 2. 현행 제품 Decision

```text
shield_guard / 방패병 → 불퇴의 성벽
archer / 궁병         → 천공 소거
priest / 사제         → 생명의 서약
mage / 마법사         → 메테오
assassin / 암살자     → 그림자 분신
```

```text
ONE_UNIQUE_SKILL_2
ONE_LANE
ONE_PRIMARY_TACTICAL_PURPOSE
AUTOMATIC_RULE_BASED_ACTIVATION
READY_STATE_PRESERVED_UNTIL_VALID_CONDITION
STANDARD_HERO_POWER < UNLOCKED_NAMED_HERO_POWER < STANDARD_LEGENDARY_POWER
```

- `생명의 서약`은 회복이 아니라 짧은 체력 하한 보호다.
- `메테오`는 deterministic 적 밀집 지점에 예고 후 메테오 1개가 지연 낙하한다.
- `그림자 분신`은 독립 AI 없이 원본 표적과 기본 공격 일부만 복제하는 owner-bound proxy 1체다.
- 정확 trigger·cooldown·duration·damage·floor·clone coefficient·최종 표시 이름은 pending이다.

## 3. 상위 등급·전역 슬롯 계보

```text
[영웅]·[전설] 등급 유닛은 표준/해금·병종·전선과 관계없이 전장 전체 최대 1명
해금 이름 지정 [영웅]은 표준 2스킬을 고유 2스킬로 교체
향후 해금 이름 지정 [전설]은 표준 3스킬을 고유 3스킬로 교체 / NOT_NOW
재전설 결과는 같은 계열 [영웅] 보상 토큰 2개 / 즉시 유닛 생성 0
```

```text
ACTIVE_UNIT_COUNT_WHERE_GRADE_IN(HERO, LEGENDARY) <= 1
```

## 4. Grill Me 벤치마크·현업 비교 정책

Process ID:

`OMW-PROC-20260803-GRILL-ME-BENCHMARK-PRODUCTION-COMPARISON-V1`

앞으로 모든 Grill Me 질문과 승인 작업은 다음을 포함한다.

1. Project Core·현행 APPROVED 문서 근거.
2. 공식 상용 게임·개발 자료 중심 직접 사례 2~4개.
3. OMENWARD와의 장르·조작·전투 규모 차이.
4. 구현·데이터·AI·pathfinding·animation·VFX/SFX·UI·save/load·determinism·QA 비용.
5. 적대적 검토와 복제 금지 경계.
6. 2~4개 선택지와 제작비·검증비·권장안.

이 운영 정책은 제품 Grill Me 카운터를 별도로 증가시키지 않는다.

## 5. Sheet 반영·read-back 범위

- `00_프로젝트_허브!E2:L2`
- `01_작업순서!A34:N35`
- `02_현재_확정결정!A42:M43`
- `03_근거_라이브러리!A12:J18`
- `04_누락_충돌_감사!A164:H172`
- `05_GDD_요약!D8:J8`
- `05_GDD_요약!B9:J9`
- `12_핵심루프!A18:J18`
- `15_조작_게임규칙!A21:J21`
- `40_핵심시스템_메인콘텐츠!A21:J21`
- `41_성장_경제!A31:I31`
- `50_메인콘텐츠!A28:J28`
- `60_UX_UI_접근성!A29:J29`
- `70_아트_오디오_에셋!A12:J12`
- `99_변경이력!A45:H46`

쓰기 전 빈 행·서식을 bounded read로 확인했고, 쓰기 뒤 같은 범위를 다시 읽어 다음을 확인한다.

```text
SAME_DECISION_ID = PASS
PROCESS_POLICY_ID_PRESENT = PASS
BENCHMARK_EVIDENCE_ROWS = PRESENT
SHEET_BOUNDED_READBACK = PASS
EXACT_PR_HEAD_MATCH = PASS
FIRST_FIVE_SKILL_CONCEPTS = PRESENT
COUNTER_7_OF_10 = PRESENT
```

## 6. 초기 5명 Sheet 불변식

```text
SHIELD_GUARD = NON_TERRAIN_DAMAGE_ABSORPTION_BARRIER
ARCHER = SAME_LANE_VALID_FLYING_TARGET_VOLLEY
PRIEST = TEMPORARY_HEALTH_FLOOR_NO_HEALING
MAGE = TELEGRAPHED_DELAYED_SINGLE_METEOR
ASSASSIN = ONE_OWNER_BOUND_DEPENDENT_CLONE_PROXY
```

```text
PRIEST_EFFECTIVE_FLOOR
= min(current_hp_at_cast, configured_floor_percent * max_hp)
```

```text
ASSASSIN_CLONE_COUNT = 1
INDEPENDENT_TARGET_SELECTION = FALSE
INDEPENDENT_PATHFINDING = FALSE
SKILL_CASTING = FALSE
ON_HIT_AND_CC_COPY = FALSE
RESOURCE_OR_REWARD_GENERATION = FALSE
HIGH_GRADE_SLOT_OCCUPANCY = FALSE
```

## 7. 근거 라이브러리

`03_근거_라이브러리`에는 다음 공식 자료를 기록한다.

- Riot Games `Clarity in League`.
- Riot Games `Quick Gameplay Thoughts: Champion Counterplay`.
- Riot Games `Braum`.
- Blizzard Entertainment `Rain of Vengeance`.
- Riot Games / Wild Rift `Kindred`.
- Riot Games / Wild Rift `Meteor Enchant` patch notes.
- Riot Games `Zed`.

이 자료는 정확 수치 권위가 아니라 가독성·counterplay·telegraph·proxy 제작 경계를 비교하는 `REFERENCE_ONLY / ADAPT / DO_NOT_COPY` 근거다.

## 8. 적대적 검토 기록

- OMW-AUD-164: 체력 하한이 한 전선 전체 무적으로 변할 위험.
- OMW-AUD-165: 체력 하한이 낮은 대상에게 숨은 회복을 제공할 위험.
- OMW-AUD-166: 메테오 즉발로 대응 불가능해질 위험.
- OMW-AUD-167: 메테오가 지나치게 빗나가 해금 보상이 사라질 위험.
- OMW-AUD-168: 분신이 독립 AI 유닛으로 팽창할 위험.
- OMW-AUD-169: 분신이 스킬·on-hit·CC까지 복제할 위험.
- OMW-AUD-170: 방벽이 navmesh를 변경할 위험.
- OMW-AUD-171: 천공 소거가 비행 Wave를 혼자 무조건 삭제할 위험.
- OMW-AUD-172: 고유 스킬 VFX가 전장 가독성을 파괴할 위험.

## 9. exact-head 검증 절차

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

## 10. 구현 경계

```text
CURRENT_PRODUCT = LEGACY_PROTOTYPE
PRODUCT_CODE = UNCHANGED
UNIQUE_SKILL_2_CONCEPTS = APPROVED
EXACT_TRIGGER_THRESHOLDS = PENDING
EXACT_COOLDOWNS = PENDING
EXACT_DURATIONS_AND_VALUES = PENDING
FINAL_DISPLAY_NAMES = PENDING
ASSETS = NOT_CREATED
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
```

## 11. 최종 검증 체크리스트

- [ ] PR actual HEAD와 Sheet SHA 동일.
- [ ] 같은 Decision ID와 Process ID.
- [ ] bounded read-back PASS.
- [ ] 필수 CI 3개 actual HEAD Green.
- [ ] latest main 대비 behind 0.
- [ ] changed paths docs-only.
- [ ] 제품 경로 0.
- [ ] comments·reviews·unresolved threads 0 또는 해결.
- [ ] Sheet `OPEN_P0`, `OPEN_P1`, `MERGE_BLOCKER` 0.
- [ ] PR #129 Draft 유지, 카운터 7/10.

## 12. 다음 Gate

```text
OMW-DEC-20260803-GAMEPLAY-HERO-UNIQUE-SKILL-2-COOLDOWN-CHARGE-AND-FAILURE-POLICY-V1
```
