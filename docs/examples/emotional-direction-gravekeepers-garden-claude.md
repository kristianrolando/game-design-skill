# Example: emotional direction review of "Gravekeeper's Garden" in Claude Code

## Trial record

- **Date:** 2026-11-03.
- **Host and model:** Claude Code CLI 2.1.287 in print mode (`claude -p`), model `claude-opus-5-5`, signed in with a claude.ai account.
- **Setup:** a disposable folder outside this repository containing only a copy of `skills/game-design-skill` at `.claude/skills/game-design-skill/`. Allowed tools: Read, Skill, Glob. Three lens trials ran in parallel in separate folders.
- **Invocation:** `/game-design-skill`. The prompt describes symptoms and does not name a lens, so lens choice is the router's.
- **Files read after the skill loaded:** `references/emotional-direction.md`, `references/core-loop-pillars.md`, `references/prototyping.md`. The run took 4 turns and about 99 seconds.
- **Output:** the final result, reproduced unedited. Its closing offer to make a shareable page comes from the host environment, not from the skill text.
- **Limits:** one run of one model. The concept and any figures in it were written for the trial; findings are design reasoning, not evidence about real players.

### Input given to the agent

> /game-design-skill Is the emotional direction of my game clear? What should players feel, and what is getting in the way?
>
> Gravekeeper's Garden: a cozy-horror farming game for PC and Switch, for adults who like Stardew Valley and spooky aesthetics. Stage: concept, with a slideshow pitch. You tend a graveyard garden at night, grow ghost flowers, and help restless spirits move on by granting their final wishes. Art: pastel watercolor. Music: upbeat chiptune. Daily login rewards with countdown timers. Jump-scare events happen when crops wither. Viewers of the pitch said "cute, but I don't know what I'm supposed to feel".

### Reviewer notes

- First trial of the emotional direction lens. It extracted the fantasy as one sentence and tabulated the tone signals of each layer (art, music, features, theme), as the lens asks.
- The ethics rule fired unprompted: daily login countdown timers are flagged as loss pressure, with a condition that would raise them to P1.
- Minor deviation: the request was a diagnosis, yet the report added a `Deliverable` section with a proposed tone guide. The router reserves Deliverable for develop requests. The content is useful and labeled as a proposal.
- Next steps are tests with continue and change signals, not opinions.

---

# Game design review: Gravekeeper's Garden (emotional direction)

**Context:** Cozy-horror farming sim · PC and Switch (controller and handheld) · adults who like Stardew Valley and spooky aesthetics · concept stage · reviewed: your summary of the slideshow pitch and one viewer reaction
**Assumptions:** (1) I haven't seen the deck itself, so slide-level evidence comes from your summary. (2) It's a premium game, not free-to-play. (3) The summary doesn't say how the ghost flowers relate to the spirits' wishes. (4) It doesn't say whether crops wither on in-game time or on real-world time while the player is away.
**Lenses:** **Emotional direction** (the main question). **Core loop** (to check whether "helping spirits move on" is something the player actually does, not just a theme). **Prototyping** (at concept stage, the next steps should be tests). Skipped: **Motivation** and **FTUE/retention**. The login rewards fall under them, but here they are covered as a tone and ethics issue. Also skipped **Pitch review**, because I don't have the deck.

## Summary
Gravekeeper's Garden has a strong core idea: farming as mourning, where you grow flowers so the dead can let go. That idea suggests one clear feeling, tender, bittersweet comfort. The pitch doesn't name that feeling, and each layer of the game points somewhere else. The art says *cute*, the music says *playful*, the jump scares say *afraid*, and the login timers say *hurry*. Viewers said "cute, but I don't know what I'm supposed to feel" because "cute" is the only signal that reached them clearly. **Verdict:** the direction is not clear yet. It is easy to fix at concept stage: pick one main emotion, and cut or rework the two features that fight it.

## Deliverable: proposed emotional target
*This is a proposal. You decide; the findings below hold for whichever direction you choose.*

