# C1 승인 룰렛 계약 복구 — 구현·정본 Shortlist

- 기준: `076b43d199fb3d76caa96c022ecd2aa80c3f63d7`
- 선택 파일: 23

## 선택 경로
- `docs/design/APPROVED_BUILDINGS_TACTICAL_MERCENARY_POC_V1.md` — ACTIVE / 149 lines
- `docs/design/APPROVED_ROULETTE_CORE_RULES.md` — ACTIVE / 270 lines
- `docs/design/APPROVED_ROULETTE_PROBABILITY_TARGETS_POC_V1.md` — ACTIVE / 138 lines
- `docs/design/APPROVED_STAGE_ECONOMY_AND_BUILDING_COST_BASELINE_V1.md` — ACTIVE / 533 lines
- `docs/design/APPROVED_UNIT_GRADE_AND_ABILITY_GROWTH.md` — ACTIVE / 240 lines
- `scenes/ui/stage_hud.tscn` — ACTIVE / 121 lines
- `scripts/battle/battle_simulator.gd` — ACTIVE / 139 lines
- `scripts/battle/unit_instance.gd` — ACTIVE / 139 lines
- `scripts/buildings/building_service.gd` — ACTIVE / 97 lines
- `scripts/core/determinism_service.gd` — ACTIVE / 24 lines
- `scripts/core/stage_run.gd` — ACTIVE / 120 lines
- `scripts/data/building_definition.gd` — ACTIVE / 7 lines
- `scripts/data/unit_spawn_definition.gd` — ACTIVE / 24 lines
- `scripts/data/wave_definition.gd` — ACTIVE / 20 lines
- `scripts/roulette/roulette_service.gd` — ACTIVE / 40 lines
- `scripts/ui/stage_hud.gd` — ACTIVE / 71 lines
- `scripts/units/deployment_service.gd` — ACTIVE / 28 lines
- `tests/README.md` — ACTIVE / 3 lines
- `tests/headless/battle_simulation_test.gd` — ACTIVE / 163 lines
- `tests/headless/economy_roulette_test.gd` — ACTIVE / 128 lines
- `tests/headless/stage_data_contract_test.gd` — ACTIVE / 152 lines
- `tests/headless/stage_run_test.gd` — ACTIVE / 109 lines
- `tests/python/test_skill_routing_contract.py` — ACTIVE / 63 lines

## `docs/design/APPROVED_BUILDINGS_TACTICAL_MERCENARY_POC_V1.md`

Category: `ACTIVE` / 149 lines

```text
# 승인된 건물 성장·전술 명령·용병 PoC V1

- 상태: **구조 승인 / 수치·이름은 첫 PoC 가설**
- 작성일: 2026-07-16
- 경제 기준: `APPROVED_STAGE_ECONOMY_AND_BUILDING_COST_BASELINE_V1.md`

## 1. 기본 병영 Tier 3

- 부모 T2 병종의 상위 분기 하나와 운영 교리 하나를 선택한다.
- Tier 3 업그레이드 비용: 보병 75, 기병 90.
- 업그레이드 시간: 보병 40초, 기병 50초.
- 생산시간: 부모 T2 ×1.15 뒤 교리 적용.
- 세부 병종 분기는 `APPROVED_PLAYER_TEN_UNIT_LINEAGES_POC_V1.md`를 따른다.

## 2. 특수병단 Tier 3

특수병단도 부모 계열 안에서 역할을 분화한다.

| T2 | T3 분기 | 비용 | 시간 |
|---|---|---:|---:|
| 사제단 | 치유사제단 / 전쟁사제단 | 100 | 55초 |
| 마도단 | 원소술단 / 주술단 | 110 | 60초 |
| 비행단 | 천공창단 / 폭풍익단 | 125 | 65초 |
| 거인단 | 파성거인단 / 고대거신단 | 150 | 75초 |

- Tier 1 준비 할인은 Tier 3 비용에 적용하지 않는다.
- Tier 3 완료 뒤 자동생산 병종과 토큰 계열은 부모를 유지한다.
- 상위 등급 룰렛 템플릿은 계열 고정이며 T3 분기는 패시브 방향만 반영한다.

## 3. 농장 성장

### Tier 1 농장
- 비용 35, 건설 20초, 식량 +6.

### Tier 2 곡물창고
- 비용 45, 업그레이드 25초, 추가 식량 +6.

### Tier 3 분기

| 분기 | 비용 | 효과 |
|---|---:|---|
| 대형 곡물창고 | 70 | 추가 식량 +10 |
| 야전 취사장 | 70 | 추가 식량 +4, 같은 라인 출격 유닛 전투 후 회복속도 +20% |

- 취사장 효과는 전투 중 직접 치유가 아니다.
- 동일 취사장 효과는 중첩하지 않는다.

## 4. 시장 성장

### Tier 1 시장
- 비용 50, 건설 25초, 20초마다 +4금화.

### Tier 2 분기

| 분기 | 비용 | 시간 | 효과 |
|---|---:|---:|---|
| 교역소 | 70 | 35초 | 시장 수입 +2, 즉 20초마다 +6 |
| 군수상회 | 70 | 35초 | 전술 명령 비용 -15%, 용병 구매비 -10% |

### Tier 3 분기

| 부모 | 분기 | 비용 | 효과 |
|---|---|---:|---|
| 교역소 | 왕립 거래소 | 110 | 20초마다 +9, 두 번째 이후 시장 비용 증가량 -5 |
| 군수상회 | 전선 보급소 | 110 | 전술 명령 비용 -25%, 이동권 가격 증가량 절반 |

- 시장 할인은 strongest-only다.
- 시장 자체 수입은 각 건물별로 합산한다.

## 5. 포탑 성장

### Tier 1 포탑
- 비용 35, 건설 22초.
- HP 500, 공격 18, 간격 1초, 사거리 270.

### Tier 2

| 분기 | 비용 | 시간 | 역할 |
|---|---:|---:|---|
| 연발포탑 | 55 | 30초 | 경장갑·군집·비행 지속 사격 |
| 노포탑 | 60 | 35초 | 대형·기병·중장갑 높은 단발 |

### Tier 3

| 부모 | 분기 | 비용 | 효과 |
|---|---|---:|---|
| 연발포탑 | 폭풍연발포 | 85 | 대공 우선·공격속도·연쇄 2기 |
| 노포탑 | 파성노포 | 90 | 대형·구조물·보스 방어 파쇄 |

- 포탑은 중앙 접전지에 건설할 수 없다.
- 포탑만으로 전선을 밀 수 없고 점령 기여도는 없다.

## 6. 전술 명령

| 명령 | 비용 | 재사용 | 첫 PoC 효과 |
|---|---:|---:|---|
| 바리케이드 | 12 | 30초 | HP 350, 시전 1.5초, 지속 18초, 라인당 1개 |
| 화살비 | 25 | 35초 | 반경 150, 3초간 5회, 회당 24 물리, 비행 포함 |
| 강화지대 | 25 | 40초 | 반경 180, 8초, 피해 +12%, 받는 피해 -10% |
| 역병 | 30 | 45초 | 반경 160, 8초, 초당 12 마법, 회복 -35%, 보스 피해 50% |

- 전역 쿨다운은 없다.
- 동일 강화지대는 중첩하지 않는다.
- 역병의 최대 체력 비례 피해는 사용하지 않는다.
- 일시정지 중 목표 지정·비용 지불은 가능하고 시간은 멈춘다.

## 7. 용병 상점

- 기본 재고 3칸.
- 활성 전투 시간 120초마다 자동 갱신.
- 수동 갱신 비용 15, 갱신마다 +5, 최대 40.
- 일반·엘리트만 판매한다. 영웅·전설은 판매하지 않는다.
- 용병은 건물 토큰을 추가하지 않는다.
- 구매한 용병은 결과 보관함으로 들어가며 식량은 배치 시 사용한다.

### 가격 가설

| 등급·유형 | 가격 |
|---|---:|
| 기본 일반병 | 25~35 |
| 전문 일반병 | 40~55 |
| 특수 일반병 | 65~90 |
| 기본 엘리트 | 70~90 |
| 특수 엘리트 | 110~140 |

### 용병 전용 후보

- 공병: 건물 수리·건설 보조.
- 정찰병: 다음 웨이브 세부 정보를 15초 일찍 공개.
- 의무병: 전투 후 회복.
- 사냥꾼: 대형·비행 표식 대응.

용병 전용 병종은 기본 10병종 역할을 완전히 대체하지 않는다.

## 8. 건설 체력·취소

- 건설 시작 HP는 완공 HP의 25%.
- 진행률에 따라 최대 HP가 선형 증가한다.
- 현재 HP 비율은 최대 HP 증가 시 유지한다.
- 건설 취소 70%, 업그레이드 취소 50%, 완공 철거 40%, 적 파괴 0% 환불.
- 특수병단 T2 취소 시 준비도 0초.

## 9. 검증 기준

- 시장 2동 이상이 모든 정상 빌드의 필수 선택이 되지 않는다.
- 포탑 중심 빌드도 병력·전술 없이 적 본진을 파괴할 수 없다.
- 특수병단 T3는 기본 병영 T3보다 강하지만 투자·생산·식량 부담이 더 크다.
- 전술 명령 반복으로 보스를 영구 지연할 수 없다.
- 용병은 룰렛 실패 복구 수단이지만 상위 등급 획득의 주 경로가 아니다.

```

## `docs/design/APPROVED_ROULETTE_CORE_RULES.md`

Category: `ACTIVE` / 270 lines

```text
# 승인된 룰렛 핵심 규칙

- 상태: **핵심 구조·등급 생성·병영 출처 추첨 승인됨 / 세부 확률 일부 미확정**
- 승인일: 2026-07-14
- 관련 문서:
  - `docs/design/APPROVED_UNIT_GRADE_AND_ABILITY_GROWTH.md`
  - `docs/design/APPROVED_BARRACKS_TIER3_EVOLUTION_AND_GRADE_SKILLS.md`
  - `docs/design/APPROVED_ECONOMY_BUILDS_AND_TERMINAL_ASSAULT.md`

## 1. 기본 판정 줄

- 기본 판정 줄은 3×3 보드의 가운데 가로줄이다.
- 상단·하단 판정은 아이템 효과가 있을 때만 허용한다.
- 판정 줄은 회전 비용을 지불한 시점에 고정한다.
- 회전 도중 장비·아이템 변경으로 판정 줄을 바꾸지 못한다.

## 2. 기본 보상 조건

판정 줄의 세 칸이 동일한 비-X 심벌일 때만 보상을 판정한다.

```text
[전사, 전사, 전사] → 전사 계열 보상
[기병, 기병, 기병] → 기병 계열 보상
[기병, 기병, 궁병] → 보상 없음
[기병, 기병, X] → 보상 없음
[X, X, X] → 보상 없음
```

- 동일 심벌 1개 또는 2개는 보상 없음
- 혼합 심벌은 종류별 분할 보상 없음
- 판정 줄이 일치하면 해당 심벌을 판정 심벌로 고정하고 전체 8개 줄을 검사한다.

## 3. 완성 줄 계산

검사 대상:

- 가로 3줄
- 세로 3줄
- 대각선 2줄

- 판정 심벌과 같은 심벌로 완성된 줄만 센다.
- 판정 줄도 완성 줄 하나에 포함한다.
- 겹치는 줄도 각각 계산한다.
- 판정 줄이 완성되지 않았다면 다른 위치의 완성 줄도 무시한다.

## 4. 룰렛 등급

| 동일 심벌 완성 줄 | 생성 등급 |
|---:|---|
| 1줄 | 일반 |
| 2줄 | 엘리트 |
| 3~7줄 | 영웅 |
| 8줄·9칸 전체 동일 | 전설 |

- `신화` 명칭은 사용하지 않고 `전설` 명칭을 유지한다.
- 등급은 최종 보드 확정 시점에 결정한다.
- 수동 합성, 처치 경험치와 건물 Tier로 등급이 상승하지 않는다.
- 병영 Tier는 일반·엘리트·영웅·전설 확률에 영향을 주지 않는다.
- 병영 자동 생산은 항상 일반 등급이다.

## 5. 전설 제한

- 전설은 한 스테이지 전체에서 병종과 관계없이 1회만 생성한다.
- 전설 생성 뒤 다시 9칸 동일 유닛 심벌이 나오면 해당 계열 영웅 2명으로 변환한다.
- 전설 사용 여부를 룰렛 UI에 항상 표시한다.
- 금화 심벌은 전설 등급을 만들지 않는다.

## 6. 계열별 공유 병종 토큰

같은 기본 병종 계열은 Tier와 세부 병종이 달라도 동일한 룰렛 심벌을 사용한다.

### 전사 토큰

- Tier 1 검사
- Tier 2 방패병·대검병·광전사 후보
- 향후 Tier 3 전사 계열 세부 병종

### 기병 토큰

- Tier 2 기병
- Tier 3 중기병·충격기병

### 궁병 토큰

- Tier 2 궁병
- Tier 3 석궁병·대공궁병·연사궁병

### 창병 토큰

- Tier 2 창병
- 향후 Tier 3 창병 세부 병종

병영 한 동은 기본적으로 각 릴에 해당 공유 토큰 1개를 제공한다.

```text
Tier 1 검사 병영 1개
Tier 2 방패병 병영 1개
→ 각 릴 전사 토큰 총 2개
```

```text
Tier 2 기병 병영 1개
Tier 3 중기병 병영 1개
→ 각 릴 기병 토큰 총 2개
```

토큰 외형은 같지만 내부 원장에는 출처 병영 ID·Tier·세부 병종·후보 가중치와 패시브 성장 단계를 보존한다.

## 7. 유닛 보상 결정 순서

```text
1. 룰렛 보드와 판정 줄 확정
2. 동일 심벌 완성 줄 수로 등급 확정
3. 당첨된 기본 병종 계열의 병영 출처 후보 풀 생성
4. 가중치로 실제 훈련 출처 병영 선택
5. 일반 등급이면 선택 출처의 실제 병종 생성
6. 엘리트·영웅·전설이면 계열별 고정 유닛 생성
7. 선택된 병영 Tier로 핵심 패시브 생성·강화 적용
8. 룰렛 등급으로 일반 스킬 생성·강화 적용
```

## 8. 병영 출처 가중치

핵심 원칙:

- 높은 Tier 일반 병종 후보가 낮은 Tier 후보보다 높은 가중치를 가진다.
- 낮은 Tier 병영이 남아 있으면 낮은 Tier 병종도 계속 등장할 수 있다.
- 정확한 가중치는 데이터로 조정한다.

초기 추천:

| 출처 | 추천 가중치 |
|---|---:|
| Tier 1 | 1 |
| Tier 2 | 2 |
| Tier 3 | 3 |

기병·궁병·창병처럼 Tier 1 후보가 없는 계열은 Tier 2와 Tier 3만 비교한다. 이 경우 기존 1:2 비율도 후보이며 최종 값은 플레이테스트로 결정한다.

## 9. 일반 등급 결과

일반 등급에서는 선택된 병영 출처의 실제 생산 병종을 생성한다.

- Tier 1 전사 출처 → 일반 검사
- Tier 2 전사 출처 → 선택한 일반 전사 병종
- Tier 2 기병 출처 → 일반 기병
- Tier 3 중기병 출처 → 일반 중기병
- Tier 3 충격기병 출처 → 일반 충격기병
- Tier 3 대공궁병 출처 → 일반 대공궁병

## 10. 고정 상위 등급 결과

엘리트·영웅·전설은 기본 병종 계열별 고정 유닛이다.

- 전사 계열 상위 등급은 전사 계열 고정 템플릿
- 기병 계열 상위 등급은 중기병·충격기병 선택과 무관하게 고정
- 궁병 계열 상위 등급은 석궁병·대공궁병·연사궁병 선택과 무관하게 고정
- 창병 계열 상위 등급은 창병 계열 고정 템플릿

선택된 훈련 출처 Tier는 고정 상위 등급 유닛의 패시브 단계에 적용한다.

### 병영 Tier별 패시브

- Tier 1: 패시브 1 기본형
- Tier 2: 패시브 1 강화 + 패시브 2 생성
- Tier 3: 패시브 1 추가 강화 + 패시브 2 강화 + 패시브 3 생성

### 등급별 일반 스킬

- 일반: 1스킬
- 엘리트: 1스킬 강화
- 영웅: 강화된 1스킬 + 2스킬 생성
- 전설: 영웅 효과 + 2스킬 강화 + 3스킬 생성

## 11. 금화 심벌

판정 줄이 금화 3개일 때 전체 금화 완성 줄 수를 센다.

| 금화 완성 줄 | 보상 |
|---:|---:|
| 1줄 | 실제 회전 비용의 75% |
| 2줄 | 실제 회전 비용의 200% |
| 3줄 이상 | 실제 회전 비용의 500% |

```text
금화 보상 = floor(실제 지불한 회전 비용 × 환급 비율)
```

- 할인 후 실제 지불액 기준
- 금화 9칸 전체 동일도 500% 상한
- 금화에는 유닛 등급을 적용하지 않음
- 별도 회전 충전, 웨이브당 횟수 제한과 연속 감쇠 없음

## 12. 럭키 찬스

```text
기본 확률: 12%
자연 실패 1회당: +8%p
6회 연속 자연 실패 후 다음 회전: 100%
자연 발생 뒤: 현재 기본 확률로 초기화
```

- 현재 확률과 확정까지 남은 실패 횟수 공개
- 행운 아이템은 초기 기본 확률 상승
- 자연 럭키 찬스는 무료 행·열 이동 1회 제공

## 13. 이동권

- 자연 럭키 찬스와 이동권을 같은 회전에 함께 사용 가능
- 회전당 이동 횟수 상한 없음
- 실제 상한은 보유 이동권 수
- 이동권 1장당 행 또는 열 1칸 순환 이동 1회
- 여러 이동을 계획하고 되돌리기·전체 초기화 가능
- 최종 확정 시에만 이동권 소비
- 최종 확정 뒤 보상은 한 번만 계산

## 14. 결과 보관함

- 유닛 보상은 공간 부족으로 사라지지 않는다.
- 결과 보관함에 생성한 뒤 대기칸 이동·즉시 출전·판매로 정리한다.
- 보관함이 남아 있으면 다음 룰렛 회전만 차단한다.
- 전투·건설·카메라·기존 유닛 배치는 계속 가능하다.
- 금화 보상은 즉시 지급한다.

## 15. UI 계약

룰렛 전:

- 릴별 공유 토큰 수
- 병종 계열별 당첨 확률
- 일반 등급의 실제 세부 병종별 확률
- Tier별 훈련 출처 확률
- Tier별 패시브 해금·강화 내용

룰렛 결과:

- 완성 줄 수와 등급
- 기본 병종 계열
- 실제 생성 유닛
- 선택된 출처 병영과 Tier
- 생성·강화된 핵심 패시브
- 생성·강화된 일반 스킬
- 전설 사용 여부

## 16. 검증 계약

- 기본 상태에서는 중앙 가로줄만 판정한다.
- 혼합 줄과 2개 일치는 보상을 만들지 않는다.
- 1/2/3~7/8줄은 일반/엘리트/영웅/전설로 매핑된다.
- Tier 1 검사와 Tier 2 이상 전사 계열은 전사 토큰을 공유한다.
- 같은 계열의 Tier 2·Tier 3 병영은 같은 심벌을 제공한다.
- 높은 Tier 후보의 가중치는 낮은 Tier보다 높다.
- 일반 등급은 선택 출처의 실제 병종을 생성한다.
- 엘리트·영웅·전설은 세부 병종과 무관한 고정 계열 유닛을 생성한다.
- 선택 출처 Tier가 패시브 해금과 강화 단계를 결정한다.
- 엘리트는 1스킬을 강화한다.
- 영웅은 2스킬을 생성한다.
- 전설은 2스킬을 강화하고 3스킬을 생성한다.
- 전설은 한 스테이지 1회 제한을 지킨다.
- 같은 시드·회전 스냅샷·최종 보드는 같은 결과를 만든다.

## 17. 미확정 세부

- 전사 계열 Tier 2 병종의 최종 명칭과 수치
- Tier별 정확한 후보 가중치
- 계열별 고정 엘리트·영웅·전설 유닛
- 대기칸 기본 용량과 결과 보관함 UI
- 판정 줄 변경·행운·이동권 아이템 세부

이 문서는 핵심 구조를 승인하지만 개별 수치를 구현 승인으로 간주하지 않는다. Godot 구현은 별도 Codex Plan Mode 제안서와 사용자 승인을 거쳐야 한다.

```

