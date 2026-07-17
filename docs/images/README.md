# 오멘워드 시각자료 관리

이 경로는 오멘워드의 승인 이미지, 부분 참고 이미지, 탐색 시안과 시각자료 인덱스를 관리한다.

가장 먼저 읽을 문서:

- `VISUAL_REFERENCE_INDEX.md`
- `../planning/03_ART_DIRECTION.md`
- `../design/APPROVED_UNIT_VISUAL_FORMAT_AND_REFERENCE_USE_V1.md`

## 공식 최신 안정 경로

- `current/battlefield-ingame-reference.png` — 우리 전장 인게임 모습 방향 기준
- `current/roulette-bellu-ui-reference.png` — 룰렛·벨루 UI 방향 기준
- `current/bellu-character-reference.png` — 벨루 외형·표정 기준 (`율비/Yulbi` 표기는 폐기)

공식 이미지는 버전·날짜 접미사 없이 같은 경로를 갱신하고 이전 버전은 Git 이력으로 보존한다.

## 상태 구분

```text
APPROVED_DIRECTION_REFERENCE
PARTIAL_REFERENCE
EXPLORATION
SUPERSEDED_FOR_SPRITE_FORMAT
ARCHIVE_SOURCE
MIGRATION_PENDING
```

이미지 파일만 보고 승인 범위를 추정하지 않는다. `VISUAL_REFERENCE_INDEX.md`에서 참고할 요소와 제외할 요소를 함께 확인한다.

## 현재 핵심 결정

- 병종 이미지는 실제 전장 안에 삽입되는 소형 고해상도 픽셀 월드 스프라이트 형식을 사용한다.
- 과거의 10병종×등급 도감표는 병종 목록과 등급 위계 비교에만 사용하며 실제 스프라이트 형식으로 사용하지 않는다.
- 참고 이미지 안의 임시 수치·문구·맵 연결·미니맵 형태는 현재 책임 기획서를 대체하지 않는다.

## 사용권과 제작

- 프로젝트 자체 생성 시안과 사용자가 제공한 기획 이미지는 방향 확인과 제작 검증에 사용한다.
- 외부 게임의 스크린샷과 타사 자산은 출처·용도와 비복제 범위를 명시한 벤치마킹 자료로만 다룬다.
- 최종 게임 자산은 직접 제작하거나 사용 권한이 확인된 자산으로 교체한다.
- 생성형 원본은 형태 탐색용이며 최종 픽셀 자산은 픽셀 그리드 위에서 정리한다.

## 누락 방지 규칙

사용자가 새 이미지를 제공한 작업은 다음 네 항목이 끝나기 전 완료로 보고하지 않는다.

1. 저장소 원본 또는 변환본 배치.
2. `VISUAL_REFERENCE_INDEX.md` 등록.
3. 아트 본책과 관련 APPROVED 기획서·Work Order 연결.
4. 이전 기준 이미지의 승인·부분 참고·폐기 상태 변경.

바이너리 이동이 끝나지 않았으면 `MIGRATION_PENDING`으로 남기고 완료했다고 표현하지 않는다.
