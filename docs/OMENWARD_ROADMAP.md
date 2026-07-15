# 오멘워드 개발 로드맵

- 갱신일: 2026-07-16
- 기준: `docs/HANDOFF_CONTEXT.md`, `docs/design/APPROVED_PREPRODUCTION_POC_BASELINE_V1.md`
- 현재 상태: **프리프로덕션 구조 승인 완료 / Phase 0 기술 제안서 사용자 검토 대기 / 구현 전**
- 현재 제안서: `docs/design/proposals/0001-phase-0-godot-bootstrap.md`
- 모든 코드·Scene·Resource·데이터 구조 변경은 제안서와 사용자 승인 후 시작한다.

---

## 1. 현재 위치

```text
프리프로덕션 구조 승인
→ 공용 10병종 데이터·진영 이미지 분리 승인
→ 전장·애니메이션 수직 슬라이스 초기값 승인
→ Phase 0 기술 제안서 작성
→ [현재] 사용자 검토·수정·승인
→ Phase 0 Godot 기술 기준선 구현
→ 수직 슬라이스 Plan Mode
→ 사용자 승인
→ 10~15분 핵심 수직 슬라이스
→ 시뮬레이션·플레이테스트
→ 콘텐츠·아트 확장
→ 캠페인·데모 통합
```

최초 작업자는 `docs/HANDOFF_CONTEXT.md`를 읽고 현재 승인 구조와 금지 범위를 확인한다.

현재 `진행`은 구현 시작을 뜻하지 않는다. Phase 0 제안서는 작성됐으며 다음 게이트는 사용자 검토와 명시적 승인이다.

---

## 2. 프로젝트 전체 완료 정의

오멘워드의 완료는 기능 수가 아니라 다음 플레이 경험과 품질을 만족하는 상태다.

- 플레이어가 다음 공세를 읽고 건물·룰렛·배치로 대응한다.
- 세 라인의 성문·중간거점·접전지 상태를 미니맵 없이 파악한다.
- 공용 10병종 데이터가 아군·적군 이미지 세트에서 동일하게 동작한다.
- 암살자 우회와 거점·성문 공방이 빌드 선택을 바꾼다.
- 첫 10분 안에 핵심 루프를 두 번 체험한다.
- 1~15웨이브와 선택적 16~20 초과전이 안정적으로 진행된다.
- 약 3시간 캠페인이 병종·Tier·위협을 단계적으로 소개한다.
- 실제 화면 크기에서 병종·진영·등급·공격 전조를 읽을 수 있다.
- 결정론적 데이터와 테스트로 주요 결과를 재현한다.
- 적군 전용 병종 데이터 복제 없이 콘텐츠를 확장한다.

---

## 3. 전체 단계 요약

| 단계 | 목표 | 현재 상태 | 다음 게이트 |
|---|---|---|---|
| P0 프리프로덕션 | 제품·전장·공용 데이터·아트·연출 계약 | 구조 승인 완료 | Phase 0 승인 |
| G1 Phase 0 제안서 | Godot 기술 기준선 합의 | **사용자 검토 대기** | `제안서 승인` |
| P1 Phase 0 구현 | 실행·데이터·결정론·검증 골격 | 미시작 | headless·계약 테스트 PASS |
| G2 수직 슬라이스 제안서 | 실제 파일 기준 핵심 루프 계획 | Phase 0 뒤 | 사용자 승인 |
| P2 핵심 수직 슬라이스 | 10~15분 핵심 재미와 위험 검증 | 미시작 | 플레이테스트 기준 충족 |
| P3 시스템 안정화 | 확률·경제·전투·성능 조정 | 미시작 | 반복 가능한 기준선 |
| P4 콘텐츠 확장 | 10병종·건물·웨이브·캠페인 | 미시작 | 캠페인 통합 QA |
| P5 데모·출시 준비 | 아트·오디오·접근성·패키징 | 미시작 | 데모 품질 게이트 |

---

## 4. Phase P0 — 프리프로덕션 디자인 기준

### 완료된 구조