## `docs/design/APPROVED_ROULETTE_PROBABILITY_TARGETS_POC_V1.md`

Category: `ACTIVE` / 138 lines

```text
# 승인된 룰렛 확률·등급·금화 기대값 PoC V1

- 상태: **확률 구조·목표 분포 승인 / 릴 가중치는 첫 시뮬레이션 가설**
- 작성일: 2026-07-16
- 적용 범위: 3×3 룰렛, 건물 토큰, X·금화·이동권, 럭키 찬스, 등급 결과

## 1. 기본 판정

- 중앙 가로줄은 기본 판정줄이다.
- 같은 비-X 심벌 3개가 완성된 판정줄만 보상한다.
- 완성 줄 수 1/2/3~7/8은 일반/엘리트/영웅/전설이다.
- 9칸 동일은 첫 전설 획득 전에는 전설, 이후에는 영웅 2기다.
- 전설은 한 스테이지당 1회다.

## 2. 릴 가중치 구조

각 릴은 고정 유틸리티 가중치와 활성 건물 토큰 가중치를 합친다.

```text
기본 고정 가중치 / 릴
X 6
금화 2
이동권 1

활성 생산시설
기본 병영 계열 토큰 +3
특수병단 계열 토큰 +2
토큰 증폭 교리 +1
```

- 한 건물의 전문화 전환은 다음 회전부터 기존 토큰을 새 토큰으로 교체한다.
- 같은 계열 건물이 여러 동이면 가중치를 합산한다.
- 특수 토큰은 강한 결과이므로 기본 병영보다 낮은 가중치로 시작한다.
- 세 릴은 같은 계열 구성을 사용하되 정지 순서와 시드는 독립이다.

## 3. 목표 자연 확률

이동권 사용 전 1회 회전의 목표 범위다.

| 결과 | 목표 확률 |
|---|---:|
| 보상 없음 | 55~68% |
| 일반 1줄 | 22~32% |
| 엘리트 2줄 | 5~9% |
| 영웅 3줄 이상 | 1.0~2.5% |
| 전설 8줄 이상 | 0.10~0.35% |

- 첫 10회 안에 자연 일반 결과를 90% 이상 경험해야 한다.
- 이동권과 럭키 찬스를 포함한 건강한 플레이에서 스테이지당 영웅 1~3기, 전설 0~1기를 목표로 한다.
- 전설 미획득 상태에서 15웨이브까지 전설 확률 누적 목표는 25~45%다.

## 4. 럭키 찬스

```text
시작 12%
실패마다 +8%p
6회 실패 뒤 다음 회전 확정
```

럭키 발동 시:

1. 회전 결과를 생성한다.
2. 완성 줄이 없으면 현재 토큰 풀에서 가장 가까운 1줄 후보를 선택한다.
3. 한 칸을 결정론적으로 교체해 최소 일반 1줄을 만든다.
4. 이미 보상이 있으면 결과를 바꾸지 않는다.

- 럭키는 등급을 직접 올리지 않는다.
- 럭키로 만들어진 줄도 일반 판정과 동일하게 이동권 조작이 가능하다.
- 성공 후 확률은 12%로 초기화한다.

## 5. 이동권

- 자연 이동과 아이템 이동권을 한 회전에 함께 사용할 수 있다.
- 첫 PoC 보유 상한은 5개다.
- 상점 기본 가격은 18금화, 같은 스테이지 구매마다 +4금화다.
- 행·열 이동 1회마다 이동권 1개를 사용한다.
- 결과 확정 전에는 되돌리기 1회를 무료로 허용하되 다른 이동을 확정하면 무료 되돌리기는 사라진다.

## 6. 금화 기대값

기본 회전비 20 기준:

| 금화 줄 | 지급 |
|---|---:|
| 1줄 | 15 |
| 2줄 | 40 |
| 3줄 이상 | 100 |

목표:

```text
장기 평균 금화 지급 <= 회전당 6
순 회전 비용 >= 평균 14
```

- 무료 회전도 지급 기준 회전비 20을 사용한다.
- 금화 결과로 자동 재회전하지 않는다.
- 금화 가중치는 시장·난이도와 무관하게 기본 2로 시작한다.

## 7. 출처 후보

같은 토큰 계열의 여러 건물이 있을 때:

| 출처 | 가중치 |
|---|---:|
| T1 | 1 |
| T2 | 2 |
| T3 | 3 |

- 일반 결과는 선택된 실제 건물 병종을 생성한다.
- 엘리트 이상은 계열 고정 템플릿을 생성하고 선택 출처 Tier의 패시브 단계만 적용한다.
- 파괴된 건물은 다음 회전부터 후보에서 제거한다.

## 8. 결과 보관함

- 기본 보관 슬롯 3개.
- 보관 중인 결과는 식량을 사용하지 않는다.
- 동일 결과를 2개 이상 합성해 승급할 수 없다.
- 슬롯 초과 시 새 결과를 버리거나 기존 결과와 교체한다.
- 전설 결과는 버리기 전에 한 번의 확인을 요구한다.

## 9. 시뮬레이션 검증

구현 전 또는 구현 초기에 최소 100,000시드를 검증한다.

- 건물 1/2/4/6동 조합.
- 기본 병영만, 특수병단 혼합, 시장 중심 빌드.
- 이동권 0/2/5개.
- 럭키 없음/기본/최대 실패 보호.
- 금화 평균 지급과 파산 확률.
- 영웅·전설 최초 획득 웨이브 분포.

실패 기준:

- 무조작 전설 확률이 0.5%를 초과.
- 금화 평균 지급이 6을 초과.
- 건물을 늘릴수록 원하는 토큰의 절대 확률이 비정상적으로 감소.
- 특수병단 하나가 모든 기본 토큰보다 자주 등장.

```

## `docs/design/APPROVED_STAGE_ECONOMY_AND_BUILDING_COST_BASELINE_V1.md`

Category: `ACTIVE` / 533 lines

```text
# 승인된 정규 스테이지 경제·건물 비용 기준표 V1

- 상태: **경제 구조 승인 / 금화·비용·시간은 첫 PoC 기준값으로 승인하며 플레이테스트 조정 가능**
- 작성일: 2026-07-15
- 적용 범위: 정규 15분 스테이지 시작 자원, 시간 수입, 접전지 수입, 룰렛 비용, 기본 건물 비용, 기본 병영 Tier 2 비용, 시장, 농장, 전술 명령 비용, 환불 규칙
- 연결 문서:
  - `docs/design/APPROVED_BARRACKS_AND_SPECIAL_CORPS_UNIT_TREE_V5.md`
  - `docs/design/APPROVED_SPECIAL_CORPS_BUILDING_AND_GIANT_CLASS_V3.md`
  - `docs/design/APPROVED_BUILDING_SPECIALIZATION_AND_TACTICAL_COMMANDS.md`
  - `docs/design/APPROVED_15_WAVE_STAGE_CLOCK_AND_OVERTIME_V2.md`
- 우선순위:
  - 특수병단 비용·시간은 V5/V3 계약을 그대로 사용한다.
  - 금화 룰렛 지급률은 기존 75%/200%/500% 계약을 유지한다.
  - 튜토리얼은 필요하면 별도 시작 자원·무료 회전을 사용하며 이 문서는 정규 스테이지 기준이다.

---

## 1. 경제 목표

정규 스테이지 경제는 다음 선택을 모두 성립시켜야 한다.

```text
안정 병력
→ 기본 병영·농장·포탑 투자

경제 운영
→ 시장 투자 뒤 중후반 금화 우위

특수병단 조기 전환
→ 높은 비용을 지불하고 특수 토큰·자동생산 조기 확보

특수병단 준비 전환
→ 150초를 기다려 Tier 2 비용 최대 50% 절감