- **Fantasy:** "I am the night gardener of the dead, who grows each spirit the flowers of its unfinished life so that it can let go, and my garden keeps what they leave behind."
- **Main emotion: tender melancholy** (bittersweet comfort). Produced by: each spirit's arc, which ends in a farewell.
- **Second emotion: eerie wonder** (spooky as atmosphere, not threat). Produced by: the night garden, strange ghost-flower varieties, and the mystery in each wish.
- **Supporting emotion: quiet pride in caring for things.** Produced by: a garden that slowly becomes a memorial to everyone you helped.
- **Emotions to avoid:** startle and obligation.
- **Never rules:**
  1. Never punish neglect with shock.
  2. Never put a real-world clock on the player.
  3. Never interrupt a farewell with a pop-up or a chore.
- **Reference moments:**
  1. The first ghost flower blooms at midnight and a spirit drifts over to look.
  2. A neglected flower bed droops, and the spirit who wanted those flowers sits beside it quietly. Sad, not scary.
  3. At dawn, a spirit takes its bouquet, fades with the sunrise and leaves a seed behind.

In this framing, the "horror" in cozy-horror means *eerie*, not *frightening*. That matches a Stardew audience that likes spooky *aesthetics*.

## Findings by lens

### Emotional direction
- **F1 · No named target emotion** (Inferred): The pitch uses a genre label ("cozy-horror") and an art label ("pastel watercolor"), but no feeling. "Cozy-horror" is two moods in tension, and nothing says which one leads or how they relate. Evidence: the concept summary; the viewer quote. Player impact: viewers fill the gap with the most visible signal (the art) and leave with "cute", which describes the art, not an emotion.
- **F2 · Four layers, four different emotions** (Observed): Each listed element signals something different:

  | Element | What it signals |
  | --- | --- |
  | Pastel watercolor art | soft, gentle |
  | Upbeat chiptune music | energetic, arcade-like |
  | Jump scares | shock |
  | Countdown timers | urgency |
  | The theme (death, final wishes) | melancholy |

  No two of these agree. Evidence: art, music and features as described; "I don't know what I'm supposed to feel". Player impact: the mixed signals cancel out, and the theme's emotional weight never comes through.
- **F3 · Jump scares on withering punish failure with shock** (Inferred): This makes the player's most common mistake (neglecting crops) the trigger for the one emotion cozy players avoid. Players will learn to feel anxious looking at their own garden. Two further problems:
  - Being made to flinch at your crops has nothing to do with "helping spirits rest".
  - Unexpected scares are an accessibility concern on handheld Switch, especially if they can't be turned off (that isn't stated).

  Evidence: the "jump-scare events when crops wither" rule. Player impact: this breaks the cozy promise, and the target audience may stop playing.
- **F4 · Login timers clash with the theme and pressure players** (Observed, and flagged as a manipulative pattern):
  - **Tone:** countdown timers create urgency and fear of missing out. Your game is about *letting go*, and this system is about *holding on*.
  - **Ethics:** this is loss pressure in a premium PC/Switch game, where the genre's reference point (Stardew) has no such system.
  - **Worse case:** if crops wither on real-world time (assumption 4), then timers, withering and jump scares together form a fear-based return loop. That would raise this to P1.

  Evidence: the "daily login rewards with countdown timers" feature. Player impact: the game feels like a mobile retention product, and that undercuts the cozy promise.

### Core loop
- **F5 · The emotional payoff isn't wired into the loop or shown as the peak** (Assumed: the summary doesn't link flowers to wishes): As written, the loop has a gap:

  plant and tend ghost flowers → bloom → **?** → grant a wish → spirit moves on → **?** reason to start the next night

  If flowers are ordinary crops and wishes are side quests, the theme only lives in the story and art while the mechanics stay standard farming. Meanwhile, the most vivid event the pitch describes is a jump scare, not a farewell. The farewell is the moment a player would describe to a friend, and nothing shows it. Evidence: the concept summary. Player impact: the theme reads as a skin, and there's no memorable peak to anchor the feeling.
