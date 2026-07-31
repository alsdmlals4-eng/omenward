# 오멘워드 프로젝트 이해·누락 방지 게이트

- 결정 ID: `OMW-DEC-20260801-PROJECT-INTEGRITY-GATE-V1`
- 승인일: `2026-08-01`
- 상태: `CURRENT_PROJECT_WORK_RULE / MANDATORY_PREFLIGHT`
- 적용 대상: 기획, 화면 명세, 이미지, UX, 데이터, 코드, 리뷰, 인계
- 제품 구현 권한: `NONE`

이 게이트는 프로젝트를 충분히 이해하지 않은 상태에서 일반 장르 관습이나 일부 문서만으로 화면·시스템·이미지를 만드는 일을 차단한다. 체크리스트를 작성했다는 사실이 아니라, 아래 증거가 실제로 일치하는지가 통과 조건이다.

---

## 1. 작업 시작 전 강제 순서

```text
최신 사용자 지시
→ AGENTS.md
→ BASE_RULES_VERSION.md
→ DOCUMENTATION_MAP.md
→ PROJECT_CORE.md
→ 작업 분야 최신 APPROVED 계약
→ PROJECT_CANON_DECISION_LEDGER.md
→ DECISIONS_PENDING.md
→ CURRENT_IMPLEMENTATION_STATUS.md
→ 실제 Scene·Script·Resource·data·tests
→ 연결 Google Sheet
→ 시각 작업이면 docs/images/VISUAL_REFERENCE_INDEX.md와 실제 이미지
→ 사실표·충돌 원장 작성
→ 적대적 검토 PASS
→ 작업 시작
```

Base 원격 최신 상태를 프로젝트 정본보다 먼저 사용하지 않는다. 현재 적용 Base 버전과 마이그레이션 후보 버전을 구분한다.

---

## 2. 필수 프로젝트 사실표

모든 중형 이상 작업은 시작 전에 다음 표를 내부 작업 기록 또는 산출물 부록에 작성한다.

| 항목 | 필수 기록 |
|---|---|
| 작업 질문 | 이번 작업이 답해야 하는 정확한 질문 |
| 최신 사용자 결정 | 이번 대화에서 새로 확정·정정된 사항 |
| CURRENT_CANON | 최신 승인 문서와 Decision ID |
| CURRENT_IMPLEMENTATION | 실제 Scene·Script·Resource·data 경로와 현재 동작 |
| LEGACY_PROVEN | 실행 증거는 있으나 최신 계약과 다른 부분 |
| PROPOSED | 아직 승인되지 않은 신규 판단 |
| REJECTED_EVIDENCE | 사용자 또는 검토에서 폐기된 산출물 |
| UNRESOLVED | 이름·수치·범위 등 미확정 항목 |
| 충돌 | 문서↔문서, 문서↔구현, Sheet↔GitHub, 시각자료↔정본 불일치 |
| 작업 차단 여부 | P0/P1 Finding과 시작 가능 여부 |

`CURRENT`라는 단일 태그만 사용하지 않는다. 최소 `CURRENT_CANON`과 `CURRENT_IMPLEMENTATION`을 분리한다.

---

## 3. 오멘워드 핵심 구조 검산

아래 항목은 작업 종류와 관계없이 오멘워드의 시스템·화면·이미지를 다룰 때 확인한다.

### 3.1 전장·노드

```text
전장 1개
라인 3개: 상 / 중 / 하
각 라인: 아군 본진 → 아군 중간 거점 → 중앙 접전지 → 적 중간 거점 → 적 본진
노드 종류: 건설 노드 1종
본진 노드: 진영당 6
중간 거점: 3라인 × 2진영 = 6곳
중간 거점 노드: 거점당 3
중앙 접전지 노드: 0
전체 건설 노드: 2×6 + 6×3 = 30
```

### 3.2 룰렛

```text
내부 구조: 왼쪽·중앙·오른쪽 세 원형 TokenInstance 배열
화면 노출: 각 릴에서 연속 3개씩 보여 주는 3×3 정지 보드
초기 최소 구조: 각 릴 길이 3 이상, X 사용
TokenSource 건물 1동: 동일 출처 토큰을 세 릴에 하나씩 공급
세로 이동: 한 릴 전체 cursor 회전
가로 이동: 노출 행의 TokenInstance를 세 릴 사이에서 순환 교환
가로 이동 결과: live 릴 배열에 영구 유지
기본 판정: 중앙 가로줄 동일 비-X 심벌 3개
```

### 3.3 병력·전선

```text
룰렛 결과 → PendingReward → 보관 / 판매 / 한 라인 배치
배치 후 라인 변경·회수·판매 불가
일반 유닛 라인 횡단 없음
생존 병력과 HP는 같은 MapRun 다음 Stage로 유지
각 라인의 중앙 접전지는 점령 목적이며 건설 장소가 아님
```

### 3.4 현재 구현 경계

```text
최신 Vertical Slice: NOT_IMPLEMENTED
Legacy roulette: 독립 9칸 가중 추첨
Legacy battlefield: 3라인 graybox와 midpoint outpost 3노드만 표시
Legacy buildings: barracks / tower / farm 3종
Legacy retry: 무료 Stage 재시작
```

Legacy가 실행된다는 이유로 최신 제품 구조를 구현했다고 표시하지 않는다.

