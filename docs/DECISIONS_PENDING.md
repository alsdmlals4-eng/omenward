# 오멘워드 미확정 결정 목록

- 갱신일: 2026-08-04
- 현재 main: `d8ce26ee3ee21dbab50839b7a1334116e147789e`
- 전체 시스템 정본: `docs/design/APPROVED_VERTICAL_SLICE_SYSTEM_CONTRACT_2026-07-27.md`
- 최신 Decision: `OMW-DEC-20260804-PLANNING-PIXEL-ILLUSTRATION-HYBRID-ART-DIRECTION-V1`
- 현재 Sync: `OMW-SYNC-20260804-POST-MERGE-PIXEL-ILLUSTRATION-HYBRID-CANON-V1`
- 운영 정책: `OMW-PROC-20260804-PLANNING-VISUALS-CODEX-IMPLEMENTATION-BOUNDARY-V1`
- 현재 Grill Me: `0/10`
- 제품 코드: `NOT_AUTHORIZED`
- 실제 아트 자산 제작: `NOT_AUTHORIZED`
- 이미지 생성: `STOPPED_BY_USER`

## 1. 해결된 최근 Gate

- PR #133의 10/10 기획 묶음이 main에 squash merge됐다.
- 픽셀·일러스트 하이브리드가 최종 아트 방향으로 확정됐다.
- 전장은 픽셀풍 가독성, 근접 UI는 일러스트풍 재질·표정을 우선한다.
- 금화 토큰은 인게임 금화, 병종 토큰은 인게임 T1·T2 병종 이미지를 재사용한다.
- T3 병종 이미지는 룰렛 병종 토큰에 사용하지 않는다.
- 결과 보상은 실제 지급 병종 이미지를 사용한다.
- 별도 금화·병종 토큰 아이콘을 제작하지 않는다.
- 제품 코드·실제 자산·추가 이미지는 변경하거나 제작하지 않았다.

## 2. 다음 GPT 핵심 재미·콘텐츠 기획

우선순위:

```text
P0 = Stage·Wave·Danger·Boss가 릴·건물·배치 결정을 시험하는 콘텐츠 압력
P1 = 세 릴을 반복 설계하게 만드는 선택 압력·보상·실패 복기
P2 = 기본 건물 6종의 T2·T3 분기·카운터·시너지
P3 = 전술스킬 목록과 마석 획득·소비·사용 시점
P4 = Stage 종료 상인의 재고·가격·이벤트 변주
P5 = T1·T2·T3 병종 역할·시너지·카운터
P6 = 영웅·전설의 콘텐츠 역할·획득 경험
P7 = 첫 10~15분 플레이 검증 시나리오
```

첫 후속 Decision은 구현 수치가 아니라 **Stage·Wave·Danger·Boss 콘텐츠 압력 구조**를 다루는 것을 권장한다.

## 3. 후속 콘텐츠 Decision

- 마석 기본 축적·최대치·마력탑 강화 방향.
- 전술스킬 목록·마석 비용·사용 시점·표현.
- 상인 이동권 재고·가격·추가 상품군.
- 농장·병력 한도의 성장 구조.
- 지휘소 돌격·수비 오라의 역할과 밸런스.
- 마력탑 T2·T3 수급형·저장형 분기.
- 건물 6종의 T2·T3 외형·효과 분기.
- 병종·영웅·전설의 실제 이름·역할·콘텐츠 배치.
- 벨루 대사 우선순위·중복 억제·접근성.

## 4. 실제 아트 제작 전 결정

- 원본 캔버스·프레임·방향 수·애니메이션 수 같은 제작 규격.
- 전장용 정리 스프라이트와 보상·도감용 확대 이미지의 파생 방식.
- T1·T2 병종 자산의 토큰 크롭 안전 영역.
- T3·영웅·전설 VFX 밀도와 화면 점유 제한.
- 아군·Veil 건물 제작 목록과 변형 우선순위.
- 벨루 표정·대사 컷아웃 최소 세트.

이는 제작 계획 단계에서 확정하며 사용자 별도 지시 전 제작하지 않는다.

## 5. Codex에 위임된 구현 결정

```text
coordinate unit and numeric representation
fixed/variable tick implementation
state/schema/class/resource design
pathfinding, avoidance and collision algorithms
distance and targeting search implementation
camera transform, FOV, occlusion and smoothing
sprite rendering and animation architecture
HUD scene and responsive layout implementation
input binding and transition implementation
canonical sort and serialization details
performance and test architecture
```

Codex 선택이 핵심 재미·콘텐츠 역할·시각 계층·플레이어 경험을 바꾸면 다시 기획 Gate로 돌아온다.

## 6. 계속 금지되는 항목

```text
PRODUCT_CODE = UNCHANGED
SIMULATION_TOOL_CODE = NOT_AUTHORIZED
ART_ASSET_PRODUCTION = NOT_AUTHORIZED
IMAGE_GENERATION = STOPPED_BY_USER
TRUE_DAMAGE_EXECUTE_REVIVE = FORBIDDEN_CURRENT_SLICE
BALANCE_CONCLUSION = FORBIDDEN
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
```

## 7. Merge Cadence

```text
LAST_MERGED_PLANNING_PR = 133
LAST_MERGED_PLANNING_COMMIT = d8ce26ee3ee21dbab50839b7a1334116e147789e
CURRENT_COUNT = 0/10
NEXT_PREFLIGHT = AFTER_10_NEW_APPROVED_DECISIONS
```
