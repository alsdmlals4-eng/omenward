# Omenward 검증 실행

활성 정본 `C:\Users\user\Documents\바이브코딩\omenward-base-full-11-migration\omenward`의 루트에서 다음 순서로 실행한다. Godot import가 전역 클래스 캐시를 준비하므로 headless보다 먼저 실행한다. 경로·원격 추적 정보는 루트의 `ACTIVE_WORKTREE.md`에서 확인한다.

```powershell
$godot = 'C:\Users\user\.cache\omenward-tools\godot-4.7.1\Godot_v4.7.1-stable_win64_console.exe'
& $godot --headless --path . --editor --quit
Get-ChildItem tests/headless/*_test.gd | Sort-Object Name | ForEach-Object { & $godot --headless --path . -s ("res://tests/headless/" + $_.Name) }
& $godot --headless --path . --quit-after 1
& C:\Users\user\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe -m unittest discover -s tests/python -v
git diff --check
```

문서 변경 뒤에는 Registry 기반 PDF·Manifest·Skill Map 생성, 활성 Markdown 링크 검사, PDF 전 페이지 렌더를 추가 실행한다. 1920×1080 및 1280×720 사람 플레이 QA는 실행 증거가 생길 때까지 `[미검증]`이다.