룰렛 집중
→ 건물을 최소화하고 즉시 병력·상위 등급 기대값 확보
```

고정 원칙:

- 적 개별 처치 금화를 제공하지 않는다.
- 웨이브 클리어 고정 금화를 제공하지 않는다.
- 주요 확정 수입은 기본 시간 수입, 시장, 중앙 접전지 통제다.
- 확률 수입은 금화 룰렛 결과로 제한한다.
- 약한 적을 남겨두고 파밍하거나 공세를 의도적으로 지연해 이득을 얻을 수 없어야 한다.
- 일시정지 중에는 모든 시간 기반 수입과 생산이 멈춘다.

---

## 2. 시작 자원

정규 스테이지 Normal 초기값:

```text
starting_gold = 160
starting_food_cap = 12
starting_food_used = 배치된 초기 유닛 기준
```

- 시작 금화는 기본 병영·포탑·농장을 지은 뒤 룰렛 2회를 돌릴 수 있는 수준이다.
- 특수병단 즉시 전문화도 가능하지만 다른 방어 투자를 크게 포기해야 한다.
- 캠페인 제약·난이도는 시작 금화를 데이터로 변경할 수 있다.
- 튜토리얼의 강제 건설·무료 룰렛은 별도 TutorialManifest가 우선한다.

---

## 3. 기본 시간 수입

```text
base_income_amount = 5 gold
base_income_interval_seconds = 20
```

활성 전투 시간 기준:

| 시간 | 누적 기본 수입 |
|---:|---:|
| 1분 | 15 |
| 5분 | 75 |
| 10분 | 150 |
| 15분 | 225 |

규칙:

- 첫 지급은 활성 전투 시간 20초에 발생한다.
- 일시정지 중 지급 타이머가 멈춘다.
- 이전 공세가 남아 있어도 지급은 계속된다.
- 본진이 파괴되거나 패배가 확정된 뒤에는 지급하지 않는다.
- 기본 수입은 시장 수와 무관하게 유지된다.

---

## 4. 중앙 접전지 통제 수입

각 라인의 중앙 접전지는 경제 보상을 제공한다.

```text
control_income_amount_per_point = 4 gold
control_income_interval_seconds = 60
```

- 활성 전투 시간 `1:00, 2:00, 3:00 ...` 시점마다 판정한다.
- 해당 시점에 아군이 점령한 중앙 접전지 한 곳당 4금화를 지급한다.
- 중립 또는 적 점령 상태에서는 지급하지 않는다.
- 최대 세 곳이므로 분당 최대 12금화다.
- 일시정지는 판정 시점도 정지시킨다.
- 점령 직전·직후의 경계는 해당 시뮬레이션 틱의 확정 점령 상태를 사용한다.
- 적 본진 접전지와 아군 본진 접전지는 이 수입을 제공하지 않는다.

15분 누적 예시:

| 평균 아군 점령 수 | 누적 통제 수입 |
|---:|---:|
| 0개 | 0 |
| 1개 | 60 |
| 1.5개 | 90 |
| 2개 | 120 |
| 3개 | 180 |

전선 우위를 금화로 전환하지만 개별 적 처치 보상보다 폭발적인 스노우볼은 낮다.

---

## 5. 기본 건물 비용

| 건물 | 금화 | 건설시간 | 기본 효과 |
|---|---:|---:|---|
| 기본 병영 Tier 1 | 40 | 20초 | 검사 자동생산·전사 토큰 |
| 특수병단 Tier 1 | 40 | 25초 | Tier 2 준비 할인 축적 |
| 농장 Tier 1 | 35 | 20초 | 식량 한도 +6 |
| 시장 Tier 1 | 50 | 25초 | 20초마다 금화 +4 |
| 포탑 Tier 1 | 35 | 22초 | 기본 방어 사격 |

- 비용은 건설 명령 확정 시 전액 선불이다.
- 건설 중에는 건물 기능이 작동하지 않는다.
- 적이 있어도 건설은 진행되며 완공 전에 파괴될 수 있다.
- 일시정지 중 건설 명령은 확정할 수 있지만 진행시간은 멈춘다.
- 포탑 전투 수치는 튜토리얼 전투 기준 문서가 우선한다.

---

## 6. 기본 병영 Tier 2 비용

| 전문화 | 금화 | 업그레이드 시간 | 초기 식량 | 역할 |
|---|---:|---:|---:|---|
| 방패병 | 45 | 25초 | 2 | 범용 전열 유지 |
| 대검전사 | 50 | 30초 | 2 | 정면 광역·파쇄·격노 |
| 암살자 | 55 | 30초 | 2 | 같은 라인 후열 제거 |
| 창병 | 45 | 25초 | 2 | 돌진·기병·대형 대응 |
| 궁병 | 50 | 25초 | 2 | 지속 원거리·대공 |
| 기병 | 65 | 35초 | 3 | 기동·돌진·후열 압박 |

공통 규칙:

- 업그레이드 중에는 Tier 1 검사 생산과 전사 토큰을 유지한다.
- 생산 진행률을 보존한다.
- 완료 뒤 처음 완성되는 생산분부터 선택 병종으로 변경한다.
- 진행 중인 룰렛은 유지하고 다음 회전부터 토큰 변경을 적용한다.
- 자동생산은 일반 등급만 생성한다.
- 기본 병영 Tier 3 비용은 상위 병종과 운영 교리 수치 확정 뒤 별도 승인한다.

---

## 7. 특수병단 Tier 2 비용

V5 계약을 유지한다.

| 전문화 | 원가 | 준비 최대 할인 비용 | 업그레이드 | 일반 생산 | 식량 |
|---|---:|---:|---:|---:|---:|
| 사제단 | 60 | 30 | 30초 | 180초 | 3 |
| 마도단 | 70 | 35 | 35초 | 210초 | 3 |
| 비행단 | 80 | 40 | 40초 | 240초 | 4 |
| 거인단 | 100 | 50 | 45초 | 300초 | 6 |

준비 할인:

```text
30초마다 Tier 2 금화 비용 -10%
150초에 -50% 최대
```

- 할인은 Tier 2 금화 비용에만 적용한다.
- Tier 1 건설비 40은 할인하지 않는다.
- 업그레이드 시간은 할인하지 않는다.
- 전문화 시작 순간 할인율과 실제 지불액을 고정한다.
- 자동생산은 일반 등급만 생성한다.
- 상위 등급 특수 유닛은 룰렛으로만 획득한다.

---

## 8. 시장 Tier 1

```text
market_base_cost = 50
market_construction_time = 25
market_income_amount = 4
market_income_interval_seconds = 20
```

한 시장의 수입:

| 운영시간 | 누적 수입 |
|---:|---:|
| 1분 | 12 |
| 5분 | 60 |
| 10분 | 120 |

첫 시장은 완공 뒤 약 4분 10초 운영하면 건설비를 회수한다.

### 시장 중복 건설 비용

```text
nth_market_cost = 50 + 25 × (현재 존재하거나 건설 중인 시장 수)
```

| 건설 순서 | 비용 | 완공 후 투자 회수시간 |
|---:|---:|---:|
| 1번째 | 50 | 약 4분 10초 |
| 2번째 | 75 | 약 6분 15초 |
| 3번째 | 100 | 약 8분 20초 |
| 4번째 | 125 | 약 10분 25초 |

- 시장마다 수입 타이머를 독립적으로 가진다.
- 첫 수입은 완공 후 활성 전투 시간 20초가 지나야 지급한다.
- 일시정지 중에는 시장 수입이 멈춘다.
- 시장이 파괴되면 해당 수입과 진행 중 타이머를 잃는다.
- 건설 중·활성·업그레이드 중 시장을 중복 비용 계산에 포함한다.
- 철거·파괴 뒤 현재 시장 수가 줄면 다음 신규 시장의 비용도 다시 낮아진다.
- 시장 Tier 2 전문화와 추가 경제 기능은 별도 작업에서 확정한다.

시장은 장기적으로 강하지만 후방 건설 노드, 초기 금화와 즉시 전투력을 포기한다.

---

## 9. 농장과 식량

### 농장 Tier 1

```text
farm_gold_cost = 35
farm_construction_time = 20
food_cap_bonus = 6
```

### 농장 Tier 2 초기 경제값

```text
farm_tier2_gold_cost = 45
farm_tier2_upgrade_time = 25
additional_food_cap_bonus = 6
```

따라서 Tier 2 농장 한 동은 총 식량 한도 +12를 제공한다.

식량 규칙:

- 시작 식량 한도는 12다.
- 전장에 배치되거나 출격 대기열에서 인도된 유닛만 식량을 점유한다.
- 결과 보관함과 아직 배치하지 않은 대기 결과는 식량을 사용하지 않는다.
- 유닛 사망·영구 퇴각 시 식량을 반환한다.
- 식량 한도를 초과해도 기존 유닛은 유지한다.
- 신규 자동생산·배치만 차단한다.
- 자동생산 완료 시 식량이 부족하면 건물 안 `완성 대기` 한 기만 유지한다.
- 농장이 파괴되어 한도가 현재 사용량보다 낮아져도 기존 유닛을 제거하지 않는다.

초기 병종별 식량:

```text
검사 1
기본 병영 Tier 2 보병 2
기병 3
사제 3
마법사 3
비행병 4
거인 6
```

---

## 10. 룰렛 비용과 금화 결과

```text
base_spin_cost = 20 gold
```

- 정규 스테이지 기본 회전비는 고정 20금화다.
- 같은 웨이브에서 여러 번 돌려도 기본 비용이 상승하지 않는다.
- 무료 튜토리얼 회전과 아이템 무료 회전은 별도 플래그를 사용한다.
- 회전 확정 시 실제 비용을 즉시 차감한다.
- 금화가 부족하면 회전을 확정할 수 없다.

금화 심벌 결과:

| 완성 줄 | 지급액 |
|---:|---:|
| 1줄 | 실제 회전비의 75% |
| 2줄 | 실제 회전비의 200% |
| 3줄 이상 | 실제 회전비의 500% |

기본 회전비 20 기준:

| 완성 줄 | 지급액 |
|---:|---:|
| 1줄 | 15 |
| 2줄 | 40 |
| 3줄 이상 | 100 |

경제 검증 목표:

```text
금화 심벌의 장기 평균 지급액
≤ 실제 회전비의 30%
```

즉 기본 기준으로 평균 지급 목표는 회전당 6금화 이하다. 정확한 토큰 구성과 확률은 룰렛 확률 모델에서 검증한다.

- 금화 결과는 회전비를 기준으로 계산하므로 비용 할인·무료 회전의 예외를 명시해야 한다.
- 무료 회전에서 금화 심벌이 완성되면 `기준 회전비 20`을 지급 기준으로 사용한다.
- 한 회전의 금화 보상은 확정 결과 처리에서 한 번만 지급한다.
- 금화 지급으로 자동 재회전하지 않는다.

---

## 11. 전술 명령 경제값

| 전술 명령 | 초기 금화 비용 | 비고 |
|---|---:|---|
| 바리케이드 | 12 | 튜토리얼 승인값 유지 |
| 화살비 | 25 | 즉시 범위 물리 피해 |
| 강화지대 | 25 | 일정 범위 아군 강화 |
| 역병 | 30 | 지속 피해·약화 |

- 전역 쿨다운은 사용하지 않는다.
- 명령별 개별 쿨다운을 유지한다.
- 일시정지 중 목표 지정과 비용 지불은 가능하지만 시전·지속·쿨다운 시간은 멈춘다.
- 정확한 피해·지속시간이 바뀌면 비용도 전술 명령 밸런스 작업에서 재검증한다.
- 전술 명령 비용은 시장 빌드의 주요 금화 소비처다.

---

## 12. 취소·철거·파괴 환불

| 상황 | 환불 |
|---|---:|
| 건설 중 사용자 취소 | 실제 지불액의 70% |
| 업그레이드 중 사용자 취소 | 실제 지불액의 50% |
| 완공 건물 사용자 철거 | 기본 건설비의 40% |
| 적에 의한 파괴 | 0% |

처리 규칙:

- 환불액은 내림 처리한다.
- 시장의 중복 비용도 실제 지불액을 기준으로 건설 취소 환불을 계산한다.
- 특수병단 Tier 2 할인 업그레이드 취소는 할인 후 실제 지불액의 50%를 환불한다.
- 특수병단 Tier 2 업그레이드를 취소하면 Tier 1로 돌아가고 준비도는 0초로 초기화한다.
- 완공 특수병단 철거 환불은 Tier 1 기본 건설비 40의 40%만 지급하며 Tier 2 비용은 반환하지 않는다.
- 파괴된 건물의 토큰·수입·생산·준비도는 해당 책임 문서의 제거 규칙을 따른다.
- 폐허 정리 비용은 첫 PoC에서는 사용하지 않는다.

---

## 13. 15분 총수입 기준

금화 룰렛 지급과 건물 지출을 제외한 총 가용 금화다.

| 시나리오 | 5분 | 10분 | 15분 |
|---|---:|---:|---:|
| 접전지 0개·시장 없음 | 235 | 310 | 385 |
| 평균 접전지 1.5개·시장 없음 | 265 | 370 | 475 |
| 접전지 3개·시장 없음 | 295 | 430 | 565 |
| 평균 접전지 1.5개·시장 1개 조기 건설 | 317 | 482 | 647 |

가정:

- 시작 금화 160 포함.
- 기본 시간 수입 포함.
- 시장 1개는 0:00에 건설을 시작해 0:25에 완공.
- 금화 룰렛 수입은 제외.
- 건설비·회전비 지출은 제외한 총 유입량이다.

첫 시장은 15분 시점에 약 172금화를 생산하고 건설비 50을 제외하면 약 122금화 순증가한다. 대신 초반 전투 건물 한 동과 후방 노드 하나를 포기한다.

---

## 14. 시작 빌드 예시

### 안정 방어

```text
기본 병영 40
+ 포탑 35
+ 농장 35
+ 룰렛 2회 40
= 150
잔여 10
```

### 병력량 집중

```text
기본 병영 2동 80
+ 농장 35
+ 룰렛 2회 40
= 155
잔여 5
```

### 시장 운영

```text
기본 병영 40
+ 시장 50
+ 농장 35
+ 룰렛 1회 20
= 145
잔여 15
```

### 사제단 즉시 전환

```text
기본 병영 40
+ 특수병단 Tier 1 40
+ 사제단 즉시 업그레이드 60
+ 룰렛 1회 20
= 160
잔여 0
```

### 거인단 즉시 전환

```text
특수병단 Tier 1 40
+ 거인단 즉시 업그레이드 100
+ 룰렛 1회 20
= 160
잔여 0
```

- 거인단 즉시 전환은 기본 병영·농장·포탑을 모두 포기하는 극단적인 고위험 시작이다.
- 거인단 최대 할인 전환은 Tier 1과 Tier 2 총 90금화지만 토큰과 생산 시작이 150초 늦다.
- 어느 시작도 모든 상황에서 항상 우월하지 않아야 한다.

---

## 15. 데이터 계약

```text
StageEconomyProfile
- starting_gold
- starting_food_cap
- base_income_amount
- base_income_interval_seconds
- control_income_amount_per_point
- control_income_interval_seconds
- roulette_base_spin_cost
- gold_result_reward_multipliers
- building_cost_profiles
- building_time_profiles
- specialization_cost_profiles
- tactical_command_costs
- refund_rates
- duplicate_market_cost_step
```

건물 비용:

```text
BuildingCostProfile
- building_family
- building_tier
- base_gold_cost
- construction_or_upgrade_seconds
- duplicate_cost_rule
- difficulty_cost_multiplier
- stage_cost_multiplier
```

실제 비용 적용 순서:

```text
1. 기본 비용
2. 난이도·스테이지 비용 배율
3. 중복 건설 비용
4. 특수병단 준비 할인
5. 올림 처리
```

환불 적용:

```text
refund_gold = floor(actual_paid_gold × refund_rate)
```

---

## 16. 검증 계약

1. 정규 Normal 시작 금화는 160이다.
2. 기본 수입은 활성 전투 시간 20초마다 5금화다.
3. 중앙 접전지는 60초마다 아군 점령 한 곳당 4금화를 지급한다.
4. 적 처치와 웨이브 클리어는 기본 금화를 지급하지 않는다.
5. 기본 룰렛 회전비는 20금화다.
6. 시작 금화만으로 안정 방어·시장·사제단 즉시 전환 중 하나를 선택할 수 있다.
7. 거인단 즉시 전환은 가능하지만 기본 방어 투자를 거의 포기한다.
8. 시장 첫 동의 비용 회수시간은 완공 후 약 4분 10초다.
9. 추가 시장은 건설 순서마다 25금화씩 비싸진다.
10. 특수병단 준비 할인은 150초·50%가 최대다.
11. 자동생산과 시간 수입은 일시정지 중 멈춘다.
12. 식량 부족은 기존 유닛을 제거하지 않고 신규 인도만 막는다.
13. 금화 룰렛의 장기 평균 지급 목표는 실제 회전비의 30% 이하다.
14. 건설 취소·업그레이드 취소·철거·파괴의 환불률이 서로 다르다.
15. 적 파괴에는 환불이 없다.
16. 15분 평균 통제 시나리오에서 총 유입 475금화 전후를 첫 기준으로 사용한다.
17. 시장 1개 조기 건설은 15분에 약 122금화의 순증가를 만들지만 노드와 초기 전력을 소비한다.
18. 수치 변경 시 안정 방어·병력량·시장·특수병단 네 빌드를 함께 재계산한다.

---

## 17. 후속 조정 대상

- 기본 병영 자동생산 간격의 60초 공세 시계 재조정.
- 시장 Tier 2·3 전문화와 추가 효과.
- 농장 Tier 3 전문화.
- 포탑 Tier 2·3 전투 효과와 비용.
- 기본 병영 Tier 3 상위 병종·교리 비용.
- 룰렛 실제 확률과 금화 심벌 기대값.
- 용병·아이템·장비 가격.
- 난이도별 시작 금화·수입·비용 배율.
- 전술 명령 정확한 효과 대비 비용.
- 접전지 통제 수입이 우세 스노우볼을 과도하게 만드는지 검증.

이 문서는 경제 데이터와 밸런스 시작값을 승인하지만 Godot 코드·Resource·Scene·테스트 구현 승인을 뜻하지 않는다. 구현은 별도 Codex Plan Mode 제안서와 사용자 승인을 거친다.

```

## `docs/design/APPROVED_UNIT_GRADE_AND_ABILITY_GROWTH.md`

Category: `ACTIVE` / 240 lines

```text
# 승인된 유닛 등급·핵심 패시브·일반 스킬 성장 규칙

- 상태: **핵심 구조 승인됨 / 병종별 세부 능력과 수치 조정 대기**
- 승인일: 2026-07-14
- 연결 문서:
  - `docs/design/APPROVED_ROULETTE_CORE_RULES.md`
  - `docs/design/APPROVED_BARRACKS_TIER3_EVOLUTION_AND_GRADE_SKILLS.md`
  - `docs/design/APPROVED_COMBAT_KEYWORDS_STATUS_EFFECTS_AND_FLIGHT.md`

이 문서는 룰렛 등급과 능력 성장 구조를 정의한다. 병영 Tier별 병종 진화·공유 토큰·패시브 강화는 `APPROVED_BARRACKS_TIER3_EVOLUTION_AND_GRADE_SKILLS.md`가 우선한다.

## 1. 등급은 룰렛로만 결정한다

| 동일 심벌 완성 줄 | 생성 등급 |
|---:|---|
| 1줄 | 일반 |
| 2줄 | 엘리트 |
| 3~7줄 | 영웅 |
| 8줄·9칸 전체 동일 | 전설 |

- `신화` 명칭은 사용하지 않고 `전설` 명칭을 유지한다.
- 수동 합성, 처치 경험치와 건물 Tier로 등급이 상승하지 않는다.
- 병영 자동 생산은 항상 일반 등급이다.
- 상점의 상위 등급 용병 직접 판매는 현재 승인 범위에서 제외한다.
- 전설은 한 스테이지 전체에서 병종과 관계없이 1회만 생성한다.
- 전설 생성 뒤 다시 9칸 동일 결과가 나오면 해당 계열 영웅 2명으로 변환한다.

## 2. 병영 Tier와 룰렛 등급은 독립 축이다

병영 Tier가 결정하는 것:

- 일반 등급의 실제 기본·상위 세부 병종
- 핵심 패시브의 개수
- 기존 핵심 패시브의 강화 단계
- 자동 생산 병종

룰렛 등급이 결정하는 것:

- 일반·엘리트·영웅·전설 고정 등급
- 일반 스킬의 강화·생성 단계
- 고정 상위 등급 유닛 템플릿

병영 Tier가 높다고 엘리트·영웅·전설 확률이 증가하지 않는다.

## 3. 병영 Tier별 핵심 패시브 성장

| 훈련 출처 | 핵심 패시브 구성 |
|---|---|
| Tier 1 | 패시브 1 기본형 |
| Tier 2 | 패시브 1 강화 + 패시브 2 생성 |
| Tier 3 | 패시브 1 추가 강화 + 패시브 2 강화 + 패시브 3 생성 |

이 규칙은 일반·엘리트·영웅·전설 모두에 적용한다.

핵심 계약:

- Tier가 오르면 신규 패시브만 추가되는 것이 아니라 기존 패시브도 강화된다.
- Tier 2는 첫 번째 패시브의 1차 강화와 두 번째 패시브 해금을 동시에 제공한다.
- Tier 3는 첫 번째 패시브의 2차 강화, 두 번째 패시브의 1차 강화와 세 번째 패시브 해금을 동시에 제공한다.
- 병영이 파괴돼도 이미 생성된 유닛의 패시브와 강화 단계는 유지한다.

예시:

```text
Tier 1 전사 출처
- 패시브 1: 전투 숙련

Tier 2 방패병 출처
- 패시브 1 강화
- 패시브 2: 방패 방어 생성

