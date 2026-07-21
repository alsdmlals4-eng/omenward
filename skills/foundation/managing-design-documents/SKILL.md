# Managing Design Documents

- Skill ID: `foundation.design-documents`
- 공통 계약: `skills/SHARED_EXECUTION_CONTRACT.md`

## 사용 조건

등록된 책임 원본·발행본·사용자 학습 노트·정본 연결형 대시보드를 작성하거나 갱신할 때.

## 사용하지 않는 조건

문서 상태와 무관한 코드 수정 또는 단순 조회.

## 고유 책임

한 질문에 하나의 Markdown/JSON 정본을 유지하고, 조건부 PDF 발행·학습 노트·시각 대시보드를 정본과 분리해 관리한다.

## 입력

- 문서 Registry와 발행 정책
- 승인된 결정·실제 상태·출처
- 독자·용도·갱신 조건
- 기존 파생본·Manifest

## 절차

- Modes: `author → update → restructure → publish → validate → learning-note → visual-dashboard`
- 책임 질문과 단일 정본을 확인한다.
- 서술은 Markdown, ID·상태·경로는 JSON으로 둔다.
- 중복 전문 대신 경로와 현재 차이만 연결한다.
- 학습 노트는 AI 지침이 아니라 개념·이유·예시·오해·연습으로 만든다.
- 대시보드는 정본을 대체하지 않고 원본 경로·갱신 시점을 표시한다.
- 정책이 요구할 때만 PDF·Manifest를 생성하고 최신성을 검증한다.

## 출력

- 갱신된 정본
- 선택적 PDF·Manifest
- 사용자 학습 노트
- 정본 연결형 대시보드
- 발행·미검증 상태

## 고유 검수

- v2·final·latest 활성 복제본을 만들지 않는다.
- CURRENT와 사람 시각 검수를 혼동하지 않는다.
- 대시보드·학습 노트가 정본이나 AI 실행 계약을 대체하지 않는다.