- **F6 · The fantasy is close to an existing game** (Inferred): Granting spirits' final wishes and then releasing them is the central loop of Spiritfarer. What is new here is the *garden*: flowers as the language of mourning, and a graveyard that grows as people leave. Evidence: the summary, compared with a known title. Player impact: if the pitch leads with wish-granting, it reads as derivative. If it leads with the garden-as-memorial, it reads as distinct.

## Priority issues
| ID | Issue | Lens | Severity | Confidence | Effort |
| --- | --- | --- | --- | --- | --- |
| F1 | No named target emotion | Emotional direction | P1 | Inferred | S |
| F3 | Jump scares as the penalty for failure | Emotional direction | P1 | Inferred | S to cut, M to replace |
| F2 | Art, music, features and theme each point to a different emotion | Emotional direction | P1 | Observed | M |
| F5 | Farewell not wired into the loop or the pitch | Core loop | P2 | Assumed | M |
| F4 | Login countdown timers (manipulative pattern) | Emotional direction | P2 (P1 if withering is real-time) | Observed | S |
| F6 | Fantasy close to Spiritfarer's | Emotional direction | P3 | Inferred | S |

## Minimal-fix recommendations
1. **F1: Adopt a one-page tone guide** (the deliverable above, or your own version) that names one main emotion. Why: everything downstream needs one test to measure against. Expected effect: the team and pitch viewers can name the feeling. Check: show the revised deck to three people and ask "what is this game supposed to feel like?" before anything else.
2. **F3: Replace jump scares with *sad* consequences.** When crops wither, the garden dims and the spirit who wanted those flowers grows quiet or restless. Keep spookiness as ambience, such as whispers and flowers that change shape in the dark. Why: failure should deepen the bond with the spirit, not shock the player. Expected effect: neglect feels regrettable, not frightening. Check: in the tone test below, watch for flinching versus "aww".
3. **F2: Keep chiptune as the instrument palette if it's part of the game's identity, but drop "upbeat".** Use slower, minor-key music-box chiptune for the night, and save the bright cues for dawn farewells. Why: the music currently undercuts both the eerie and the melancholy notes. Expected effect: the art and music agree. Check: an A/B audio test on the same footage (next step 2).
4. **F5: Make flowers the way wishes are granted.** Each spirit needs a specific bloom tied to its memory. End each in-game night at dawn with a farewell, and have each departed spirit leave a perennial behind. Why: this puts the theme's verb into the core loop and gives every session a peak. Expected effect: farming *is* helping spirits, and the garden at hour ten visibly holds the story of the hours before it. Check: the paper prototype (next step 3).
5. **F4: Cut daily login rewards and countdown timers.** Why: they fight the theme and apply pressure the audience will notice. Give players reasons to return through content instead: an unfinished spirit story, or a bloom about to open. Expected effect: the game returns to the cozy promise. Check: none needed; this is a design decision.
6. **F6: Lead the pitch with the garden-as-memorial, not with wish-granting.** Check: viewers stop naming comparable games first.

## Next steps
1. **Revise the deck (designer, this week).** Add the tone guide as slide 2. Replace any jump-scare or login slides with a three-panel storyboard of one spirit's arc, from wish to bloom to dawn farewell.
2. **Tone test (art and audio, about one week).** Make a 60-second animatic of the dawn farewell, cut once with the current upbeat chiptune and once with a slower minor-key version. Show it to 5 to 8 target-audience strangers, not the team, and ask "what did you feel?" before anything else.
   - Continue if most of them name a warm or sad feeling without prompting.
   - If they still say "cute" to both versions, the problem goes deeper than audio. Revisit the art direction or the strength of the moment itself.
3. **Paper prototype of one spirit arc (designer, about 2 hours).** Play the wish → specific flower → farewell arc, with a facilitator acting as the spirit. The question to answer: do players care whether the flowers succeed *before* they know what reward they'll get? If they only care about the reward, the emotional loop isn't working yet, and the wish system needs another pass before production.

I can turn this into a page you can share with your team if that would help.