Tier 3 전사 계열 출처
- 패시브 1 추가 강화
- 패시브 2 강화
- 패시브 3 생성
```

상위 등급 고정 유닛도 선택된 훈련 출처 Tier의 패시브 성장 단계를 적용한다.

## 4. 등급별 일반 스킬 성장

핵심 패시브와 별도로 일반 스킬은 룰렛 등급에 따라 성장한다.

### 일반

- 1스킬 기본형

### 엘리트

- 1스킬 강화
- 계열별 고정 엘리트 유닛 템플릿
- 고정 능력치·외형·AI 프로필 적용

### 영웅

- 엘리트 단계의 1스킬 강화 유지
- 2스킬 생성

### 전설

- 영웅 단계의 모든 효과 유지
- 2스킬 강화
- 3스킬 생성

```text
일반: 1스킬
엘리트: 강화된 1스킬
영웅: 강화된 1스킬 + 신규 2스킬
전설: 강화된 1스킬 + 강화된 2스킬 + 신규 3스킬
```

전설에서 1스킬을 다시 강화하는 것은 기본 계약이 아니다. 필요할 경우 병종 고유 전설 패시브나 능력치로 별도 보정한다.

## 5. 고정 상위 등급 유닛

엘리트·영웅·전설은 기본 병종 계열별 고정 템플릿이다.

- 전사 계열의 엘리트·영웅·전설은 전사 계열 고정 유닛
- 기병 계열의 엘리트·영웅·전설은 기병 계열 고정 유닛
- 궁병 계열의 엘리트·영웅·전설은 궁병 계열 고정 유닛
- 창병 계열의 엘리트·영웅·전설은 창병 계열 고정 유닛

Tier 3 세부 병종 선택은 상위 등급 고정 유닛의 정체성·외형·기본 스킬 세트를 바꾸지 않는다.

다만 선택된 훈련 출처 Tier는 상위 등급 유닛의 패시브 해금과 강화 단계를 결정한다.

## 6. 일반 등급 세부 병종

일반 등급은 병영 출처 후보 풀에서 실제 병종을 확률로 선택한다.

예시:

- Tier 1 전사 출처 → 일반 검사
- Tier 2 전사 출처 → 일반 방패병·대검병·광전사 후보
- Tier 2 기병 출처 → 일반 기병
- Tier 3 중기병 출처 → 일반 중기병
- Tier 3 충격기병 출처 → 일반 충격기병
- Tier 3 대공궁병 출처 → 일반 대공궁병

높은 Tier 일반 병종 후보는 낮은 Tier 후보보다 높은 가중치를 가진다.

## 7. 초기 병종 능력 예시

### 방패병

- 패시브 후보: 원거리 공격 피해 감소
- 1스킬 후보: 방패 밀치기

### 창병

- 패시브 후보: `[기병]` 추가 피해와 일반 `[돌진]` 저지
- 1스킬: 쓰러스트

### 기병

- 패시브 후보: 이동력 증가
- 1스킬: 돌진

### 궁병

- 패시브 후보: 원거리 사격
- 1스킬: 성공한 기본 공격 3회 뒤 다음 공격 확정 치명타

### 암살자

- 패시브 후보: 후방 공격 시 치명타 확률 증가
- 1스킬 후보: 그림자 이동

정확한 병종별 패시브 1·2·3의 기본형·강화형과 스킬 1·2·3은 별도 능력표에서 확정한다.

## 8. 데이터 계약

```text
unit_type_id
base_unit_family
normal_unit_variant
grade
training_source_tier
passive_unlock_ids
passive_upgrade_ids
skill_1_id
skill_1_upgrade_id
skill_2_id
skill_2_upgrade_id
skill_3_id
fixed_grade_template_id
source_building_id
spawned_unit_modifier_ids
```

- `grade`와 `training_source_tier`를 분리한다.
- 패시브 해금과 패시브 강화는 서로 다른 ID로 기록한다.
- 신규 스킬과 기존 스킬 강화는 서로 다른 ID로 기록한다.
- 생산시설 운영 교리 버프는 `spawned_unit_modifier_ids`로 분리한다.

## 9. UI 계약

룰렛 결과 화면:

- 기본 병종 계열
- 실제 생성 유닛
- 생성 등급
- 선택된 훈련 출처 Tier
- 새로 생성된 핵심 패시브
- 강화된 핵심 패시브
- 새로 생성되거나 강화된 일반 스킬

유닛 정보창:

1. 기본 병종 계열·실제 세부 병종·등급
2. 훈련 출처 병영과 Tier
3. 병종 태그·상성·이동 레이어
4. 핵심 패시브 1·2·3과 강화 단계
5. 일반 스킬 1·2·3과 강화 상태
6. 내부 쿨타임·발동 조건·대상 레이어

## 10. 검증 계약

- 1/2/3~7/8줄은 일반/엘리트/영웅/전설로 매핑된다.
- 병영 Tier가 룰렛 등급 결과를 바꾸지 않는다.
- Tier 1은 패시브 1 기본형을 적용한다.
- Tier 2는 패시브 1 강화와 패시브 2 생성을 적용한다.
- Tier 3는 패시브 1 추가 강화, 패시브 2 강화와 패시브 3 생성을 적용한다.
- 엘리트는 1스킬을 강화한다.
- 영웅은 강화된 1스킬을 유지하고 2스킬을 생성한다.
- 전설은 영웅 효과를 유지하고 2스킬을 강화하며 3스킬을 생성한다.
- 엘리트·영웅·전설 유닛의 정체성은 Tier 3 세부 병종 선택과 무관하게 고정된다.
- 자동 생산은 항상 일반 등급이다.
- 생성된 유닛은 출처 병영 파괴 뒤에도 병종·등급·패시브·스킬을 유지한다.

## 11. 미확정 세부

- 전사 계열 Tier 2 병종 최종 목록
- 계열별 엘리트·영웅·전설 고정 유닛
- 병종별 패시브 1·2·3과 Tier별 강화 내용
- 병종별 스킬 1·2·3과 등급별 강화 내용
- Tier별 병종 후보 가중치
- 엘리트 고정 능력치 배율

이 문서는 핵심 구조를 승인하지만 개별 수치를 구현 승인으로 간주하지 않는다. Godot 구현은 별도 Codex Plan Mode 제안서와 사용자 승인을 거쳐야 한다.

```

## `scenes/ui/stage_hud.tscn`

Category: `ACTIVE` / 121 lines

```text
[gd_scene load_steps=2 format=3]

[ext_resource type="Script" path="res://scripts/ui/stage_hud.gd" id="1_view"]

[node name="StageHud" type="Control"]
layout_mode = 3
anchors_preset = 15
anchor_right = 1.0
anchor_bottom = 1.0
grow_horizontal = 2
grow_vertical = 2
mouse_filter = 2
script = ExtResource("1_view")

[node name="ResourceLabel" type="Label" parent="."]
layout_mode = 0
offset_left = 20.0
offset_top = 16.0
offset_right = 250.0
offset_bottom = 38.0
theme_override_colors/font_color = Color(0.9, 0.93, 0.97, 1)
theme_override_font_sizes/font_size = 16

[node name="WaveLabel" type="Label" parent="."]
layout_mode = 0
offset_left = 20.0
offset_top = 40.0
offset_right = 150.0
offset_bottom = 62.0
theme_override_colors/font_color = Color(0.76, 0.84, 0.94, 1)

[node name="OmenLabel" type="Label" parent="."]
layout_mode = 0
offset_left = 160.0
offset_top = 40.0
offset_right = 320.0
offset_bottom = 62.0
theme_override_colors/font_color = Color(0.94, 0.8, 0.42, 1)

[node name="SpinButton" type="Button" parent="."]
layout_mode = 0
offset_left = 20.0
offset_top = 450.0
offset_right = 132.0
offset_bottom = 486.0
text = "Spin (20)"

[node name="TowerButton" type="Button" parent="."]
layout_mode = 0
offset_left = 144.0
offset_top = 450.0
offset_right = 232.0
offset_bottom = 486.0
text = "Tower"

[node name="FarmButton" type="Button" parent="."]
layout_mode = 0
offset_left = 242.0
offset_top = 450.0
offset_right = 330.0
offset_bottom = 486.0
text = "Farm"

[node name="CardsLabel" type="Label" parent="."]
layout_mode = 0
offset_left = 344.0
offset_top = 450.0
offset_right = 700.0
offset_bottom = 486.0
theme_override_colors/font_color = Color(0.84, 0.89, 0.94, 1)
autowrap_mode = 2

[node name="DeployTop" type="Button" parent="."]
layout_mode = 0
offset_left = 710.0
offset_top = 438.0
offset_right = 786.0
offset_bottom = 468.0
text = "Top"

[node name="DeployMiddle" type="Button" parent="."]
layout_mode = 0
offset_left = 794.0
offset_top = 438.0
offset_right = 870.0
offset_bottom = 468.0
text = "Middle"

[node name="DeployBottom" type="Button" parent="."]
layout_mode = 0
offset_left = 878.0
offset_top = 438.0
offset_right = 952.0
offset_bottom = 468.0
text = "Bottom"

[node name="ResultLabel" type="Label" parent="."]
layout_mode = 0
offset_left = 340.0
offset_top = 210.0
offset_right = 620.0
offset_bottom = 250.0
theme_override_colors/font_color = Color(1, 0.9, 0.45, 1)
theme_override_font_sizes/font_size = 24
horizontal_alignment = 1

[node name="RetryButton" type="Button" parent="."]
layout_mode = 0
offset_left = 414.0
offset_top = 258.0
offset_right = 546.0
offset_bottom = 294.0
text = "Retry Stage"

[connection signal="pressed" from="SpinButton" to="." method="_on_spin_pressed"]
[connection signal="pressed" from="TowerButton" to="." method="_on_tower_pressed"]
[connection signal="pressed" from="FarmButton" to="." method="_on_farm_pressed"]
[connection signal="pressed" from="DeployTop" to="." method="_on_deploy_pressed" binds= [&"top"]]
[connection signal="pressed" from="DeployMiddle" to="." method="_on_deploy_pressed" binds= [&"middle"]]
[connection signal="pressed" from="DeployBottom" to="." method="_on_deploy_pressed" binds= [&"bottom"]]
[connection signal="pressed" from="RetryButton" to="." method="_on_retry_pressed"]

```

## `scripts/battle/battle_simulator.gd`

Category: `ACTIVE` / 139 lines

```text
class_name BattleSimulator
extends RefCounted

const UnitInstanceScript = preload("res://scripts/battle/unit_instance.gd")
const LaneStateScript = preload("res://scripts/battle/lane_state.gd")
const GateStateScript = preload("res://scripts/battle/gate_state.gd")
const ClashZoneStateScript = preload("res://scripts/battle/clash_zone_state.gd")
const AssassinBypassStateScript = preload("res://scripts/battle/assassin_bypass_state.gd")

const FIXED_STEP_SECONDS := 0.1
const LANE_IDS := [&"top", &"middle", &"bottom"]

var registry: DataRegistry
var seed := 0
var lanes := {}
var gates := {}
var clash_zones := {}
var bypasses: Array = []

var _rng := RandomNumberGenerator.new()
var _accumulator := 0.0
var _tick := 0
var _next_unit_id := 1


func _init(assigned_registry: DataRegistry, seed_value: int = 0) -> void:
	registry = assigned_registry
	seed = seed_value
	_rng.seed = seed
	for lane_id in LANE_IDS:
		lanes[lane_id] = LaneStateScript.new(lane_id)
		clash_zones[lane_id] = ClashZoneStateScript.new(lane_id)
	gates = {
		"lumern": {"top": GateStateScript.new(), "middle": GateStateScript.new(), "bottom": GateStateScript.new()},
		"veil": {"top": GateStateScript.new(), "middle": GateStateScript.new(), "bottom": GateStateScript.new()},
	}


func spawn_unit(spawn: UnitSpawnDefinition) -> Variant:
	if spawn == null or not registry.archetypes.has(str(spawn.archetype_id)) or not lanes.has(spawn.lane_id):
		return null
	var unit: Variant = UnitInstanceScript.new(spawn, registry, _next_unit_id, _rng.randi_range(0, 9999))
	_next_unit_id += 1
	if not lanes[spawn.lane_id].add_unit(unit):
		return null
	return unit


func request_lane_move(unit: Variant, requested_lane_id: StringName) -> bool:
	return unit != null and unit.lane_id == requested_lane_id


func request_assassin_bypass(unit: Variant, enemy_outpost_position: float) -> bool:
	if unit == null or unit.archetype_id != &"assassin" or not lanes.has(unit.lane_id):
		return false
	var lane: Variant = lanes[unit.lane_id]
	if not lane.remove_unit(unit):
		return false
	bypasses.append({
		"unit": unit,
		"state": AssassinBypassStateScript.new(unit.lane_id, enemy_outpost_position),
	})
	return true


func advance(delta: float) -> void:
	_accumulator += maxf(0.0, delta)
	while _accumulator + 0.000001 >= FIXED_STEP_SECONDS:
		_accumulator -= FIXED_STEP_SECONDS
		_advance_fixed_step()


func snapshot() -> Dictionary:
	var lane_snapshots: Array = []
	var unit_snapshots: Array = []
	var zone_snapshots: Array = []
	var gate_snapshots := {}
	for lane_id in LANE_IDS:
		var lane: Variant = lanes[lane_id]
		lane_snapshots.append(lane.snapshot())
		for unit in lane.ordered_units():
			unit_snapshots.append(unit.to_snapshot())
		zone_snapshots.append(clash_zones[lane_id].snapshot())
	for team_id in [&"lumern", &"veil"]:
		var team_gates := {}
		for lane_id in LANE_IDS:
			team_gates[str(lane_id)] = gates[str(team_id)][str(lane_id)].snapshot()
		gate_snapshots[str(team_id)] = team_gates
	return {
		"seed": seed,
		"tick": _tick,
		"accumulator": _accumulator,
		"lanes": lane_snapshots,
		"units": unit_snapshots,
		"gates": gate_snapshots,
		"clash_zones": zone_snapshots,
		"bypasses": bypasses.map(func(entry: Dictionary) -> Dictionary: return entry["state"].snapshot()),
	}


func _advance_fixed_step() -> void:
	_tick += 1
	_advance_bypasses(FIXED_STEP_SECONDS)
	for lane_id in LANE_IDS:
		var lane: Variant = lanes[lane_id]
		for unit in lane.ordered_units():
			if not unit.is_alive():
				continue
			var target: Variant = lane.find_target(unit)
			unit.target_unit_id = target.unit_id if target != null else -1
			if target == null:
				unit.state = "idle"
				continue
			if unit.distance_to(target) > float(unit.combat_stats()["attack_range"]):
				unit.move_toward(target, FIXED_STEP_SECONDS)
				continue
			var damage: float = unit.advance_attack(FIXED_STEP_SECONDS)
			if damage > 0.0:
				target.receive_damage(damage)
		lane.remove_dead_units()
		clash_zones[lane_id].advance(FIXED_STEP_SECONDS)
	for team_id in [&"lumern", &"veil"]:
		for lane_id in LANE_IDS:
			gates[str(team_id)][str(lane_id)].advance(FIXED_STEP_SECONDS)


func _advance_bypasses(delta: float) -> void:
	var active_bypasses: Array = []
	for entry: Dictionary in bypasses:
		var bypass: Variant = entry["state"]
		bypass.advance(delta)
		if not bypass.is_complete():
			active_bypasses.append(entry)
			continue
		var unit: Variant = entry["unit"]
		unit.lane_position = bypass.exit_position
		unit.state = "bypass_exit"
		lanes[unit.lane_id].add_unit(unit)
	bypasses = active_bypasses

```

## `scripts/battle/unit_instance.gd`

Category: `ACTIVE` / 139 lines

