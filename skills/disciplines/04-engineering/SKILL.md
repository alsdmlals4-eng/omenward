# Omenward Engineering

- Skill ID: `discipline.engineering`
- 공통 계약: `skills/SHARED_EXECUTION_CONTRACT.md`

## 사용 조건

Godot·GDScript·데이터·저장·성능 구현 또는 런타임 오류를 진단할 때.

## 사용하지 않는 조건

구현과 무관한 순수 기획 문구 작업.

## 고유 책임

Godot 4.7.1, 상태 단일 소유, 공용 10병종 데이터와 승인된 Scene·Signal·저장 계약을 유지하며 최소 수정한다.

## 입력

- 엔진·플랫폼·빌드
- 재현 절차·로그·최근 diff
- Scene·Node·Signal·데이터 흐름
- 승인 계약·baseline 테스트

## 절차

- Modes: `architecture → implementation → data-schema → runtime-diagnosis → performance → save-compatibility`
- 실제 호출·상태·데이터 소유를 확인한다.
- 런타임 오류는 같은 조건에서 재현하고 원인 가설을 반증한다.
- Scene·Node·Signal·Resource·데이터 연결을 좁힌다.
- 가장 작은 수정으로 원인을 제거한다.
- 정상·실패·경계·저장·플랫폼·인접 경로를 재검증한다.

## 출력

- 구현·영향 범위
- 재현·원인·반증
- 최소 수정
- 성능·저장·호환성 결과
- 재발 방지 테스트

## 고유 검수

- 재현 없이 대규모 추측 수정하지 않는다.
- EnemyUnitProfile 등 승인되지 않은 데이터 분기를 만들지 않는다.
- 오류 메시지만 숨기거나 수정 후 재검증을 생략하지 않는다.
