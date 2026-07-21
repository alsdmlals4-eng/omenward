# Omenward Local Base Operating Model

Source: `alsdmlals4-eng/Base@ee265576da7f67d3278f8099dd97d4e714ef0651`

이 문서는 Base의 최신 운영 모델을 Omenward에 분화한 로컬 실행 원본이다. 원격 Base를 일상 작업마다 암묵적으로 따라가지 않는다.

## Layers

1. 사용자 지시와 승인 계약
2. Omenward AGENTS·Active Context·책임 원본
3. Work Mode와 자동 Skill routing
4. 실제 코드·데이터·자산·테스트
5. 검증·발행·PR·Learning
6. 고정 Base와 공용화 제안

## Work Modes

- PLAN: 사실 조사, 모호성 해소, 분해, 제안, 승인 조건
- BUILD: 승인 범위의 변경과 단계별 검증
- REVIEW: 계약·diff·정본·참조·실행·회귀·미검증 판정

Skill 내부의 `audit`, `verify`, `frame` 같은 mode와 Work Mode는 별도다.

## Skill layers

- Foundation: 요청·운영체계·문서·Context·검증·Base 제안
- Specialist: 컨셉·Vertical Slice·외부 AI·정본 최신성·아트 프롬프트·UI 감사
- Discipline: Omenward의 11개 책임 본책과 구현 라우터

기본 제한은 Foundation 3개, 주 분야 1개다. Specialist는 구체적 trigger가 있을 때만 추가한다.

## Existing project rule

Omenward는 기존 운영 프로젝트다.

```text
audit
→ 보존·참조·위험·목표 구조
→ 사용자 승인
→ reconcile-legacy / migrate
→ verify
```

사용자 승인 전 대량 삭제·이동·통합·강제 개명 금지.

## Canonical and publication rule

- 한 질문에는 등록된 단일 Markdown/JSON 책임 원본
- PDF·DOCX·다이어그램은 파생본
- 발행 정책과 Manifest로 CURRENT 판정
- 변경된 정본의 소비자·참조·테스트·파생본을 추적
- 오래된 ID·경로는 Alias·stub·archive·승인 삭제 중 하나로 판정

## Validation rule

검사는 존재 여부와 실제 실행·강제를 구분한다. `PASS / PARTIAL / FAIL / NOT_RUN`과 증거를 사용한다.

## Learning rule

Learning Log에는 반복 실패·중요 결정·재사용 교훈·실제 검증 결과만 남긴다. 프로젝트 고유 사실과 Base 공용 원리를 분리한다.
