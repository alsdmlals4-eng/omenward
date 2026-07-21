# Omenward Shared Skill Execution Contract

모든 `skills/*/*/SKILL.md`에 공통 적용되는 실행 계약이다. 개별 Skill은 고유 책임만 기록하며 이 문서를 반복하지 않는다.

## 우선순위

1. 사용자의 최신 지시
2. Omenward `AGENTS.md`, 승인된 Issue·Plan·프로젝트 코어
3. 등록된 책임 원본과 실제 코드·데이터·자산·테스트
4. `docs/base/SKILL_REGISTRY.json`과 프로젝트에 채택된 Base 기준
5. Base 원격 원본과 외부 참고

Base는 방법의 원본이지 Omenward의 세계관·수치·구현·자산을 덮는 권한이 아니다.

## Work Mode

- `PLAN`: 사실 조사, 요구·코어·구조·순서 제안. 승인 전 제품 변경 금지.
- `BUILD`: 승인 범위만 구현·이주·정리. 단계별 검증과 롤백 유지.
- `REVIEW`: 적대적 검토·반례·증거 판정. 기본 읽기 전용.
- 복합 작업은 `PLAN → BUILD → REVIEW`로 전환한다. 수정 뒤 다시 `REVIEW`한다.

## 자동 라우팅

- `tools/route_skills.py`가 요청을 단계별 Work Mode와 최소 Skill·mode로 선택한다.
- 주 책임 분야는 1개, 지원 분야는 최대 2개다.
- 새 Skill을 만들기 전에 기존 mode 통합을 우선한다.
- REVIEW에는 `foundation.adversarial-review`, `foundation.validation-review`, `discipline.integration-review`를 강제한다.
- 과거 ID는 `skills/LEGACY_SKILL_ALIASES.json`으로만 해석한다.

## 기능 보존과 구조 변경

구조 축소는 다음 순서를 사용한다.

```text
foundation.pruning
→ foundation.skill-simplification
→ foundation.contract-refactor
→ foundation.adversarial-review
→ foundation.validation-review
→ discipline.integration-review
```

삭제·병합 전에 고유 입력·출력·권한·검증·소비자·호환성을 coverage에 연결한다. 파일 수 감소 자체는 성공 기준이 아니다.

## 공통 상태와 증거

- `NOT_RUN`: 실행하지 않음
- `PARTIAL`: 일부만 확인
- `PASSED`: 정의된 검사를 통과
- `FAILED`: 완료 기준 실패
- `UNVERIFIED`: 필요한 입력·환경·근거 없음

문서·테스트·Workflow 파일 존재는 실행 성공이 아니다. CI, 런타임, 렌더, 사람 QA는 서로 다른 증거다.

## 중단 조건

- 프로젝트 코어·승인 문서·실제 구현이 충돌한다.
- 삭제 대상의 고유 기능·소비자·롤백이 확인되지 않는다.
- 필요한 엔진·권한·입력·도구가 없어 결과를 증명할 수 없다.
- Base와 프로젝트 정본이 충돌하며 프로젝트 승인 없이 선택할 수 없다.

중단 시 완료한 결과, 미완료, 원인, 보호 대상, 다음 정확한 행동을 분리한다.

## 실행 보고

L1 이상 작업은 다음을 남긴다.

```yaml
work_mode_sequence:
skills_and_modes:
selection_reason:
work_performed:
result_and_evidence:
status:
not_run:
remaining_risk:
rollback:
```

실제로 실행하지 않은 Skill·검사·렌더·권한을 사용 또는 통과로 보고하지 않는다.
