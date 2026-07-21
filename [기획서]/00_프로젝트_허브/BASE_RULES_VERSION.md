# Base 적용 기준

## Canonical baseline

- Base repository: `alsdmlals4-eng/Base`
- 고정 branch: `main`
- 고정 commit: `ee265576da7f67d3278f8099dd97d4e714ef0651`
- 적용 날짜: 2026-07-21
- 전수 감사: `docs/base/BASE_SYNC_AUDIT_2026-07-21.md`

일상 작업은 이 고정 commit과 Omenward 로컬 분화본을 기준으로 한다. Base 원격의 이후 변경을 암묵적으로 적용하지 않는다.

## Applied contracts

- PLAN·BUILD·REVIEW Work Mode 분리
- trigger 기반 자동 Skill 선택과 실행 보고
- Foundation·Specialist·분야 Skill의 최소 로딩
- 기존 프로젝트 audit→승인→reconcile/migrate→verify
- Markdown/JSON 단일 책임 원본과 정책 기반 발행
- 정본·경로·ID·Schema·생성기 변경의 reference-freshness 감사
- 변경 계약·정적·런타임·접근성·성능·회귀·증거 통합 검증
- Legacy Alias와 구형 산출물 처리표
- Skill Registry와 실제 패키지 1:1 무결성 검사

## Omenward adaptation

Omenward에는 실제 책임이 있는 11개 분야 본책·분야 Skill을 모두 `selected_disciplines`로 유지한다. Base 공용 13개 활성 Skill은 Omenward 경로·게이트에 맞춘 13개 로컬 Foundation/Specialist 어댑터로 설치한다.

## Preserved non-canonical extension

Base PR #18의 `d2457e75a856260d309203e20262f2a2142d2dd6`와 `skills/PRODUCTIVITY_SOURCE_MANIFEST.json`은 현재 Base main에 존재하지 않는다.

- 삭제하지 않고 `SKILL_REGISTRY.json > legacy_extensions`에 기록
- 현재 Base main의 활성 규칙으로 주장하지 않음
- 프로젝트 Registry 자동 라우팅에서 비활성
- 전역 handoff/resume-work는 실행 환경 기능으로만 사용 가능
- 향후 사용자 결정 없이 로컬 복사·활성화하지 않음

## Update rule

Base 갱신 전에는 다음을 수행한다.

1. 새 main commit과 이 고정 commit 비교
2. 파일별 적용·비적용·대체·충돌·보존 판정
3. Registry·Skill·문서·테스트·파생본 영향 지도
4. 사용자 승인
5. 별도 PR에서 적용
6. reference-freshness·패키지 무결성·콜드 스타트 검수
