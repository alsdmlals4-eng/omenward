# OMENWARD 프로젝트 인수인계 컨텍스트

- 갱신일: 2026-07-24
- 현재 상태: `V2_SPEC_APPROVED / V2_CANON_CANDIDATE / V2_IMPLEMENTATION_NOT_STARTED`
- 기존 증거: `LEGACY_C1_C2_C3_PROVEN`
- 사람 플레이: `HUMAN_QA_NOT_RUN`
- 현재 Issue: `#56`
- 프로젝트 코어: `docs/PROJECT_CORE.md`
- 실제 구현 상태: `docs/CURRENT_IMPLEMENTATION_STATUS.md`

이 문서는 새 작업자가 이전 대화 없이 현재 제품 방향, 승인 규칙, 구현 경계와 다음 조사 순서를 이해하기 위한 출발점이다.

## 1. 가장 먼저 알아야 할 것

1. 오멘워드는 건물과 가로 이동으로 세 원형 릴의 미래 배열을 설계하고, 당첨 병력을 세 라인 중 하나에 영구 배치하는 실시간 전략 오토배틀이다.
2. V2 설계와 열린 7개 계약은 2026-07-24 사용자 승인을 받았다.
3. 현재 main의 C1·C2·C3는 기존 설계 기준 실행 증거이며 V2 구현 완료 증거가 아니다.
4. V2 제품 코드는 아직 시작하지 않았다.
5. 문서 PR 병합과 검증 뒤 각 제품 단계별 Plan Mode 제안과 사용자 승인이 필요하다.
6. 공용 10병종과 진영 Visual 분리, Godot 4.7.1·GDScript 기술 기준선은 유지한다.
7. 전술 아이템 룰렛 심벌과 mid-run save는 현재 코어 범위가 아니다.

## 2. 읽기 순서

```text
최신 사용자 지시
→ AGENTS.md
→ docs/PROJECT_CORE.md
→ docs/design/APPROVED_CORE_V2_INTEGRATED_SPEC.md
→ docs/design/APPROVED_ROULETTE_CORE_RULES.md
→ docs/design/APPROVED_MAPRUN_STAGE_WAVE_AND_MIDPOINT_CORE_V1.md
→ docs/CURRENT_IMPLEMENTATION_STATUS.md
→ docs/DOCUMENTATION_MAP.md
→ docs/OMENWARD_GAME_DESIGN.md
→ docs/OMENWARD_ROADMAP.md
→ Issue #56·현재 PR
→ 실제 code/data/Scene/tests
→ docs/ACTIVE_CONTEXT.md
```

## 3. 제품 약속

> **예고된 세 전선의 공세를 읽고, 제한된 건물로 세 원형 릴의 토큰 구조를 설계·영구 편집한 뒤, 당첨 병력을 어느 전선에 커밋할지 결정해 전황을 뒤집는다.**

핵심 플레이 감정:

```text
설계했다 → 릴 토큰·출처·인접 순서를 만들었다
읽어냈다 → 보드·공세·보관·식량을 비교했다
적중했다 → 비가역 배치가 전선을 뒤집었다
```

## 4. 핵심 구조

- 독립 상·중·하 3라인.
- TokenSource 건물이 각 릴에 같은 출처 토큰 1개씩 제공.
- 길이 3 이상의 세 원형 릴.
- 세로 이동은 릴 cursor 회전.
- 가로 이동은 노출 인덱스 토큰 순환 교환과 미래 배열 영구 편집.
- 중앙줄 선행 판정과 1/2/3~7/8 완성선 등급.
- immutable snapshot과 명시적 한 번 확정.
- 보관함 4칸, 무손실 결과 대기, 판매와 라인 영구 배치.
- 식량은 배치 수용량.
- 스테이지 준비, 일반 전술계획, 위험 실시간 전투.
- 3기 묶음 웨이브, 10초 예고·20초 시작.
- 전투 반경 기반 고정 8초 중간 접전지.

## 5. 기존 구현 증거

보존 가능한 legacy 증거:

- 중앙 판정·완성선·등급·금화.
- 결정론과 출처 ID.
- 3라인과 공용 병종.
- 구조물·본진 승패 경로.
- 도메인 snapshot→HUD와 원인 보고.

교체할 legacy 계약:

- 독립 9칸 가중 추첨.
- 구형 럭키·이동·전설 제한.
- 60초/T-30·15·5.
- 점령력 합산.
- StageRun 중심 런 상태.

## 6. 구현 전 확인

제품 코드 변경 전 반드시 확인한다.

- 승인된 단계별 Plan Mode 제안서.
- 목표와 플레이어 가치.
- 포함·제외 범위.
- 상태 소유와 데이터 마이그레이션.
- Red 테스트와 회귀 테스트.
- 롤백 기준.
- 실행할 Godot 명령.

## 7. 다음 순서

1. Issue #56 문서 PR을 검증·병합한다.
2. 순수 RouletteBoardResolver 분리 계획을 승인받는다.
3. 물리 릴 도메인을 UI·경제 없이 구현한다.
4. 건물 출처, snapshot, 이동, 럭키, 전설 주기를 연결한다.
5. 보관·배치·식량을 연결한다.
6. MapRun, 묶음 웨이브, 접전지를 연결한다.
7. V2 UX와 100,000시드·사람 검증을 실행한다.

## 8. 금지된 완료 표현

다음 조건 전에는 `CORE_LOCK_V2`, `V2_IMPLEMENTED`, `CORE_LOOP_PROVEN`, `MVP_COMPLETE`를 사용하지 않는다.

- 문서 PR main 병합.
- V2 자동 계약 통과.
- 10~15분 사람 플레이.
- 1080p·720p 가독성 검증.
