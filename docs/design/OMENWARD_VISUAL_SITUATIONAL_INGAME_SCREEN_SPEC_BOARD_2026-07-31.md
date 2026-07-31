# 오멘워드 상황별 인게임 화면 명세 보드 — 폐기 기록

- 기존 결정 ID: `OMW-DEC-20260731-VISUAL-SCREEN-BOARD-V1`
- 최초 작성일: `2026-07-31`
- 재검토일: `2026-08-01`
- 현재 상태: `REJECTED_EVIDENCE / SUPERSEDED_PENDING_REBUILD`
- 제품 구현 권한: `NONE`
- 실제 이미지·제품 에셋 승인: `NO`
- 대체 게이트: `OMW-DEC-20260801-PROJECT-INTEGRITY-GATE-V1`

이 문서의 이전 버전은 오멘워드가 구현되면 보일 화면을 정리하는 텍스트 와이어프레임으로 승인됐으나, 후속 이미지 제작과 사용자 검토에서 **프로젝트 핵심 구조와 시각 방향을 정확히 반영하지 못한 입력**으로 판정됐다. 이전 본문은 Git 이력에 남기고 활성 화면 명세로 사용하지 않는다.

---

## 1. 폐기 사유

1. 실제 사용자 시각자료보다 문서 기반 추론을 우선해 `어두운 청회색 전장`, `짙은 금속 패널`을 목표 비주얼처럼 고정했다.
2. 밝은 백색·청색·금색 아군 진영과 검보라·적색 베일 침식의 대비를 충분히 반영하지 못했다.
3. 룰렛을 왼쪽·중앙·오른쪽 세 원형 TokenInstance 배열이 노출하는 3×3 정지 보드로 고정하지 못해, 후속 이미지에서 독립 원판 세 개처럼 왜곡됐다.
4. 하나의 전장 안에 있는 상·중·하 세 라인과 양측 중간 거점 구조가 후속 이미지에서 별도 전투장 또는 일반 3레인 디펜스로 왜곡됐다.
5. 건설 노드가 한 종류이고 본진 6개/진영, 중간 거점 3개/거점, 중앙 접전지 0개라는 검산이 없었다.
6. 승인 문서와 실제 Legacy 구현을 모두 `CURRENT`로 묶어 근거 수준을 충분히 분리하지 못했다.
7. 생성 실패를 Sheet·PR·검수 로그에 즉시 환류하지 않아 같은 오류가 반복됐다.

---

## 2. 재사용 금지

이 문서의 이전 버전에서 다음을 신규 화면·이미지·코드의 입력으로 사용하지 않는다.

- 비주얼 팔레트와 조명 방향.
- 메인·전투·자원 관리·결과 화면 와이어프레임.
- 노드·전선·룰렛 배치.
- 벨루 또는 기타 안내자 외형 추론.
- `TEXT_WIREFRAME_COMPLETE`, `APPROVED_SPEC` 상태 주장.

이전 내용은 실패 원인 분석용 `REJECTED_EVIDENCE`로만 읽는다.

---

## 3. 재작성 전 필수 입력

새 화면 보드를 작성하려면 다음이 모두 필요하다.

1. `docs/operations/PROJECT_UNDERSTANDING_AND_OMISSION_PREVENTION_GATE_2026-08-01.md`의 사실표와 충돌 원장 `PASS`.
2. `docs/design/APPROVED_BATTLEFIELD_TOPOLOGY_AND_CONSTRUCTION_NODE_INVARIANTS_2026-08-01.md` 검산.
3. `docs/design/APPROVED_ROULETTE_CORE_RULES.md`의 물리 릴·3×3 보드·이동 계약 검산.
4. `docs/images/VISUAL_REFERENCE_INDEX.md`의 최신 사용자 시각자료 등록과 참고/금지 요소 확인.
5. `CURRENT_CANON`, `CURRENT_IMPLEMENTATION`, `LEGACY_PROVEN`, `PROPOSED`, `PLACEHOLDER`, `REJECTED_EVIDENCE`, `UNRESOLVED` 분리.
6. 벨루·율비 관계 등 열린 P1 시각 Finding 해결 또는 명시적 제외.
7. 화면별 브리프의 사용자 확인.

---

## 4. 현재 판정

```text
VISUAL_SCREEN_BOARD_V1: REJECTED
TEXT_WIREFRAME: NOT_VALID_FOR_REUSE
GENERATED_IMAGES: REJECTED_PROJECT_MISMATCH
NEW_VISUAL_BOARD: BLOCKED_PENDING_FACT_MATRIX
CURRENT_PRODUCT_UI: LEGACY_TECHNICAL_GRAYBOX_ONLY
PRODUCT_ASSET_APPROVAL: NO
PRODUCT_CODE_AUTHORIZATION: NO
```