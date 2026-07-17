$ErrorActionPreference = "Stop"

$repoRoot = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
$requiredBooks = @(
    "docs/planning/01_GAME_DESIGN.md",
    "docs/planning/02_PROGRAMMING_MVP_ROADMAP.md",
    "docs/planning/03_ART_DIRECTION.md",
    "docs/planning/04_SOUND_DIRECTION.md",
    "docs/planning/05_QA_PM_PLAN.md"
)
$requiredImages = @(
    "docs/images/current/battlefield-ingame-reference.png",
    "docs/images/current/roulette-bellu-ui-reference.png",
    "docs/images/current/bellu-character-reference.png"
)
$errors = [System.Collections.Generic.List[string]]::new()

foreach ($relativePath in $requiredBooks) {
    $absolutePath = Join-Path $repoRoot $relativePath
    if (-not (Test-Path -LiteralPath $absolutePath -PathType Leaf)) {
        $errors.Add("Missing planning book: $relativePath")
        continue
    }

    $content = Get-Content -LiteralPath $absolutePath -Raw -Encoding UTF8
    $metadataLines = [regex]::Matches($content, '(?m)^- [^:\r\n]+: .+$')
    if ($metadataLines.Count -lt 3) {
        $errors.Add("Expected at least three metadata fields in $relativePath")
    }
    if ($content -notmatch '\d{4}-\d{2}-\d{2}') {
        $errors.Add("Missing updated date in $relativePath")
    }
}

foreach ($relativePath in $requiredImages) {
    if (-not (Test-Path -LiteralPath (Join-Path $repoRoot $relativePath) -PathType Leaf)) {
        $errors.Add("Missing current image: $relativePath")
    }
}

$visualIndexPath = Join-Path $repoRoot "docs/images/VISUAL_REFERENCE_INDEX.md"
$visualIndex = Get-Content -LiteralPath $visualIndexPath -Raw -Encoding UTF8
foreach ($relativePath in $requiredImages) {
    $indexPath = $relativePath.Replace("docs/images/", "")
    if (-not $visualIndex.Contains($indexPath)) {
        $errors.Add("Visual index does not reference: $indexPath")
    }
}

$documentationMapPath = Join-Path $repoRoot "docs/DOCUMENTATION_MAP.md"
$documentationMap = Get-Content -LiteralPath $documentationMapPath -Raw -Encoding UTF8
$classificationMatch = [regex]::Match($documentationMap, '(?s)## 5\..*?## 6\.')
if (-not $classificationMatch.Success) {
    $errors.Add("Missing approved-document classification section in docs/DOCUMENTATION_MAP.md")
} else {
    $supersededApproved = @(
        "APPROVED_ART_DIRECTION_AND_PRODUCTION_GUIDE_V1.md",
        "APPROVED_UI_ART_AUDIO_POC_BIBLE_V1.md"
    )
    $approvedFiles = Get-ChildItem -LiteralPath (Join-Path $repoRoot "docs/design") -File -Filter "APPROVED_*.md" |
        Where-Object { $supersededApproved -notcontains $_.Name }
    foreach ($approvedFile in $approvedFiles) {
        $count = [regex]::Matches($classificationMatch.Value, [regex]::Escape($approvedFile.Name)).Count
        if ($count -ne 1) {
            $errors.Add("Approved document must have exactly one primary classification: $($approvedFile.Name) (found $count)")
        }
    }
}

$markdownFiles = Get-ChildItem -LiteralPath (Join-Path $repoRoot "docs") -Recurse -File -Filter "*.md" |
    Where-Object {
        $_.FullName -notmatch "[\\/]docs[\\/]issues[\\/]" -and
        $_.FullName -notmatch "[\\/]docs[\\/]archive[\\/]"
    }

$linkPattern = [regex]'\[[^\]]*\]\((?<target>[^)]+)\)'
foreach ($file in $markdownFiles) {
    $content = Get-Content -LiteralPath $file.FullName -Raw -Encoding UTF8
    foreach ($match in $linkPattern.Matches($content)) {
        $target = $match.Groups["target"].Value.Trim().Trim('<', '>')
        if ($target -match '^(https?://|mailto:|#)') { continue }
        $pathOnly = ($target -split '#', 2)[0]
        if ([string]::IsNullOrWhiteSpace($pathOnly)) { continue }
        $decodedPath = [Uri]::UnescapeDataString($pathOnly)
        $resolved = [System.IO.Path]::GetFullPath((Join-Path $file.DirectoryName $decodedPath))
        if (-not (Test-Path -LiteralPath $resolved)) {
            $relativeFile = $file.FullName.Substring($repoRoot.Length + 1)
            $errors.Add("Broken relative link in ${relativeFile}: $target")
        }
    }
}

$activeFiles = @(
    "AGENTS.md",
    "README.md",
    "docs/DOCUMENTATION_MAP.md",
    "docs/HANDOFF_CONTEXT.md",
    "docs/ACTIVE_CONTEXT.md"
) + $requiredBooks
$legacyActiveReferences = @(
    "docs/OMENWARD_GAME_DESIGN.md",
    "docs/OMENWARD_ROADMAP.md",
    "docs/design/APPROVED_ART_DIRECTION_AND_PRODUCTION_GUIDE_V1.md",
    "docs/design/APPROVED_UI_ART_AUDIO_POC_BIBLE_V1.md"
)
foreach ($relativePath in $activeFiles) {
    $content = Get-Content -LiteralPath (Join-Path $repoRoot $relativePath) -Raw -Encoding UTF8
    foreach ($legacyPath in $legacyActiveReferences) {
        if ($content.Contains($legacyPath)) {
            $errors.Add("Active document references superseded path in ${relativePath}: $legacyPath")
        }
    }
}

if ($errors.Count -gt 0) {
    $errors | ForEach-Object { Write-Error $_ }
    exit 1
}

Write-Host "Documentation validation passed: 5 books, metadata, current images, and relative links."
