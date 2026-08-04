# OMENWARD 병종 역할·시너지·카운터 설계 Spec

```yaml
decision_id: OMW-DEC-20260805-PLANNING-TROOP-ROLES-SYNERGIES-AND-COUNTERS-V1
approval: USER_FINAL_APPROVAL
planning_counter_target: 4_OF_10
status: APPROVED_DESIGN_SPEC / NOT_CANONIZED / NOT_IMPLEMENTED
product_code_authority: NONE
simulation: NOT_RUN
runtime: NOT_RUN
human_validation: NOT_RUN
```

## 1. 목적

현행 Stage 압력과 건물 전문화를 실제 병종 선택으로 연결한다.

```text
예고된 압력
→ 병영·건물로 병종 결과의 방향을 설계
→ 룰렛에서 T1/T2 병종을 획득
→ 보관·판매·한 전선 비가역 배치
→ 병종 역할과 조합 결과를 복기
```

병종은 단순 공격력 차이가 아니라 다음 중 하나 이상을 바꿔야 한다.

- 어떤 압력과 표적을 우선 처리하는가.
- 어느 전선·Route·Layer에 배치할 가치가 있는가.
- 어떤 병종과 함께 있을 때 역할 수행 시간이 확보되는가.
- 무엇을 얻는 대신 어떤 역할을 포기하는가.

## 2. 승인 범위

```text
ROSTER_BASELINE: 10
ROSTER_COUNT_IS_NOT_SACRED
```

현행 10종은 보존 목표이지 불변 조건이 아니다.

병종 추가 조건:

```text
ADD_UNIT_ONLY_IF
= 기존 병종으로 표현할 수 없는 압력 대응·전선 판단·Route 판단을 만든다.
```

병종 제거·교체 조건:

```text
REMOVE_OR_REPLACE_IF
= 다른 병종과 역할·표적·배치 판단·포기 비용이 실질적으로 같다.
```

단순히 콘텐츠 수를 늘리기 위한 병종 추가, 외형만 다른 중복 병종, 특정 Stage의 열쇠 역할만 수행하는 하드키 병종은 금지한다.

## 3. 권장 로스터 기준선

| 병종 | 전장 역할 | 주 대응 압력 | 명확한 포기 비용 |
|---|---|---|---|
| 방패수호병 | 전선 고정·후열 보호 | MASS·INFILTRATION | 낮은 처치력·기동성 |
| 대검병 | 근접 광역·밀집 해체 | MASS | 낮은 방어·대공 불가 |
| 창병 | 대형·돌진·공성 차단 | SIEGE·ARMORED | 다수 소형 처리 취약 |
| 궁수 | 공중 억제·원거리 견제 | FLYING | 장갑 대상·근접 취약 |
| 마도사 | 장갑 약화·제한 광역 | ARMORED·MASS | 낮은 생존력·느린 템포 |
| 사제 | 유지력·보호·회복 | 장기 복합 압력 | 직접 처치력 부족 |
| 암살자 | 우회 Route 추적·후열 제거 | INFILTRATION·SIEGE | 전선 유지·점령 취약 |
| 기병 | 공개 Route 신속 대응 | INFILTRATION·SIEGE | 장기 교전·대공 취약 |
| 비행병 | 공중 우세·후방 급습 | FLYING·SIEGE | 점령 불가·대공에 취약 |
| 거인 | 장갑 돌파·승리 전선 구조물 파괴 | ARMORED·SIEGE | 느림·다전선 대응 불가 |

기존 프로토타입의 이름·외형 계보는 가능한 한 유지한다. 다만 `암살자 / 기병 / 비행병`처럼 현재 데이터에서 모두 후열 우선 역할에 가까운 병종은 각각 `우회 추적 / 공개 Route 대응 / 공중 우세`로 분리한다.

## 4. 다섯 압력의 병종 대응

| 압력 | 주 대응 병종 | 보조 대응 | 금지되는 단일 정답 |
|---|---|---|---|
| MASS | 대검병·마도사 | 방패수호병 | 광역 병종 하나만 보유하면 자동 해결 |
| ARMORED | 마도사·창병 | 거인 | 방어 무시 병종 하나가 모든 장갑·Boss 해결 |
| FLYING | 궁수·비행병 | 후속 전술스킬 | 궁수 미보유 시 통과 불가 |
| INFILTRATION | 암살자·기병 | 후방 방패수호병 | 우회 Route를 전투 중 숨겨 특정 병종 요구 |
| SIEGE | 창병·기병 또는 암살자 | 거인의 역공 | 공성 저지와 구조물 파괴를 한 병종이 모두 최적 수행 |

