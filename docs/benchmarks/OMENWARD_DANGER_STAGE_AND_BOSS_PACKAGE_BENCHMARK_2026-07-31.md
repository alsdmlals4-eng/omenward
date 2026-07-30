# 오멘워드 위험 Stage·보스 행동 패키지 경량 벤치마킹

- 작성일: `2026-07-31`
- 상태: `BENCHMARK_COMPLETE / DESIGN_NOT_YET_APPROVED`
- Work Mode: `PLAN / PLANNING_ONLY_PROFILE`
- 제품 구현 권한: `NONE`
- 대상: Stage 5·10·15·20 위험 공세와 보스 행동 패키지

## 1. 조사 목적

다음을 결정하기 위한 경량 벤치마킹이다.

1. 위험 Stage가 일반 Stage와 무엇으로 구별되는가.
2. Stage 5·10·15·20이 각각 어떤 지휘 능력을 시험해야 하는가.
3. 보스가 공용 10병종 계약을 깨지 않고 어떻게 특수성을 가지는가.
4. 35분 런에서 보스 페이즈와 정보량을 어디까지 허용하는가.
5. 패배가 숨은 규칙이 아니라 읽을 수 있었던 우선순위 실패로 귀인되는가.

이 문서는 근거 자료이며 사용자 승인 전 제품 정본이 아니다.

## 2. 내부 정본 기준

- 위험 Stage: 5·10·15, 최종 위험 Stage: 20.
- 위험 Stage에는 전술계획 정지가 없다.
- 위험 Stage에서 신규 튜토리얼을 추가하지 않는다.
- 실시간 필수 조작 종류는 최대 2개를 목표로 한다.
- Stage 5는 첫 무정지 통합 시험이며 별도 보스를 두지 않는다.
- Stage 10은 영웅급 지휘 적.
- Stage 15는 전설급 돌파 보스.
- Stage 20은 신화급 최종 보스.
- 공세 라인, 병종, 수량과 치명적 특수 행동은 사전 공개한다.
- 일반 적은 공용 10개 UnitArchetype을 사용한다.
- 보스는 `base_archetype_id + BossBehaviorPackage + BossPhaseProfile + Visual Set`으로 구성한다.
- 정확한 Threat·수량·전투 수치는 아직 미확정이다.

## 3. 선별 사례

### 3.1 Into the Breach

공식 Steam 설명은 모든 적 공격을 사전에 보여 주고, 플레이어가 그 정보를 분석해 대응하도록 명시한다.

오멘워드 적용 원칙:

- 보스의 치명적 행동은 숨기지 않는다.
- 준비 단계에서는 라인·역할·주요 패턴을 공개한다.
- 전투 중에는 다음 행동의 대상 라인·전조·실행 시점을 지속 표시한다.
- 난이도는 정보 은폐가 아니라 여러 공개 위협 사이의 우선순위 충돌에서 만든다.

### 3.2 Thronefall

공식 Steam 설명은 짧은 세션에서 경제와 방어의 균형, 낮과 밤의 준비·방어 대비, 반복 공세를 핵심으로 제시한다.

오멘워드 적용 원칙:

- 위험 Stage는 새로운 하위 시스템이 아니라 이전 준비 선택의 결산이어야 한다.
- 보스마다 플레이어가 이미 가진 건물·병력·보관·룰렛 구조 중 무엇을 우선할지 바꾼다.
- 공세 전 준비와 전투 중 제한된 실행의 대비를 유지한다.

### 3.3 Dome Keeper

공식 Steam 설명은 지상·공중의 서로 다른 이동·공격 방식을 가진 적을 방어하고, 업그레이드·수리·준비의 선택을 반복하는 구조를 강조한다.

오멘워드 적용 원칙:

- 한 위험 패키지에서 핵심 위협 축은 최대 2개로 제한한다.
- 공중·후열·대형·공성 등 역할 차이는 시각·아이콘·징조로 즉시 판독되어야 한다.
- 단순 HP 증가보다 접근 경로와 목표 우선순위 차이로 위험을 만든다.

### 3.4 Bad North

공식 Steam 설명은 한 번의 방어 기회와 지형·배치 기반의 냉혹하지만 간결한 실시간 전술을 강조한다.

오멘워드 적용 원칙:

- 위험 Stage 패배 원인은 플레이어가 사전에 확인할 수 있었던 배치·우선순위 문제여야 한다.
- 보스가 예고 없이 라인을 바꾸거나 숨은 즉사기를 사용하는 구조를 금지한다.
- 실전에서 선택 가능한 대응 수단은 적어도 두 가지 이상이어야 한다.

## 4. 추출된 공통 원칙

