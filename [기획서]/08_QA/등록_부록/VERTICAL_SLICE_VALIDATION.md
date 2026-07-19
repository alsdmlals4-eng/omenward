# Vertical Slice Validation

## Automated

Run from the active Issue #41 worktree with Godot 4.7.1 console. Editor import must run before the six scripts and runtime smoke:

```powershell
C:\Users\user\.cache\omenward-tools\godot-4.7.1\Godot_v4.7.1-stable_win64_console.exe --headless --path . --editor --quit
Get-ChildItem tests/headless/*_test.gd | ForEach-Object { & C:\Users\user\.cache\omenward-tools\godot-4.7.1\Godot_v4.7.1-stable_win64_console.exe --headless --path . -s ("res://tests/headless/" + $_.Name) }
C:\Users\user\.cache\omenward-tools\godot-4.7.1\Godot_v4.7.1-stable_win64_console.exe --headless --path . --quit-after 1
& C:\Users\user\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe -m unittest discover -s tests/python -v
git diff --check
```

The suite covers shared-unit data, three isolated lanes, gates, outposts, economy, building nodes, roulette, deployment, tutorial unlock, W1–W20 scheduling, and assassin bypass timing.

## Manual QA still required

1. Complete the tutorial, then start the regular stage.
2. Check roulette, build, deploy, and retry controls at 1920×1080.
3. Repeat at 1280×720 and confirm HUD, gates, outposts, and lane state remain readable.
4. Play through W1–W20 and inspect W15 legendary and W20 mythic milestones.