- 오멘워드 공식명, 세계관과 벨루 단일 안내자.
- 건물 기반 3×3 룰렛과 첫 10분 핵심 루프.
- 좌우 대칭 독립 3라인과 라인별 성문.
- 중간거점 점령, 전방 2·후방 1 노드, 건설권·생산권 이전.
- 독립 중앙 접전지.
- 암살자 같은 라인 안개 우회로.
- 전장 전체 조망과 미니맵 미사용.
- 공용 UnitArchetype 10개와 Tier·Rank 능력 계보.
- 아군·적군 전투 데이터 공유, 진영별 이미지 세트 분리.
- 기본 병영·특수병단·경제·건물·전술·용병 구조.
- 60초 공세 시계와 W5·W10·W15·W20 이정표.
- 튜토리얼 1 + 정규 9의 약 3시간 캠페인 초안.
- UI·아트·애니메이션·오디오·성능·테스트 계약.
- 중간거점·성문·암살자 우회로 초기값.
- 프로젝트 인수인계와 Base 공용 지식 체계.

### 승인된 전장 초기값

```text
중간거점: 중립화 10초 + 점령 10초, 최대 점령력 2.0
거점 생산: 금화 +2 / 30초, 안정화 5초
성문: HP 5000, 방어·마저 80, 일반 40%, 공성 200%, 붕괴 2초
암살자: 진입 1초, 이동 9초, 경고 2.5초, 출현 준비 0.6초
```

### 남은 검증

- 룰렛 최소 100,000시드 확률·금화 EV.
- 기본·시장·접전지·중간거점 경제 시간축.
- 전투·생산·웨이브 표 계산.
- 실제 병종 키포즈와 전략 줌 축소 모션.
- 점령·성문·우회 대응 시간.

프리프로덕션은 새로운 대형 시스템을 추가하는 단계가 아니라 구현 가능한 책임 경계와 첫 수치를 검증하는 단계로 전환됐다.

---

## 5. Gate 1 — Phase 0 기술 제안서 검토

책임:

- Issue #1.
- `docs/goals/0001-engine-selection-and-bootstrap.md`.
- `docs/design/proposals/0001-phase-0-godot-bootstrap.md`.

### 제안서 추천안

```text
Godot 4.7.1 standard x86_64
GDScript
Compatibility renderer
1920×1080 출력
960×540 내부 viewport
viewport stretch / keep aspect / integer scale
```

구조:

```text
Main
└─ GameSession
   ├─ CombatClock
   ├─ DeterminismService
   └─ DataRegistry
```

- Phase 0 AutoLoad 없음.
- 60Hz active combat tick.
- planning 중 active tick 정지.
- master seed와 이름 기반 RNG stream.
- typed Resource + StageManifest·replay JSON.
- 외부 플러그인 없는 GDScript headless test runner.

### 사용자 결정

1. Godot 4.7.1 standard와 Compatibility renderer.
2. 960×540 내부 해상도와 1280×720 레터박스 QA.
3. Phase 0 AutoLoad 미사용.
4. Resource·JSON·CSV 경계.
5. 공용 10개 archetype과 20개 Visual Profile 골격.

추천안 전체 승인 표현:

```text
제안서 승인
```

### 현재 금지

- `project.godot`, Scene, GDScript, Resource, 데이터, 테스트 생성.
- 구현 브랜치와 PR.
- 기술 선택을 코드로 사실상 고정.

### Gate 완료 기준

- 사용자가 추천안 또는 수정안을 명시적으로 승인한다.
- 수정안이 있으면 제안서·Issue·Active Context를 다시 동기화한다.
- 승인 범위와 제외 범위가 한 문서에서 명확하다.

---

## 6. Phase P1 — Godot 기술 기준선

사용자 승인 뒤 별도 구현 브랜치와 PR로 진행한다.

### P1.1 프로젝트·화면 기준선

구현:

- `project.godot`.
- Godot 4.7.1 standard.
- Compatibility renderer.
- 960×540 viewport와 1920×1080 window 기준.
- Main Scene과 bootstrap status panel.
- `.godot/`과 로컬 생성물 Git 제외.

완료:

