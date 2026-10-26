#!/usr/bin/env bash
set -euo pipefail

root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
tools="$root/.tools"
mkdir -p "$tools" "$tools/soundfonts"

lily_archive="$tools/lilypond-2.26.0-linux-x86_64.tar.gz"
lily_root="$tools/lilypond-2.26.0"
lily_hash="cd8a097a9f52cb2b9f4e7914774786f203f4fc61fcd299afcbb63c23fa5c6b24"

if [[ ! -x "$lily_root/bin/lilypond" ]]; then
  if [[ ! -f "$lily_archive" ]]; then
    curl -fL --retry 3 \
      "https://gitlab.com/lilypond/lilypond/-/releases/v2.26.0/downloads/lilypond-2.26.0-linux-x86_64.tar.gz" \
      -o "$lily_archive"
  fi
  actual="$(sha256sum "$lily_archive" | awk '{print $1}')"
  [[ "$actual" == "$lily_hash" ]] || {
    echo "LilyPond archive hash mismatch: $actual" >&2
    exit 1
  }
  tar -xzf "$lily_archive" -C "$tools"
fi

soundfont="$tools/soundfonts/FluidR3_GM.sf2"
soundfont_hash="74594e8f4250680adf590507a306655a299935343583256f3b722c48a1bc1cb0"
if [[ ! -f "$soundfont" ]]; then
  curl -fL --retry 3 \
    "https://github.com/pianobooster/fluid-soundfont/releases/download/v3.1/FluidR3_GM.sf2" \
    -o "$soundfont"
fi
actual="$(sha256sum "$soundfont" | awk '{print $1}')"
[[ "$actual" == "$soundfont_hash" ]] || {
  echo "Soundfont hash mismatch: $actual" >&2
  exit 1
}

"$lily_root/bin/lilypond" --version | head -n 1
"$lily_root/bin/convert-ly" --version | head -n 1
abc2midi -ver | head -n 1
fluid_version="$(fluidsynth --version 2>&1)"
echo "$fluid_version" | head -n 1
[[ "$fluid_version" == *"2.6.1"* ]] || {
  echo "FluidSynth 2.6.1 is required" >&2
  exit 1
}
ffmpeg -version | head -n 1
ffprobe -version | head -n 1

if [[ -n "${GITHUB_PATH:-}" ]]; then
  echo "$lily_root/bin" >>"$GITHUB_PATH"
fi
cat <<EOF
LilyPond: $lily_root/bin
Soundfont: $soundfont
For a local shell:
  export LILYPOND_PATH="$lily_root/bin/lilypond"
  export SOUNDFONT_PATH="$soundfont"
EOF