각 압력은 병종 경로 최소 두 개와 건물·전술 경로를 함께 가져야 한다. 병종 하나가 다섯 압력 모두에서 최적이면 역할을 분리하거나 포기 비용을 강화한다.

## 5. 시너지 문법

시너지는 별도 세트 보너스가 아니라 실제 전장 행동의 연결로 만든다.

```text
방패수호병이 적을 고정
→ 대검병·마도사가 밀집을 처리

마도사가 장갑을 약화
→ 창병·거인이 핵심 표적을 마무리

암살자가 우회 Route를 추적·표시
→ 기병·궁수가 공개된 목표를 차단

사제가 비가역 배치 전선을 유지
→ 전문 병종이 역할을 수행할 시간 확보

궁수·비행병이 공중을 통제
→ 거인과 전열 병력이 지상 목표에 집중
```

가드레일:

- 각 병종은 단독으로도 최소 역할을 수행한다.
- 특정 짝이 없으면 기능하지 않는 의존형 설계 금지.
- `병종 둘 보유 시 공격력 +N%` 같은 단순 세트 보너스는 기본 문법으로 사용하지 않는다.
- 시너지의 원인과 결과를 전장·결과 로그·복기에서 설명할 수 있어야 한다.
- 하나의 고정 조합이 모든 Stage의 최적해가 되면 Stop-ship이다.

## 6. 병영 전문화 연결

```text
전열 병영 가중 계열
= 방패수호병 / 대검병 / 창병 / 거인

기동 병영 가중 계열
= 궁수 / 암살자 / 기병 / 비행병

공통 지원 계열
= 마도사 / 사제
```

병영 분기는 반대 계열을 영구 삭제하지 않는다. 병영은 다음을 조절한다.

- TokenSource 등장 가중.
- 보상 후보의 역할 분포.
- 해당 계열의 승급 기회.
- Stage 예고에 맞춘 결과 예측 가능성.

공통 지원 계열은 어느 한 분기의 필수 독점물이 되지 않는다. 정확한 가중치·등장 확률·승급 비용은 `PENDING_SIMULATION`이다.

## 7. Tier와 룰렛 자산

```text
T1 병종 토큰 = 실제 T1 인게임 이미지
T2 병종 토큰 = 실제 T2 인게임 이미지
T3 병종 토큰 = FORBIDDEN
결과 Preview = 실제 지급 병종 이미지
```

T1→T2→T3는 같은 역할 계보를 유지한다.

- T1: 역할을 처음 읽히는 기본형.
- T2: 같은 역할을 더 안정적으로 수행하거나 특정 압력에 전문화.
- T3: 단순 능력치 증가가 아니라 표적 우선순위·Route 대응·Layer 상호작용·전선 유지 방식 중 하나를 변화.

T3는 결과 Preview·보관함·배치 카드·전장 실제 병종에서 표현하되 룰렛용 신규 토큰을 만들지 않는다.

## 8. 전선·Route·Layer 규칙

- 일반 병력은 배치 뒤 자유 전선 이동·회수·판매가 불가능하다.
- 기병의 신속 대응은 배치 전 선택과 공개된 Route 내 행동으로 표현하며 자유 Cross-lane 이동이 아니다.
- 암살자의 추적은 Stage 시작 전 공개된 우회 Route와 목표에만 반응한다.
- 궁수와 비행병의 공격 가능 Layer는 UI·시각·실제 판정이 일치해야 한다.
- 비행병의 공중 이동은 점령·구조물 상호작용을 자동으로 허용하지 않는다.
- 거인은 느린 결정 전선 병종이며 세 전선의 문제를 동시에 해결하지 않는다.

## 9. 벤치마킹·현업 비교

### 채택할 원칙

- Age of Wonders 4: 다수 유닛을 빠르게 구분할 수 있는 명확한 역할 분류.
- Age of Empires IV: 병종의 강점·약점과 카운터 관계가 플레이어에게 읽히는 구조.
- Teamfight Tactics 개발 회고: 특정 조합에 플레이어를 조기 고정하지 않고 여러 조합이 성립하는 유연성.

### 오멘워드와 다른 조건

- 오멘워드는 실시간 직접 조작 RTS가 아니라 룰렛 결과와 비가역 전선 커밋을 사용하는 오토배틀 전략 게임이다.
- 병종 선택은 상시 생산이 아니라 TokenSource·룰렛·보관함·배치 순서에 영향을 받는다.
- 대응 수단은 병종뿐 아니라 건물 전문화와 전술스킬에도 분산된다.

### 복제하지 않을 부분

- 타 게임의 상성 수치·피해 배율·유닛 비용 직접 복제.
- 고정된 가위바위보 하나로 모든 교전을 결정하는 구조.
- 강한 세트 보너스로 정해진 조합을 강제하는 구조.
- 병종마다 별도 자원·미니게임·독립 메뉴를 추가하는 구조.

