# 오멘워드 종합 프로젝트 무결성·적대적 검토

- 결정 ID: `OMW-DEC-20260801-PROJECT-INTEGRITY-GATE-V1`
- 연계 결정: `OMW-DEC-20260801-BELU-IDENTITY-V1`
- 검토일: `2026-08-01`
- 상태: `REVIEW_COMPLETE / VERIFIED_WITH_OPEN_P1 / PRODUCT_CODE_BLOCKED`
- 검토 범위: 권위 문서, 실제 Godot Scene·Script·data·tests, Google Sheet, 시각자료, Draft PR
- 제품 코드 변경: `NONE`
- Runtime·자동 최신 계약·사람 검증: `NOT_RUN`

## 1. 검토 목적

프로젝트를 일부만 읽어 일반 장르 관습을 보충하거나, Legacy 구현을 최신 제품 구조로 오인하거나, 실패 산출물을 기록하지 않는 재발을 차단한다.

## 2. 프로젝트 사실표

### CURRENT_CANON

- 전장 1개, 상·중·하 3라인.
- 각 라인은 `아군 본진 → 아군 중간 거점 → 중앙 접전지 → 적 중간 거점 → 적 본진`.
- 건설 노드 종류 1개.
- 본진 6노드/진영.
- 중간 거점 `3라인 × 2진영 = 6곳`, 거점당 3노드.
- 중앙 접전지 노드 0개.
- 전체 건설 노드 `2×6 + 6×3 = 30`.
- 룰렛은 왼쪽·중앙·오른쪽 세 원형 TokenInstance 배열과 3×3 정지 보드.
- TokenSource 1동은 같은 출처 토큰을 세 릴에 하나씩 공급.
- 가로 이동은 live 릴 배열에 영구 유지.
- 결과 병력은 보관·판매·한 라인 비가역 배치 중 하나로 처리.
- 안내자는 `벨루 / Belu`; 과거 `율비 / Yulbi`는 동일 인물의 역사 별칭.
- 최신 Vertical Slice는 제품 구현되지 않음.

### CURRENT_IMPLEMENTATION

- `main.tscn`은 Battlefield·StageHud·StageSelect를 조립하며 제품 메인 메뉴가 없다.
- Battlefield와 Unit은 code-drawn graybox다.
- RouletteService는 독립 9칸 가중 추첨 방식이다.
- BuildingService는 barracks·tower·farm 3종만 가진다.
- 중간 거점당 `front_a / front_b / rear` node ID만 존재하며 본진 6노드 모델이 없다.
- 점령은 `capture_power` 합산이다.
- Retry는 영구재화 없이 동일 Stage를 무료 재시작한다.
- StageHud는 Label·개발 버튼 중심이다.

### LEGACY_PROVEN

- 중앙줄 판정·완성선·등급 resolver.
- 금화 75/200/500% resolver.
- 3라인 전투·구조물 피해·승패.
- 공용 병종 데이터와 진영 Visual 분리.
- snapshot→HUD 경계와 원인 보고 seam.

### REJECTED_EVIDENCE

- 일반 다크 판타지 RPG·영웅 파티·장비 인벤토리 중심 이미지.
- 룰렛을 독립 원형 판 3개로 표현한 이미지.
- 세 개의 별도 전투장 또는 일반 3레인 디펜스로 표현한 이미지.
- 접전지 건설 노드와 방어·전진·특수 노드 유형을 발명한 설명.
- 잘못된 어두운 비주얼 추론을 목표로 둔 화면 보드 V1.

### UNRESOLVED

- 사용자 제공 최신 시각자료 바이너리 저장소 배치.
- 정확한 UI 팔레트·폰트·아이콘·화면별 정보 예산.
- 건물·병종·Stage·경제·Retry 비용의 정확한 수치.
- save schema·migration·transaction journal.
- Base v9.3 최종 채택과 활성 Adapter 전환.

벨루·율비 관계는 더 이상 `UNRESOLVED`가 아니다.

## 3. Finding 최종 상태

