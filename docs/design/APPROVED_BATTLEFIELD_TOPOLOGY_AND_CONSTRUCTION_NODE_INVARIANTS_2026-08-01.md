# 오멘워드 전장 토폴로지·건설 노드 불변 계약

- 결정 ID: `OMW-DEC-20260801-PROJECT-INTEGRITY-GATE-V1`
- 승인 근거: 2026-08-01 사용자 직접 정정
- 상태: `CURRENT_USER_CONFIRMED_CANON / PLANNING_ONLY`
- 제품 구현 권한: `NONE`
- 사람·Runtime 검증: `NOT_RUN`

이 문서는 전장 구조와 건설 노드 수량을 요약 숫자만으로 해석하다 생기는 누락을 방지한다. 다른 문서·이미지·와이어프레임·코드가 이 계약과 충돌하면 최신 사용자 지시와 이 문서를 우선한다.

---

## 1. 노드 종류

오멘워드의 물리 노드 종류는 하나다.

```text
CONSTRUCTION_NODE / 건설 노드
```

다음과 같은 별도 노드 종류를 임의로 만들지 않는다.

- 본진 노드
- 방어 노드
- 전진 노드
- 특수 노드
- 접전지 노드

`본진`과 `중간 거점`은 노드 종류가 아니라 건설 노드가 속한 전장 위치다. 건물의 실제 건설 가능 여부는 소유권·안정 상태·점유 상태·건물 계약으로 판정하며, 노드 종류를 추가해 설명하지 않는다.

---

## 2. 전장 전체 구조

전장은 하나이며 상·중·하 세 라인을 가진다.

각 라인의 순서는 다음과 같다.

```text
아군 본진
→ 아군 중간 거점
→ 중앙 접전지
→ 적 중간 거점
→ 적 본진
```

- 아군과 적은 대칭 토폴로지를 사용한다.
- 중앙 접전지는 교전·점령 목적지이며 건설 장소가 아니다.
- 일반 병력은 라인 사이를 자유롭게 이동하지 않는다.

---

## 3. 건설 노드 수량

| 위치 | 장소 수 | 장소당 건설 노드 | 합계 |
|---|---:|---:|---:|
| 아군 본진 | 1 | 6 | 6 |
| 적 본진 | 1 | 6 | 6 |
| 아군 중간 거점 | 3 | 3 | 9 |
| 적 중간 거점 | 3 | 3 | 9 |
| 중앙 접전지 | 3 | 0 | 0 |
| **전체** |  |  | **30** |

검산식:

```text
본진: 2진영 × 6 = 12
중간 거점: 3라인 × 2진영 × 3 = 18
중앙 접전지: 3 × 0 = 0
전체: 12 + 18 = 30
```

`중간 거점 전체 6곳`은 서로 다른 여섯 종류가 아니라 `3라인 × 2진영`의 대칭 구조다.

---

## 4. 화면·이미지 표현 불변 조건

전장·UI·이미지 브리프는 다음을 모두 만족해야 한다.

1. 하나의 전장 안에서 상·중·하 세 라인이 동시에 읽힌다.
2. 양 진영 본진에는 각각 건설 노드 6개가 있다.
3. 각 라인의 양측 중간 거점에는 각각 건설 노드 3개가 있다.
4. 중앙 접전지에는 건설 노드를 그리지 않는다.
5. 노드를 방어·전진·특수 등 별도 유형으로 색분류하지 않는다.
6. 건물·룰렛·전선의 연결을 표현할 때 노드 하나가 릴 하나에 대응하는 것처럼 그리지 않는다.
7. TokenSource 건물은 위치와 관계없이 플레이어의 세 릴에 계약된 토큰을 공급한다.

위 항목 중 하나라도 불명확하면 이미지·화면 보드 제작을 중단하고 사실표를 다시 확인한다.

---

## 5. 구현·데이터·테스트 불변 조건

향후 최신 Vertical Slice 구현에는 최소 다음 자동 계약이 필요하다.

```text
construction_node_kind_count == 1
base_count == 2
construction_nodes_per_base == 6
lane_count == 3
midpoint_outposts_per_lane == 2
construction_nodes_per_midpoint_outpost == 3
clash_zones_per_lane == 1
construction_nodes_per_clash_zone == 0
total_construction_nodes == 30
```

Legacy 코드의 `front_a / front_b / rear` 세 노드 등록과 `construct_home()`의 중단 아군 거점 별칭은 최신 전장 토폴로지 구현 증거가 아니다. 최신 구현에서는 본진 노드와 여섯 중간 거점 노드를 명시적으로 데이터화해야 한다.

---

## 6. 금지 해석

- 중앙 접전지를 중간 거점과 동일한 건설 가능 구조물로 취급하지 않는다.
- 전체 30개를 플레이어가 항상 동시에 사용할 수 있는 노드 수로 해석하지 않는다.
- 본진 6개를 라인별 6개로 복제하지 않는다.
- 중간 거점 6곳을 한 진영만의 6곳으로 해석하지 않는다.
- 시각자료 안의 임시 노드 배치를 제품 토폴로지로 복사하지 않는다.

---

## 7. 현재 상태

```text
TOPOLOGY_CANON: USER_CONFIRMED
NODE_KIND: CONSTRUCTION_NODE_ONLY
BASE_NODES: 6_PER_FACTION
MIDPOINT_NODES: 3_PER_OUTPOST
MIDPOINT_OUTPOSTS: 3_LANES_X_2_FACTIONS
CLASH_NODE_COUNT: ZERO
TOTAL_CONSTRUCTION_NODES: 30
LATEST_PRODUCT_IMPLEMENTATION: NOT_STARTED
LEGACY_IMPLEMENTATION: MIGRATION_REQUIRED
```