```text
class_name UnitInstance
extends RefCounted

var unit_id := 0
var archetype_id: StringName
var tier_id: StringName
var rank_id: StringName
var owner_team_id: StringName
var visual_faction_id: StringName
var lane_id: StringName
var lane_position := 0.0
var target_unit_id := -1
var state := "idle"
var health := 0.0
var cooldown_remaining := 0.0
var deterministic_animation_offset := 0

var _stats := {}
var _preparation_seconds := 0.1
var _hit_seconds := 0.1
var _recovery_seconds := 0.1


func _init(spawn: UnitSpawnDefinition, registry: DataRegistry, assigned_unit_id: int, animation_offset: int) -> void:
	unit_id = assigned_unit_id
	archetype_id = spawn.archetype_id
	tier_id = spawn.tier_id
	rank_id = spawn.rank_id
	owner_team_id = spawn.owner_team_id
	visual_faction_id = spawn.visual_faction_id
	lane_id = spawn.lane_id
	lane_position = 0.0 if owner_team_id == &"lumern" else 100.0
	deterministic_animation_offset = animation_offset
	_stats = _build_combat_stats(registry)
	health = float(_stats["max_health"])
	_load_attack_timing(registry)


func combat_stats() -> Dictionary:
	return _stats.duplicate()


func is_alive() -> bool:
	return health > 0.0


func distance_to(other: UnitInstance) -> float:
	return absf(lane_position - other.lane_position)


func move_toward(other: UnitInstance, delta: float) -> void:
	state = "move"
	var direction := signf(other.lane_position - lane_position)
	lane_position += direction * float(_stats["move_speed"]) * delta


func advance_attack(delta: float) -> float:
	if state == "idle" or state == "move":
		state = "attack_preparation"
		cooldown_remaining = _preparation_seconds
		return 0.0
	if state == "attack_preparation":
		cooldown_remaining -= delta
		if cooldown_remaining <= 0.0:
			state = "attack_hit"
			cooldown_remaining = _hit_seconds
		return 0.0
	if state == "attack_hit":
		state = "attack_recovery"
		cooldown_remaining = _recovery_seconds
		return float(_stats["attack"])
	if state == "attack_recovery":
		cooldown_remaining -= delta
		if cooldown_remaining <= 0.0:
			state = "idle"
		return 0.0
	return 0.0


func receive_damage(raw_damage: float) -> float:
	var mitigated := raw_damage * 100.0 / (100.0 + float(_stats["armor"]))
	health = maxf(0.0, health - mitigated)
	if health <= 0.0:
		state = "dead"
		target_unit_id = -1
	return mitigated


func to_snapshot() -> Dictionary:
	return {
		"unit_id": unit_id,
		"archetype_id": str(archetype_id),
		"tier_id": str(tier_id),
		"rank_id": str(rank_id),
		"owner_team_id": str(owner_team_id),
		"visual_faction_id": str(visual_faction_id),
		"lane_id": str(lane_id),
		"lane_position": lane_position,
		"target_unit_id": target_unit_id,
		"state": state,
		"health": health,
		"cooldown_remaining": cooldown_remaining,
		"deterministic_animation_offset": deterministic_animation_offset,
	}


func _build_combat_stats(registry: DataRegistry) -> Dictionary:
	var profile: Variant = registry.archetypes.get(str(archetype_id))
	if profile == null or profile.base_stats.is_empty():
		push_error("unknown shared archetype: %s" % archetype_id)
		return {}
	var multiplier := _tier_multiplier(registry) * _rank_multiplier(registry)
	var result := {}
	for key in profile.base_stats:
		result[key] = float(profile.base_stats[key]) * multiplier
	return result


func _tier_multiplier(registry: DataRegistry) -> float:
	for profile in registry.catalog.tier_profiles:
		if profile.tier_id == tier_id:
			return profile.stat_multiplier
	return 1.0


func _rank_multiplier(registry: DataRegistry) -> float:
	for profile in registry.catalog.rank_profiles:
		if profile.rank_id == rank_id:
			return profile.stat_multiplier
	return 1.0


func _load_attack_timing(registry: DataRegistry) -> void:
	for profile in registry.catalog.attack_profiles:
		if profile.profile_id == archetype_id:
			_preparation_seconds = float(profile.preparation_ms) / 1000.0
			_hit_seconds = float(profile.hit_ms) / 1000.0
			_recovery_seconds = float(profile.recovery_ms) / 1000.0
			return

```

## `scripts/buildings/building_service.gd`

Category: `ACTIVE` / 97 lines

```text
class_name BuildingService
extends RefCounted

const PLAYER_TEAM_ID := &"lumern"
const BuildingDefinitionScript = preload("res://scripts/data/building_definition.gd")
const BuildingStateScript = preload("res://scripts/buildings/building_state.gd")

var economy: Variant
var manifest: Variant
var definitions := {}
var _outposts := {}
var _nodes := {}
var _buildings := {}


func _init(assigned_economy: Variant, assigned_manifest: Variant) -> void:
	economy = assigned_economy
	manifest = assigned_manifest
	definitions = {
		&"tower": _definition(&"tower", 35, 0, &"shield_guard"),
		&"farm": _definition(&"farm", 35, 6, &"archer"),
	}


func register_outpost(outpost_id: StringName, outpost: Variant, node_ids: Array) -> void:
	_outposts[outpost_id] = outpost
	_nodes[outpost_id] = node_ids.duplicate()


func try_construct(outpost_id: StringName, node_id: StringName, building_id: StringName) -> bool:
	if not definitions.has(building_id) or not _node_is_available(outpost_id, node_id):
		return false
	var definition: Variant = definitions[building_id]
	if not economy.try_spend_gold(definition.gold_cost):
		return false
	var outpost: Variant = _outposts[outpost_id]
	var state: Variant = BuildingStateScript.new(outpost_id, node_id, definition, outpost.capture_revision)
	_buildings[_key(outpost_id, node_id)] = state
	if definition.food_cap_bonus > 0:
		economy.add_food_cap(definition.food_cap_bonus)
	manifest.input_log.append({
		"action": "build",
		"outpost_id": str(outpost_id),
		"node_id": str(node_id),
		"building_id": str(building_id),
	})
	return true


func roulette_archetype_ids() -> Array[StringName]:
	var tokens: Array[StringName] = []
	for key in _buildings:
		var state: Variant = _buildings[key]
		if _outpost_is_active_for_player(state.outpost_id) and _building_matches_current_capture(state):
			tokens.append(state.definition.roulette_archetype_id)
	if tokens.is_empty():
		tokens.append(&"shield_guard")
	return tokens


func _node_is_available(outpost_id: StringName, node_id: StringName) -> bool:
	if not _nodes.has(outpost_id) or not (_nodes[outpost_id] as Array).has(node_id):
		return false
	var key := _key(outpost_id, node_id)
	if _buildings.has(key):
		var state: Variant = _buildings[key]
		if _building_matches_current_capture(state):
			return false
		_buildings.erase(key)
	return _outpost_is_active_for_player(outpost_id)


func _outpost_is_active_for_player(outpost_id: StringName) -> bool:
	if not _outposts.has(outpost_id):
		return false
	var outpost: Variant = _outposts[outpost_id]
	return outpost.owner_team_id == PLAYER_TEAM_ID and outpost.state == outpost.STABLE and not outpost.construction_locked


func _building_matches_current_capture(state: Variant) -> bool:
	if not _outposts.has(state.outpost_id):
		return false
	var outpost: Variant = _outposts[state.outpost_id]
	return state.capture_revision == outpost.capture_revision


func _definition(building_id: StringName, gold_cost: int, food_cap_bonus: int, token_id: StringName) -> Variant:
	var definition: Variant = BuildingDefinitionScript.new()
	definition.building_id = building_id
	definition.gold_cost = gold_cost
	definition.food_cap_bonus = food_cap_bonus
	definition.roulette_archetype_id = token_id
	return definition


func _key(outpost_id: StringName, node_id: StringName) -> String:
	return "%s:%s" % [outpost_id, node_id]

```

## `scripts/core/determinism_service.gd`

Category: `ACTIVE` / 24 lines

```text
class_name DeterminismService
extends RefCounted

var seed: int
var _rng := RandomNumberGenerator.new()

func _init(seed_value: int) -> void:
	seed = seed_value
	_rng.seed = seed

func create_stage_manifest(stage_id: String, archetype_ids: Array[String]) -> StageManifest:
	var manifest := StageManifest.new()
	manifest.stage_id = stage_id
	manifest.seed = seed
	manifest.archetype_ids = archetype_ids.duplicate()
	manifest.archetype_ids.sort()
	manifest.random_roll = _rng.randi()
	return manifest


func create_roulette_rng(spin_seed: int) -> RandomNumberGenerator:
	var roulette_rng := RandomNumberGenerator.new()
	roulette_rng.seed = seed ^ spin_seed
	return roulette_rng

```

## `scripts/core/stage_run.gd`

Category: `ACTIVE` / 120 lines

```text
class_name StageRun
extends RefCounted

const DataRegistryScript = preload("res://scripts/core/data_registry.gd")
const CombatClockScript = preload("res://scripts/core/combat_clock.gd")
const StageEconomyScript = preload("res://scripts/core/stage_economy.gd")
const BuildingServiceScript = preload("res://scripts/buildings/building_service.gd")
const RouletteServiceScript = preload("res://scripts/roulette/roulette_service.gd")
const DeploymentServiceScript = preload("res://scripts/units/deployment_service.gd")
const WaveDirectorScript = preload("res://scripts/waves/wave_director.gd")
const BattleSimulatorScript = preload("res://scripts/battle/battle_simulator.gd")
const StageProgressionScript = preload("res://scripts/core/stage_progression.gd")
const OutpostStateScript = preload("res://scripts/battle/outpost_state.gd")

const RUNNING := &"running"
const VICTORY := &"victory"
const DEFEAT := &"defeat"

var progression: Variant
var stage: Variant
var manifest: Variant
var clock: Variant
var economy: Variant
var buildings: Variant
var roulette: Variant
var deployment: Variant
var wave_director: Variant
var battle: Variant
var current_wave := 0
var result_state: StringName = &""

var _registry: Variant
var _home_outpost: Variant


func _init(assigned_progression: Variant = null) -> void:
	progression = assigned_progression if assigned_progression != null else StageProgressionScript.new()


func start(assigned_stage: Variant, seed: int) -> void:
	stage = assigned_stage
	current_wave = 0
	result_state = &""
	if stage == null or not progression.can_start(stage):
		return
	_registry = DataRegistryScript.new()
	var errors: PackedStringArray = _registry.load_bootstrap_catalog("res://data/bootstrap_catalog.tres")
	if not errors.is_empty():
		result_state = DEFEAT
		return
	manifest = stage.build_manifest(seed)
	clock = CombatClockScript.new()
	clock.is_planning = false
	economy = StageEconomyScript.new(manifest)
	buildings = BuildingServiceScript.new(economy, manifest)
	_home_outpost = OutpostStateScript.new(&"lumern")
	buildings.register_outpost(&"home", _home_outpost, [&"front_a", &"front_b"])
	roulette = RouletteServiceScript.new(economy, buildings, manifest, &"lumern")
	deployment = DeploymentServiceScript.new(economy, manifest)
	wave_director = WaveDirectorScript.new(stage)
	battle = BattleSimulatorScript.new(_registry, seed)
	result_state = RUNNING


func spin_roulette(seed_input: Dictionary) -> Array:
	return roulette.spin(seed_input) if roulette != null else []


func construct_home(building_id: StringName) -> bool:
	if buildings == null:
		return false
	var node_id := &"front_a" if building_id == &"tower" else &"front_b"
	return buildings.try_construct(&"home", node_id, building_id)


func deploy_card(card: UnitSpawnDefinition, lane_id: StringName) -> bool:
	if deployment == null or battle == null or not deployment.deploy(card, lane_id, 10.0):
		return false
	var deployed := card.duplicate() as UnitSpawnDefinition
	deployed.lane_id = lane_id
	return battle.spawn_unit(deployed) != null


func submit_command(command: Dictionary) -> bool:
	if result_state != RUNNING:
		return false
	match command.get("action", ""):
		"stage_victory":
			result_state = VICTORY
			progression.record_victory(stage)
		"stage_defeat":
			result_state = DEFEAT
		_:
			return false
	manifest.input_log.append(command.duplicate(true))
	return true


func advance(delta: float) -> void:
	if result_state != RUNNING:
		return
	clock.advance(delta)
	economy.advance(delta, 0, _stable_owned_outpost_count())
	for wave in wave_director.advance(delta):
		current_wave = wave.wave_number
		for spawn in wave.spawns:
			battle.spawn_unit(spawn.duplicate() as UnitSpawnDefinition)
		manifest.input_log.append({"action": "wave", "wave_number": current_wave})
	battle.advance(delta)


func _stable_owned_outpost_count() -> int:
	if battle == null:
		return 0
	var count := 0
	for lane_id in battle.LANE_IDS:
		var outpost: Variant = battle.clash_zones[lane_id].outpost
		if outpost.owner_team_id == &"lumern" and outpost.state == outpost.STABLE:
			count += 1
	return count

```

## `scripts/data/building_definition.gd`

Category: `ACTIVE` / 7 lines

```text
class_name BuildingDefinition
extends Resource

@export var building_id: StringName
@export var gold_cost: int
@export var food_cap_bonus: int
@export var roulette_archetype_id: StringName

```

## `scripts/data/unit_spawn_definition.gd`

Category: `ACTIVE` / 24 lines

```text
class_name UnitSpawnDefinition
extends Resource

@export var archetype_id: StringName
@export var tier_id: StringName = &"tier_1"
@export var rank_id: StringName = &"common"
@export var owner_team_id: StringName
@export var visual_faction_id: StringName
@export var lane_id: StringName
@export var spawn_delay_seconds: float = 0.0
@export var food_cost: int = 1


func to_dictionary() -> Dictionary:
	return {
		"archetype_id": str(archetype_id),
		"tier_id": str(tier_id),
		"rank_id": str(rank_id),
		"owner_team_id": str(owner_team_id),
		"visual_faction_id": str(visual_faction_id),
		"lane_id": str(lane_id),
		"spawn_delay_seconds": spawn_delay_seconds,
		"food_cost": food_cost,
	}

```

## `scripts/data/wave_definition.gd`

Category: `ACTIVE` / 20 lines

```text
class_name WaveDefinition
extends Resource

const UnitSpawnDefinition = preload("res://scripts/data/unit_spawn_definition.gd")

@export var wave_number: int
@export var omen_lead_seconds: float = 5.0
@export var spawns: Array[UnitSpawnDefinition] = []
@export var boss_kind: StringName
@export var is_overtime := false


func to_dictionary() -> Dictionary:
	return {
		"wave_number": wave_number,
		"omen_lead_seconds": omen_lead_seconds,
		"spawns": spawns.map(func(spawn): return spawn.to_dictionary()),
		"boss_kind": str(boss_kind),
		"is_overtime": is_overtime,
	}

```

## `scripts/roulette/roulette_service.gd`

Category: `ACTIVE` / 40 lines

```text
class_name RouletteService
extends RefCounted

const SPIN_COST := 20
const BOARD_SIZE := 9
const UnitSpawnDefinitionScript = preload("res://scripts/data/unit_spawn_definition.gd")
const DeterminismServiceScript = preload("res://scripts/core/determinism_service.gd")

var economy: Variant
var buildings: Variant
var manifest: Variant
var player_team_id: StringName


func _init(assigned_economy: Variant, assigned_buildings: Variant, assigned_manifest: Variant, assigned_player_team_id: StringName) -> void:
	economy = assigned_economy
	buildings = assigned_buildings
	manifest = assigned_manifest
	player_team_id = assigned_player_team_id


func spin(seed_input: Dictionary) -> Array[UnitSpawnDefinition]:
	if not economy.try_spend_gold(SPIN_COST):
		return []
	var spin_seed := int(seed_input.get("seed", manifest.seed))
	var rng: RandomNumberGenerator = DeterminismServiceScript.new(manifest.seed).create_roulette_rng(spin_seed)
	var token_ids: Array[StringName] = buildings.roulette_archetype_ids()
	var cards: Array = []
	for index in BOARD_SIZE:
		var card: Variant = UnitSpawnDefinitionScript.new()
		card.archetype_id = token_ids[rng.randi_range(0, token_ids.size() - 1)]
		card.owner_team_id = player_team_id
		card.visual_faction_id = player_team_id
		cards.append(card)
	manifest.input_log.append({
		"action": "roulette",
		"seed": rng.seed,
		"cards": cards.map(func(card): return card.to_dictionary()),
	})
	return cards

```

## `scripts/ui/stage_hud.gd`

Category: `ACTIVE` / 71 lines

```text
class_name StageHud
extends Control

@onready var _resource_label: Label = $ResourceLabel
@onready var _wave_label: Label = $WaveLabel
@onready var _omen_label: Label = $OmenLabel
@onready var _cards_label: Label = $CardsLabel
@onready var _result_label: Label = $ResultLabel
@onready var _retry_button: Button = $RetryButton

var run: Variant
var _pending_cards: Array = []
var _spin_index := 0


func bind_run(assigned_run: Variant) -> void:
	run = assigned_run
	_pending_cards.clear()
	_update_display()


func _process(_delta: float) -> void:
	_update_display()


func _on_spin_pressed() -> void:
	if run == null:
		return
	_spin_index += 1
	_pending_cards = run.spin_roulette({"seed": _spin_index})
	_update_display()


func _on_tower_pressed() -> void:
	if run != null:
		run.construct_home(&"tower")
	_update_display()


func _on_farm_pressed() -> void:
	if run != null:
		run.construct_home(&"farm")
	_update_display()


func _on_deploy_pressed(lane_id: StringName) -> void:
	if run == null or _pending_cards.is_empty():
		return
	var card: Variant = _pending_cards.front()
	if run.deploy_card(card, lane_id):
		_pending_cards.pop_front()
	_update_display()


func _on_retry_pressed() -> void:
	var session := get_node_or_null("../../GameSession")
	if session != null:
		session.retry_stage()


func _update_display() -> void:
	if run == null or run.economy == null:
		return
	_resource_label.text = "Gold %d   Food %d/%d" % [run.economy.gold, run.economy.food_used, run.economy.food_cap]
	_wave_label.text = "Wave %d" % run.current_wave
	var omen: float = float(run.wave_director.omen_seconds_remaining()) if run.wave_director != null else 0.0
	_omen_label.text = "Next omen %.0fs" % omen
	_cards_label.text = "Cards: %s" % ", ".join(_pending_cards.map(func(card: Variant) -> String: return str(card.archetype_id)))
	_result_label.visible = run.result_state != run.RUNNING
	_result_label.text = "Stage %s" % str(run.result_state).capitalize()
	_retry_button.visible = run.result_state != run.RUNNING

```

