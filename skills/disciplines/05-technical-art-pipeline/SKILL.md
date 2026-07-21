# Omenward Technical Art Pipeline

- Skill ID: `discipline.technical-art`
- 공통 계약: `skills/SHARED_EXECUTION_CONTRACT.md`

## 사용 조건

리소스 임포트·스프라이트·애니메이션·렌더 규격과 아트 프롬프트의 기술 제약을 관리할 때.

## 사용하지 않는 조건

순수 세계관 문구 또는 게임 수치 작업.

## 고유 책임

공용 AnimationContract·피벗·프레임·판정 이벤트와 자산 출처·해시·교체 상태를 파이프라인 전반에서 보존한다.

## 입력

- Asset Registry·승인 이미지
- 엔진 임포트·렌더 설정
- 스프라이트·애니메이션 계약
- 목표 플랫폼·아트 프롬프트

## 절차

- Modes: `asset-pipeline → import → animation-contract → art-prompt-technical → render-validation`
- 자산 ID·경로·출처·승인 상태를 확인한다.
- 아군·적군 시트의 상태·프레임·피벗·이벤트 호환성을 검사한다.
- 생성 프롬프트에 출력 규격·카메라·조명·후처리 제약을 명시한다.
- 임포트 결과와 실제 렌더를 검증한다.

## 출력

- 자산·임포트 계약
- 애니메이션 호환성
- 기술 프롬프트·기법 카드 제약
- 렌더 검증·교체 목록

## 고유 검수

- 임시 자산을 승인 완료로 표시하지 않는다.
- 이미지 임시 수치를 기획값으로 해석하지 않는다.
- 실제 임포트·렌더 없이 파이프라인 통과를 주장하지 않는다.
