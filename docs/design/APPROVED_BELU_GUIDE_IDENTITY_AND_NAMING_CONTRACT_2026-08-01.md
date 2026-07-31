# 오멘워드 안내자 벨루 정체성·명칭 계약

- 결정 ID: `OMW-DEC-20260801-BELU-IDENTITY-V1`
- 승인 시각: `2026-08-01T05:15:00+09:00`
- 상태: `CURRENT_USER_CONFIRMED_CANON / PLANNING_ONLY`
- 제품 코드 권한: `NONE`
- 에셋 구현·Runtime·사람 검증: `NOT_RUN`

## 1. 최종 결정

사용자가 제공한 `요정 율비 시안.png`의 캐릭터와 기존 문서의 안내자 `벨루`는 **동일 인물**이다.

제품 정본에서 사용하는 최종 이름은 다음으로 통일한다.

```text
CANONICAL_NAME_KO = 벨루
CANONICAL_NAME_EN = Belu
HISTORICAL_ALIAS_KO = 율비
IDENTITY_RELATION = SAME_CHARACTER
```

`율비`는 과거 시안 파일명과 변경 이력을 추적하기 위한 역사 별칭으로만 보존한다. 새 기획서, UI 문구, 대사, 에셋 ID, 파일명, 데이터 키와 구현 식별자에는 `벨루 / Belu`를 사용한다.

## 2. 역할 불변 조건

벨루는 플레이어의 전술 결정을 대신하는 자동 결정자가 아니다.

벨루가 담당할 수 있는 기능:

- 첫 실행과 신규 개념의 짧은 비모달 안내
- 공세·위험 행동·선택 결과의 설명
- 건물→TokenSource→릴→배치→전선 변화의 인과 설명
- 승리·패배·정산의 감정 반응
- 접근성 보조와 선택 근거 제시

벨루가 담당하지 않는 기능:

- 자동 건설·자동 릴 조작·자동 병력 배치
- 최적 선택의 강제
- 숨은 정보 공개
- 공세 정보 변경
- 입력을 장시간 차단하는 모달 튜토리얼 남용

## 3. 시각자료 적용

`요정 율비 시안.png`는 벨루의 현재 사용자 제공 외형 방향 자료로 취급한다.

참고할 것:

- 백색·하늘색·금색의 소형 요정 실루엣
- 위험 경고·결과 반응·짧은 안내에 사용할 수 있는 표정 세트
- 아군 진영의 밝은 시각 언어와의 일치

확정하지 않는 것:

- 최종 픽셀 크기와 애니메이션 프레임 수
- 정확한 의상·장신구·색상값
- 최종 UI 배치와 등장 빈도
- 음성·대사량·표정별 정확한 사용 조건

최종 제품 에셋 승인은 별도의 화면·에셋 Manifest와 실제 가독성 검증을 요구한다.

## 4. 명명 규칙

향후 신규 파일·데이터·UI 식별자는 다음을 사용한다.

```text
belu
Belu
벨루
```

다음 신규 명칭은 금지한다.

```text
yulbi
Yulbi
율비
```

단, 과거 출처를 설명할 때는 다음 형식을 허용한다.

```text
벨루 시안 — 과거 첨부 파일명: `요정 율비 시안.png`
```

과거 기록 자체를 삭제하거나 소급 변조하지 않는다.

## 5. 동기화 대상

- `docs/PROJECT_CORE.md`
- `docs/DOCUMENTATION_MAP.md`
- `docs/DECISIONS_PENDING.md`
- `docs/PROJECT_CANON_DECISION_LEDGER.md`
- `docs/images/VISUAL_REFERENCE_INDEX.md`
- `docs/reviews/OMENWARD_COMPREHENSIVE_PROJECT_INTEGRITY_REVIEW_2026-08-01.md`
- 연결 Google Sheet의 결정·감사·UX·변경 이력
- Draft PR #116 설명과 추적 댓글

## 6. 현재 판정

```text
BELU_YULBI_RELATION: RESOLVED_SAME_CHARACTER
CANONICAL_GUIDE_NAME: BELU
HISTORICAL_ALIAS: YULBI
GUIDE_CANON_BLOCKER: CLOSED
PRODUCT_ASSET_APPROVAL: NOT_RUN
PRODUCT_CODE: NOT_AUTHORIZED
```
