# OMENWARD 프로젝트 인수인계 컨텍스트

- 갱신일: 2026-07-16
- 현재 단계: **프리프로덕션 구조 승인 완료 / Phase 0 기술 제안서 작성 완료·사용자 검토 대기 / 게임 구현 전**
- 현재 제안서: `docs/design/proposals/0001-phase-0-godot-bootstrap.md`
- 현재 Issue·Goal: Issue #1 / `docs/goals/0001-engine-selection-and-bootstrap.md`
- 다음 행동: 제안서 검토·수정 또는 명시적 승인
- 최신 통합 원본: `docs/design/APPROVED_PREPRODUCTION_POC_BASELINE_V1.md`

이 문서는 새 ChatGPT, Codex, 기획자, 아티스트 또는 개발자가 이전 대화 없이도 오멘워드의 제품 방향, 데이터 소유, 현재 상태, 금지 범위와 다음 작업을 이해하기 위한 시작점이다. 세부 수치와 규칙은 링크된 책임 원본을 따른다.

---

## 1. 지금 가장 먼저 알아야 할 것

1. 오멘워드는 아직 Godot 게임 구현 전이다.
2. `project.godot`, Scene, GDScript, Resource와 테스트는 현재 존재하지 않는다.
3. Phase 0 기술 제안서는 작성됐지만 아직 사용자가 승인하지 않았다.
4. 사용자 승인 전 구현 브랜치·커밋·PR과 게임 파일 생성을 시작하지 않는다.
5. 적군 병종 데이터를 별도로 만들지 않는다.
6. 공용 병종 10개에 아군 이미지 세트 또는 적군 이미지 세트를 연결한다.
7. 다음 구현 단계는 전체 게임이 아니라 Godot 기술 기준선 Phase 0이다.

현재 상태를 구현 완료로 오해하지 않는다.

```text
기획 승인
≠ 제안서 승인
≠ 구현 완료
≠ 플레이테스트 검증
```

---

## 2. 최초 읽기 순서

```text
1. AGENTS.md
2. docs/BASE_RULES_VERSION.md
3. docs/HANDOFF_CONTEXT.md
4. docs/DOCUMENTATION_MAP.md
5. docs/OMENWARD_GAME_DESIGN.md
6. 현재 작업과 관련된 APPROVED 책임 문서
7. docs/OMENWARD_ROADMAP.md
8. 현재 Issue / Goal / 제안서
9. 실제 코드·데이터·Scene·테스트
10. docs/ACTIVE_CONTEXT.md
```

Phase 0 검토 시 추가 필수:

- `docs/PROPOSAL_WORKFLOW.md`
- `docs/GODOT_PROJECT_STRUCTURE.md`
- `docs/design/APPROVED_PERFORMANCE_DATA_TEST_READINESS_POC_V1.md`
- `docs/design/APPROVED_SHARED_UNIT_ARCHETYPE_AND_FACTION_VISUAL_DATA_V1.md`
- `docs/design/proposals/0001-phase-0-godot-bootstrap.md`
- Issue #1

모든 문서를 무조건 읽지 않고 `DOCUMENTATION_MAP.md`에서 작업별 책임 원본을 선택한다.

---

## 3. 제품 약속

### 한 문장

> 건물을 지어 룰렛 확률과 증원 체계를 설계하고, 베일의 징조로 예고된 공세를 세 전선에서 뒤집는 판타지 전략 오토배틀 게임.

### 핵심 플레이 경험

플레이어는 다음 공세의 라인과 위협 태그를 미리 읽고, 제한된 금화·식량·건설 노드 안에서 건물과 룰렛 확률을 설계한다. 룰렛으로 얻은 병력을 원하는 라인에 배치하고, 접전지·중간거점·성문·암살자 우회로를 이용해 위기를 역전한다.

### 핵심 루프

```text
베일의 징조 확인
→ 건물·토큰·전술 선택
→ 3×3 룰렛
→ 병력 획득·라인 배치
→ 3라인 교전
→ 접전지·중간거점 공방
→ 암살자 우회 또는 성문 공성
→ 다음 공세 준비
```

### 첫 10분 약속

- 세계관과 전선 위기를 짧게 이해한다.
- 건설→룰렛→배치→역전을 두 번 체험한다.
- 이동권 조작으로 상위 등급의 강함을 체감한다.
- 방패병·대검전사·암살자 중 첫 전문화를 선택한다.
- 설명보다 행동과 즉시 반응으로 시스템을 학습한다.

