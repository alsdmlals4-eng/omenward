# Active Context

- 갱신일: 2026-07-17
- 공식명: **오멘워드 / OMENWARD**
- 상태: **5개 책임 본책 통합 중 / 수직 슬라이스 자동 기준선 통과 / 수동 해상도 QA 미실행**
- 현재 브랜치: `codex/five-discipline-planning`
- Base 의존성: `2420f1c6a7c8d8631c8956e579b087909c9baa07`, Base Draft PR #5

## 현재 작업

게임·프로그래밍·아트·사운드·QA·PM을 `docs/planning/`의 다섯 활성 본책으로 통합하고, 최신 공식 이미지 3종과 지속 갱신·문서 검증 장치를 반영한다. 기존 `APPROVED_*.md`는 구체 수치와 데이터 계약을 보존하는 부록으로 분류한다.

## 읽기 순서

1. `AGENTS.md`
2. `docs/DOCUMENTATION_MAP.md`
3. 영향 분야의 `docs/planning/01_GAME_DESIGN.md` ~ `05_QA_PM_PLAN.md`
4. 관련 승인 부록과 실제 파일·테스트
5. `docs/HANDOFF_CONTEXT.md`

## 다음 게이트

1. 문서 링크·이미지 안정 경로·폐기 경로 검증.
2. headless 6종, Godot editor import, runtime smoke 재실행.
3. 1920×1080·1280×720 수동 QA와 전장·UI 시각 프로브.
4. 측정·플레이테스트 결과에 따라 수치·연출 조정 범위 승인.

## 보호·금지

- 사용자 소유 `project.godot` 변경과 `.superpowers/`를 이 문서 작업에 포함하지 않는다.
- 적군 전용 전투 데이터, 미니맵, 일반 유닛 라인 횡단을 추가하지 않는다.
- `율비/Yulbi`를 공식 캐릭터명으로 사용하지 않는다.
- 확인하지 않은 수동 QA·성능·예산을 완료 또는 확정으로 기록하지 않는다.
