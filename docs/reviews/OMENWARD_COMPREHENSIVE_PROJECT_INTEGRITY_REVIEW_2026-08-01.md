# 오멘워드 종합 프로젝트 무결성·적대적 검토

- 결정 ID: `OMW-DEC-20260801-PROJECT-INTEGRITY-GATE-V1`
- 검토일: `2026-08-01`
- 상태: `REVIEW_COMPLETE / CORRECTIONS_IN_PROGRESS / PRODUCT_CODE_BLOCKED`
- 검토 범위: GitHub 권위 문서, Base 기준, 실제 Godot Scene·Script, 데이터·테스트, Google Sheet, 비주얼 문서·이미지 상태
- 제품 코드 변경: `NONE`
- Runtime·사람 검증: `NOT_RUN`

---

## 1. 검토 목적

이번 검토는 특정 화면 하나를 다시 만드는 작업이 아니다. 프로젝트를 일부만 읽어 일반 장르 관습을 보충하거나, Legacy 구현을 최신 제품 구조로 오인하거나, 실패한 산출물을 기록하지 않는 재발을 차단하는 것이 목적이다.

---

## 2. 프로젝트 사실표

### 2.1 CURRENT_CANON

- 하나의 전장, 상·중·하 3라인.
- 각 라인은 `아군 본진 → 아군 중간 거점 → 중앙 접전지 → 적 중간 거점 → 적 본진`.
- 건설 노드는 한 종류다.
- 본진은 진영당 6노드.
- 중간 거점은 `3라인 × 2진영 = 6곳`, 거점당 3노드.
- 중앙 접전지는 라인당 하나이며 건설 노드는 0개.
- 전체 건설 노드는 `2×6 + 6×3 = 30`.
- 룰렛은 왼쪽·중앙·오른쪽 세 원형 TokenInstance 배열이며 화면에는 3×3 정지 보드가 보인다.
- TokenSource 건물 하나는 같은 출처 토큰을 세 릴에 하나씩 공급한다.
- 가로 이동은 세 릴의 노출 행 TokenInstance를 순환 교환하고 미래 회전에도 유지된다.
- 결과 병력은 보관·판매·한 라인 비가역 배치 중 하나로 처리한다.
- 최신 Vertical Slice는 아직 제품 구현되지 않았다.

### 2.2 CURRENT_IMPLEMENTATION

- `main.tscn`은 별도 제품 메인 메뉴 없이 Battlefield, StageHud, StageSelect를 조립한다.
- Battlefield는 코드 드로잉 graybox이며 라인마다 양측 중간 거점 노드 3개를 원으로 표시한다.
- 본진 건설 노드 6개는 구현·표시되지 않았다.
- RouletteService는 독립 9칸 가중 추첨 방식이다.
- BuildingService는 barracks, tower, farm 3종만 가진다.
- `construct_home()`은 실제 본진이 아니라 아군 중단 중간 거점의 세 노드로 별칭 처리한다.
- RetryButton은 영구재화 없이 현재 Stage를 무료 재시작한다.
- StageHud는 기술 검증용 다중 Label·텍스트 로그 중심이다.

### 2.3 LEGACY_PROVEN

- 중앙 가로줄 선행 판정과 완성선 등급 계산.
- 금화 75/200/500% resolver.
- 3라인 전투·구조물 피해·전장 승패.
- snapshot→HUD 표시 경계와 원인 보고 개념.

위 항목은 최신 세 물리 릴·30노드·고정 점령·유료 재시도·제품 HUD가 검증됐다는 뜻이 아니다.

### 2.4 REJECTED_EVIDENCE

- 일반 다크 판타지 RPG·수집형 영웅·장비 인벤토리 중심 이미지.
- 3개의 독립 원형 뽑기판으로 룰렛을 표현한 이미지.
- 세 개의 별도 전투장 또는 일반 3레인 디펜스로 전선을 표현한 이미지.
- 접전지에 건설 노드를 추가하거나 노드를 방어·전진·특수 유형으로 나눈 설명.
- 어두운 청회색 전장·검은 금속 패널을 목표 비주얼처럼 확정한 기존 화면 보드.

### 2.5 UNRESOLVED

