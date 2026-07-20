# 활성 OMENWARD 작업 경로

이 폴더가 Godot에서 열고 실행할 활성 정본입니다.

- 로컬 경로: `C:\Users\user\Documents\바이브코딩\omenward-base-full-11-migration\omenward`
- 로컬 브랜치: `codex/omenward-active`
- 추적 원격: `origin/codex/issue-41-base-pr18-refresh`
- GitHub 저장소: `https://github.com/alsdmlals4-eng/omenward`

## 동기화

다른 환경에서 푸시된 변경을 받기 전에는 이 폴더에서 다음을 실행한다.

```powershell
git status
git pull
```

`git status`가 깨끗해야 한다. 변경을 만들었다면 검증·커밋 후 작업자는 활성 원격 브랜치로 푸시한다.

## 보존본

이전 `main` 작업본과 사용자의 미커밋 아트·설정 변경은 다음 경로에 복구 가능하게 보관한다.

`C:\Users\user\Documents\바이브코딩\omenward-base-full-11-migration\omenward-pre-cutover-20260720`

원본 변경은 원래 Git 저장소의 `stash@{0}: pre-cutover-20260720-user-art-and-project-config`에도 보존되어 있다. 보존본은 활성 실행·구현 기준이 아니다.