---

## 4. 변경 시 사용자 승인이 필요한 불변 구조

### 전장

```text
아군 본진
→ 라인별 아군 성문
→ 아군 중간거점
→ 중앙 접전지
→ 적 중간거점
→ 라인별 적 성문
→ 적 본진
```

- 좌우 대칭의 독립된 상·중·하 3라인.
- 일반 유닛의 라인 간 횡단과 기본 라인 변경 없음.
- 각 라인에 진영별 독립 성문 1개, 총 6개.
- 각 중간거점에 전방 건설 노드 2개와 후방 노드 1개.
- 중간거점 점령 시 건설권과 기본 생산권 이전.
- 중앙 접전지는 다른 라인과 연결되지 않고 건설 불가.
- 암살자는 적 후방 직접 배치가 아니라 같은 라인의 안개 우회로 사용.
- 기본 전략 화면에 전장 전체가 들어오므로 미니맵 없음.
- 건물 점유 영역은 주 도로를 완전히 막지 않음.

책임 원본: `docs/design/APPROVED_BATTLEFIELD_TOPOLOGY_AND_SCALE_V1.md`

### 공용 병종 데이터

오멘워드에는 전투 규칙 기준 병종 아키타입이 정확히 10개뿐이다.

```text
UnitArchetypeProfile × 10
+ TierProfile
+ RankProfile
+ owner_team_id
+ FactionVisualProfile
```

공유:

- HP·공격·방어·사거리·이동.
- 스킬·패시브·타기팅.
- 점령력·구조물 피해.
- Tier·Rank 적용.
- 이동·공격·피격·사망 상태.
- AnimationContract와 판정 이벤트 타이밍.

분리:

- 소유 팀과 적대 관계.
- 룰렛·생산 또는 웨이브라는 출격 방식.
- 스프라이트·초상화·아이콘·팔레트.
- 세계관 표시명과 설명 문구.

금지:

- 별도 `EnemyUnitProfile`.
- 아군 Unit Scene을 복사한 Enemy Unit Scene.
- 적군 전용 stats·skills·targeting·AnimationContract.
- 진영별 숨은 Tier·Rank 배율.
- 표시명 차이를 이유로 새 combat archetype ID 생성.

일반 적군 난이도는 수량, Tier, Rank, 라인 편성, 출격 시점과 생산시설 상태로 만든다.

W15·W20 보스:

```text
공용 base_archetype_id
+ BossBehaviorPackage
+ BossPhaseProfile
+ 전용 Visual Set
```

책임 원본: `docs/design/APPROVED_SHARED_UNIT_ARCHETYPE_AND_FACTION_VISUAL_DATA_V1.md`

### 등급과 Tier

- 플레이어 Rank: 일반·엘리트·영웅·전설.
- 플레이어 신화 Rank 없음.
- W20 신화는 보스 패키지 전용.
- Tier는 생산시설·병종 전문화 축.
- Rank는 룰렛 결과와 스킬 성장 축.

---

## 5. 공용 10병종

### 기본 병영

| archetype_id | 아군 표시명 | 역할 |
|---|---|---|
| `shield_guard` | 방패병 | 전열·원거리 대응 |
| `greatsword_warrior` | 대검전사 | 정면 범위·파쇄 |
| `assassin` | 암살자 | 같은 라인 우회·후열 제거 |
| `spearman` | 창병 | 돌진·대형 저지 |
| `archer` | 궁병 | 지속 원거리·대공 |
| `cavalry` | 기병 | 기동·돌진·후열 압박 |

### 특수병단

| archetype_id | 아군 표시명 | 역할 |
|---|---|---|
| `priest` | 사제 | 치유·전투 지원 |
| `mage` | 마법사 | 광역 마법·제어 |
| `flying_lancer` | 비행병 | 지상 전열 우회·후열 압박 |
| `giant` | 거인 | 대형 범위·방어·공성 |

적군 표시명과 이미지는 FactionVisualProfile이 소유하며 전투 데이터 ID를 새로 만들지 않는다.

---

## 6. 승인된 수직 슬라이스 전장 초기값

### 중간거점

```text
중립화 10초 + 점령 10초 at 점령력 1.0
최대 유효 점령력 2.0
진행 유지 3초
복귀 초당 10%
점령 완료 후 안정화 5초
소유 수입 금화 +2 / 30초
```

점령력:

- 방패·수호형 1.25.
- 일반 근접·기병 1.0.
- 원거리·지원·거인 0.5.
- 암살자·비행·순수 공성 병기 0.

