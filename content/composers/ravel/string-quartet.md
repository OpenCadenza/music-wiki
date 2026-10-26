<!-- music-kb:page {"id": "page.045c61fea249441384d4990bee264cd9"} -->
# Ravel: String Quartet in F major

<!-- knowledge: ensemble.ravel.string-quartet -->

This page supports both analysis of Ravel's only string quartet and the design
of a new quartet that uses related compositional procedures. The score facts
come from the OpenScore CC0 encoding and the public-domain score scans listed in
`sources.json`. Formal and cyclic claims are cross-checked against independent
analyses and remain analytical interpretations.

## Basic frame

- Composer and work: Maurice Ravel, *String Quartet in F major* (M.35).
- Composition and publication: composed 1902-03 and revised before publication
  in 1910; do not use the 1902 date alone as the Published Version.
- Ensemble: two violins, viola, violoncello.
- Movements: I *Allegro moderato - très doux*; II *Assez vif - très rythmé*;
  III *Très lent*; IV *Vif et agité*.
- Source encoding used for measure and pitch checks: OpenScore score
  `8482283`, MuseScore 4.5.2 source, released as CC0 by the corpus.

The first movement is a Type 3 sonata-form reading in modern Sonata Theory
terms, but Wikipedian or textbook labels are not a substitute for locating the
actual exposition, development, recapitulation, and coda mechanisms in the
score.

## id: `ravel.sq.opening-material`

- type: analysis
- facets: Ravel, string quartet, F major, A Aeolian, motif, mode, first movement
- sources: openscore-string-quartets, ravel-jenkins-quartet-thesis
- confidence: established
- scope: Opening melody and its immediate accompaniment in movement I
- signals: The first violin presents a five-note opening cell; the lower parts establish a slowly changing modal/registral field before the phrase completes its broader four-plus-four organization.
- counterexample: Calling the whole opening simply "A minor" loses the F-major key signature, modal color, and changing bass.
- limits: Mode labels describe the local passage and need a stated tonic/collection.

The exact melody-only reduction is in
[the opening-excerpt analysis](examples/chamber-cyclic-writing.md).

## id: `ravel.sq.cyclic-return`

- type: analysis
- facets: Ravel, string quartet, cyclic form, motive, transformation, large-scale form, coda
- sources: ravel-jenkins-quartet-thesis, ravel-heinzelmann-dissertation
- confidence: interpretive
- scope: Reappearance and transformation of first-movement material later in the cycle
- signals: The slow movement repeatedly quotes the opening cell; the finale builds a new theme from other first-movement material; the coda recombines first-movement and finale material.
- counterexample: A literal cut-and-paste return is not the only possible cyclic relation.
- limits: the older Jenkins thesis supplies a detailed page-level inventory; readers should recheck exact measure numbers in the chosen modern edition because old page references differ.

Treat cyclic form as an auditable relation:

```text
source material
-> operation (quote, contraction, reharmonization, registral transfer,
              rhythmic change, contrapuntal combination)
-> new section or instrument
-> audible recognition cue
```

For a new quartet, store at least one later realization for each claimed return.
A plan comment such as "the theme returns" is not evidence.

## id: `ravel.sq.four-voice-division`

- type: procedure
- facets: Ravel, quartet, texture, orchestration, four voices, doubling, counterpoint
- sources: openscore-string-quartets, ravel-jenkins-quartet-thesis, ravel-sound
- confidence: provisional
- scope: Quartet scoring informed by the analyzed work
- signals: Outer voices, inner harmonic/motivic roles, attacks, register distance, and doubling are inspectable; the four parts have identifiable functions even when they combine into one stream.
- counterexample: Keeping four staffs populated does not guarantee quartet texture.
- limits: Score inspection cannot prove balance without audition, room, and player feedback.

Use the full quartet for changes that need four independent functions. Use
octave or unison doubling to make a structural arrival, alter an attack, or
construct a deliberately fused sound object. Avoid assigning a large-orchestra
density to the quartet merely because the pitch content fits.

## id: `ravel.sq.metric-and-formal-contrast`

- type: analysis
- facets: Ravel, quartet, rhythm, meter, scherzo, 6/8, 3/4, 5/4, finale
- sources: openscore-string-quartets, ravel-jenkins-quartet-thesis, philharmonie-ravel-quartet
- confidence: provisional
- scope: Movement II and the second-theme area of movement IV
- signals: The scherzo sets 6/8 against 3/4 within its opening design; the finale later introduces a 5/4 secondary area.
- counterexample: An odd meter alone does not produce Ravelian character or coherent hypermeter.
- limits: The source sources disagree in small details, and notation can be clear while audience perception remains ambiguous.

When transferring this device, specify both the notated measure and the pulse
the listener should entrain to. Check phrase endings against the actual meter.

## Cross-work transfer rules

For "a Ravel-influenced string quartet", select:

1. one modal/melodic procedure;
2. one harmonic or registral color procedure;
3. one quartet-specific texture or metric procedure;
4. one cycle or form relation;
5. one chosen anti-pastiche constraint, such as no literal quotation from
   Ravel.

These are design hypotheses. Success is measured by audible and score-visible
realization, not by the number of named traits.

## Source map

- OpenScore `8482283`: CC0 encoding used for score facts and the short exact
  opening excerpt.
- IMSLP / Wikimedia score scans and proofs: historical reference, public-domain
  status recorded at file level.
- Heinzelmann dissertation abstract: sonata-form and motivic transformation
  framework.
- Jenkins thesis: page-level inventory of cyclic returns and movement sections,
  used as a discovery index and independently checked against the score.
- Philharmonie de Paris: accessible movement-level listening guide; not treated
  as a compositional rulebook.

