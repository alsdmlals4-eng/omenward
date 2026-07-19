# 벤치마킹 문서

벤치마킹은 참고 게임을 복제하기 위한 문서가 아니라, 플레이어 반응과 시스템 문제를 분석해 Roulettebound에 적용하거나 제외할 결론을 남기는 공간이다.

## 현재 상태

- `0001-core-game-benchmark-proposal.md`: 사용자 검토 완료
- 승인된 결론의 책임 원본: `../design/APPROVED_BENCHMARK_DECISIONS.md`
- 구현 전 후속 기획: `../design/DESIGN_FREEZE_CHECKLIST.md`

## 문서 목록

- [`0001-core-game-benchmark-proposal.md`](0001-core-game-benchmark-proposal.md) — 슬롯·오토배틀·노드 건설·웨이브 전조 핵심 비교 제안서
- [`SOURCE_SNAPSHOT_2026-07-14.md`](SOURCE_SNAPSHOT_2026-07-14.md) — 조사 시점 출처·수치 스냅샷
- [`PLAYER_REACTION_THEMES.md`](PLAYER_REACTION_THEMES.md) — 반복된 긍정·부정 반응
- [`APPLICATION_CANDIDATES.md`](APPLICATION_CANDIDATES.md) — 적용·실험·제외 후보
- [`REVIEW_CHECKLIST.md`](REVIEW_CHECKLIST.md) — 검토 체크리스트

## 사용 규칙

- Steam 평가 비율과 시장 상태는 조사 시점 스냅샷으로 기록한다.
- 장문 리뷰를 복사하지 않고 반복되는 강점·불만과 프로젝트 적용 결론만 남긴다.
- 후보가 승인되면 `docs/design/`에 확정 결정으로 이동한다.
- 과거 조사 원문은 근거 보존을 위해 승인 이후에도 원형을 유지할 수 있다.
- 실제 구현은 별도의 Codex Plan Mode 제안서와 사용자 승인 뒤 진행한다.