처리:

- 점령 시도 중 생산·신규 건설·업그레이드 정지.
- 중립화 시 기존 건물 비활성.
- 점령 완료 시 기존 건물 폐허화, 환불 없음.
- 5초 안정화 후 새 소유자의 건설·생산 활성.

### 성문

```text
HP 5000
방어 80
마법저항 80
일반 구조물 피해 40%
공성 태그 피해 200%
고정 피해 50%
붕괴 2초
```

- 아군은 통과하고 적은 파괴 전까지 차단.
- 군중제어·밀쳐내기·비율 피해 면역.
- 폐허는 길을 막지 않음.
- 수직 슬라이스에서는 수리·재건 없음.

### 암살자 우회

```text
진입 준비 1초
오프맵 이동 9초
도착 2.5초 전 수비 경고
출현 후 준비 0.6초
적 중간거점에서 본진 방향 120 units
도착 영역 160 × 120 units
막힘 보정 반경 80 units
점령력 0
```

- 진입 확정 후 취소·후퇴 불가.
- 우회 중 전투·피격·점령·버프 없음.
- 경로는 암살자 선택·배치 중에만 표시.
- 탐지 전용 건물은 수직 슬라이스 제외.

위 수치는 PoC 초기값이며 구조를 유지한 채 플레이테스트로 조정할 수 있다.

---

## 7. 애니메이션·전투 연출 계약

공통 필수 상태:

```text
deploy
idle
move
attack_basic
skill_1
hit_light
death
victory
```

역할별 추가:

- 점령 가능 병종: `capture`.
- 암살자: `bypass_enter`, `bypass_exit`.
- 기병: `charge`, `turn_recover`.
- 비행병: 상승·순항·급강하·회복.
- 거인: `structure_attack`, `heavy_stagger`.

핵심 원칙:

- 공격은 준비→판정→회복으로 구분.
- 무기 접촉·투사체 발사와 실제 판정은 한 프레임 이내로 동기화.
- 이동 위치는 코드가 소유하며 루트 모션을 사용하지 않음.
- 가벼운 연속 피격은 큰 경직 대신 짧은 플래시·미세 반동.
- 공용 AnimationContract에 아군·적군 이미지 시트를 각각 맞춤.
- 적군 모션을 별도 상태 머신이나 타이밍 데이터로 제작하지 않음.
- 개별 처치마다 승리 모션을 재생하지 않음.
- 스테이지 승리는 2.5~4초 병종별 시퀀스 뒤 결과 UI.

책임 원본: `docs/design/APPROVED_UNIT_ANIMATION_AND_BATTLE_PRESENTATION_GUIDE_V1.md`

---

## 8. UI·아트 방향

- 기준 출력 1920×1080.
- 내부 해상도는 Phase 0 제안서에서 960×540을 추천하며 아직 승인 전.
- 기본 전략 줌에서 양측 본진과 세 라인 전체 확인.
- 미니맵 대신 실제 전장 위 성문·거점·접전지 상태 표시.
- 클린 전술 픽셀 + 미니어처 치비 + 고해상도 픽셀 재질.
- 병종은 얼굴보다 무기·자세·몸통·이동 리듬으로 식별.
- 진영·병종·등급을 색상만으로 구분하지 않음.
- 생성형 콘셉트는 탐색용이며 최종 자산은 픽셀·손·무기·관절·광원 후처리 필수.

책임 원본:

- `docs/design/APPROVED_ART_DIRECTION_AND_PRODUCTION_GUIDE_V1.md`
- `docs/design/APPROVED_UI_ART_AUDIO_POC_BIBLE_V1.md`

---

## 9. 경제·공세 기준

```text
시작 금화 160
시작 식량 12
기본 수입 +5 / 20초
중앙 접전지 +4 / 60초 / 소유 지점
중간거점 +2 / 30초 / 소유 지점
룰렛 비용 20
```

- 적 처치·웨이브 클리어 고정 금화 없음.
- active combat time 기준 60초마다 공세 충돌.
- W5 엘리트, W10 영웅, W15 전설 보스, W20 신화 보스.
- W15 보스 처치 표준 승리, 이전 적 본진 파괴는 조기 승리.
- 일반 적 웨이브는 공용 archetype을 Tier·Rank·수량·라인·시간으로 조합.

책임 원본:

