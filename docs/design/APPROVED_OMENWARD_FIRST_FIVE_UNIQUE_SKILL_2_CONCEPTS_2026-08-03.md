# OMENWARD 초기 5명 해금 영웅 고유 2스킬 콘셉트 승인안

```yaml
decision_id: OMW-DEC-20260803-GAMEPLAY-HERO-FIRST-FIVE-UNIQUE-SKILL-2-CONCEPTS-V1
approved_at: 2026-08-03 00:06 KST
approval: USER_APPROVED_RECOMMENDATION_WITH_DIRECT_REFINEMENTS
status: USER_APPROVED / ACTIVE_PLANNING_BRANCH / NOT_IMPLEMENTED
scope: FIRST_FIVE_UNLOCKED_NAMED_HERO_UNIQUE_SKILL_2_CONCEPTS
parent_decision: OMW-DEC-20260802-GAMEPLAY-HERO-GRADE-SLOT-AND-UNLOCKED-SKILL-REPLACEMENT-V1
activation_authority: APPROVED_OMENWARD_HERO_ABILITY_ACTIVATION_MODE_2026-08-02.md
initial_roster_authority: APPROVED_OMENWARD_HERO_INITIAL_ROSTER_ARCHETYPE_SELECTION_2026-08-02.md
benchmark_policy: OMW-PROC-20260803-GRILL-ME-BENCHMARK-PRODUCTION-COMPARISON-V1
product_code_authority: NONE
exact_hero_identities: PENDING
exact_values: PENDING
assets: NOT_CREATED
simulation: NOT_RUN
runtime_validation: NOT_RUN
human_validation: NOT_RUN
```

## 1. 결정 요약

초기 해금 이름 지정 영웅 5명의 고유 2스킬 전술 콘셉트를 다음과 같이 승인한다.

```text
shield_guard / 방패병 → 불퇴의 성벽
archer / 궁병         → 천공 소거
priest / 사제         → 생명의 서약
mage / 마법사         → 메테오
assassin / 암살자     → 그림자 분신
```

표시 이름은 현행 기획명이다. 최종 캐릭터 이름·세계관 어휘·로컬라이징 과정에서 이름을 바꿀 수 있지만, 아래 전술 목적과 금지 경계는 같은 Decision을 명시적으로 수정하기 전까지 유지한다.

모든 능력은 표준 `[영웅]` 등급의 **2스킬 슬롯을 교체**한다. 추가 세 번째 스킬·영웅 전용 패시브·숨은 상시 보너스를 만들지 않는다.

## 2. 공통 전술 계약

```text
ONE_UNIQUE_SKILL_2
ONE_LANE
ONE_PRIMARY_TACTICAL_PURPOSE
AUTOMATIC_RULE_BASED_ACTIVATION
LONG_COOLDOWN_FRAMEWORK
READY_STATE_PRESERVED_UNTIL_VALID_CONDITION
STANDARD_HERO_POWER < NAMED_HERO_POWER < STANDARD_LEGENDARY_POWER
```

공통 규칙:

- 해당 영웅이 배치된 한 전선만 직접 영향을 받는다.
- 수동 버튼·수동 타깃·수동 보류를 사용하지 않는다.
- cooldown이 끝나도 유효 조건이 없으면 `READY_WAITING_FOR_VALID_CONDITION`을 유지한다.
- trigger·target filter·priority·tie-break는 데이터로 공개하고 저장·재현 가능한 결정 규칙을 사용한다.
- 발동 직전 유효성을 다시 검사한 뒤 `CAST_COMMIT`한다.
- 스킬은 해당 전선의 국면을 식별 가능하게 바꾸되 표준 전설 전체 키트의 총 전투 가치보다 낮아야 한다.
- 다른 전선·룰렛 확률·보관함·경제·건물 상태를 직접 변경하지 않는다.
- exact 수치·cooldown·지속시간·범위·피해량·체력 하한·복제 계수는 후속 Decision과 simulation 전까지 고정하지 않는다.

## 3. 방패병 — 불퇴의 성벽

### 전술 목적

붕괴 직전의 전열을 짧게 고정해 아군이 사격·회복·증원을 이어 갈 시간을 만든다.

### 콘셉트

```text
같은 전선의 전열 압력이 유효 임계치를 넘음
→ 방패병이 현재 위치에서 방어 태세
→ 짧은 시간 넓은 방벽 효과 전개
→ 정해진 피해 예산까지 원거리 투사체·전방 피해를 대신 흡수
→ 지속시간 또는 흡수 예산 종료
```

### 필수 경계

- 방벽은 새 영구 지형·navmesh·건설물·점령 오브젝트를 만들지 않는다.
- 적 경로를 영구 재탐색시키지 않는다.
- 핵심 목적은 `전열 유지` 하나다.
- 수동 이동·전선 이동·아군 전체 무적을 제공하지 않는다.
- 정확 투사체 차단 범위, 흡수 예산, displacement 저항은 pending이다.

