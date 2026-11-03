# Regression runs for v0.1.2, 2026-11-03

Checks of the v0.1.2 report rule in `skills/game-design-skill/SKILL.md`: develop requests keep the full report around the requested artifact. Runs used the same hosts, setup and inputs as the [v0.1.1 regression runs](regression-v0.1.1-2026-11-03.md), in new disposable folders outside this repository, each holding only a copy of the v0.1.2 `skills/game-design-skill`. All six runs started together at 14:56 Asia/Jakarta.

## Inputs

- **Develop:** the Lantern Post one-page design doc request from [the direct-skill trial](../examples/one-page-gdd-lantern-post-claude-skill.md). Under v0.1.0 and v0.1.1, Codex answered this request with the document only.
- **Diagnose:** the Gravekeeper's Garden emotional direction question, to check that the Deliverable rule from v0.1.1 still holds.

Codex prompts were the v0.1.1 Codex prompts verbatim (`Use $game-design-skill:` and the final FILES READ line); Claude Code prompts used `/game-design-skill`.

## Results

| Run | Host | Lens files read | Deliverable section | Report structure |
| --- | --- | --- | --- | --- |
| Develop 1 | Codex | pitch and GDD, core loop, scoping | Yes, with the one-page doc | Full template in order: header, Summary, Deliverable, findings, priority table, minimal fixes, next steps |
| Develop 2 | Codex | pitch and GDD, core loop, scoping | Yes | Full template in order; Lens column missing from the priority table |
| Develop 3 | Codex | pitch and GDD, core loop, scoping | Yes | Full template in order; findings labelled by lens inline instead of lens subheadings |
| Diagnose 1 | Codex | emotional direction | None | Template headings in order |
| Develop | Claude Code | pitch and GDD, core loop, scoping | Yes, with the one-page doc | Full template in order, with lens subheadings |
| Diagnose | Claude Code | emotional direction, flow and fairness, FTUE and retention | None | Template headings in order; Summary answers "is it clear", "what should players feel" and "what is in the way" directly |

Hosts: Codex CLI 0.166.0-alpha.5.1, `codex exec --sandbox read-only`, model `gpt-6.1-sol` from the local configuration, native discovery from `.agents/skills/`. Claude Code CLI 2.1.287, `claude -p --output-format stream-json`, model `claude-opus-5-5`, direct skill in `.claude/skills/`, allowed tools Read, Skill and Glob; each init event listed the project skill, and each run took 4 turns (about 74 and 84 seconds).

## What this shows

- **The develop-mode gap is closed in these runs.** All three Codex develop runs kept the full report around the document, where the three earlier Codex runs of the same input (two under v0.1.1, one under v0.1.0) returned the document alone. The Claude Code develop run also kept the full report, as the v0.1.0 Lantern Post trial did.
- **No regression in diagnose mode.** Neither diagnose run added a Deliverable section.
- **Minor format drift remains in Codex:** one run dropped the Lens column again (also seen once under v0.1.1), and two develop runs wrote the lens name inside each finding instead of as a subheading. The sections and their order were always correct.

## Limits

Three runs for the Codex develop cell and one run for each other cell, one model per host, invented concepts. A 3 of 3 against 0 of 3 result is strong for this input and host but does not cover other artifact types (pillars, plans, options). Outputs were kept in a temporary scratch folder and are not part of this repository; the first Codex develop output is reproduced below unedited, apart from removing the trailing file list (shown in the table) and trailing spaces.

## Develop 1 output (Codex, v0.1.2)

