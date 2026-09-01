# OMENWARD 단일 전선 지휘 화면 · 벤치마킹 역공학

```yaml
record_id: OMW-BENCH-20260901-SINGLE-FRONT-COMMAND-01
created_at: 2026-09-01 KST
status: RESEARCHED__BLUEPRINT_INPUT
scope: SINGLE_FRONT_COMMAND_UI / BATTLE_READABILITY / PROBABILITY_AGENCY
user_request: "블루프린트(와이어프레임, 플로우 맵) 작업 시작 전 비슷한 장르 10개 이상 벤치마킹"
current_product_owner: docs/CURRENT_CONFIRMED_DECISIONS.md
current_visual_owner: docs/design/APPROVED_OMENWARD_BATTLE_PRIMARY_MARCH_MINIMAP_2026-08-30.md
runtime_mutation: NONE
asset_mutation: NONE
source_policy: OFFICIAL_PUBLISHER_OR_STOREFRONT_PAGES_PLUS_USER_PROVIDED_REFERENCE_IMAGES
rights_policy: REFERENCE_ONLY__NO_ASSET_COPY_OR_MODEL_TRAINING_INPUT
```

## 1. 목적과 비교 기준

이 기록은 다른 게임의 아트, 텍스처, UI 배치, 고유 규칙을 복제하기 위한 자료가 아니다. OMENWARD의
현재 정체성인 **플레이어가 구성한 확률 엔진 → 단일 전선 커밋 → 자동전투 → 인과 복기**에 도움이 되는
정보 구조만 분리한다.

비교 기준은 다음 다섯 가지다.

1. 준비 선택이 전투 결과까지 얼마나 읽히는가.
2. 단일 전장의 현재 위험과 전체 진행 맥락을 얼마나 분명히 분리하는가.
3. 병종 역할이 역할 → 무기 → 크기 → 진영색 순으로 빠르게 읽히는가.
4. 제한된 슬롯/공간이 의미 있는 우선순위를 만드는가.
5. RNG가 단순 운이나 사행성 연출이 아니라 설계 가능한 선택으로 보이는가.

## 2. 원출처 기반 사례

