# [대체됨] 15웨이브 단일 Stage 시계·초과전 V2

```yaml
lifecycle: SUPERSEDED
superseded_at: 2026-08-04
superseded_by: docs/design/APPROVED_OMENWARD_STAGE_WAVE_DANGER_BOSS_PRESSURE_MATRIX_2026-08-04.md
implementation_authority: NONE
historical_evidence: PRESERVED_IN_GIT_HISTORY
```

이 문서는 다음 구형 구조를 소유했던 역사 자료다.

```text
하나의 Stage 안에서 15웨이브 표준 승리
→ 16~19웨이브 초과전
→ 20웨이브 신화 보스
→ 모든 공세 60초 간격
```

현행 OMENWARD 구조와 직접 충돌하므로 신규 기획·Codex 구현·밸런스 입력으로 사용하지 않는다.

현행 구조:

```text
한 MapRun = 20 Stage
기본 Stage = 3개 Wave Beat 기준선
Danger Stage = 4 / 9 / 14 / 19
Boss Stage = 5 / 10 / 15 / 20
정확한 시간·Threat Budget = 시뮬레이션 후 결정
```

유효하게 승계된 원칙:

- 공세의 치명적 정보와 Boss 존재를 사전에 예고한다.
- 이전 Wave 잔존 병력이 다음 Wave와 겹칠 수 있다.
- Boss는 일반 적보다 명확한 패턴·징조·대응 기회를 가진다.
- 정확한 수치는 플레이테스트와 시뮬레이션으로 조정한다.

승계되지 않은 항목:

- Stage당 15~20 Wave.
- 고정 60초 공세 간격.
- 5/10/15/20 Wave 등급 이정표.
- 15웨이브 Boss 처치를 모든 Stage의 표준 승리로 사용하는 구조.
- 20웨이브를 단일 Stage의 소프트 패배 시한으로 사용하는 구조.

현재 책임 원본:

- `docs/design/APPROVED_OMENWARD_STAGE_WAVE_DANGER_BOSS_PRESSURE_MATRIX_2026-08-04.md`
- `docs/design/APPROVED_OMENWARD_MAPRUN_STAGE_WAVE_MAINTENANCE_2026-08-02.md`
- `docs/PROJECT_CORE.md`
