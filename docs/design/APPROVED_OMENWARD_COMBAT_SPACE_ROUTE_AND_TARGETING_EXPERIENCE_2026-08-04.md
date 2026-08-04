# OMENWARD Combat Space·Route·Targeting Experience

```yaml
decision_id: OMW-DEC-20260804-PLANNING-COMBAT-SPACE-ROUTE-AND-TARGETING-EXPERIENCE-V1
updated_at: 2026-08-04
status: USER_APPROVED / ACTIVE_PLANNING_BRANCH / NOT_IMPLEMENTED
grill_me_count: 7_OF_10
work_mode: TOTAL_PLANNING
process_boundary: OMW-PROC-20260804-PLANNING-VISUALS-CODEX-IMPLEMENTATION-BOUNDARY-V1
product_code_authority: NONE
image_production_authority: NONE
```

## 1. 결정

OMENWARD 전투 공간은 **세 전선의 압박과 우회 선택을 한눈에 읽을 수 있는 명시적 Route 전장**으로 확정한다.

이 Decision은 플레이어가 체감하는 전선·이동·Targeting 규칙과 이미지 요구만 소유한다. 좌표 단위·거리 계산식·경로탐색·충돌 알고리즘은 Codex가 구현 단계에서 결정한다.

## 2. 플레이어 약속

```text
어디서 싸우는가
누구를 노리는가
왜 Target이 바뀌었는가
어떤 길로 후방을 노리는가
```

플레이어는 전투를 멈추고 로그를 읽지 않아도 위 네 가지를 화면에서 이해할 수 있어야 한다.

## 3. 전장 구조

- 전장은 상단·중단·하단의 세 전선을 중심으로 구성한다.
- 각 전선은 본진에서 적 본진까지 이어지는 주 이동 경로를 가진다.
- 우회·침투·공중 이동은 주 경로와 구분되는 **눈에 보이는 별도 Route**로 표현한다.
- Route 입구와 출구는 배치 전에 확인 가능해야 한다.
- 전선 변경은 명시적 능력·전술 명령·Route 분기에서만 발생한다.
- 보이지 않는 자동 길찾기가 플레이어의 배치 의도를 다른 전선으로 바꾸면 안 된다.

## 4. Ground·Flying·Infiltration 경험

### Ground

- Ground 병력은 해당 전선의 전열과 후열을 형성한다.
- 앞의 아군과 적을 무시하고 시각적으로 겹쳐 통과하지 않는다.
- 다수 병력이 모이면 전선이 밀리고 있다는 감각이 보여야 한다.
- 혼잡 때문에 이동이 늦어지는 경우 전열 정체로 이해 가능해야 한다.

### Flying

- Flying은 Ground 전열의 물리적 혼잡을 넘을 수 있다.
- Flying도 특정 전선 또는 공중 Route에 속하며 화면 밖에서 임의로 이동하지 않는다.
- Ground 차단을 무시한다고 해서 모든 Target·사거리·방어 규칙을 무시하지 않는다.
- 대공 가능 여부는 유닛·건물·스킬의 명확한 역할로 표현한다.

### Infiltration·Bypass

- 암살자·침투 병력은 순간이동처럼 후열에 나타나지 않는다.
- 우회로 진입, 이동, 출구 도달, 후열 접촉이 시각적으로 연결돼야 한다.
- 우회 성공은 강력하지만 입구·이동 중간·출구에서 대응할 기회가 존재해야 한다.

## 5. 기본 Targeting 규칙

기본 공격의 플레이어 체감 규칙:

```text
같은 전선의 공격 가능한 대상
→ 현재 교전선에서 가장 가까운 유효 대상
→ 대상이 사라지거나 공격 불가능해지면 다음 대상 선택
```

- 기본 공격은 같은 전선 또는 같은 Route의 가장 가까운 유효 대상을 우선한다.
- Cross-lane 공격·지원·Aura는 능력이나 건물이 명시적으로 허용할 때만 가능하다.
- Cross-lane 효과는 연결된 전선·범위·대상 유형을 사전에 보여준다.
- 건물·Objective 우선 공격은 병종 또는 스킬 정체성으로 명시한다.
- Target 변경은 사망·사거리 이탈·은신·도발·강제 이동·Route 변경처럼 설명 가능한 이유가 있어야 한다.
- 낮은 내부 ID나 처리 순서 때문에 플레이어가 예측하지 못한 Target이 선택되면 실패다.

