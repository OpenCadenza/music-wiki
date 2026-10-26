# Music Wiki

Music theory and composition knowledge with embedded ABC and LilyPond examples.

`content/` is the published knowledge snapshot. Its maintained source is the separate `references-origin` Git repository. Edit the source, then publish; do not maintain a second independent copy in `content/`.

Run the repeatable publication from PowerShell 7:

```powershell
./scripts/publish-content.ps1 -SourceRepository E:/programfiles/MusicKnowledgeBase/references-origin -DestinationRepository E:/github/music-wiki
```

The script commits source changes, copies tracked knowledge files, verifies SHA-256, records the source commit in `.publication.json`, commits the publication and pushes `main`. Git metadata and `_maintenance/` stay outside the knowledge snapshot. Only stale files recorded in the previous publication manifest are removed. A repeated publication with unchanged input creates no new commit.

OpenViking is responsible for syncing this repository's `content/` subtree to `viking://resources/music-wiki/`. No additional Git synchronization service is included here.

VitePress configuration, GitHub Actions compilation of ABC/LilyPond into SVG and playable audio, and Pages deployment are planned separately. This initial publication does not implement them. Source Markdown and score code remain authoritative; rendered artifacts will be build outputs.

Source licenses and permissions are documented in `content/LICENSE.md` and `content/knowledge/sources.json`. Individual score examples retain their source, rights and verification metadata.
