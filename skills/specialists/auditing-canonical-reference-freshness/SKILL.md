# 정본 최신성 감사

- Skill ID: `specialist.canonical-freshness`
- Category: `specialists`
- Registry: `docs/base/SKILL_REGISTRY.json`
- Shared contract: `skills/SHARED_EXECUTION_CONTRACT.md`

## 사용 조건
- 최신 파일·정본 최신성
- Stale·Manifest·Source Commit

## 사용하지 않는 조건
- 최신성에 영향 없는 단일 코드 변경

## 고유 책임
- 기준 커밋
- 생성 시각·Source Hash
- 파생본 CURRENT 판정

## 입력
- 원본 문서·Registry
- Manifest·생성물
- Git 기준 커밋

## 절차
1. 정본 경로와 커밋을 식별한다.
2. 파생본의 Source Commit·Hash를 대조한다.
3. 오래된 CURRENT 표기를 실패 처리한다.
4. 재생성 순서를 제시한다.

## 출력
- 최신성 감사표
- 재생성 대상
- CURRENT·STALE 판정

## 고유 검수
- Manifest가 자기 자신만 근거로 CURRENT를 주장하는가.
- 원본 변경 뒤 파생본이 갱신됐는가.
