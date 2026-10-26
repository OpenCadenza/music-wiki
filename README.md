# Music Wiki

Composition knowledge with embedded ABC and LilyPond examples. The public site is deployed to:

- Site: <https://opencadenza.github.io/music-wiki/>
- Repository: <https://github.com/OpenCadenza/music-wiki>

`content/` is the published knowledge snapshot. Its maintained source is the separate
`references-origin` Git repository. Edit the source, then publish; do not maintain a
second independent copy in `content/`.

## LilyPond 2.26.0

Every fenced `lilypond` or `ly` block must declare exactly `\version "2.26.0"`.
`source_version` remains historical provenance and may name an older encoding; the
executable code and `target_version` must use 2.26.0.

## Build

Install Node 24 and pnpm 12.3.4, then run:

```bash
pnpm install --frozen-lockfile
pnpm build
```

The full build checks all content, compiles all 66 notation blocks into SVG and MIDI,
renders MP3 previews with FluidR3 GM, validates the artifact manifest, builds
VitePress, and smoke-tests the generated site.

Linux/WSL prerequisites:

```bash
sudo apt install abcmidi ffmpeg fluidsynth
bash scripts/install-toolchain.sh
```

Windows:

```powershell
./scripts/install-toolchain.ps1
```

Set the printed `LILYPOND_PATH`, `ABC2MIDI_PATH`, `FLUIDSYNTH_PATH`, and
`SOUNDFONT_PATH` values in the shell before `pnpm notation`. Generated files live in
`public/notation/` and `.notation-work/`, which are ignored by Git.

## Publish

The source repository is committed first, then copied into `content/` and published:

```powershell
./scripts/publish-content.ps1 `
  -SourceRepository E:/programfiles/MusicKnowledgeBase/references-origin `
  -DestinationRepository E:/Github/music-wiki
```

The publication script validates LilyPond versions, records the source commit in
`.publication.json`, verifies copied files with SHA-256, commits the site, pushes
`main`, and verifies the remote commit. A push to `main` triggers
`.github/workflows/deploy.yml`, which builds the notation and deploys `dist/` through
GitHub Pages.

OpenViking syncs the GitHub `content/` subtree to
`viking://resources/music-wiki/`; that synchronization is managed outside this
repository.

Source licenses and permissions are documented in `content/LICENSE.md` and
`content/knowledge/sources.json`. Individual score examples retain their source,
rights, and verification metadata.
