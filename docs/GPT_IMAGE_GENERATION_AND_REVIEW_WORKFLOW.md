# Omenward GPT 이미지 생성·검수 워크플로

- Base: `alsdmlals4-eng/Base@c987647d01ad2baa028a16e03d85ddfc1572a727`
- Sheet: `PROJECT_SHEET_CONFIGURED`
- Mode: `planning-visualization`, `final-visual-candidate`, `visual-qa-and-approval`

## 기획 중
1. 3개 원형 릴과 각 릴 결과·확률·예측 정보 구조.
2. 3개 전선의 위협·보상·유닛 상태·건물 토큰 원천 가독성.
3. 예측 → 선택 → 확정 → 자동전투 → 보상·건설 루프 목업.
4. 유닛·건물·위협·보상의 색·형태·아이콘 언어.
5. 1920×1080·1280×720 실제 HUD 비교.

## 기획 종료
1. Demo 키아트·Steam 캡슐·스크린샷 후보.
2. 릴/전선 HUD 고도화 목업.
3. 유닛·건물·상징·전장 환경 시트.
4. 캠페인 진행·보상·건설 선택 설명 이미지.

상태는 `PLANNED → GENERATED_EXPLORATION → IN_REVIEW → REVISION_REQUIRED/REJECTED/APPROVED_CANDIDATE → PROJECT_ASSET_APPROVED → APPLIED_AND_RUNTIME_VERIFIED`다. 전선 정보가 가려지거나 릴 결과·위협·보상·유닛 상태가 혼동되면 실패다. 특정 IP 유사성·원출처·라이선스·실제 Godot 적용을 검수한다. 생성 이미지는 자동 최종 자산이 아니다.
