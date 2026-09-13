param([Parameter(Mandatory = $true)][string]$Godot)
$ErrorActionPreference = 'Stop'
$projectRoot = Split-Path $PSScriptRoot -Parent
foreach ($testScript in @('tests/replan_slice_test.gd', 'tests/replan_screen_test.gd')) {
    $testOutput = & $Godot --headless --path $projectRoot --script $testScript 2>&1
    $testExit = $LASTEXITCODE
    $testOutput | Write-Output
    if ($testExit -ne 0 -or ($testOutput -match '(^|\s)(SCRIPT ERROR:|ERROR:)')) { throw "Replan verification failed: $testScript ($testExit)" }
}
$smokeOutput = & $Godot --headless --path $projectRoot --quit-after 10 2>&1
$smokeExit = $LASTEXITCODE
$smokeOutput | Write-Output
if ($smokeExit -ne 0 -or ($smokeOutput -match '(^|\s)(SCRIPT ERROR:|ERROR:)')) { throw 'Default scene smoke failed' }
Write-Output 'REPLAN_LOCAL_GATE_PASS (model + UI/save + default scene; not full-project/Human/CI approval)'