## 6. 전투 가독성

전략 카메라에서 동시에 보여야 하는 정보:

- 세 전선별 아군·적군 압박 방향.
- 현재 주요 교전 위치.
- 우회 Route의 입구·이동 방향·출구.
- Flying과 Ground의 이동 층 차이.
- 건물·중간거점·Objective의 소유 상태.
- 선택한 유닛이나 능력의 Target 가능 범위.

항상 표시하지 않아도 되는 정보:

- 모든 유닛의 Target 선.
- 모든 Aura와 사거리 원.
- 내부 이동 노드·좌표·경로탐색 데이터.

정보는 선택·Hover·위험 발생 시 단계적으로 드러내며 전장을 선과 원으로 뒤덮지 않는다.

## 7. 이미지 제작 요구

후속 이미지 Prototype은 최소 다음 4종을 준비한다.

1. **전장 전체 구도 이미지** — 세 전선·본진·중간거점·주요 건물 위치.
2. **Route Overlay** — 주 경로·우회로·공중 경로의 차이.
3. **교전 가독성 확대 이미지** — 전열·후열·Flying·Target 방향.
4. **Cross-lane 효과 이미지** — 어느 전선까지 지원하거나 공격하는지 명확한 표현.

이미지는 실제 기획 규칙을 설명해야 하며 분위기만 좋은 Concept Art로 끝나면 안 된다.

## 8. Codex 구현 위임

Codex가 결정할 항목:

```text
coordinate representation
movement integration
pathfinding and avoidance
collision and spacing algorithm
distance and range calculation
target-search data structure
tie-break implementation
performance optimization
```

Codex 구현안이 이 문서의 플레이어 체감 규칙을 변경하면 다시 사용자 승인을 받는다.

## 9. 적대적 검토

| Audit ID | 위험 | 기획 완화 |
|---|---|---|
| OMW-AUD-290 | GPT가 구현 세부까지 정본화 | Planning/Visuals와 Codex 권한 분리 |
| OMW-AUD-291 | 자동 길찾기가 배치 전선을 변경 | 전선 변경은 명시적 분기·능력만 허용 |
| OMW-AUD-292 | 우회 병력이 순간이동처럼 출현 | 입구·이동·출구 전 과정 표시 |
| OMW-AUD-293 | Flying이 모든 규칙을 무시 | Ground 혼잡만 우회, Target 규칙 유지 |
| OMW-AUD-294 | Cross-lane 공격이 화면 밖에서 발생 | 연결 전선·범위·대상을 사전 표시 |
| OMW-AUD-295 | 병력 겹침으로 전열이 읽히지 않음 | Ground 전열·후열·혼잡 표현 필요 |
| OMW-AUD-296 | Target 변경 이유를 알 수 없음 | 변경 reason을 전투 피드백과 로그에 연결 |
| OMW-AUD-297 | 사거리·Target 선이 화면을 덮음 | 선택·Hover·위험 시 단계적 표시 |
| OMW-AUD-298 | Concept Art와 실제 규칙 불일치 | 이미지마다 기획 규칙 Callout 포함 |
| OMW-AUD-299 | 모바일을 위해 PC 전장을 축소 | PC 16:9 우선, 모바일은 별도 타당성 Gate |

## 10. 검수 기준

- 화면 정지 이미지에서 세 전선을 구분할 수 있다.
- 우회로 입구와 출구를 별도 설명 없이 찾을 수 있다.
- Ground·Flying·침투 병력의 이동 방식이 실루엣과 Route로 구분된다.
- 기본 공격이 어느 대상을 향하는지 이해할 수 있다.
- Cross-lane 효과가 영향을 주는 전선을 예측할 수 있다.
- 이미지와 GDD의 전장 규칙이 서로 충돌하지 않는다.

## 11. 다음 Visual Gate

```text
8/10 = OMW-DEC-20260804-PLANNING-BATTLEFIELD-VISUAL-HIERARCHY-AND-CAMERA-V1
9/10 = OMW-DEC-20260804-PLANNING-COMBAT-HUD-REEL-AND-BUILD-UX-V1
10/10 = OMW-DEC-20260804-PLANNING-ART-DIRECTION-AND-IMAGE-PROTOTYPE-BRIEF-V1
```

10/10 preflight와 사용자 승인 후 실제 이미지 제작을 시작한다.