## `scripts/units/deployment_service.gd`

Category: `ACTIVE` / 28 lines

```text
class_name DeploymentService
extends RefCounted

const LANE_IDS := [&"top", &"middle", &"bottom"]

var economy: Variant
var manifest: Variant
var deployed_cards: Array[UnitSpawnDefinition] = []


func _init(assigned_economy: Variant, assigned_manifest: Variant) -> void:
	economy = assigned_economy
	manifest = assigned_manifest


func deploy(card: UnitSpawnDefinition, lane_id: StringName, position: float) -> bool:
	if card == null or not LANE_IDS.has(lane_id) or not economy.try_reserve_food(card.food_cost):
		return false
	var deployed := card.duplicate() as UnitSpawnDefinition
	deployed.lane_id = lane_id
	deployed_cards.append(deployed)
	manifest.input_log.append({
		"action": "deploy",
		"lane_id": str(lane_id),
		"position": position,
		"card": deployed.to_dictionary(),
	})
	return true

```

## `tests/README.md`

Category: `ACTIVE` / 3 lines

```text
# Tests placeholder

엔진 선정 후 헤드리스 시뮬레이션, 데이터 검증, 상성 테스트, 룰렛 확률 테스트의 실행 방법을 이곳에 기록합니다.

```

## `tests/headless/battle_simulation_test.gd`

Category: `ACTIVE` / 163 lines

```text
extends SceneTree

const DataRegistry = preload("res://scripts/core/data_registry.gd")
const UnitSpawnDefinition = preload("res://scripts/data/unit_spawn_definition.gd")

const BOOTSTRAP_CATALOG_PATH := "res://data/bootstrap_catalog.tres"
const BATTLE_SIMULATOR_PATH := "res://scripts/battle/battle_simulator.gd"
const GATE_STATE_PATH := "res://scripts/battle/gate_state.gd"
const OUTPOST_STATE_PATH := "res://scripts/battle/outpost_state.gd"


func _init() -> void:
	var failures := PackedStringArray()
	var simulator_script := load(BATTLE_SIMULATOR_PATH)
	var gate_script := load(GATE_STATE_PATH)
	var outpost_script := load(OUTPOST_STATE_PATH)
	_expect(simulator_script != null, "battle simulator script exists", failures)
	_expect(gate_script != null, "gate state script exists", failures)
	_expect(outpost_script != null, "outpost state script exists", failures)
	if simulator_script != null:
		_test_shared_stats_and_lane_isolation(simulator_script, failures)
		_test_fixed_seed_snapshot_repeatability(simulator_script, failures)
	if gate_script != null:
		_test_gate_multipliers_and_collapse(gate_script, failures)
	if outpost_script != null:
		_test_outpost_capture_sequence(outpost_script, failures)
		_test_outpost_capture_power_scaling(outpost_script, failures)
		_test_outpost_capture_power_requires_discrete_values(outpost_script, failures)
		_test_outpost_exit_hold_and_reversion(outpost_script, failures)
	_finish(failures)


func _test_shared_stats_and_lane_isolation(simulator_script: GDScript, failures: PackedStringArray) -> void:
	var simulator: Variant = simulator_script.new(_registry(), 91)
	var registry: Variant = _registry()
	for archetype in registry.catalog.archetypes:
		var public_stats: Variant = archetype.get("base_stats")
		_expect(public_stats is Dictionary and not public_stats.is_empty(), "%s exposes public base combat stats" % archetype.archetype_id, failures)
		var lumern: Variant = simulator.spawn_unit(_spawn(&"lumern", &"top", archetype.archetype_id))
		var veil: Variant = simulator.spawn_unit(_spawn(&"veil", &"top", archetype.archetype_id))
		_expect(lumern.combat_stats() == veil.combat_stats(), "%s visual faction does not alter combat stats" % archetype.archetype_id, failures)
		if public_stats is Dictionary:
			_expect(lumern.combat_stats() == public_stats, "%s unit stats derive from public profile data" % archetype.archetype_id, failures)
	var lumern: Variant = simulator.lanes[&"top"].units[0]
	_expect(not simulator.request_lane_move(lumern, &"middle"), "ordinary top lane units cannot move to middle", failures)
	_expect(lumern.lane_id == &"top", "rejected lane movement preserves the original lane", failures)
	_expect(simulator.lanes[&"middle"].units.is_empty(), "middle lane does not own top lane units", failures)


func _test_gate_multipliers_and_collapse(gate_script: GDScript, failures: PackedStringArray) -> void:
	var gate: Variant = gate_script.new()
	var expected_normal := 1000.0 * 0.4 * 100.0 / 180.0
	_expect(is_equal_approx(gate.apply_damage(1000.0, false), expected_normal), "normal damage uses the 0.4 structure multiplier and 80 resistance", failures)
	var expected_siege := 1000.0 * 2.0 * 100.0 / 180.0
	_expect(is_equal_approx(gate.apply_damage(1000.0, true), expected_siege), "siege damage uses the 2.0 structure multiplier and 80 resistance", failures)
	gate.apply_damage(100000.0, true)
	_expect(gate.is_collapsing(), "destroyed gate enters the two-second collapse state", failures)
	gate.advance(1.9)
	_expect(not gate.is_collapsed(), "gate does not collapse before two seconds", failures)
	gate.advance(0.1)
	_expect(gate.is_collapsed(), "gate collapses after two seconds", failures)


func _test_outpost_capture_sequence(outpost_script: GDScript, failures: PackedStringArray) -> void:
	var outpost: Variant = outpost_script.new(&"veil", true)
	outpost.begin_capture(&"lumern", 2.0)
	_expect(outpost.construction_locked and not outpost.existing_buildings_enabled, "capture start locks construction and disables existing buildings", failures)
	outpost.advance(5.0)
	_expect(outpost.state == outpost.CAPTURING, "power two neutralizes an outpost in five seconds", failures)
	outpost.advance(5.0)
	_expect(outpost.owner_team_id == &"lumern", "capture completion assigns the new owner", failures)
	_expect(outpost.prior_building_ruined, "capture completion ruins the prior building", failures)
	_expect(outpost.state == outpost.STABILIZING, "capture completion begins stabilization", failures)
	outpost.advance(5.0)
	_expect(outpost.state == outpost.STABLE and not outpost.construction_locked, "five-second stabilization unlocks new-owner construction", failures)


func _test_outpost_capture_power_scaling(outpost_script: GDScript, failures: PackedStringArray) -> void:
	var zero_power: Variant = outpost_script.new(&"veil")
	zero_power.begin_capture(&"lumern", 0.0)
	zero_power.advance(20.0)
	_expect(zero_power.state == zero_power.NEUTRALIZING, "capture power zero does not progress neutralization", failures)
	_expect(is_equal_approx(float(zero_power.snapshot().get("capture_progress", -1.0)), 0.0), "capture power zero keeps progress at zero", failures)
	var one_power: Variant = outpost_script.new(&"veil")
	one_power.begin_capture(&"lumern", 1.0)
	one_power.advance(9.9)
	_expect(one_power.state == one_power.NEUTRALIZING, "capture power one has not neutralized before ten seconds", failures)
	one_power.advance(0.1)
	_expect(one_power.state == one_power.CAPTURING, "capture power one neutralizes in ten seconds", failures)
	var two_power: Variant = outpost_script.new(&"veil")
	two_power.begin_capture(&"lumern", 2.0)
	two_power.advance(4.9)
	_expect(two_power.state == two_power.NEUTRALIZING, "capture power two has not neutralized before five seconds", failures)
	two_power.advance(0.1)
	_expect(two_power.state == two_power.CAPTURING, "capture power two neutralizes in five seconds", failures)


func _test_outpost_capture_power_requires_discrete_values(outpost_script: GDScript, failures: PackedStringArray) -> void:
	for invalid_power in [0.5, 1.5]:
		var outpost: Variant = outpost_script.new(&"veil")
		outpost.begin_capture(&"lumern", invalid_power)
		outpost.advance(20.0)
		_expect(is_equal_approx(float(outpost.snapshot().get("capture_power", -1.0)), 0.0), "capture power %s normalizes to zero" % invalid_power, failures)
		_expect(is_equal_approx(float(outpost.snapshot().get("capture_progress", -1.0)), 0.0), "capture power %s does not drive capture progress" % invalid_power, failures)


func _test_outpost_exit_hold_and_reversion(outpost_script: GDScript, failures: PackedStringArray) -> void:
	var outpost: Variant = outpost_script.new(&"veil", true)
	outpost.begin_capture(&"lumern", 2.0)
	outpost.advance(5.0)
	outpost.lose_capture_power(20.0)
	_expect(outpost.state == outpost.CAPTURING, "capturer exit does not immediately discard capture progress", failures)
	_expect(is_equal_approx(float(outpost.snapshot().get("capture_progress", -1.0)), 1.0), "capturer exit preserves capture progress during the hold", failures)
	outpost.advance(3.0)
	_expect(is_equal_approx(float(outpost.snapshot().get("capture_progress", -1.0)), 1.0), "capture progress remains frozen for the three-second exit hold", failures)
	outpost.advance(1.0)
	_expect(is_equal_approx(float(outpost.snapshot().get("capture_progress", -1.0)), 0.9), "capture progress reverts at ten percent per second after the hold", failures)
	outpost.advance(9.0)
	_expect(outpost.state == outpost.STABLE and outpost.owner_team_id == &"veil", "fully reverted capture restores the previous stable owner", failures)
	_expect(not outpost.construction_locked and outpost.existing_buildings_enabled, "fully reverted capture restores the previous stable building state", failures)


func _test_fixed_seed_snapshot_repeatability(simulator_script: GDScript, failures: PackedStringArray) -> void:
	var first: Variant = simulator_script.new(_registry(), 314159)
	var second: Variant = simulator_script.new(_registry(), 314159)
	for simulator in [first, second]:
		simulator.spawn_unit(_spawn(&"lumern", &"top"))
		simulator.spawn_unit(_spawn(&"veil", &"top"))
		simulator.spawn_unit(_spawn(&"lumern", &"bottom", &"archer"))
		for _step in 20:
			simulator.advance(0.1)
	_expect(JSON.stringify(first.snapshot()) == JSON.stringify(second.snapshot()), "identical seeds and inputs reproduce the same battle snapshot", failures)


func _registry() -> Variant:
	var registry: Variant = DataRegistry.new()
	var errors: PackedStringArray = registry.load_bootstrap_catalog(BOOTSTRAP_CATALOG_PATH)
	if not errors.is_empty():
		push_error("battle test registry failed to load: %s" % errors)
	return registry


func _spawn(visual_faction_id: StringName, lane_id: StringName, archetype_id: StringName = &"shield_guard") -> UnitSpawnDefinition:
	var spawn := UnitSpawnDefinition.new()
	spawn.archetype_id = archetype_id
	spawn.owner_team_id = visual_faction_id
	spawn.visual_faction_id = visual_faction_id
	spawn.lane_id = lane_id
	return spawn


func _expect(condition: bool, message: String, failures: PackedStringArray) -> void:
	if not condition:
		failures.append(message)


func _finish(failures: PackedStringArray) -> void:
	if failures.is_empty():
		print("Battle simulation checks passed")
		quit(0)
	else:
		printerr("Battle simulation failures:\n%s" % "\n".join(failures))
		quit(1)

```

## `tests/headless/economy_roulette_test.gd`

Category: `ACTIVE` / 128 lines

```text
extends SceneTree

const StageManifest = preload("res://scripts/core/stage_manifest.gd")
const OutpostState = preload("res://scripts/battle/outpost_state.gd")
const UnitSpawnDefinition = preload("res://scripts/data/unit_spawn_definition.gd")


func _init() -> void:
	var failures := PackedStringArray()
	var economy_script := load("res://scripts/core/stage_economy.gd")
	var building_service_script := load("res://scripts/buildings/building_service.gd")
	var roulette_script := load("res://scripts/roulette/roulette_service.gd")
	var deployment_script := load("res://scripts/units/deployment_service.gd")
	_expect(economy_script != null, "stage economy service exists", failures)
	_expect(building_service_script != null, "building service exists", failures)
	_expect(roulette_script != null, "roulette service exists", failures)
	_expect(deployment_script != null, "deployment service exists", failures)
	if economy_script != null:
		_test_stage_economy(economy_script, failures)
	if economy_script != null and building_service_script != null:
		_test_building_ownership_and_capture_lock(economy_script, building_service_script, failures)
		_test_stabilized_capture_allows_rebuilding(economy_script, building_service_script, failures)
	if economy_script != null and building_service_script != null and roulette_script != null:
		_test_deterministic_nine_cell_roulette(economy_script, building_service_script, roulette_script, failures)
	if economy_script != null and deployment_script != null:
		_test_deployment_food_limit(economy_script, deployment_script, failures)
	_finish(failures)


func _test_stage_economy(economy_script: GDScript, failures: PackedStringArray) -> void:
	var economy: Variant = economy_script.new(_manifest())
	_expect(economy.gold == 160, "regular stage starts at 160 gold", failures)
	_expect(economy.food_cap == 12, "regular stage starts with 12 food", failures)
	economy.advance(60.0, 1, 1)
	_expect(economy.gold == 183, "active combat grants base, controlled clash, and stable outpost income on their exact intervals", failures)


func _test_building_ownership_and_capture_lock(economy_script: GDScript, building_service_script: GDScript, failures: PackedStringArray) -> void:
	var economy: Variant = economy_script.new(_manifest())
	var buildings: Variant = building_service_script.new(economy, _manifest())
	var enemy_outpost := OutpostState.new(&"veil")
	var player_outpost := OutpostState.new(&"lumern")
	buildings.register_outpost(&"enemy_top", enemy_outpost, [&"front_a"])
	buildings.register_outpost(&"player_top", player_outpost, [&"front_a", &"front_b"])
	_expect(not buildings.try_construct(&"enemy_top", &"front_a", &"tower"), "enemy-owned node rejects player building", failures)
	_expect(buildings.try_construct(&"player_top", &"front_a", &"tower"), "owned stabilized outpost accepts a tower", failures)
	player_outpost.begin_capture(&"veil", 1.0)
	_expect(not buildings.try_construct(&"player_top", &"front_b", &"farm"), "capture locks construction nodes", failures)


func _test_stabilized_capture_allows_rebuilding(economy_script: GDScript, building_service_script: GDScript, failures: PackedStringArray) -> void:
	var economy: Variant = economy_script.new(_manifest())
	var buildings: Variant = building_service_script.new(economy, _manifest())
	var outpost := OutpostState.new(&"veil", true)
	buildings.register_outpost(&"captured_top", outpost, [&"front_a"])
	outpost.begin_capture(&"lumern", 1.0)
	outpost.advance(20.0)
	outpost.advance(5.0)
	_expect(buildings.try_construct(&"captured_top", &"front_a", &"farm"), "a captured outpost accepts new construction after stabilization", failures)


func _test_deterministic_nine_cell_roulette(economy_script: GDScript, building_service_script: GDScript, roulette_script: GDScript, failures: PackedStringArray) -> void:
	var first_manifest := _manifest()
	var first_economy: Variant = economy_script.new(first_manifest)
	var first_buildings: Variant = building_service_script.new(first_economy, first_manifest)
	var outpost := OutpostState.new(&"lumern")
	first_buildings.register_outpost(&"player_top", outpost, [&"front_a"])
	first_buildings.try_construct(&"player_top", &"front_a", &"tower")
	var first_roulette: Variant = roulette_script.new(first_economy, first_buildings, first_manifest, &"lumern")
	var first_result: Array = first_roulette.spin({"seed": 12})
	_expect(first_result.size() == 9, "a paid roulette spin resolves a deterministic 3x3 board", failures)
	_expect(first_economy.gold == 105, "tower construction and one roulette spin charge their approved costs", failures)
	for card in first_result:
		_expect(card is UnitSpawnDefinition, "roulette produces only shared unit spawn definitions", failures)
		if card is UnitSpawnDefinition:
			_expect(card.owner_team_id == &"lumern" and card.visual_faction_id == &"lumern", "roulette cards use the player shared-unit faction contract", failures)
	var second_manifest := _manifest()
	var second_economy: Variant = economy_script.new(second_manifest)
	var second_buildings: Variant = building_service_script.new(second_economy, second_manifest)
	var second_outpost := OutpostState.new(&"lumern")
	second_buildings.register_outpost(&"player_top", second_outpost, [&"front_a"])
	second_buildings.try_construct(&"player_top", &"front_a", &"tower")
	var second_roulette: Variant = roulette_script.new(second_economy, second_buildings, second_manifest, &"lumern")
	var second_result: Array = second_roulette.spin({"seed": 12})
	_expect(_cards_json(first_result) == _cards_json(second_result), "identical roulette seed and build inputs reproduce identical cards", failures)
	_expect(first_manifest.input_log.size() == 2, "construction and roulette commands are recorded in the manifest", failures)


func _test_deployment_food_limit(economy_script: GDScript, deployment_script: GDScript, failures: PackedStringArray) -> void:
	var manifest := _manifest()
	var economy: Variant = economy_script.new(manifest)
	var deployment: Variant = deployment_script.new(economy, manifest)
	var card := UnitSpawnDefinition.new()
	card.archetype_id = &"shield_guard"
	card.owner_team_id = &"lumern"
	card.visual_faction_id = &"lumern"
	card.food_cost = 12
	_expect(deployment.deploy(card, &"top", 10.0), "deployment reserves available food", failures)
	_expect(not deployment.deploy(card, &"top", 20.0), "deployment rejects cards that exceed the food cap", failures)
	_expect(economy.food_used == 12, "rejected deployment does not spend additional food", failures)
	_expect(manifest.input_log.size() == 1, "only accepted deployment commands are recorded", failures)


func _manifest() -> StageManifest:
	var manifest := StageManifest.new()
	manifest.stage_id = "regular_stage"
	manifest.seed = 101
	manifest.starting_gold = 160
	manifest.starting_food_cap = 12
	return manifest


func _cards_json(cards: Array) -> String:
	return JSON.stringify(cards.map(func(card: UnitSpawnDefinition) -> Dictionary: return card.to_dictionary()))


func _expect(condition: bool, message: String, failures: PackedStringArray) -> void:
	if not condition:
		failures.append(message)


func _finish(failures: PackedStringArray) -> void:
	if failures.is_empty():
		print("Economy, construction, roulette, and deployment checks passed")
		quit(0)
	else:
		printerr("Economy, construction, roulette, and deployment failures:\n%s" % "\n".join(failures))
		quit(1)

```

