# OMENWARD Development Gates

| 게이트 | 통과 조건 |
|---|---|
| Definition of Ready | 목적·범위·제외·보호 대상·책임 분야·수용 기준·검증·롤백이 승인 계약에 있음 |
| Work Mode | PLAN·BUILD·REVIEW와 Skill 내부 mode가 구분됨 |
| Skill routing | trigger 기반 자동 선택, Foundation ≤3, 주 분야 ≤1, 실행 보고 존재 |
| 문서 구조 | 단일 책임 원본·Registry·24개 활성 Skill 경로·Learning Log·Legacy Alias가 일치 |
| 정본 최신성 | Base commit·경로·ID·Schema·생성기·참조·파생본에 stale 활성 참조 없음 |
| 발행 | 원본→PDF/Markdown/assets→Manifest 재생성 후 working tree diff 없음 |
| 구현 | 승인 범위의 최소 변경, 저장·호환성·승인 자산·표시 계약 보존 |
| 자동 검증 | Python 계약·링크·Schema·패키지 무결성·publication 검사 통과 |
| Godot | editor import → headless 6종 → runtime smoke |
| 접근성·성능 | 적용 범위와 목표 장치·예산을 명시하고 실행 증거를 기록 |
| 수동 QA | 1920×1080·1280×720 플레이/시각 확인; 미실행은 NOT_RUN |
| 통합 완료 | Active Context·Roadmap·PR·발행 Manifest·검증 증거가 일치 |

게이트를 실행하지 못했으면 PASS로 처리하지 않는다. 실패 시 원인·영향·롤백·재검증 조건을 기록한다.