- editor와 headless에서 프로젝트가 열린다.
- 1920×1080에서 픽셀 probe가 정확히 2배 확대된다.
- 1280×720 레터박스와 UI 가독성 결과를 기록한다.

### P1.2 시간·시드·입력 로그

구현:

- GameSession.
- CombatClock.
- DeterminismService.
- InputLog.
- 60Hz active combat tick.
- planning pause.
- 이름 기반 RNG stream.

완료:

- planning 중 UI는 동작하고 active tick은 증가하지 않는다.
- 같은 seed와 input log는 같은 결과를 낸다.
- 하나의 RNG stream 호출 변화가 다른 stream을 바꾸지 않는다.

### P1.3 typed Resource 스키마

구현:

- UnitArchetypeProfile.
- TierProfile.
- RankProfile.
- FactionVisualProfile.
- AnimationContract.
- BattlefieldProfile.
- BootstrapCatalog.

완료:

- Inspector에서 타입이 확인된다.
- 필수 ID·참조 누락이 validator에서 실패한다.
- 런타임 체력·타깃·타이머를 정적 Resource에 저장하지 않는다.

### P1.4 공용 병종·진영 Visual 골격

구현:

```text
UnitArchetype 10개
Tier 3개
player Rank 4개
AnimationContract 10개
allied Visual Profile 10개
veil Visual Profile 10개
```

- placeholder 이미지는 진영별 두 장을 공유할 수 있다.
- 실제 능력·밸런스·개별 아트는 만들지 않는다.

완료:

- 공용 archetype 수가 정확히 10개다.
- 모든 archetype에 양 진영 Visual Profile이 존재한다.
- `EnemyUnitProfile`, Enemy Unit Scene과 적군 전용 전투 데이터가 없다.
- visual faction 변경 전후 전투 데이터가 동일하다.

### P1.5 Registry·Manifest·전장 계약

구현:

- DataRegistry.
- StageManifest JSON loader.
- bootstrap BattlefieldProfile.
- ID·중복·참조·금지 필드 validator.

완료:

- StageManifest가 공용 archetype만 참조한다.
- 직접 HP·공격·스킬 복사 필드가 실패한다.
- BattlefieldProfile이 3라인·성문 6개·거점·노드·assassin 우회를 검사한다.

### P1.6 Visual Contract probe

구현:

- 같은 archetype의 allied/veil placeholder 나란히 표시.
- 공용 AnimationContract 상태 순환.
- frame count·pivot·impact/projectile event 비교.

완료:

- `visual_faction_id`만 변경해 이미지가 바뀐다.
- 양 진영이 같은 AnimationContract를 참조한다.
- 상태·프레임·피벗·이벤트 불일치가 조용히 대체되지 않고 실패한다.

### P1.7 테스트·문서·다음 Gate

검증:

```powershell
$env:GODOT_BIN = "C:\Tools\Godot\Godot_v4.7.1-stable_win64_console.exe"
& $env:GODOT_BIN --version
& $env:GODOT_BIN --headless --path . --editor --quit
& $env:GODOT_BIN --headless --path . --script res://tests/run_all.gd
& git diff --check
```

문서 갱신:

- README 실행·검증 명령.
- `docs/GODOT_PROJECT_STRUCTURE.md` 실제 경로.
- Handoff·Active Context·Roadmap.
- Goal 0002와 Issue #32의 실제 파일·명령.

### Phase P1 종료 기준

- 프로젝트 headless 로드 PASS.
- 모든 계약 테스트 PASS.
- 실패 fixture가 예상 오류로 실패.
- 1920×1080·1280×720 수동 결과 기록.
- 실제 경로와 명령이 책임 문서와 일치.
- 수직 슬라이스 구현은 아직 시작하지 않음.

---

## 7. Gate 2 — 핵심 수직 슬라이스 제안서

책임:

- Issue #32.
- `docs/goals/0002-core-vertical-slice.md`.
- Issue #33 애니메이션·연출 계약.

Phase 0 구현 뒤 실제 파일과 명령을 기준으로 제안한다.

### 제안할 플레이 흐름

