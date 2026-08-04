# OMENWARD 프로젝트 AI 작업 규칙

이 저장소는 GPT/Work가 핵심 재미·콘텐츠·플레이어 규칙·UX·아트 정본을 관리하고, Codex가 별도 승인된 범위에서 Godot 구현·테스트를 수행하는 공동 작업 저장소다.

## 1. 규칙 우선순위

```text
사용자의 최신 지시
→ docs/PROJECT_CORE.md
→ docs/DOCUMENTATION_MAP.md
→ docs/DOCUMENT_LIFECYCLE_REGISTRY.md
→ 주제별 [현행] 책임 원본
→ 실제 코드·데이터·Scene·실행 증거
→ [증거]
→ [대체됨]·[보류]·[폐기]
```

파일명에 `APPROVED`가 있어도 lifecycle registry가 `[보류]` 또는 `[대체됨]`으로 분류하면 구현 권위가 없다.

## 2. 작업 전 읽기 순서

1. `AGENTS.md`
2. `docs/PROJECT_CORE.md`
3. `docs/ACTIVE_CONTEXT.md`
4. `docs/DOCUMENTATION_MAP.md`
5. `docs/DOCUMENT_LIFECYCLE_REGISTRY.md`
6. `docs/OMENWARD_GDD_CURRENT_CANON.md`
7. 작업 주제의 `[현행]` 책임 원본
8. `docs/CURRENT_IMPLEMENTATION_STATUS.md`
9. `docs/DECISIONS_PENDING.md`
10. 현재 Issue·PR·실제 코드·테스트

Stage·Wave·Boss 작업은 `docs/design/APPROVED_OMENWARD_STAGE_WAVE_DANGER_BOSS_PRESSURE_MATRIX_2026-08-04.md`를 반드시 읽는다.

## 3. 역할 분리

```text
GPT / Work
= 핵심 재미, 플레이 동기, 콘텐츠 구조, 플레이어 규칙, UX, 이미지·아트 방향, 검수 기준

Codex
= 자료구조, 알고리즘, 좌표, 경로탐색, 충돌, Spawn·Timer 구조, 성능, 코드, 테스트
```

Codex 구현 선택이 플레이어 경험·콘텐츠 역할·시각 계층을 바꾸면 구현을 중단하고 새 기획 Gate로 돌아온다.

## 4. 현재 프로젝트 코어

> **건물로 룰렛을 만들고, 룰렛으로 전선을 지휘한다.**

```text
Stage 압력·Wave 순서 확인
→ 건설·TokenSource 구성
→ 세 원형 릴 회전
→ 3×3 노출창의 열·행 이동
→ 결과 확정
→ 보관·판매·한 전선 비가역 배치
→ 자동전투·점령·건물 운영
→ 결과 원인 복기
→ 다음 Stage 설계
```

- 세 원형 릴은 3×3 노출창의 세 열이다.
- 상·중·하 세 전선.
- 치명적 공세 정보는 기본·일반 난이도에서 숨기지 않는다.
- 일반 유닛의 자유로운 전선 횡단은 없다.
- Cross-lane 효과는 명시적 능력·건물만 허용하고 사전 표시한다.
- 배치 뒤 자유 회수·전선 변경·판매는 없다.
- 보상은 명시적 확정 한 번에만 지급한다.

## 5. 현행 Stage·Wave 규칙

```text
MapRun = 20 Stage
Wave Beat 기준선 = 3
Danger = 4 / 9 / 14 / 19
Boss = 5 / 10 / 15 / 20
압력 = MASS / ARMORED / FLYING / INFILTRATION / SIEGE
```

- Stage 1~5는 압력 문해력, 6~10은 압력 조합, 11~15는 기회비용, 16~20은 종합 숙련이다.
- Normal은 `Probe → Complication → Commitment Test`.
- Danger는 공개된 한 가지 규칙 변형만 사용한다.
- Boss는 Route·태세·목표·호위·집중 공격 기회를 실제로 바꾼다.
- Stage 시작 뒤 치명적 Route·필요 공격 Layer·필수 카운터를 숨은 무작위로 바꾸지 않는다.
- 압력 역할과 학습 목표는 고정하되 적 패키지·전선·Route는 맵별 작성 변형으로 둔다.
- exact Spawn 초·수량·Threat Budget은 시뮬레이션 전 정본화하지 않는다.
- 특정 병종·건물 하나만 정답인 Stage를 만들지 않는다.

