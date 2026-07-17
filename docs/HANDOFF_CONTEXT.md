# OMENWARD 프로젝트 인수인계 컨텍스트

- 갱신일: 2026-07-17
- 현재 상태: **Godot 4.7.1 수직 슬라이스 구현·자동 기준선 통과 / 1920×1080·1280×720 수동 QA 대기**
- 다음 작업: `docs/work_orders/0002-current-main-audit-and-next-iteration-plan-mode.md`

이 문서는 본책 내용을 복제하지 않는 인수인계 라우터다. 새 작업자는 아래 순서로 실제 상태를 확인한다.

## 최초 읽기 순서

1. 최신 사용자 지시와 `AGENTS.md`
2. `docs/BASE_RULES_VERSION.md`
3. `docs/DOCUMENTATION_MAP.md`
4. 영향 분야의 다섯 본책
   - `docs/planning/01_GAME_DESIGN.md`
   - `docs/planning/02_PROGRAMMING_MVP_ROADMAP.md`
   - `docs/planning/03_ART_DIRECTION.md`
   - `docs/planning/04_SOUND_DIRECTION.md`
   - `docs/planning/05_QA_PM_PLAN.md`
5. 관련 `docs/design/APPROVED_*.md` 상세 부록
6. 현재 Issue·Goal·Work Order와 실제 파일·테스트
7. `docs/ACTIVE_CONTEXT.md`

## 현재 핵심

- 게임 약속: 건물로 룰렛 확률과 증원을 설계하고 예고된 공세를 세 전선에서 뒤집는다.
- 전장: 상·중·하 독립 3라인, 라인별 성문·중간거점·접전지, 총 4개 우회로, 미니맵 없음.
- 데이터: 공용 UnitArchetype 10개와 진영별 Visual Set을 분리하며 적군 전용 전투 데이터 복제를 금지한다.
- 구현: `project.godot`, Scene, GDScript, 데이터, headless 테스트와 플레이 가능한 수직 슬라이스가 존재한다.
- 자동 검증: headless 6종, editor import, runtime smoke 통과 기준선을 유지한다.
- 미검증: 1920×1080·1280×720 수동 플레이·가독성, 최종 밸런스, 최종 아트·오디오.
- 공식 캐릭터명: **벨루/Bellu**. 이미지의 `율비/Yulbi`는 폐기된 표기다.

## 최신 시각자료

- 전장 인게임 기준: `docs/images/current/battlefield-ingame-reference.png`
- 룰렛·벨루 UI 기준: `docs/images/current/roulette-bellu-ui-reference.png`
- 벨루 외형·표정 기준: `docs/images/current/bellu-character-reference.png`
- 해석·출처·권리: `docs/images/VISUAL_REFERENCE_INDEX.md`

이미지의 임시 수치·문구·토폴로지는 승인된 시스템 계약이 아니다. 전장 구조는 게임 본책과 `APPROVED_BATTLEFIELD_TOPOLOGY_AND_SCALE_V1.md`가 우선한다.

## 작업 종료 조건

- 영향 분야와 관련 본책을 갱신했다.
- 자동·수동 검증 결과와 미검증 항목을 구분했다.
- 최신 이미지·음원의 출처·권리·교체 상태를 기록했다.
- Handoff와 Active Context에는 현재 상태·다음 순서만 반영했다.
- Base 승격 후보 여부와 남은 위험을 보고했다.
