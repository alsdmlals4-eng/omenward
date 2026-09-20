---
name: governing-omenward-core-design-and-data
description: Use when changing OMENWARD game rules, unit roles, balance or structured game data.
---

# OMENWARD Core Design and Data

현재 등록 ID: `omenward-core-design`; 역사 호환 ID: `discipline.omenward-core-design`.
[공통 계약](../../SHARED_EXECUTION_CONTRACT.md)을 따른다.

## 사용 조건
게임 규칙·병종·성장·경제·밸런스·데이터 계약에 적용한다.
## 사용하지 않는 조건
순수 코드 정리·아트 제작은 해당 전문 스킬로 보낸다.
## 고유 책임
현재 Decision/GDD와 실제 데이터의 의미를 연결한다. 전선 수·건설 방식·수치·기획 단계는 여기서 고정하지 않는다.
## 입력
docs/CURRENT_CONFIRMED_DECISIONS.md → 해당 승인 owner, docs/OMENWARD_GDD_CURRENT_CANON.md, 실제 데이터·consumer·테스트.
## 절차
1. 변경 기능 ID와 경험 원본의 path/section, 입력·상태·규칙·선택·결과·실패 조건을 기존 Spec에 연결한다.
2. [재미 검증 연결](../../../docs/BASE_RULES_VERSION.md#재미-검증의-프로젝트-연결)을 적용해 가설과 반증을 정한다. 기준 없는 수치는 HYPOTHESIS로 둔다.
3. 기존 구현·유효한 조사부터 재사용하고 새 판단만 필요한 공식 자료/벤치마크와 ADOPT/ADAPT/REJECT로 비교한다.
4. 실제 consumer가 없으면 PLANNED, 필요한 사람 경험은 NOT_RUN으로 구분한다. 규칙 효과의 권위와 UI/아트 표현을 분리한다.
## 출력
기존 owner에 규칙·데이터·consumer·성공/실패/중단 기준과 최소 검증·교정 방향을 연결한다. 별도 재미 문서나 스킬을 만들지 않는다.
## 고유 검수
오래된 스킬 예시로 현재 결정을 되돌리거나, 구현 사실만으로 새 규칙을 승인하거나, 데이터와 표현 코드가 규칙을 이중 소유하면 실패다.
