#!/usr/bin/env bash
set -euo pipefail

root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
tools="$root/.tools"
read -r version url expected_hash < <(node -e '
  const { ffmpeg } = require(process.argv[1]);
  console.log(ffmpeg.version, ffmpeg.linux.url, ffmpeg.linux.sha256);
' "$root/toolchains.json")
prefix="$tools/ffmpeg-${version}-${expected_hash}"

if [[ ! -x "$prefix/bin/ffmpeg" || ! -x "$prefix/bin/ffprobe" ]]; then
  mkdir -p "$tools"
  staging="$(mktemp -d "$tools/ffmpeg-install.XXXXXX")"
  trap 'rm -rf "$staging"' EXIT
  archive="$staging/ffmpeg.tar.xz"
  curl -fL --retry 3 --retry-all-errors "$url" -o "$archive"
  actual_hash="$(sha256sum "$archive" | awk '{print $1}')"
  [[ "$actual_hash" == "$expected_hash" ]] || {
    echo "FFmpeg archive hash mismatch: $actual_hash" >&2
    exit 1
  }
  mkdir "$staging/package"
  tar -xJf "$archive" -C "$staging/package"
  test -x "$staging/package/bin/ffmpeg"
  test -x "$staging/package/bin/ffprobe"
  rm -rf "$prefix"
  mv "$staging/package" "$prefix"
fi

ffmpeg_version="$("$prefix/bin/ffmpeg" -version | sed -n '1p')"
ffprobe_version="$("$prefix/bin/ffprobe" -version | sed -n '1p')"
[[ "$ffmpeg_version" == "ffmpeg version $version "* ]] || {
  echo "FFmpeg $version is required: $ffmpeg_version" >&2
  exit 1
}
[[ "$ffprobe_version" == "ffprobe version $version "* ]] || {
  echo "FFprobe $version is required: $ffprobe_version" >&2
  exit 1
}

if [[ -n "${GITHUB_PATH:-}" ]]; then
  echo "$prefix/bin" >>"$GITHUB_PATH"
fi

echo "$ffmpeg_version"
echo "$ffprobe_version"
