# 오멘워드 미확정 결정 목록

- 갱신일: 2026-08-04
- 현재 main: `RESOLVE_FROM_REPOSITORY_DEFAULT_BRANCH`
- 전체 시스템 정본: `docs/design/APPROVED_VERTICAL_SLICE_SYSTEM_CONTRACT_2026-07-27.md`
- 현재 Decision: `OMW-DEC-20260804-PLANNING-BATTLEFIELD-VISUAL-HIERARCHY-AND-CAMERA-V1`
- 운영 정책: `OMW-PROC-20260804-PLANNING-VISUALS-CODEX-IMPLEMENTATION-BOUNDARY-V1`
- 현재 Grill Me: `8/10`
- 제품 코드·이미지 제작: `NOT_AUTHORIZED`

## 1. 이번 Decision으로 해결된 항목

- PC 16:9 고각도 3/4 전략 카메라 방향.
- 기본 화면에서 상·중·하 세 전선을 동시에 읽는 원칙.
- 전선 흐름→우회 위협→거점 상태→핵심 병종→세부 수치의 정보 우선순위.
- 전투 공간 약 70~75%, 하단 HUD 약 25~30%의 기획 구성 목표.
- 강제 카메라 이동 최소화와 선택형 확대·이동.
- 주 경로·우회로·공중 Route의 시각 언어 차이.
- 체력·Status·Target 선의 단계적 공개.
- Danger·Boss가 다른 전선 정보를 가리지 않는 연출 원칙.
- GPT의 핵심 재미→콘텐츠→UX·이미지·아트 우선순위.

## 2. 다음 최우선 사용자 Decision — 9/10

`OMW-DEC-20260804-PLANNING-COMBAT-HUD-REEL-AND-BUILD-UX-V1`

결정 필요:

- 하단 HUD에서 세 원형 릴과 상·중·하 전선의 연결 방식.
- 건설·전술 스킬 버튼과 목록의 배치.
- 룰렛 Spin·재굴림·슬롯 이동·배치 확정의 조작 흐름.
- 비가역 전선 배치의 경고·확정·취소 표현.
- 현재 전선 위험·Target·건물 효과의 정보 단계.
- 키보드·마우스 중심 PC 조작과 접근성.
- 전투 화면 70~75%를 침범하지 않는 HUD 밀도.

## 3. 10/10 — 아트·이미지 Prototype Brief

`OMW-DEC-20260804-PLANNING-ART-DIRECTION-AND-IMAGE-PROTOTYPE-BRIEF-V1`

- 전장·유닛·건물·Veil의 미술 방향.
- 색상·재질·광원·실루엣 규칙.
- 전장 전체·Route Overlay·교전 확대·HUD 결합 이미지 Brief.
- 기본 전략·위험 전선·교전 확대·Danger/Boss 이미지 구성.
- 이미지별 검수 기준과 금지 표현.
- 10/10 preflight 후 실제 이미지 제작 순서.

## 4. 10/10 이후 핵심 재미·콘텐츠 기획

이미지 방향 이후 GPT가 우선 논의할 항목:

- 세 릴을 반복 설계하게 만드는 선택 압력과 보상.
- Stage마다 달라지는 세 전선 공세 패턴.
- Wave·Danger·Boss가 릴·건물·배치 선택을 어떻게 시험하는지.
- 표준 병종·영웅·건물의 역할과 카운터 관계.
- 성장·해금·수집이 핵심 재미를 어떻게 확장하는지.
- 첫 10~15분 사람 검증 시나리오.

## 5. Codex에 위임된 구현 결정

아래는 Grill Me에서 구현 정본으로 고정하지 않는다.

```text
coordinate unit and numeric representation
fixed/variable tick implementation
state/schema/class/resource design
pathfinding, avoidance and collision algorithms
distance and targeting search implementation
camera transform, FOV, occlusion and smoothing
canonical sort and serialization details
performance and test architecture
```

Codex의 선택이 핵심 재미·콘텐츠 역할·플레이어 경험이나 밸런스를 바꾸면 다시 기획 Gate로 돌아온다.

## 6. 계속 금지되는 항목

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

## 7. Merge Cadence

```text
CURRENT_COUNT = 8/10
NEXT_PREFLIGHT = AT_10_OF_10
EARLY_PREFLIGHT = only high-risk conflict / session boundary / large canon impact
```
