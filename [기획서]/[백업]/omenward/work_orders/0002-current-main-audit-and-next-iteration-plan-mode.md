# Codex 새 채팅 작업 제안서 — 현재 main 감사·다음 수직 슬라이스 개선 Plan Mode

- 작성일: 2026-07-16
- 상태: **새 Codex 채팅 Plan Mode 입력 준비 / 구현 금지**
- 목적: 과거 Phase 0 가정이 아니라 실제 현재 main의 코드·데이터·테스트·시각자료를 조사하고, 다음 품질 개선 작업을 위한 검토 가능한 제안서를 작성한다.

이 문서는 Codex가 제출할 최종 제안서가 아니다. 새 채팅에 전달하는 Work Order다.

## 1. 새 Codex 채팅에 붙여 넣을 시작 프롬프트

```text
저장소: https://github.com/alsdmlals4-eng/omenward
작업 모드: Codex Plan Mode / 읽기 전용 조사
시작 문서: docs/work_orders/0002-current-main-audit-and-next-iteration-plan-mode.md

먼저 시작 문서를 처음부터 끝까지 읽고, 그 안의 읽기 순서와 조사 지시에 따라 현재 main의 문서·코드·데이터·Scene·Resource·테스트·검증 문서를 확인하세요.

과거 Work Order의 `구현 전` 상태를 현재 사실로 가정하지 마세요. project.godot과 실제 파일, 최신 커밋·Issue·PR·validation 문서를 근거로 현재 완료·미완료·충돌·기술 부채를 구분하세요.

시각 작업에서는 반드시 다음을 읽으세요.
- docs/images/VISUAL_REFERENCE_INDEX.md
- docs/design/APPROVED_UNIT_VISUAL_FORMAT_AND_REFERENCE_USE_V1.md
- docs/design/APPROVED_ART_DIRECTION_AND_PRODUCTION_GUIDE_V1.md
- docs/design/APPROVED_UNIT_ANIMATION_AND_BATTLE_PRESENTATION_GUIDE_V1.md

병종 월드 이미지는 첫 번째 전장 UI 참고 이미지의 실제 전장 삽입형 소형 고해상도 픽셀 스프라이트 형식을 따릅니다. 과거 10병종×등급 도감표의 큰 전신 캐릭터 형식을 월드 스프라이트 기준으로 사용하지 마세요. 도감표는 병종 목록과 일반→엘리트→영웅→전설 위계 참고에만 사용합니다.

이번 실행에서는 구현·자산 제작·브랜치·커밋·PR을 만들지 마세요. 최종 산출물은 docs/PROPOSAL_WORKFLOW.md 형식의 다음 개선 제안서입니다. 실제 영향 파일, 상태 소유, 작은 구현 단계, 자동·수동 검증, 시각 비교 캡처, 위험과 사용자 승인 요청을 포함하세요.

제안서 마지막:
현재 상태: 제안서 검토 대기
사용자 승인 전 구현 금지
```

## 2. 필수 읽기 순서

```text
1. 최신 사용자 지시
2. AGENTS.md
3. docs/BASE_RULES_VERSION.md
4. docs/HANDOFF_CONTEXT.md
5. docs/DOCUMENTATION_MAP.md
6. docs/PROPOSAL_WORKFLOW.md
7. docs/work_orders/0002-current-main-audit-and-next-iteration-plan-mode.md
8. docs/OMENWARD_GAME_DESIGN.md
9. docs/design/APPROVED_PREPRODUCTION_POC_BASELINE_V1.md
10. 현재 작업과 관련된 APPROVED 책임 문서
11. docs/images/VISUAL_REFERENCE_INDEX.md
12. docs/OMENWARD_ROADMAP.md
13. docs/DECISIONS_PENDING.md
14. 현재 Issue·Goal·PR
15. project.godot, Scene, scripts, data, tests
16. docs/PHASE_0_VALIDATION.md
17. docs/VERTICAL_SLICE_VALIDATION.md
18. docs/ACTIVE_CONTEXT.md
```

## 3. 실제 저장소 감사

Codex는 다음을 직접 확인한다.

- `project.godot`의 엔진·renderer·해상도·main Scene 설정.
- 현재 Scene 트리와 상태 소유.
- 공용 UnitArchetype, Tier, Rank, Attack, AnimationContract, FactionVisual 데이터.
- 적군 전용 중복 병종 데이터·Scene·스킬·모션 계약이 생겼는지.
- 독립 3라인, 성문, 중간거점, 접전지, 건설 노드와 암살자 우회 구현.
- 룰렛, 배치, 경제, 웨이브와 승패 흐름.
- 튜토리얼 4웨이브와 일반 W1~W20 데이터·실행 가능 범위.
- headless 테스트와 수동 QA가 실제로 통과했는지.
- 문서가 현재 코드 상태와 충돌하는 부분.
- 시각자료 원본이 저장소에 존재하는지, 인덱스만 있고 `MIGRATION_PENDING`인지.

확인하지 않은 내용을 완료로 쓰지 않는다.

## 4. 제품 불변 조건

### 전장

- 좌우 대칭 독립 상·중·하 3라인.
- 진영당 라인별 성문 3개.
- 중간거점마다 전방 2·후방 1 건설 노드.
- 점령 시 건설권과 기본 생산권 이전.
- 중앙 접전지 건설 불가, 다른 라인 연결 없음.
- 암살자는 적 후방 직접 생성이 아니라 같은 라인의 안개 우회로 사용.
- 전장 전체 조망, 미니맵 없음.

