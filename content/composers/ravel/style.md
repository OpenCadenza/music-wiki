<!-- music-kb:page {"id": "page.e0df9ea1f71d4eb4a9eea9806c82b759"} -->
# Ravel: operational style profile

<!-- knowledge: composer.ravel.style -->

"Ravel-like" is a retrieval hint and a hypothesis to test. Build the actual
brief from observable decisions: pitch collection, harmonic function, spacing,
melodic interval pattern, rhythmic layering, formal boundary, and instrumental
role. The label "Impressionist" is too coarse to determine those decisions.

## id: `ravel.style.modal-melody-with-tonal-anchors`

- type: concept
- facets: Ravel, melody, mode, tonality, Aeolian, Dorian, Phrygian, Ionian
- sources: ravel-jenkins-quartet-thesis, ravel-kilpatrick-mere, omt-impressionism
- confidence: provisional
- scope: Modal melodies in the analyzed chamber and fairy-tale works
- signals: The melodic collection and characteristic degree are stated; a bass arrival or cadence still defines closure when the passage is tonal.
- counterexample: A white-note scale or an unresolved chord does not by itself establish a Ravelian mode.
- limits: Modal labels can depend on the analytical span and on notes supplied by accompaniment.

Write the intended mode, its tonic or referential center, the characteristic
degree, and the cadence strategy. Check the realized melody rather than relying
on a score comment.

## id: `ravel.style.extended-sonority-and-function`

- type: concept
- facets: Ravel, harmony, ninth, eleventh, added tone, function, colour
- sources: ravel-cambridge-harmony, omt-impressionism
- confidence: interpretive
- scope: Tertian and coloristic sonorities where a functional or registral anchor can be identified
- signals: The chord spelling, bass, outer voices, resolution, and local formal purpose are all visible in the score.
- counterexample: Stacking ninths and elevenths at every change is a generic modernist texture, not a style model.
- limits: A vertical pitch set alone does not determine harmonic function, root, or intended color.

Prefer a small number of designed sonorities with specific spacing and
resolution behavior. Require the agent to state which pitch is the bass, which
voice carries identity, and whether the sonority prolongs, displaces, or
abandons a function.

## id: `ravel.style.parallel-planes-with-controlled-voice-leading`

- type: procedure
- facets: Ravel, planing, parallelism, parallel chords, register, texture
- sources: omt-impressionism, ravel-jenkins-quartet-thesis
- confidence: provisional
- scope: Deliberate harmonic or registral planes described by the sources
- signals: The moved sonority preserves a stated interval pattern; entry, exit, bass anchor, and interaction with an independent melody are marked in the score.
- counterexample: A parser warning about parallel motion is not proof that an intentional plane fails, and unplanned consecutive fifths are not automatically stylistic.
- limits: Historical treatises and listeners may classify the same parallel motion differently.

Plan a plane for an audible reason: color shift, static suspension, ritual
repetition, register change, or formal transition. If strict counterpoint is a
separate task constraint, state which rule yields and why.

## id: `ravel.style.timbre-and-form`

- type: procedure
- facets: Ravel, orchestration, timbre, auditory stream, form, register, doubling
- sources: ravel-sound, ravel-bhogal-bolero
- confidence: interpretive
- scope: Multi-instrument passages and transcriptions
- signals: Instrumental entrances, onset alignment, register, attack, and doubling are mapped to an audible stream and a formal event.
- counterexample: More instruments or a new color on every phrase does not guarantee orchestral development.
- counterexample: A gesture borrowed from a large orchestra may exceed a quartet's means or obscure the quartet's four independent lines.
- limits: Timbre, balance, and masking require score study or audition and cannot be established by MIDI pitch alone.

For each phrase, list four roles: leading line, harmonic support, bass,
counterline/color. Then test whether the listener hears one blended stream or
several streams. The choice should change at meaningful boundaries rather than
at an arbitrary fixed interval.

## id: `ravel.style.classical-frame-with-distortion`

- type: analysis
- facets: Ravel, form, sonata, cycle, proportion, cadence, closure
- sources: ravel-heinzelmann-dissertation, ravel-jenkins-quartet-thesis, omt-sonata-intro
- confidence: provisional
- scope: Pre-war chamber works discussed by the cited scholarship
- signals: Exposition, development, recapitulation, coda, and cyclic return are supported by harmonic arrival or departure and by thematic transformation, not only by rehearsal letters.
- counterexample: An unusual key or missing literal repeat does not make a movement formless.
- limits: Sonata-form boundaries remain interpretive, and different editions can shift page or measure references.

Build the form as expected events plus permitted distortions. For every claimed
return or closure, record the exact material, pitch center, bass arrival, and
measure range.

## Working checklist

Before writing:

- name a period and work scope;
- distinguish modal collection from harmonic function;
- choose at most three color mechanisms;
- define how the target ensemble can realize each mechanism;
- state the expected formal points where texture or metric behavior changes.

Before delivery:

- compile the current source;
- inspect all four string parts as sounding lines and as playable gestures;
- verify claimed modal, harmonic, and cyclic relations from actual notes;
- compare accidental similarity with the source work;
- report technical, musical, and user-constraint outcomes separately.