```text
베일의 징조
→ 건설
→ 룰렛
→ 병력 배치
→ 3라인 교전
→ 접전지·중간거점 점령
→ 암살자 우회
→ 성문 공성
→ 스테이지 승리
```

### 제안할 실제 구조

- Battle Scene tree와 상태 소유.
- 3라인 이동 그래프.
- 성문 6개.
- 중간거점·접전지 상태 머신.
- 전방 2·후방 1 건설 노드.
- 최소 건물 2종.
- 최소 3×3 룰렛.
- 대표 공용 archetype 3~5종.
- 각 대표 archetype의 allied/veil Visual Set.
- 첫 네 공세.
- 암살자 우회 또는 공성 역할.
- 이동·공격·피격·사망·승리 모션.
- 디버그 overlay와 결정론 재현.
- 자동·수동·성능 검증.

### Gate 완료 기준

- 실제 Phase 0 경로와 명령을 사용한다.
- 범위를 작은 end-to-end 단계로 나눈다.
- 플레이어가 볼 수 있는 결과가 각 단계에 있다.
- 전체 10병종·전체 캠페인·최종 아트는 제외한다.
- 사용자 승인 전 구현하지 않는다.

---

## 8. Phase P2 — 10~15분 핵심 수직 슬라이스

### 목표

한 맵에서 오멘워드의 차별점과 가장 위험한 가정을 검증한다.

```text
건물로 룰렛 풀을 만든다
→ 예고된 공세를 읽는다
→ 병력을 세 라인에 나눈다
→ 거점·우회·성문으로 전선을 뒤집는다
```

### 최소 콘텐츠

- 한 개의 3라인 전장.
- 성문·중간거점·접전지.
- 포탑과 기본 병영 또는 바리케이드.
- 3×3 룰렛, 일반·엘리트.
- 첫 네 공세.
- 대표 공용 archetype 3~5종.
- allied/veil 이미지 세트.
- 암살자 우회 또는 거인 공성.
- 벨루 HUD 더미.
- 최소 승리·패배·재시도.

### 제외

- 공용 10병종 전체 스킬.
- 영웅·전설 전체.
- W1~20 전체.
- 절차 생성 전체.
- 최종 UI·아트·음악·성우.
- 성문 수리·재건.
- 암살자 탐지 건물.

### 핵심 검증 질문

1. 플레이어가 다음 공세와 위험 라인을 읽는가?
2. 건물 선택이 룰렛 확률에 체감 가능한 영향을 주는가?
3. 룰렛 결과를 어느 라인에 둘지 고민하는가?
4. 중간거점의 건설권·수입 이전이 전선을 바꾸는가?
5. 암살자 우회가 순간이동이 아니라 예고된 침투로 읽히는가?
6. 공성 역할이 성문 돌파 시간을 의미 있게 바꾸는가?
7. 같은 archetype의 양 진영 전투 결과가 동일한가?
8. 화면이 혼잡해도 병종·진영·전조를 읽을 수 있는가?

### 종료 기준

- 10~15분 플레이 경로 완주.
- 핵심 루프 최소 두 번.
- 첫 역전과 첫 전문화 체감.
- 공용 데이터·양 진영 Visual 계약 유지.
- 주요 결과 seed·input log 재현.
- 성능 정상 목표에서 60fps 기준 계측.
- 사용자 플레이테스트 기록과 다음 조정 목록.

---

## 9. Phase P3 — 시스템 안정화·밸런스

수직 슬라이스가 핵심 재미를 입증한 뒤 진행한다.

### 확률·룰렛

- 최소 100,000시드 분포.
- 금화 기대값 회전비 30% 이하 검증.
- 럭키 실패 누적과 6회 보장.
- 전설 스테이지 1회 제한.
- 건물 파괴·비활성 후 토큰 반영 시점.

### 경제

- 기본·시장·접전지·중간거점 수입 시간축.
- 건물 회수시간.
- 특수병단 준비 할인.
- 식량 부족 완성 대기.
- 점령·폐허·생산 재개.

### 전투