> # Game design review: Lantern Post
>
> **Context:** Cozy narrative delivery · Switch and PC/controller · Adults playing in 30-minute sessions · Concept · Supplied notes
> **Assumptions:** New design proposals below are provisional; six months targets a vertical slice, not release.
> **Lenses:** Pitch/GDD for clarity, core loop/pillars for coherence, scoping for solo feasibility. Detailed onboarding deferred until a prototype exists.
>
> ## Summary
>
> Lantern Post’s strongest hook is the tension between carrying someone’s private words and becoming part of their story. The main design risk is making reading so rewarding that respecting privacy feels like missing content. The proposed document preserves that choice while keeping the slice small enough to test.
>
> ## Deliverable
>
> ### Lantern Post — One-page design doc
>
> **Logline:** Become the night courier of a mountain village, plotting lantern-lit delivery routes and deciding how closely to enter the lives behind each letter.
>
> **Genre / audience / platforms:** Cozy narrative exploration for adults who enjoy slow, story-rich play in approximately 30-minute sessions. Nintendo Switch and PC, designed around controller input.
>
> **Player fantasy:** Be a familiar light on a dark mountain: learn its paths, connect its households, and discover how much a trusted courier should know.
>
> **Core loop:** Pick 3–5 letters → inspect weather and plan a route on a hand-drawn map → walk or sled between houses → read or preserve each letter → deliver and experience villagers’ reactions → return home, progress stories, and prepare for another night.
>
> **Design pillars**
>
> - **Care over speed:** Reward attentive deliveries rather than fast completion; proposed design has no delivery countdown.
> - **Curiosity with discretion:** Reading reveals intimate context; preserving privacy must also produce satisfying story moments.
> - **Familiarity over scale:** Revisit a compact village whose weather and relationships change, instead of continually adding territory.
>
> **Key features**
>
> - **Route planning:** Choose delivery order and paths on a readable, controller-friendly map.
> - **Night travel:** Walk intimate village paths and sled suitable stretches; weather changes available connections.
> - **Private words:** Choose whether to read before delivery. Reading changes reactions and opens small side stories; proposed consequences have understandable causes.
> - **Lantern progression:** Upgrade the lantern to access farther paths, expanding route choices and introducing new households.
>
> **Session and progression:** One night targets 30 minutes, ending with a quiet return and a reason to revisit tomorrow. Proposed suspend/save support accommodates interruptions. Relationships and lantern access provide continuing progression.
>
> **Proposed presentation:** Stylized mountain silhouettes, warm windows and hand-drawn cartography. Snow, wind, footsteps and sparse music carry the atmosphere; text-led dialogue limits production demands.
>
> **Comparables:** A Short Hike and Spiritfarer are reference points for the intended warmth and character focus. Lantern Post’s distinguishing hook is delivery-route planning joined to the choice to read private correspondence.
>
> **Six-month slice — proposed scope:** One compact village area, four households, three authored nights, 9–12 letters, two weather states, one short sled route and one lantern unlock. Build a PC controller slice first; Switch remains a target platform. Prototype the loop in months 1–2, integrate representative content in months 3–4, and reserve months 5–6 for testing and polish. This is a planning target pending developer availability and prototype results.
>
> **Open questions / biggest risks:** How do villagers learn a letter was read? Is discretion equally engaging? Does travel sustain interest within 30 minutes? Branching narrative and sled handling are the main scope risks; simplify sledding first if needed.
>
> ## Findings by lens
>
> - **F1 · Choice imbalance — Core loop (Inferred):** The notes reward reading with additional stories but specify no equivalent for discretion. Players may feel compelled to read.
> - **F2 · Consequence clarity — Pitch/GDD (Observed):** Reading changes reactions, but the mechanism is unspecified. Unexplained knowledge could undermine trust.
> - **F3 · Production load — Scoping (Inferred):** Walking, sledding, weather and narrative branches compete for one developer’s six-month window.
>
> ## Priority issues
>
> | ID | Issue | Lens | Severity | Confidence | Effort |
> |---|---|---|---|---|---|
> | F1 | Reading dominates | Core loop | P2 | Inferred | M |
> | F2 | Unclear reaction logic | Pitch/GDD | P2 | Observed gap | S |
> | F3 | Interacting systems exceed capacity | Scoping | P2 | Inferred | M |
>
> ## Minimal-fix recommendations
>
> 1. **F1:** Give one unopened delivery a distinctive relationship scene. Check whether testers find both choices worthwhile.
> 2. **F2:** Tie changed reactions to information the courier reveals or an established observable clue. Check whether testers can explain the consequence.
> 3. **F3:** Use authored weather changes and a constrained sled route. Check development cost before expanding either system.
>
> ## Next steps
>
> 1. **Solo developer, first prototype:** Build one three-letter night with one consequential read/discretion choice.
> 2. **Before content production:** Test route enjoyment, consequence comprehension and session length with target players; revise slice scope from the results.
