# 오멘워드 영웅 이상 등급 단일 활성·반복 출전 승인 계약

```yaml
decision_id: OMW-DEC-20260802-GAMEPLAY-HERO-UNIQUENESS-AND-ACTIVE-LIMIT-V1
approved_at: 2026-08-02 16:24 KST
refined_at: 2026-08-02 23:07 KST
status: USER_APPROVED / REFINED_TO_ALL_HERO_AND_LEGENDARY_GRADES / NOT_IMPLEMENTED
current_authority: OMW-DEC-20260802-GAMEPLAY-HERO-GRADE-SLOT-AND-UNLOCKED-SKILL-REPLACEMENT-V1
product_code_authority: NONE
simulation: NOT_RUN
runtime: NOT_RUN
human_validation: NOT_RUN
```

## 1. 전역 고등급 단일 활성

한 MapRun의 전장 전체에는 등급이 `[영웅]` 또는 `[전설]`인 유닛이 동시에 최대 1명만 존재할 수 있다.

```text
ACTIVE_UNIT_COUNT_WHERE_GRADE_IN(HERO, LEGENDARY) <= 1
```

제한 대상:

- 표준 `[영웅]` 등급 유닛.
- 해금 이름 지정 `[영웅]`.
- 표준 `[전설]` 등급 유닛.
- 향후 해금 이름 지정 `[전설]`.

제한하지 않는 대상:

- 일반 등급.
- 엘리트 등급.

- 상·중·하 전선 전체가 하나의 슬롯을 공유한다.
- 이름·병종·전선·표준/해금 여부를 바꾸어 우회할 수 없다.
- 과거 `이름 지정 해금 영웅만 전역 1명` 해석은 폐기한다.
- 과거 `이름 지정 영웅이 활성 중이어도 표준 영웅 배치 가능` 해석도 폐기한다.

## 2. 획득과 배치 분리

전역 슬롯은 룰렛 결과 생성·토큰 획득을 막지 않고 전장 배치만 제한한다.

```text
영웅 이상 등급 토큰 획득
→ 슬롯 비어 있음: 합법 후보 선택·변환·비가역 배치
→ 슬롯 차 있음: 보관 또는 판매
```

- 슬롯이 차 있어도 새 영웅·전설 결과는 정상 생성한다.
- 해당 토큰을 자동 소멸시키거나 낮은 등급으로 강제 변환하지 않는다.
- 현재 고등급 유닛을 자동 삭제하고 새 유닛으로 교체하지 않는다.
- 슬롯 충돌 상태와 보관·판매 선택을 UI에서 명확히 표시한다.

## 3. 슬롯 해제

```text
active_high_grade_unit_instance_id != null
→ 다른 [영웅]·[전설] 변환·배치 차단

active_high_grade_unit_instance_id == null
→ 합법적인 [영웅]·[전설] 후보 배치 가능
```

슬롯 해제 사건:

- 활성 고등급 유닛 사망·완전 제거.
- MapRun 승리·실패·중단 확정으로 전장 종료.

슬롯을 해제하지 않는 사건:

- Stage 종료.
- Act 전환.
- 정비시간 진입.
- Wave 종료.
- 플레이어의 수동 교체 요구.

- 살아 있는 고등급 유닛은 동일 전선·동일 인스턴스로 다음 Stage와 Act에 지속한다.
- 수동 퇴각·교대·판매·재보관·전선 이동은 금지한다.

## 4. 이름 지정 영웅 반복 출전

동일한 이름과 `hero_id`를 가진 해금 영웅은 한 MapRun에서 여러 번 출전할 수 있으나 동시에 둘 이상 존재할 수 없다.

```text
현재 고등급 active slot 비어 있음
+ 이전 이름 지정 영웅의 사망 이후 새로 생성된 동병종 [영웅] 등급 토큰
+ 해당 hero_id 해금
→ 같은 이름 지정 영웅 재출전 가능
```

- 반복 출전마다 별도 토큰 1개를 소비한다.
- `token.created_sequence > previous_named_hero.ended_sequence`를 만족한다.
- 사망 전에 보관한 토큰은 이름 지정 영웅 재출전에 사용할 수 없다.
- 사망 전 보관 토큰의 표준 영웅·전설 사용 가능 여부는 기존 공통 토큰 계약과 후속 Decision을 따른다.
- 새 인스턴스는 최대 HP·cooldown 기본 상태·초기 충전 상태로 시작한다.
- 이전 인스턴스의 HP·상태·누적 효과를 복제하지 않는다.

## 5. 표준 영웅·전설의 후속 배치 경계

최신 사용자는 동시 활성 수를 1명으로 확정했으며, 모든 교대·provenance 세부를 새로 확정한 것은 아니다.

따라서:

- 표준 영웅·전설도 슬롯이 차 있으면 배치할 수 없다.
- 슬롯이 빈 뒤 보관 토큰을 사용할 수 있는 세부 조건은 기존 공통 보관·배치 계약을 따른다.
- 이름 지정 영웅의 사망 후 재출전 provenance 규칙은 유지한다.
- 표준 영웅·전설까지 동일 post-death provenance를 의무화하지 않는다. 필요하면 별도 Decision으로 확정한다.

