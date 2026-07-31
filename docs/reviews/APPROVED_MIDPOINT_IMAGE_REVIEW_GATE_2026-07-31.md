# 오멘워드 중간 이미지 점검 게이트 — 재설정

- 기존 결정 ID: `OMW-DEC-20260731-MID-IMAGE-REVIEW-V1`
- 최초 승인일: `2026-07-31`
- 재검토일: `2026-08-01`
- 현재 상태: `WORKFLOW_RETAINED / CURRENT_BATCH_REJECTED / RESET_REQUIRED`
- 제품 구현 권한: `NONE`
- 실제 이미지 생성 상태: `GENERATED_BUT_REJECTED`
- 제품 에셋 승인: `NO`
- 대체 선행 게이트: `OMW-DEC-20260801-PROJECT-INTEGRITY-GATE-V1`

중간 이미지 점검이라는 절차 자체는 유지한다. 다만 기존 텍스트 화면 보드와 이를 입력으로 만든 이미지들은 프로젝트 불일치로 폐기됐다. 기존 배치를 `AWAITING_IMAGE`나 `NOT_RUN`으로 되돌리지 않고 실패 증거로 보존한다.

---

## 1. 실패 판정

사용자 검토에서 다음 오류가 확인됐다.

- 일반 다크 판타지 RPG·수집형 영웅·장비 인벤토리 화면으로 변질.
- 3개의 독립 원형 룰렛처럼 표현.
- 실제 세 물리 릴이 노출하는 3×3 정지 보드 구조 누락.
- 하나의 전장과 상·중·하 세 라인을 일반 3레인 디펜스 또는 분리 전투장처럼 표현.
- 건설 노드의 단일 종류·정확한 수량·위치 누락.
- 중앙 접전지에 노드를 추가하거나 별도 노드 유형을 발명.
- 최신 사용자 시각자료보다 잘못된 텍스트 추론을 우선.

판정:

```text
PROJECT_MATCH: FAIL
ROULETTE_STRUCTURE: FAIL
BATTLEFIELD_STRUCTURE: FAIL
NODE_TOPOLOGY: FAIL
CURRENT_PROPOSED_BOUNDARY: FAIL
VISUAL_DIRECTION: FAIL
```

---

## 2. 기존 Image ID 상태

| Image ID | 기존 목적 | 현재 상태 |
|---|---|---|
| `OM-IMG-005` | 메인·런 진입 | `REJECTED_PROJECT_MISMATCH / RESET_REQUIRED` |
| `OM-IMG-006` | Stage 준비·자원 관리 | `REJECTED_ROULETTE_AND_NODE_MISMATCH / RESET_REQUIRED` |
| `OM-IMG-007` | 일반 3전선 전투 | `REJECTED_BATTLEFIELD_TOPOLOGY_MISMATCH / RESET_REQUIRED` |
| `OM-IMG-008` | Stage 15 위험 보스 | `REJECTED_FOUNDATION_MISMATCH / RESET_REQUIRED` |
| `OM-IMG-009` | Stage 정산·복기 | `REJECTED_CAUSAL_UI_MISMATCH / RESET_REQUIRED` |
| `OM-IMG-010` | 패배·유료 재시도 | `REJECTED_FOUNDATION_MISMATCH / RESET_REQUIRED` |

여러 생성 이미지가 하나의 보드에 섞여 Image ID별 파일 경계가 불명확했다. 따라서 제품 자산 버전으로 등록하지 않고 `REJECTED_CONVERSATION_EVIDENCE` 묶음으로 기록한다.

---

## 3. 재시작 전 강제 조건

새 이미지를 만들기 전에 다음이 모두 충족돼야 한다.

1. 프로젝트 사실표와 충돌 원장이 작성되고 열린 P0가 없다.
2. 전장 토폴로지 검산이 통과한다.
3. 룰렛 물리 구조 검산이 통과한다.
4. 최신 사용자 제공 시각자료가 `docs/images/VISUAL_REFERENCE_INDEX.md`에 등록된다.
5. 잘못된 화면 보드 V1을 입력으로 사용하지 않는다.
6. 각 Image ID를 한 장씩 독립 브리프로 작성한다.
7. 브리프에는 화면에 있어야 하는 구조뿐 아니라 **절대 넣지 않을 구조**를 명시한다.
8. 사용자가 브리프를 확인하기 전 전체 보드 이미지를 생성하지 않는다.

---

## 4. 필수 구조 검산

### 룰렛 이미지

```text
세로로 보이는 3개 릴 열
각 열에서 연속 3개 토큰 노출
전체 화면 결과는 3×3
독립 원판 3개 금지
독립 9칸 확률 추첨 표현 금지
TokenSource 1동 → 세 릴에 같은 출처 토큰 1개씩
```

### 전장 이미지

```text
전장 1개
상·중·하 3라인
라인마다 양측 중간 거점
라인마다 중앙 접전지 1개
본진 노드 6개/진영
중간 거점 노드 3개/거점
중앙 접전지 노드 0개
노드 종류는 건설 노드 1종
```

---

## 5. 근거 상태

새 브리프는 다음 상태를 사용한다.

```text
CURRENT_CANON
CURRENT_IMPLEMENTATION
LEGACY_PROVEN
INFERRED
PROPOSED
PLACEHOLDER
REJECTED_EVIDENCE
UNRESOLVED
```

`CURRENT` 단일 표기는 사용하지 않는다.

---

## 6. 검수 기록 계약

Google Sheet의 `71_이미지기획_생성목록`과 `72_이미지검수_승인로그`에 다음을 기록한다.

- 실제 생성 여부.
- 사용자 판정.
- 오류 종류.
- 폐기 또는 재설계 이유.
- 사용한 정본·시각자료.
- 다음 생성 차단 조건.

사용자에게 폐기된 이미지를 `이미지 미제공`, `AWAITING_IMAGE`, `NOT_RUN`으로 되돌리지 않는다.

---

## 7. 현재 상태

```text
MIDPOINT_IMAGE_REVIEW_WORKFLOW: RETAINED
PREVIOUS_TEXT_WIREFRAME: REJECTED
PREVIOUS_GENERATED_IMAGES: REJECTED_EVIDENCE
OM_IMG_005_TO_010: RESET_REQUIRED
NEW_IMAGE_BRIEFS: NOT_APPROVED
NEW_IMAGE_GENERATION: BLOCKED
PRODUCT_ASSET_APPROVAL: NO
PRODUCT_CODE_AUTHORIZATION: NO
```