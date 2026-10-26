param(
    [Parameter(Mandatory = $true)][string] $SourceRepository,
    [Parameter(Mandatory = $true)][string] $DestinationRepository,
    [string] $CommitMessage = 'Update music composition knowledge',
    [string] $ProxyUrl = 'http://127.0.0.1:7890',
    [string] $ReportPath,
    [switch] $PrepareOnly
)
$ErrorActionPreference = 'Stop'
$sourceRoot = [IO.Path]::GetFullPath($SourceRepository).TrimEnd('\', '/')
$destinationRoot = [IO.Path]::GetFullPath($DestinationRepository).TrimEnd('\', '/')
$contentRoot = Join-Path $destinationRoot 'content'
$manifestPath = Join-Path $destinationRoot '.publication.json'
$expectedRemote = 'https://github.com/OpenCadenza/music-wiki.git'
$validatorName = 'validate_lilypond_versions.py'
$validatorSourcePath = Join-Path $PSScriptRoot $validatorName
$validatorHelperPath = Join-Path $destinationRoot ('scripts/' + $validatorName)

function Invoke-Git([string] $repository, [string[]] $gitArguments) {
    $result = & git -C $repository @gitArguments
    if ($LASTEXITCODE -ne 0) { throw "git failed in $repository (exit $LASTEXITCODE): $($gitArguments[0])" }
    return $result
}
function Resolve-ContainedPath([string] $rootPath, [string] $relativePath) {
    $absolutePath = [IO.Path]::GetFullPath((Join-Path $rootPath $relativePath))
    if (-not $absolutePath.StartsWith($rootPath + [IO.Path]::DirectorySeparatorChar, [StringComparison]::OrdinalIgnoreCase)) { throw "Path escapes declared root: $relativePath" }
    return $absolutePath
}
function Write-Bytes([string] $path, [byte[]] $bytes) {
    New-Item -ItemType Directory -Path ([IO.Path]::GetDirectoryName($path)) -Force | Out-Null
    Set-Content -LiteralPath $path -Value $bytes -AsByteStream -Force
}
function Assert-NoReparsePath([string] $path) {
    $probe = $path
    while ($probe) {
        if (Test-Path -LiteralPath $probe) {
            if ((Get-Item -LiteralPath $probe -Force).Attributes -band [IO.FileAttributes]::ReparsePoint) { throw "Refusing linked/reparse path: $probe" }
        }
        $parent = [IO.Path]::GetDirectoryName($probe)
        if ($parent -eq $probe) { break }
        $probe = $parent
    }
}
function Assert-LilyPondVersions([string] $rootPath) {
    if (-not (Test-Path -LiteralPath $validatorSourcePath -PathType Leaf)) {
        throw "LilyPond version validator is missing: $validatorSourcePath"
    }
    $python = Get-Command python -ErrorAction Stop
    & $python.Source $validatorSourcePath --root $rootPath
    if ($LASTEXITCODE -ne 0) {
        throw 'LilyPond version policy failed; refusing to commit or publish'
    }
}

if ($sourceRoot -eq $destinationRoot -or $sourceRoot.StartsWith($destinationRoot + '\', [StringComparison]::OrdinalIgnoreCase) -or $destinationRoot.StartsWith($sourceRoot + '\', [StringComparison]::OrdinalIgnoreCase)) { throw 'Source and destination must be separate repositories' }
foreach ($repository in @($sourceRoot, $destinationRoot)) {
    Assert-NoReparsePath $repository
    $actualRoot = Invoke-Git $repository @('rev-parse', '--show-toplevel')
    if ([IO.Path]::GetFullPath($actualRoot).TrimEnd('\', '/') -ne $repository) { throw "Not an exact repository root: $repository" }
}
if ((Invoke-Git $destinationRoot @('branch', '--show-current')) -ne 'main') { throw 'Publish destination must be on main' }
$originUrl = Invoke-Git $destinationRoot @('remote', 'get-url', 'origin')
if ($originUrl -notin @($expectedRemote, ($expectedRemote -replace '\.git$', ''), 'git@github.com:OpenCadenza/music-wiki.git')) { throw 'Destination origin differs from OpenCadenza/music-wiki' }
if (Invoke-Git $destinationRoot @('status', '--porcelain')) { throw 'Destination has uncommitted work; preserve it and resolve before publishing' }
Assert-NoReparsePath $contentRoot
$previousFiles = @{}
if (Test-Path -LiteralPath $manifestPath) {
    $previous = Get-Content -LiteralPath $manifestPath -Raw | ConvertFrom-Json
    foreach ($record in $previous.files) { $previousFiles[$record.path] = $record.sha256 }
}
if ((Test-Path -LiteralPath $contentRoot) -and $previousFiles.Count -eq 0 -and (Get-ChildItem -LiteralPath $contentRoot -Recurse -File -Force | Select-Object -First 1)) { throw 'Existing content is unmanaged; do not overwrite it on the first publication' }

# The source repository is authoritative. Commit it before copying any content.
Assert-LilyPondVersions $sourceRoot
Invoke-Git $sourceRoot @('add', '--all') | Out-Null
& git -C $sourceRoot diff --cached --quiet
$stagedExit = $LASTEXITCODE
if ($stagedExit -eq 1) { Invoke-Git $sourceRoot @('commit', '-m', $CommitMessage) | Out-Host }
elseif ($stagedExit -ne 0) { throw 'Unable to inspect staged source changes' }
$sourceCommit = Invoke-Git $sourceRoot @('rev-parse', 'HEAD')
$sourceBranch = Invoke-Git $sourceRoot @('branch', '--show-current')
$filePaths = @(Invoke-Git $sourceRoot @('-c', 'core.quotepath=false', 'ls-files'))
$excluded = @($filePaths | Where-Object { $_ -match '^(_maintenance/|\.github/|\.gitignore$|\.gitattributes$)' })
$publishedPaths = @($filePaths | Where-Object { $_ -notin $excluded } | Sort-Object)
$records = @()
foreach ($relativePath in $publishedPaths) {
    $sourcePath = Resolve-ContainedPath $sourceRoot $relativePath
    $targetPath = Resolve-ContainedPath $contentRoot $relativePath
    Assert-NoReparsePath $sourcePath
    Assert-NoReparsePath $targetPath
    Write-Bytes $targetPath ([IO.File]::ReadAllBytes($sourcePath))
    $sourceHash = (Get-FileHash -LiteralPath $sourcePath -Algorithm SHA256).Hash.ToLowerInvariant()
    if ((Get-FileHash -LiteralPath $targetPath -Algorithm SHA256).Hash.ToLowerInvariant() -ne $sourceHash) { throw "Copy mismatch: $relativePath" }
    $records += [ordered]@{ path = $relativePath; sha256 = $sourceHash }
}
$removed = @()
foreach ($relativePath in $previousFiles.Keys) {
    if ($relativePath -notin $publishedPaths) {
        $targetPath = Resolve-ContainedPath $contentRoot $relativePath
        Assert-NoReparsePath $targetPath
        if (Test-Path -LiteralPath $targetPath -PathType Leaf) {
            # Delete only previously managed files at a verified exact target.
            Remove-Item -LiteralPath $targetPath -Force
            $removed += $relativePath
        }
    }
}
$manifest = [ordered]@{ schema_version = 1; source_commit = $sourceCommit; source_branch = $sourceBranch; content_root = 'content'; excluded_paths = $excluded; files = $records }
Write-Bytes $manifestPath ([Text.UTF8Encoding]::new($false).GetBytes(($manifest | ConvertTo-Json -Depth 6) + "`n"))
$helperPath = Join-Path $destinationRoot 'scripts/publish-content.ps1'
if ([IO.Path]::GetFullPath($PSCommandPath) -ne [IO.Path]::GetFullPath($helperPath)) { Write-Bytes $helperPath ([IO.File]::ReadAllBytes($PSCommandPath)) }
Write-Bytes $validatorHelperPath ([IO.File]::ReadAllBytes($validatorSourcePath))
$readmePath = Join-Path $destinationRoot 'README.md'
if (-not (Test-Path -LiteralPath $readmePath -PathType Leaf)) {
    $readme = @'
# 音乐知识库

`content/` 是从 `references-origin/` 生成的发布快照。

完整的内容编辑规则、谱例元数据、构建命令和发布流程见仓库根目录
`README.md`。提交前运行 `pnpm validate` 与 `pnpm build`。
'@
    Write-Bytes $readmePath ([Text.UTF8Encoding]::new($false).GetBytes($readme + "`n"))
}
if ($PrepareOnly) {
    [ordered]@{ source_commit = $sourceCommit; published_files = $records.Count; removed_paths = $removed; excluded_paths = $excluded; prepared_only = $true } | ConvertTo-Json -Depth 5
    return
}
Invoke-Git $destinationRoot @('add', '--all') | Out-Null
& git -C $destinationRoot diff --cached --quiet
$publicationExit = $LASTEXITCODE
if ($publicationExit -eq 1) {
    Invoke-Git $destinationRoot @('commit', '-m', ('Publish music knowledge from ' + $sourceCommit.Substring(0, 12)), '-m', ('Source-Commit: ' + $sourceCommit)) | Out-Host
} elseif ($publicationExit -ne 0) { throw 'Unable to inspect staged publication changes' }
$publicationCommit = Invoke-Git $destinationRoot @('rev-parse', 'HEAD')
$networkArguments = @()
if ($ProxyUrl) { $networkArguments += @('-c', ('http.proxy=' + $ProxyUrl)) }
Invoke-Git $destinationRoot ($networkArguments + @('push', '--set-upstream', 'origin', 'HEAD:main')) | Out-Host
$remoteLine = Invoke-Git $destinationRoot ($networkArguments + @('ls-remote', 'origin', 'refs/heads/main'))
$remoteCommit = ($remoteLine -split '\s+')[0]
if ($remoteCommit -ne $publicationCommit) { throw 'Remote main does not match the local publication commit' }
$report = [ordered]@{ source_commit = $sourceCommit; publication_commit = $publicationCommit; remote_commit = $remoteCommit; published_files = $records.Count; removed_paths = $removed; excluded_paths = $excluded; pushed = $true; repository = 'https://github.com/OpenCadenza/music-wiki' }
if ($ReportPath) { Write-Bytes ([IO.Path]::GetFullPath($ReportPath)) ([Text.UTF8Encoding]::new($false).GetBytes(($report | ConvertTo-Json -Depth 5) + "`n")) }
$report | ConvertTo-Json -Depth 5
