# 오멘워드 문서 아카이브

이 폴더는 과거 결정·증거·파생본을 복구 가능하게 보존하는 비활성 영역입니다.

- 이 경로의 자료는 현재 정본이 아니며 구현 권한이 없습니다.
- 현재 기준은 `docs/DOCUMENTATION_MAP.md`, 활성 `docs/design/APPROVED_*.md`와 `MANIFEST.json`의 `superseded_by`에서 확인합니다.
- 원문을 비우지 않습니다. 경로만 남기고 본문을 삭제하는 방식은 금지합니다.
- 실제 아카이브 항목은 원래 경로, 현재 경로, SHA-256, 대체 정본, 사유, rollback ref와 검증 상태를 기록합니다.
- 비밀키·API token·자격증명·private key는 아카이브하지 않습니다.
- inactive Skill은 `docs/base/SKILL_REGISTRY.json`의 `inactive`·`replaced_by`·alias 계약을 유지하며 Router가 직접 선택하지 않습니다.
- Git branch는 폴더로 이동할 수 없습니다. unique commit 감사와 rollback tag 검증 뒤 삭제 가능할 때만 별도 처리합니다.
- 일반적인 이전 버전은 Git 이력으로 복구하며, 외부 납품본·대규모 방향 전환 비교본·링크 호환 문서만 분류와 Manifest를 갖춰 보관합니다.

현재 이 폴더에는 정책 파일만 있으며 이번 채택 작업에서 기존 구형 자료를 이동하거나 삭제하지 않습니다.
