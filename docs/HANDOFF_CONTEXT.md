# OMENWARD 프로젝트 인수인계 컨텍스트

```yaml
updated_at: 2026-08-02
project: OMENWARD / 오멘워드
work_mode: TOTAL_PLANNING
phase: CANON_RECOVERY_AND_ADVERSARIAL_PLANNING
recovery_decision: OMW-DEC-20260802-CANON-RECOVERY-V1
baseline_main: 9a39f6869f95ec4e6e1f6b96a6a2f896a22c5739
branch: gpt/omenward-canon-recovery-20260802
base: 9.4.0_RELEASED
current_product: LEGACY_PROTOTYPE
latest_planning: APPROVED_NOT_IMPLEMENTED
product_code_authority: NONE
codex: BLOCKED
sheet_sync: IN_PROGRESS
superseded_pr: 116
```

## 1. 가장 먼저 알아야 할 것

1. 오멘워드는 건물과 TokenSource로 세 물리 릴의 미래 배열을 설계하고, 당첨 병력을 세 전선 중 하나에 비가역 배치하는 전략 오토배틀이다.
2. 주 플랫폼은 PC다. 모바일은 후속 고려이며 현재 구현 범위가 아니다.
3. 현재 `main`은 Base v9.4 운영 계약을 채택했다.
4. PR #116에는 유효한 승인 기획이 많지만 Base v9.3 전제·오래된 HEAD·stale validator·거대 scope drift 때문에 병합 단위로 사용하지 않는다.
5. PR #116의 승인 결정은 새 복구 PR에서 선별 승계한다.
6. 최신 기획은 제품에 구현되지 않았다. 실제 제품은 Legacy 9칸 룰렛·3건물·capture_power·무료 Stage retry다.
7. 현재 목표는 기획 작성과 적대적 검토다. 제품 코드와 Codex 실행은 승인되지 않았다.
8. 상세 수치는 GPT 권장안을 `RECOMMENDED_DEFAULT/TEST_VALUE`로 제시하고 simulation·playtest·사용자 승인 뒤 제품값으로 승격한다.
9. 중요한 기획 충돌만 Grill Me로 한 번에 하나씩 결정한다.
10. 한 Decision이 승인되면 GitHub와 Sheet를 같은 ID·commit으로 동기화한 뒤 다음 질문으로 간다.

## 2. 보호할 프로젝트 코어

```text
공세 예고
→ 건설·TokenSource·세 물리 릴 설계
→ 회전·영구 이동·immutable snapshot·확정
→ 보관·판매·한 라인 비가역 배치
→ 세 라인 자동전투·고정시간 점령
→ 정산·인과 복기
```

- 20 Stage·4막·약 35분.
- 위험 Stage 5/10/15/20.
- 30개 건설 노드.
- 금고·농장·타워·병영·지휘소.
- paid Retry 원칙.
- 안내자 벨루.

## 3. 권위 읽기 순서

```text
최신 사용자 지시
→ AGENTS.md
→ docs/BASE_RULES_VERSION.md
→ docs/DOCUMENTATION_MAP.md
→ docs/PROJECT_CORE.md
→ docs/PROJECT_CANON_DECISION_LEDGER.md
→ docs/audits/OMENWARD_CANON_RECOVERY_AND_TOTAL_PLANNING_RESTART_2026-08-02.md
→ docs/CURRENT_IMPLEMENTATION_STATUS.md
→ docs/ACTIVE_CONTEXT.md
→ 관련 분야 정본·Sheet
→ 실제 code/data/Scene/tests
```

## 4. 현재 적대적 검토 핵심

### 자동 보완 대상

- Base v9.4 기준선과 PR #116 대체 관계.
- GitHub·Sheet HEAD와 authority commit 의미 분리.
- 상태·수치 레이블 통일.
- Context·Handoff·Documentation Map·Workbook 복구.
- 검증된 Sheet schema/열 밀림 오류.

### 사용자 결정 큐

1. `OMW-DEC-20260802-META-PROGRESSION-ROLE-V1` — Profile 영구 성장 역할.
2. 세계·세력·플레이어 동기와 20 Stage 반복의 연결.
3. 10병종·20전문화의 완성형 데모 대표 범위.

### 조사·테스트 큐

- 룰렛 통제감 사람 검증.
- 100K 경제·Retry·save simulation.
- save/retry fault injection.
- 위험 Stage 인지 부하.
- 35분 런 피로도.
- 해상도·접근성 검증.

## 5. 금지된 해석

```text
APPROVED_PLAN != IMPLEMENTED
LEGACY_PROVEN != LATEST_PROVEN
TEXT_SPEC != PRODUCT_UI
RECOMMENDED_DEFAULT != PRODUCT_VALUE
SHEET_SYNC_PENDING != SYNCED
```

- PR #116을 병합하지 않는다.
- Base v9.3 migration을 다시 실행하지 않는다.
- 제품 코드·Scene·Resource·data·asset을 변경하지 않는다.
- 수치·영구 성장·콘텐츠 범위를 AI가 조용히 확정하지 않는다.
- 실행하지 않은 검증을 통과로 기록하지 않는다.

## 6. 바로 다음 작업

```text
정본 복구 완료
→ Sheet read-back SYNCED
→ 대체 Draft PR 생성
→ PR #116 superseded 처리
→ Grill Me #1
```

첫 Grill Me는 Profile 영구 성장의 역할을 결정한다. 이 결정이 확정되기 전에는 Retry 통화·시작 해금·보관 용량·영구 성장 수치를 제품값으로 고정하지 않는다.
