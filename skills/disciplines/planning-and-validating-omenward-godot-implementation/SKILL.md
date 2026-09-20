---
name: planning-and-validating-omenward-godot-implementation
description: Use when implementing OMENWARD Godot behavior, scenes, persistence, deterministic systems or runtime tests.
---

# OMENWARD Godot Implementation

현재 ID: `omenward-godot`; 역사 호환 ID: `discipline.omenward-godot`.
[공통 계약](../../SHARED_EXECUTION_CONTRACT.md)을 따른다.

## 사용 조건
Godot 코드·씬·런타임 데이터·저장/로드·결정론·성능 변경.
## 사용하지 않는 조건
기획만 논의하거나 운영 문서만 고치는 작업.
## 고유 책임
현재 승인 규칙과 실제 엔진 경계·consumer·실행 증거를 일치시킨다.
## 입력
현재 승인 Spec, 실제 project.godot/코드/씬/데이터, 기존 테스트·저장 format과 compatibility.
## 절차
1. 편집기·실행 대상 프로젝트와 채택 엔진을 확인한다. 전역 설정·플러그인을 자동 변경하지 않는다.
2. 변경 동작의 입력·상태·실패 경계를 테스트로 재현하고 최소 구현 후 회귀한다. 순수 문구/운영 변경에 게임 실행 의무를 붙이지 않는다.
3. 저장 검사는 별도 test 저장 루트/slot을 사용한다. 기존 저장 및 알 수 없는 미래 format을 덮지 않고 migration은 별도 승인 범위에서 검증한다.
4. UI/모션은 domain 상태를 표시하고 의도를 전달한다. 장식 완료·중복 이벤트가 피해/구매/보상을 재실행하지 않도록 한다.
5. 플레이어-facing 변경이면 [재미 검증 연결](../../../docs/BASE_RULES_VERSION.md#재미-검증의-프로젝트-연결)의 기능 ID→consumer→검증을 양방향 확인한다.
6. 자동·헤드리스·실제 실행/입력·화면·기기·사람을 분리한다. 보호 검사 실패는 우회하지 않고 승인 scope와 원인을 분리한다.
## 출력
기존 작업 기록에 코드/씬·데이터 경계·검사 결과·저장 호환성·미실행·복구 경로를 연결한다.
## 고유 검수
실사용 저장 오염, 승인 없는 엔진/규칙 변경, 비결정적 결과, 끊긴 consumer, 다른 PR 변경을 완료 처리하지 않는다. 실행하지 않은 Godot/사람 증거는 NOT_RUN이다.