- `docs/design/APPROVED_STAGE_ECONOMY_AND_BUILDING_COST_BASELINE_V1.md`
- `docs/design/APPROVED_ROULETTE_PROBABILITY_TARGETS_POC_V1.md`
- `docs/design/APPROVED_SHARED_ARCHETYPE_WAVE_1_20_POC_V1.md`

---

## 10. 현재 Phase 0 제안서

책임 문서: `docs/design/proposals/0001-phase-0-godot-bootstrap.md`

### 추천안

```text
Godot 4.7.1 standard x86_64
GDScript
Compatibility renderer
1920×1080 출력
960×540 내부 viewport
viewport stretch / keep aspect / integer scale
```

상태 소유:

```text
Main
└─ GameSession
   ├─ CombatClock
   ├─ DeterminismService
   └─ DataRegistry
```

- Phase 0 AutoLoad 없음.
- 60Hz `active_combat_tick`.
- planning 중 active tick 정지, UI는 계속 동작.
- master seed와 이름 기반 RNG stream.
- input log 기록·재생 골격.

데이터 경계:

- typed `.tres`: UnitArchetype·Tier·Rank·FactionVisual·AnimationContract·Battlefield.
- JSON: StageManifest·replay/input log.
- CSV: Phase 0 런타임 원본으로 사용하지 않음.

Phase 0 데이터 골격:

- 공용 UnitArchetype 10개.
- Tier 3개.
- player Rank 4개.
- AnimationContract 10개.
- allied Visual Profile 10개.
- veil Visual Profile 10개.
- 3라인 BattlefieldProfile 계약.
- bootstrap StageManifest.

애니메이션 권위:

```text
AttackProfile·active tick
→ 판정 예약
→ AnimationContract 이벤트 일치 검증
→ AnimatedSprite2D·AnimationPlayer 표현
```

제안서 추천은 아직 승인된 구현 사양이 아니다.

---

## 11. 현재 실행 순서

### Gate 1 — Phase 0 제안서 검토

현재 위치.

사용자가 검토할 항목:

- Godot 4.7.1 standard와 Compatibility renderer.
- 960×540 내부 해상도와 1280×720 레터박스 QA.
- Phase 0 AutoLoad 미사용.
- Resource·JSON·CSV 경계.
- 공용 10개 archetype과 20개 Visual Profile 골격 범위.

승인 표현:

```text
제안서 승인
```

질문·부분 동의·단순 진행 요청은 수정된 제안서 범위를 승인한 것으로 자동 간주하지 않는다.

### Gate 2 — Phase 0 구현

승인 뒤 별도 구현 브랜치와 PR에서 다음만 진행한다.

1. Godot 프로젝트·화면 기준선.
2. 시간·시드·입력 로그.
3. typed Resource 스키마.
4. 공용 10병종·양 진영 Visual 골격.
5. DataRegistry·StageManifest·Battlefield validator.
6. allied/veil Visual Contract probe.
7. headless 테스트와 실제 경로 문서화.

완료 조건:

- editor·headless 프로젝트 로드.
- 같은 seed·input log 재현.
- planning 중 active tick 정지.
- 공용 archetype 10개와 양 진영 Visual 존재.
- 적군 전용 데이터 복사본 없음.
- Visual 상태·프레임·피벗·이벤트 호환 검사.
- 3라인 topology 계약 검사.
- 실제 경로·명령을 Goal 0002와 Issue #32에 반영.

### Gate 3 — 수직 슬라이스 제안서

책임: Issue #32 / Goal 0002.

- 실제 3라인 그레이박스.
- 성문·중간거점·접전지.
- 최소 건설·경제·룰렛.
- 암살자 우회.
- 대표 공용 archetype 3~5종과 양 진영 이미지.
- 대표 이동·공격·피격·사망·승리 모션.
- 자동·수동·성능 검증.

사용자 승인 전 구현 금지.

### Gate 4 — 핵심 수직 슬라이스

10~15분 플레이에서 핵심 루프와 가장 위험한 가정을 검증한다. 전체 10병종 최종 아트, 전체 캠페인과 최종 밸런스는 범위 밖이다.

---

## 12. Phase 0에서 만들지 않는 것

- 실제 전투·피해 계산.
- 유닛 이동·타기팅·공격 AI.
- 3라인 Battle Scene.
- 룰렛·건설·경제·점령·성문·웨이브 실행.
- 실제 Unit 전투 Scene.
- 암살자 우회 동작.
- 최종 스프라이트·초상·아이콘·VFX·오디오.
- 캠페인 저장·불러오기.
- 외부 ECS·GDExtension·대형 애드온.
- 적군 전용 UnitProfile·Unit Scene·AnimationContract.

