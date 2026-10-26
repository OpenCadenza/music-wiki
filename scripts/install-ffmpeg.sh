#!/usr/bin/env bash
set -euo pipefail

root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
tools="$root/.tools"
prefix="$tools/ffmpeg-8.1.3"
archive="$tools/ffmpeg-8.1.3-linux64-gpl.tar.xz"
url="https://github.com/BtbN/FFmpeg-Builds/releases/download/autobuild-2026-10-26-14-25/ffmpeg-n8.1.3-24-g92611900bb-linux64-gpl-8.1.tar.xz"
expected_hash="d113aa5b57ab0dcfee171d835240ce3ea5db826a0ee80ed7528c8d26a61e87a4"

if [[ ! -x "$prefix/bin/ffmpeg" || ! -x "$prefix/bin/ffprobe" ]]; then
  mkdir -p "$tools"
  rm -rf "$prefix"
  rm -f "$archive"
  curl -fL --retry 3 --retry-all-errors "$url" -o "$archive"
  actual_hash="$(sha256sum "$archive" | awk '{print $1}')"
  [[ "$actual_hash" == "$expected_hash" ]] || {
    echo "FFmpeg archive hash mismatch: $actual_hash" >&2
    exit 1
  }
  mkdir -p "$prefix"
  tar -xJf "$archive" --strip-components=1 -C "$prefix"
  rm -f "$archive"
fi

ffmpeg_version="$("$prefix/bin/ffmpeg" -version | sed -n '1p')"
ffprobe_version="$("$prefix/bin/ffprobe" -version | sed -n '1p')"
[[ "$ffmpeg_version" == *"n8.1.3"* ]] || {
  echo "FFmpeg 8.1.3 is required: $ffmpeg_version" >&2
  exit 1
}
[[ "$ffprobe_version" == *"n8.1.3"* ]] || {
  echo "FFprobe 8.1.3 is required: $ffprobe_version" >&2
  exit 1
}

if [[ -n "${GITHUB_PATH:-}" ]]; then
  echo "$prefix/bin" >>"$GITHUB_PATH"
fi

echo "$ffmpeg_version"
echo "$ffprobe_version"
