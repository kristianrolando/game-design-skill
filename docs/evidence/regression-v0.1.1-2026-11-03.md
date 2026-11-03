# Regression runs for v0.1.1, 2026-11-03

Checks of the v0.1.1 Deliverable rule in `skills/game-design-skill/SKILL.md`, run on macOS in disposable folders outside this repository. Each folder held only a copy of `skills/game-design-skill`. Baseline folders replaced `SKILL.md` with the copy from tag `v0.1.0`; the lens files are identical in both versions.

## Inputs

The two prompts reuse the inputs of earlier trials verbatim, so results can be compared with them:

- **Diagnose:** the Gravekeeper's Garden emotional direction question from [the v0.1.0 trial that showed the deviation](../examples/emotional-direction-gravekeepers-garden-claude.md).
- **Develop:** the Lantern Post one-page design doc request from [the direct-skill trial](../examples/one-page-gdd-lantern-post-claude-skill.md).

For Codex, the leading `/game-design-skill` was replaced with `Use $game-design-skill:`, and the prompt ended with the line used in the Ember Pact trial: "After your answer, add one final line: FILES READ: followed by the skill files you read."

## Claude Code

Claude Code CLI 2.1.287, `claude -p`, model `claude-opus-5-5`, direct skill in `.claude/skills/`, allowed tools Read, Skill and Glob. Both runs (diagnose and develop) stopped before any model turn: the account had reached its five-hour session limit. **No Claude result exists for v0.1.1.** This is the host where the original deviation was observed, so the fix is not yet confirmed there.

## Codex

Codex CLI 0.166.0-alpha.5.1, `codex exec --sandbox read-only`, model `gpt-6.1-sol` from the local configuration, native project skill discovery from `.agents/skills/`. Each run took about 47 to 59 seconds. Every run read `SKILL.md` and then only the lens files listed.

| Run | SKILL.md | Lens files read | Deliverable section | Report structure |
| --- | --- | --- | --- | --- |
| Diagnose 1 | v0.1.1 | emotional direction | None | Template headings in order; a proposed farewell scene sits inside minimal fix F4 |
| Diagnose 2 | v0.1.1 | emotional direction | None | Same sections in order, written as bold labels instead of Markdown headings; Lens column missing from the priority table |
| Diagnose baseline | v0.1.0 | emotional direction | None | Template headings in order |
| Develop 1 | v0.1.1 | pitch and GDD, core loop, scoping | n/a | One-page design doc only; no Summary, findings, priority table, fixes or next steps |
| Develop 2 | v0.1.1 | pitch and GDD, core loop, scoping | n/a | One-page design doc only |
| Develop baseline | v0.1.0 | pitch and GDD, core loop, scoping | n/a | One-page design doc only |

## What this shows

- **No regression in diagnose mode.** Under v0.1.1 neither diagnose run added a Deliverable section, and the first run placed its proposed artifact inside a minimal fix, as the new wording asks.
- **The fix is not demonstrated by these runs.** The Codex baseline under v0.1.0 also omitted Deliverable, so Codex does not reproduce the original deviation. Confirming the fix needs a Claude Code rerun of the diagnose input.
- **Known limit, not caused by v0.1.1:** in develop mode Codex returned only the requested document, without the surrounding report. This happened under both versions, so it predates v0.1.1. The earlier Claude develop trial (Lantern Post) did keep the full report. A clearer instruction for develop requests is a candidate for a later version.
- **Minor format drift:** one v0.1.1 diagnose run used bold labels instead of headings and dropped the Lens column. Single runs cannot tell whether this is related to the wording change.

## Limits

Single runs per cell, one Codex model, invented concepts. Outputs were kept in a temporary scratch folder and are not part of this repository; the first v0.1.1 diagnose output is reproduced below unedited, apart from removing the trailing file list (shown in the table) and trailing spaces.

## Diagnose 1 output (Codex, v0.1.1)

