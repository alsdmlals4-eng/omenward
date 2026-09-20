---
name: governing-omenward-art-animation-and-assets
description: Use when creating or connecting OMENWARD images, sprites, animation, VFX or asset imports.
---

# OMENWARD Art, Animation and Assets

현재 ID: `omenward-art-assets`; 역사 호환 ID: `discipline.omenward-art-assets`.
[공통 계약](../../SHARED_EXECUTION_CONTRACT.md)을 따른다.

## 사용 조건
이미지·모션·VFX·임포트·자산 교체.
## 사용하지 않는 조건
규칙만 수정하거나 내부 코드만 정리하는 경우.
## 고유 책임
현재 시각 owner와 실제 소비 크기에 맞는 자산·상태군·모션을 연결한다.
## 입력
현재 Decision의 visual owner, 실제 Scene/Node/Resource consumer, 승인 자산·규격·권리 기록.
## 절차
1. 필요한 시각 정보·경험, 실제 consumer, 표시 크기·방향·pivot·여백·상태군·fallback을 기존 자산 기록에 정한다. consumer가 예정이면 PLANNED다.
2. 재사용 가능성을 확인한 뒤 필요한 raster는 실제 이미지 도구로 제작한다. 투명 오브젝트는 단색 크로마키 배경으로 만든 후 제거한다. 배경 그림 전체를 투명화하는 규칙은 아니다.
3. RGBA alpha·밝고 어두운 배경의 테두리 잔색·잘림·발 접지·프레임 연속성을 확인한다. Aseprite 사용/미사용과 실제 작업·도구를 구분한다.
4. idle/이동/공격/피격 등 필요한 모션과 판정 이벤트를 연결한다. 상태군을 임의 누락하거나 표시 callback이 피해를 재계산하지 않게 한다.
5. 효과·정보의 시점/강도·반복·중단·복귀는 [경험→표현 채택](../../../docs/BASE_RULES_VERSION.md#재미-검증의-프로젝트-연결)을 적용한다. 실제 전장과 UI에 배치해 가독성·연출/판정 일치를 검증한다.
## 출력
기존 manifest에 원본·제작 근거·hash·규격·상태군·consumer·검수 결과를 연결한다. 후보/승인/정본 등록/런타임 연결/화면 검증은 별도 상태다.
## 고유 검수
투명 배경처럼 보이기만 하는 이미지, 손상된 alpha, 모션/판정 불일치, 출처 미확인, 실제 consumer 없는 최종 자산 주장을 통과시키지 않는다. 미실행 화면·사람 검수는 NOT_RUN이다.
