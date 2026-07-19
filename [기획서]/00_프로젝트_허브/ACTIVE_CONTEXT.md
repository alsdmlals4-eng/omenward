# OMENWARD Active Context

## 현재 단계

Issue #41의 Base PR #18 기반 단일 정본 전환 및 문서 발행 갱신. 플레이 가능한 수직 슬라이스의 규칙·콘텐츠는 재설계하지 않는다.

## 확정

- 공식명: OMENWARD / 오멘워드, 루메른 왕국, 루미엔 영토, 트리븐 전선, 실베른 성채, 베일런 황야, 베일의 법칙, 벨루, 베일종.
- 전장: 좌우 대칭 독립 3라인, 본진→성문→중간거점→중앙 접전지→적 중간거점→적 성문→적 본진.
- 전투 데이터: 진영별 별도 전투 아키타입을 만들지 않고 공용 `UnitArchetypeProfile` 10개와 `FactionVisualProfile`을 사용한다.
- 기본 전략 줌에는 미니맵을 두지 않는다.

## 미확정·금지 범위

- 최종 팔레트·스프라이트·해상도·stretch·전체 Visual Set은 제작 검증 대상이다.
- 게임 규칙·콘텐츠·Scene·Resource·게임 데이터·저장 형식은 변경하지 않는다. `project.godot`은 Godot 4.7 feature 메타데이터만 갱신하며 승인된 viewport·stretch·filter 계약은 유지한다.

## 다음 작업과 검증

`START_HERE.md` → 관련 본책 → 실제 파일·테스트 → `11_통합검수` 순서로 확인한다. 활성 정본은 Issue #41 브랜치 worktree이며, 내부 `omenward/`는 변경 회수용 보존 작업본이다. 문서 변경 뒤에는 링크·Registry·PDF·Manifest·콜드 스타트를 먼저 검증한다.

## 구조 이주·Issue #41 검증 기록 (2026-07-20)

- 기준 `4cb0ae4`의 파일 267개: 보존표 대조 `preserved=267`, 누락·해시 불일치 0건.
- 11개 본책 + 프로젝트 허브, PDF 13개와 Publication Manifest 13개, 11개 분야 스킬, 세 Registry를 확인했다.
- 이전 구조 이주에서는 Godot editor import → headless 6종 → runtime smoke, Python 회귀 6종, 활성 Markdown 링크, `git diff --check`를 통과했다. Issue #41 결과는 새 정본 worktree에서 다시 기록한다.
- 1920×1080 및 1280×720 사람 플레이 QA는 아직 `[미검증]`이다.

## Issue #41 정본 갱신 증거 (2026-07-20)

- 활성 브랜치: `codex/issue-41-base-pr18-refresh`; 내부 `omenward/`의 dirty worktree는 수정·삭제하지 않았다.
- 승인 전장 시안은 원본과 활성 Asset Registry가 모두 SHA-256 `8bd54c1660adaf073dc759d127e0d2e3da12d0fef71b04af6d08100591ab51b5`로 일치한다.
- Godot 4.7.1 editor import → headless 6종 → runtime smoke, Python 회귀 9종, 활성 Markdown 링크, 마이그레이션 보존표를 재실행했다.
- 1920×1080 및 1280×720 사람 플레이 QA는 실행하지 않았으므로 계속 `[미검증]`이다.
