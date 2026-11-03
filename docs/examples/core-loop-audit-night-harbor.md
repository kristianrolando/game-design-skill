# Example: core loop audit of "Night Harbor"

## Trial record

- **Date:** 2026-11-03.
- **How it was produced:** a fresh agent (Claude Opus 5.5, run as a Claude Code subagent with no context from the authoring conversation) was told the skill was installed at `skills/game-design-skill/`. It was instructed to read `SKILL.md`, follow it, and load reference files only where the router directed. It was not allowed to read the README, tests or docs, or to write files.
- **Files the agent reported reading, in order:** `SKILL.md`, `references/core-loop-pillars.md`, `references/flow-fairness-failure.md`, `references/ftue-retention.md`.
- **Output:** reproduced below unedited, apart from removing the agent's trailing file list (shown above).
- **Limits:** this tests the skill text with explicit file reads, not native skill discovery or plugin loading in any host. It is one run of one model. The concept was written for the trial, and its findings are design reasoning, not playtest evidence. The user context was complete, so the intake-question branch was not exercised here; see the intake check below.

### Input given to the agent

> Use the game design skill to audit the core loop of my concept. What's the actual loop, where is it weak, and what should I fix first?
>
> Night Harbor: a cozy mobile fishing game (iOS and Android, portrait, one thumb). Target players: adults 25-40 who play cozy games in 5-10 minute breaks. Stage: concept, nothing built yet. I'm a solo developer.
>
> You run a small harbor lighthouse at night. Each night you pick a fishing spot on a map, sail there (a 30-second boat ride; a later upgrade makes it skippable), then cast your line: a timing mini-game where you tap when the bobber dips. Caught fish go into a cooler with 8 slots. When it's full you sail back to the dock and sell fish at the market for coins; prices change daily. Coins buy boat upgrades (faster travel, bigger cooler), new rods and bait. You can also buy furniture to decorate the lighthouse. There's a collection book with 60 species, and daily quests like "catch 5 mackerel". An energy bar gives 5 casts; it refills 1 cast every 20 minutes and refills can be bought. Legendary fish appear with a 1% chance per cast. The lighthouse keeper's story of her lost brother is told through letters, one unlocked every 10 species collected.

### Reviewer notes

- The report follows the skill's template: context, assumptions and lenses, then Summary, Findings by lens, Priority issues, Minimal-fix recommendations and Next steps.
- Lens choice matches the router's rules: three lenses for a standard review, starting with structure. Skipped lenses are named with reasons.
- Every finding carries a confidence label, and assumptions (A1 to A6) are listed and referenced.
- The skill's ethics rule fired without being asked: F1 flags paid refills that sell relief from designed friction.
- The arithmetic in F7 is correct (0.99^100 ≈ 0.366).

### Intake check

A second fresh agent run on the same date, under the same rules, received a request with almost no context: "Is the core loop of my game any good? You fight monsters, get loot, and upgrade your gear." It read only `SKILL.md`. Instead of analyzing, it asked three questions in one message, covering genre and platform, the choices inside the loop, and the production stage. Each question had a default and the option to reply "defaults are fine". This matches the intake rule. Its reply is summarized here rather than reproduced.

---

# Game design review: Night Harbor (core loop audit)

**Context:** Cozy fishing · iOS/Android, portrait, one thumb · adults 25-40 playing in 5-10 minute breaks · concept (nothing built) · solo developer · material reviewed: the concept summary in your message
**Assumptions:**
- A1: A missed cast (tapping at the wrong time) still uses one energy.
- A2: You can only sail home when the cooler is full, as written ("When it's full you sail back").
- A3: A cast takes about 10-20 seconds from cast to bite.
- A4: The game is free-to-play, since refills can be bought.
- A5: Spot choice decides which species can bite. The concept implies this but doesn't say it.
- A6: Some of the 60 species are legendary (1%) fish.

