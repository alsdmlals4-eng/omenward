# Omenward Analytics and User Research

- Skill ID: `discipline.analytics-research`
- 공통 계약: `skills/SHARED_EXECUTION_CONTRACT.md`

## 사용 조건

시장·벤치마크·SWOT·VRIO·사용자·플레이테스트·튜토리얼·UX·텔레메트리·밸런스·실험·채택 근거를 운영할 때.

오멘워드의 첫 10~15분 코어 루프, C3 정보 UX, 1920×1080·1280×720 가독성 또는 `CORE_LOOP_PROVEN` 승격을 검토할 때는 `docs/CORE_LOOP_HUMAN_PLAYTEST_PROTOCOL.md`를 함께 사용한다.

## 사용하지 않는 조건

근거 없는 인기 목록 또는 단순 수치 계산. 자동 테스트 통과만으로 플레이어 이해·재미·가독성을 증명하는 작업.

## 고유 책임

Games User Research 11영역의 자리·상태·근거를 누락 없이 관리하고 사실·자기보고·행동·실험·해석을 구분한다. 오멘워드 사람 QA에서는 건설→룰렛→배치→3라인 결과→다음 설계의 인과를 플레이어 행동과 설명으로 검증한다.

## 입력

- 결정 질문·대상 집단
- 출처·날짜·버전·표본
- 정확한 브랜치·빌드·StageManifest·seed·알려진 문제
- 과제·행동 이벤트·퍼널·화면 녹화·행동 시각
- 밸런스·실험·채택 결과

## 절차

- Modes: `coverage-11 → market-genre → benchmark → swot-positioning → user-research → playtest-analysis → tutorial-comprehension → ux-analysis → telemetry-funnel → balance-data → hypothesis-experiment → decision-evidence`
- 11영역을 NOT_STARTED·IN_PROGRESS·EVIDENCED·NOT_APPLICABLE로 감사한다.
- 시장·제품 사실·플레이어 자기보고·행동·실험을 분리한다.
- SWOT을 SO·WO·ST·WT 행동으로, VRIO를 가치·희소성·모방 비용·조직화의 지속 우위 판정으로 변환한다.
- 플레이테스트마다 한 가지 우선 가설, 빌드·표본·과제·관찰·통과·중단 규칙을 고정한다.
- 진행자가 정답 건물·룰렛 조작·배치 라인을 유도하지 않는다.
- 오멘워드 코어 루프 결과는 `LOOP_PROVEN`, `UX_GAP`, `RULE_GAP`, `CONTENT_GAP`, `TECHNICAL_BLOCKED`, `NOT_RUN`으로 분류한다.
- 결과를 ADOPT·ADAPT·AVOID·TEST·IGNORE와 유지·수정·삭제·보류 결정에 연결한다.
- 자동 계약 증거와 사람 관찰 증거를 분리하고, 후자가 없으면 `CORE_LOOP_PROVEN`을 사용하지 않는다.

## 출력

- 11영역 coverage matrix
- 출처·표본·한계
- 가설·빌드·seed·과제·관찰 행동·설명 증거
- KPI·이벤트·퍼널
- 밸런스·실험 결과
- 결과 분류와 가장 작은 후속 변경
- 갱신해야 할 정본·상태 문서와 미검증 항목

## 고유 검수

- 빈 섹션을 완료로 보지 않는다.
- 조사하지 않은 결과를 사실로 작성하지 않는다.
- 자기보고와 행동 데이터를 혼동하지 않는다.
- 한 번의 운 좋은 룰렛 결과나 진행자 안내를 코어 루프 증거로 사용하지 않는다.
- 1080p 결과를 720p 가독성 증거로, 자동 회귀를 사람 플레이 증거로 대체하지 않는다.