| 사례 | 원출처와 관찰 가능한 구조 | OMENWARD 적용 판정 | 프로젝트에 맞춘 차이 |
| --- | --- | --- | --- |
| Slotbound | [공식 Steam 커뮤니티](https://steamcommunity.com/app/4459590/allnews/)는 3×3 슬롯으로 병력을 소환하고 방어 파도에 대비하는 auto-battler 구조를 설명한다. | **ADAPT** | 룰렛 결과가 병력을 만든다는 짧은 인과만 쓴다. 유닛 흡수, 잭팟, 슬롯 자체의 보상 판타지는 쓰지 않는다. |
| Commander Quest | [공식 Steam](https://store.steampowered.com/app/2697930/Commander_Quest/)는 덱 구성, 유닛 상성, 시너지와 auto battle을 결합한다. | **ADOPT** | 내정과 룰렛에서 만든 조합이 전선 전투에서 읽히고 복기되어야 한다. 카드 덱/3D 배치 UI는 복사하지 않는다. |
| Loop Hero | [공식 Steam](https://store.steampowered.com/app/1282730/LoopHero/?l=english)는 카드로 지형·적·건물을 배치하고 원정과 캠프 성장을 연결한다. | **ADAPT** | 건물은 전장 배치물이 아니라 전역 로스터에서 확률·경제 조건을 바꾸는 요소로 변형한다. |
| Thronefall | [공식 Steam](https://store.steampowered.com/app/2239150/Thronefall/)은 낮의 준비와 밤의 방어를 구분하고, 거점·병력·방어의 결과를 짧은 리듬으로 연결한다. | **ADAPT** | `PREPARE → COMMIT → BATTLE → REVIEW`의 위상 구분만 채택한다. 직접 영웅 난전과 지도 건물 설치는 채택하지 않는다. |
| Kingdom Two Crowns | [공식 Steam](https://store.steampowered.com/app/701160/Kingdom_Two_Crowns/)은 자원, 방어, 재탈환, 몬스터 파도를 한 방향 위협 축에서 다룬다. | **ADOPT** | 수호 성채에서 베일 성채로 향하는 하나의 읽기 쉬운 압력 축과 성채 앵커만 채택한다. |
| Bad North | [공식 Steam 발표](https://store.steampowered.com/news/posts/?appgroupname=Bad+North&appids=688420&enddate=1561991839&feed=steam_community_announcements)는 작은 전술 지형과 캠페인 맵을 분리한다. 사용자가 제공한 화면도 소규모 전장과 병력 가독성을 참고한다. | **ADAPT** | 전투 단위의 실루엣 우선 원칙만 적용한다. 섬 단위 전술 격자나 독립 맵 선택은 쓰지 않는다. |
| The Last Spell | [공식 Steam 발표](https://store.steampowered.com/news/posts/?appids=1105670&enddate=1620397804&feed=steam_community_announcements)는 마지막 거점을 대규모 적으로부터 방어하는 전술 구조를 설명한다. | **ADAPT** | 궁수·마법사·전열·지원처럼 역할이 섞인 전투군의 가독성을 적용한다. 턴제 전술 조작은 도입하지 않는다. |
| Dome Keeper | [공식 Steam](https://store.steampowered.com/app/1637320/Dome%20Keeper/)는 자원 탐색·장비 업그레이드·다가오는 적 파도 사이의 준비 시간을 강조한다. | **ADAPT** | 다음 전투 전에 한정된 준비 결정을 내리는 긴장만 활용한다. 채굴/물리 탐색은 범위 밖이다. |
| Backpack Battles | [공식 Steam](https://store.steampowered.com/app/2427700/Backpack_Battles/)은 한정된 인벤토리 공간과 배치 우선순위를 자동전투 결과와 연결한다. | **ADAPT** | 기본 6칸과 점령에 따른 최대 9칸 로스터로 우선순위를 만든다. 격자형 아이템 배치는 사용하지 않는다. |
| Despot's Game | [공식 Steam](https://store.steampowered.com/app/1227280/Despots_Game/)은 조합을 준비한 뒤 자동전투를 관찰하고 다음 선택을 만드는 army battler다. | **ADOPT** | 준비한 병력 조합을 전투 결과와 인과 복기까지 연결한다. 희생 개그·절차적 던전은 범위 밖이다. |
| Vivid Knight | [공식 Steam](https://store.steampowered.com/app/1569090/Vivid_Knight/)은 수집한 동료와 상징 조합으로 파티 역할을 만든다. | **ADAPT** | 룰렛 토큰과 병종 역할의 그룹화를 선명하게 보여 준다. 보석 인벤토리와 동일한 조합 규칙은 쓰지 않는다. |
| Super Fantasy Kingdom | [공식 Steam](https://store.steampowered.com/app/2289750/Super_Fantasy_Kingdom/)은 왕국 재건, 다양한 수호대, 몬스터 군세 방어를 한 run에 묶는다. | **ADAPT** | 전역 내정이 단일 전선 방어를 바꾸는 큰 인과만 사용한다. 도시 건설을 전장 건설로 바꾸지 않는다. |
| Slots & Daggers / Luck be a Landlord | [Slots & Daggers 공식 Steam](https://store.steampowered.com/app/3631290/____Slots__Daggers/)은 슬롯머신과 RPG의 직접 결합을 전면에 둔다. Luck be a Landlord의 공식 Steam 발표도 slot-machine roguelike로 규정한다. | **REJECT** | OMENWARD의 룰렛은 플레이어 구성 확률 엔진이며, 사행성 판타지·잭팟·근접 보상 연출로 포지셔닝하지 않는다. |

## 3. 채택한 역공학 결론

### ADOPT

- **전투 하나, 맥락 하나**: 전투 중에는 가까운 전장 하나가 시각 질량을 가져야 하며, 전체 전진 상태는 별도 전장처럼 경쟁하지 않는 짧은 context strip으로 압축한다.
- **준비의 결과가 보이는 자동전투**: 내정/룰렛/커밋으로 만든 병력과 전투 결과가 Review에서 원인-결과로 이어져야 한다.
- **역할 실루엣 우선**: 전열, 창, 궁수, 마법, 기병을 같은 방패병 그림으로 대체하지 않는다. 역할을 모르는 상태는 가짜 병종 표현보다 정직한 fallback으로 취급한다.
- **제한된 로스터**: 6~9칸의 전역 건물 로스터가 "무엇을 우선 활성화할 것인가"라는 실제 판단을 만든다.

### ADAPT

- Kingdom/Thronefall의 한 방향 압력은 `Ward Citadel → Veil Citadel`의 다섯 구역으로 변형한다.
- Loop Hero의 사전 조건 설계는 전장 건물 배치가 아니라 룰렛 분포·경제를 미리 바꾸는 글로벌 로스터로 변형한다.
- 자동전투 게임의 조합 표현은 병력 재배치가 아니라 비가역 단일 전선 커밋과 전투 후 복기로 변형한다.

### REJECT

- 슬롯머신/카지노/잭팟을 제품 판타지로 쓰는 연출.
- 전장 안의 건설 노드, 건물 모델, 울타리, 바리케이드, 별도 건물 배치 모드.
- 세 개의 병렬 전선, 긴 도로 전체 표시, 개별 유닛을 되풀이하는 미니맵.
- 결과 확정 뒤의 무료 reroll, 병력 판매·회수·재분배.
- 벤치마크 원본의 UI 레이아웃, 텍스처, 폰트, 상징, 고유 메커닉 복제.

## 4. Blueprint에 전달하는 직접 요구

```text
PRIMARY_VISUAL_MASS = BATTLE_FOCUS_VIEWPORT
SECONDARY_VISUAL_MASS = TOP_SINGLE_ROW_MARCH_MINIMAP + PHASE_APPROPRIATE_LOWER_DECK
ONE_PRIMARY_QUESTION_PER_MODE = TRUE
ROLE_READ_ORDER = ROLE -> WEAPON -> SCALE -> FACTION_COLOR -> TIER -> DECORATION
GLOBAL_BUILDING_ROSTER = 6 + STABLE_PLAYER_HELD_CAPTURE_POINTS, MAX 9
GAMBLING_FANTASY_POSITIONING = FORBIDDEN
MAP_BUILDING_PLACEMENT = FORBIDDEN
```

## 5. 증거 경계

- 이 조사는 각 공식 출처에 공개된 게임 구조와 사용자가 제공한 참조 화면을 해석한 결과다. 플레이 시간, 내부 데이터, 접근성, 밸런스, 상업적 성공 원인에 대한 증거는 아니다.
- 벤치마크는 OMENWARD의 승인 결정·코드·자산을 덮어쓰지 않는다. 충돌 시 `CURRENT_CONFIRMED_DECISIONS.md`와 실제 consumer가 항상 우선한다.
- 외부 게임의 이미지·텍스처·폰트·사운드·UI 스크린샷은 OMENWARD 제품 자산이 아니다. 이후 생성 자산은 독립 brief, repository path, SHA-256, provenance, approval 상태, consumer를 별도로 기록한다.
