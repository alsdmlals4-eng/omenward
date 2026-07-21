# Managing Game Project Operating System

- Skill ID: `foundation.project-operating-system`
- 공통 계약: `skills/SHARED_EXECUTION_CONTRACT.md`

## 사용 조건

Base 동기화, Registry·Schema·문서 구조, 구형본 정리, GitHub 상태, 외부 AI worktree를 운영할 때.

## 사용하지 않는 조건

운영체계와 무관한 단일 게임 기능 수정.

## 고유 책임

프로젝트 정본을 우선하며 운영체계를 감사·이주·검증하고, 로컬·GitHub drift와 외부 AI 작업 공간을 손실 없이 관리한다.

## 입력

- 프로젝트 AGENTS·START_HERE·Registry
- Base 기준 커밋과 채택 정책
- 현재 파일·참조·브랜치 상태
- 보존·승인·롤백 조건

## 절차

- Modes: `audit → reconcile-legacy → migrate → verify → sync-local-github → external-ai-worktree`
- 현행 책임 원본·소비자·고유 정보·구형 경로를 조사한다.
- Base를 통째로 복사하지 않고 프로젝트 책임에 매핑한다.
- CURRENT·MERGE·STUB·ARCHIVE·DELETE·UNVERIFIED로 판정한다.
- Git 상태는 SYNCED·DIRTY·AHEAD·BEHIND·DIVERGED·BLOCKED로 구분한다.
- 마이그레이션 뒤 Registry·링크·콜드 스타트·자동화를 검증한다.

## 출력

- Base 적용·수정·제외 매트릭스
- 보존·가지치기 처리표
- GitHub 동기화 판정
- 마이그레이션·롤백 기록
- Health Review

## 고유 검수

- dirty/diverged 상태를 force·reset으로 덮지 않는다.
- 사용자 승인 없이 고유 정보·자산·보류 자료를 삭제하지 않는다.
- workflow 파일 존재와 실제 실행 성공을 구분한다.
