[CmdletBinding()]
param(
    [string]$ProjectRoot = "C:\Users\user\Documents\GitHub\Ninza\omenward",
    [string]$BaseRoot = "C:\Users\user\Documents\GitHub\Base",
    [string]$Repository = "alsdmlals4-eng/omenward",
    [int]$IssueNumber = 174,
    [string]$ExecutionBranch = "runtime/barracks-role-output-implementation-20260809",
    [switch]$NonInteractive
)

$ErrorActionPreference = "Stop"
Set-StrictMode -Version Latest

function Assert-Command([string]$Name) {
    if (-not (Get-Command $Name -ErrorAction SilentlyContinue)) {
        throw "Required command '$Name' was not found in PATH."
    }
}

function Invoke-ExpectedNativeProbe([scriptblock]$Command) {
    # Windows PowerShell 5.1 can surface native stderr as NativeCommandError when
    # $ErrorActionPreference is Stop. Expected probes are allowed to return
    # nonzero, so temporarily make native stderr non-terminating and return only
    # the exit code to the caller.
    $savedPreference = $ErrorActionPreference
    try {
        $ErrorActionPreference = "Continue"
        & $Command 1>$null 2>$null
        return $LASTEXITCODE
    }
    finally {
        $ErrorActionPreference = $savedPreference
    }
}

function Get-ExactRequirement([string]$RequirementsPath, [string]$PackageName) {
    if (-not (Test-Path -LiteralPath $RequirementsPath -PathType Leaf)) {
        throw "Base requirements file is missing: $RequirementsPath"
    }
    $pattern = "^\s*$([regex]::Escape($PackageName))=="
    $line = Get-Content -LiteralPath $RequirementsPath | Where-Object { $_ -match $pattern } | Select-Object -First 1
    if ([string]::IsNullOrWhiteSpace($line)) {
        throw "Base does not declare an exact $PackageName requirement in $RequirementsPath"
    }
    return $line.Trim()
}

function Test-PythonRequirement([string]$Requirement) {
    $parts = $Requirement -split "==", 2
    if ($parts.Count -ne 2) {
        return $false
    }
    $packageName = $parts[0]
    $expectedVersion = $parts[1]

    # find_spec() avoids PackageNotFoundError traceback when the module is absent.
    # The metadata version check is evaluated only when the import is available.
    $probe = "import importlib.util as u, importlib.metadata as m, sys; sys.exit(0 if u.find_spec('$packageName') is not None and m.version('$packageName') == '$expectedVersion' else 1)"
    $exitCode = Invoke-ExpectedNativeProbe { & $script:PythonExecutable -c $probe }
    return ($exitCode -eq 0)
}

function Ensure-BaseValidatorDependency([string]$RequirementsPath) {
    $requirement = Get-ExactRequirement $RequirementsPath "jsonschema"
    if (Test-PythonRequirement $requirement) {
        Write-Host "Base validator dependency OK: $requirement" -ForegroundColor Green
        return
    }

    Write-Host "Recovering Base validator dependency from Base authority: $requirement" -ForegroundColor Yellow

    $pipProbe = Invoke-ExpectedNativeProbe { & $script:PythonExecutable -m pip --version }
    if ($pipProbe -ne 0) {
        Write-Host "pip is unavailable; attempting Python ensurepip recovery." -ForegroundColor Yellow
        & $script:PythonExecutable -m ensurepip --upgrade
        if ($LASTEXITCODE -ne 0) {
            throw "Could not bootstrap pip for Base validator dependency recovery."
        }
    }

    & $script:PythonExecutable -m pip install $requirement
    if ($LASTEXITCODE -ne 0) {
        Write-Host "Environment install failed; retrying user-site install." -ForegroundColor Yellow
        & $script:PythonExecutable -m pip install --user $requirement
        if ($LASTEXITCODE -ne 0) {
            throw "Could not install Base-authoritative dependency $requirement"
        }
    }

    if (-not (Test-PythonRequirement $requirement)) {
        throw "Installed dependency is still not visible to the active Python: $requirement"
    }
    Write-Host "Recovered Base validator dependency: $requirement" -ForegroundColor Green
}

Assert-Command git
Assert-Command gh
Assert-Command codex
Assert-Command python

