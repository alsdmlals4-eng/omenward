# OMENWARD 병종·건물 Tier 매트릭스 및 궁병 T3 정정 승인 계약

```yaml
decision_id: OMW-DEC-20260806-PLANNING-UNIT-BUILDING-TIER-MATRIX-V1
approved_at: 2026-08-06 KST
approval: USER_DIRECT_APPROVAL
status: USER_APPROVED_PLANNING_CANON / NOT_IMPLEMENTED
work_mode: PLANNING_ONLY
product_code_authority: NONE
simulation: NOT_RUN
runtime: NOT_RUN
human_validation: NOT_RUN
```

## 1. 결정 목적

이 문서는 다음 두 범위를 소유한다.

1. 구글 시트 `42_병종_Tier_등급`, `43_건물_Tier_효과` 탭과 GitHub 기획 정본의 연결 계약.
2. 기존 궁병 T3 세 갈래 중 `대공궁병`을 제거하고 현행 T3를 두 갈래로 정정하는 계약.

건물 Tier 구조 자체는 다음 문서를 따른다.

- `docs/design/APPROVED_OMENWARD_BUILDING_TIER_REALIGNMENT_2026-08-06.md`

병종 역할·등급 예산의 기반은 다음 문서를 따른다.

- `docs/design/APPROVED_OMENWARD_TROOP_ROLES_SYNERGIES_AND_COUNTERS_2026-08-05.md`
- `docs/design/APPROVED_PLAYER_TEN_UNIT_LINEAGES_POC_V1.md`
- `docs/design/APPROVED_COMMON_COMBAT_AND_RANK_BUDGET_POC_V1.md`

이 문서는 위 문서 전체를 폐기하지 않는다. 아래에 명시한 궁병 T3 문구만 더 최신 결정으로 대체한다.

## 2. 궁병 Tier 현행 계약

```text
T2_ARCHER_ROLE
= 지속 원거리 화력
+ 비행 적 우선 타기팅
+ FLYING 압력의 기본 병종 대응

ARCHER_T3_BRANCHES
= CROSSBOW_ARCHER / RAPID_FIRE_ARCHER

ANTI_AIR_ARCHER_T3
= SUPERSEDED / REMOVED / IMPLEMENTATION_INPUT_FORBIDDEN
```

### 2.1 T2 궁병

- T2 궁병은 자동생산 대상이자 궁병 TokenSource다.
- 기본 궁병 단계에서 비행 적 우선 타기팅을 가진다.
- 대공 대응을 수행하기 위해 반드시 별도의 T3 대공궁병을 요구하지 않는다.
- 정확한 대공 피해 배율, 사거리, 공격 간격과 표적 전환 임계값은 시뮬레이션 전까지 확정하지 않는다.

### 2.2 T3 석궁병

- 낮은 공격속도와 높은 단발 피해.
- 방어력 관통 또는 중장갑 대상 보너스.
- 부모 궁병의 기본 비행 우선 타기팅은 유지할 수 있지만, 비행 추가 피해·지상화 같은 대공 전용 기능은 자동 부여하지 않는다.

### 2.3 T3 연사궁병

- 높은 공격속도와 낮은 1발 피해.
- 경장갑·소형 군집에 대한 지속 화력.
- 공격 횟수 조건형 스킬과 높은 시너지.
- 부모 궁병의 기본 비행 우선 타기팅은 유지할 수 있지만, 비행 추가 피해·지상화 같은 대공 전용 기능은 자동 부여하지 않는다.

### 2.4 제거되는 항목

```text
T3_ANTI_AIR_ARCHER_BUILDING_BRANCH = FORBIDDEN
T3_ANTI_AIR_ARCHER_AUTO_PRODUCTION = FORBIDDEN
T3_ANTI_AIR_ARCHER_TOKEN_SOURCE = FORBIDDEN
T3_ANTI_AIR_ARCHER_REWARD_CANDIDATE = FORBIDDEN
T3_ANTI_AIR_ARCHER_UNIT_ID = FORBIDDEN
```

현재 대공궁병을 대체하는 세 번째 T3 분기는 만들지 않는다. 세 번째 분기가 필요하다면 역할 공백 증거와 별도 사용자 승인을 요구한다.

## 3. 대체되는 과거 문구

다음 문서의 `대공궁병` 관련 문장은 역사적 증거로만 보존되며 현행 구현 입력으로 사용할 수 없다.

- `docs/design/APPROVED_PLAYER_TEN_UNIT_LINEAGES_POC_V1.md`
  - `## 6. 궁병 계보`의 T3 세 갈래 목록 중 `대공궁병`.