## `tests/headless/stage_data_contract_test.gd`

Category: `ACTIVE` / 152 lines

```text
extends SceneTree

const BootstrapValidator = preload("res://scripts/core/bootstrap_validator.gd")
const DataRegistry = preload("res://scripts/core/data_registry.gd")
const StageDefinition = preload("res://scripts/data/stage_definition.gd")
const UnitSpawnDefinition = preload("res://scripts/data/unit_spawn_definition.gd")

const BOOTSTRAP_CATALOG_PATH := "res://data/bootstrap_catalog.tres"
const TUTORIAL_STAGE_PATH := "res://data/stages/tutorial_stage.tres"
const REGULAR_STAGE_PATH := "res://data/stages/regular_stage.tres"
const MANIFEST_SEED := 20260716


func _init() -> void:
	var failures := PackedStringArray()
	var tutorial := ResourceLoader.load(TUTORIAL_STAGE_PATH)
	var regular := ResourceLoader.load(REGULAR_STAGE_PATH)

	_expect(tutorial != null, "tutorial stage resource must load", failures)
	_expect(regular != null, "regular stage resource must load", failures)
	if tutorial != null:
		_expect(_waves(tutorial).size() == 4, "tutorial has four waves", failures)
	if regular != null:
		var waves := _waves(regular)
		_expect(waves.size() == 20, "regular stage has W1 through W20", failures)
		if waves.size() >= 20:
			_expect(waves[14].boss_kind == &"legendary", "W15 is legendary", failures)
			_expect(waves[19].boss_kind == &"mythic", "W20 is mythic", failures)
		_assert_regular_manifest_contract(regular as StageDefinition, failures)

	_expect_spawn_is_rejected(
		&"enemy_only",
		&"veil",
		&"veil",
		&"top",
		"unknown spawn archetype IDs are rejected",
		"unknown spawn archetype_id: enemy_only",
		failures,
	)
	_expect_spawn_is_rejected(
		&"shield_guard",
		&"other",
		&"veil",
		&"top",
		"non-lumern/veil visual factions are rejected",
		"invalid spawn visual_faction_id: other",
		failures,
	)
	_expect_spawn_is_rejected(
		&"shield_guard",
		&"veil",
		&"other",
		&"top",
		"non-lumern/veil owner teams are rejected",
		"invalid spawn owner_team_id: other",
		failures,
	)
	_expect_spawn_is_rejected(
		&"shield_guard",
		&"veil",
		&"veil",
		&"side",
		"lane IDs outside top/middle/bottom are rejected",
		"invalid spawn lane_id: side",
		failures,
	)

	if failures.is_empty():
		print("Stage data contract checks passed")
		quit(0)
	else:
		printerr("Stage data contract failures:\n%s" % "\n".join(failures))
		quit(1)


func _waves(stage: Resource) -> Array:
	return stage.get("waves") as Array


func _assert_regular_manifest_contract(regular: StageDefinition, failures: PackedStringArray) -> void:
	var parsed: Variant = JSON.parse_string(regular.build_manifest(MANIFEST_SEED).to_json())
	_expect(parsed is Dictionary, "regular manifest JSON parses into an object", failures)
	if not parsed is Dictionary:
		return
	var manifest: Dictionary = parsed
	_expect(manifest.get("stage_id") == "regular_stage", "manifest includes the regular stage ID", failures)
	_expect(manifest.get("seed") == MANIFEST_SEED, "manifest includes the supplied seed", failures)
	_expect(manifest.get("starting_gold") == 160, "manifest includes starting gold", failures)
	_expect(manifest.get("starting_food_cap") == 12, "manifest includes starting food cap", failures)
	_expect(manifest.get("tutorial_stage") == false, "manifest identifies the regular stage", failures)
	_expect(manifest.get("wave_count") == 20, "manifest includes the regular wave count", failures)

	var manifest_waves: Array = manifest.get("waves", []) as Array
	_expect(manifest_waves.size() == 20, "manifest includes resolved waves", failures)
	if manifest_waves.is_empty():
		return
	var first_wave: Dictionary = manifest_waves[0] as Dictionary
	_expect(first_wave.has("wave_number"), "manifest wave includes a wave number", failures)
	_expect(first_wave.has("omen_lead_seconds"), "manifest wave includes omen lead time", failures)
	_expect(first_wave.has("boss_kind"), "manifest wave includes boss kind", failures)
	_expect(first_wave.has("is_overtime"), "manifest wave includes overtime state", failures)
	var spawns: Array = first_wave.get("spawns", []) as Array
	_expect(not spawns.is_empty(), "manifest wave includes resolved spawns", failures)
	if spawns.is_empty():
		return
	var first_spawn: Dictionary = spawns[0] as Dictionary
	for field in ["archetype_id", "tier_id", "rank_id", "owner_team_id", "visual_faction_id", "lane_id", "spawn_delay_seconds"]:
		_expect(first_spawn.has(field), "manifest spawn includes %s" % field, failures)

	var input_log: Variant = manifest.get("input_log")
	_expect(input_log is Array, "manifest includes an input log array", failures)
	if input_log is Array:
		_expect((input_log as Array).is_empty(), "new manifests begin with an empty input log", failures)


func _expect_spawn_is_rejected(
	archetype_id: StringName,
	visual_faction_id: StringName,
	owner_team_id: StringName,
	lane_id: StringName,
	message: String,
	expected_error: String,
	failures: PackedStringArray,
) -> void:
	var errors := _invalid_spawn_errors(archetype_id, visual_faction_id, owner_team_id, lane_id)
	_expect(errors.has(expected_error), "%s: %s" % [message, errors], failures)


func _invalid_spawn_errors(
	archetype_id: StringName,
	visual_faction_id: StringName,
	owner_team_id: StringName,
	lane_id: StringName,
) -> PackedStringArray:
	var registry: DataRegistry = DataRegistry.new()
	var load_errors := registry.load_bootstrap_catalog(BOOTSTRAP_CATALOG_PATH)
	if not load_errors.is_empty():
		return load_errors
	var regular: StageDefinition = registry.stage_definition(&"regular_stage").duplicate(true) as StageDefinition
	var spawn: UnitSpawnDefinition = regular.waves[0].spawns[0].duplicate() as UnitSpawnDefinition
	spawn.archetype_id = archetype_id
	spawn.visual_faction_id = visual_faction_id
	spawn.owner_team_id = owner_team_id
	spawn.lane_id = lane_id
	regular.waves[0].spawns[0] = spawn
	registry.stages[str(regular.stage_id)] = regular
	return BootstrapValidator.new().validate_registry(registry)


func _expect(condition: bool, message: String, failures: PackedStringArray) -> void:
	if not condition:
		failures.append(message)

```

## `tests/headless/stage_run_test.gd`

Category: `ACTIVE` / 109 lines

```text
extends SceneTree

const DataRegistry = preload("res://scripts/core/data_registry.gd")
const UnitSpawnDefinition = preload("res://scripts/data/unit_spawn_definition.gd")

const BOOTSTRAP_CATALOG_PATH := "res://data/bootstrap_catalog.tres"
const TUTORIAL_STAGE_PATH := "res://data/stages/tutorial_stage.tres"
const REGULAR_STAGE_PATH := "res://data/stages/regular_stage.tres"


func _init() -> void:
	var failures := PackedStringArray()
	var stage_run_script := load("res://scripts/core/stage_run.gd")
	var progression_script := load("res://scripts/core/stage_progression.gd")
	var wave_director_script := load("res://scripts/waves/wave_director.gd")
	var bypass_script := load("res://scripts/battle/assassin_bypass_state.gd")
	var battle_script := load("res://scripts/battle/battle_simulator.gd")
	_expect(stage_run_script != null, "stage run service exists", failures)
	_expect(progression_script != null, "stage progression service exists", failures)
	_expect(wave_director_script != null, "wave director service exists", failures)
	_expect(bypass_script != null, "assassin bypass state exists", failures)
	if stage_run_script != null and progression_script != null:
		_test_tutorial_unlock_and_regular_wave_progression(stage_run_script, progression_script, failures)
	if bypass_script != null:
		_test_assassin_bypass_timing(bypass_script, failures)
	if bypass_script != null and battle_script != null:
		_test_assassin_bypass_leaves_and_returns_to_same_lane(battle_script, failures)
	_finish(failures)


func _test_tutorial_unlock_and_regular_wave_progression(stage_run_script: GDScript, progression_script: GDScript, failures: PackedStringArray) -> void:
	var tutorial: Resource = ResourceLoader.load(TUTORIAL_STAGE_PATH)
	var regular: Resource = ResourceLoader.load(REGULAR_STAGE_PATH)
	var progression: Variant = progression_script.new()
	var run: Variant = stage_run_script.new(progression)
	run.start(tutorial, 1001)
	_expect(run.result_state == &"running", "stage run begins with the tutorial", failures)
	_advance_waves(run, 4)
	_expect(run.current_wave == 4, "tutorial reaches W4 from its declared data", failures)
	run.submit_command({"action": "stage_victory"})
	_expect(progression.regular_unlocked, "tutorial victory unlocks the regular stage for this session", failures)
	run.start(regular, 1001)
	_advance_waves(run, 15)
	_expect(run.current_wave == 15, "regular progression reaches W15", failures)
	_expect(run.wave_director.current_wave().boss_kind == &"legendary", "W15 uses the existing legendary wave definition", failures)
	_advance_waves(run, 16)
	for wave_number in range(16, 20):
		_expect(run.wave_director.wave_at(wave_number).is_overtime, "W%s is marked as overtime" % wave_number, failures)
	_advance_waves(run, 20)
	_expect(run.current_wave == 20, "regular progression reaches W20", failures)
	_expect(run.wave_director.current_wave().boss_kind == &"mythic", "W20 uses the existing mythic wave definition", failures)


func _test_assassin_bypass_timing(bypass_script: GDScript, failures: PackedStringArray) -> void:
	var bypass: Variant = bypass_script.new(&"middle", 500.0)
	_expect(bypass.capture_power == 0.0, "assassin bypass never contributes capture power", failures)
	bypass.advance(1.0)
	_expect(bypass.state == &"travel", "assassin enters travel after one second of windup", failures)
	bypass.advance(6.49)
	_expect(not bypass.warning_active, "warning remains hidden until 2.5 seconds before arrival", failures)
	bypass.advance(0.01)
	_expect(bypass.warning_active, "warning activates exactly 2.5 seconds before arrival", failures)
	bypass.advance(2.5)
	_expect(bypass.state == &"recovery" and bypass.exit_position == 620.0, "assassin arrives in the same lane 120 units behind the enemy outpost", failures)
	bypass.advance(0.6)
	_expect(bypass.is_complete(), "assassin completes the required 0.6 second arrival recovery", failures)


func _test_assassin_bypass_leaves_and_returns_to_same_lane(battle_script: GDScript, failures: PackedStringArray) -> void:
	var battle: Variant = battle_script.new(_registry(), 11)
	var assassin := UnitSpawnDefinition.new()
	assassin.archetype_id = &"assassin"
	assassin.owner_team_id = &"lumern"
	assassin.visual_faction_id = &"lumern"
	assassin.lane_id = &"bottom"
	var unit: Variant = battle.spawn_unit(assassin)
	_expect(battle.request_assassin_bypass(unit, 100.0), "assassin can start its same-lane bypass", failures)
	battle.advance(1.0)
	_expect(battle.lanes[&"bottom"].units.is_empty(), "assassin is removed from the lane during travel", failures)
	battle.advance(9.6)
	_expect(battle.lanes[&"bottom"].units.size() == 1, "assassin returns to its original lane after recovery", failures)
	_expect(is_equal_approx(float(battle.lanes[&"bottom"].units[0].lane_position), 220.0), "assassin returns behind the same lane enemy outpost", failures)


func _advance_waves(run: Variant, target_wave: int) -> void:
	while run.current_wave < target_wave:
		run.advance(60.0)


func _registry() -> Variant:
	var registry := DataRegistry.new()
	var errors: PackedStringArray = registry.load_bootstrap_catalog(BOOTSTRAP_CATALOG_PATH)
	if not errors.is_empty():
		push_error("stage run test registry failed to load: %s" % errors)
	return registry


func _expect(condition: bool, message: String, failures: PackedStringArray) -> void:
	if not condition:
		failures.append(message)


func _finish(failures: PackedStringArray) -> void:
	if failures.is_empty():
		print("Stage run, wave, progression, and assassin bypass checks passed")
		quit(0)
	else:
		printerr("Stage run, wave, progression, and assassin bypass failures:\n%s" % "\n".join(failures))
		quit(1)

```

## `tests/python/test_skill_routing_contract.py`

Category: `ACTIVE` / 63 lines

```text
from __future__ import annotations

import pathlib
import sys
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools"))

from route_skills import load_registry, route  # noqa: E402

REGISTRY = load_registry(ROOT / "docs" / "base" / "SKILL_REGISTRY.json")


def ids(result: dict) -> list[str]:
    return [item["id"] for item in result["skills"]]


class SkillRoutingTests(unittest.TestCase):
    def test_review_forces_adversarial_stack(self) -> None:
        result = route("PR의 누락과 중복을 적대적으로 검토하고 레드팀 검증해줘", REGISTRY)
        selected = ids(result)
        self.assertEqual(result["mode"], "REVIEW")
        self.assertIn("foundation.project-intake", selected)
        self.assertIn("foundation.validation-review", selected)
        self.assertIn("discipline.integration-review", selected)
        self.assertEqual(len(selected), len(set(selected)))

    def test_game_design_plan(self) -> None:
        result = route("룰렛 확률과 보상 규칙을 기획해줘", REGISTRY)
        self.assertEqual(result["mode"], "PLAN")
        self.assertIn("discipline.game-design", ids(result))

    def test_engineering_build(self) -> None:
        result = route("Godot GDScript 성능 버그를 수정해줘", REGISTRY)
        self.assertEqual(result["mode"], "BUILD")
        self.assertIn("discipline.engineering", ids(result))

    def test_ui_art_audit_selects_specialist(self) -> None:
        result = route("HUD UI 아트의 화면 가독성을 시각 감사해줘", REGISTRY)
        selected = ids(result)
        self.assertEqual(result["mode"], "REVIEW")
        self.assertIn("specialist.ui-art-audit", selected)
        self.assertTrue({"discipline.ux-ui-accessibility", "discipline.art"} & set(selected))

    def test_dependencies_precede_dependents(self) -> None:
        result = route("수직 슬라이스 MVP를 설계해줘", REGISTRY)
        selected = ids(result)
        specialist_index = selected.index("specialist.vertical-slice")
        for dependency in ("discipline.game-design", "discipline.engineering", "discipline.production-pm"):
            self.assertLess(selected.index(dependency), specialist_index)

    def test_generic_request_does_not_enable_specialists(self) -> None:
        result = route("프로젝트 작업을 정리해줘", REGISTRY)
        self.assertFalse(any(skill_id.startswith("specialist.") for skill_id in ids(result)))

    def test_unknown_manual_override_is_rejected(self) -> None:
        with self.assertRaises(ValueError):
            route("검토", REGISTRY, forced_skills=["specialist.does-not-exist"])


if __name__ == "__main__":
    unittest.main()

```