$pythonCommand = Get-Command python -CommandType Application -ErrorAction Stop | Select-Object -First 1
$script:PythonExecutable = $pythonCommand.Source
if ([string]::IsNullOrWhiteSpace($script:PythonExecutable) -or -not (Test-Path -LiteralPath $script:PythonExecutable -PathType Leaf)) {
    throw "Could not resolve the exact Python executable used for Base validation."
}
$pythonExecutable = $script:PythonExecutable
$pythonDirectory = Split-Path -Parent $script:PythonExecutable
if ([string]::IsNullOrWhiteSpace($pythonDirectory) -or -not (Test-Path -LiteralPath $pythonDirectory -PathType Container)) {
    throw "Could not resolve the Python installation directory used for Base validation."
}

if (-not (Test-Path -LiteralPath $ProjectRoot -PathType Container)) {
    throw "Project root does not exist: $ProjectRoot"
}
if (-not (Test-Path -LiteralPath $BaseRoot -PathType Container)) {
    throw "Base repository does not exist: $BaseRoot"
}

Push-Location $ProjectRoot
try {
    $inside = (& git rev-parse --is-inside-work-tree 2>$null).Trim()
    if ($inside -ne "true") {
        throw "Not a git worktree: $ProjectRoot"
    }

    $origin = (& git remote get-url origin).Trim()
    if ($origin -notmatch "alsdmlals4-eng[/:]omenward(?:\.git)?$") {
        throw "Unexpected origin remote: $origin"
    }

    & git fetch origin --prune
    if ($LASTEXITCODE -ne 0) {
        throw "git fetch origin failed."
    }

    $dirty = @(& git status --porcelain)
    if ($dirty.Count -gt 0) {
        Write-Host "Working tree has unrelated/local changes:" -ForegroundColor Yellow
        $dirty | ForEach-Object { Write-Host "  $_" }
        throw "Refusing to discard or mix existing local work. Isolate/stash it intentionally, then run again."
    }

    $remoteBranchProbe = Invoke-ExpectedNativeProbe { & git show-ref --verify --quiet "refs/remotes/origin/$ExecutionBranch" }
    if ($remoteBranchProbe -ne 0) {
        throw "Remote execution branch is missing: origin/$ExecutionBranch"
    }

    $localBranchProbe = Invoke-ExpectedNativeProbe { & git show-ref --verify --quiet "refs/heads/$ExecutionBranch" }
    if ($localBranchProbe -eq 0) {
        & git switch $ExecutionBranch
    }
    else {
        & git switch --track -c $ExecutionBranch "origin/$ExecutionBranch"
    }
    if ($LASTEXITCODE -ne 0) {
        throw "Could not switch to $ExecutionBranch"
    }

    & git pull --ff-only origin $ExecutionBranch
    if ($LASTEXITCODE -ne 0) {
        throw "Could not fast-forward $ExecutionBranch from origin."
    }

    # The executor must be based on fresh main. If main moved beyond this branch,
    # stop instead of silently authoring against stale project state.
    $ancestorProbe = Invoke-ExpectedNativeProbe { & git merge-base --is-ancestor origin/main HEAD }
    if ($ancestorProbe -ne 0) {
        $mainSha = (& git rev-parse origin/main).Trim()
        $headSha = (& git rev-parse HEAD).Trim()
        throw "STALE_EXECUTION_BRANCH: origin/main=$mainSha is not an ancestor of HEAD=$headSha. Re-enter the OMENWARD Gate before authoring."
    }

    # Freshen the local Base authority without discarding or rewriting unrelated Base work.
    $baseInside = (& git -C $BaseRoot rev-parse --is-inside-work-tree 2>$null).Trim()
    if ($baseInside -ne "true") {
        throw "Base root is not a git worktree: $BaseRoot"
    }
    $baseDirty = @(& git -C $BaseRoot status --porcelain)
    if ($baseDirty.Count -gt 0) {
        Write-Host "Base worktree has local changes:" -ForegroundColor Yellow
        $baseDirty | ForEach-Object { Write-Host "  $_" }
        throw "Refusing to mutate a dirty Base worktree. Isolate Base changes before executor launch."
    }
    & git -C $BaseRoot fetch origin --prune
    if ($LASTEXITCODE -ne 0) {
        throw "Base git fetch origin failed."
    }
    $baseBranch = (& git -C $BaseRoot branch --show-current).Trim()
    if ($baseBranch -ne "main") {
        throw "Base must be on main for executor validation; current branch is '$baseBranch'."
    }
    $baseHead = (& git -C $BaseRoot rev-parse HEAD).Trim()
    $baseRemoteMain = (& git -C $BaseRoot rev-parse origin/main).Trim()
    if ($baseHead -ne $baseRemoteMain) {
        & git -C $BaseRoot pull --ff-only origin main
        if ($LASTEXITCODE -ne 0) {
            throw "Could not fast-forward local Base main to origin/main."
        }
    }

    # The Base operating-contract validator depends on the exact version declared
    # by Base itself. Recover only that declared dependency for the exact Python
    # executable that is also handed to child Codex for router-mandated revalidation.
    $baseRequirements = Join-Path $BaseRoot "requirements-publication.txt"
    Ensure-BaseValidatorDependency $baseRequirements

    $baseValidator = Join-Path $BaseRoot "tools\check_project_operating_contract.py"
    Write-Host "Running Base project operating-contract validation before Codex launch..." -ForegroundColor Cyan
    & $script:PythonExecutable $baseValidator --project-root $ProjectRoot --base-repository $BaseRoot --check
    if ($LASTEXITCODE -ne 0) {
        throw "BLOCKED_UNVERIFIED: Base project operating-contract validation failed after dependency recovery."
    }

    # The generated router names repository-root skill artifacts, not paths relative
    # to the router's own .agents/skills directory. Resolve and verify them once here.
    $projectBaseAdapter = Join-Path $ProjectRoot "skills\PROJECT_BASE_ADAPTER.json"
    $projectSkillSnapshot = Join-Path $ProjectRoot "skills\PROJECT_SKILL_SNAPSHOT.json"
    foreach ($routingInput in @($projectBaseAdapter, $projectSkillSnapshot)) {
        if (-not (Test-Path -LiteralPath $routingInput -PathType Leaf)) {
            throw "BLOCKED_UNVERIFIED: required repository-root routing input is missing: $routingInput"
        }
    }

    $projectGodot = Join-Path $ProjectRoot "project.godot"
    $projectText = Get-Content -LiteralPath $projectGodot -Raw
    foreach ($plugin in @(
        "res://addons/godot_ai/plugin.cfg",
        "res://addons/gut/plugin.cfg",
        "res://addons/hera_agent_godot/plugin.cfg"
    )) {
        if ($projectText -notmatch [regex]::Escape($plugin)) {
            throw "Required enabled plugin entry not found in project.godot: $plugin"
        }
    }

    # Godot AI exposes MCP on the local HTTP server. The editor/plugin should
    # already be running before this PowerShell entrypoint is used.
    $mcpReachable = Test-NetConnection 127.0.0.1 -Port 8000 -InformationLevel Quiet -WarningAction SilentlyContinue
    if (-not $mcpReachable) {
        throw "Godot AI MCP port 8000 is not reachable. Open OMENWARD in Godot, confirm the Godot AI dock is connected, then run this script again."
    }

    & codex login status | Out-Host
    if ($LASTEXITCODE -ne 0) {
        throw "Codex is not authenticated. Run 'codex login' first."
    }

    # Preserve a working dock-generated configuration. Only add the documented
    # streamable-HTTP fallback when the godot-ai entry does not exist at all.
    $mcpProbe = Invoke-ExpectedNativeProbe { & codex mcp get godot-ai --json }
    if ($mcpProbe -ne 0) {
        Write-Host "Codex MCP entry 'godot-ai' is missing; adding local HTTP fallback." -ForegroundColor Yellow
        & codex mcp add godot-ai --url "http://127.0.0.1:8000/mcp"
        if ($LASTEXITCODE -ne 0) {
            throw "Could not configure Codex MCP server 'godot-ai'."
        }
    }

    $issueBody = (& gh issue view $IssueNumber --repo $Repository --json body --jq .body)
    if ($LASTEXITCODE -ne 0 -or [string]::IsNullOrWhiteSpace(($issueBody -join "`n"))) {
        throw "Could not read GitHub Issue #$IssueNumber."
    }
    $issueText = $issueBody -join "`n"

    # The Issue contains an operator-facing re-entry block for starting this parent
    # executor. It is not part of the child task and must never be recursively run.
    $childIssueText = [regex]::Replace(
        $issueText,
        '(?ms)^## No-approval local execution\s.*\z',
        "## Operator-only local execution`r`n`r`nOperator-only local executor re-entry instructions omitted from child packet. The parent PowerShell executor already completed the fresh git entry gate and owns final commit/push. Do not invoke the PowerShell executor recursively."
    )
    if ($childIssueText -match [regex]::Escape("invoke_barracks_role_output_executor.ps1")) {
        throw "BLOCKED_UNVERIFIED: recursive executor instruction remained in child packet after sanitization."
    }

    $branchSha = (& git rev-parse HEAD).Trim()
    $mainSha = (& git rev-parse origin/main).Trim()
    $baseSha = (& git -C $BaseRoot rev-parse HEAD).Trim()

    # Use Codex's documented structured-output handoff so parent logic does not
    # confuse a natural-language BLOCKED result with process exit code 0.
    $resultRoot = Join-Path $env:TEMP "omenward-issue-$IssueNumber-codex"
    New-Item -ItemType Directory -Force -Path $resultRoot | Out-Null
    $resultSchemaPath = Join-Path $resultRoot "result-schema.json"
    $resultPath = Join-Path $resultRoot "result.json"
    if (Test-Path -LiteralPath $resultPath) {
        Remove-Item -LiteralPath $resultPath -Force
    }
    $resultSchema = @'
{
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "status": {"type": "string", "enum": ["READY_TO_COMMIT", "BLOCKED_UNVERIFIED"]},
    "summary": {"type": "string"},
    "blocker": {"type": "string"},
    "gut_red": {"type": "string", "enum": ["PROVEN", "NOT_RUN", "FAILED"]},
    "gut_discovered_tests": {"type": "integer", "minimum": 0},
    "godot_import": {"type": "string", "enum": ["PASS", "NOT_RUN", "FAILED"]},
    "gut_green": {"type": "string", "enum": ["PASS", "NOT_RUN", "FAILED"]},
    "headless_regressions": {"type": "string", "enum": ["PASS", "NOT_RUN", "FAILED"]},
    "fv_repeat_identity": {"type": "string", "enum": ["PASS", "NOT_RUN", "FAILED"]},
    "fv_registered_fixtures": {"type": "integer", "minimum": 0},
    "fv_runs_per_fixture": {"type": "integer", "minimum": 0},
    "hera_source_delta": {"type": "string", "enum": ["NONE", "NOT_RUN", "CHANGED"]},
    "forbidden_sidecars": {"type": "string", "enum": ["NONE", "PRESENT"]},
    "final_numeric_selection": {"type": "string", "enum": ["NONE", "PRESENT"]},
    "changed_files": {"type": "array", "items": {"type": "string"}}
  },
  "required": [
    "status", "summary", "blocker", "gut_red", "gut_discovered_tests",
    "godot_import", "gut_green", "headless_regressions", "fv_repeat_identity",
    "fv_registered_fixtures", "fv_runs_per_fixture", "hera_source_delta",
    "forbidden_sidecars", "final_numeric_selection", "changed_files"
  ]
}
'@
    Set-Content -LiteralPath $resultSchemaPath -Value $resultSchema -Encoding UTF8

    $prompt = @"
