<!-- music-kb:page {"id": "page.0694c618f11741c5a186eb46276dd06c"} -->
# Phrase and form cards

## id: `form.motif-identity`

- type: procedure
- facets: motif, motive, identity, development, recurrence
- sources: omt-sentence, omt-sonata-development
- confidence: established
- scope: Tonal and post-tonal material that is explicitly derived
- signals: The card names the actual pitch-class, interval, rhythm, contour, or
  register features being preserved or changed.
- counterexample: A similar character, dynamic, or texture does not by itself
  establish the same motive.
- limits: Identity is contextual. One missing feature can be a deliberate
  variation.

Store an authoritative motif excerpt. Derivation claims must compare that
excerpt with real derived notes.

## id: `form.sentence`

- type: procedure
- facets: form, theme, sentence, presentation, continuation, cadence
- sources: omt-sentence
- confidence: established
- scope: Classical sentence theme prototype
- signals: An opening presentation repeats or varies a basic idea over stable
  harmony; a continuation uses at least one of fragmentation, sequence,
  liquidation, or rhythmic acceleration; a cadence closes it.
- counterexample: Four bars plus four bars is not automatically a sentence.
- limits: Lengths and cadences can be expanded, compressed, or elided.

Plan both presentations before writing the continuation. Prove the closing
cadence in the actual voices.

## id: `form.period`

- type: procedure
- facets: form, theme, period, antecedent, consequent, cadence
- sources: omt-period
- confidence: established
- scope: Classical period theme prototype
- signals: A basic idea recurs between antecedent and consequent; two cadences
  form a weak-to-strong relationship.
- counterexample: Repeated material without a second, stronger cadence is not
  sufficient evidence of a period.
- limits: Consequent material can be varied or partly new.

Show both cadence targets and the melodic scale degrees at their arrivals.

## id: `form.hybrid-and-compound`

- type: concept
- facets: form, theme, hybrid, compound, sentence, period
- sources: omt-theme-types
- confidence: established
- scope: Classical theme taxonomy
- signals: The theme's phrase functions are labeled individually before a
  category name is chosen.
- counterexample: Every unusual eight-bar theme should not be forced into a
  hybrid type.
- limits: The taxonomy is an analytical model, not a general law for later
  styles.

Describe observed functions first. Use a category only when it explains the
actual phrase organization.

## id: `form.sonata-exposition`

- type: procedure
- facets: form, sonata, exposition, primary, transition, secondary, closing
- sources: omt-sonata-intro, omt-sonata-exposition
- confidence: established
- scope: Common-practice sonata-form exposition
- signals: P, transition, S, and closing functions can be located through
  thematic behavior, cadences, and key regions.
- counterexample: Two melodies separated by a barline do not automatically make
  a two-theme exposition.
- limits: Continuous expositions, monothematic designs, and later-period
  deformations remain valid.

Write a function map before inventing headings. Connect each label to a bar
range, thematic anchor, and tonal arrival.

## id: `form.sonata-transition-and-caesura`

- type: procedure
- facets: form, sonata, transition, modulation, medial caesura
- sources: omt-sonata-exposition
- confidence: established
- scope: Sonata expository action
- signals: A transition either drives toward the secondary key or grows from the
  primary material; a medial caesura or an elided continuation is explicit.
- counterexample: A simple modulation is not necessarily a complete transition
  function.
- limits: Multiple valid exposition types exist.

Mark the tonal destination and the formal break, then check the arrival in every
voice.

## id: `form.sonata-secondary-and-eec`

- type: procedure
- facets: form, sonata, secondary theme, closing, EEC, cadence
- sources: omt-sonata-exposition
- confidence: established
- scope: Tonal sonata exposition
- signals: The secondary action reaches a new key; its essential expositional
  closure is evidenced by a cadence before closing material.
- counterexample: A half cadence in a new key is not a completed essential
  expositional closure.
- limits: Specific closure types vary by theory and repertoire.

State the cadence type, key, bass scale degree, and melodic arrival.

## id: `form.sonata-development-tonal-plan`

- type: procedure
- facets: form, sonata, development, key, instability, retransition
- sources: omt-sonata-development
- confidence: established
- scope: Common-practice development sections
- signals: Subordinate key areas are explored without the same stable closure
  expected in exposition; tension points toward a recapitulatory return.
- counterexample: A development is not merely a list of remote keys.
- limits: Key plans are heuristic and often individualized.

Plan key regions, cadence strength, and the retransition as separate axes.

## id: `form.sonata-development-modules`

- type: procedure
- facets: form, sonata, development, core, preparation, retransition
- sources: omt-sonata-development
- confidence: established
- scope: Common-practice development organization
- signals: Preparation, central action, and retransition can be distinguished by
  stability, material treatment, and harmonic function.
- counterexample: A new theme or a loud passage does not by itself create a
  development core.
- limits: Optional modules and overlapping functions are common.

At minimum state where instability begins, where the core peaks, and how the
return is prepared.

## id: `form.sonata-recap-and-crux`

- type: procedure
- facets: form, sonata, recapitulation, correspondence, crux, ESC
- sources: omt-sonata-recap
- confidence: established
- scope: Sonata recapitulation
- signals: Exposition and recapitulation are compared for corresponding,
  referential, or altered material; the crux and essential sonata closure are
  located.
- counterexample: Repetition of the opening theme does not prove a complete
  recapitulation.
- limits: The theory's closure term is specific to its analytical framework.

Align the exposition and recapitulation bar by bar. State what changed to bring
secondary material toward tonic closure.

## id: `form.rondo`

- type: procedure
- facets: form, rondo, refrain, episode, return
- sources: omt-rondo
- confidence: established
- scope: Classical rondo prototypes
- signals: A refrain recurs with identifiable boundaries, separated by
  contrasting episodes.
- counterexample: An ABA melody does not automatically become a five-part rondo.
- limits: Episode function and return treatment vary.

Provide a return map and scale-degree context for every refrain.

## id: `form.minuet-and-trio`

- type: procedure
- facets: form, minuet, trio, scherzo, dance
- sources: omt-minuet
- confidence: established
- scope: Common-practice minuet or scherzo and trio
- signals: Each dance has internally coherent binary or rounded sections, while
  the trio changes key, instrumentation, texture, or character and returns to the
  first dance.
- counterexample: A literal da capo does not excuse an incomplete trio.
- limits: Later scherzi expand the model substantially.

Write both members before evaluating the return. Check transition bars and
repeat directions.

## id: `form.variation`

- type: procedure
- facets: form, variation, theme, transformation, character
- sources: umn-variations
- confidence: provisional
- scope: Theme-and-variations tasks
- signals: Each variation preserves a checkable ground, or deliberately
  replaces it, while changing a named parameter such as melody, harmony,
  rhythm, texture, register, or role.
- counterexample: Repeating the same accompaniment with louder dynamics is weak
  evidence of a new variation.
- limits: Free variation and character variation can relax literal recurrence.

Record the ground and the operation for every variation. Vary the mechanism,
not only the decoration.

## id: `form.multi-movement-coherence`

- type: procedure
- facets: form, cycle, movement, transition, return, unity
- sources: project-workflow
- confidence: provisional
- scope: Multi-movement compositions with a requested cycle-level arc
- signals: Movements have distinct functions and a designed relationship in key,
  tempo, weight, material, or ending posture.
- counterexample: Giving every movement the same subject does not automatically
  make a cycle coherent.
- limits: Coherence can be contrastive rather than thematic.

Write an inter-movement plan and inspect the final bars against the following
opening. Preserve the exact source of any returning theme.

