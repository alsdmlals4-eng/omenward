# 오멘워드 미확정 결정 목록

- 갱신일: 2026-08-04
- 현재 main: `RESOLVE_FROM_REPOSITORY_DEFAULT_BRANCH`
- 현재 Decision: `OMW-DEC-20260804-PLANNING-COMBAT-SPACE-ROUTE-AND-TARGETING-EXPERIENCE-V1`
- 운영 정책: `OMW-PROC-20260804-PLANNING-VISUALS-CODEX-IMPLEMENTATION-BOUNDARY-V1`
- 현재 Grill Me: `7/10`
- 제품 코드·이미지 제작: `NOT_AUTHORIZED`

## 1. 이번 Decision으로 해결된 항목

- 세 전선 중심의 전장 구조.
- 주 경로·우회로·공중 Route의 플레이어 가시성.
- Ground·Flying·침투 병력의 체감 차이.
- 기본 같은 전선 최근접 Targeting.
- Cross-lane 공격·지원의 명시적 허용과 사전 표시.
- Target 변경 이유의 가시성.
- Concept Art와 실제 규칙의 일치 기준.
- GPT 기획·이미지와 Codex 구현 권한 분리.

## 2. 다음 최우선 사용자 Decision — 8/10

`OMW-DEC-20260804-PLANNING-BATTLEFIELD-VISUAL-HIERARCHY-AND-CAMERA-V1`

결정 필요:

- PC 16:9 기준 전장 전체 구도와 카메라 거리.
- 세 전선을 동시에 읽을 수 있는 화면 비율.
- 본진·성문·중간거점·건물 노드의 시각 우선순위.
- 주 경로·우회로·공중 Route의 선·재질·고도 표현.
- 교전 밀집 시 유닛 실루엣·체력·상태 표시 밀도.
- 위험 전선·점령 변화·후방 침투 경고 방식.
- 일반 전투와 Danger/Boss 전투의 카메라 차이.

## 3. 9/10 — 전투 HUD·룰렛·건설 UX

`OMW-DEC-20260804-PLANNING-COMBAT-HUD-REEL-AND-BUILD-UX-V1`

- 세 원형 릴과 전선 정보의 연결.
- 건설·전술 스킬 목록 진입 방식.
- 배치 확정·취소·경고·비가역성 표현.
- 현재 Target·위험·건물 효과의 정보 단계.
- 키보드·마우스 중심 PC 조작.

## 4. 10/10 — 아트·이미지 Prototype Brief

`OMW-DEC-20260804-PLANNING-ART-DIRECTION-AND-IMAGE-PROTOTYPE-BRIEF-V1`

- 전장·유닛·건물·Veil의 미술 방향.
- 색상·재질·광원·실루엣 규칙.
- 전장 전체·Route Overlay·교전 확대·HUD 결합 이미지 Brief.
- 이미지별 검수 기준과 금지 표현.
- 10/10 preflight 후 실제 이미지 제작 순서.

## 5. Codex에 위임된 구현 결정

아래는 더 이상 Grill Me에서 구현 정본으로 고정하지 않는다.

```text
coordinate unit and numeric representation
fixed/variable tick implementation
state/schema/class/resource design
pathfinding, avoidance and collision algorithms
distance and targeting search implementation
canonical sort and serialization details
performance and test architecture
```

Codex의 선택이 플레이어 경험이나 밸런스를 바꾸면 다시 기획 Gate로 돌아온다.

## 6. 후속 콘텐츠 기획

이미지·UX 방향 이후 결정할 항목:

- 표준 병종·적·건물의 역할별 Parameter Set.
- 다섯 영웅 Trigger·Timer·Effect 기획 값.
- Stage·Wave·Danger·Boss 구성.
- 첫 10~15분 사람 검증 시나리오.
- PC 완료 후 모바일 별도 타당성 검토.

## 7. 계속 금지되는 항목

```text
PRODUCT_CODE = UNCHANGED
SIMULATION_TOOL_CODE = NOT_AUTHORIZED
IMAGE_ANIMATION_HX_PRODUCTION = NOT_AUTHORIZED_UNTIL_10_OF_10_PREFLIGHT
TRUE_DAMAGE_EXECUTE_REVIVE = FORBIDDEN_CURRENT_SLICE
BALANCE_CONCLUSION = FORBIDDEN
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
```

## 8. Merge Cadence

```text
CURRENT_COUNT = 7/10
NEXT_PREFLIGHT = AT_10_OF_10
EARLY_PREFLIGHT = only high-risk conflict / session boundary / large canon impact
```
