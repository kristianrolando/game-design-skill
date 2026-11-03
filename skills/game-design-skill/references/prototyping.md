# Prototyping lens

Covers turning uncertainty into tests: mapping what the team does not know, choosing the right prototype, defining when to stop, pressure-testing plans and widening options when stuck.

## When to use

- A concept is about to move into production with untested core assumptions.
- The team cannot agree on what to prototype first.
- A prototype has grown into a production build without answering its question.
- A plan needs a pre-mortem before commitment.
- The design is stuck between one or two options, or none.

## Gather

- The concept, core loop and pillars, even if rough.
- What has already been built or tested, and what was learned.
- Team skills, tools and time available for prototyping.
- The decision the prototype should inform: greenlight, pitch, pivot or tuning.

## Checks

### Uncertainty map

Sort the design's beliefs into four groups.

1. **Known**: verified by a build, playtest or data.
2. **Known unknown**: open questions the team is aware of.
3. **Untested belief**: things the team treats as true without evidence, often "obviously fun" or "players will understand".
4. **Blind spot**: areas nobody has discussed. Probe controls on the target device, readability at real screen size, content cost per hour of play, multiplayer dynamics, monetization fit and performance limits.
5. Rank items by impact if wrong multiplied by how uncertain they are. The top two or three are the prototype targets.

### Prototype questions

1. Turn each target into one falsifiable question, such as "Can first-time players read enemy intent within one second on a phone screen?"
2. Define the signal that answers it: an observed behavior, a completion rate, a quote pattern, a time measure.
3. Name who will play: the team, friends, or target-audience strangers. Team opinions answer feasibility questions, not fun questions.

### Prototype type

Match fidelity to the question.

1. Paper or tabletop: rules, economy, turn structure, choices.
2. Greybox in engine: feel, controls, camera, pacing, level flow.
3. Spreadsheet or simulation: economy balance, progression curves, drop rates.
4. Faked system (a person or script behind the curtain): AI behavior, matchmaking, narrative reactivity.
5. Art or audio target: tone, readability, style feasibility.
6. Technical spike: performance, networking, platform limits.
7. Vertical slice: production pipeline and final quality bar, only after core questions are answered.

### Stop and kill criteria

1. Set a timebox and the result that means continue, change or stop.
2. Agree the kill result before building, so sunk cost does not decide later.
3. Check prototype intent: is the build still answering its question, or have polish and features crept in?

### Pre-mortem

1. Assume the game or feature failed a year after launch. List the most credible causes across design, audience, scope, technology, market and team.
2. For each cause, name the earliest warning sign and the cheapest test that would show it now.

### Options when stuck

1. Generate at least five distinct approaches before choosing. Include "remove the feature", "reuse an existing system" and "solve it with presentation instead of mechanics".
2. Describe the ideal player-facing result, then work backward to the steps needed.
3. Name the main blocker and imagine it gone; what would the design be? Then find a path around it.

## Common problems

- **Building the fun last**: art and systems before the core is proven.
- **Unfalsifiable prototype**: "see if it's fun" with no signal or players defined.
- **Wrong fidelity**: a full engine build to test an economy a spreadsheet could check.
- **Prototype creep**: the test build becomes the production build without a decision.
- **No kill criteria**: every result is read as "promising".
- **Single-option thinking**: the first idea is the only idea.

## Fix menu

- Write a one-paragraph prototype brief: question, type, players, signal, timebox, kill result.
- Prototype the riskiest untested belief first, at the lowest fidelity that can answer it.
- Run one stranger playtest before any production commitment.
- Hold a 30-minute pre-mortem and turn the top three causes into tests.
- Before deciding, list five options and the cost of each.

## Reporting notes

- Present the uncertainty map as a ranked table: belief, group, impact, uncertainty, test.
- Every prototype recommendation must include its question and kill result.
- Next steps should be tests, not opinions.
