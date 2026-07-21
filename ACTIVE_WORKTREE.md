# OMENWARD 활성 Git 작업 기준

이 문서는 저장소의 활성 브랜치와 동기화 절차만 기록한다. 로컬 절대경로·개인 캐시·stash 번호는 환경별 정보이므로 프로젝트 정본이 아니다.

- GitHub 저장소: `alsdmlals4-eng/omenward`
- 기본 브랜치: `main`
- 현재 통합 PR 브랜치: `codex/omenward-active`
- 현재 PR: `#45`

## 안전한 동기화

```powershell
git fetch origin
git status
git switch codex/omenward-active
git pull --ff-only origin codex/omenward-active
```

- `git status`가 깨끗하지 않으면 pull·rebase·merge 전에 사용자 변경을 커밋하거나 별도 stash/백업으로 보존한다.
- 로컬 브랜치의 upstream이 `origin/codex/omenward-active`인지 `git branch -vv`로 확인한다.
- 현재 PR은 `main`과 diverged 상태이므로 충돌 해결 전 강제 push·브랜치 초기화·파일 일괄 덮어쓰기를 금지한다.
- 로컬 백업·stash는 해당 환경에서 실제 존재를 확인한 뒤에만 복구 근거로 사용한다.

## 검증

브랜치를 최신화한 뒤 Python 계약 검사, 활성 Markdown 링크, 문서 발행 재생성, Godot import·headless·runtime smoke를 실행한다. 실행하지 않은 검사는 `NOT_RUN`으로 기록한다.
