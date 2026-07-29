# OMENWARD 프로젝트 AI 작업 규칙

이 저장소는 ChatGPT가 기획·문서·Issue·Goal을 정리하고, Codex가 승인된 범위 안에서 Godot 프로젝트를 구현하는 공동 작업용 저장소다.

## 규칙 우선순위

1. 사용자의 최신 지시.
2. 사용자가 승인한 Plan Mode 제안서와 현재 Issue·Goal.
3. `AGENTS.md`.
4. `docs/PROJECT_CORE.md`와 관련 V2 APPROVED 책임 원본.
5. 실제 코드·데이터·Scene·실행 증거.
6. 프로젝트가 고정한 Base 기준과 로컬 공용 규칙.
7. 외부 참고와 벤치마킹.

충돌하거나 불명확하면 추정해 구현하지 않고 `확인 필요`로 보고한다.

## 작업 전 읽기 순서

1. `AGENTS.md`
2. `docs/PROJECT_CORE.md`
3. `docs/design/APPROVED_CORE_V2_INTEGRATED_SPEC.md`
4. 작업별 세부 V2 APPROVED 문서
5. `docs/CURRENT_IMPLEMENTATION_STATUS.md`
6. `docs/HANDOFF_CONTEXT.md`
7. `docs/DOCUMENTATION_MAP.md`
8. 현재 Issue·PR·승인 제안서
9. 실제 코드·데이터·Scene·테스트
10. `docs/ACTIVE_CONTEXT.md`

모든 문서를 무조건 읽지 않고 Documentation Map으로 책임 원본을 선택한다.

## 역할 분리

- 기획/조정 AI: 플레이어 경험, 규칙, 범위, 책임 원본과 검증 기준을 정리한다.
- Codex Plan Mode: 실제 저장소를 읽기 전용으로 조사하고 구현 전 제안서를 작성한다.
- Codex 구현 모드: 사용자가 승인한 제안서와 Issue만 구현한다.
- 사용자: 방향, 우선순위, 제안서와 중요한 미확정 사항을 승인한다.

## GitHub 원칙

- 사용자 확정 규칙은 책임 원본과 현재 Issue·PR에 동기화한다.
- 문서 정본 변경과 제품 코드 구현을 같은 PR에 섞지 않는다.
- push·PR·검증에 실패한 작업을 반영 완료로 보고하지 않는다.
- Base 또는 다른 PR을 자동 병합하지 않는다.
- 과거 버전은 Git 이력을 사용하고 활성 폴더에 중복 정본을 만들지 않는다.

## Plan Mode 게이트

코드·Scene·Resource·게임 데이터 변경은 다음이 준비되기 전 시작하지 않는다.

- 사용자 승인 제안서.
- 목표와 플레이어 가치.
- 포함·제외 범위.
- 변경 파일과 상태 소유.
- Red 테스트와 완료 기준.
- 회귀·수동 검증.
- 마이그레이션과 롤백 기준.

질문, 의견과 부분 동의는 구현 승인으로 보지 않는다.

## 기술 불변 조건

- Godot 4.7.1 Standard, GDScript, Compatibility renderer.
- `.godot/`과 로컬 캐시를 커밋하지 않는다.
- Scene은 `scenes/`, Script는 `scripts/`, 정적 데이터는 `data/` 또는 `resources/`, 검증은 `tests/`에 둔다.
- AutoLoad는 여러 Scene이 공유해야 하는 상태에만 사용한다.
- 같은 상태를 두 객체가 동시에 책임 원본으로 소유하지 않는다.
- UI는 표시 데이터를 입력받고 사용자 의도를 반환하며 게임 규칙을 직접 계산하지 않는다.
- 공용 UnitArchetype과 진영 Visual 데이터를 분리한다.

## 프로젝트 코어 V2

```text
정확 공세 예고
→ TokenSource 건설로 세 원형 릴 설계
→ 회전·세로 이동·영구 가로 이동
→ 중앙 판정·명시적 확정
→ 보관·판매·라인 영구 배치
→ 3라인 자동전투·접전지·본진
→ 원인 확인과 다음 설계
```

불변:

- 일반 유닛의 라인 횡단 없음.
- 기본 난이도의 치명적 정보 은폐 없음.
- 가로 이동은 TokenInstance만 교환하며 길이·cursor 불변.
- X는 가장 낮은 안정 index부터 교체.
- stopped 보상은 immutable snapshot 사용.
- 이동 실행 즉시 소비·undo 없음.
- 숨김 럭키 15/25/35/45/55/100%.
- 전설은 5스테이지 위험 주기당 1회.
- 전술 아이템 룰렛 심벌은 보류.
- TokenSource 건물만 토큰 공급.
- 코어 PoC·첫 수직 슬라이스 mid-run save 없음.
- 배치 후 회수·라인 변경·판매 없음.

책임 원본:

- `docs/PROJECT_CORE.md`
- `docs/design/APPROVED_ROULETTE_CORE_RULES.md`
- `docs/design/APPROVED_MAPRUN_STAGE_WAVE_AND_MIDPOINT_CORE_V1.md`

## 기존 구현 해석

현재 C1·C2·C3는 `LEGACY_*_PROVEN`이다. 보존할 resolver·3라인·공용 데이터·원인 보고와 교체할 독립 9칸·구형 시간·점령 계약을 구분한다.

```text
LEGACY_PROVEN != V2_PROVEN
V2_SPEC_APPROVED != V2_IMPLEMENTED
```

## 구현 원칙

- 실제 호출 흐름과 테스트를 먼저 확인한다.
- 승인 범위 밖 기능과 리팩터링을 추가하지 않는다.
- 실패·경계 조건을 먼저 테스트한다.
- 기존 resolver 계약은 보존 seam을 만든 뒤 이동한다.
- 가역 adapter를 사용하고 전환 커밋을 작게 나눈다.
- 변경 뒤 Godot import, 관련 headless, 전체 회귀, 실제 플레이 순으로 검증한다.

## 완료 보고

- 변경 파일과 이유.
- 실행한 검증과 결과.
- 미실행 항목.
- legacy 보존·V2 교체 경계.
- 잔여 위험과 롤백.
- 사용자 확인 항목.

테스트하지 않은 항목을 완료했다고 보고하지 않는다.

## GDD Google Sheets 계약

- `docs/PROJECT_GOOGLE_SHEET_WORKBOOK.md`와 실제 Sheet를 GitHub 정본과 함께 읽는다.
- Sheet는 `USER_FACING_GDD_WORKSPACE`이며 독립 정본이 아니다.
- GitHub에 없는 편집은 `PROPOSED_SHEET_CHANGE`로 보존한다.
- 승인 후 GitHub와 Sheet를 모두 재조회한 경우에만 `SYNCED`로 판정한다.
- 생성 이미지와 실제 적용·런타임 승인 상태를 구분한다.
