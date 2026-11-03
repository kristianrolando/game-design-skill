# Example: prototyping plan for "Echo Rooms" in Claude Code

## Trial record

- **Date:** 2026-11-03.
- **Host and model:** Claude Code CLI 2.1.287 in print mode (`claude -p`), model `claude-opus-5-5`, signed in with a claude.ai account.
- **Setup:** a disposable folder outside this repository containing only a copy of `skills/game-design-skill` at `.claude/skills/game-design-skill/`. Allowed tools: Read, Skill, Glob. Three lens trials ran in parallel in separate folders.
- **Invocation:** `/game-design-skill`. The prompt describes symptoms and does not name a lens, so lens choice is the router's.
- **Files read after the skill loaded:** `references/prototyping.md`, `references/scoping-budget.md`, `references/core-loop-pillars.md`. The run took 4 turns and about 127 seconds.
- **Output:** the final result, reproduced unedited. Its closing offer to make a shareable page comes from the host environment, not from the skill text.
- **Limits:** one run of one model. The concept and any figures in it were written for the trial; findings are design reasoning, not evidence about real players.

### Input given to the agent

> /game-design-skill We go into production in four months. What should we prototype first, and how do we know when to stop?
>
> Echo Rooms: a VR puzzle game for Meta Quest, for puzzle fans who own a headset. Team of 3. Players record short phrases with their own voice and replay them to trigger doors, shatter glass and calm creatures. So far we only have a tech demo that records and plays back audio. Untested ideas: players will be comfortable speaking aloud at home, voice recognition can tell phrases apart, 40 hand-built rooms, and an online co-op mode where two players combine voices.

### Reviewer notes

- First trial of the prototyping lens. It built the ranked uncertainty map (belief, group, impact, uncertainty, test) that the lens's reporting notes require, including blind spots the user had not listed.
- Every prototype brief has a question, type, players, signals and a kill result, and the plan ends with go/no-go criteria for production.
- It used the "options when stuck" checks to lay out five listening methods before recommending one.
- The request asked for a plan, so the `Deliverable` section fits the router rule here.

---

# Game design review: Echo Rooms, what to prototype first and when to stop

**Context:** VR puzzle · Meta Quest, voice plus hands or controllers · puzzle fans who own a headset · late concept, 4 months before production · reviewed a one-paragraph concept and a tech demo that records and plays back audio
**Assumptions:** (1) At least one of the three of you is a programmer who can build for Quest, and nobody works full-time on QA. (2) "Production" means you start building content at scale, so these 4 months are the last cheap chance to change the core. (3) No publisher or funder requires co-op. If #3 is wrong, tell me, because it changes the co-op advice.
**Lenses:** Prototyping, because it is the main question. Core loop, because the puzzle itself isn't defined yet and the puzzle decides what the voice tech has to do. Scoping, because 40 rooms and online co-op are a lot for 3 people. I skipped the Multiplayer lens since I recommend postponing co-op, and FTUE since onboarding is premature before the loop exists.

## Summary
Echo Rooms has a hook nobody else has: your own voice is the tool. The tech demo proves the cheap part (recording and playback). It doesn't test any of the four ideas the game depends on. The biggest problem is that the concept describes an input, not a puzzle. If you record a phrase, replay it and the door opens, that is a password. Also, the most expensive technical risk (voice recognition) depends on a design choice you haven't made yet: what the game actually listens for. My verdict: first, prototype the puzzle rules and whether people will talk at home, with a teammate faking the recognition by hand. Test recognition in parallel, but only for what the design turns out to need. Postpone co-op, and don't commit to 40 rooms until you've timed how long one takes to build.

## Deliverable: four-month prototype plan

### Uncertainty map (ranked by impact × uncertainty)

| # | Belief | Group | Impact if wrong | Uncertainty | Test |
| --- | --- | --- | --- | --- | --- |
| 1 | Recording and replaying creates puzzles that need thought, not just a password | Blind spot | Very high: there is no game | High | P1 |
| 2 | Players are comfortable speaking aloud at home | Untested belief | Very high: players avoid the core input | High | P1, P3 |
| 3 | Voice recognition can tell phrases apart | Untested belief | High, but how high depends on #1 | High | P2 |
| 4 | 40 hand-built rooms fit a team of 3 | Untested belief | High: the schedule | Medium | P4 |
| 5 | Online co-op where two players combine voices | Untested belief | Low for the core idea, high for cost | High | Postpone |
| 6 | Unexamined risks: game audio leaking into the mic, storing voice recordings, players who can't or won't speak | Blind spot | Medium to high | Medium | Fold into P2 and P3 |