- 공통 피해 공식·방어·저항.
- Tier·Rank 배율.
- 병종 상성.
- 상태이상과 보스 제어.
- 타깃 재탐색 주기.
- 공격 판정과 시각 이벤트 오차.

### 성능

정상 목표:

```text
지상 유닛 120
비행 유닛 24
대형 8
투사체 160
VFX 80
건물 36
```

하드 안전 상한과 갱신 주기를 실제 프로파일링으로 조정한다.

### 종료 기준

- 동일 시드 회귀 테스트.
- 경제·확률 자동 시뮬레이션.
- 대표 전투 match-up 테스트.
- 객체 정상 목표에서 성능 기준 충족.
- 주요 PoC 수치가 채택·수정·제외로 분류됨.

---

## 10. Phase P4 — 콘텐츠·아트 확장

핵심 시스템이 안정된 뒤 단계적으로 확장한다.

### 병종

- 공용 10병종 전체.
- Tier 2 전문화.
- Tier 3 후보.
- 일반·엘리트·영웅·전설 능력 계보.
- archetype별 allied/veil 최종 Visual Set.

적군 전용 전투 데이터를 추가하지 않는다.

### 건물

- 기본 병영 6종 전문화.
- 특수병단 4종.
- 농장·시장·포탑.
- Tier 2·3 효과와 제작 자산.

### 웨이브·보스

- W1~15 표준 구조.
- W16~19 초과 공세.
- W20 신화 보스.
- StageManifest·WavePatternCard.
- 보스 행동·페이즈·전용 Visual Set.

### 캠페인

- 튜토리얼 1.
- 정규 스테이지 9.
- 약 3시간 진행.
- 병종·전장·위협의 단계적 소개.
- 결정론적 절차 조합과 validator.

### 아트·연출

- 실제 전략 줌 실루엣 검수.
- 양 진영 프레임·피벗·이벤트 호환.
- 벨루 표정과 상태 반응.
- 공격·점령·성문 붕괴·승리 연출.
- UI 아이콘·팔레트·오디오.

---

## 11. Phase P5 — 데모·출시 준비

### 품질

- 첫 10분 이탈 구간과 이해도 측정.
- 1920×1080·1280×720·창 모드 검증.
- 한국어·영문 UI 길이.
- 색각·텍스트·입력 접근성.
- 튜토리얼 스킵·재학습.

### 안정성

- 저장·불러오기와 버전 호환.
- seed·Manifest·입력 로그 회귀.
- 장시간 실행과 메모리.
- 오류 보고와 안전 fallback.

### 패키징

- Windows export preset.
- Steam 데모 빌드.
- 라이선스·크레딧.
- 옵션·키 바인딩·오디오.
- 소개 이미지와 스토어 문구.

### 출시 게이트

- 치명적 진행 차단 0.
- 주요 데이터 참조 오류 0.
- 공용 archetype·Visual 계약 자동 검사 PASS.
- 대표 PC 환경 성능 기준 충족.
- 첫 10분과 전체 데모 수동 QA PASS.

---

## 12. 단계 공통 운영 규칙

- 한 번에 하나의 승인된 Issue/Goal만 구현한다.
- 문서 작업과 게임 구현을 같은 커밋에 섞지 않는다.
- 실제 파일을 확인하기 전 경로·API를 단정하지 않는다.
- 정상 동작 중인 사용자 변경사항을 되돌리지 않는다.
- 범위 밖 필요가 발견되면 구현을 멈추고 제안서 수정으로 돌아간다.
- 테스트하지 못한 결과는 완료로 보고하지 않는다.
- 이전 버전은 Git 이력으로 보존하고 활성 문서는 최신 기준만 유지한다.
- 프로젝트 해결안은 먼저 프로젝트에서 검증하고 공용 가치가 확인된 교훈만 Base cases로 승격한다.

---

## 13. 지금 해야 하는 단 하나의 결정

현재는 Phase 0 구현을 시작하는 단계가 아니라 제안서를 승인하거나 수정하는 단계다.

추천안 전체로 진행할 때의 승인 표현:

```text
제안서 승인
```

승인 전 상태:

```text
Phase 0 제안서 사용자 검토 대기
게임 구현 전
```
