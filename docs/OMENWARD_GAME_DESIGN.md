# [대체됨] 오멘워드 게임 기획서 v0.26

```yaml
status: SUPERSEDED / HISTORICAL_REFERENCE_ONLY
superseded_at: 2026-08-04
superseded_by: docs/OMENWARD_GDD_CURRENT_CANON.md
implementation_authority: NONE
```

이 파일의 과거 본문은 Git 이력에 보존되어 있다. 신규 기획·Codex 구현·아트 제작의 책임 원본으로 사용하지 않는다.

## 대체 이유

과거 v0.26은 다음 구형 가정을 현행처럼 포함했다.

- 식량을 핵심 런 자원으로 사용.
- 기본 건물 5종.
- 지휘소 주변 범위 오라.
- 골드/초 중심 경제.
- 구형 첫 10분·Hero·Legendary 계약.

현재 정본은 다음을 사용한다.

```text
자원 = 골드 / 마석 / 배치 병력·병력 한도 / 이동권
건물 = 금고 / 농장 / 병영 / 방어탑 / 지휘소 / 마력탑
지휘소 = 현재 MapRun 전체 아군 병력 오라
```

## 현행 책임 원본

- `docs/PROJECT_CORE.md`
- `docs/OMENWARD_GDD_CURRENT_CANON.md`
- `docs/DOCUMENTATION_MAP.md`
- `docs/DOCUMENT_LIFECYCLE_REGISTRY.md`
- `docs/design/APPROVED_VERTICAL_SLICE_SYSTEM_CONTRACT_2026-07-27.md`
- `docs/design/APPROVED_OMENWARD_CORE_FUN_AND_CONTENT_GUARDRAILS_2026-08-04.md`

과거 상세가 필요하면 Git history에서 조회하되, 새 Decision으로 재검토·승인하기 전에는 되살리지 않는다.
