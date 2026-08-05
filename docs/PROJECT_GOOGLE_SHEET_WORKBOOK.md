# [현행] OMENWARD Google Sheet 정본 동기화 계약

```yaml
updated_at: 2026-08-05
spreadsheet_id: 1VLwRtXGDtyj0JFt98wdIOtG6Zqc3wtdfCzSF9Fo6lpw
status: PROJECT_SHEET_CONFIGURED / USER_FACING_GDD_WORKSPACE / PROPOSED_SHEET_CHANGE
current_decision: OMW-DEC-20260805-PLANNING-STAGE-END-MERCHANT-V1
current_count: 6_OF_10
next_decision: OMW-DEC-20260805-PLANNING-FIRST-10-15-MINUTES-FLOW-V1
```

Google Sheet는 GitHub 정본을 운영·탐색 목적으로 미러링하는 `USER_FACING_GDD_WORKSPACE`다. Sheet 단독 변경은 정본 변경이 아니며, PR 병합 전 쓰기는 `PROPOSED_SHEET_CHANGE` 상태로 취급한다.

## 1. 6/10 동기화 대상

반드시 기록할 항목:

```text
Decision ID
exact PR HEAD
Planning counter = 6_OF_10
Stage 1~19 종료 상인 방문
Stage 20 상인 금지 / MapRun 최종 정산
재고 4칸 = 룰렛 제어 / 복구 / 성장 보조 / 가변 기회
이동권 3/3 = 다음 룰렛 1회 할인
구매 통화 = 골드
상시 상점·무한 구매·무한 reroll·직접 핵심 보상 판매 금지
OMW-AUD-468~491
RED run 986
최종 Green run IDs
다음 Gate = 첫 10~15분 흐름 7/10
```

## 2. 상품 역할

```text
A = 보관형 이동권 또는 다음 룰렛 1회 할인
B = 손상 건물 수리
C = 전술 연구 가속
D = 이동권·수리·연구·다음 건설/업그레이드/룰렛 1회 할인 후보
```

금지:

```text
병종·T3·Hero·Legendary 직접 판매
전술스킬 직접 해금
마력 직접 판매
건물 분기 재선택
Stage 정보 판매
```

## 3. 수명주기

과거 상시 상점·무한 재고·직접 핵심 보상 판매는 다음 상태로 기록한다.

```text
SUPERSEDED
IMPLEMENTATION_INPUT_FORBIDDEN
```

과거 3/10·4/10·5/10 행은 수정하거나 삭제하지 않고 새 6/10 행을 추가한다.

## 4. 기록 탭

- `00_프로젝트_허브`: 현재 Decision·counter·exact HEAD·상태.
- `01_작업순서`: 6/10 작업 범위와 검증 증거.
- `02_현재_확정결정`: Stage 종료 상인 정본 요약.
- `03_근거_라이브러리`: 사용자 승인·Spec·Review·TDD·Lifecycle 근거.
- `04_누락_충돌_감사`: `OMW-AUD-468~491`.
- `05_GDD_요약`: Stage 종료 정비시간·4칸 재고·골드 기회비용.
- `12_핵심루프`: 결과 정산→상인→다음 Stage 설계 연결.
- `15_조작_게임규칙`: 상품 공개·대상 선택·구매 확인·소멸 조건.
- `40_핵심시스템_메인콘텐츠`: 유한 재고·상태 기반 대체·거래 경계.
- `50_메인콘텐츠`: Act·Boss 직전 상품 역할과 단일 하드키 금지.
- `99_변경이력`: exact HEAD·PR·병합 SHA·read-back 상태.

## 5. 쓰기 규칙

1. GitHub 책임 원본과 Decision ID를 먼저 확정한다.
2. exact PR HEAD를 기록한다.
3. 과거 행을 덮어쓰지 않고 신규 행을 사용한다.
4. 쓰기 직후 같은 bounded range를 다시 읽는다.
5. Decision ID·HEAD·counter·감사 범위·다음 Gate 불일치는 blocker다.
6. PR 병합 뒤 현재 6/10 상태 범위만 merged main SHA로 갱신한다.

## 6. 차단 표식

```text
OPEN_P0
OPEN_P1
MERGE_BLOCKER
READBACK_PENDING
```

fresh preflight에서 열린 차단 표식이 있으면 병합하지 않는다.

## 7. 제품 경계

```text
PRODUCT_CODE = UNCHANGED
DATA_MIGRATION = NOT_AUTHORIZED
EXACT_NUMERICS = PENDING_SIMULATION
IMAGE_GENERATION = STOPPED_BY_USER
```

## 8. 완료 이력

```text
OMW-DEC-20260805-PLANNING-SIX-BUILDING-T2-T3-BRANCHES-AND-COUNTERS-V1
3_OF_10
OMW-DEC-20260805-PLANNING-TROOP-ROLES-SYNERGIES-AND-COUNTERS-V1
4_OF_10
OMW-DEC-20260805-PLANNING-TACTICAL-SKILLS-AND-MANA-V1
5_OF_10
LEGACY_C1_C2_C3_PROVEN
```
