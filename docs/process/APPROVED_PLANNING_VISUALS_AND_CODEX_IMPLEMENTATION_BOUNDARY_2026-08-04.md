# OMENWARD Planning·Visuals / Codex Implementation Boundary

```yaml
policy_id: OMW-PROC-20260804-PLANNING-VISUALS-CODEX-IMPLEMENTATION-BOUNDARY-V1
updated_at: 2026-08-04
status: ACTIVE_STANDING_POLICY / NON_COUNTER
scope: OMENWARD planning workflow
product_code_authority: NONE
```

## 1. 목적

OMENWARD의 현재 작업은 **기획과 이미지·UX 방향을 먼저 완성**하고, 실제 구현 방식은 Codex가 프로젝트 구조와 테스트를 확인한 뒤 결정한다.

```text
GPT / Work
= 플레이어 경험·게임 규칙·콘텐츠·UX·아트 방향·이미지 Brief·검수 기준

Codex
= 자료구조·알고리즘·좌표 표현·경로탐색·물리·성능·코드 구조·테스트 구현
```

## 2. GPT가 정본으로 소유하는 것

- 무엇이 재미의 중심인지.
- 플레이어가 무엇을 보고 어떤 판단을 하는지.
- 전선·룰렛·건물·유닛·영웅의 역할과 상호작용.
- 플레이어에게 보이는 규칙과 예외.
- 밸런스 목표·수치의 기획 기본값.
- HUD·카메라·전장 가독성·피드백 원칙.
- 이미지·애니메이션·아트 방향과 제작 Brief.
- 사람 검증에서 확인할 성공·실패 기준.

## 3. Codex가 소유하는 것

- 좌표 단위·정수/실수 표현·고정 Tick 여부와 주기.
- 데이터 Schema·클래스·Resource·Scene·노드 구성.
- 거리식·충돌·경로탐색·회피·Target 탐색 알고리즘.
- 처리 phase 이름·내부 순서·정렬 키·직렬화 방식.
- 성능 최적화·메모리·캐시·병렬화·Headless 구조.
- 테스트 파일 구성·Fixture 형식·구체적인 구현 전략.

Codex는 기획 결과를 바꾸지 않는 범위에서 최적 구현을 선택한다.

## 4. 다시 기획 승인이 필요한 경우

Codex의 구현 선택이 아래 중 하나를 바꾸면 작업을 멈추고 Grill Me로 되돌린다.

- 플레이어가 인지하는 이동·사거리·Target 우선순위.
- 유닛·영웅·건물의 역할 또는 카운터 관계.
- 전장·HUD·이미지에서 보이는 정보 우선순위.
- 난이도·전투 템포·밸런스 곡선.
- 세 전선·세 릴·비가역 배치라는 프로젝트 코어.

## 5. 기존 Decision 1~6 재분류

기존 문서의 플레이어 경험·밸런스 의도는 계속 기획 정본이다. 아래 구현 세부는 앞으로 **Codex 참고안 / 비구속 구현 제안**으로 취급한다.

```text
exact state/schema names
R00~R130 phase naming
30 TPS and ms-to-tick representation
integer arithmetic and basis-point storage
canonical sorting keys
snapshot storage method
headless harness architecture
```

다만 다음 결과 요구는 유지한다.

```text
same input produces explainable stable results
no hidden first-strike or callback advantage
combat outcomes preserve deployment provenance
damage/protection/status behavior is readable
stacking cannot create opaque exponential growth
```

## 6. 앞으로의 Grill Me 방향

```text
7/10  전투 공간·이동·Targeting의 플레이 경험
8/10  전장 시각 계층·카메라·정보 밀도
9/10  전투 HUD·룰렛·건설·전술 UX
10/10 아트 방향·이미지 Prototype Brief
→ preflight·적대적 검토
→ 승인 이미지 제작
→ Codex 구현 계약
```

## 7. 금지선

- GPT가 구현 편의를 이유로 플레이어 경험을 임의 변경하지 않는다.
- Codex가 기술 편의를 이유로 기획 정본을 임의 변경하지 않는다.
- 기술 수치를 기획 정본처럼 강제하지 않는다.
- 이미지가 실제 게임 규칙과 다른 전장을 보여주지 않는다.
- 사용자 승인 전 제품 코드·이미지·애니메이션·HX를 제작하지 않는다.