### 공용 병종

```text
UnitArchetypeProfile × 10
+ TierProfile
+ RankProfile
+ owner_team_id
+ FactionVisualProfile
```

- 아군·적군 별도 전투 병종 데이터 금지.
- 같은 병종·Tier·Rank는 능력치·스킬·타기팅·점령력·구조물 피해·AnimationContract 공유.
- 적군은 이미지·초상화·아이콘·팔레트·표시명·출격 방식만 다름.

### 판정과 애니메이션

- 공격은 준비→판정→회복.
- 실제 판정이 권위 원본.
- 접촉·투사체 발사와 판정 오차 한 프레임 이내.
- 위치는 코드가 소유, 루트 모션 사용 안 함.

## 5. 최신 병종 비주얼 결정

### 승인 형식

```text
실제 전장 삽입형 소형 고해상도 픽셀 월드 스프라이트
약 2.5~3등신 전술 미니어처
일반 인간형 34~40px 첫 표시 높이
무기·자세·몸통 덩어리와 공격 방향 우선
```

첫 번째 전장 UI 참고 이미지에서 다음을 본다.

- 전장 속 유닛 크기와 디테일 균형.
- 작은 크기의 병종·진영 판독.
- 전장, 전투, HUD, 건설·전술 패널과 벨루의 정보 계층.

다음은 복사하지 않는다.

- 임시 수치·문구·세력명·비용.
- 이미지의 맵 연결과 거점·요새·건물 위치.
- 좌하단 전장 요약 또는 미니맵 형태.

### 과거 도감표

두 번째 10병종×등급 도감표는 다음에만 사용한다.

- 공용 10병종 확인.
- 같은 병종의 일반·엘리트·영웅·전설 비교.
- 상위 등급에서 무기·자세·실루엣이 강화되는 방향.

큰 전신 캐릭터 비율과 렌더링 밀도는 월드 스프라이트 형식이 아니다.

## 6. 제안해야 할 다음 작업 묶음

현재 main 감사 결과를 바탕으로 하나의 우선 추천안을 제시한다. 범위 후보:

### A. 구현·문서 정합성

- 구현 전이라고 남은 레거시 문구 제거.
- 실제 main과 validation 결과에 맞춘 Handoff·Active Context·Roadmap·Issue 동기화.
- 오래된 Phase 0 Work Order를 기록용으로 강등하고 현재 Work Order를 활성 라우터로 지정.

### B. 수동 QA와 계측

- 1920×1080 및 1280×720 실행.
- 3라인 이탈, 건물 도로 차단, 점령권 이전, 성문 독립 상태, 우회 경고 검증.
- 튜토리얼 4웨이브와 W1~20 진입·보스 이정표 검증.
- 동일 시드·입력 재현과 성능 상한 확인.

### C. 병종 시각 프로브

- 방패병, 궁병, 암살자, 사제, 거인 또는 공성 더미의 아군·적군 시각 프로브.
- 첫 번째 전장 이미지 형식의 작은 픽셀 월드 스프라이트로 제작 계획.
- 5기 이상 중첩, 밝고 어두운 전장, 1080p·720p 비교 캡처.
- 일반·엘리트·영웅·전설의 기능적 위계 테스트.
- 실제 자산 대량 제작 전 키포즈·idle·move·attack 최소 세트 승인 게이트.

### D. 애니메이션·판정 연결

- 현재 AnimationContract와 실제 전투 이벤트 연결 상태 확인.
- placeholder 표현과 최종 스프라이트 시트의 프레임·피벗·이벤트 계약.
- 아군·적군 Visual Set이 같은 계약을 재사용하는 자동 검증.

### E. 시각자료 마이그레이션

- `MIGRATION_PENDING` 자료 중 다음 작업에 필요한 파일만 저장소 공식 경로로 이동.
- 각 이미지의 사용·비사용·변경점 기록 검수.
- 전장 맵 툴과 사용법의 도구 경로·버전·책임 문서 결정.
- 레거시 GDD는 활성 기획이 아닌 archive source로 분류.

제안서는 위 전체를 한 번에 구현하도록 요구하지 않는다. 현재 위험과 플레이어 가치가 가장 큰 최소 묶음을 추천하고 후속 작업을 분리한다.

## 7. 제안서 필수 산출물

- 현재 실제 구현 상태 표.
- 문서와 코드 충돌 표.
- 추천 범위와 제외 범위.
- 정확한 영향 파일·Scene·Resource·테스트.
- 상태 소유와 Signal·데이터 흐름.
- 단계별 관찰 가능한 결과.
- 자동 검증 명령.
- 1080p·720p 수동 QA 절차.
- 병종 스프라이트 비교 캡처 규격.
- 시각자료 migration 완료·pending 구분.
- 위험, 롤백과 사용자 결정 요청.

## 8. 금지

- Plan Mode에서 구현 또는 자산 대량 제작.
- 첫 번째 이미지의 맵·수치·미니맵까지 전체 승인안으로 복제.
- 두 번째 도감표의 큰 전신 캐릭터를 월드 스프라이트로 축소 사용.
- 적군 전용 병종 데이터나 애니메이션 상태 머신 추가.
- 실제 테스트 없이 완료·가독성·성능 통과 보고.
- File Library에서 찾았다는 사실을 저장소 이동 완료로 표현.
