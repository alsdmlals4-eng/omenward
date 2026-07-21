# Base 규칙·공용 지식 버전

- 원본 저장소: `alsdmlals4-eng/Base`
- 기준 커밋: `41a20584dd2ee51d917e5c9d7cab6838e1ceba7e`
- 동기화 기준일: `2026-07-22`
- 적용 정책: Omenward 정본 우선·명시적 채택·자동 덮어쓰기 금지
- 기계 정본: `docs/base/SKILL_REGISTRY.json`
- Base 기능 보존표: `docs/base/BASE_CAPABILITY_COVERAGE.json`
- 공통 실행 계약: `skills/SHARED_EXECUTION_CONTRACT.md`

## 채택 결과

Base 활성 Skill 25개의 입력·산출물·권한·검증 책임을 모두 Omenward에 매핑했다. Omenward의 기존 11개 분야 Skill을 활용해 전문 기능을 mode로 통합하고, 독립 경계가 필요한 프로젝트 코어·적대적 검토·가지치기·본문 간소화·계약 보존 리팩토링만 별도 Foundation으로 유지했다.

```text
Base 25개 책임
→ Omenward Foundation 12개 + Discipline 11개
→ 총 23개 패키지
```

## 보호 원칙

- 게임 코드·Scene·Resource·데이터·승인 자산·세계관·수치는 Base 구조에 맞춰 임의 변경하지 않는다.
- Base의 파일 구조·예시·프로젝트 사례를 통째로 복사하지 않는다.
- 과거 Skill ID는 `skills/LEGACY_SKILL_ALIASES.json`으로 해석하며 새 계약에는 현행 ID만 사용한다.
- 기능 축소 여부는 파일 수가 아니라 `BASE_CAPABILITY_COVERAGE.json`과 회귀 테스트로 판정한다.
