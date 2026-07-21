# Omenward UX UI Accessibility

- Skill ID: `discipline.ux-ui-accessibility`
- 공통 계약: `skills/SHARED_EXECUTION_CONTRACT.md`

## 사용 조건

HUD·조작·가독성·접근성·구현 UI 아트·대시보드 상호작용을 설계·감사할 때.

## 사용하지 않는 조건

UI 영향 없는 서버·데이터 작업.

## 고유 책임

세 라인 위협·거점·성문·웨이브·룰렛 상태를 동시에 이해시키고 실제 입력·정보·시간·모션 장벽과 시각 품질을 검수한다.

## 입력

- 승인 UX 흐름·표시 계약
- 실제 Scene·렌더·입력
- 해상도·플랫폼·접근성 요구
- 아트 방향·사용자 과제

## 절차

- Modes: `ux-flow → hud-layout → accessibility-review → ui-art-audit → dashboard-interaction`
- 핵심 과제와 정보 우선순위를 정한다.
- 960×540 논리 화면과 1920×1080·1280×720에서 가독성을 확인한다.
- 텍스트·대비·정보 채널·입력·시간·모션의 장벽과 대안을 검사한다.
- UI 아트 finding을 A~E 영역으로 분류하고 승인된 항목만 수정한다.
- 실제 전후 렌더와 조작 경로로 재검수한다.

## 출력

- UX 흐름·HUD 계약
- 접근성 장벽·대안
- UI 아트 finding·전후 증거
- 대시보드 상호작용 규칙

## 고유 검수

- 정적 패턴을 자동 결함으로 판정하지 않는다.
- 옵션 존재를 접근성 통과로 보지 않는다.
- 실제 렌더 없이 시각 검수를 완료하지 않는다.
