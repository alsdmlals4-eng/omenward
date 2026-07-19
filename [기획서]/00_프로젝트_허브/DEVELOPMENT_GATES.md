# OMENWARD Development Gates

| 게이트 | 통과 조건 |
|---|---|
| 문서 구조 | 11 본책·1:1 스킬·Registry·보존표·링크가 존재 |
| 발행 | 각 본책 Markdown→PDF→Manifest, 전 페이지 렌더 성공 |
| 구현 준비 | 승인 Issue·Plan Mode, 보호 경로·검증 계획 명시 |
| Godot | editor import → headless 6종 → runtime smoke |
| 수동 QA | 1920×1080·1280×720 플레이 확인 |
| 통합 완료 | Active Context·Roadmap·Handoff·PR 증거가 일치 |

현재 문서 구조 단계에서 로컬 `pdftoppm`은 실행 불가이므로 PDF 렌더는 `NOT_RUN`이며, Linux·Windows CI에서 통과해야 한다.
