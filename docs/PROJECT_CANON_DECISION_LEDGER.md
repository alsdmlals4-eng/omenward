# 오멘워드 기획 정본 결정 원장

```yaml
updated_at: 2026-08-02
status: CURRENT_DECISION_LEDGER / ACTIVE_PLANNING_BRANCH
current_recovery_decision: OMW-DEC-20260802-CANON-RECOVERY-V1
current_planning_decision: OMW-DEC-20260802-GAMEPLAY-HERO-SIGNATURE-DELTA-BALANCE-V1
current_world_decision: OMW-DEC-20260802-WORLD-VEILSPECIES-PURPOSE-V1
current_operating_decision: OMW-DEC-20260802-GRILL-ME-MERGE-CADENCE-V1
current_main: RESOLVE_FROM_REPOSITORY_DEFAULT_BRANCH
working_branch: gpt/omenward-hero-kit-planning-20260802
current_planning_pr: 129
active_base: 9.4.3
product_code_authority: NONE
sheet_id: 1VLwRtXGDtyj0JFt98wdIOtG6Zqc3wtdfCzSF9Fo6lpw
grill_me_approved_since_last_merge: 2
future_merge_cadence: 10_APPROVED_GRILL_ME_DECISIONS
planning_docs_merge_policy: AUTO_PROCEED_AFTER_GREEN_PREFLIGHT_UNDER_STANDING_USER_AUTHORIZATION
product_code_merge_policy: SEPARATE_CONTRACT_REQUIRED
preflight: NEXT_AT_10_OF_10
next_gate: OMW-DEC-20260802-GAMEPLAY-HERO-INITIAL-ROSTER-SCOPE-V1
```

`current_main`은 저장소 기본 브랜치에서 실행 시점에 해석한다. 이 문서는 현재 승인 Decision과 다음 10건 카운터를 소유한다.

## 1. 상태 언어

```text
USER_APPROVED_PLAN
!= PRODUCT_IMPLEMENTED
!= AUTOMATED_VALIDATED
!= HUMAN_VALIDATED
!= RELEASE_READY
```

## 2. 현재 묶음 Decision 2/10

| Decision ID | 상태 | 결정 | 책임 원본 | 미완료 경계 |
|---|---|---|---|---|
| `OMW-DEC-20260802-GAMEPLAY-HERO-SIGNATURE-DELTA-BALANCE-V1` | `USER_APPROVED / ACTIVE_BRANCH_SYNCED / NOT_IMPLEMENTED` | 이름 지정 영웅은 원본 `[영웅]` 등급 병종 데이터를 우선 복사하고 단일 패시브 또는 자동 사용스킬의 가치와 직접 관련된 상쇄 축 하나만 하향·조건화하며 나머지 원본 데이터는 유지한다 | `design/APPROVED_OMENWARD_HERO_SIGNATURE_DELTA_BALANCE_2026-08-02.md` | 정확 상쇄 축·수치·허용 편차·simulation pending |
| `OMW-DEC-20260802-GAMEPLAY-HERO-ABILITY-KIT-STRUCTURE-V1` | `USER_APPROVED / ACTIVE_BRANCH_SYNCED / NOT_IMPLEMENTED` | 이름 지정 영웅은 기존 병종 `[영웅]` 등급 유닛을 기반으로 한 스킨형 변주이며, 영웅 전용 차이는 패시브 1개 또는 자동 `[사용스킬]` 1개 중 정확히 하나만 가진다 | `design/APPROVED_OMENWARD_HERO_ABILITY_KIT_STRUCTURE_2026-08-02.md` | 실제 영웅 명단·단일 차이 효과·자산 범위·simulation pending |

## 3. 영웅 단일 차이·상쇄 계약

```text
기존 병종 [영웅] 등급 유닛
+ 스킨·이름·최소 식별 연출
+ PASSIVE XOR AUTOMATIC_ACTIVE_SKILL
- 직접 관련된 상쇄 축 1개
= 이름 지정 영웅
```

```text
SIGNATURE_DELTA_COUNT = 1
COMPENSATION_AXIS_COUNT = 1
COMPENSATION_MUST_BE_CAUSALLY_RELATED = TRUE
ALL_OTHER_SOURCE_AXES_INHERITED = TRUE
```

- 원본 병종의 역할·기본 공격·사거리·이동·AI·리그·기본 애니메이션을 우선 재사용한다.
- 패시브와 영웅 전용 사용스킬을 동시에 제공하지 않는다.
- `[사용스킬]`은 수동 버튼이 아니라 규칙 기반 자동 발동이다.
- 고유 자원·궁극기·새 AI·전체 신규 리그·전체 신규 애니메이션은 기본 금지다.
- 단일 차이의 전투 가치는 그 효과와 직접 관련된 능력치·효율·조건 축 하나에서만 상쇄한다.
- 여러 스탯 동시 조정·전체 성장 곡선 재설계·모든 영웅 공통 세금은 금지한다.
- 원본 병종이 더 나은 대표 상황을 유지한다.

## 4. 기존 main 정본 연결

PR #121에서 승인된 다음 계약은 계속 유지한다.

- 영웅 해금·동병종 바인딩·복수 동병종 영웅.
- 동병종 `[영웅]` 토큰의 원본 또는 이름 지정 영웅 1:1 변환.
- 세 전선 전체 이름 지정 영웅 최대 1명.
- 수동 퇴각·교대·판매·재보관·전선 이동 금지.
- Stage 경계 상태 지속과 사망 후 새 적격 토큰 재출전.
- 원본 병종과 유사 평균 전투 예산의 조건부 전문화 sidegrade.
- 이름 지정 영웅 능력의 규칙 기반 자동 발동·결정론·save reroll 금지.

## 5. 충돌 해소

- 이전 초안의 `고유 특성 1 + 자동 능력 1` 동시 보유 구조는 폐기했다.
- 원본 스탯을 그대로 유지한 무료 능력 추가는 금지한다.
- 여러 스탯을 조금씩 조정해 사실상 신규 유닛으로 만드는 것도 금지한다.
- 상쇄 축은 능력 가치와 직접 관련돼야 하며 형식적 약점은 허용하지 않는다.
- `스킨형`은 장식 전용을 뜻하지 않으며 실제 전술 선택을 바꾸는 차이 하나가 필요하다.

## 6. 구현·검증 경계

```text
CURRENT_PRODUCT = LEGACY_PROTOTYPE
LATEST_APPROVED = DOCUMENTED_NOT_IMPLEMENTED
PRODUCT_CODE_AUTHORITY = NONE
EXACT_HERO_VARIANTS = PENDING
EXACT_VALUES = PENDING
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
```

## 7. 카운터·병합 규칙

```text
CURRENT_COUNT_SINCE_MERGE = 2_OF_10
NEXT_PREFLIGHT_AT = 10_OF_10
```

- 승인 즉시 GitHub·Sheet에 같은 Decision ID로 반영한다.
- 10번째 승인 뒤 문서·기획 PR이 Green preflight와 blocker 0을 만족하면 별도 승인 대기 없이 병합한다.
- 제품 코드 구현·병합은 별도 계약 대상이다.