구형 `15웨이브=1스테이지`, 고정 60초 공세, 식량·병영 자동생산 기반 첫 4공세는 현행 구현 입력이 아니다.

## 6. 현행 자원·건물·HUD

```text
자원 = 골드 / 마석 / 배치 병력·병력 한도 / 이동권
건물 = 금고 / 농장 / 병영 / 방어탑 / 지휘소 / 마력탑
하단 = [룰렛] [보관함] [건설] [전술스킬] [벨루]
상인 = Stage 종료 정비시간
```

- 식량은 현행 핵심 HUD 자원이 아니다.
- 지휘소는 현재 MapRun 전체 아군 병력 오라다.
- 토큰은 초당 공급되지 않는다.
- 건물별 지속 유지비는 없다.
- 룰렛 금화·병종 토큰은 인게임 금화·T1/T2 병종 이미지를 재사용한다.
- T3 병종 이미지는 룰렛 병종 토큰에 사용하지 않는다.

## 7. 핵심 재미 검수

새 기능은 다음 중 최소 두 축에 관찰 가능한 영향을 줘야 한다.

```text
공세 예측
릴·TokenSource 설계
회전·이동·결과 처리
전선 배치·전투 결과
결과 복기·다음 설계
```

숫자만 증가시키고 핵심 선택을 바꾸지 않는 기능은 추가하지 않는다.

## 8. 문서 수명주기

- `[현행]`: 신규 기획·구현 사용 허용.
- `[대체됨]`: 후속 문서가 권위 승계. 역사 근거만 허용.
- `[보류]`: 최신 정본과 재검증 전 사용 금지.
- `[폐기]`: 채택하지 않음. 사용 금지.
- `[증거]`: 과거 검증 사실만 증명.

`current_main`과 `context_baseline_commit`은 `RESOLVE_FROM_REPOSITORY_DEFAULT_BRANCH`로 동적 해석한다. 과거 병합 SHA는 `last_merged_*` 증거 필드에만 기록한다.

## 9. GitHub·Sheet 원칙

- 사용자 승인 Decision은 GitHub 권위 문서와 Google Sheet에 같은 ID로 반영한다.
- bounded read-back 전에는 `SYNCED`로 보고하지 않는다.
- 문서 정본 변경과 제품 코드 구현을 같은 PR에 섞지 않는다.
- push·PR·CI·Sheet 검증에 실패한 작업을 완료로 보고하지 않는다.
- Green 문서/기획 PR은 standing authorization 범위에서 preflight 후 병합할 수 있다.
- 제품 코드·Scene·Resource·실제 게임 데이터 PR은 별도 사용자 승인 없이 병합하지 않는다.

## 10. 구현 Gate

제품 코드 변경 전 필수:

- 건물·병종·전술이 다섯 압력에 실제 대응 경로를 제공.
- 사용자 승인 구현 계획.
- 플레이어 가치와 포함·제외 범위.
- Red 테스트와 완료 기준.
- 상태 소유·마이그레이션·롤백.
- 관련 자동 검증과 수동 플레이 계획.

문서 승인과 CI 통과는 제품 구현 완료가 아니다.

## 11. 기술 기준

- Godot 4.7.1 Standard, GDScript, Compatibility renderer.
- `.godot/`과 로컬 캐시를 커밋하지 않는다.
- Scene `scenes/`, Script `scripts/`, 정적 데이터 `data/` 또는 `resources/`, 검증 `tests/`.
- UI는 표시 데이터를 입력받고 사용자 의도를 반환하며 게임 규칙을 직접 계산하지 않는다.
- 같은 상태를 두 객체가 동시에 책임 원본으로 소유하지 않는다.
- 기존 Legacy 증거와 최신 미구현 정본을 구분한다.

```text
LEGACY_PROVEN != LATEST_IMPLEMENTED
PLANNING_APPROVED != PRODUCT_IMPLEMENTED
```

## 12. 완료 보고

- 변경 파일과 이유.
- 적용한 Decision·Sync ID.
- 실행한 검증과 결과.
- 미실행 항목.
- lifecycle 상태 변경.
- 잔여 위험과 다음 작업.

테스트하지 않은 항목을 완료했다고 보고하지 않는다.