공식 참고:

- https://www.paradoxinteractive.com/games/age-of-wonders-4/news/age-of-wonders-4-dev-diary-1
- https://support.ageofempires.com/hc/en-us/articles/4409243714836-Digital-Deluxe-Edition
- https://teamfighttactics.leagueoflegends.com/en-us/news/dev/dev-teamfight-tactics-galaxies-learnings/
- https://teamfighttactics.leagueoflegends.com/en-us/news/dev/dev-tft-ko-coliseum-learnings/

## 10. 로스터 증감 판정 절차

로스터 증감은 다음 순서로 판단한다.

```text
1. 역할 공백 또는 중복을 증거로 제시
2. 기존 병종의 역할 수술로 해결 가능한지 검토
3. 이름·외형 계보 유지 가능성 검토
4. 추가/삭제가 룰렛·보관함·학습량·아트 비용에 미치는 영향 검토
5. 적대적 검토와 시뮬레이션 Gate 통과
6. 별도 정본 변경으로 승인
```

현재 기준선에서는 10종을 유지한다. 4/10 정본 작성 과정에서 역할 공백이 해소되지 않을 때만 8~12종 범위의 변경안을 다시 제시한다.

## 11. 정보 공개·UX 계약

병종 카드·보관함·배치 Preview에는 최소 다음 정보를 표시한다.

```text
핵심 역할
공격 가능 Layer
우선 표적
유리한 압력
명확한 약점
추천 전선·Route 조건
```

압력 대응을 설명할 때 숨은 보정값 대신 관찰 가능한 행동을 우선한다. 플레이어는 Stage 시작 전 `왜 이 병종이 필요한지`, 결과 복기에서 `왜 역할을 수행했거나 실패했는지` 설명할 수 있어야 한다.

## 12. 제품·수치 경계

이 Spec은 기획 계약이며 제품 코드 변경 권한이 아니다.

```text
EXACT_HEALTH: PENDING_SIMULATION
EXACT_DAMAGE: PENDING_SIMULATION
EXACT_ARMOR_AND_PENETRATION: PENDING_SIMULATION
EXACT_RANGE_AND_SPEED: PENDING_SIMULATION
TOKEN_WEIGHTS: PENDING_SIMULATION
UPGRADE_COSTS: PENDING_ECONOMY
PRODUCT_IMPLEMENTATION: NOT_AUTHORIZED
ART_ASSET_PRODUCTION: NOT_AUTHORIZED
```

현행 `.tres` 병종 수치는 Legacy prototype evidence일 뿐 최신 정본 수치로 승계하지 않는다.

## 13. TDD 수용 계약

후속 구현 계획은 RED 단계에서 최소 다음 실패를 자동 검증한다.

- 4/10 책임 원본이 없거나 중앙 문서가 다른 Decision을 가리킴.
- 로스터 기준선과 `ROSTER_COUNT_IS_NOT_SACRED`가 함께 기록되지 않음.
- 다섯 압력 중 병종 대응 경로가 두 개 미만인 압력이 존재함.
- T3 룰렛 토큰 금지 규칙이 누락됨.
- 병종 시너지가 단순 세트 보너스만으로 정의됨.
- 전열·기동 병영 계열과 공통 지원 계열의 역할이 누락됨.
- 제품 코드·실제 수치가 승인 없이 변경됨.
- Google Sheet가 같은 Decision ID·exact HEAD·4/10을 기록하지 않음.

## 14. 성공 기준

- 각 병종의 역할과 약점을 한 문장으로 설명할 수 있다.
- 같은 압력에 최소 두 병종 대응 경로가 존재한다.
- 같은 병종이 모든 압력의 최적해가 아니다.
- 암살자·기병·비행병의 배치 판단이 서로 다르다.
- 병영 분기가 반대 계열을 영구 삭제하지 않으면서 결과 방향을 바꾼다.
- T1/T2/T3 역할 계보와 룰렛 자산 규칙이 충돌하지 않는다.
- 정확 수치 없이도 Stage·건물·병종의 인과가 검수 가능하다.

## 15. 다음 단계

Spec 승인 뒤 `writing-plans`로 다음 작업을 구체화한다.

1. 병종 정본 자동 계약 테스트 작성과 RED 확인.
2. 책임 원본·적대적 검토·중앙 라우터 작성.
3. 구형 병종·적 계보 문서 lifecycle 분류.
4. Google Sheet Decision·감사·exact HEAD 동기화.
5. GREEN·REFACTOR·fresh PR preflight.
6. 문서 PR 병합 후 다음 5/10 전술스킬·마석 Gate로 이동.