#1 ranks above #3 because the puzzle design decides what recognition must do. It may not need to understand words at all.

### First decision (week 1, on paper): what does the game listen for?
1. **Words** (speech-to-text): the most magical option and the most expensive. Accents, languages, kids' voices and processing delay all need handling.
2. **Sound qualities** (pitch, loudness, length, rhythm): cheaper, works in any language, and allows humming, whistling or clapping, which helps both comfort and accessibility.
3. **A match with your own earlier recording** ("the door remembers what you said"): medium cost.
4. **No recognition**: what you say doesn't matter. The puzzle is where, when and how you replay it: echoes off walls, timing, layering several clips, playing them reversed or slowed.
5. **A mix** of options 4 and 2, with words used only for flavor.

I recommend prototyping options 4 and 2 first. They are cheap, and you only need option 1 if playtesters show they want the words to matter. (Inferred)

### Prototype briefs

**P1: Puzzle rules, with recognition faked** (weeks 1–5)
- **Question:** Do puzzle fans treat record-and-replay rooms as puzzles? Do they form a guess, fail, and then get an "aha"?
- **Type:** Greybox rooms built on the existing tech demo. A teammate at a laptop triggers the door, glass or creature by hand whenever a replay meets the room's rule.
- **Players:** The team for two weeks of iteration, then 5–8 strangers who own a Quest and like puzzle games.
- **Signals:** Number of failed tries before solving; solving without hints; whether players can explain the solution afterward; which room they want more of.
- **Continue if:** at least 3 of 5 room types get solved after a failed try, and testers can explain why it worked.
- **Change if:** solves happen on the first try (a password) or come from random flailing.
- **Kill result:** after two rounds of iteration, no room type is more interesting than "say the right word". Rethink the hook before production.

**P2: Recognition test** (weeks 2–6, one programmer)
- **Question:** Can the listening method chosen in week 1 classify a player's recording correctly on Quest hardware, fast enough to feel instant?
- **Players:** Recordings from 10 or more varied voices (ages, accents, quiet speakers), made in rooms with normal household noise.
- **Signals:** How often it confuses the categories the rooms need; delay between the end of a recording and the result; false triggers from the game's own audio.
- **Kill result:** agree an error limit before you start. As a starting point, a wrong result more often than about 1 in 20 tries will probably feel unfair. If the method misses that limit, fall back to a simpler listening method.
- **Design note:** analyze each clip once, when it's recorded, and show the player what the game heard, for example a symbol on the recording. Misrecognition then becomes visible feedback the player can fix, and the mic never has to tell the player's voice apart from the game's playback.

**P3: Speaking at home** (weeks 6–9)
- **Question:** Will players make the sounds the puzzles need, in their own homes, with other people around?
- **Type:** Sideload the P1 build to 4–6 testers who play at home.
- **Signals:** Whether they whisper, hesitate, or take the headset off to check who's nearby. Afterward, ask: "Would you play this with someone in the next room?"
- **Change if:** testers whisper. Then design for quiet input, accept non-speech sounds, and drop any puzzle that requires loudness. Note that "shatter glass" implies shouting, so this test can directly contradict a mechanic.
- **Kill result:** most testers avoid making sound even when quiet options exist.

**P4: Cost of one room** (weeks 9–14)
- **Question:** How long does one room take, from greybox to shippable?
- **Type:** Take one passing P1 room to final quality, and record the time spent on each discipline.
- **Decision:** number of rooms = available production person-weeks ÷ measured cost per room, with 20–30% held back as buffer.
- **Illustration only:** if a finished room takes 1.5–3 person-weeks, 40 rooms is 60–120 person-weeks. That's roughly 5–10 months of all three of you doing nothing but rooms.

**Weeks 15–16:** hold the go/no-go decision, write the production plan, and keep the rest as buffer.

### How you know when to stop
1. **A prototype stops when it answers its question, not when it looks good.** When the timebox ends, choose continue, change or stop, even if the result is unclear. An unclear result means the question was vague: rewrite the question instead of building more.
2. **Write down the kill results before you build anything,** so sunk cost doesn't make the decision for you later.
3. **Warning signs of prototype creep:** adding final art, menus, a save system or a second mechanic before P1 passes.
4. **Go into production only if, at week 16:**
   - P1 passed with strangers.
   - P2 met the error and delay limits you agreed, or the design no longer needs recognition.
   - P3 testers made the sounds the puzzles require.
   - The room count comes from P4's measured cost.
   - Co-op is on the cut list with a date to revisit it.

