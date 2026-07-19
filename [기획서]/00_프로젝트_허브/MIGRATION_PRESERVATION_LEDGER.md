# Omenward 구조 마이그레이션 보존표

## 감사 기준

- 원격 기준: `4cb0ae4b144f41597b0731a8cf26affff9713b13`.
- Base 기준: `d2457e75a856260d309203e20262f2a2142d2dd6`.
- 코드·Scene·데이터·저장 형식·`project.godot`: `[현행 승계 / 변경 없음]`.

## 파일군 판정

| 기존 파일군 | 판정 | 새 책임 위치 | 보존 조건 |
|---|---|---|---|
| `docs/OMENWARD_GAME_DESIGN.md`, `docs/design/APPROVED_*.md` | 부록 | 01~07 분야 본책 | 승인 수치·예외·미확정 상태를 원 경로로 등록 보존 |
| `docs/HANDOFF_CONTEXT.md`, `ACTIVE_CONTEXT.md`, `OMENWARD_ROADMAP.md`, `DECISIONS_PENDING.md` | 현행 승계 | 00 허브, 09 PM | 새 허브 라우터가 우선; 원본은 이력·세부 부록 |
| `docs/PHASE_0_VALIDATION.md`, `VERTICAL_SLICE_VALIDATION.md`, `tests/` | 증거 | 08 QA, 11 통합검수 | 실행 결과와 미검증 상태 보존 |
| `docs/benchmarks/` | 부록 | 10 분석·유저리서치 | 출처·가설·채택 결론 보존 |
| `docs/issues/`, `docs/goals/`, `docs/work_orders/`, `docs/proposals/` | 증거 | 09 PM | 과거 승인·작업 이력; 기본 읽기 제외 |
| `docs/design/proposals/`, `docs/design/notes/` | 보류 | 관련 분야 | 재개 승인 전 구현 근거로 사용하지 않음 |
| `docs/archive/` | 백업 | 기존 경로 | 기본 읽기 제외 |
| `docs/images/` | 증거 | 05 파이프라인, 06 아트 | 기존 참조를 유지하고 Asset Registry로 연결 |

## 사용자 dirty 작업 승계

| 항목 | 판정 | 새 위치 | SHA-256 / 조건 |
|---|---|---|---|
| 승인 아트 문구 | 현행 승계 | `06_아트_본책.md` | 전장 인게임 기준 승인, 최종 텍스처 아님, 기능 배치는 전장 토폴로지 책임 |
| `omenward-battlefield-3lane-concept-v1.png` | 증거 | `06_아트/승인_참고_자산/` | `8bd54c1660adaf073dc759d127e0d2e3da12d0fef71b04af6d08100591ab51b5` |
| `project.godot` dirty 변경 | 제외 | 원본 worktree | 읽기·복사·수정하지 않음 |

## 제거 판정

이 PR에서는 기존 활성 문서를 삭제·이동하지 않는다. 새 책임 원본·PDF·Manifest·내부 참조·콜드 스타트 검증을 통과한 후에만 별도 PR에서 제거 후보를 판단한다.
