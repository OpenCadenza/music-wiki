<!-- music-kb:page {"id": "page.1aea231ada704eb2a4f313c65bf408cb"} -->
# Format and compiler cards

## id: `format.abc.version-and-header`

- type: fact
- facets: format, ABC, parser, strict, header
- sources: abc-2-1
- confidence: established
- scope: ABC 2.1 documents and compatible host tools
- signals: The source declares the intended dialect and gives each tune the
  fields needed to interpret pitch and duration. Every required header appears
  before musical content.
- counterexample: A parser accepting a line does not prove that another host
  interprets it under the same dialect.
- limits: Host extensions and older ABC variants can differ. Check the actual
  compiler report.

Write one unambiguous tune or movement per expected `X:` record. Check that
the host sees the version, mode, and requested output path.

## id: `format.abc.pitch-and-accidental`

- type: fact
- facets: format, ABC, pitch, octave, accidental, key
- sources: abc-2-1
- confidence: established
- scope: Standard ABC octave and accidental syntax
- signals: Letter case, commas, apostrophes, key mode, and explicit accidentals
  are all accounted for when converting notation to sounding pitch.
- counterexample: Lowercase `c` and uppercase `C` are not the same octave.
- limits: Parser diagnostics and imported source conventions can diverge. Use
  parsed pitch evidence when available.

Record the accidental and resulting sounding pitch for disputed notes. Do not
infer absolute pitch from a letter alone.

## id: `format.abc.duration-and-pickup`

- type: fact
- facets: format, ABC, duration, meter, pickup, anacrusis
- sources: abc-2-1
- confidence: established
- scope: ABC duration multipliers and bar accounting
- signals: Each event expands using the active unit-note length. The opening
  and closing measure total matches the meter or an explicit pickup convention.
- counterexample: Equal note counts do not imply equal durations.
- limits: Invalid measure totals can compile in some toolchains.

Sum durations by voice and measure. State how an anacrusis is completed at the
end; do not silently discard beats.

## id: `format.abc.voices`

- type: procedure
- facets: format, ABC, voices, polyphony, playback
- sources: abc-2-1
- confidence: established
- scope: Explicit multi-voice ABC
- signals: Every sounding line has a `V:` declaration, a stable identifier, and
  a location where its events can be checked.
- counterexample: A chord name or automatic accompaniment directive does not
  replace the required sounding notes.
- limits: Voice syntax support varies. Confirm that the host preserves all
  requested staves and playback material.

Keep one line's content locatable when possible. For revisions, inspect every
voice sharing the changed musical unit.

## id: `format.lilypond.version-and-self-contained`

- type: procedure
- facets: format, LilyPond, version, include, portability
- sources: lilypond-2-26
- confidence: established
- scope: New standalone candidates and compiler-verified deliveries
- signals: The file declares a compatible version and resolves every definition
  from the file or a declared internal facility.
- counterexample: Compiling in a directory that happens to contain an old local
  include does not make the score self-contained.
- limits: Existing multi-file projects can legitimately retain includes. Report
  that dependency instead of deleting it.

For a new candidate, set the tested version and keep musical definitions in the
candidate. Compile in a fresh output directory.

## id: `format.lilypond-relative-and-absolute-pitch`

- type: fact
- facets: format, LilyPond, pitch, relative, absolute, octave
- sources: lilypond-2-26
- confidence: established
- scope: LilyPond pitch entry
- signals: The mode is explicit. Relative anchors and inherited durations are
  traced through octave marks and intervening commands.
- counterexample: Assuming every unmarked pitch returns to the previous explicit
  octave can introduce silent octave errors.
- limits: Music21 or MIDI evidence can help, but must be tied to the compiled
  source version.

Absolute mode is easier to audit; relative mode is acceptable when its anchors
are checked.

## id: `format.lilypond-polyphony`

- type: procedure
- facets: format, LilyPond, Staff, Voice, polyphony, piano
- sources: lilypond-2-26
- confidence: established
- scope: Independent or rhythmically distinct voices
- signals: `Staff`, `Voice`, and simultaneous grouping reflect the intended
  musical roles; each independent voice starts and ends cleanly.
- counterexample: Two melodic strands in one keyboard sequence are not
  automatically two voice contexts.
- limits: Staff count expresses notation layout, not necessarily perceptual
  voice identity.

Use explicit voice contexts when independence or overlapping durations require
them. Review the rendered structure, not only the source labels.

## id: `format.compile-evidence`

- type: fact
- facets: verification, compile, artifact, hash, diagnostics
- sources: project-workflow
- confidence: established
- scope: Technical acceptance claims
- signals: The report's source hash matches the delivered score, the expected
  PDF or MIDI exists, and the diagnostics are complete.
- counterexample: A stale success report does not validate an edited source.
- limits: Compilation cannot establish form, stylistic fit, or performance
  quality.

Report compiler status, product presence, and the source version separately
from musical review.

## id: `corpus.source-admission`

- type: procedure
- facets: corpus, source, license, provenance, conversion, score
- sources: project-workflow
- confidence: established
- scope: Admitting a score excerpt into retrieval or training
- signals: The record has a canonical source URL, retrieval date, content hash,
  license, allowed uses, format version, conversion loss, parser or compiler
  status, and a locatable bar or source range.
- counterexample: Publicly downloadable PDFs or ABC files do not automatically
  grant redistribution, retrieval, or training rights.
- limits: Record-level rights and source-edition rights can differ; the card
  cannot replace a legal review.

Keep score evidence as `retrieval`, `display`, and `training` permissions
separately. Reject a record as trusted evidence when provenance or the precise
excerpt range is unknown.

