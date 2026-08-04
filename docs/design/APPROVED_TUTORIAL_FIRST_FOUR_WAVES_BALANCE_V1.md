# [보류] 실베른 성채 첫 4공세 밸런스 1차안

```yaml
lifecycle: HELD
held_at: 2026-08-04
implementation_authority: NONE
revalidation_gate: OMW-DEC-20260804-PLANNING-FIRST-10-TO-15-MINUTE-FLOW-V1
historical_evidence: PRESERVED_IN_GIT_HISTORY
```

이 문서는 구형 첫 10분 튜토리얼의 수치·병영 자동생산·식량·바리케이드·공세 시계를 검증하기 위해 작성됐다.

현행 정본과 충돌하는 항목:

- 식량을 배치 자원으로 사용.
- 병영이 시간에 따라 병력을 자동생산.
- 바리케이드가 기본 건물·전술 선택으로 등장.
- 첫 네 공세를 현재 20 Stage 구조와 분리된 고정 시간축으로 운용.
- 구형 병종 능력치와 전투 수치를 구현 기준으로 사용.

따라서 최신 첫 10~15분 흐름을 다시 승인하기 전 신규 기획·구현·밸런스 입력으로 사용하지 않는다.

승계 가능한 학습 원칙:

```text
작은 승리
→ 새 압력 인지
→ 룰렛·건물 선택으로 대응
→ 선택 결과를 전장에서 확인
→ 다음 Stage에서 더 복합적인 압력 해결
```

현재 첫 Stage 학습 목표는 다음 정본이 소유한다.

- Stage 1: `MASS` 처리량과 병력 한도.
- Stage 2: `ARMORED` 집중 화력.
- Stage 3: `FLYING` 공격 가능 Layer.
- Stage 4: `INFILTRATION` Route와 후방 예비대.
- Stage 5: `SIEGE` Boss와 구조물 보호.

현재 책임 원본:

- `docs/design/APPROVED_OMENWARD_STAGE_WAVE_DANGER_BOSS_PRESSURE_MATRIX_2026-08-04.md`
- `docs/OMENWARD_GDD_CURRENT_CANON.md`
- `docs/PROJECT_CORE.md`

정확한 첫 10~15분 시간·지급 자원·보장 결과·벨루 안내는 7/10 Decision에서 재설계한다.
