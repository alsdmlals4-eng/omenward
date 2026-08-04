# 오멘워드 미확정 결정 목록

- 갱신일: 2026-08-04
- 현재 main: `RESOLVE_FROM_REPOSITORY_DEFAULT_BRANCH`
- 전체 시스템 정본: `docs/design/APPROVED_VERTICAL_SLICE_SYSTEM_CONTRACT_2026-07-27.md`
- 현재 Decision: `OMW-DEC-20260804-PLANNING-PIXEL-ILLUSTRATION-HYBRID-ART-DIRECTION-V1`
- 운영 정책: `OMW-PROC-20260804-PLANNING-VISUALS-CODEX-IMPLEMENTATION-BOUNDARY-V1`
- 현재 Grill Me: `10/10`
- 제품 코드: `NOT_AUTHORIZED`
- 실제 아트 자산 제작: `NOT_AUTHORIZED`
- 이미지 생성: `STOPPED_BY_USER`

## 1. 이번 Decision으로 해결된 항목

- 최종 스타일을 `픽셀+일러스트 하이브리드`로 확정.
- 전장에서는 픽셀풍 실루엣과 원거리 가독성, 근접 UI에서는 일러스트풍 재질과 표정을 강화.
- 전체 감성을 `멋지고 따뜻한 동화풍 성전 판타지`로 확정.
- 아군 상아·청색·절제된 금색, Veil 흑색·심자색·적자색 대비.
- Veil을 아군 자산의 재도색이 아닌 비대칭·가시·유기 고딕 형태로 확정.
- T1→T2→T3 성장 시 장비·자세·실루엣·역할 판타지를 강화.
- 영웅·전설은 기본 병종 계보를 유지하며 개인 문장·고유 장비·VFX로 차별화.
- 금고·농장·병영·방어탑·지휘소·마력탑의 역할별 실루엣 기준 확정.
- 벨루를 일러스트 우선 SD 컷아웃으로 유지.
- 룰렛 토큰용 별도 금화·병종 아이콘 제작 금지.
- 인게임 금화 이미지와 T1·T2 병종 이미지를 룰렛에 재사용.
- T3 병종 이미지는 룰렛 병종 토큰에 사용하지 않음.
- 결과 보상은 실제 지급 병종의 인게임 이미지 사용.
- 생성된 비교 이미지를 선택 근거·레이아웃 참고용 비정본으로 분류.

## 2. 즉시 다음 작업 — 10/10 Preflight

```text
1. GitHub 중앙 정본·Decision 원장·Sheet same-ID 동기화
2. exact PR HEAD CI 3종 확인
3. main 대비 ahead/behind·changed paths 확인
4. 리뷰·미해결 thread 확인
5. OPEN_P0 / OPEN_P1 / MERGE_BLOCKER 검색
6. TODO / TBD / 모순 / 범위 이탈 검사
7. 제품 코드·실제 자산 변경 0 확인
8. Green·blocker 0일 때 merge readiness 판정
```

## 3. Preflight 이후 GPT 핵심 재미·콘텐츠 기획

우선순위:

- 세 릴을 반복 설계하게 만드는 선택 압력과 보상.
- Stage마다 달라지는 상·중·하 전선 공세 패턴.
- Wave·Danger·Boss가 릴·건물·배치 선택을 어떻게 시험하는지.
- 기본 건물 6종의 T2·T3 분기와 카운터 관계.
- 전술스킬 목록과 마석 획득·소비의 선택 압력.
- Stage 종료 상인의 재고·가격·이벤트 변주.
- T1·T2·T3 병종 역할·시너지·카운터.
- 영웅·전설의 콘텐츠 역할과 획득 경험.
- 첫 10~15분 플레이 검증 시나리오.

## 4. 후속 콘텐츠 Decision

- 마석 기본 축적량·최대치·마력탑 강화 폭.
- 전술스킬 목록·마석 비용·사용 시점·표현.
- 상인 이동권 재고·가격·추가 상품군.
- 농장·병력 한도의 정확한 성장 구조.
- 지휘소 돌격·수비 오라의 효과와 밸런스.
- 마력탑 T2·T3 수급형·저장형 분기.
- 건물 6종의 T2·T3 외형·효과 분기.
- 병종·영웅·전설의 실제 이름·역할·콘텐츠 배치.
- 벨루 대사 우선순위·중복 억제·접근성.

## 5. 실제 아트 제작 전 결정

- 원본 캔버스·프레임·방향 수·애니메이션 수 같은 제작 규격.
- 전장용 정리 스프라이트와 보상·도감용 확대 이미지의 파생 방식.
- T1·T2 인게임 병종 자산의 토큰 크롭 안전 영역.
- T3·영웅·전설 VFX 밀도와 화면 점유 제한.
- 아군·Veil 건물의 제작 목록과 변형 우선순위.
- 벨루 표정·대사 컷아웃 최소 세트.

이는 아트 방향 정본이 아니라 제작 계획 단계에서 확정한다. 사용자 별도 지시 전 제작을 시작하지 않는다.

## 6. Codex에 위임된 구현 결정

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

## 7. 계속 금지되는 항목

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

## 8. Merge Cadence

```text
CURRENT_COUNT = 10/10
NEXT_PREFLIGHT = NOW
MERGE = ONLY_AFTER_FRESH_GREEN_AND_ZERO_BLOCKERS
NEXT_COUNTER_AFTER_MERGE = 0/10
```
