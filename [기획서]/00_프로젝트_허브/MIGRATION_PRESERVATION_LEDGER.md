# Omenward 구조 마이그레이션 보존표

## 감사 기준

- 원격 기준: `4cb0ae4b144f41597b0731a8cf26affff9713b13`
- Base 기준: `d2457e75a856260d309203e20262f2a2142d2dd6`
- 파일별 경로·크기·SHA-256·제목·판정·목표 경로: `MIGRATION_INVENTORY_BEFORE.json`
- 이주 후 해시 대조: `MIGRATION_INVENTORY_AFTER.json`

## 판정 규칙

| 원본 집합 | 판정 | 새 책임 위치 | 보존 조건 |
|---|---|---|---|
| 승인 게임·전장·경제·병종·세계·UI·아트·성능 문서 | [등록 부록] | 해당 01~10 분야 `등록_부록/` | 원문·표·수치·승인·미검증 표기를 해시 동일하게 보존 |
| 현행 시작·상태·지도·Roadmap·검증 문서 | [본책 이주] 또는 [등록 부록] | 00 허브, 08 QA, 09 PM | 새 본책과 허브가 유일한 활성 라우터 |
| 시각 자료와 테스트·실행 결과 | [증거] | 06 아트 또는 08 QA | Asset Registry와 검증 경로로 연결 |
| 미결 제안·설계 노트 | [보류] | `[기획서]/[보류]/omenward/` | 재개 승인 전 구현 지시로 사용 금지 |
| 과거 Issue·Goal·Work Order·archive·기존 README/AGENTS | [백업] | `[기획서]/[백업]/omenward/` | 역사 보존 전용, 기본 읽기 제외 |
| 문서 이주로 더 이상 실행 대상이 아닌 Issue 동기화·스테이징 CI | [제거] | Git 이력과 이 표 | 새 Publication CI로 대체, 삭제 전 참조 검사 |

## 보호 범위와 외부 작업 승계

| 항목 | 판정 | 보존 위치 / 조건 |
|---|---|---|
| 게임 코드·Scene·데이터·저장 형식 | [증거] | 이주 전후 SHA-256 동일; 본 Issue에서 수정하지 않음 |
| `project.godot` | [승인된 정합성 변경] | `config/features=PackedStringArray("4.7")`만 추가; 960×540/1920×1080, `viewport`, `aspect="keep"`, integer scaling, nearest filter 유지 |
| 승인 전장 시안 | [증거] | `06_아트/승인_참고_자산/omenward-battlefield-3lane-concept-v1.png` |
| 전장 시안 SHA-256 | [증거] | `8bd54c1660adaf073dc759d127e0d2e3da12d0fef71b04af6d08100591ab51b5` |
| 전장 시안 해석 | [등록 부록] | 최종 텍스처가 아니며 기능 배치는 게임 디자인 전장 규칙이 책임짐 |
| 원래 dirty worktree | [백업] | 원래 위치를 수정·삭제·정리하지 않음 |

`MIGRATION_INVENTORY_BEFORE.json`의 모든 행은 위 여섯 판정 중 하나와 실제 목표 경로를 가진다. 대조기에서 누락, 해시 불일치, 끊긴 활성 링크가 1건이라도 나오면 이 PR은 Ready가 아니다.
