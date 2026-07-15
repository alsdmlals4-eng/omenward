# 승인된 오멘워드 프리프로덕션 PoC 통합 기준 V1

- 상태: **11단계 구조 초안 완료 / 세부 수치는 플레이테스트 조정 대상 / 구현 미승인**
- 작성일: 2026-07-16

사용자 결정에 따라 세부 밸런스는 첫 PoC 가설로 두고, 구현이 뒤집히지 않도록 역할·상태·데이터·검증 경계를 11단계까지 먼저 고정한다.

## 완료된 11단계

1. 공통 전투 계산식과 Tier·등급 예산.
2. 기본 병영 6종 생산·T3·등급 능력 계보.
3. 특수병단 4종 생산·T3·등급 능력 계보.
4. 룰렛 가중치·목표 확률·럭키·금화 기대값.
5. 적군 대칭 10병종.
6. 1~15웨이브 편성과 전설 보스.
7. 16~20웨이브 초과전과 신화 보스.
8. 건물 Tier 3·전술 명령·용병.
9. 튜토리얼·약 3시간 캠페인·절차 생성.
10. HUD·아트·오디오 제작 계약.
11. 성능 예산·데이터 구조·테스트·Plan Mode 진입 조건.

## 책임 문서

- `docs/design/APPROVED_COMMON_COMBAT_AND_RANK_BUDGET_POC_V1.md`
- `docs/design/APPROVED_PLAYER_TEN_UNIT_LINEAGES_POC_V1.md`
- `docs/design/APPROVED_ROULETTE_PROBABILITY_TARGETS_POC_V1.md`
- `docs/design/APPROVED_ENEMY_TEN_UNIT_AND_WAVE_1_20_POC_V1.md`
- `docs/design/APPROVED_BUILDINGS_TACTICAL_MERCENARY_POC_V1.md`
- `docs/design/APPROVED_TUTORIAL_CAMPAIGN_PROCEDURAL_POC_V1.md`
- `docs/design/APPROVED_UI_ART_AUDIO_POC_BIBLE_V1.md`
- `docs/design/APPROVED_ART_DIRECTION_AND_PRODUCTION_GUIDE_V1.md`
- `docs/design/APPROVED_PERFORMANCE_DATA_TEST_READINESS_POC_V1.md`

기존 책임 문서 중 다음은 계속 우선 적용한다.

- 세계관·명칭.
- 벨루 단일 안내자.
- 전장 토폴로지와 스케일.
- 특수병단 최대 50% 준비 할인과 V5 경제.
- 정규 스테이지 경제 V1.
- 60초 공세 시계와 5·10·15·20 이정표.
- 아트는 `클린 전술 픽셀 + 미니어처 치비 비율 + 고해상도 픽셀 완성도`를 기본 제작 규격으로 사용한다.

## 수치 상태

다음은 구조 승인과 동시에 첫 구현 시작값으로 사용할 수 있지만 플레이테스트에서 조정한다.

- HP·공격력·방어·사거리·쿨다운.
- 생산시간·식량·Threat.
- 건물 T3 비용.
- 룰렛 릴 가중치와 목표 분포.
- 웨이브 수량과 예산.
- 전술 명령 피해·지속.
- 시장·농장·포탑 T2·T3 효과.
- 성능 상한과 갱신 주기.
- 최종 픽셀 팔레트·스프라이트 프레임·캔버스 크기.

## 변경 규칙

- 병종 삭제·통합·건물 계열 변경은 사용자 승인 대상이다.
- 수치 조정은 플레이테스트 근거가 있으면 같은 구조 안에서 변경할 수 있다.
- 이름·외형은 역할·실루엣 계약을 훼손하지 않는 범위에서 교체할 수 있다.
- 아트 변경은 40px 유닛·128px 건물 축소 가독성 기준을 통과해야 한다.
- 플레이어 등급은 일반·엘리트·영웅·전설을 유지한다.
- 적 신화급은 20웨이브 전용이다.
- 구현은 별도 Codex Plan Mode 제안서와 사용자 승인 전 시작하지 않는다.

## 남은 프리프로덕션 작업

- 실제 확률 시뮬레이션과 전투 표 계산.
- 승인된 아트 규격에 따른 실제 스프라이트·아이콘 제작.
- 최종 팔레트·캔버스 크기·방향 수 결정.
- 벨루 영문 철자·성우·표정 원화 확정.
- 적군·영웅·전설의 최종 고유명.
- 정확한 Godot 버전과 폴더 구조 선택.
- 구현 Plan Mode 제안서.

이후 작업은 새로운 구조를 추가하기보다 이 기준의 수치·이름·아트 품질을 검증하고 다듬는 단계다.