## 활성 파일의 구형 상태·명칭 후보

### `AGENTS.md`

Hits: `구현 전` [37]

```text
   35: 
   36: - 기획/조정 AI: 플레이어 경험, 사양, 범위, 제외 범위, 책임 원본, 완료 기준과 검증 방법을 정리하고 확정 사항을 GitHub 문서에 반영한다.
   37: - Codex Plan Mode: 저장소와 참고 자료를 읽기 전용으로 조사하고 구현 전에 검토 가능한 제안서를 작성한다.
   38: - Codex 구현 모드: 사용자가 승인한 제안서와 Issue/Goal만 구현하고 제품 방향을 임의로 확장하지 않는다.
   39: - 아트·콘텐츠 작업자: 프로젝트 아트·연출 계약과 공용 데이터 구조를 유지하며 실제 화면 크기에서 검수한다.
```

### `docs/ACTIVE_CONTEXT.md`

Hits: `구현 전` [241]

```text
  239: 
  240: - 새 Codex 채팅은 `docs/PROJECT_CORE.md`와 `docs/CURRENT_IMPLEMENTATION_STATUS.md`를 먼저 읽는다.
  241: - 현재 저장소를 `구현 전` 또는 `수직 슬라이스 완료` 중 하나로 단순화하지 않는다.
  242: - 다음 게임 기능 PR은 승인 룰렛 계약 복구만 포함한다.
  243: - 시각·병종·UI 작업은 새 병종 비주얼 책임 문서와 시각자료 인덱스를 반드시 읽는다.
```

### `docs/CURRENT_IMPLEMENTATION_STATUS.md`

Hits: `구현 전` [137]

```text
  135: - README·GDD·로드맵·상태·인수인계·미확정 목록이 같은 단계 용어를 사용한다.
  136: - 현재 구현과 미구현을 파일 증거로 분리한다.
  137: - 과거 `구현 전`과 과도한 `수직 슬라이스 완료` 주장을 현재 상태로 사용하지 않는다.
  138: - 프로젝트 코어는 2026-07-22 사용자 확인으로 `CORE_CONFIRMED`·`CORE_LOCKED`다.
  139: - 다음 변경은 게임 코드 전체가 아니라 승인 룰렛 계약 복구로 한정한다.
```

### `docs/DOCUMENTATION_MAP.md`

Hits: `0001-phase-0-codex-plan-mode` [40, 59, 68], `구현 전` [43, 69], `roulettebound` [108], `율비` [108], `경계의 율` [108], `은종성채` [108], `무명야` [108]

```text
   38: |---|---|---|
   39: | 현재 main 감사·다음 개선 Plan Mode | `work_orders/0002-current-main-audit-and-next-iteration-plan-mode.md` | **활성 시작 문서** |
   40: | Phase 0 Bootstrap | `goals/0001-engine-selection-and-bootstrap.md`, `work_orders/0001-phase-0-codex-plan-mode.md` | 구현 이후의 과거 입력·변경 이력 |
   41: | 수직 슬라이스 | `goals/0002-core-vertical-slice.md`, 관련 Issue·validation | 실제 main과 테스트 재확인 대상 |
   42: 
   43: 새 Codex 채팅은 `work_orders/0002-current-main-audit-and-next-iteration-plan-mode.md`에서 시작한다. 과거 `0001` Work Order의 `구현 전` 문구를 현재 상태로 사용하지 않는다.
   44: 
   45: ## 항상 확인할 공식 문서
   57: | `images/VISUAL_REFERENCE_INDEX.md` | 이미지 상태·우선순위·누락 감사 |
   58: | `work_orders/0002-current-main-audit-and-next-iteration-plan-mode.md` | 현재 새 Codex 채팅 작업 요청·복사 프롬프트 |
   59: | `work_orders/0001-phase-0-codex-plan-mode.md` | Phase 0 이전에 사용한 과거 작업 요청 |
   60: | `design/proposals/0001-phase-0-godot-bootstrap.md` | Phase 0 사전 기술 추천안·변경 이력 |
   61: 
   66: | 프로젝트 코어·우선순위·기능 제거 판단 | `PROJECT_CORE.md`, `CURRENT_IMPLEMENTATION_STATUS.md`, 관련 APPROVED 문서 |
   67: | 새 Codex 채팅·현재 main 조사 | `PROJECT_CORE.md`, `CURRENT_IMPLEMENTATION_STATUS.md`, `work_orders/0002-current-main-audit-and-next-iteration-plan-mode.md`, `PROPOSAL_WORKFLOW.md`, 현재 Issue·PR·Goal |
   68: | 과거 Phase 0 결정 추적 | `work_orders/0001-phase-0-codex-plan-mode.md`, `design/proposals/0001-phase-0-godot-bootstrap.md`, Goal 0001 |
   69: | Codex가 작성한 구현 전 제안 검토 | Codex 제출 제안서, 관련 작업 요청서, 현재 Issue/Goal |
   70: | 문서 추가·교체·정리·인수인계 | `DOCUMENT_LIFECYCLE.md`, `HANDOFF_CONTEXT.md`, `archive/README.md` |
   71: | GitHub Issue·로컬 미러 동기화 | `issues/README.md`, `DOCUMENT_LIFECYCLE.md`, `tools/sync_repo.ps1` |
  106: ```
  107: 
  108: 레거시 명칭 `Roulettebound`, `율비`, `경계의 율`, `은종성채`, `무명야`는 과거 변경 이력 외에는 사용하지 않는다.
  109: 
  110: ## 핵심 책임 원본
```

### `docs/HANDOFF_CONTEXT.md`

Hits: `구현 전` [19]

```text
   17: 1. 오멘워드는 건물로 룰렛의 토큰·확률과 증원 체계를 설계하고 세 전선을 지휘하는 판타지 전략 오토배틀 게임이다.
   18: 2. 저장소에는 Phase 0 기술 기준선과 수직 슬라이스 구성요소가 존재하지만 승인 룰렛·전투 목적·코어 UX는 미완결이다.
   19: 3. 과거 Phase 0 Work Order의 `구현 전`과 README의 과도한 `수직 슬라이스 완료`를 현재 상태로 재사용하지 않는다.
   20: 4. 새 Codex 채팅은 `PROJECT_CORE.md`, `CURRENT_IMPLEMENTATION_STATUS.md`, 실제 main, validation 문서와 Issue·PR을 대조한 뒤 다음 최소 변경을 제안한다.
   21: 5. 아군과 적군은 별도 병종 전투 데이터를 만들지 않고 공용 10병종에 서로 다른 FactionVisualProfile을 연결한다.
```

### `docs/OMENWARD_GAME_DESIGN.md`

Hits: `구현 전` [718]

```text
  716: - 최종 이미지·팔레트·아이콘·오디오.
  717: 
  718: ### 구현 전 미확정
  719: 
  720: - 정확한 Godot stable 버전.
```

### `docs/OMENWARD_ROADMAP.md`

Hits: `0001-phase-0-codex-plan-mode` [89, 110]

```text
   87: ### 완료 산출물
   88: 
   89: - `docs/work_orders/0001-phase-0-codex-plan-mode.md`.
   90: - 복사 가능한 시작 프롬프트.
   91: - 제품 컨텍스트와 불변 조건.
  108: - Issue #1.
  109: - Goal 0001.
  110: - `docs/work_orders/0001-phase-0-codex-plan-mode.md`.
  111: 
  112: ### Codex가 조사할 것
```

### `docs/PROJECT_CORE.md`

Hits: `구현 전` [117]

```text
  115: 
  116: - 프로젝트 코어, GDD, 로드맵, 현재 상태와 Issue가 같은 구현 단계를 가리킨다.
  117: - `구현 전`, `완료`, `검증됨`을 실제 증거 없이 사용하지 않는다.
  118: 
  119: ### C1 — 룰렛 인과
```

### `docs/design/APPROVED_BELLU_MASCOT_AND_GUIDE_CONTRACT.md`

Hits: `율비` [8, 24, 210], `경계의 율` [210]

```text
    6: - 세계관 명칭: `docs/design/APPROVED_OMENWARD_WORLD_AND_NAMING.md`
    7: 
    8: 이 문서는 기존 `율비` 명칭을 사용하는 마스코트 문서보다 우선한다.
    9: 
   10: ## 1. 한 문장 정의
   22: 이름은 종을 연상시키는 부드러운 `벨`과 루메른 문화권의 어감을 가진 `루`가 합쳐진 인상이다. 게임 안에서 어원을 직접 설명하지는 않는다.
   23: 
   24: 기존 `율비` 명칭은 사용하지 않는다.
   25: 
   26: ## 3. 단일 안내자 역할
  208: 
  209: - 모든 필수 안내는 벨루와 HUD만으로 이해할 수 있다.
  210: - `율비`, `경계의 율` 명칭이 신규 UI·대사에 노출되지 않는다.
  211: - 상태 반응 뒤 기본형으로 돌아와도 지속 상태가 끝난 것으로 오해되지 않는다.
  212: - 벨루가 전장 조작이나 중요 정보를 가리지 않는다.
```

### `docs/design/APPROVED_BELLU_SINGLE_GUIDE_AND_FIRST_10_MINUTE_FLOW.md`

Hits: `율비` [8, 260], `roulettebound` [260], `경계의 율` [260]

```text
    6: - 마스코트 계약: `docs/design/APPROVED_BELLU_MASCOT_AND_GUIDE_CONTRACT.md`
    7: 
    8: 이 문서는 기존 `율비` 이름을 사용하는 첫 10분 문서보다 우선한다.
    9: 
   10: ## 1. 단일 안내자
  258: - 두 번째 룰렛은 플레이어 조작으로 2줄 엘리트가 된다.
  259: - 첫 10분 안에 건설→룰렛→배치→방어 루프를 두 번 경험한다.
  260: - 신규 대사와 UI에 `율비`, `경계의 율`, `Roulettebound`를 사용하지 않는다.
```

### `docs/design/APPROVED_DOPAMINE_DRIVEN_DESIGN_AND_FIRST_10_MINUTES.md`

Hits: `roulettebound` [164], `율비` [164], `경계의 율` [164]

```text
  162: - 벨루의 설명 없이도 HUD가 필수 숫자를 전달한다.
  163: - 설명을 건너뛰어도 플레이가 막히지 않는다.
  164: - 신규 문서와 대사에 `Roulettebound`, `율비`, `경계의 율`을 사용하지 않는다.
```

### `docs/design/APPROVED_OMENWARD_WORLD_AND_NAMING.md`

Hits: `roulettebound` [7, 41, 174], `율비` [7, 177], `경계의 율` [7, 94, 175], `은종성채` [7, 62, 178], `무명야` [7, 180]

```text
    5: - 적용 범위: 게임명, 세계관, 튜토리얼, HUD, 웨이브 카드, 대사, 마케팅, 이후 모든 기획 문서
    6: 
    7: 이 문서는 기존 `Roulettebound`, `경계의 율`, `율비`, `은종성채`, `무명야` 등 임시·이전 명칭보다 우선한다.
    8: 
    9: ## 1. 게임 공식 명칭
   39: ```
   40: 
   41: 저장소명과 내부 코드명 `roulettebound-prototype`은 구현 마이그레이션 계획이 승인될 때까지 유지한다.
   42: 
   43: ## 2. 명명 원칙
   60: 
   61: - `실버벨 배스천`처럼 영어 일반명사를 모두 음차
   62: - `은종성채`처럼 번역투 고유명사만 사용
   63: - 같은 문화권에서 음차형과 한자풍 고유명사를 불규칙하게 혼합
   64: 
   92: ## 4. 베일과 베일의 법칙
   93: 
   94: 기존 `경계의 율` 공식 명칭을 다음으로 교체한다.
   95: 
   96: ```text
  172: | 이전 명칭 | 공식 명칭 |
  173: |---|---|
  174: | Roulettebound | 오멘워드 / OMENWARD |
  175: | 경계의 율 | 베일의 법칙 |
  176: | 율 | 법칙 / 베일 |
  177: | 율비 | 벨루 |
  178: | 은종성채·실버벨 배스천 | 실베른 성채 |
  179: | 삼문경계·쓰리게이트 프론트 | 트리븐 전선 |
  180: | 무명야·베일와일즈 | 베일런 황야 |
  181: | 외경종·비욘드본 | 베일종 |
  182: | 경계의 징조·바운더리 오멘 | 베일의 징조 |
```

### `docs/design/APPROVED_PERFORMANCE_DATA_TEST_READINESS_POC_V1.md`

Hits: `phase 0 plan mode` [411]

```text
  409: - 패배 직전 60초 결정 로그.
  410: 
  411: ## 9. Phase 0 Plan Mode 진입 조건
  412: 
  413: 현재 충족된 구조:
```

### `docs/design/APPROVED_PREPRODUCTION_POC_BASELINE_V1.md`

Hits: `phase 0 plan mode` [3, 193], `구현 전` [3, 179]

```text
    1: # 승인된 오멘워드 프리프로덕션 PoC 통합 기준 V1
    2: 
    3: - 상태: **프리프로덕션 구조 승인 완료 / 공용 10병종 데이터·진영 비주얼 분리 승인 / 전장·연출 초기값 승인 / Phase 0 Plan Mode 대기 / 구현 전**
    4: - 작성일: 2026-07-16
    5: - 최신 갱신일: 2026-07-16
  177: 이 값은 플레이테스트와 측정 근거로 같은 승인 구조 안에서 변경할 수 있다.
  178: 
  179: ## 9. 구현 전 남은 결정
  180: 
  181: - 정확한 Godot stable 버전.
  191: 
  192: ```text
  193: Issue #1 Phase 0 Plan Mode
  194: → 사용자 승인
  195: → Phase 0 구현
```

### `docs/design/APPROVED_ROULETTE_PROBABILITY_TARGETS_POC_V1.md`

Hits: `구현 전` [124]

```text
  122: ## 9. 시뮬레이션 검증
  123: 
  124: 구현 전 또는 구현 초기에 최소 100,000시드를 검증한다.
  125: 
  126: - 건물 1/2/4/6동 조합.
```

### `tests/python/test_project_core_docs.py`

Hits: `플레이 가능한 수직 슬라이스 구현 완료` [25], `existing_core_identified` [50], `core_lock_pending_user_confirmation` [51], `pending_user_confirmation` [51]

```text
   23:             readme.write_text(
   24:                 readme.read_text(encoding="utf-8")
   25:                 + "\n플레이 가능한 수직 슬라이스 구현 완료\n",
   26:                 encoding="utf-8",
   27:             )
   48:             core.write_text(
   49:                 core.read_text(encoding="utf-8")
   50:                 .replace("- 상태: `CORE_CONFIRMED`", "- 상태: `EXISTING_CORE_IDENTIFIED`")
   51:                 .replace("- 잠금 상태: `CORE_LOCKED`", "- 잠금 상태: `CORE_LOCK_PENDING_USER_CONFIRMATION`"),
   52:                 encoding="utf-8",
   53:             )
```

### `tools/validate_project_core_docs.py`

Hits: `플레이 가능한 수직 슬라이스 구현 완료` [38], `phase 0 plan mode` [39, 40, 43], `구현 전` [43, 46], `existing_core_identified` [140], `core_lock_pending_user_confirmation` [141], `pending_user_confirmation` [141, 142]

```text
   36: STALE_CURRENT_CLAIMS = {
   37:     "README.md": (
   38:         "플레이 가능한 수직 슬라이스 구현 완료",
   39:         "Issue #1 Phase 0 Plan Mode",
   40:         "정확한 경로와 파일은 Phase 0 Plan Mode 승인 후 확정합니다.",
   41:     ),
   42:     "docs/OMENWARD_GAME_DESIGN.md": (
   43:         "Phase 0 Plan Mode 대기 / 구현 전",
   44:     ),
   45:     "docs/OMENWARD_ROADMAP.md": (
   46:         "Codex Plan Mode 실행 대기 / 구현 전",
   47:         "현재는 Phase 0 구현이나 수직 슬라이스 구현을 시작하지 않는다.",
   48:     ),
  138: 
  139:     pending_core_terms = (
  140:         "EXISTING_CORE_IDENTIFIED",
  141:         "CORE_LOCK_PENDING_USER_CONFIRMATION",
  142:         "PENDING_USER_CONFIRMATION",
  143:     )
  144:     for relative in (
```

## 역사·Work Order·Proposal로 향하는 활성 마크다운 참조
- 없음
