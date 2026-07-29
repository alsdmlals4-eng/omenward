
> # OMENWARD

**오멘워드**는 건물과 가로 이동으로 세 원형 릴의 토큰 구조를 설계하고, 예고된 공세에 맞춰 당첨 병력을 상·중·하 세 전선 중 하나에 커밋하는 판타지 전략 오토배틀 게임입니다.

> 설계 상태: **V2_SPEC_APPROVED**  
> 정본 상태: **V2_CANON_CURRENT_BY_PR_57_MERGE**  
> 구현 상태: **V2_IMPLEMENTATION_NOT_STARTED / LEGACY_C1_C2_C3_PROVEN**  
> 사람 검증: **HUMAN_QA_NOT_RUN**  
> 잠금 상태: **CORE_LOCK_V2_PENDING**  
> 엔진: Godot 4.7.1 Standard / GDScript / Compatibility / 960×540 논리 화면 / 1920×1080 출력

## 핵심 문장

> **건물로 룰렛을 만들고, 룰렛으로 전선을 지휘한다.**

## 코어 V2

- 독립된 상·중·하 3라인.
- TokenSource 건물이 각 릴에 같은 출처 토큰 1개씩 공급.
- 길이 3 이상의 세 가변 원형 릴.
- 세로 이동으로 숨은 토큰 탐색.
- 가로 이동으로 현재 보드와 미래 릴을 영구 편집.
- 중앙줄 선행 판정과 동일 심벌 완성선 등급.
- immutable SpinSnapshot과 명시적 한 번 확정.
- 보관함 4칸, 무손실 결과 대기, 판매와 영구 라인 배치.
- 일반 전술계획 정지와 위험 실시간 실행.
- 3기 묶음 웨이브, 10초 예고·20초 시작.
- 적 존재 시 정지하는 고정 8초 중간 접전지.

## 현재 구현 경계

현재 main에는 기존 설계 기준 C1 룰렛, C2 전투 목적, C3 코어 UX 자동 증거가 있습니다. 중앙 판정·등급·금화·결정론·3라인·공용 병종·원인 보고는 보존합니다.

다음은 V2와 충돌해 교체가 필요합니다.

- 독립 9칸 추첨.
- 공개 12% 럭키와 이동 되돌리기.
- 스테이지당 전설 1회.
- 60초 공세와 T-30/T-15/T-5.
- 점령력 합산.
- 단일 StageRun 런 상태.

문서 승인과 정본 병합만으로 V2가 구현됐거나 검증됐다고 보지 않습니다.

## 먼저 읽을 문서

1. [`AGENTS.md`](AGENTS.md)
2. [`docs/PROJECT_CORE.md`](docs/PROJECT_CORE.md)
3. [`docs/design/APPROVED_CORE_V2_INTEGRATED_DECISION_LEDGER_2026-07-25.md`](docs/design/APPROVED_CORE_V2_INTEGRATED_DECISION_LEDGER_2026-07-25.md)
4. [`docs/design/APPROVED_CORE_V2_INTEGRATED_SPEC.md`](docs/design/APPROVED_CORE_V2_INTEGRATED_SPEC.md)
5. [`docs/CURRENT_IMPLEMENTATION_STATUS.md`](docs/CURRENT_IMPLEMENTATION_STATUS.md)
6. [`docs/HANDOFF_CONTEXT.md`](docs/HANDOFF_CONTEXT.md)
7. [`docs/DOCUMENTATION_MAP.md`](docs/DOCUMENTATION_MAP.md)
8. [`docs/OMENWARD_GAME_DESIGN.md`](docs/OMENWARD_GAME_DESIGN.md)
9. [`docs/OMENWARD_ROADMAP.md`](docs/OMENWARD_ROADMAP.md)
10. [`docs/DECISIONS_PENDING.md`](docs/DECISIONS_PENDING.md)

## 다음 순서

```text
V2 정본·Skill·아카이브 연결 완료
→ 2026-07-24 구현 계획을 GM-01~GM-106 기준으로 재검증
→ 첫 V2 구현 패키지 Plan Mode 승인
→ resolver 보존 seam
→ 물리 릴·SpinSnapshot·SpinSession 순수 도메인
→ 후속 승인 패키지
→ 자동 계약·100,000시드·사람 플레이
→ CORE_LOCK_V2 검토
```

제품 코드 변경은 최신 통합 결정 원장에 맞춘 별도 Plan Mode 제안과 사용자 승인 뒤 시작합니다.

## GDD Google Sheets 운영

- Base·GDD 기준: `c987647d01ad2baa028a16e03d85ddfc1572a727`
- Sheet: `PROJECT_SHEET_CONFIGURED`
- Workbook: `docs/PROJECT_GOOGLE_SHEET_WORKBOOK.md`
- 역할: `USER_FACING_GDD_WORKSPACE`
- 사용자 편집: `PROPOSED_SHEET_CHANGE`
- UX/UI 전용 Base content commit은 `docs/UX_UI_SYSTEM.md`가 별도로 소유한다.