**Lenses:**
- Applied: **Core loop and pillars**, because it's the question you asked. **Flow, fairness and failure**, because energy, missed casts and the 1% odds decide whether the loop feels fair. **FTUE and retention**, because the 5-10 minute session and the paid refills decide whether the loop fits your players.
- Skipped: Emotional direction (the cozy fantasy reads clearly and isn't in question), Prototyping and Scoping (they show up only as next steps), Motivation and Multiplayer (not relevant yet).

## Summary
Night Harbor is a cozy collection fishing game. A one-tap timing cast feeds a sell-and-upgrade economy, a 60-species book and a story told in letters. Its strongest asset is the link between collection and story: every 10 species unlocks a letter about the lost brother. That gives players a reason to return out of curiosity rather than obligation, which is the right kind of hook for this audience. The biggest problem is that the numbers stop the loop from finishing. Energy gives 5 casts but the cooler holds 8, so a player can't complete one trip (cast, fill, sell, upgrade) without waiting about an hour or paying. That turns the energy bar into friction you then sell relief from. Around that sit a 60-second round trip of dead travel and a cast mini-game with nothing yet that changes from cast 1 to cast 50. Verdict: the parts are promising, but the loop is broken as written. Fix the energy and cooler mismatch on paper first, then prototype the cast on its own before building any meta.

## Findings by lens

### Core loop and pillars

**The loop as written, at three time scales** (✗ = broken step, ☐ = dead step that changes nothing):

- **Seconds:** cast → wait → bobber dips → tap → catch or miss → cast again *(only if energy remains)*
- **Minutes (one trip):** pick spot → ☐ sail 30 s → cast ×8 to fill the cooler ✗ *(only 5 energy)* → ☐ sail back 30 s → sell (prices change daily) → buy upgrades, rods, bait or furniture → pick spot
- **Day or session:** daily quests and daily prices refresh → energy refills (1 cast every 20 min) → every 10 new species unlocks a letter → legendary fish at 1% per cast

The loop you described and the loop the numbers allow are different. The numbers allow: sail, 5 casts, wait or pay, 3 more casts, sail back, sell.

- **F1 · A trip can't finish on free energy** (Inferred, from your numbers)
  - What happens: energy is 5 casts, the cooler is 8 slots, and you sail back when the cooler is full. Filling it needs 3 more casts, which is at least 60 more minutes of regen, plus 20 minutes per missed cast under A1. The payoff step (sell, then upgrade) sits behind a timer or a purchase on every single trip. The "bigger cooler" upgrade makes this worse: progress lengthens the wait.
  - Evidence: "energy bar gives 5 casts; refills 1 cast every 20 minutes and refills can be bought"; "cooler with 8 slots. When it's full you sail back."
  - Player impact: a player on a 5-10 minute break usually can't reach the satisfying end of a cycle. The break ends mid-task, stranded at sea with a half-full cooler.
  - Ethics flag: this is friction created by the design and sold back to the player through paid refills. For an adult cozy audience it also undercuts the core promise of the game.

- **F2 · The boat ride is a dead step, and removing it is sold as progress** (Inferred)
  - What happens: the round trip is 60 seconds of watching the boat. Under A3, the 5 casts are roughly 1-2 minutes of real play, so a third to half of each trip is passive travel.
  - Evidence: "a 30-second boat ride; a later upgrade makes it skippable."
  - Player impact: the early sessions, which shape a player's first impression, carry the most dead time.
  - Note: because the upgrade costs coins rather than money, this is a pacing problem, not an ethics one.

- **F3 · The cast loop has no stated variety, so the meta is carrying the core** (Inferred)
  - What happens: "tap when the bobber dips" tests one skill. Nothing in the concept says fish bite differently, or that rods or bait change the cast itself. Run the self-standing check (remove coins, collection and story, and ask whether casting is still pleasant): as written, the answer is probably no.
  - Evidence: the cast description. Rods and bait are listed only as purchases.
  - Player impact: cast 50 feels like cast 1. Rewards have to do all the motivating, which fails once upgrades slow down.
  - What works: fast, forgiving timing suits one thumb, portrait play and short breaks. The mode is right; the content is thin.

- **F4 · Two decision points are non-decisions, and furniture is an orphan** (Inferred)
  - Daily prices only matter if you can choose when to sell. An 8-slot cooler that has to be emptied to keep fishing forces a sale at whatever today's price is.
  - Spot choice is only meaningful if the map tells you something about what lives where (A5), and the concept doesn't say it does.
  - Furniture spends coins but feeds no step of the loop. Nothing in the lighthouse affects or reflects fishing.
  - Evidence: the market, map and furniture lines.
  - Player impact: the loop's few choices feel empty, and for a solo developer, furniture is effort spent away from the core.

- **F5 · No pillars, so the conflicts go unresolved** (Observed: none are stated)
  - Implied pillars: "cozy and pressure-free", "fits a 5-10 minute break", "collect and uncover the story".
  - F1 and F2 break the first two of these. Without a rule like "we choose a complete trip per break, even when it costs monetization pressure", the conflict will come back with every new feature.

### Flow, fairness and failure

- **F6 · A missed tap costs 20 minutes** (Assumed: A1)
  - What happens: with only 5 casts, one timing miss burns a fifth of the session's play and 20 minutes of real time.
  - Player impact: in a cozy game, players will read this as punishment, not practice. The failure loop teaches little ("tap earlier") and costs a lot.
  - Evidence: the energy rules together with the timing mini-game.

- **F7 · Legendary droughts, with the story possibly behind them** (Inferred; story gating Assumed: A6)
  - The odds: at 1% per cast, the expected wait is 100 casts, and about 37% of players will have no legendary after 100 casts (0.99^100 ≈ 0.37).
  - The wait in days: at 3-4 breaks of 5 casts each, that's roughly 5-7 days on average, with long, unprotected tails.
  - The story risk: if legendaries count toward the 60 species, the last letters, which are your strongest emotional payoff, depend on luck or paid energy.
  - Missing: odds display and bad-luck protection are not mentioned.
  - Evidence: "Legendary fish appear with a 1% chance per cast"; "one [letter] unlocked every 10 species collected."

### FTUE and retention

- **F8 · The story hook arrives late and slowly** (Inferred)
  - What happens: the first letter needs 10 species. At 5 casts per break, with some casts catching duplicates, that probably takes several sessions, and there are only 6 letters in the whole game.
  - Player impact: your healthiest return reason (curiosity about the brother) shows up after the point where many new players decide whether to keep the game.
  - Evidence: the letter cadence.

- **F9 · Return reasons lean on timers** (Inferred)
  - Healthy: letters (curiosity), the collection book (the player's own plans), daily prices (mild anticipation).
  - Pressure: the energy refill timer and the daily quests (obligation).
  - What's missing: no stated plan for a player who returns after two weeks.
  - Player impact: the energy refill timer is currently the loudest "come back" signal, and it's the least cozy one.

## Priority issues

| ID | Issue | Lens | Severity | Confidence | Effort |
| --- | --- | --- | --- | --- | --- |
| F1 | Energy (5) is smaller than the cooler (8): a trip can't finish without waiting or paying; paid refills monetize that friction | Core loop / Retention | P1 | Inferred | S |
| F6 | A missed tap burns scarce energy | Flow and fairness | P2 | Assumed | S |
| F3 | The cast loop has no variety and wouldn't hold up without the meta | Core loop | P2 | Inferred | M |
| F2 | 60 s round trip of dead travel per trip, early game hit hardest | Core loop | P2 | Inferred | S |
| F7 | 1% legendary with no protection; the story may be gated behind it | Flow and fairness | P2 | Inferred / Assumed | S |
| F8 | First letter arrives too late to hook new players | FTUE | P2 | Inferred | S |
| F4 | Daily prices and spot choice aren't real decisions; furniture is an orphan | Core loop | P2 | Inferred | S (cut) to M (connect) |
| F5 | No pillars to settle the cozy-versus-energy conflict | Pillars | P3 | Observed | S |

## Minimal-fix recommendations

1. **F1: Make one energy unit buy one whole trip, not one cast.**
   - The change: call it lantern oil, which fits the night harbor. One charge lets you sail out and fish until the cooler is full. Remove the per-cast energy cost, and let the player sail home early whenever they like.
   - Sizing: size the cooler so one trip fits a 3-6 minute break.
   - Monetization: if you do monetize, sell cosmetics or a one-time premium unlock, not refills.
   - Why: it lines up energy, cooler and session length, so every break ends on the sell-and-upgrade payoff.
   - Expected effect: every session reaches a natural, satisfying stopping point. "Bigger cooler" then means a longer trip, not a longer wait.
   - Check: on paper, run 10 simulated breaks of 5-10 minutes each. Every one should end at the dock.
2. **F6: Missed casts are free.** The fish just swims off. Keep the timing window generous for the first species.
   - Why: it removes a punishment that doesn't fit a cozy game.
   - Expected effect: misses read as "almost had it", not "lost 20 minutes".
   - Check: in the prototype, watch whether players flinch or say "ugh" after a miss.
3. **F3: Give each species a distinct bite pattern.** For example: one quick dip, a double nibble then the real bite, or a slow drag. Show the species' silhouette or ripple before the bite so the player can read it.
   - Why: it adds one source of variety that also feeds the collection book, because learning a fish means learning its bite.
   - Expected effect: cast 50 asks for different reading than cast 1.
   - Check: in a no-rewards prototype, see whether players keep casting voluntarily past 20 casts.
4. **F2: Cut the ride to a 3-5 second animation from day one.** Alternatively, make the ride a moment of light play, such as spotting fish shadows to choose where to drop anchor. Drop the skip upgrade.
   - Why: it removes the dead step instead of selling its removal.
   - Check: time a full trip and aim for under 10% of it being passive.
5. **F7 and F8: Show the legendary odds and add a pity counter.** For example, the chance grows with each cast without a legendary, guaranteeing one within 60-80 casts. Make the letters depend only on common species. Deliver the first letter in the first session (a letter waiting in the lighthouse, or one at 3 species), then space the rest out.
   - Why: it protects the story payoff from luck and brings the curiosity hook forward.
   - Check: simulate the casts-to-first-legendary distribution, and count how many minutes it takes to reach the first letter.
6. **F4: For v1, cut daily price changes and postpone furniture.** Or tie furniture to the loop, for example by displaying caught trophy fish and the letters in the lighthouse. For a solo developer, cutting is the stronger recommendation.
   - Why: it removes decisions that are really chores, and features that feed no step of the loop.
   - Check: every remaining feature should name the loop step it strengthens on a one-page loop map.

## Next steps

1. **Decide this week (you):** the energy model (per trip or none) and the business model (premium, or free-to-play without paid refills). Then rewrite the concept with the trip-based loop and two or three pillars written as trade-offs. Example: "Every break ends at the dock, even when that costs us monetization."
2. **Build a one-to-two-day greybox prototype (you):** only the cast mini-game, with 3 species bite patterns and no economy, story or upgrades. Have 5 people from your target group (cozy players aged 25-40) play during a real break. Note whether they keep casting past 20 casts without rewards, and how misses make them feel. This confirms or refutes F3 and F6. Nothing here has been playtested yet.
3. **Do the paper math after the prototype:** a one-page loop map at three time scales, the trip length, and simulations of the cooler size, energy, legendary pity and letter cadence. Do this before committing to the meta systems.
