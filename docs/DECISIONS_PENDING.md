# [현행] 오멘워드 미확정 결정 목록

```yaml
updated_at: 2026-08-04
current_main: RESOLVE_FROM_REPOSITORY_DEFAULT_BRANCH
current_decision: OMW-DEC-20260804-PLANNING-CORE-FUN-AND-CONTENT-GUARDRAILS-V1
current_process_policy: OMW-PROC-20260804-DYNAMIC-CURRENT-MAIN-AND-DOCUMENT-LIFECYCLE-V1
current_grill_me_count: 1_OF_10
product_code_authority: NONE
art_asset_production_authority: NONE
image_generation: STOPPED_BY_USER
```

## 1. 이번 Decision으로 해결된 항목

- 핵심 재미를 `예고된 압력 → 제작한 확률 → 비가역 전선 커밋 → 설명 가능한 결과`로 재정의.
- 세 원형 릴과 3×3 노출창의 관계 명시.
- 현행 자원을 골드·마석·배치 병력/한도·이동권으로 통일.
- 기본 건물 6종과 MapRun 전체 지휘소 오라 재확인.
- Stage 콘텐츠 압력을 MASS/ARMORED/FLYING/INFILTRATION/SIEGE로 분류.
- README·AGENTS·PROJECT_CORE·GDD·Roadmap의 구형 계약 제거.
- 구형 master GDD를 `[대체됨]`으로 봉인.
- Hero·Meta·첫 10분 구형 상세 문서를 `[보류]`로 격리.
- 채택되지 않은 자원·건물·아이콘 가정을 `[폐기]`로 분류.
- `current_main` 고정 SHA 재귀를 동적 해석 정책으로 수정.

## 2. 다음 Decision — Stage 압력 매트릭스

`OMW-DEC-20260804-PLANNING-STAGE-WAVE-DANGER-BOSS-PRESSURE-MATRIX-V1`

다룰 내용:

- 20 Stage 또는 현행 MapRun 구조에서 압력 학습 순서.
- 일반 Stage의 1~2개 명확한 압력.
- Danger Stage의 규칙 변형.
- Boss Stage의 선택 구조 변화.
- 공세 예고 카드의 공개 정보.
- 건물·병종·전술 대응 축.
- 실패 원인 복기 문구.

다루지 않을 내용:

- exact HP·Damage·Spawn 수치.
- 좌표·Tick·Pathfinding 구현.
- 제품 코드.

## 3. 후속 Planning Batch

```text
2/10 Stage·Wave·Danger·Boss 압력 매트릭스
3/10 건물 6종 T2/T3 분기·카운터
4/10 T1/T2/T3 병종 역할·시너지·카운터
5/10 전술스킬·마석 획득/소비
6/10 Stage 종료 상인 재고·가격·이벤트
7/10 최신 첫 10~15분 흐름·벨루
8/10 Hero·Legendary family 재조정
9/10 Meta·Hub 재조정
10/10 통합 플레이 시나리오·구현 handoff readiness
```

## 4. [보류] 항목

다음은 유효 가능성이 있지만 최신 코어와 재검증 전 사용하지 않는다.

- 구형 첫 10분 타임라인.
- Hero·Legendary 획득·배치·자동 스킬·고유 스킬 문서군.
- Meta Profile·ReadinessPerk·주점·허브 병영·연구.
- 과거 V2 구현 계획.

상세 파일 목록은 `DOCUMENT_LIFECYCLE_REGISTRY.md`가 소유한다.

## 5. [폐기] 항목

- 식량을 현행 핵심 HUD 자원으로 사용.
- 기본 건물 5종.
- 지휘소 주변 범위 오라.
- 룰렛 전용 금화·병종 상징 아이콘.
- T3 병종 룰렛 토큰.
- 채택되지 않은 초기 세계관 명명안.

## 6. 실제 아트 제작 전 결정

- 원본 캔버스·프레임·방향 수·애니메이션 수.
- 전장 정리 스프라이트와 확대 일러스트의 파생 방식.
- T1·T2 토큰 크롭 안전 영역.
- T3·영웅·전설 VFX 화면 점유 제한.
- 벨루 표정·컷아웃 최소 세트.

사용자 별도 지시 전 실제 제작하지 않는다.

## 7. Codex 구현 결정

```text
coordinate unit and numeric representation
fixed/variable tick implementation
state/schema/class/resource design
pathfinding, avoidance and collision algorithms
targeting search and distance implementation
camera transform, FOV, occlusion and smoothing
sprite rendering and animation architecture
HUD scene and responsive layout
serialization, performance and test architecture
```

플레이어 경험·콘텐츠 역할을 바꾸는 선택은 기획 Gate로 되돌린다.

## 8. 계속 금지되는 항목

```text
PRODUCT_CODE = UNCHANGED
SIMULATION_TOOL_CODE = NOT_AUTHORIZED
ART_ASSET_PRODUCTION = NOT_AUTHORIZED
IMAGE_GENERATION = STOPPED_BY_USER
BALANCE_CONCLUSION = FORBIDDEN
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
```

## 9. Merge Cadence

```text
CURRENT_COUNT = 1/10
NEXT_PREFLIGHT = AFTER_10_APPROVED_DECISIONS_OR_HIGH_RISK_CANON_CHANGE
CURRENT_PR = FRESH_PREFLIGHT_REQUIRED_BECAUSE_P0_CANON_CONFLICT_FIXED
```