## 6. 등급·해금 스킬 연결

```text
표준 [영웅] = 강화 1스킬 + 표준 2스킬
해금 이름 지정 [영웅] = 강화 1스킬 + 고유 2스킬
표준 [전설] = 강화 1스킬 + 강화 표준 2스킬 + 표준 3스킬
향후 해금 이름 지정 [전설] = 강화 1스킬 + 강화 표준 2스킬 + 고유 3스킬
```

전역 슬롯은 위 네 유형 모두에 동일하게 적용한다.

## 7. Stage 지속 상태

살아 있는 고등급 유닛의 다음 상태는 Stage 경계를 넘어 유지한다.

- 현재 HP.
- 남은 cooldown.
- `READY_WAITING_FOR_VALID_CONDITION` 상태.
- 사용 횟수·충전·영속 고유 상태가 있을 경우 그 상태.
- active slot의 unit instance·grade·variant·lane 참조.

Stage 정산에서 제거하는 상태:

- 일시 버프·디버프.
- 현재 타깃·어그로.
- 진행 중 시전·투사체·장판.
- 일시 소환물.

정비시간에는 회복·cooldown·charge clock이 정지한다.

## 8. 데이터 방향

```yaml
HighGradeBattlefieldState:
  active_high_grade_unit_instance_id
  active_grade
  active_variant_type
  active_unit_archetype_id
  active_lane_id
  active_deployment_record_id

HighGradeDeploymentRecord:
  deployment_id
  source_token_instance_id
  grade
  variant_type
  named_variant_id
  unit_instance_id
  lane_id
  deployed_at_stage
  ended_at_stage
  ended_reason
  ended_sequence
```

- 슬롯 검증, 토큰 변환, 배치는 하나의 원자 transaction이어야 한다.
- 동시 입력·재시도·저장 복구로 고등급 유닛 둘이 생성되지 않게 한다.
- 사망·완전 제거 시 슬롯 해제와 종료 기록을 같은 transaction으로 처리한다.

## 9. 적대적 검토

| 공격 | 판정 | 보완 |
|---|---|---|
| 영웅이 살아 있는 중 전설 당첨을 사용할 수 없다 | 유효 | 결과 생성 유지·보관/판매·충돌 UI·경제 가치 검증 |
| 한 영웅이 오래 살아 이후 고등급 보상을 막는다 | 유효 | 평균 슬롯 점유시간·고등급 결과 충돌률·좌절도 측정 |
| 표준/해금 구분으로 두 명을 배치한다 | 금지 | grade 기반 전역 단일 슬롯 |
| 서로 다른 전선에 영웅과 전설을 각각 배치한다 | 금지 | 세 전선 전체 합산 |
| 더 좋은 유닛 획득 시 기존 영웅을 수동 교체한다 | 금지 | 비가역 커밋·수동 퇴각 금지 |
| 슬롯 충돌로 전설 토큰을 자동 삭제한다 | 금지 | 보관·판매 유지 |
| 모든 고등급에 post-death provenance를 소급 적용한다 | 미승인 | 이름 지정 재출전 규칙만 유지, 나머지는 후속 결정 |

## 10. 책임 계보

- 현행 슬롯·스킬 책임 원본: `APPROVED_OMENWARD_HERO_GRADE_SLOT_AND_UNLOCKED_SKILL_REPLACEMENT_2026-08-02.md`.
- Stage 상태: `APPROVED_OMENWARD_HERO_STAGE_STATE_PERSISTENCE_2026-08-02.md`.
- 이름 지정 영웅 재출전: `APPROVED_OMENWARD_HERO_REDEPLOYMENT_INITIAL_STATE_2026-08-02.md`.
- 자동 발동: `APPROVED_OMENWARD_HERO_ABILITY_ACTIVATION_MODE_2026-08-02.md`.

## 11. 구현 경계

```text
DESIGN = USER_APPROVED_HIGH_GRADE_SINGLE_ACTIVE
COUNTED_GRADES = HERO | LEGENDARY
COUNTED_VARIANTS = STANDARD | UNLOCKED_NAMED
SIMULTANEOUS_ACTIVE_HIGH_GRADE_UNITS = MAX_1
MANUAL_RETREAT_AND_REPLACEMENT = FORBIDDEN
STAGE_ACT_MAINTENANCE_TRANSITION = SAME_INSTANCE_REMAINS
ACTIVE_SLOT_CLEAR = UNIT_DEATH_OR_MAPRUN_END
NAMED_HERO_POST_DEATH_TOKEN_PROVENANCE = REQUIRED
STANDARD_HIGH_GRADE_PROVENANCE_EXTENSION = NOT_DECIDED
FUTURE_NAMED_LEGENDARY = NOT_NOW
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
PRODUCT_CODE = UNCHANGED
```
