# OMENWARD 초기 이름 지정 영웅 병종 선정 승인안

```yaml
decision_id: OMW-DEC-20260802-GAMEPLAY-HERO-INITIAL-ROSTER-ARCHETYPE-SELECTION-V1
approved_at: 2026-08-02 22:10 KST
approval: USER_DIRECT_SELECTION
status: USER_APPROVED / ACTIVE_PLANNING_BRANCH / NOT_IMPLEMENTED
scope: GAMEPLAY_HERO_INITIAL_ROSTER_ARCHETYPE_SELECTION
supersedes_roster_count_in: OMW-DEC-20260802-GAMEPLAY-HERO-INITIAL-ROSTER-SCOPE-V1
parent_kit_decision: OMW-DEC-20260802-GAMEPLAY-HERO-ABILITY-KIT-STRUCTURE-V1
parent_balance_decision: OMW-DEC-20260802-GAMEPLAY-HERO-SIGNATURE-DELTA-BALANCE-V1
product_code_authority: NONE
exact_hero_identities: PENDING
exact_signature_effects: PENDING
exact_compensation_axes: PENDING
assets: NOT_CREATED
simulation: NOT_RUN
runtime_validation: NOT_RUN
human_validation: NOT_RUN
```

## 1. 사용자 수정과 최종 범위

사용자는 이전 초기 로스터 4명 권장안을 다음 다섯 병종으로 직접 확장·수정했다.

```text
shield_guard / 방패병
archer / 궁병
priest / 사제
mage / 마법사
assassin / 암살자
```

따라서 현재 초기 제작·검증 로스터는 **서로 다른 기존 UnitArchetype 5종에 이름 지정 영웅 1명씩, 총 5명**이다.

```text
INITIAL_NAMED_HERO_COUNT = 5
INITIAL_SOURCE_ARCHETYPE_COUNT = 5
HEROES_PER_SOURCE_ARCHETYPE = 1
DUPLICATE_SOURCE_ARCHETYPE_IN_INITIAL_ROSTER = FORBIDDEN
INITIAL_ROSTER_IS_FINAL_RELEASE_CAP = FALSE
```

이 Decision은 이전 `OMW-DEC-20260802-GAMEPLAY-HERO-INITIAL-ROSTER-SCOPE-V1`의 `4명·4병종·2:2` 수량 부분을 대체한다. 스킨형 제작·단일 차이·단일 상쇄 축·최종 출시 상한 아님 등 나머지 원칙은 유지한다.

## 2. 병종·역할·현행 데이터 근거

| 순서 | archetype_id | 표시명 | 현행 role | 대표 타기팅·상성 | 초기 검증 목적 |
|---:|---|---|---|---|---|
| 1 | `shield_guard` | 방패병 | `frontline` | `nearest`, `ranged_defense` | 전열 유지·점령·원거리 방어 |
| 2 | `archer` | 궁병 | `ranged` | `flying`, `nearest`, `anti_air` | 지속 원거리·대공·우선순위 |
| 3 | `priest` | 사제 | `support` | `lowest_health_ally`, `sustain` | 아군 타기팅·치유·지원 |
| 4 | `mage` | 마법사 | `ranged` | `cluster`, `nearest`, `frontline_cluster` | 군집 판단·광역·제어 |
| 5 | `assassin` | 암살자 | `bypass` | `backline` | 후열 침투·우선 대상 제거 |

현행 `data/units/*.tres`와 `data/bootstrap_catalog.tres`에 다섯 archetype의 전투 Profile·attack profile·animation contract·진영 visual profile 연결이 존재한다. 이 문서는 해당 현행 ID를 정본 ID로 사용한다.

## 3. 능력 유형 배정

다섯 병종의 역할과 기존 타기팅 문법에 맞춰 다음을 초기 설계 방향으로 고정한다.

```text
PASSIVE_VARIANT_COUNT = 3
AUTOMATIC_ACTIVE_SKILL_VARIANT_COUNT = 2
```

| archetype_id | 능력 유형 | 이유 |
|---|---|---|
| `shield_guard` | `PASSIVE` | 전열 유지·피해 대응·인접 보호 같은 지속 조건을 단순하게 검증 |
| `archer` | `PASSIVE` | 대공·표적 누적·거리 조건 등 기본 공격 기반 변주에 적합 |
| `assassin` | `PASSIVE` | 후열·첫 타격·표식 대상 조건을 별도 수동 스킬 없이 검증 |
| `priest` | `AUTOMATIC_ACTIVE_SKILL` | 부상 아군 탐색·대상 재검증·cooldown·tie-break 검증에 적합 |
| `mage` | `AUTOMATIC_ACTIVE_SKILL` | 군집 탐색·광역 위치·cooldown·유효 대상 재검증에 적합 |

```text
PASSIVE_ARCHETYPES = [shield_guard, archer, assassin]
AUTOMATIC_ACTIVE_ARCHETYPES = [priest, mage]
```

구체 패시브·사용스킬 효과와 관련 상쇄 축은 별도 후속 Decision 전까지 확정하지 않는다.

## 4. 검증 커버리지