- `벨루`와 사용자 제공 `율비` 시안의 동일 인물·개명·별도 인물 여부.
- 최신 사용자 제공 비주얼 파일의 저장소 바이너리 배치.
- 정확한 UI 팔레트·폰트·아이콘 세트.
- 건물·병종·Stage·경제의 세부 수치.
- Base v9.3 계획 패키지의 최종 채택·활성 Adapter 전환 여부.

---

## 3. Finding 원장

| Finding | 심각도 | 상태 | 문제 | 영향 | 조치 |
|---|---|---|---|---|---|
| `OM-FIND-20260801-01` | P0 | `MITIGATED_PENDING_VERIFY` | 생성·폐기된 이미지가 GitHub·Sheet·PR에 `미생성/AWAITING`으로 남음 | 실패 원인 소실, 같은 오류 반복 | 이미지 게이트·Sheet·PR을 `REJECTED/RESET_REQUIRED`로 정정 |
| `OM-FIND-20260801-02` | P0 | `MITIGATED_PENDING_VERIFY` | 잘못된 텍스트 화면 보드가 `APPROVED_SPEC`으로 후속 생성 입력이 됨 | 프로젝트와 다른 시각 방향 반복 | 기존 보드를 `REJECTED_EVIDENCE`로 대체하고 재작성 차단 |
| `OM-FIND-20260801-03` | P0 | `MITIGATED_PENDING_VERIFY` | 프로젝트 이해 사실표·충돌 원장 없이 이미지 생성 가능 | 정본 일부만 읽고 일반 장르 요소 발명 | 필수 Project Understanding Gate 신설 |
| `OM-FIND-20260801-04` | P1 | `MITIGATED_PENDING_VERIFY` | 30노드 수량은 있었지만 단일 노드 종류·접전지 0노드·대칭 계산이 불명확 | 노드 유형과 위치 오독 | 별도 토폴로지 불변 계약 신설 |
| `OM-FIND-20260801-05` | P1 | `OPEN` | Documentation Map의 시각자료 인덱스 경로가 `images/...`로 잘못됨 | 이미지 정본 탐색 실패 | `docs/images/VISUAL_REFERENCE_INDEX.md`로 수정 |
| `OM-FIND-20260801-06` | P1 | `OPEN` | 최신 사용자 제공 5개 비주얼 자료와 생성 실패물이 시각자료 인덱스에 없음 | 실제 방향보다 오래된 VR-001/002만 참조 | 신규 VR 항목·금지 해석·MIGRATION_PENDING 등록 |
| `OM-FIND-20260801-07` | P1 | `DECLARED` | 활성 Base는 v9.1인데 PR은 v9.3 적용 패키지를 다룸 | 계획과 활성 버전 혼동 | `ACTIVE_V9_1 / V9_3_MIGRATION_NOT_ADOPTED`를 명시 |
| `OM-FIND-20260801-08` | P1 | `OPEN` | PROJECT_CORE·CURRENT_IMPLEMENTATION_STATUS가 후속 결정과 실패 기록을 모두 반영하지 못함 | 새 작업자가 오래된 상태로 시작 | 상태·Decision·차단 게이트 갱신 |
| `OM-FIND-20260801-09` | P1 | `DECLARED` | Legacy 독립 9칸, capture_power, 3건물, 무료 Retry가 최신 계약과 공존 | Legacy를 제품 구현으로 오인 | 모든 완료 보고에 migration 경계 의무화 |
| `OM-FIND-20260801-10` | P1 | `OPEN` | 최신 30노드·세 물리 릴·유료 Retry 자동 계약이 없음 | 구현 후 구조 회귀 탐지 불가 | 구현 승인 패키지의 필수 Red 테스트로 등록 |
| `OM-FIND-20260801-11` | P1 | `OPEN` | 벨루/율비 명칭·역할 충돌 | 화면·아트·대사 정체성 불일치 | 사용자 결정 전 `UNRESOLVED`, 임의 사용 금지 |
| `OM-FIND-20260801-12` | P2 | `OPEN` | Sheet의 구형 PR97/PR92/F-30 행이 CURRENT와 pending 상태를 함께 가짐 | 역사 계보와 현행 정본 혼동 | 역사/현재 분류 정리 필요 |

---

## 4. 적대적 검토 루프

### 검토 1 — 권위 계층 완전성

**질문:** 최신 사용자 지시부터 실제 파일까지 확인했는가.

