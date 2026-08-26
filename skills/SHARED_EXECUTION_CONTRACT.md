# Omenward Skill 공통 실행 계약

모든 `skills/**/SKILL.md`는 이 계약을 상속한다. 개별 Skill은 고유 판단만 정의하며 공통 안전·검증 규칙을 반복하지 않는다.

## 우선순위

1. 사용자의 최신 지시
2. 승인된 Plan·Issue·Goal
3. `AGENTS.md`와 프로젝트 책임 원본
4. 실제 코드·데이터·Scene·실행 증거
5. fresh Base latest completed main의 `AGENTS.md`와 현재 trigger가 요구하는 Base owner
6. 외부 참고 자료

`docs/BASE_RULES_VERSION.md`는 과거 project adoption 증거이며 current Base 행동 정본이 아니다. Skill은 프로젝트 정본을 덮어쓰는 권한이 없다.

## Work Mode

- `PLAN`: 읽기·분석·제안만 수행한다. 제품 코드·Scene·Resource·데이터를 수정하지 않는다.
- `BUILD`: 승인된 범위만 최소 변경으로 구현한다.
- `REVIEW`: 증거를 수집하고 병합 가능 여부를 판정한다. 명백한 결함 수정은 승인 범위 안에서만 수행한다.

모드가 불명확하면 `PLAN`으로 시작한다. 실제 Godot 제품 구현의 owner 분류는 current Base 역할 계약과 프로젝트 `AGENTS.md`를 따른다.

## 자동 라우팅

1. `routing.always_on`은 비워 두고 요청의 trigger와 실행 stage로만 Skill을 선택한다.
2. `foundation.project-intake`는 요청이 직접 일치하거나 선택된 Skill의 dependency일 때만 포함한다.
3. 주 책임 Omenward Discipline은 최대 1개, 지원 Discipline은 최대 1개다.
4. Specialist는 명시적 trigger 또는 REVIEW stage 계약이 있을 때만 선택한다.
5. `REVIEW`에는 current Base validation/freshness trigger에 맞는 검증 Skill을 추가한다.
6. 같은 산출물을 둘 이상의 Skill이 동시에 소유하지 않는다. 주 책임 Skill이 편집하고 지원 Skill은 검토만 한다.
7. 사용자가 Skill을 직접 지정하면 current Registry의 활성 ID 또는 등록된 compatibility alias만 허용한다.
8. `inactive` 패키지는 과거 기록으로만 유지하며 Router가 직접 선택하지 않는다.
9. Base active Skill 개수나 이름을 이 파일에 고정하지 않고 current Registry에서 발견한다.

## 공통 실행 순서

1. 요청을 목표·범위·제외 범위·완료 기준으로 정규화한다.
2. 책임 원본과 실제 파일을 찾는다.
3. 변경 지도와 보호 경로를 만든다.
4. 선택된 Skill의 고유 절차를 수행한다.
5. `Adversarial Review`로 숨은 가정, 누락, 중복, 잘못된 완료 주장을 찾는다.
6. `Red Teaming`으로 실패 경로, 권한 우회, 오래된 파일, 부분 적용을 공격한다.
7. L1 이상 retained change/review는 current Base `running-adversarial-review-and-refinement`에 따라 **최소 5회 full-scope loop**를 수행하고 이후 clean까지 계속한다. 유효 finding을 고쳤으면 수정된 전체 상태를 다시 공격한다.
8. 독립된 검증으로 결과를 확인한다.
9. 실행·미실행·잔여 위험을 분리해 보고한다.

더 구체적인 사용자 지시 또는 current Base owner가 더 엄격한 게이트를 요구하면 그것이 우선한다.

## Workspace authority

```text
NOTION = CURRENT_HUMAN_FACING_CANON
REPOSITORY = CURRENT_STRUCTURED_RUNTIME_CANON
GOOGLE_SHEETS = COMPATIBILITY_ONLY_MIGRATION_SOURCE
```

Sheet의 역사 자료가 존재해도 신규 기본 입력면이나 active sync authority로 승격하지 않는다.

## 심각도

- `P0`: 데이터 손실, 정본 파괴, 보안·권한 우회, 빌드 불가, 핵심 규칙 반전
- `P1`: 주요 기능 오동작, 잘못된 병합 판정, 반복 가능한 누락·중복
- `P2`: 제한된 경로의 오류, 유지보수 위험, 검증 공백
- `P3`: 표현·정리·후속 개선

## 증거 등급

- `PROVEN`: 자동 검사와 실제 실행 또는 독립된 근거가 일치
- `PARTIAL`: 일부 검사만 완료
- `NOT_RUN`: 실행하지 않음
- `FAILED`: 검사 실패
- `BLOCKED`: 선행 조건이 없어 실행 불가

문서에 테스트 이름이 존재한다는 사실은 `PROVEN`이 아니다.

## 완료 보고

- 선택한 Work Mode와 Skill
- 변경 파일과 이유
- Adversarial Review·Red Teaming에서 발견한 문제
- 실제 full-loop 검토와 수정 회차
- 실행한 검증과 결과
- 미검증 항목
- 잔여 위험과 병합 판정
