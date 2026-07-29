# UX·UI·접근성

- Skill ID: `discipline.ux-ui-accessibility`
- Category: `disciplines`
- Registry: `docs/base/SKILL_REGISTRY.json`
- Shared contract: `skills/SHARED_EXECUTION_CONTRACT.md`
- Project source of truth: `docs/UX_UI_SYSTEM.md`
- Base shared skill: `auditing-and-refining-ui-art`

## 사용 조건

- UI·UX·HUD·조작
- 가독성·접근성
- 위협→릴 설계→배치→전투→복기 흐름
- 3라인 정보 우선순위와 포커스

## 사용하지 않는 조건

- 최종 아트 제작
- 위협·릴·배치·전투 수치나 규칙 변경
- 제품 코드·Scene 구현이 요청되지 않은 문서 작업
- HTML 기획 대시보드 제작

## 고유 책임

- 정보 계층
- 상태 피드백
- 조작 계약
- 3라인 위험 우선순위
- 선택 비용·예상 효과·불확실성
- 전투 결과의 인과와 다음 설계 연결

## Base Mode 연결

| 작업 | Base Mode |
|---|---|
| 플레이어 경험과 화면 중심 질문 | `experience-contract` |
| 사용자 여정·3라인 정보 구조 | `flow-and-information-architecture` |
| 공용 패턴 채택·변환 | `pattern-selection` |
| 상태·컴포넌트·피드백 | `design-system-contract` |
| Godot Theme·Control·Signal 경계 | `godot-ui-contract` |
| 입력·포커스·다중 채널 | `accessibility-gate` |
| 실제 플레이 과제와 성공 기준 | `playtest-contract` |
| 구현 화면 검수 | `runtime-ui-audit` |

## 입력

- `docs/UX_UI_SYSTEM.md`
- 승인된 UI·코어 문서
- 실제 HUD·배치 Scene과 상태 소유자
- 최소·목표 해상도
- 키보드·마우스·게임패드 입력 계약

## 절차

1. `docs/UX_UI_SYSTEM.md`의 플레이어 약속과 보호 대상을 먼저 읽는다.
2. 화면별 중심 질문과 첫 시선을 하나씩 고정한다.
3. 위협·비용·범위·불확실성을 실행 전에 확인할 수 있게 한다.
4. 3라인의 시각 순서와 포커스 순서를 일치시킨다.
5. 실패·빈 상태·잠금·취소·복귀를 설계한다.
6. UI는 권위 상태를 재계산하지 않고 사용자 의도만 Signal/Command로 반환한다.
7. 자동·런타임·사람 검증을 분리하고 미실행은 `NOT_RUN` 또는 `HUMAN_NOT_RUN`으로 둔다.
8. 구현 결과가 있으면 A~E 감사와 적대적 검토를 수행한다.

## 출력

- 프로젝트 UX/UI 책임 원본 갱신
- UI 계약과 와이어 구조
- 공용 패턴 `ADOPT / ADAPT / AVOID / TEST / IGNORE` 판정
- Godot 상태 소유·Signal·Theme 계약
- 접근성·입력·포커스 체크
- 런타임·사람 검증 매트릭스

## 고유 검수

- 실제 해상도에서 위협·비용·다음 행동이 읽히는가.
- 조작 대상과 결과가 즉시 구분되는가.
- 3라인 중 가장 위험한 곳이 색 하나 없이도 구분되는가.
- 선택·배치·전투 결과의 인과를 플레이어가 설명할 수 있는가.
- 기존 V2 코어와 전투 규칙이 UX 변경으로 변질되지 않았는가.
