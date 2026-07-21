# Skill 통합 적대적 검토·개선 기록

## Cycle 1 — 실패 가정

- 최신 Base 25개 중 이전 Omenward에 없는 책임이 누락됐다.
- 모든 Base Skill을 그대로 추가하면 분야 Skill과 중복돼 선택 비용이 커진다.
- Specialist 파일 삭제가 기능·과거 ID·라우팅을 끊을 수 있다.
- 키워드 Router가 REVIEW만 선택하거나 너무 많은 Skill을 선택할 수 있다.

## Cycle 2 — 비판 검증

- 누락 12개 책임은 실제 Registry·coverage에서 확인됐다.
- 프로젝트 분야가 소유하는 전문 기능은 mode 통합이 가능하지만 가지치기·간소화·리팩토링·적대적 검토·코어 권한은 독립 경계가 필요했다.
- 삭제 전 Alias·coverage·mode·회귀가 필요했다.
- 단일 mode Router는 복합 요청에 약해 단계 순서가 필요했다.

## Cycle 3 — 최소 개선

- Base 25개를 Omenward 23개 패키지에 전수 매핑.
- 기존 Specialist 6개를 분야 mode로 흡수하고 Alias 제공.
- stage-aware `PLAN → BUILD → REVIEW` Router로 교체.
- coverage·Alias·Schema·패키지·의존성·대표 요청을 Validator와 테스트로 고정.

## Cycle 4 — Red Team 시나리오

- Base mapping 하나 삭제
- 존재하지 않는 local mode 지정
- 과거 Specialist Alias 삭제
- Specialist 패키지 부활
- 중복 ID·경로·mode·trigger 삽입
- REVIEW 강제 스택 제거
- 의존성 순환
- 일반 요청에서 과도한 분야 선택
- 런타임 오류가 Engineering·QA로 라우팅되지 않음
- 가지치기 요청에서 무손실 검증 단계 누락

## 최종 판정 기준

모든 변조가 실패하고 정상 시나리오가 통과해야 `PROVEN`이다. GitHub Actions 실행 전에는 로컬 결과만 `LOCAL_PROVEN`, Actions 성공 뒤 `REMOTE_PROVEN`으로 기록한다.
