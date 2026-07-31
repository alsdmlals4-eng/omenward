# 오멘워드 종합 프로젝트 무결성·적대적 검토

- 결정 ID: `OMW-DEC-20260801-PROJECT-INTEGRITY-GATE-V1`
- 검토일: `2026-08-01`
- 상태: `REVIEW_COMPLETE / CORRECTIONS_VERIFIED / PRODUCT_CODE_BLOCKED`
- 검토 범위: GitHub 권위 문서, Base 기준, 실제 Godot Scene·Script, 데이터·테스트, Google Sheet, 비주얼 문서·이미지 상태
- 제품 코드 변경: `NONE`
- Runtime·사람 검증: `NOT_RUN`

---

## 1. 검토 목적

프로젝트 일부만 읽어 일반 장르 관습을 보충하거나, Legacy 구현을 최신 제품 구조로 오인하거나, 실패 산출물을 기록하지 않아 같은 오류를 반복하는 문제를 차단한다.

---

## 2. 프로젝트 사실표

### CURRENT_CANON

- 하나의 전장, 상·중·하 3라인.
- 각 라인은 `아군 본진 → 아군 중간 거점 → 중앙 접전지 → 적 중간 거점 → 적 본진`.
- 건설 노드 종류는 하나다.
- 본진은 진영당 6노드.
- 중간 거점은 `3라인 × 2진영 = 6곳`, 거점당 3노드.
- 중앙 접전지는 라인당 하나이며 건설 노드는 0개.
- 전체 건설 노드는 `2×6 + 6×3 = 30`.
- 룰렛은 왼쪽·중앙·오른쪽 세 원형 TokenInstance 배열이며 화면에는 3×3 정지 보드가 보인다.
- TokenSource 건물 하나는 같은 출처 토큰을 세 릴에 하나씩 공급한다.
- 가로 이동은 세 릴의 노출 행 TokenInstance를 순환 교환하고 이후 회전에도 유지된다.
- 결과 병력은 보관·판매·한 라인 비가역 배치 중 하나로 처리한다.
- 최신 Vertical Slice는 제품 구현되지 않았다.

### CURRENT_IMPLEMENTATION

- `main.tscn`은 별도 제품 메인 메뉴 없이 Battlefield, StageHud, StageSelect를 조립한다.
- Battlefield는 코드 드로잉 graybox이며 라인마다 양측 중간 거점 노드 3개를 원으로 표시한다.
- 본진 건설 노드 6개는 구현·표시되지 않았다.
- RouletteService는 독립 9칸 가중 추첨 방식이다.
- BuildingService는 barracks, tower, farm 3종만 가진다.
- `construct_home()`은 실제 본진이 아니라 아군 중단 중간 거점의 세 노드로 별칭 처리한다.
- RetryButton은 영구재화 없이 현재 Stage를 무료 재시작한다.
- StageHud는 기술 검증용 다중 Label·텍스트 로그 중심이다.

### LEGACY_PROVEN

- 중앙 가로줄 선행 판정과 완성선 등급 계산.
- 금화 75/200/500% resolver.
- 3라인 전투·구조물 피해·전장 승패.
- snapshot→HUD 표시 경계와 원인 보고 개념.

이는 최신 세 물리 릴·30노드·고정 점령·유료 재시도·제품 HUD 검증을 의미하지 않는다.

### REJECTED_EVIDENCE

- 일반 다크 판타지 RPG·수집형 영웅·장비 인벤토리 중심 이미지.
- 3개의 독립 원형 뽑기판으로 룰렛을 표현한 이미지.
- 세 개의 별도 전투장 또는 일반 3레인 디펜스로 전선을 표현한 이미지.
- 접전지에 건설 노드를 추가하거나 노드를 방어·전진·특수 유형으로 나눈 설명.
- 어두운 청회색 전장·검은 금속 패널을 목표 비주얼처럼 확정한 화면 보드 V1.

### UNRESOLVED

- `벨루`와 사용자 제공 `율비` 시안의 관계.
- 최신 사용자 제공 비주얼 바이너리의 저장소 배치.
- 정확한 UI 팔레트·폰트·아이콘 세트.
- 건물·병종·Stage·경제의 세부 수치.
- Base v9.3 계획 패키지의 최종 채택·활성 Adapter 전환 여부.

---

## 3. Finding 최종 상태