- `docs/design/APPROVED_BARRACKS_TIER3_EVOLUTION_AND_GRADE_SKILLS.md`
  - 궁병 패시브 성장 예시의 `Tier 3 대공궁병`.
  - 초기 T3 궁병 계열의 `대공궁병` 항목.
  - 궁병 토큰 목록과 일반 등급 예시의 `대공궁병`.
- `docs/design/APPROVED_BARRACKS_TIER2_TIER3_INTEGRATED_TREE_V2.md`
  - Tier 3 통합 분기표의 `대공궁병` 행.

충돌 시 이 문서가 위 궁병 T3 문구보다 우선한다.

## 4. 궁병 등급 스킬·영웅 연결

대공궁병 분기 삭제는 궁병 공통 등급 스킬과 초기 이름 지정 영웅을 삭제하지 않는다.

```text
ARCHER_ELITE
= 집중 사격 요구 횟수 감소

ARCHER_HERO_SKILL
= 표적 지정
= 같은 라인 아군 원거리 공격이 지정 대상에게 추가 피해

ARCHER_LEGENDARY_SKILL
= 별비
= 넓은 고정 지역 연속 사격
= 비행 대상 포함 가능

ARCHER_INITIAL_NAMED_HERO
= 1
EXACT_HERO_IDENTITY
= PENDING
UNIQUE_SKILL_2
= RETAINED
```

엘리트·영웅·전설 공통 수치 예산은 기존 첫 PoC 가설을 유지한다.

```text
ELITE  = Threat 2.2 / HP ×1.55 / 기본 피해 ×1.25
HERO   = Threat 5.0 / HP ×2.40 / 기본 피해 ×1.55
LEGEND = Threat 10.0 / HP ×4.00 / 기본 피해 ×2.00
```

이 배율은 제품 확정값이 아니라 시뮬레이션 입력 후보다. 지원 병종은 직접 피해 대신 회복·보호·버프 예산을 포함한다.

## 5. 병영과의 연결

```text
GENERAL_BARRACKS_T1
= 기본 보병 자동생산 + 기본 보병 TokenSource

GENERAL_BARRACKS_T2_ARCHER
= 궁병 자동생산 + 궁병 TokenSource

GENERAL_BARRACKS_T3_ARCHER
= 석궁병 또는 연사궁병 자동생산
+ 궁병 계열 TokenSource 유지
+ 별도 T3 토큰 없음
```

T3 선택은 일반 등급 자동생산 병종을 바꾸지만, 룰렛 등급 자체를 올리지 않는다.

## 6. 비행 압력 대응 가드레일

대공궁병을 삭제하더라도 FLYING 압력이 단일 하드키를 요구해서는 안 된다.

```text
FLYING_PRIMARY_UNIT_PATHS
= T2 궁병 / 비행병

FLYING_ADDITIONAL_PATHS
= 공개된 전술스킬·방어 건물·룰렛 준비 중 별도 승인된 경로

ARCHER_T3_REQUIRED_FOR_BASIC_ANTI_AIR
= FALSE
```

T2 궁병을 보유하지 않으면 진행 불가능하거나, 석궁병·연사궁병 중 하나가 모든 공중·지상 상황의 자동 최적해가 되면 Stop-ship이다.

## 7. 구글 시트 권위 연결

```text
UNIT_MATRIX_SHEET = 42_병종_Tier_등급
BUILDING_MATRIX_SHEET = 43_건물_Tier_효과
```

병종 탭은 다음 정보를 함께 보존한다.

- T1·T2·T3 역할과 업그레이드 변화.
- 자동생산과 TokenSource.
- T2 기본 수치와 생산시간·식량 첫 PoC 가설.
- 엘리트·영웅·전설 수치 예산과 스킬.
- 초기 해금 이름 지정 영웅.
- 승인·PoC·미정·충돌 상태.

건물 탭은 다음 정보를 함께 보존한다.

- T1·T2·T3 효과.
- 분기형·직선 성장형 구분.
- 자동생산과 TokenSource.
- 업그레이드 기회비용.
- 정확 수치와 후속 Gate.

## 8. 제품·수치 경계

```text
PRODUCT_CODE = UNCHANGED
SCENE_RESOURCE_DATA = UNCHANGED
ART_ASSETS = UNCHANGED
EXACT_NUMERICS = PENDING_SIMULATION
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
```

기존 `.tres`, GDScript, Scene, Resource와 아트 자산은 이 결정만으로 변경하지 않는다.
