# OMENWARD Active Context

## 현재 단계

Base 최신 `main` `ee265576da7f67d3278f8099dd97d4e714ef0651`의 운영 모델·자동 Skill 라우팅·Legacy 정합성·정본 최신성·패키지 무결성 계약을 `codex/omenward-active` PR에 통합하는 단계다. 플레이 가능한 수직 슬라이스의 게임 규칙·콘텐츠는 재설계하지 않는다.

## 확정

- 공식명: OMENWARD / 오멘워드, 루메른 왕국, 루미엔 영토, 트리븐 전선, 실베른 성채, 베일런 황야, 베일의 법칙, 벨루, 베일종.
- 전장: 좌우 대칭 독립 3라인, 본진→성문→중간거점→중앙 접전지→적 중간거점→적 성문→적 본진.
- 전투 데이터: 진영별 별도 전투 아키타입 대신 공용 `UnitArchetypeProfile` 10개와 `FactionVisualProfile`.
- 기본 전략 줌에는 미니맵을 두지 않는다.
- 11개 분야는 Omenward에서 모두 실제 책임이 있어 `selected_disciplines`로 유지한다.
- Base 공용 13개 활성 Skill은 Omenward용 로컬 Foundation/Specialist 어댑터로 설치한다.

## Base reconciliation

- 현행 기준: `ee265576da7f67d3278f8099dd97d4e714ef0651`
- 이전 기준: Base PR #18 `d2457e75a856260d309203e20262f2a2142d2dd6`는 현행 main이 아닌 분기.
- PR #18 전용 Productivity Manifest 연결은 삭제하지 않고 비정본 legacy extension으로 격리.
- Work Mode는 PLAN/BUILD/REVIEW, Skill은 trigger 기반 자동 최소 선택.
- 구형 ID·경로·파생본은 `LEGACY_SKILL_ALIASES.md`와 처리표를 사용한다.

## 금지·미확정

- 게임 규칙·콘텐츠·Scene·Resource·게임 데이터·저장 형식은 별도 승인 없이 변경하지 않는다.
- 최종 팔레트·스프라이트·전체 Visual Set은 제작 검증 대상이다.
- 승인 전장 시안과 표시 계약을 임의 변경하지 않는다.
- 1920×1080·1280×720 사람 플레이·시각 QA는 실행 증거가 없으면 `[미검증]`.

## 다음 작업과 검증

1. Registry·24개 Skill 패키지·Schema·문서 링크 검증
2. Skill Map Markdown/PDF/assets/Manifest 재생성
3. Python 계약·정본 최신성·패키지 무결성 검사
4. PR diff·중복 PR·리뷰·CI 확인
5. 게임 파일 미변경 확인
6. 사람 QA는 별도 실행 전 `[미검증]`

## 보존 증거

기존 `4cb0ae4` 기준 267개 파일의 보존표와 승인 자산 해시는 유지한다. 이번 작업은 운영체계 파일만 갱신하며 기존 코드·Scene·데이터·자산을 삭제·재설계하지 않는다.
