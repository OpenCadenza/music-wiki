#!/usr/bin/env bash
set -euo pipefail

root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
tools="$root/.tools"
prefix="$tools/ffmpeg-8.1.3-source"
archive="$tools/ffmpeg-8.1.3.tar.xz"
url="https://ffmpeg.org/releases/ffmpeg-8.1.3.tar.xz"
expected_hash="7138d28c96d9d3e3af4ee3d8cad72741f8ffb40da90c1112235dea3ecd3178a3"

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
  source_dir="$(mktemp -d)"
  trap 'rm -rf "$source_dir"' EXIT
  tar -xJf "$archive" --strip-components=1 -C "$source_dir"
  (cd "$source_dir" && ./configure --prefix="$prefix" --enable-libmp3lame --disable-doc --disable-debug && make -j"$(nproc)" && make install)
  rm -f "$archive"
fi

ffmpeg_version="$("$prefix/bin/ffmpeg" -version | sed -n '1p')"
ffprobe_version="$("$prefix/bin/ffprobe" -version | sed -n '1p')"
[[ "$ffmpeg_version" == *"8.1.3"* ]] || {
  echo "FFmpeg 8.1.3 is required: $ffmpeg_version" >&2
  exit 1
}
[[ "$ffprobe_version" == *"8.1.3"* ]] || {
  echo "FFprobe 8.1.3 is required: $ffprobe_version" >&2
  exit 1
}

if [[ -n "${GITHUB_PATH:-}" ]]; then
  echo "$prefix/bin" >>"$GITHUB_PATH"
fi

echo "$ffmpeg_version"
echo "$ffprobe_version"