---

## 13. 구현 전·후 미확정 경계

제안서 승인으로 결정할 후보:

- Godot 4.7.1 standard.
- Compatibility renderer.
- 960×540 viewport 정책.
- Phase 0 AutoLoad 없음.
- typed Resource + JSON 경계.
- headless GDScript test runner.

Phase 0 구현 뒤 결정:

- 실제 경로와 노드 이름.
- 1280×720 레터박스 허용 여부.
- DataRegistry AutoLoad 승격 필요성.
- Visual placeholder의 전략 줌 가독성.

수직 슬라이스 플레이테스트로 조정:

- 유닛·건물·룰렛·웨이브 수치.
- 점령·성문·우회 시간과 대응성.
- 애니메이션 FPS와 프레임 수.
- 카메라 흔들림·히트 스톱 강도.
- 최종 팔레트·스프라이트·아이콘·오디오.

장기 콘텐츠에서 결정:

- 최종 적군 표시명과 보스 고유명.
- 전체 캠페인 대사와 스테이지 보스.
- 성문 수리·재건.
- 암살자 탐지 건물.
- 전체 Tier 3와 최종 밸런스.

---

## 14. Base 공용 지식 사용

Base 저장소는 프로젝트 규칙보다 낮은 공용 참고자료다.

- 인수인계: `Base/docs/knowledge/methods/PROJECT_HANDOFF_CONTEXT_METHOD.md`
- 아트 디렉션: `Base/docs/knowledge/methods/ART_DIRECTION_METHOD.md`
- 애니메이션·연출: `Base/docs/knowledge/methods/ANIMATION_AND_PRESENTATION_METHOD.md`
- 조사·벤치마킹: `Base/docs/knowledge/research/DESIGN_RESEARCH_AND_EVIDENCE_METHOD.md`
- 실무 검수: `Base/docs/knowledge/skills/`
- 일반화된 사례: `Base/docs/knowledge/cases/`

적용 순서:

```text
오멘워드 최신 사용자 결정·책임 문서
→ 현재 Issue·Goal·제안서
→ 실제 파일과 실행 결과
→ Base 공용 방법·스킬·사례
→ 외부 벤치마킹
```

Base의 사례와 방법을 그대로 복제하지 않고 오멘워드의 화면·성능·데이터 요구에 맞게 사용한다.

---

## 15. 하지 말아야 할 것

- 적군 10병종의 별도 스탯·스킬·애니메이션 데이터 제작.
- 아군 Scene을 복사해 Enemy Scene으로 분기.
- 미니맵 추가.
- 암살자 적 후방 직접 생성.
- 라인 간 일반 횡단로 추가.
- 중간거점 노드를 전방 2·후방 1 외 구조로 변경.
- 일반 공격마다 큰 화면 흔들림·히트 스톱 사용.
- 전설 등급을 크기와 발광만으로 표현.
- PoC 수치를 최종 밸런스로 고정.
- 승인 없이 Godot 코드·Scene·Resource·데이터·테스트 생성.
- 제안서 작성 완료를 구현 승인으로 해석.
- Base 또는 벤치마킹 자료가 최신 사용자 결정을 덮어쓰게 함.

---

## 16. 콜드 스타트 확인 질문

새 작업자는 문서를 읽고 10분 안에 다음을 답해야 한다.

1. 오멘워드의 핵심 루프는 무엇인가?
2. 현재 Godot 구현은 존재하는가?
3. Phase 0 제안서는 승인됐는가?
4. 지금 바로 `project.godot`을 만들어도 되는가?
5. 전장 불변 구조는 무엇인가?
6. 아군과 적군은 몇 개의 전투 병종 데이터를 사용하는가?
7. 적군과 아군의 차이는 어디에 저장하는가?
8. W15·W20 보스는 일반 적군 데이터와 어떻게 다른가?
9. 현재 제안서가 추천하는 엔진·화면·상태 소유는 무엇인가?
10. Phase 0과 수직 슬라이스의 범위 차이는 무엇인가?
11. 어떤 수치는 PoC 조정 가능하고 어떤 구조는 승인 대상인가?
12. Base와 프로젝트 책임 문서가 충돌하면 무엇이 우선하는가?

정확히 답하지 못하면 이 문서와 Documentation Map의 링크·상태·용어를 먼저 보강한다.