이 다섯 병종은 다음 타기팅과 전투 판단을 함께 검증한다.

```text
shield_guard → nearest enemy / frontline sustain
archer       → flying first, then nearest
priest       → lowest-health ally
mage         → enemy cluster, then nearest
assassin     → enemy backline
```

검증 축:

- 적 최근접 대상.
- 비행 우선 대상.
- 아군 체력 기반 대상.
- 적 군집 기반 대상.
- 적 후열 우선 대상.
- 전열·원거리·지원·광역 제어·우회 역할.
- 패시브형 3명과 자동 사용스킬형 2명의 제작량·가독성·밸런스 차이.

## 5. 스킨형 제작 계약

각 영웅은 원본 병종에서 다음을 우선 재사용한다.

- 역할·기본 공격·사거리·이동.
- AI와 target priority 기본 구조.
- 리그·기본 애니메이션·피격·사망.
- 투사체·충돌·전선 이동·공통 UI.

신규 제작은 이름·초상·스킨·장비 또는 실루엣·머티리얼·단일 차이용 최소 VFX/SFX에 집중한다.

```text
FIVE_FULL_NEW_UNITS = FORBIDDEN
FIVE_SKIN_LIKE_TACTICAL_VARIANTS = REQUIRED
```

## 6. 단일 차이·상쇄 계약

각 영웅은 다음 불변식을 유지한다.

```text
signature_delta_count == 1
signature_delta_type == PASSIVE XOR AUTOMATIC_ACTIVE_SKILL
compensation_axis_count == 1
compensation_axis_is_related == true
all_other_source_axes_inherited == true
```

- 무료 능력 추가를 금지한다.
- 여러 스탯 동시 하향과 전체 성장 곡선 재설계를 금지한다.
- 원본 병종이 더 나은 대표 상황을 병종마다 최소 하나 유지한다.
- 다섯 영웅이 동일한 상쇄 패턴에 편중되지 않도록 후속 설계에서 검토한다.

## 7. 적대적 검토

| 공격 | 판정 | 보완 |
|---|---|---|
| 4명 승인과 5명 선정이 충돌한다 | 유효 | 사용자 최신 직접 수정이 수량 부분을 명시적으로 대체 |
| 후열 병종이 궁병·사제·마법사로 편중된다 | 유효 | 타기팅은 대공·아군·군집으로 분리하고 콘텐츠 노출을 별도 검증 |
| 마법사와 궁병이 둘 다 ranged라 역할이 겹친다 | 유효 | 궁병은 지속 화력·대공, 마법사는 군집·광역 자동 스킬로 분리 |
| 암살자 패시브가 기존 후열 우선 규칙과 구별되지 않을 수 있다 | 유효 | 후속 능력은 실제 선택을 바꾸는 단일 조건·보상·상쇄를 요구 |
| 방패병 패시브가 무료 방어력 증가가 될 수 있다 | 유효 | 직접 관련 상쇄 축과 원본 우위 상황 필수 |
| 사제·마법사 자동 스킬이 동시에 복잡한 타기팅 오류를 만든다 | 유효 | ally-lowest-health와 enemy-cluster 테스트를 분리하고 결정론 검증 |
| 5명으로 늘면서 자산 범위가 과도해진다 | 유효 | 완전 신규 유닛 금지, 원본 자산 재사용률과 병종별 제작시간 측정 |
| 5명이 최종 출시 전부로 오해될 수 있다 | 유효 | 초기 검증 로스터이며 확장 상한은 미확정 |

## 8. 금지

- 거인·기병 등 사용자가 선택하지 않은 병종을 초기 5명에 자동 추가.
- 동일 병종 복수 영웅.
- 사제·마법사에 수동 사용 버튼 추가.
- 암살자·궁병·방패병에 패시브와 사용스킬 동시 제공.
- 완전 신규 리그·전체 애니메이션·별도 AI 구조를 기본 전제로 설계.
- 초기 5명을 출시 전체 로스터 상한으로 해석.
- 구체 영웅 이름·스킬·상쇄 수치를 승인 없이 확정.

## 9. 후속 결정

다음 Decision은 다섯 영웅의 **전술 정체성과 단일 차이 방향**을 한 명씩 설계하는 것이다.

```text
NEXT_GATE = OMW-DEC-20260802-GAMEPLAY-HERO-FIRST-FIVE-SIGNATURE-CONCEPTS-V1
```

## 10. 구현 경계

```text
USER_APPROVED = TRUE
GITHUB_AUTHORITY = THIS_DOCUMENT
INITIAL_NAMED_HERO_COUNT = 5
INITIAL_SOURCE_ARCHETYPE_COUNT = 5
EXACT_ARCHETYPES = [shield_guard, archer, priest, mage, assassin]
PASSIVE_VARIANT_COUNT = 3
AUTOMATIC_ACTIVE_SKILL_VARIANT_COUNT = 2
EXACT_HERO_IDENTITIES = PENDING
EXACT_SIGNATURE_EFFECTS = PENDING
EXACT_COMPENSATION_AXES = PENDING
PRODUCT_IMPLEMENTED = FALSE
ASSETS = NOT_CREATED
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
```
