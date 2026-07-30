# Base 공용 Skill 연결 기준

이 문서는 `omenward`가 Base 공용 Skill을 프로젝트에 복제하지 않고 v9.1 계약과 생성 route view로 사용하는 현재 연결의 사람용 안내다.

## 고정 기준

- Base 저장소: `alsdmlals4-eng/Base`
- Base v9.1 release/evidence pin: `3c158f52cfdad889970aef4d6ce6650a6fea0645` / `dd20ad3852e264d7e337e34d2cb963f71053a6cb`
- 프로젝트 계약 정본: `skills/PROJECT_BASE_ADAPTER.json`
- 생성 route view: `skills/PROJECT_SKILL_SNAPSHOT.json`
- 레거시 보존 어댑터: `docs/archive/ARCHIVE_RETENTION_ADAPTER.json`
- 프로젝트 고유 Skill Registry: `skills/SKILL_REGISTRY.json`

`docs/base/SKILL_REGISTRY.json`과 `skills/BASE_SHARED_SKILL_ROUTES.json`은 한 전환 주기 동안 보존하는 호환 자료이며 자동 라우팅에 사용하지 않는다.

## 라우팅 원칙

```text
작업 요청
→ skills/PROJECT_BASE_ADAPTER.json
→ skills/PROJECT_SKILL_SNAPSHOT.json의 effective_routes
→ Base pin과 프로젝트 경로·정본·검증기 확인
→ omenward 고유 전투·룰렛·성장 판단이 필요할 때만 프로젝트 Skill 선택
```

- Base 공용 Skill 본문을 프로젝트에 복사하지 않는다.
- Base 메인 Registry의 공용 Skill은 `base_registry_route`를 통해 프로젝트 어댑터를 사용한다.
- 프로젝트 전용 Skill은 omenward의 전투 판정, 결정론적 결과, 룰렛과 데이터 계약처럼 다른 프로젝트에 직접 적용할 수 없는 책임만 소유한다.
- 기존 로컬 공용 Skill 복사본은 즉시 삭제하지 않고 레거시 보존 Skill로 별도 판정한다.

## 명시적 extension route

| route | Base Skill | 프로젝트 어댑터 |
|---|---|---|
| `legacy_retention_and_archives` | `governing-legacy-retention-and-archives` | `docs/archive/ARCHIVE_RETENTION_ADAPTER.json` |
| `godot_assets_before_creation` | `evaluating-godot-assets-and-plugins-before-creation` | `skills/PROJECT_BASE_SKILL_ADAPTER.json` |

## Godot 직접 생성 전 조사

```text
Godot 기본 기능
→ 공식 Godot Asset Store
→ 기존 Godot Asset Library
→ 제작자 GitHub 안정 Release·tag
→ itch.io
→ 제작자 공식 판매처·신뢰 가능한 상용 마켓
→ 평가 후 ADOPT / ADAPT / TRIAL / REJECT / BUILD_CUSTOM
```

omenward에서는 룰렛, 결정론 테스트, 3라인 전투 보조, 상태 머신, 디버그 시각화와 데이터 검증을 우선 조사한다. 핵심 전투 판정, 결정론적 결과 규칙과 게임 데이터 정본은 범용 플러그인에 위임하지 않는다.

## 기록 위치

- 조사·채택 자산: `docs/technical/ADOPTED_ASSETS.md`
- 라이선스·크레딧: `docs/technical/THIRD_PARTY_LICENSES.md`
- 아카이브 기계 인덱스: `docs/archive/MANIFEST.json`

## 검증

```bash
python tests/test_base_shared_skill_adapter.py
python tools/check_archive_governance.py
python tools/validate_skill_system.py
```

Godot 실행·Windows 빌드·사람 플레이는 실제 실행 전까지 `NOT_RUN`이다.
