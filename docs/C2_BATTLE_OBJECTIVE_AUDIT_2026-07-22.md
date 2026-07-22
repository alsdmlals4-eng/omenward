# C2 전투 목적 루프 감사·복구 기록

- 기준 main: `227f6678839d32b8ec3d0f109664bcb63356fe08`
- 작업 상태: `C2_BATTLE_OBJECTIVE_REMOTE_PROVEN`
- 프로젝트 코어: `CORE_CONFIRMED / CORE_LOCKED`
- 선행 완료: `C1_ROULETTE_CORE_REMOTE_PROVEN`
- 별도 결정 게이트: `C1U_PENDING_USER_DECISION`

## 1. 적용 Skill

- `foundation.project-intake` — 범위·보호 대상·중단 조건 고정.
- `foundation.project-core` — 예측→확률 설계→전선 커밋의 결과 인과 보호.
- `foundation.pruning` — C1 완료 뒤 구형 현재 상태·실행 입력 참조 제거.
- `discipline.game-design` — 접전지·거점·성문·본진·승패 계약 대조.
- `discipline.engineering` — 상태 소유·고정 틱·결정론·경제 연결.
- `discipline.qa` — 점령·교착·성문·본진·경제·건물·라인 격리 회귀.
- `foundation.adversarial-review` — 유닛 공격 우회 테스트·영구 교착·유령 건물·허위 승패 공격.
- `foundation.validation-review`, `discipline.integration-review` — 정본·코드·테스트·문서·PR 일치.

## 2. 기계 감사

저장소 텍스트 248개를 조사했다.

- 전투 목적 관련 파일: 88개.
- 구형 현재 상태 후보: 4개.
- 깨진 내부 Markdown 링크: 0개.
- 본진·승리·패배 문맥: 177개.

실제 활성 문제는 C1 진행 중·PR #49 대기·C2 미구현 표현이었으며, Validator·mutation fixture의 구형 문자열은 공격 입력으로 분리했다. 임시 감사 입력과 수집 Workflow는 제거했다.

## 3. 복구한 인과

```text
3라인 교전
→ 접전지 점령 또는 교착
→ 적 중간거점 점령
→ 건설권·생산 효과·경제 전환
→ 같은 라인 성문 공성
→ 적 본진 파괴 또는 W15 전설 보스 처치
→ 자연 승리·패배
```

## 4. 핵심 구현

- 중앙 접전지 3개, 양측 중간거점 6개, 성문 6개, 본진 2개를 `BattleSimulator`가 소유한다.
- 유닛은 적이 없을 때 idle이 아니라 같은 라인의 다음 목적 객체로 전진한다.
- 공용 10병종 데이터에 점령력·구조물 피해 태그를 추가하며 적군 복사본을 만들지 않는다.
- 승인 점령력 0.5·1.0·1.25와 상한 2.0을 실수로 보존한다.
- 양 진영이 범위에 있으면 진행·유지·복귀 없이 교착으로 정지한다.
- 양측 이탈 시 안정 접전지의 교착 표시를 해제한다.
- 거점 소유권과 capture revision이 건물 활성·비활성·폐허·재건설과 식량 한도에 반영된다.
- 실제 전투 소유 수가 접전지·중간거점 시간 수입에 전달된다.
- 같은 라인 공성 유닛의 실제 공격 틱이 해당 성문과 본진에 피해를 준다.
- 적 본진 파괴, 아군 본진 파괴, W15 전설 보스 사망이 `StageRun` 결과를 만든다.
- 전투 목적 상태 변화와 결과를 결정론적 input log에 기록한다.

## 5. 적대적 검토로 추가 수정한 사항

1. `BuildingService`의 Variant 비교를 명시적 bool로 고쳐 Godot 경고-오류 정책을 통과시켰다.
2. 안정 중립 접전지에서도 양 진영 동시 도착을 교착으로 표시하도록 했다.
3. 양측 이탈 뒤 안정 접전지의 교착 표시가 영구 잔류하지 않도록 했다.
4. 성문·본진 회귀가 구조물 메서드를 직접 호출해 실제 유닛 공격 경로를 우회하던 문제를 제거했다.
5. 목적 좌표를 넘나드는 고정 틱 overshoot를 clamp했다.
6. 거점 중립화 시 농장 식량 효과를 해제하고 소유권 변경 시 이전 건물을 폐허화했다.

## 6. 가역 기술 fallback

- 본진 독립 방어 수치 미승인: 미지정 시 승인 성문 프로필 재사용.
- 중앙 접전지 별도 점령 시간 미승인: 승인 중간거점 상태기 재사용.
- 정규화 0~100 좌표: 결정론적 테스트 좌표이며 시각 scale 아님.

이 값은 최종 밸런스 확정이 아니며 사용자 결정·플레이테스트 전 교체 가능하다.

## 7. 검증 현황

구현·적대적 보강 단계에서 다음이 통과했다.

- Godot 4.7.1 editor import.
- 모든 `tests/headless/*_test.gd`.
- runtime smoke.
- C1·C2 Python 계약과 mutation tests.
- 프로젝트 코어·Skill Validator·whitespace.

최종 공통 검증은 구현 head `85e2930a839fd210548c7aa2a53125d18c4de875`, GitHub Actions run `29934172758`에서 통과했다. 판정은 `C2_BATTLE_OBJECTIVE_REMOTE_PROVEN`이다.

## 8. 미실행

- 1920×1080·1280×720 사람 플레이.
- 실제 전장 가독성과 목적 상태 표현 QA.
- 10~15분 코어 재미·학습 검증.
- W1~W20 연속 플레이.
- 룰렛 100,000시드·경제·전투 밸런스·성능 계측.
