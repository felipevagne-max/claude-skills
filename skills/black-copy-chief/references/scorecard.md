# Creative Route Scorecard

Use this scorecard only after duplicate routes have been resolved through territory
redistribution and reruns, or the Chief has approved an explicit degradation. Score each
remaining route independently against the same frozen Argument Bible on a 1–5 scale;
do not reward attractive prose that changes the agreed strategy.

## Dimensions

| Dimension | 1 — fails | 3 — workable | 5 — exceptional |
|---|---|---|---|
| Hook force | Generic, predictable, or disconnected from the prospect. | Relevant and clear but not difficult to ignore. | Creates immediate, credible tension and pays for the prospect's next moment of attention. |
| One Belief coherence | Introduces a competing thesis or contradicts the Bible. | Supports the One Belief with minor drift or avoidable detours. | Every major beat advances the same belief transformation without visible strain. |
| Belief-building | Asserts the conclusion or relies on pressure instead of conviction. | Supplies a plausible chain with one underdeveloped bridge. | Moves from accepted premise to conclusion through clear, resistance-aware causal steps. |
| Tension and curiosity | Closes loops too early, stalls, or uses empty teasing. | Sustains interest with occasional flat or decorative passages. | Opens meaningful loops, pays them off, and makes each answer create the next useful question. |
| Specificity | Depends on abstractions, adjectives, or stock copy language. | Uses some concrete scenes, distinctions, or mechanisms. | Makes the problem, process, consequence, and solution vividly concrete without unsupported precision. |
| Natural PT-BR | Sounds translated, robotic, theatrical, or unlike the audience. | Mostly natural with isolated generic or written-only phrasing. | Sounds human when read aloud and matches the prospect's vocabulary, rhythm, and social context. |
| Full-format sustainability | Has a strong fragment but cannot carry the requested format. | Can support the piece with predictable repetition or thin middle sections. | Provides enough causal, emotional, narrative, and proof-bearing material to sustain the whole format. |
| Factual integrity | Invents, inflates, disguises, or implies unsupported material. | Contains no clear invention but blurs an inference, boundary, or evidence condition. | Every material claim stays within the Proof Ledger, preserves conditions, and marks every gap visibly. |

Use whole-number scores only. Add one concise evidence note for every score; the note
must cite a route element or a specific absence rather than a general impression.

Store evidence notes in the canonical `Route × Dimension × Score × Evidence` shape,
with exactly one record per route and dimension:

```yaml
score_evidence:
  - route: "visceral-v2"
    dimension: "hook_force"
    score: 5
    evidence: "The opening makes the cost of reactive work concrete without adding a new claim."
```

Use these dimension keys: `hook_force`, `one_belief_coherence`, `belief_building`,
`tension_curiosity`, `specificity`, `natural_pt_br`, `full_format_sustainability`, and
`factual_integrity`. The summary table is derived from these records; it does not
replace them.

## Score table

```markdown
| Route | Hook | One Belief | Belief-building | Tension | Specificity | Natural PT-BR | Sustainability | Integrity | Total | Eligible? |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| Visceral |  |  |  |  |  |  |  |  |  |  |
| Mechanism |  |  |  |  |  |  |  |  |  |  |
| Story |  |  |  |  |  |  |  |  |  |  |
```

Factual integrity below `5` disqualifies a route. One Belief coherence below `4`
disqualifies a route. A disqualified route cannot win on total score, and its unsafe
or incoherent elements cannot be imported into the winner.

## Selection procedure

1. Confirm that all routes used the same frozen Bible version and complete route schema.
2. Diagnose duplicates, preserve the clearest representative, and rerun redundant slots under redistributed territories until three distinct routes or an explicit Chief-approved degradation exists.
3. Score every dimension with an evidence note, then apply the two disqualification rules.
4. Sum the eight scores only for eligible routes and rank them by total.
5. When eligible routes tie, choose the route whose mechanism is easiest to demonstrate honestly in the requested format.
6. Record the winner and the specific reason it can sustain the complete piece.
7. Evaluate secondary elements separately for compatibility with the winner's One Belief, villain, mechanism, emotion, evidence boundary, and voice.
8. The Chief makes and records the final decision; workers do not self-select or merge their routes.
