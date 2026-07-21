# Omenward 구조 마이그레이션 보존표

## 감사 기준

- 현재 기본 브랜치 기준: `4cb0ae4b144f41597b0731a8cf26affff9713b13`
- Base 현행 기준: `ee265576da7f67d3278f8099dd97d4e714ef0651`
- 과거 Base PR #18 기준: `d2457e75a856260d309203e20262f2a2142d2dd6` — 비정본 legacy 기록만 허용
- 파일별 경로·크기·SHA-256·제목·판정·목표 경로: `MIGRATION_INVENTORY_BEFORE.json`
- 이주 후 해시 대조: `MIGRATION_INVENTORY_AFTER.json`
- Base 전수 대조: `docs/base/BASE_SYNC_AUDIT_2026-07-21.md`

현재 PR은 `main`보다 34커밋 뒤처진 diverged 상태다. 아래 보존 판정은 안전한 rebase/merge와 충돌 해결 뒤 다시 검증해야 한다.

## 판정 규칙

| 원본 집합 | 판정 | 새 책임 위치 | 보존 조건 |
|---|---|---|---|
| 승인 게임·전장·경제·병종·세계·UI·아트·성능 문서 | [등록 부록] | 해당 01~10 분야 `등록_부록/` | 원문·표·수치·승인·미검증 표기를 해시 동일하게 보존 |
| 현행 시작·상태·지도·Roadmap·검증 문서 | [본책 이주] 또는 [등록 부록] | 00 허브, 08 QA, 09 PM | 새 본책과 허브가 유일한 활성 라우터 |
| 시각 자료와 테스트·실행 결과 | [증거] | 06 아트 또는 08 QA | Asset Registry와 검증 경로로 연결 |
| 미결 제안·설계 노트 | [보류] | `[기획서]/[보류]/omenward/` | 재개 승인 전 구현 지시로 사용 금지 |
| 과거 Issue·Goal·Work Order·archive·기존 README/AGENTS | [백업] | `[기획서]/[백업]/omenward/` | 역사 보존 전용, 기본 읽기 제외 |
| Issue 동기화 Workflow | [유지] | `.github/workflows/issue-to-repo.yml`, `.github/workflows/repo-to-issue.yml` | 명시적 폐기 승인과 대체 경로 전에는 삭제 금지 |

## 보호 범위와 실제 PR 변경

| 항목 | 현재 판정 | 보존 위치 / 조건 |
|---|---|---|
| 기존 게임 코드·Scene·데이터·저장 형식 | [보호] | Base 동기화 자체는 변경하지 않음. 다만 이 PR의 별도 HUD·룰렛·건설 커밋이 코드 6개와 HUD Scene을 변경하므로 승인 기획·테스트·회귀를 별도로 통과해야 함 |
| `project.godot` | [승인된 정합성 변경] | `config/features=PackedStringArray("4.7")`만 추가; 960×540/1920×1080, `viewport`, `aspect="keep"`, integer scaling, nearest filter 유지 |
| 승인 전장 시안 | [증거] | `06_아트/승인_참고_자산/omenward-battlefield-3lane-concept-v1.png` |
| 전장 시안 SHA-256 | [증거] | `8bd54c1660adaf073dc759d127e0d2e3da12d0fef71b04af6d08100591ab51b5` |
| 전장 시안 해석 | [등록 부록] | 최종 텍스처가 아니며 기능 배치는 게임 디자인 전장 규칙이 책임짐 |
| `.staging` 시각 조각 | [이주 중간재] | 최종 바이너리 배치·Asset Registry 해시·참조 검증 전에는 완료 증거가 아님 |
| 원래 dirty worktree | [외부 보존 주장] | 저장소 문서만으로 존재를 보장하지 않음. 해당 로컬 환경에서 경로·stash·해시를 직접 확인해야 함 |

## Ready 차단 조건

다음 중 하나라도 남으면 PR을 Ready로 전환하거나 병합하지 않는다.

- `main`과의 divergence·충돌 미해결
- `MIGRATION_INVENTORY_BEFORE.json` 행의 누락·해시 불일치·끊긴 활성 링크
- 승인 룰렛 정본과 구현·테스트의 보상 수량 또는 전설 제한 불일치
- Skill Registry와 Skill Map/PDF/Manifest의 source hash·source commit 불일치
- Python·Godot import·headless·runtime smoke 미실행 또는 실패
- 1920×1080·1280×720 사람 시각 QA 미실행
- 시각자료가 `MIGRATION_PENDING` 또는 `.staging` 중간재로만 존재
