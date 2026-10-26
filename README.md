# Music Wiki

Music theory and composition knowledge with embedded ABC and LilyPond examples.

`content/` is the published knowledge snapshot. Its maintained source is the separate `references-origin` Git repository. Edit the source, then publish; do not maintain a second independent copy in `content/`.

## LilyPond 2.26.0 requirement

Every fenced `lilypond` or `ly` code block in this repository MUST declare `\version "2.26.0"`. Every LilyPond `opusloom:example` MUST set `target_version` to `2.26.0`. Publication is refused when any executable LilyPond block declares another version, omits the declaration, or targets another version.

`source_version` records the version of a historical source encoding and may remain older for provenance. It does not relax the executable-code rule: convert or retype the example for 2.26.0 and compile the converted code before publishing. Do not merely replace the version string when syntax changes are required.

Run the repeatable publication from PowerShell 7:

```powershell
./scripts/publish-content.ps1 -SourceRepository E:/programfiles/MusicKnowledgeBase/references-origin -DestinationRepository E:/github/music-wiki
```

The script validates the LilyPond version policy, commits source changes, copies tracked knowledge files, verifies SHA-256, records the source commit in `.publication.json`, commits the publication and pushes `main`. Git metadata and `_maintenance/` stay outside the knowledge snapshot. Only stale files recorded in the previous publication manifest are removed. A repeated publication with unchanged input creates no new commit.

OpenViking is responsible for syncing this repository's `content/` subtree to `viking://resources/music-wiki/`. No additional Git synchronization service is included here.

VitePress, the score player, the ABC/LilyPond build pipeline and GitHub Pages deployment are included. Generated SVG/MIDI/MP3 files stay in ignored build directories. Source Markdown and score code remain authoritative.

Local site build on Linux/WSL:

```bash
sudo apt install abcmidi ffmpeg fluidsynth
pnpm install --frozen-lockfile
pnpm build
```

On Windows, run `scripts/install-toolchain.ps1` and expose the printed tool paths before `pnpm build`. The deployed site uses the pinned toolchain in `.github/workflows/deploy.yml`.

Source licenses and permissions are documented in `content/LICENSE.md` and `content/knowledge/sources.json`. Individual score examples retain their source, rights and verification metadata.