1. `TELEGRAPH_BEFORE_PUNISHMENT`
   - 치명적 행동 전에 라인, 대상, 역할, 전조와 예상 결과를 보여 준다.
2. `ONE_PRIMARY_TEST_PER_DANGER_STAGE`
   - 위험 Stage 하나는 하나의 주 지휘 능력을 시험한다.
3. `MAX_TWO_CONCURRENT_THREAT_AXES`
   - 한 시점의 핵심 위협 축은 최대 두 개다.
4. `BOSS_RECOMBINES_EXISTING_RULES`
   - 보스는 새 미니게임보다 기존 전선·건물·병종·영토 규칙을 재조합한다.
5. `COUNTERPLAY_MINIMUM_TWO`
   - 주요 패턴에는 최소 두 가지 대응 경로가 존재한다.
6. `NO_HIDDEN_ENEMY_DATA`
   - 난이도를 위해 적군 전용 숨은 스탯·스킬 복사본을 만들지 않는다.
7. `FAILURE_ATTRIBUTION_REQUIRED`
   - 패배 화면에서 어떤 공개 위협을 놓쳤는지 설명할 수 있어야 한다.
8. `NO_NEW_TUTORIAL_ON_DANGER`
   - 위험 Stage에서는 이미 배운 규칙만 시험한다.
9. `PHASE_CHANGE_CHANGES_PRIORITY`
   - 페이즈 변화는 규칙을 무효화하지 않고 목표 우선순위를 바꾼다.
10. `DANGER_STAGE_TIME_BUDGET`
    - Stage 5·10·15는 90~120초, Stage 20은 150~210초 목표를 지킨다.

## 5. 오멘워드 적용 방향

| Stage | 핵심 시험 | 보스 여부 | 주요 위협 축 후보 |
|---:|---|---|---|
| 5 | 무정지 실행·두 전선 우선순위 | 없음 | 정면 압박 + 원거리 견제 |
| 10 | 지휘 적의 호위·지원망 해체 | 영웅급 | 지휘 버프 + 비대칭 두 전선 |
| 15 | 한 라인 돌파와 밀집 처벌 | 전설급 | 공성 돌파 + 광역 분산 요구 |
| 20 | 전체 빌드·세 전선·건물 보호 통합 | 신화급 | 전선→구조→최종 커밋 3페이즈 |

## 6. 공용 데이터 경계

일반 적:

```text
UnitArchetypeProfile
+ TierProfile
+ RankProfile
+ lane/count/spawn_time
+ veil Visual Set
```

보스:

```text
base_archetype_id
+ BossBehaviorPackage
+ BossPhaseProfile
+ boss Visual Set
```

보스 패키지는 전용 패턴·페이즈·제어 보정·구조물 우선 행동·Threat 배율을 추가할 수 있다. 일반 적군 아키타입의 스탯·스킬·AI 원본을 복제하거나 덮어쓰지 않는다.

## 7. 설계 금지선

- Stage 5에 보스 추가.
- 위험 Stage에서 신규 시스템 튜토리얼.
- 세 라인에 서로 다른 치명적 특수 위협을 동시에 하나씩 배치.
- 예고 없는 라인 순간 이동·즉사·건물 삭제.
- 무조건 제어 면역.
- 보스와 호위를 동시에 처치해야만 하는 숨은 승리 조건.
- 보스 HP만 과도하게 올려 전투시간을 채우는 방식.
- 모든 위험 Stage를 같은 주력 라인 돌파로 반복.
- 보스 패키지를 일반 병종 데이터에 직접 덮어쓰기.

## 8. 후속 설계 질문

- Stage 5의 정확한 두 전선 구조와 실시간 조작 2종.
- Stage 10 지휘 적의 버프 범위·호위 관계·처치 우선순위.
- Stage 15 돌파 보스의 패턴 순환과 밀집 처벌 범위.
- Stage 20 세 페이즈의 전환 조건과 최종 승리 조건.
- 각 Stage의 Threat 예산·수량·출격 시각.
- 보스 제어 저항·구조물 피해·HP 배율의 정확한 수치.
- 사람 플레이에서 공개 정보가 과밀하지 않은지.

## 9. 출처

- Into the Breach, official Steam store description.
- Thronefall, official Steam store description.
- Dome Keeper, official Steam store description.
- Bad North: Jotunn Edition, official Steam store description.
- Omenward internal approved shared UnitArchetype and W1~20 evidence documents.

이 벤치마킹은 위험 Stage와 보스 설계의 원칙만 제공한다. 아래 상세 편성안은 별도 사용자 승인 후 같은 Decision ID로 정본화해야 한다.