## Findings by lens

### Core loop
- **F1 · The concept has no puzzle yet** (Inferred): the concept lists effects (doors, glass, creatures) but no limit or rule that makes the player think. Evidence: "replay them to trigger doors, shatter glass and calm creatures." Player impact: if a replay works like a key, rooms are solved on the first try and 40 rooms repeat the same action.
- **F2 · What the game listens for is undefined** (Inferred): "voice recognition can tell phrases apart" assumes the words matter. Player impact: if recognition is word-based and wrong, players will feel "I said it right!", which is the most damaging kind of unfairness in a puzzle game.

### Prototyping
- **F3 · The demo only proves the safe part** (Observed): record and playback works. All four ideas the game depends on are labeled untested. Player impact: none yet, but nothing about the core experience has been checked.
- **F4 · Speaking at home is untested, and it clashes with loud mechanics** (Assumed): many Quest owners play in shared living spaces. Glass shattering suggests loud input. Player impact: players whisper, the loud puzzles fail, or players stop playing when someone else is home.
- **F5 · Unexamined risks** (Inferred): Quest allows younger players on parent-managed accounts, and the game records their voices. Some players can't speak or hear. Game audio may leak into the mic. Player impact: privacy problems, players excluded, and false triggers.

### Scoping
- **F6 · "40 rooms" is a number, not an estimate** (Observed): nothing has been timed. Player impact: rushed late rooms, or a missed date.
- **F7 · Online co-op is the biggest cost the core idea doesn't need** (Inferred): it means networked voice and designing puzzles twice (every co-op room needs a two-voice solution). It also needs enough players online to find a partner in a niche audience, and moderation duties once strangers hear each other's voices. Player impact: months taken away from the solo experience.

## Priority issues

| ID | Issue | Lens | Severity | Confidence | Effort |
| --- | --- | --- | --- | --- | --- |
| F1 | Record and replay is not yet a puzzle | Core loop | P1 | Inferred | M |
| F2 | Listening method undefined; misrecognition feels unfair | Core loop | P1 | Inferred | S to decide, M to test |
| F4 | Speaking aloud at home untested; clashes with loud mechanics | Prototyping | P1 | Assumed | S |
| F7 | Online co-op is a large cost the core doesn't need | Scoping | P2 | Inferred | S (to cut) |
| F6 | Room count has no estimate behind it | Scoping | P2 | Observed | M |
| F5 | Voice privacy, accessibility, mic leakage | Prototyping | P2 | Inferred | S |
| F3 | Demo tests none of the core ideas | Prototyping | P2 | Observed | Covered by P1–P3 |

## Minimal-fix recommendations
1. **F1: build 5 greybox rooms with recognition faked by a teammate (P1).** Why: it tests the puzzle without building any recognition. Expected effect: you learn within 5 weeks whether the hook makes puzzles. Check: stranger solves happen after a failed try, and testers can explain them.
2. **F2: pick the listening method on paper in week 1, analyze each clip when it's recorded, and show what was heard.** Why: the tech should follow the design, not the other way round. Expected effect: errors are visible and fixable instead of mysterious. Check: P2 error rate and delay.
3. **F4: accept quiet and non-speech sounds, and add no loudness-gated puzzles until P3 passes.** Why: protects the core input from embarrassment at home. Check: P3 observations.
4. **F7: put co-op on a written cut list and revisit it after the solo game ships.** Why: it removes the largest scope driver. Expected effect: frees months of time for the core. Check: the production plan no longer depends on networking.
5. **F6: replace "40" with the P4 formula.** Check: the week-16 plan shows a room count, cost per room and buffer.
6. **F5: keep recordings on the device, and add an input option for players who can't use their voice.** Check: a short privacy and accessibility review at the week-16 decision.

## Next steps
1. **This week (whole team, 1 hour):** choose the listening method for each room type, then write and sign the four prototype briefs with their kill results.
2. **Weeks 1–2:** the designer builds 5 greybox rooms on the tech demo with a teammate triggering by hand. The programmer starts the P2 recognition test.
3. **Now:** start recruiting 5–8 stranger puzzle fans who own a Quest for weeks 4–5. Recruiting takes longer than building.