---

## 4. 충돌 원장 규칙

작업 중 발견한 충돌은 즉시 다음 필드로 기록한다.

```text
Finding ID
Severity: P0 / P1 / P2
Source A
Source B
충돌 내용
사용자 영향
현재 권위 판정
수정 대상
검증 방법
상태: OPEN / MITIGATED / VERIFIED / DEFERRED
```

- P0가 하나라도 `OPEN`이면 이미지 생성·제품 구현·최종 기획 승인을 중단한다.
- P1은 관련 작업 범위의 진입을 차단한다.
- `DEFERRED`는 해결이 아니라 명시적 보류다.
- 수정 후 원본 문서, 실제 파일, Sheet를 다시 읽기 전 `VERIFIED`로 닫지 않는다.

---

## 5. 사용자 정정 처리

사용자가 구조·용어·수량·시각 방향을 정정하면 다음 순서로 처리한다.

1. 기존 이해가 왜 틀렸는지 명시한다.
2. 관련 정본·구현·Sheet·이미지 상태를 검색한다.
3. 같은 Decision ID 또는 새 의미형 Decision ID로 권위 문서를 갱신한다.
4. 잘못된 문서·이미지·브리프를 `SUPERSEDED` 또는 `REJECTED_EVIDENCE`로 낮춘다.
5. Sheet 결정·감사·검수·변경 이력을 갱신한다.
6. 재조회하여 정정이 모든 surface에 반영됐는지 확인한다.
7. 같은 종류의 오독을 막는 검산 항목을 이 게이트나 분야 계약에 추가한다.

대화에서 사과하거나 다음 답변에서 올바르게 설명한 것만으로 정정 완료로 보지 않는다.

---

## 6. 이미지·비주얼 작업 추가 게이트

이미지 생성 전 다음이 모두 `PASS`여야 한다.

- 최신 사용자 제공 이미지가 `docs/images/VISUAL_REFERENCE_INDEX.md`에 상태·참고/금지 요소와 함께 등록됨.
- 화면에 들어가는 모든 구조가 사실표에 있음.
- 전장 노드 수량·위치와 접전지 0노드가 검산됨.
- 룰렛이 3개의 독립 원판이나 독립 9칸 추첨으로 표현되지 않음.
- 하나의 전장과 세 라인, 양측 중간 거점 구조가 명시됨.
- `CURRENT_CANON`, `CURRENT_IMPLEMENTATION`, `PROPOSED`, `PLACEHOLDER`가 분리됨.
- 이전 생성 실패와 사용자 피드백이 검수 로그에 기록됨.
- 안내자 이름·비주얼처럼 미확정인 요소를 임의로 확정하지 않음.

이미지가 생성된 뒤에는 성공·실패와 관계없이 검수 로그를 갱신한다. 사용자에게 폐기 판정을 받은 이미지는 `이미지 미생성`으로 되돌리지 않는다.

---

## 7. 기획 작업 추가 게이트

- 새 시스템·핵심 규칙·콘텐츠 구조·UX 흐름은 Benchmark-First 적용 여부를 확인한다.
- 기존 정본을 다시 설계하는지, 빈 계약을 설계하는지 구분한다.
- 수량 요약만 쓰지 않고 관계식·대칭 구조·0개인 항목을 함께 쓴다.
- 프로젝트에 없는 일반 장르 관습을 기본값으로 넣지 않는다.
- 사용자 승인 항목과 설계 제안을 같은 표에서 확정처럼 섞지 않는다.

---

## 8. 구현·Codex 인계 추가 게이트

- 최신 계약과 Legacy 보존 seam을 구분한다.
- 변경 파일과 상태 소유자를 명시한다.
- 최신 불변 조건의 Red 테스트가 있다.
- 특히 다음 계약 테스트가 있어야 한다.
  - 건설 노드 종류 1개.
  - 본진 노드 6개/진영.
  - 중간 거점 6곳·3노드/거점.
  - 접전지 노드 0개.
  - 전체 노드 30개.
  - 세 물리 릴과 영구 가로 이동.
  - 유료 재시도와 개발 무료 재시도 분리.
- 사용자 최종 승인 전 Codex 실행을 시작하지 않는다.

---

## 9. 완료 보고 필수 항목

```text
검토한 권위 문서
검토한 실제 파일
검토한 Sheet 범위
CURRENT_CANON 요약
CURRENT_IMPLEMENTATION 요약
LEGACY / MIGRATION_REQUIRED 요약
열린 P0/P1/P2 Finding
수정한 경로와 commit
Sheet 변경 범위
재검증 결과
미실행 검증
다음 차단 게이트
```

`모두 확인했다`, `문제없다`, `완료했다` 같은 포괄 표현은 위 증거 없이 사용하지 않는다.

---

## 10. 현재 적용 판정

```text
PROJECT_UNDERSTANDING_GATE: MANDATORY
FACT_MATRIX: REQUIRED
CONTRADICTION_REGISTER: REQUIRED
REJECTED_EVIDENCE_LOGGING: REQUIRED
IMAGE_CREATION_WITH_OPEN_P0: BLOCKED
PRODUCT_IMPLEMENTATION: NOT_AUTHORIZED
CODEX_EXECUTION: BLOCKED
PR_MERGE: NOT_AUTHORIZED
```