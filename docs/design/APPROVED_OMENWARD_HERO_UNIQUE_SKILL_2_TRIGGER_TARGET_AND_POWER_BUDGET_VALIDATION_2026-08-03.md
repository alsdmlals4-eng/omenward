# [보류] 해금 영웅 고유 2스킬 Trigger·대상·파워 검증

```yaml
status: HELD_FOR_CURRENT_COMBAT_AND_CONTENT_RECONCILIATION
held_at: 2026-08-04
implementation_authority: NONE
```

공개 가능한 Trigger·대상 우선순위·숨은 임의 재타깃 금지·결과 설명 가능성은 유효한 설계 후보로 보존한다.

다만 이 문서는 `SAME_LANE_ONLY`, stable-ID tie-break, 고정 평가 주기와 같은 구현 세부를 포함하며, 최신 전투 공간의 명시적 Cross-lane 능력·Route 규칙, Modifier 의미, GPT/Codex 구현 경계와 아직 재조정되지 않았다. 또한 Stage 압력·병종 카운터가 미정인 상태에서 Hero 능력의 정확한 가치를 판단할 수 없다.

재개 조건:

```text
Stage 압력 매트릭스
→ 병종 역할·시너지
→ 건물·전술스킬 역할
→ Hero·Legendary family 통합 재검토
```

현행 전투 의미 문서와 Lifecycle Registry를 우선하며, 이 파일은 신규 Hero 구현·AI·수치 입력으로 사용하지 않는다.
