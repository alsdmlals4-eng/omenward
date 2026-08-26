# Omenward Skill 공통 실행 계약

모든 `skills/**/SKILL.md`는 이 계약을 상속한다. 개별 Skill은 프로젝트 고유 판단만 정의하며 Base 공용 절차를 복제하지 않는다.

## 우선순위

1. 사용자의 최신 지시
2. OMENWARD `AGENTS.md`와 승인된 Decision / Active Context / 작업계약
3. 프로젝트 구조화 정본과 실제 코드·데이터·Scene·Resource·테스트·runtime evidence
4. Project Notion Home과 관련 human-facing owner
5. fresh Base current authority — latest completed Base main의 root `AGENTS.md`와 trigger가 맞는 current owner/Skill
6. 날짜·버전이 확인된 외부 참고 자료

Skill은 프로젝트 정본을 덮어쓰는 권한이 없다. `docs/BASE_RULES_VERSION.md`의 과거 release pin이나 `PROJECT_SKILL_SNAPSHOT.json`을 fresh Base current authority 대신 사용하지 않는다.

## Workspace authority

```text
NOTION = CURRENT_HUMAN_FACING_CANON
GITHUB_REPOSITORY_AND_ACTUAL_RUNTIME = STRUCTURED_RUNTIME_AUTHORITY
Google Sheet = COMPATIBILITY_ONLY_MIGRATION_SOURCE
```

GitHub와 Notion이 현재 의미에서 충돌하면 material mutation 전에 `CONTEXT_DRIFT_RECHECK_REQUIRED`로 되돌린다.

## Work Mode

- `PLAN`: 읽기·분석·제안만 수행한다. 제품 코드·Scene·Resource·데이터를 수정하지 않는다.
- `BUILD`: 승인된 범위만 최소 변경으로 구현한다.
- `REVIEW`: 증거를 수집하고 병합 가능 여부를 판정한다. 명백한 결함 수정은 승인 범위 안에서만 수행한다.

실제 Godot 제품 구현은 current Base 역할 경계에 따라 Codex Godot 제품 구현 handoff로 넘기며, GPT가 PowerShell로 local Codex를 실행하지 않는다.

## 자동 라우팅

1. fresh Base `skills/SKILL_REGISTRY.json` 전체를 inventory하고 current Goal trigger와 negative trigger를 대조한다.
2. OMENWARD `skills/SKILL_REGISTRY.json`의 project-local route를 함께 읽는다.
3. 필요한 Base owner만 progressive-load하며 모든 Skill을 무조건 읽거나 실행하지 않는다.
4. 같은 산출물을 둘 이상의 Skill이 동시에 소유하지 않는다.
5. project-local route와 Base shared route가 같은 이름으로 충돌하면 project-local 의미를 우선한다.
6. `PROJECT_SKILL_SNAPSHOT.json`은 historical/compatibility evidence이며 current Base Skill count를 고정하지 않는다.
7. REVIEW에는 실제 변경 검증과 canonical freshness owner를 current Base Registry에서 resolve한다.
8. 읽은 Skill과 실제 실행한 Skill을 완료 보고에서 구분한다.

## 공통 실행 순서

1. 요청을 목표·범위·제외 범위·완료 기준으로 정규화한다.
2. Base latest completed main + OMENWARD GitHub + Project Notion을 fresh-read하고 entry-state를 대조한다.
3. 책임 원본과 실제 파일·consumer·증거를 찾는다.
4. 변경 지도와 보호 경로를 만든다.
5. 선택된 Skill의 고유 절차를 수행한다.
6. 코드·정책·계약 변경은 RED→GREEN 증거를 남긴다.
7. 최소 5회 full-scope adversarial review를 수행하고 유효 finding을 최소 교정한다.
8. 독립 검증, exact-head PR gate, merge/readback이 적용되는 범위면 끝까지 닫는다.
9. 실행·미실행·잔여 위험을 분리해 보고한다.

## 심각도

- `P0`: 데이터 손실, 정본 파괴, 보안·권한 우회, 빌드 불가, 핵심 규칙 반전
- `P1`: 주요 기능 오동작, 잘못된 병합 판정, 반복 가능한 누락·중복
- `P2`: 제한된 경로의 오류, 유지보수 위험, 검증 공백
- `P3`: 표현·정리·후속 개선

## 증거 등급

- `PROVEN`: 요구된 자동 검사와 실제 실행 또는 독립된 근거가 일치
- `PARTIAL`: 일부 검사만 완료
- `NOT_RUN`: 실행하지 않음
- `FAILED`: 검사 실패
- `BLOCKED`: 선행 조건이 없어 실행 불가

문서에 테스트 이름이나 asset 경로가 존재한다는 사실은 runtime/player evidence가 아니다.

## 완료 보고

- 선택한 Work Mode와 Skill
- 변경 파일과 이유
- RED/GREEN 또는 acceptance evidence
- adversarial review finding과 교정
- 실행한 검증과 결과
- GitHub/Notion readback 상태
- 미검증 항목
- 잔여 위험과 다음 작업