> # Game design review: Gravekeeper’s Garden
>
> **Context:** Cozy-horror farming · PC/Switch · adults drawn to Stardew Valley and spooky aesthetics · concept · supplied description and pitch-viewer feedback; slideshow not supplied.
> **Assumptions:** Caring for spirits is the central promise; emotional effects below are hypotheses until tested. Effort estimates refer to concept/pitch revisions.
> **Lenses:** Emotional direction, focused on fantasy and conflicting tone signals. Skipped a full retention audit and pitch review because the question concerns emotion and the slides weren’t supplied.
>
> ## Summary
>
> Your premise is clear, but its emotional direction is not yet coherent. Its strongest promise is **making an unsettling place feel cared for**: players should feel tenderness first, eerie curiosity during discovery, and bittersweet relief when a spirit leaves. The supported fantasy is: “I am a graveyard gardener who grows ghost flowers and fulfills final wishes so restless spirits can find peace.” Jump scares tied to crop failure and countdown rewards pull that promise toward vigilance and obligation, while upbeat chiptune may obscure its quieter emotional moments.
>
> ## Findings by lens
>
> ### Emotional direction
>
> - **F1 · Caring and punishment conflict (Assumed).** Evidence: withered crops trigger jump scares. Players may learn that imperfect care brings an unpleasant shock, making tending feel anxious rather than comforting. Horror can support this concept, but tying fright to gardening failure makes the player’s main caring activity feel threatening.
>
> - **F2 · The return invitation becomes pressure (Assumed).** Evidence: daily login rewards with countdown timers. These introduce a loss-pressure pattern: players may return to avoid missing something rather than because they want to visit their garden. There is no evidence of paid rewards or monetization here; the concern is the emotional pressure of expiring opportunities.
>
> - **F3 · Presentation lacks an emotional hierarchy (Assumed).** Evidence: pastel watercolor, upbeat chiptune, final wishes, and jump scares. These ingredients can coexist, but they currently suggest comfort, playfulness, grief, and alarm without establishing which leads. Pastels can make the supernatural approachable; continuous upbeat music could make a farewell feel emotionally weightless.
>
> - **F4 · The distinctive emotional payoff is underspecified (Observed).** Evidence: helping spirits move on is described, but no particular wish, player decision, or farewell is supplied. Viewers explicitly reported uncertainty about what to feel. That feedback establishes a communication problem; it does not yet prove the eventual game would feel confused.
>
> ## Priority issues
>
> | ID | Issue | Lens | Severity | Confidence | Effort |
> | --- | --- | --- | --- | --- | --- |
> | F1 | Crop failure threatens the caring fantasy | Emotional direction | P1 Critical | Assumed | S |
> | F2 | Countdown rewards introduce obligation | Emotional direction | P2 Major | Assumed | S |
> | F4 | No concrete emotional payoff demonstrated | Emotional direction | P2 Major | Observed | M |
> | F3 | Audio and presentation lack hierarchy | Emotional direction | P2 Major | Assumed | S |
>
> ## Minimal-fix recommendations
>
> 1. **F1: Replace failure-triggered jump scares with an eerie, recoverable response.** A withered flower could whisper or lose its glow, inviting restoration. Keep unease in discoveries and encounters. Expected effect: mistakes preserve the desire to care. Check whether viewers anticipate repair or punishment.
>
> 2. **F2: Remove countdowns and expiring daily rewards from the concept.** Let unfinished wishes and garden discoveries provide reasons to return. Expected effect: anticipation without attendance pressure. Check whether players describe returning as something they want to do.
>
> 3. **F4: Show one complete emotional sequence in the pitch.** For example, a spirit requests a flower associated with someone they miss; tending it reveals a memory, and offering it enables a quiet goodbye. This is a proposed scene, not an existing feature. Expected effect: viewers can identify the game’s emotional destination.
>
> 4. **F3: Give each target emotion a producing system and presentation cue.** Tenderness comes from tending and fulfilling wishes; curiosity from discovering spirits’ histories; bittersweet relief from farewells and their lasting traces. Reserve upbeat chiptune for routine activity and test a quieter treatment for departures. Avoid **guilt about absence**.
>
> ## Next steps
>
> 1. Revise the pitch around one sentence: **“Tend a gentle haunted garden, learn whom its spirits miss, and help them say goodbye.”**
> 2. Build a short storyboard of tending → uncanny discovery → final wish → farewell.
> 3. Show it to target players without naming the intended emotions. Ask what they expect to feel during play and after a spirit leaves. Look for independently expressed care, curiosity, and bittersweet relief.
