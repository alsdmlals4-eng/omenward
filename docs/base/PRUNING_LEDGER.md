# Skill 구조 가지치기 처리표

## 유지

- Foundation 7개 기존 책임
- Omenward Discipline 11개
- 공통 실행 계약·Router·Validator·CI
- 모든 Base 25개 기능 책임

## 새 독립 Skill

- `foundation.project-core`
- `foundation.adversarial-review`
- `foundation.pruning`
- `foundation.skill-simplification`
- `foundation.contract-refactor`

독립 권한·입력·산출물·검증 경계가 있어 mode 흡수 시 책임이 흐려지는 항목이다.

## mode로 통합

- GitHub sync·외부 AI worktree → 프로젝트 운영체계
- 장기 작업 continuity → Context/Handoff
- 학습 노트·대시보드 → 문서 관리
- 정본 최신성 → 변경 검증
- 컨셉·Vertical Slice → Game Design
- 11영역 연구 → Analytics/Research
- 아트 프롬프트·UI 감사 → Art·Technical Art·UX/UI
- 런타임 진단 → Engineering·QA

## 제거

기존 `skills/specialists/*` 6개 패키지는 현행 분야 mode와 Alias가 준비된 뒤 삭제한다. 일반 이전 버전은 Git 이력이 보존하므로 활성 백업 복제본을 만들지 않는다.

## 무손실 확인

- Base capability 25/25
- Omenward 분야 11/11
- 과거 Specialist ID 6/6 Alias
- Registry와 실제 패키지 1:1
- Router 대표 시나리오와 변조 테스트