| Finding | 심각도 | 상태 | 판정·조치 |
|---|---|---|---|
| `OM-FIND-20260801-01` 생성·폐기 이미지가 미생성으로 남음 | P0 | `VERIFIED_FIXED` | GitHub·Sheet·PR을 `REJECTED/RESET_REQUIRED`로 정정 |
| `OM-FIND-20260801-02` 잘못된 화면 보드가 활성 정본 | P0 | `VERIFIED_FIXED` | `REJECTED_EVIDENCE / DO_NOT_REUSE`로 강등 |
| `OM-FIND-20260801-03` 프로젝트 이해 선행 게이트 부재 | P0 | `VERIFIED_FIXED` | Project Understanding Gate를 작업 진입점에 연결 |
| `OM-FIND-20260801-04` 30노드 관계식·접전지 0 의미 부족 | P1 | `VERIFIED_FIXED` | `6/3/0=30` 토폴로지 계약 신설 |
| `OM-FIND-20260801-05` 시각자료 인덱스 경로 오류 | P1 | `VERIFIED_FIXED` | `docs/images/VISUAL_REFERENCE_INDEX.md`로 수정 |
| `OM-FIND-20260801-06` 최신 사용자 시각자료 미등록 | P1 | `MITIGATED_MIGRATION_PENDING` | VR-003~008 등록; 바이너리 이전은 남음 |
| `OM-FIND-20260801-07` 활성 Base v9.1과 v9.3 계획 혼동 | P1 | `DECLARED_NOT_ADOPTED` | v9.3은 PR 계획, 활성 전환 아님 |
| `OM-FIND-20260801-08` Project Core·상태 문서 노후화 | P1 | `VERIFIED_FIXED` | Project Core와 Documentation Map 갱신 |
| `OM-FIND-20260801-09` Legacy와 최신 제품 계약 혼재 | P1 | `DECLARED_MIGRATION_REQUIRED` | CURRENT_IMPLEMENTATION과 최신 정본 분리 |
| `OM-FIND-20260801-10` 최신 구조 자동 계약 없음 | P1 | `OPEN_BLOCKS_CODEX_BUILD` | 다음 작업으로 Red 테스트 명세 필요 |
| `OM-FIND-20260801-11` 벨루·율비 명칭·역할 충돌 | P1 | `VERIFIED_FIXED` | 동일 인물·벨루 통일, 율비는 역사 별칭 |
| `OM-FIND-20260801-12` Sheet 역사·현행 행 혼재 | P2 | `MITIGATED_CLASSIFICATION_ADDED` | 현재 결정 행과 과거 행에 상태 분류; 추가 정리는 후속 가능 |

열린 P0는 0개다. 열린 P1은 해당 영역 작업을 차단한다.

## 4. 적대적 검토 루프

### A — 권위 계층

일부 문서만 읽고 작업할 수 있는지 공격했다. 기본 읽기 순서·사실표·충돌 원장을 필수화했다. `PASS`.

### B — 정본과 구현 분리

실행되는 Legacy를 최신 Vertical Slice로 오인할 수 있는지 공격했다. Project Core와 Current Implementation Status에 차이를 고정했다. `PASS_WITH_MIGRATION_REQUIRED`.

### C — 수량과 관계식

전체 30개만 보고 노드 위치·종류를 잘못 그릴 수 있는지 공격했다. 단일 건설 노드, 본진 6, 거점당 3, 접전지 0, `3×2` 대칭을 고정했다. `PASS`.

### D — 룰렛 표현

세 릴을 독립 원판 또는 9개 독립 셀로 표현할 수 있는지 공격했다. 세 원형 TokenInstance 배열·3×3 노출 보드·영구 가로 이동을 강제한다. `PASS_FOR_PLANNING / AUTOMATION_PENDING`.

### E — 안내자 정체성

벨루와 율비를 별도 인물 또는 임의 개명으로 처리할 수 있는지 공격했다. 동일 인물, 정본명 벨루, 율비는 역사 별칭으로 계약했다. `PASS`.

### F — 실패 증거

실패 이미지를 `NOT_CREATED`로 되돌릴 수 있는지 공격했다. `REJECTED_EVIDENCE != NOT_CREATED`를 문서·Sheet에 고정했다. `PASS`.

### G — 후속 구현 차단력

최신 계약 Red 테스트 없이 Codex 구현을 시작할 수 있는지 공격했다. 관련 P1을 `OPEN_BLOCKS_CODEX_BUILD`로 유지한다. `PASS_AS_BLOCKED`.

## 5. 다음 작업 우선순위

1. 최신 계약 Red 테스트 명세.
2. Legacy 테스트 보존·교체·폐기 판정.
3. 화면 명세 보드 V2.
4. 화면별 독립 브리프와 대표 화면 중간 검수.
5. 경제·Retry 비용·save schema 계약.
6. 사용자 최종 승인 후 Codex 구현 Plan.

## 6. 현재 차단 상태

```text
OPEN_P0: 0
BELU_IDENTITY_CONFLICT: CLOSED
PROJECT_CORE_REFRESH: COMPLETE
VISUAL_BINARY_MIGRATION: PENDING
LATEST_CONTRACT_RED_TEST_SPEC: NOT_WRITTEN
LATEST_CONTRACT_AUTOMATION: NOT_RUN
VISUAL_SCREEN_BOARD_V2: NOT_WRITTEN
IMAGE_CREATION: BLOCKED_PENDING_BRIEF_APPROVAL
PRODUCT_CODE: NOT_AUTHORIZED
CODEX_EXECUTION: BLOCKED
RUNTIME: NOT_RUN
HUMAN_QA: NOT_RUN
PR_MERGE: NOT_AUTHORIZED
```

문서·Sheet·PR을 재조회해 같은 Decision ID와 authority commit이 일치해야 이번 정리가 최종 `VERIFIED`가 된다.