### 제작 권장

원본 방패병 리그·방어 자세를 재사용하고 전방 호형 VFX, 충격 SFX, 남은 방벽 예산 UI만 추가한다. 신규 방벽 유닛 AI나 별도 구조물 Scene은 기본안에서 금지한다.

## 4. 궁병 — 천공 소거

### 전술 목적

비행 적이 누적된 전선에서 궁병의 대공 전문성을 한 번에 폭발시킨다.

### 콘셉트

```text
같은 전선의 유효 비행 표적 수 또는 위협 합계가 임계치 이상
→ 짧은 조준 예고
→ 현재 유효한 모든 비행 표적에 동시 일제사격
→ 각 표적은 한 번의 고유 타격 판정
```

### 필수 경계

- 지상 표적·건물·다른 전선에는 피해를 주지 않는다.
- 유효 비행 표적이 없으면 READY 상태를 유지한다.
- 무한 연쇄·반복 추적·전선 전체 지속 피해를 만들지 않는다.
- 같은 표적에 중복 투사체를 과도하게 몰아 단일 보스 처형기로 변형하지 않는다.
- 정확 대상 수 상한·위협 점수·피해량은 pending이다.

### 제작 권장

원본 사격 모션을 시간차 재생하고 표적별 궤적 VFX를 공유한다. 각 비행 표적마다 독립적인 새 애니메이션이나 카메라 연출을 만들지 않는다.

## 5. 사제 — 생명의 서약

### 전술 목적

같은 전선이 짧은 집중 피해로 한꺼번에 붕괴하는 순간을 유예한다.

### 콘셉트

```text
같은 전선의 생존 아군 전투 유닛이 설정된 체력 하한 아래로 떨어질 위험이 유효 조건을 만족
→ 짧은 성역 발동
→ 지속시간 동안 대상들의 체력이 각자 정해진 유효 하한 아래로 감소하지 않음
→ 종료 후 저장 피해 없이 정상 피해 규칙 복귀
```

### 체력 하한 계약

회복과 체력 하한 보호를 분리한다.

```text
effective_floor_per_target
= min(current_hp_at_cast, configured_floor_percent * max_hp)
```

- 발동 시 체력을 올리지 않는다.
- 이미 설정 하한보다 낮은 대상은 현재 체력을 유효 하한으로 사용하므로 숨은 회복이 없다.
- 지속시간 동안 들어온 피해를 종료 시 한꺼번에 적용하지 않는다.
- 사망한 유닛을 부활시키지 않는다.
- 건물·성문·타워·보관 토큰에는 적용하지 않는다.
- 적 유닛에게 같은 보호를 주지 않는다.
- exact 체력 비율·대상 수·지속시간·발동 위기 조건은 pending이다.

### 적대적 경계

지속시간이나 적용 범위가 크면 사실상 같은 전선 전체 무적으로 변한다. 따라서 짧은 생존 유예만 허용하며, 공격·회복·보호막·부활을 함께 제공하지 않는다.

## 6. 마법사 — 메테오

### 전술 목적

밀집 공세의 중심을 예고된 대형 단발 폭발로 붕괴시킨다.

### 콘셉트

```text
같은 전선에서 적 밀집도와 위협 합계가 유효 임계치 이상
→ deterministic cluster center 선택
→ 지면 경고·낙하 궤적·SFX 예고
→ 지연 후 메테오 1개 낙하
→ 넓은 범위에 단발 대형 피해
```

### 필수 경계

- 현재 영웅이 배치된 한 전선만 대상으로 한다.
- `CAST_COMMIT` 뒤에는 적이 이동해 피할 수 있으며, 메테오는 확정 지점에 낙하한다.
- 즉시 명중·화면 밖 공격·전선 전체 피해·다중 메테오 난사는 금지한다.
- 기본안은 단발 폭발이며 지속 화염 지대·군중제어·방어력 감소를 함께 묶지 않는다.
- cluster 동률은 위협 합계, 적 수, 아군 본진 접근도, stable entity ID 순으로 결정하는 방향을 사용한다. exact 순서는 구현 계획에서 고정한다.
- exact 지연시간·반경·피해·낙하 높이·카메라 흔들림은 pending이다.

### 제작 권장

낙하 위치를 충분히 일찍 표시하고 메테오가 다른 영웅 스킬보다 높은 시청각 위계를 갖되, 표준 전설 스킬보다 과도한 화면 점유를 만들지 않는다.

## 7. 암살자 — 그림자 분신

### 전술 목적

한 후열 우선 표적에 짧은 집중 화력을 만들어 암살자의 역할을 강화한다.

### 콘셉트

