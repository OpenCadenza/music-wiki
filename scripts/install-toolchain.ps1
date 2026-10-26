param(
    [switch] $SkipDownload
)

$ErrorActionPreference = 'Stop'
$root = Split-Path -Parent $PSScriptRoot
$tools = Join-Path $root '.tools'
$archive = Join-Path $tools 'lilypond-2.26.0-mingw-x86_64.zip'
$lilyRoot = Join-Path $tools 'lilypond-2.26.0'
$soundfontDirectory = Join-Path $tools 'soundfonts'
$soundfont = Join-Path $soundfontDirectory 'FluidR3_GM.sf2'
$lilyHash = '14ddddc233b469ef60d4ffc1c7f35520f15ac6b58e38cab458c60bdcc3af650c'
$soundfontHash = '74594e8f4250680adf590507a306655a299935343583256f3b722c48a1bc1cb0'
$localSoundfont = 'E:\programfiles\i-score\data\soundfonts\fluidr3-gm\FluidR3_GM.sf2'

New-Item -ItemType Directory -Force -Path $tools, $soundfontDirectory | Out-Null
if (-not (Test-Path -LiteralPath (Join-Path $lilyRoot 'bin\lilypond.exe'))) {
    if ($SkipDownload) { throw 'LilyPond 2.26.0 is not installed' }
    if (-not (Test-Path -LiteralPath $archive)) {
        Invoke-WebRequest -Uri 'https://gitlab.com/lilypond/lilypond/-/releases/v2.26.0/downloads/lilypond-2.26.0-mingw-x86_64.zip' -OutFile $archive
    }
    $actual = (Get-FileHash -LiteralPath $archive -Algorithm SHA256).Hash.ToLowerInvariant()
    if ($actual -ne $lilyHash) { throw "LilyPond archive hash mismatch: $actual" }
    Expand-Archive -LiteralPath $archive -DestinationPath $tools -Force
}

if (-not (Test-Path -LiteralPath $soundfont)) {
    if (Test-Path -LiteralPath $localSoundfont) {
        Copy-Item -LiteralPath $localSoundfont -Destination $soundfont
    } elseif ($SkipDownload) {
        throw 'FluidR3 GM is not installed'
    } else {
        Invoke-WebRequest -Uri 'https://github.com/pianobooster/fluid-soundfont/releases/download/v3.1/FluidR3_GM.sf2' -OutFile $soundfont
    }
}
$actual = (Get-FileHash -LiteralPath $soundfont -Algorithm SHA256).Hash.ToLowerInvariant()
if ($actual -ne $soundfontHash) { throw "Soundfont hash mismatch: $actual" }

$env:LILYPOND_PATH = Join-Path $lilyRoot 'bin\lilypond.exe'
$env:SOUNDFONT_PATH = $soundfont
$abcCandidate = Join-Path $tools 'abcmidi-20261016\abc2midi.exe'
if (-not (Test-Path -LiteralPath $abcCandidate)) {
    $abcCandidate = (Get-Command abc2midi -ErrorAction SilentlyContinue).Source
}
$fluidCandidate = Join-Path $tools 'fluidsynth-v2.6.1-win10-x64-cpp11\bin\fluidsynth.exe'
if (-not (Test-Path -LiteralPath $fluidCandidate)) {
    $fluidCandidate = (Get-Command fluidsynth -ErrorAction SilentlyContinue).Source
}
if (-not $abcCandidate -or -not (Test-Path -LiteralPath $abcCandidate)) { throw 'abc2midi is unavailable. Install a Windows-compatible abcMIDI build or use WSL/Linux.' }
if (-not $fluidCandidate -or -not (Test-Path -LiteralPath $fluidCandidate)) { throw 'FluidSynth 2.6.1 is unavailable.' }
$convertLy = Get-ChildItem -LiteralPath (Join-Path $lilyRoot 'bin') -Filter 'convert-ly*' |
    Select-Object -First 1
& $env:LILYPOND_PATH --version | Select-Object -First 1
if (-not $convertLy) { throw 'convert-ly is missing from the LilyPond package' }
$abcOutput = & $abcCandidate -ver 2>&1
$fluidOutput = & $fluidCandidate --version 2>&1
$abcOutput | Select-Object -First 1
$fluidOutput | Select-Object -First 1
Get-Command ffmpeg, ffprobe -ErrorAction Stop | Select-Object Name, Source
$env:ABC2MIDI_PATH = $abcCandidate
$env:FLUIDSYNTH_PATH = $fluidCandidate

[pscustomobject]@{
    lilypond = $env:LILYPOND_PATH
    soundfont = $env:SOUNDFONT_PATH
    abc2midi = $env:ABC2MIDI_PATH
    fluidsynth = $env:FLUIDSYNTH_PATH
    next = 'Set these four variables in the shell before running pnpm notation.'
} | Format-List
