# OMENWARD / 오멘워드

**오멘워드**는 예고된 세 전선 공세를 읽고, 건물로 세 원형 릴의 미래 결과를 설계한 뒤, 룰렛에서 얻은 병력을 한 전선에 비가역 배치해 전황을 뒤집는 판타지 전략 오토배틀 게임입니다.

> **건물로 룰렛을 만들고, 룰렛으로 전선을 지휘한다.**

```yaml
updated_at: 2026-08-04
current_main: RESOLVE_FROM_REPOSITORY_DEFAULT_BRANCH
work_mode: TOTAL_PLANNING
current_planning: CORE_FUN_AND_CONTENT_GUARDRAILS / NOT_IMPLEMENTED
current_grill_me_count: 1_OF_10
product_code_authority: NONE
art_asset_production_authority: NONE
image_generation: STOPPED_BY_USER
human_validation: HUMAN_QA_NOT_RUN
```

## 핵심 루프

```text
공세 예고
→ 건설·TokenSource 구성
→ 세 원형 릴 회전
→ 3×3 노출창에서 열·행 이동
→ 결과 확정
→ 보관·판매·한 전선 배치
→ 자동전투·점령·건물 운영
→ 결과 원인 복기
→ 다음 Stage 설계
```

세 원형 릴은 3×3 노출창의 세 열을 구성합니다.

## 현재 핵심 규칙

- 상·중·하 세 전선과 보이는 주 경로·우회로·공중 Route.
- 골드, 마석, 배치 병력·병력 한도, 룰렛 이동권.
- 기본 건물 6종: 금고, 농장, 병영, 방어탑, 지휘소, 마력탑.
- 지휘소는 현재 MapRun 전체 아군 병력 오라.
- 상인은 Stage 종료 정비시간에만 방문.
- 룰렛 금화·병종 토큰은 별도 아이콘이 아니라 인게임 금화·T1/T2 병종 이미지를 재사용.
- T3 병종 이미지는 룰렛 병종 토큰에 사용하지 않음.
- 최종 아트 방향은 픽셀 가독성과 동화풍 일러스트 재질을 결합한 하이브리드.

## 먼저 읽을 문서

1. [`AGENTS.md`](AGENTS.md)
2. [`docs/PROJECT_CORE.md`](docs/PROJECT_CORE.md)
3. [`docs/ACTIVE_CONTEXT.md`](docs/ACTIVE_CONTEXT.md)
4. [`docs/DOCUMENTATION_MAP.md`](docs/DOCUMENTATION_MAP.md)
5. [`docs/DOCUMENT_LIFECYCLE_REGISTRY.md`](docs/DOCUMENT_LIFECYCLE_REGISTRY.md)
6. [`docs/OMENWARD_GDD_CURRENT_CANON.md`](docs/OMENWARD_GDD_CURRENT_CANON.md)
7. [`docs/CURRENT_IMPLEMENTATION_STATUS.md`](docs/CURRENT_IMPLEMENTATION_STATUS.md)
8. [`docs/DECISIONS_PENDING.md`](docs/DECISIONS_PENDING.md)
9. [`docs/HANDOFF_CONTEXT.md`](docs/HANDOFF_CONTEXT.md)

`[대체됨]`, `[보류]`, `[폐기]` 문서는 신규 기획·Codex 구현·아트 제작 입력으로 사용하지 않습니다.

## 현재 단계

최근 10개 기획 결정은 전투 의미·공간·HUD·룰렛 자산·아트 방향을 정본화했습니다. 다음 단계는 기술 세부가 아니라 다음 콘텐츠를 확정하는 것입니다.

```text
Stage·Wave·Danger·Boss 압력 매트릭스
→ 건물 6종 T2/T3 분기·카운터
→ 병종 역할·시너지
→ 전술스킬·마석
→ Stage 종료 상인
→ 첫 10~15분 흐름
→ Hero·Legendary 재조정
→ Meta·Hub 재조정
```

제품 코드, 런타임, 실제 아트 자산은 별도 승인 전 변경하지 않습니다.