```text
같은 전선에 유효한 후열 고가치 표적 존재
→ 암살자 주변의 합법 위치에 그림자 분신 1체 생성
→ 짧은 지속시간 동안 원본 암살자의 현재 표적과 기본 공격을 종속 복제
→ 지속시간·원본 사망·MapRun 종료 시 제거
```

### 종속 분신 계약

분신은 독립 영웅·독립 병종·독립 AI가 아니다.

```text
CLONE_COUNT = 1
INDEPENDENT_TARGET_SELECTION = FALSE
INDEPENDENT_PATHFINDING = FALSE
SKILL_CASTING = FALSE
ON_HIT_AND_CC_COPY = FALSE
RESOURCE_OR_REWARD_GENERATION = FALSE
HIGH_GRADE_SLOT_OCCUPANCY = FALSE
LANE_TRANSFER = FALSE
BODY_BLOCKING = FALSE
```

- 분신은 원본의 현재 합법 표적을 따라가며 독립적으로 새 표적을 평가하지 않는다.
- 기본 공격의 시각과 일부 피해만 복제하며 스킬·패시브·군중제어·처형·흡혈·자원 생성은 복제하지 않는다.
- 적 AI의 별도 공격 대상이나 탱킹 수단으로 사용하지 않는 비표적 전투 proxy를 기본안으로 한다.
- 원본과 다른 전선으로 이동하거나 영구 잔존하지 않는다.
- 분신 피해 계수·공격 동기화·spawn offset·지속시간은 pending이다.

### 제작 권장

원본 모델·리그·기본 공격 애니메이션을 반투명 재사용하고, 원본과 분신을 잇는 짧은 시각적 관계 표식을 둔다. 신규 범용 유닛 AI·경로 탐색·상태 저장을 만들지 않는다.

## 8. 상용 게임 벤치마크와 차별화

벤치마크는 복제 대상이 아니라 실패 경계와 제작 선택을 검증하는 비교 자료다. 조회 기준일은 2026-08-03이다.

| OMENWARD 콘셉트 | 공식 비교 사례 | 배운 점 | OMENWARD 차별화 |
|---|---|---|---|
| 불퇴의 성벽 | League of Legends `Braum - Unbreakable` | 방패 역할은 전방 방향성·명확한 시각 언어·피해 차단 목적이 읽혀야 함 | 새 지형 없이 같은 전선의 짧은 전열 유지 사건으로 축소 |
| 천공 소거 | Diablo III `Demon Hunter - Rain of Vengeance` | 넓은 사격 사건은 짧은 예고와 범위 위계가 중요 | 지상 광역기가 아니라 유효 비행 표적만 동시 타격하는 대공 전문 스킬 |
| 생명의 서약 | League/Wild Rift `Kindred - Lamb's Respite` | 체력 하한은 강력하므로 지속시간·대상·종료 동작을 명확히 해야 함 | 아군 한 전선만, 회복 없음, 적 보호 없음, 건물 제외 |
| 메테오 | Wild Rift `Meteor Enchant` | 큰 광역 피해는 지연 낙하와 지면 예고가 대응 가능성을 만든다 | 수동 지점 지정 대신 deterministic 적 밀집 자동 선택, 단발 1개 |
| 그림자 분신 | League of Legends `Zed - Living Shadow` | 분신을 완전한 자율 유닛보다 제한된 행동 proxy로 두면 정체성과 제작비를 통제 가능 | 위치 교환 없음, 독립 AI 없음, 원본 표적·기본 공격만 종속 복제 |

공식 비교 자료:

- Riot Games, `Clarity in League`: https://www.leagueoflegends.com/en-us/news/dev/clarity-in-league/
- Riot Games, `Quick Gameplay Thoughts: Champion Counterplay`: https://www.leagueoflegends.com/en-au/news/dev/quick-gameplay-thoughts-may-14/
- Riot Games, `Braum`: https://www.leagueoflegends.com/ko-kr/champions/braum/
- Blizzard Entertainment, `복수의 비`: https://eu.diablo3.blizzard.com/ko-kr/class/demon-hunter/active/rain-of-vengeance
- Riot Games, `Kindred`: https://wildrift.leagueoflegends.com/en-gb/champions/kindred/
- Riot Games, `Wild Rift Patch Notes 3.4 - Meteor Enchant`: https://wildrift.leagueoflegends.com/en-sg/news/game-updates/wild-rift-patch-notes-3-4/
- Riot Games, `Zed`: https://www.leagueoflegends.com/ko-kr/champions/zed/

## 9. 현업 제작 비교

