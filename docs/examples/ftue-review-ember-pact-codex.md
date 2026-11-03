# Example: FTUE review of "Ember Pact" in Codex

## Trial record

- **Date:** 2026-11-03.
- **Host and model:** Codex CLI 0.166.0-alpha.5.1 (`codex exec`, read-only sandbox), model reported as `gpt-6.1-sol`.
- **Setup:** a disposable folder outside this repository with only a copy of `skills/game-design-skill` at `.agents/skills/game-design-skill/`. The prompt named `$game-design-skill` but gave no file path.
- **Files the agent reported reading:** `SKILL.md`, `references/ftue-retention.md`, `references/flow-fairness-failure.md`. The run log shows it located the project-local skill copy itself.
- **Output:** reproduced below unedited, apart from removing the trailing file list (shown above).
- **Limits:** one run of one model. The concept and playtest numbers were written for the trial; findings are design reasoning, not real playtest evidence.

### Input given to the agent

> Use $game-design-skill to review the first-time experience of my game and tell me where new players will drop and what to fix first.
>
> Ember Pact: a single-player deckbuilding roguelite for PC (mouse), for players who already enjoy Slay the Spire-style games. Stage: playable prototype, 12 playtesters so far. First launch: a 90-second unskippable lore cutscene, then account creation, then a tutorial that explains all six card types, energy, block, status effects and the map in 14 text pop-ups before the first fight. The first fight uses a fixed starter deck. After it, the player picks 1 of 3 cards. Playtest notes: 5 of 12 testers alt-tabbed during the cutscene; 3 asked "can I skip this?"; most said the first fight felt easy; 2 quit at the account screen.
>
> After your answer, add one final line: FILES READ: followed by the skill files you read.

### Reviewer notes

- Same report template as the Claude trial: context, assumptions and lenses, then Summary, Findings by lens, Priority issues, Minimal-fix recommendations and Next steps.
- Two lenses, chosen by the router's symptom table; the skipped core-loop lens is named with a reason.
- Confidence labels track the evidence: findings backed by playtest counts are Observed, others Inferred. It also cautions that 12 testers is directional, not a drop rate.
- Every minimal fix carries a check.

---

# Game design review: Ember Pact

**Context:** Single-player deckbuilding roguelite · PC/mouse · experienced genre players · playable prototype · opening sequence and notes from 12 testers.
**Assumptions:** Account creation currently gates play. Effort estimates are relative; implementation details are unknown.
**Lenses:** FTUE and retention for entry friction and learning; flow, fairness and failure for opening challenge. Skipped a full core-loop audit: the supplied material cannot establish whether later combat and deckbuilding work.

## Summary

**Fix the account gate first, then the unskippable cutscene, then the tutorial dump.** Ember Pact’s strongest opening asset is its familiar fight → card reward structure, which gives your audience a clear route into deckbuilding. Currently, players must watch, register and read before experiencing it. The account screen has confirmed exits; the cutscene has confirmed disengagement; tutorial abandonment and combat boredom remain predictions to test.

## Findings by lens

### FTUE and retention

Opening timeline: **90-second cutscene → account creation → 14 pop-ups → first fight → choose 1 of 3 cards.** Meaningful combat begins more than 90 seconds after launch; the actual delay is unmeasured.

- **F1 · Account gate loses players (Observed).** Evidence: 2 of 12 testers quit at the account screen. Player impact: they leave before sampling the core experience. Their reasons for quitting remain unknown.
- **F2 · Forced lore loses attention (Observed).** Evidence: 5 of 12 alt-tabbed and 3 asked to skip. Player impact: the opening already prompts disengagement. These groups may overlap; neither observation establishes that they quit.
- **F3 · Teaching precedes context (Inferred).** Evidence: 14 text pop-ups explain six card types and several systems before combat. Player impact: players may dismiss explanations or forget them before use. Experienced deckbuilder players also have to sit through familiar concepts before discovering Ember Pact’s differences.

### Flow, fairness and failure

- **F4 · First combat may undersell the game (Inferred).** Evidence: most testers described it as easy; the starter deck is fixed, with the first explicit deckbuilding choice afterward. Player impact: victory may demonstrate little tactical competence or personal direction. Easy does not automatically mean boring, and a fixed deck can still support meaningful combat choices.

| Phase | Demand versus audience | Likely experience |
| --- | --- | --- |
| Cutscene and account | Waiting and registration before play | Observed disengagement/exits |
| Tutorial | Many explanations without immediate practice | Inferred overload or impatience |
| First fight | Reportedly easy for genre veterans | Inferred underchallenge |
| Card reward | First explicit deckbuilding choice | Promising agency; response untested |

## Priority issues

| ID | Issue | Lens | Severity | Confidence | Effort |
| --- | --- | --- | --- | --- | --- |
| F1 | Account blocks access to play | FTUE | P1 Critical | Observed | M |
| F2 | Unskippable opening delays play | FTUE | P2 Major | Observed | S |
| F3 | Fourteen explanations before practice | FTUE | P2 Major | Inferred | M |
| F4 | Opening may lack a satisfying decision | Flow | P2 Major | Inferred | M |

## Minimal-fix recommendations

1. **F1: Let players start locally without registering.** Offer an account when a relevant benefit becomes useful. This removes the confirmed exit point. **Check:** can fresh testers reach combat without account-related abandonment?

2. **F2: Add a clearly visible skip control immediately.** Keep lore available for interested players. This restores control with a small change. **Check:** record skips, alt-tabs and time to first card played; skipping alone is not failure.

3. **F3: Replace the pop-up sequence with contextual teaching.** Explain only what the current turn needs, then let players use it. Introduce other card types, statuses and the map when encountered; keep details available on hover. **Check:** observe unaided play and rule misunderstandings, rather than asking whether players read everything.

4. **F4: Give the first fight one readable tactical tradeoff.** Keep the fixed deck for now. Make attack versus defence produce an understandable consequence without requiring tutorial-perfect play. Preserve the immediate card reward and let players use their selection soon afterward. **Check:** ask what decision affected the fight and why they chose their reward. Avoid increasing enemy health merely to extend combat.

## Next steps

1. **Next prototype build:** implement account bypass and cutscene skip first, then contextual prompts.
2. **Next fresh-player test:** track each opening step, exits, first card played, reward selection and entry into fight two. Treat the existing 12 testers as directional evidence, not a reliable population drop rate.
3. **After removing entry friction:** evaluate first-fight decisions before retuning difficulty. Players need enough attention left to judge combat fairly.
