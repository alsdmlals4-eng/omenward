# [현행] OMENWARD Google Sheet 정본 동기화 계약

```yaml
updated_at: 2026-08-05
spreadsheet_id: 1VLwRtXGDtyj0JFt98wdIOtG6Zqc3wtdfCzSF9Fo6lpw
status: CONFIGURED / DECISION_5_SYNC_PENDING
current_decision: OMW-DEC-20260805-PLANNING-TACTICAL-SKILLS-AND-MANA-V1
current_count: 5_OF_10
next_decision: OMW-DEC-20260805-PLANNING-STAGE-END-MERCHANT-V1
```

Google Sheet는 GitHub 정본을 운영·탐색 목적으로 미러링한다. Sheet 단독 변경은 정본 변경이 아니다.

## 1. 5/10 동기화 대상

반드시 기록할 항목:

```text
Decision ID
exact PR HEAD
Planning counter = 5_OF_10
마력탑 최대 1개
마력탑 T1 → T2 → T3
연구 = 골드 + 시간
시전 = 마력
전술스킬 = T1 4 / T2 3 / T3 3
MapRun 연구·해금·마력 초기화
OMW-AUD-444~467
RED run 954
최종 Green run IDs
다음 Gate = Stage 종료 상인 6/10
```

## 2. 전술 목록

```text
T1 = 속박진 / 수호장 / 집중 명령 / 충격파
T2 = 폭풍 억제 / 파쇄 명령 / 봉쇄 결계
T3 = 결전의 깃발 / 성역 / 시간 왜곡
```

## 3. 용어·수명주기

Sheet의 현행 결정·GDD·핵심루프·조작·핵심시스템 행은 전술 자원을 마력으로 기록한다.

과거 마력탑 분기와 구형 자원명은 다음 상태로 기록한다.

```text
SUPERSEDED
IMPLEMENTATION_INPUT_FORBIDDEN
```

과거 3/10·4/10 행은 수정하거나 삭제하지 않고 새 5/10 행을 추가한다.

## 4. 기록 탭

- `00_프로젝트_허브`: 현재 Decision·counter·exact HEAD·상태.
- `01_작업순서`: 5/10 작업 범위와 검증 증거.
- `02_현재_확정결정`: 전술·마력 정본 요약.
- `03_근거_라이브러리`: 사용자 승인·Spec·Review·TDD·Lifecycle 근거.
- `04_누락_충돌_감사`: `OMW-AUD-444~467`.
- `05_GDD_요약`: 마력탑·전술 연구·시전 흐름.
- `12_핵심루프`: 연구→해금→수동 시전→복기 연결.
- `15_조작_게임규칙`: 대상 미리보기·수동 확정·무효 시전 무소비.
- `40_핵심시스템_메인콘텐츠`: 단일 마력탑·4·3·3 전술.
- `50_메인콘텐츠`: 다섯 압력 대응 재검증.
- `99_변경이력`: exact HEAD·PR·병합 SHA·read-back 상태.

## 5. 쓰기 규칙

1. GitHub 책임 원본과 Decision ID를 먼저 확정한다.
2. exact PR HEAD를 기록한다.
3. 과거 행을 덮어쓰지 않고 신규 행을 사용한다.
4. 쓰기 직후 같은 bounded range를 다시 읽는다.
5. Decision ID·HEAD·counter·감사 범위·다음 Gate 불일치는 blocker다.
6. PR 병합 뒤 현재 5/10 상태 범위만 merged main SHA로 갱신한다.

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
LEGACY_C1_C2_C3_PROVEN
```