You are the local OMENWARD runtime executor operating from PowerShell/Codex with the live Godot AI MCP connection.

Execute GitHub Issue #$IssueNumber completely, using the sanitized issue body below as the authoritative child executor packet.

Fresh local facts at launch:
- repository: $Repository
- project root: $ProjectRoot
- execution branch: $ExecutionBranch
- branch HEAD: $branchSha
- origin/main: $mainSha
- Base root: $BaseRoot
- Base HEAD: $baseSha
- Base validator Python: $pythonExecutable
- Base validator Python directory granted to Codex sandbox: $pythonDirectory
- Repository-root Project Base adapter: $projectBaseAdapter
- Repository-root Project Skill snapshot: $projectSkillSnapshot
- Base project operating-contract validation: PASS in PowerShell preflight
- Godot AI MCP localhost:8000 is reachable
- Parent git entry gate: fetch/switch/pull/clean-tree/main-ancestor checks already PASS

Hard boundaries:
1. Persistent Godot/product authoring MUST go through the godot-ai MCP / HiGodot tools. Do not use shell redirection, generic text editors, apply_patch, or direct filesystem writes for scripts/, data/, scenes/, project.godot, addons/, or GDScript GUT test authoring.
2. Use shell commands only for read-only repository inspection/status, approved test execution, and evidence capture. Do not run git fetch, git switch, git pull, git commit, or git push inside child Codex. The parent PowerShell executor owns all .git mutations and final push.
3. Establish GUT RED first with >0 discovered tests and preserve the intended failing evidence before battle-runtime authoring.
4. Then perform the minimal HiGodot implementation, Godot import/parse, GUT GREEN (>0 tests), existing regressions, deterministic FV evidence, and Hera live QA with tracked-source delta NONE.
5. Hera is QA/observability only and must not persistently mutate source.
6. Never serialize BLOCKED_RUNTIME_OUTPUT as numeric zero. Do not choose a final weighted functional-value index, final parameter vector, or final product numerics.
7. Do not merge locally and do not commit or push from child Codex. When every required local evidence gate is complete, return READY_TO_COMMIT in the required structured result; the parent will independently inspect the working tree, commit, and push only the execution branch.
8. Do not discard unrelated work and do not re-add docs/analysis/barracks_simulation/*.csv.import or *.translation sidecars.
9. The Base operating-contract validator already passed in the PowerShell preflight using the exact executable shown as `Base validator Python`. The generated project workflow router still requires validation before selecting a route. If the project workflow router requires revalidation, use this exact validated Python executable and command:
   & '$pythonExecutable' '$baseValidator' --project-root '$ProjectRoot' --base-repository '$BaseRoot' --check
   The executor grants only the validated Python installation directory to the Codex sandbox via `--add-dir`; keep `workspace-write` and do not broaden to full-access. Use this exact validated Python executable. Do not invoke this executor recursively to recover validator dependencies inside Codex. The parent preflight already verified the Base-declared jsonschema requirement for this exact executable. If this exact revalidation command fails, return BLOCKED_UNVERIFIED rather than substituting another Python or changing PowerShell ExecutionPolicy.
10. After router validation, read exactly the repository-root routing inputs shown above. They are rooted at `ProjectRoot`; do not resolve them relative to .agents/skills/omenward-workflow-router and do not prepend `.agents\skills`. If either exact path cannot be read, return BLOCKED_UNVERIFIED and report that exact path.
11. Treat Issue sequence step 1 as already satisfied by the parent entry gate. Treat Issue sequence step 10 commit/push as delegated to the parent. Do not recursively execute any operator entry command. Your final answer MUST match the provided output schema. Return READY_TO_COMMIT only when GUT RED is PROVEN with >0 discovered tests, Godot import PASS, GUT GREEN PASS, existing headless regressions PASS, all 5 registered FV fixtures ran twice with identical raw outputs, Hera tracked-source delta is NONE, forbidden sidecars are NONE, final numeric selection is NONE, and the working tree contains the intended same-scope changes. Otherwise return BLOCKED_UNVERIFIED with a concrete blocker.

GitHub Issue #$IssueNumber sanitized child body follows:

$childIssueText
"@

    Write-Host "Launching Codex with Issue #$IssueNumber as the initial instruction..." -ForegroundColor Cyan
    Write-Host "PowerShell -> Base preflight -> Codex -> godot-ai MCP -> Godot Editor -> structured parent git handoff" -ForegroundColor Cyan

    if ($NonInteractive) {
        # Child authoring remains workspace-write. Git metadata stays protected; the
        # parent process performs git mutations only after a structured ready result.
        $prompt | & codex --add-dir $pythonDirectory exec -C $ProjectRoot --sandbox workspace-write -c 'approval_policy="never"' --output-schema $resultSchemaPath --output-last-message $resultPath -
    }
    else {
        # Interactive mode is for operator-guided authoring and does not auto-commit.
        & codex --add-dir $pythonDirectory -C $ProjectRoot --sandbox workspace-write --ask-for-approval on-request $prompt
    }

    $codexExit = $LASTEXITCODE
    Write-Host "Codex exited with code $codexExit" -ForegroundColor Cyan

    if (-not $NonInteractive) {
        Write-Host "Interactive mode leaves git finalization to the operator." -ForegroundColor Cyan
        & git status --short
        exit $codexExit
    }

    if ($codexExit -ne 0) {
        throw "BLOCKED_UNVERIFIED: child Codex process exited with code $codexExit"
    }
    if (-not (Test-Path -LiteralPath $resultPath -PathType Leaf)) {
        throw "BLOCKED_UNVERIFIED: child Codex did not produce the structured result file: $resultPath"
    }

    try {
        $childResult = Get-Content -LiteralPath $resultPath -Raw | ConvertFrom-Json
    }
    catch {
        throw "BLOCKED_UNVERIFIED: child Codex result was not valid JSON: $($_.Exception.Message)"
    }

    if ($childResult.status -ne "READY_TO_COMMIT") {
        throw "BLOCKED_UNVERIFIED: child result status=$($childResult.status); blocker=$($childResult.blocker)"
    }

    $readyChecks = @(
        @{ Name = "gut_red"; Actual = $childResult.gut_red; Expected = "PROVEN" },
        @{ Name = "godot_import"; Actual = $childResult.godot_import; Expected = "PASS" },
        @{ Name = "gut_green"; Actual = $childResult.gut_green; Expected = "PASS" },
        @{ Name = "headless_regressions"; Actual = $childResult.headless_regressions; Expected = "PASS" },
        @{ Name = "fv_repeat_identity"; Actual = $childResult.fv_repeat_identity; Expected = "PASS" },
        @{ Name = "hera_source_delta"; Actual = $childResult.hera_source_delta; Expected = "NONE" },
        @{ Name = "forbidden_sidecars"; Actual = $childResult.forbidden_sidecars; Expected = "NONE" },
        @{ Name = "final_numeric_selection"; Actual = $childResult.final_numeric_selection; Expected = "NONE" }
    )
    foreach ($check in $readyChecks) {
        if ($check.Actual -ne $check.Expected) {
            throw "BLOCKED_UNVERIFIED: structured ready check '$($check.Name)' expected '$($check.Expected)' but got '$($check.Actual)'"
        }
    }
    if ([int]$childResult.gut_discovered_tests -le 0) {
        throw "BLOCKED_UNVERIFIED: child reported no discovered GUT tests."
    }
    if ([int]$childResult.fv_registered_fixtures -ne 5 -or [int]$childResult.fv_runs_per_fixture -ne 2) {
        throw "BLOCKED_UNVERIFIED: registered FV evidence must be exactly 5 fixtures run twice."
    }

    $currentBranch = (& git branch --show-current).Trim()
    if ($currentBranch -ne $ExecutionBranch) {
        throw "BLOCKED_UNVERIFIED: child changed branch unexpectedly: $currentBranch"
    }

    $changedPaths = @(& git diff --name-only)
    $changedPaths += @(& git ls-files --others --exclude-standard)
    $changedPaths = @($changedPaths | Where-Object { -not [string]::IsNullOrWhiteSpace($_) } | Sort-Object -Unique)
    if ($changedPaths.Count -eq 0) {
        throw "BLOCKED_UNVERIFIED: READY_TO_COMMIT was returned but the working tree has no changes."
    }
    foreach ($path in $changedPaths) {
        $normalized = $path -replace '\\', '/'
        if ($normalized -eq ".agents/skills/omenward-workflow-router/SKILL.md") {
            throw "BLOCKED_UNVERIFIED: generated workflow router was modified by child execution."
        }
        if ($normalized -match '^docs/analysis/barracks_simulation/.*\.csv\.(import|translation)$') {
            throw "BLOCKED_UNVERIFIED: forbidden simulation CSV sidecar was created: $path"
        }
    }

    # Reconfirm the remote execution branch did not move while the child authored.
    & git fetch origin --prune
    if ($LASTEXITCODE -ne 0) {
        throw "BLOCKED_UNVERIFIED: parent git fetch failed before finalization."
    }
    $remoteExecutionSha = (& git rev-parse "origin/$ExecutionBranch").Trim()
    if ($remoteExecutionSha -ne $branchSha) {
        throw "BLOCKED_UNVERIFIED: execution branch moved remotely during child authoring: launch=$branchSha remote=$remoteExecutionSha"
    }

    & git add -A
    if ($LASTEXITCODE -ne 0) {
        throw "BLOCKED_UNVERIFIED: parent could not stage child changes."
    }
    $stagedProbe = Invoke-ExpectedNativeProbe { & git diff --cached --quiet }
    if ($stagedProbe -eq 0) {
        throw "BLOCKED_UNVERIFIED: parent found no staged changes after READY_TO_COMMIT."
    }

    & git commit -m "fix: close Issue #$IssueNumber barracks runtime gaps"
    if ($LASTEXITCODE -ne 0) {
        throw "BLOCKED_UNVERIFIED: parent git commit failed."
    }
    $committedSha = (& git rev-parse HEAD).Trim()

    & git push origin $ExecutionBranch
    if ($LASTEXITCODE -ne 0) {
        throw "BLOCKED_UNVERIFIED: parent git push failed for $ExecutionBranch."
    }

    Write-Host "Parent commit/push completed: $committedSha" -ForegroundColor Green
    Write-Host "Child summary: $($childResult.summary)" -ForegroundColor Green
    Write-Host "Current branch/status:" -ForegroundColor Cyan
    & git branch --show-current
    & git status --short
    exit 0
}
finally {
    Pop-Location
}