- AGENTS, Base version, Documentation Map, Project Core, 분야별 계약, 결정 원장, pending, 실제 Scene·Script·tests, Sheet를 확인했다.
- 결과: `PASS_WITH_FINDINGS`.

### 검토 2 — 정본과 구현 분리

**공격:** 실행되는 코드가 있으면 최신 구현으로 오인할 수 있는가.

- 실제 RouletteService는 9칸 독립 추첨이다.
- 실제 무료 Retry와 3건물은 최신 유료 Retry·5건물 계약과 다르다.
- 결과: `PASS_AFTER_LABEL_SPLIT`.

### 검토 3 — 수량과 관계식

**공격:** 전체 30개만 보고 노드 위치를 잘못 배치할 수 있는가.

- 기존 표는 숫자는 맞지만 `단일 노드 종류`, `접전지 0`, `3×2 대칭`이 충분히 강조되지 않았다.
- 결과: `FAIL → TOPOLOGY_CONTRACT_ADDED`.

### 검토 4 — 시각자료 최신성

**공격:** 최신 사용자 이미지를 보지 않고 오래된 인덱스나 텍스트 추론으로 작업할 수 있는가.

- 가능했다. 실제로 잘못된 화면이 생성됐다.
- 결과: `FAIL → VISUAL_PREFLIGHT_BLOCKED`.

### 검토 5 — 실패 증거 보존

**공격:** 실패 산출물을 “미생성”으로 되돌려 같은 시도를 반복할 수 있는가.

- Sheet와 PR이 그렇게 남아 있었다.
- 결과: `FAIL → REJECTED_EVIDENCE_REQUIRED`.

### 검토 6 — Sheet·GitHub 동기화

**공격:** GitHub에서 상태를 바꿔도 Sheet의 `APPROVED/AWAITING`이 남을 수 있는가.

- 현재 가능하다.
- 결과: `FAIL → SAME_DECISION_SYNC_REQUIRED`.

### 검토 7 — 후속 작업 차단력

**공격:** 문서가 있어도 이미지 생성이나 Codex가 바로 실행될 수 있는가.

- 기존 게이트는 체크 권고였고 사실표 PASS가 강제되지 않았다.
- 결과: `FAIL → MANDATORY_PREFLIGHT`.

---

## 5. 보완 우선순위

### 즉시 정정

1. AGENTS에 Project Understanding Gate 추가.
2. Documentation Map에 토폴로지·무결성 게이트 라우팅 추가.
3. 잘못된 화면 보드와 이미지 게이트를 `REJECTED/RESET_REQUIRED`로 강등.
4. Sheet의 OM-IMG-005~010과 검수 로그를 `REJECTED_PROJECT_MISMATCH`로 변경.
5. 시각자료 인덱스에 최신 사용자 자료와 실패 산출물 기록.
6. PR #116 설명을 실제 상태로 갱신.

### 구현 승인 전 필수

1. 30노드 구조 자동 계약.
2. 세 물리 릴·가로 이동 영속성 자동 계약.
3. 고정 점령 계약으로 capture_power test 교체.
4. 5건물·본진 노드 데이터 계약.
5. 제품 유료 Retry와 개발 무료 Retry 분리 테스트.

---

## 6. 현재 완료·차단 판정

```text
REPOSITORY_AND_SHEET_REVIEW: COMPLETE_FOR_PLANNING_SCOPE
PROJECT_FACT_MATRIX: WRITTEN
TOPOLOGY_INVARIANT: USER_CONFIRMED
OMISSION_PREVENTION_GATE: WRITTEN
VISUAL_SCREEN_BOARD: REJECTED_PENDING_REBUILD
GENERATED_IMAGES: REJECTED_EVIDENCE
LATEST_VERTICAL_SLICE_IMPLEMENTATION: NOT_STARTED
AUTOMATED_LATEST_CONTRACTS: NOT_RUN
HUMAN_QA: NOT_RUN
IMAGE_CREATION: BLOCKED
PRODUCT_CODE: NOT_AUTHORIZED
CODEX_EXECUTION: BLOCKED
PR_MERGE: NOT_AUTHORIZED
```

모든 수정 surface를 재조회하기 전 Finding 상태를 `VERIFIED`로 닫지 않는다.