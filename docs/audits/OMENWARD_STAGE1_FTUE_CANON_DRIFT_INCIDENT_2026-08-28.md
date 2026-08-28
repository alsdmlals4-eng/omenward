# OMENWARD Stage 1 FTUE 정본 drift Incident · 2026-08-28

```yaml
incident_id: OMW-INC-20260828-STAGE1-FTUE-CANON-DRIFT-01
status: RESOLVED__CANON_UPDATED__IMPLEMENTATION_NOT_STARTED
scope: PROJECT_SPECIFIC_FIRST_SESSION_EXPOSURE
decision: OMW-PLAN-20260828-STAGE1-PREBUILT-EXPLAIN-01
github_evidence: https://github.com/alsdmlals4-eng/omenward/issues/208#issuecomment-5450880112
base_promotion: NO_BASE_PROMOTION
runtime_evidence: NOT_RUN
```

## Incident

현행 First 5 FTUE owner는 Stage 1에서 여섯 T1을 플레이어가 직접 건설한 뒤 첫 룰렛을 열도록 요구했다. 그러나 fresh-read한 Run Command UI와 실제 building service는 병영·농장·방어탑 세 선택지만 노출했고, 여섯 건물 gate도 강제하지 않았다. 이 불일치는 첫 세션의 학습 목적과 실제 구현을 동시에 잘못 설명할 위험이 있었다.

## Solution

사용자 승인에 따라 Stage 1을 사전 구축 시설 학습으로 바꿨다.

```text
Ward Citadel: 일반병 병영 x1 + 농장 x1
각 Ward 전진기지: 방어탑 x1
→ 시설 종류를 하나씩 설명
→ 첫 3×3 징조륜
→ 비가역 전선 커밋
→ Stage 2의 첫 실제 건설/업그레이드 선택
```

이 변경은 이전 `필수 T1 6종 직접 건설` 및 `여섯 T1 뒤 첫 룰렛` gate만 supersede한다. 방어탑의 정확한 기능 효과와 Veil 전진기지의 대칭 표기는 아직 결정하지 않았다.

## Lesson

FTUE의 학습 노출 순서는 “현재 구현에 있는 버튼 수”와 “정본에 적힌 건설 gate”를 분리해 검증해야 한다. 특히 prebuilt 설명과 player choice가 섞이면, 실제 행동·피드백·다음 단계의 의미가 쉽게 흐려진다.

## Base promotion assessment

`NO_BASE_PROMOTION`: 이 교정의 시설 조합, Stage 1/2 순서, 전진기지 방어탑은 OMENWARD의 고유 제품 규칙이다. 공용 workflow 변경이나 여러 프로젝트에 독립 적용할 수 있는 규칙은 새로 발생하지 않았다.

## Verification boundary

- Repository structured canon / router checks: PASS.
- Existing C1/C2/C3 static validators: PASS.
- Godot runtime, Human usability, Player Experience: `NOT_RUN` for this amendment.
