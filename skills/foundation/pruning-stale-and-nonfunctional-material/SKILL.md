# Pruning Stale and Nonfunctional Material

- Skill ID: `foundation.pruning`
- 공통 계약: `skills/SHARED_EXECUTION_CONTRACT.md`

## 사용 조건

중복·죽은 자료·오래된 경로·행동 중립 부피를 고유 기능 손실 없이 정리할 때.

## 사용하지 않는 조건

소비자·고유 기능·승인·롤백을 확인하지 못한 상태에서 파일 수만 줄일 때.

## 고유 책임

KEEP·MERGE·MOVE_TO_REFERENCE·STUB·ARCHIVE·DELETE·UNVERIFIED 판정으로 고유 기능·근거·호환성을 보존한다.

## 입력

- Registry·entrypoint
- 정본·소비자·생성 경로
- 고유 기능·증거
- 호환성·역사·승인·롤백

## 절차

- Modes: `inventory → classify → preserve-unique → prune-approved → verify-no-loss`
- 중복·도달 불가·오래된 ID·기본 읽기 혼입을 찾는다.
- 삭제 전에 고유 입력·출력·검증·참조·호환성을 추출한다.
- 가장 안전한 병합·reference·stub·archive·삭제를 선택한다.
- 승인이 필요한 삭제는 보류한다.
- Registry·링크·라우팅·테스트·콜드 스타트를 재검증한다.

## 출력

- 후보·사용 근거
- 처리 판정
- 보존 기능·근거·호환성
- 제거·축소량
- 회귀·롤백

## 고유 검수

- 사용 흔적이 없다는 이유만으로 자동 삭제하지 않는다.
- 테스트·문서만 지워 결함을 숨기지 않는다.
- 고유 기능을 병합 중 잃지 않는다.
