# [현행] OMENWARD 동적 main·문서 수명주기 정책

```yaml
policy_id: OMW-PROC-20260804-DYNAMIC-CURRENT-MAIN-AND-DOCUMENT-LIFECYCLE-V1
status: ACTIVE_STANDING_POLICY / NON_COUNTER
approved_by: USER_DIRECTIVE
product_code_authority: NONE
```

## 1. 목적

정본 상태 문서가 병합 직후 과거 SHA를 가리키는 재귀 오류를 방지하고, 파일명에 `APPROVED`가 남은 구형 문서가 현행 구현 권위로 오인되는 것을 막는다.

## 2. 현재 main 해석

```text
current_main: RESOLVE_FROM_REPOSITORY_DEFAULT_BRANCH
context_baseline_commit: RESOLVE_FROM_REPOSITORY_DEFAULT_BRANCH
```

- `current_main`과 `context_baseline_commit`에 40자 commit SHA를 고정하지 않는다.
- 특정 병합의 증거는 `last_merged_planning_pr`, `last_merged_planning_commit`, `source_head`, `preflight_runs`처럼 의미가 불변인 필드에 기록한다.
- post-merge 상태 갱신만을 위해 새 SHA를 다시 current 필드에 박는 연쇄 Sync를 만들지 않는다.

## 3. 문서 상태

| 상태 | 의미 | 신규 기획·구현 사용 |
|---|---|---|
| `[현행]` | 현재 주제의 책임 원본 | 허용 |
| `[대체됨]` | 후속 문서가 권위를 승계 | 금지, 역사 근거만 허용 |
| `[보류]` | 기존 승인은 있으나 최신 정본과 재검증 필요 | 금지 |
| `[폐기]` | 채택하지 않았거나 명시 철회 | 금지 |
| `[증거]` | 과거 PR·검증·실험 결과 | 사실 증거로만 허용 |

`APPROVED`라는 파일명이나 과거 `MAIN_CANONICAL` YAML은 `DOCUMENT_LIFECYCLE_REGISTRY.md`의 최신 상태보다 우선하지 않는다.

## 4. 우선순위

```text
사용자의 최신 지시
→ PROJECT_CORE.md
→ DOCUMENTATION_MAP.md
→ DOCUMENT_LIFECYCLE_REGISTRY.md
→ 주제별 [현행] 책임 원본
→ [증거]
→ [대체됨]·[보류]·[폐기]
```

## 5. 구형 문서 처리

- 직접 충돌하고 후속 정본이 존재하면 `[대체됨]`.
- 유효할 가능성이 있으나 최신 전투·HUD·경제·아트와 재조정되지 않았으면 `[보류]`.
- 채택되지 않은 제안·철회 가정이면 `[폐기]`.
- 삭제 대신 상태·승계 문서를 남겨 Git 이력과 결정 근거를 보존한다.

## 6. 자동 검증

문서 CI는 다음을 실패로 처리한다.

- `ACTIVE_CONTEXT.md`의 고정 `current_main` 또는 고정 `context_baseline_commit`.
- 문서 수명주기 레지스트리 누락.
- 구형 master GDD에 `[대체됨]` 표식 누락.
- `PROJECT_CORE.md`에 `storage_selling_food` 같은 폐기된 식량 코어 계약 재유입.

## 7. 경계

```text
PRODUCT_CODE = UNCHANGED
RUNTIME = NOT_RUN
SIMULATION = NOT_RUN
HUMAN_QA = NOT_RUN
```