| Finding | 심각도 | 상태 | 판정·후속 조치 |
|---|---|---|---|
| `OM-FIND-20260801-01` 생성·폐기 이미지가 미생성으로 남음 | P0 | `VERIFIED_FIXED` | GitHub·Sheet·PR을 `REJECTED/RESET_REQUIRED`로 정정하고 재조회 |
| `OM-FIND-20260801-02` 잘못된 화면 보드가 활성 정본 | P0 | `VERIFIED_FIXED` | 화면 보드 V1을 `REJECTED_EVIDENCE`로 강등하고 라우팅 제거 |
| `OM-FIND-20260801-03` 프로젝트 이해 선행 게이트 부재 | P0 | `VERIFIED_FIXED` | AGENTS와 Documentation Map에 Mandatory Preflight 연결 |
| `OM-FIND-20260801-04` 노드 관계식·접전지 0 의미 누락 | P1 | `VERIFIED_FIXED` | 전장 토폴로지·건설 노드 불변 계약 신설 |
| `OM-FIND-20260801-05` 시각자료 인덱스 경로 오류 | P1 | `VERIFIED_FIXED` | `docs/images/VISUAL_REFERENCE_INDEX.md`로 라우팅 수정 |
| `OM-FIND-20260801-06` 최신 사용자 시각자료·실패물 미등록 | P1 | `MITIGATED_MIGRATION_PENDING` | VR-003~008 등록; 원본 바이너리 이동은 미완료 |
| `OM-FIND-20260801-07` 활성 Base v9.1과 v9.3 계획 혼동 | P1 | `DECLARED_NOT_ADOPTED` | 활성 v9.1, v9.3는 PR 계획 상태로 명시 |
| `OM-FIND-20260801-08` 상태 문서 최신성 부족 | P1 | `PARTIAL_CURRENT_STATUS_VERIFIED` | CURRENT_IMPLEMENTATION_STATUS 갱신; PROJECT_CORE 종합 상태 갱신은 후속 정리 필요 |
| `OM-FIND-20260801-09` Legacy와 최신 계약 혼재 | P1 | `DECLARED_MIGRATION_REQUIRED` | 완료 보고와 인계에서 Legacy seam을 강제 분리 |
| `OM-FIND-20260801-10` 최신 구조 자동 계약 부재 | P1 | `OPEN_BLOCKS_CODEX_BUILD` | 30노드·세 물리 릴·고정 점령·유료 Retry Red tests 필요 |
| `OM-FIND-20260801-11` 벨루·율비 충돌 | P1 | `OPEN_BLOCKS_GUIDE_CANON` | 사용자 결정 전 안내자 비주얼·대사 정본 금지 |
| `OM-FIND-20260801-12` 구형 Sheet 역사 행 혼재 | P2 | `OPEN_CLEANUP_PENDING` | 역사/현재 행 분리 정리 필요 |

열린 P0는 0개다. 열린 P1은 관련 영역만 차단한다.

---

## 4. 적대적 검토 루프 결과

| 검토 축 | 최초 판정 | 수정·재검증 결과 |
|---|---|---|
| 권위 계층 완전성 | `PASS_WITH_FINDINGS` | 게이트·라우터·결정 원장 연결 완료 |
| 정본과 구현 분리 | `FAIL_RISK` | CURRENT_CANON / IMPLEMENTATION / LEGACY 분리 완료 |
| 수량과 관계식 | `FAIL` | `6/3/0 = 30`, 단일 노드 종류 계약 추가 |
| 시각자료 최신성 | `FAIL` | 경로 수정, 최신 자료·실패 증거 인덱싱 |
| 실패 증거 보존 | `FAIL` | `REJECTED_EVIDENCE != NOT_CREATED` 강제 |
| Sheet·GitHub 동기화 | `FAIL` | 같은 Decision ID·authority commit으로 재동기화·재조회 |
| 후속 작업 차단력 | `FAIL` | 열린 P0/P1 기반 Mandatory Preflight 적용 |

---

## 5. 수정된 권위 경로

- `AGENTS.md`
- `docs/DOCUMENTATION_MAP.md`
- `docs/CURRENT_IMPLEMENTATION_STATUS.md`
- `docs/PROJECT_CANON_DECISION_LEDGER.md`
- `docs/operations/PROJECT_UNDERSTANDING_AND_OMISSION_PREVENTION_GATE_2026-08-01.md`
- `docs/design/APPROVED_BATTLEFIELD_TOPOLOGY_AND_CONSTRUCTION_NODE_INVARIANTS_2026-08-01.md`
- `docs/design/OMENWARD_VISUAL_SITUATIONAL_INGAME_SCREEN_SPEC_BOARD_2026-07-31.md`
- `docs/reviews/APPROVED_MIDPOINT_IMAGE_REVIEW_GATE_2026-07-31.md`
- `docs/images/VISUAL_REFERENCE_INDEX.md`

---

## 6. Google Sheet 검증

재조회 범위:

- `00_프로젝트_허브!E2:K2`
- `02_현재_확정결정!A10:L12`
- `04_누락_충돌_감사!A6:H13`
- `15_조작_게임규칙!A4:J5`
- `60_UX_UI_접근성!A6:J8`
- `71_이미지기획_생성목록!E6:F11/J6:J11/L6:L11`
- `72_이미지검수_승인로그!C3:L8`
- `80_데모_버티컬슬라이스_플레이테스트!A6:L8`
- `99_변경이력!A12:H12`

검증 결과:

```text
DECISION_ID_MATCH: PASS
AUTHORITY_COMMIT_MATCH: PASS
REJECTED_EVIDENCE_STATUS: PASS
TOPOLOGY_6_3_0_30: PASS
EXISTING_CELL_FORMATS: PRESERVED
SYNC_STATE: SYNCED_TO_PR_HEAD
```

---

## 7. 현재 완료·차단 판정

```text
REPOSITORY_AND_SHEET_REVIEW: COMPLETE_FOR_PLANNING_SCOPE
PROJECT_FACT_MATRIX: WRITTEN
CONTRADICTION_REGISTER: WRITTEN
TOPOLOGY_INVARIANT: USER_CONFIRMED
OMISSION_PREVENTION_GATE: ACTIVE
OPEN_P0: ZERO
VISUAL_SCREEN_BOARD_V1: REJECTED_PENDING_REBUILD
GENERATED_IMAGES: REJECTED_EVIDENCE
LATEST_VERTICAL_SLICE_IMPLEMENTATION: NOT_STARTED
LATEST_CONTRACT_TESTS: NOT_RUN
HUMAN_QA: NOT_RUN
NEW_IMAGE_GENERATION: BLOCKED_BY_RELATED_P1
PRODUCT_CODE: NOT_AUTHORIZED
CODEX_EXECUTION: BLOCKED
PR_MERGE: NOT_AUTHORIZED
```