| 스킬 | 상대 제작비 | 주요 의존성 | 권장 구현 형태 | 피해야 할 범위 팽창 |
|---|---:|---|---|---|
| 불퇴의 성벽 | 중 | 피해 전달·투사체 판정·방어 자세·VFX | hero 상태 + 전방 barrier effect | 새 구조물·navmesh·적 경로 AI |
| 천공 소거 | 낮음~중 | 비행 태그·다중 대상 정렬·공유 궤적 | 동일 이벤트에서 대상 목록 snapshot | 표적별 독립 시네마틱·무한 추적 |
| 생명의 서약 | 중 | 피해 적용 전 clamp·대상 snapshot·상태 UI | 짧은 lane buff + per-target floor | 회복·부활·건물 보호·적 포함 |
| 메테오 | 중 | cluster 선택·telegraph·지연 event·AoE | committed point + delayed impact | 다중 메테오·지속 장판·전역 공격 |
| 그림자 분신 | 중 | 종속 공격 proxy·animation reuse·귀속 로그 | owner-bound non-targetable clone proxy | 독립 AI·pathfinding·스킬 복제·보상 생성 |

현업 권장 검증 순서:

1. 데이터 계약과 deterministic target selection 단위 테스트.
2. 최소 VFX placeholder로 발동 시점·대상·종료 가독성 확인.
3. 같은 encounter에서 표준 영웅·해금 영웅·표준 전설 총 기여 비교.
4. 세 전선 중 한 전선만 과도하게 지배하는지 확인.
5. 저사양·다수 유닛 상황에서 VFX와 분신 animation 비용 확인.
6. 저장·재개 직전과 직후 발동 결과가 동일한지 확인.
7. 사람 테스트에서 스킬이 왜 발동했고 무엇을 바꿨는지 설명 가능한지 확인.

## 10. 적대적 검토

| Audit ID | 공격 | 판정 | 보완 |
|---|---|---|---|
| `OMW-AUD-164` | 체력 하한이 사실상 한 전선 전체 무적으로 변한다 | 유효 | 짧은 지속시간·전투 유닛 한정·회복/부활 없음 |
| `OMW-AUD-165` | 체력 하한 적용 시 낮은 유닛을 하한까지 올려 숨은 회복이 된다 | 유효 | `min(current_hp_at_cast, configured_floor)` 계약 |
| `OMW-AUD-166` | 메테오가 즉발이면 대응 불가능하고 자동전투 결과가 일방적이다 | 유효 | 지면 telegraph·지연 낙하·확정 지점 회피 가능 |
| `OMW-AUD-167` | 메테오가 너무 자주 빗나가 해금 보상이 무의미하다 | 유효 | 발동 밀집 임계치·예측 창·명중률 simulation 필요 |
| `OMW-AUD-168` | 분신이 별도 AI 유닛이 되어 제작량·저장·동시성 범위를 폭증시킨다 | 유효 | owner-bound proxy·독립 target/pathfinding 금지 |
| `OMW-AUD-169` | 분신이 스킬·on-hit·CC까지 복제해 전설급 다중 효과가 된다 | 유효 | 기본 공격 일부 피해만 복제, 스킬·패시브·CC 금지 |
| `OMW-AUD-170` | 방벽이 navmesh를 바꾸어 적이 정지하거나 우회 오류를 낸다 | 유효 | 비지형 barrier effect, 영구 경로 변경 금지 |
| `OMW-AUD-171` | 천공 소거가 비행 Wave를 혼자 삭제해 상성을 무효화한다 | 유효 | 대상 상한·피해 예산·표준 전설 미만 검증 |
| `OMW-AUD-172` | 다섯 고유 스킬의 VFX가 동시에 전장 가독성을 파괴한다 | 부분 유효 | 전역 영웅 이상 1명 제한 + 시각 위계·노이즈 예산 |

## 11. 금지

- 표준 2스킬과 고유 2스킬 동시 보유.
- 다섯 스킬 중 하나가 여러 전선을 직접 공격·보호하는 것.
- 사제 스킬의 회복·부활·건물 보호·적 보호.
- 메테오의 즉발·전역 타격·기본 다중 낙하·기본 지속 장판.
- 분신의 독립 영웅 취급·전역 고등급 슬롯 점유·독립 AI·pathfinding·스킬 복제·보상 생성.
- 방벽을 영구 지형·건물로 구현하는 것.
- 정확 수치·구현·simulation·runtime·human QA를 실행 전 완료로 표시하는 것.

## 12. 구현·검증 경계

```text
CURRENT_PRODUCT = LEGACY_PROTOTYPE
LATEST_APPROVED = DOCUMENTED_NOT_IMPLEMENTED
PRODUCT_CODE = UNCHANGED
EXACT_HERO_IDENTITIES = PENDING
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

## 13. 다음 Decision

다음 Grill Me는 다섯 스킬의 **cooldown·충전 구조와 발동 실패 정책**을 결정한다.

```text
NEXT_GATE = OMW-DEC-20260803-GAMEPLAY-HERO-UNIQUE-SKILL-2-COOLDOWN-CHARGE-AND-FAILURE-POLICY-V1
```
