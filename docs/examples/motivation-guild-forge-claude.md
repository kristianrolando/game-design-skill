# Example: player motivation review of "Guild Forge" in Claude Code

## Trial record

- **Date:** 2026-11-03.
- **Host and model:** Claude Code CLI 2.1.287 in print mode (`claude -p`), model `claude-opus-5-5`, signed in with a claude.ai account.
- **Setup:** a disposable folder outside this repository containing only a copy of `skills/game-design-skill` at `.claude/skills/game-design-skill/`. Allowed tools: Read, Skill, Glob. Three lens trials ran in parallel in separate folders.
- **Invocation:** `/game-design-skill`. The prompt describes symptoms and does not name a lens, so lens choice is the router's.
- **Files read after the skill loaded:** `references/motivation.md`, `references/core-loop-pillars.md`, `references/flow-fairness-failure.md`. The run took 4 turns and about 71 seconds.
- **Output:** the final result, reproduced unedited. Its closing offer to make a shareable page comes from the host environment, not from the skill text.
- **Limits:** one run of one model. The concept and any figures in it were written for the trial; findings are design reasoning, not evidence about real players.

### Input given to the agent

> /game-design-skill Why do players ignore our crafting feature, and who is this game really for?
>
> Guild Forge: a free-to-play mobile RPG (portrait, touch) in live operation for 8 months. Players form 5-person guilds and fight weekly raid bosses. Analytics: only 8% of daily players use crafting. Crafting takes six menu screens and is first offered on the defeat screen after a lost raid. Crafted gear is slightly weaker than raid drops. Daily quests require crafting 3 items for 50 gems. Player survey quotes: "crafting is just a chore for the daily", "I only open it for gems". Our marketing says the game is "for everyone".

### Reviewer notes

- First trial of the player motivation lens. It diagnosed adoption through motivation, ability and prompt before suggesting rewards, and wrote a persona and anti-persona derived from what the design rewards.
- It warned against the reward-crutch fix (raising the gem payout) without being asked.
- It named a tension between lenses (crafting as a solo path versus feeding the guild core) and chose with a reason.
- All findings are P2, with an explicit statement that nothing reaches P1; the next steps start with analytics that would confirm or refute the key inference.

---

# Game design review: Guild Forge crafting adoption and target player

**Context:** F2P mobile RPG · portrait, touch · claimed audience "for everyone" · live for 8 months · reviewed your brief: analytics (8% crafting use), the crafting flow (six screens), where crafting is first offered, gear power, the daily quest, and two survey quotes
**Assumptions:** (A1) Gems are the premium currency. (A2) Raid drops are random in slot and stats. (A3) The "craft 3 items" daily is one of several dailies and players can skip it. (A4) Crafting has no link to guilds.
**Lenses:** *Player motivation* is the main lens because the question is about whether players adopt a feature and who the game is for. *Core loop and pillars* checks whether crafting has a job in the loop. *Flow, fairness and failure* covers the defeat-screen offer. I skipped *Multiplayer and social*: guild dynamics shape the target player, but there's no social data. I also skipped *FTUE and retention*: I cover the daily quest under reward quality.

## Summary
The game's core is a weekly 5-person guild raid, and that's what it rewards. Crafting has no job in that loop. Its gear is weaker than raid drops. It takes six screens. Players first see it right after losing a raid. The only reason to use it is a gem bribe, and players describe it in exactly those terms. Even the bribe doesn't work: 92% of daily players skip a gem reward rather than go through the flow. Nothing here is P1, because the raid core doesn't depend on crafting. But crafting is currently teaching players that it's a chore. On who the game is for: it's built for a committed guild raider, not "everyone", and the claim should change or the design should.

## Findings by lens

### Player motivation
- **F1 · Motivation, ability and prompt are all missing** (Observed): A behavior happens when there's a reason, it's easy enough, and something prompts it at the right moment (Fogg's model). Crafting fails all three. *Reason:* "crafted gear is slightly weaker than raid drops". *Ease:* six menu screens. *Prompt:* first offered "on the defeat screen after a lost raid". Evidence: your brief. Player impact: no group of players has a reason to try crafting, so the 8% isn't a tuning problem. A bigger reward can't fix a feature that's missing all three.
- **F2 · The daily quest turns crafting into a chore** (Observed): "Craft 3 items for 50 gems" is a reward that controls ("do this, get paid") rather than one that tells players they got better. The survey quotes say this outright: "just a chore for the daily", "I only open it for gems". This kind of reward wears down interest over time. Here it does worse: it's the first thing that defines crafting for most players. Evidence: daily quest rule, survey. Player impact: the people who do craft are probably doing it reluctantly, and their word of mouth will be negative.
- **F3 · Even 50 gems doesn't beat six screens** (Inferred, depends on A1 and A3): If a premium-currency reward is on offer and 92% of daily players still don't craft, the effort is costing them more than the gems are worth. This also suggests the 8% is mostly people clearing the daily rather than people who want to craft. Evidence: the 8% figure next to the daily quest rule. Player impact: the real number of players who craft by choice may be close to zero. That's testable (see Next steps).
- **F4 · "For everyone" doesn't match what the game rewards** (Inferred): The design rewards players who show up on a weekly schedule, coordinate with four others, and accept a group loss. That's a socially committed raider. **Anti-persona:** a solo or irregular player, or someone who likes making things. They leave when their guild stalls or a raid is lost, and that's exactly the moment crafting is offered to them. Weaker crafted gear tells them the game's main power path isn't for them. Evidence: 5-person guilds, weekly bosses, crafted gear weaker than drops. Player impact: marketing brings in players the game will drop, and every feature tries to please types it can't serve.

### Core loop and pillars
- **F5 · Crafting is an orphan feature** (Inferred): The extracted loop is **form/join a guild → raid → loot drops → equip → raid next week**. Crafting connects only to the gem economy: **craft → gems**. Its output (gear) is beaten by raid drops, so it strengthens no step of the core loop. A support loop that doesn't feed the core will lose players' time to it. Evidence: gear power comparison, quest reward. Player impact: experienced players can see that crafting doesn't matter, and that's what they're telling you.

### Flow, fairness and failure
- **F6 · The defeat screen is the worst place to introduce crafting** (Inferred): Right after a loss, players are frustrated, often about to leave, and possibly blaming teammates. Offering gear there tells them "your gear caused this". The gear on offer can't fix it, though, because it's weaker than what raids drop. Six screens on top of a loss is stacked friction. Evidence: where crafting is first offered. Player impact: the first impression links crafting to failure and to a fix that doesn't work. The screen should also be teaching why the raid was lost, and the crafting offer takes that space.

**Tension between lenses:** The motivation lens suggests crafting could be the path for solo players the game currently neglects. The core-loop lens says support systems should feed the core, which is the guild raid. I'd go with the core loop. If crafting becomes a separate solo track, it competes with raids and splits the audience. If it helps the guild raid, it fits the player the game is actually built for.

**Ethics:** I didn't see any clearly manipulative patterns. One risk to watch: if the planned fix for adoption is a bigger gem payout, that's a reward crutch, paying players to do something that isn't worth doing. It would also make premium currency depend on a daily chore.

## Priority issues
| ID | Issue | Lens | Severity | Confidence | Effort |
| --- | --- | --- | --- | --- | --- |
| F1/F5 | Crafting has no job; its output is beaten by raid drops | Motivation, Core loop | P2 | Inferred | M |
| F6 | First offered on the defeat screen | Motivation, Flow | P2 | Inferred | S |
| F2 | The daily quest makes crafting a chore | Motivation | P2 | Observed | S |
| F3 | The six-screen flow costs more than a 50-gem reward is worth | Motivation, Flow | P2 | Inferred | M |
| F4 | The "for everyone" claim doesn't match the guild-raider design | Motivation | P2 | Inferred | S (doc) / L (product) |

## Minimal-fix recommendations
1. **F1/F5: Give crafting one job that raid drops can't do, or cut it down to a simple sink.** A job that fits the raid player: **targeted crafting**. The player picks the slot or stat they're missing (depends on A2) and crafts for themselves or a guildmate. Raid drops stay the power ceiling. Why: this ties crafting into the gear-up step and the guild (relatedness) without competing with drops on raw power. Expected effect: crafting becomes "how I prepare for next week's boss". Check: the equip rate of crafted items, and how often players craft beyond the daily's 3.
2. **F6: Move the first offer to a calm, high-motivation moment.** For example, the hub after a win, or when the player has materials and a clear gear gap. Use the defeat screen to show why the raid was lost. Why: it fixes the bad timing. Expected effect: a better first impression and more players willing to try it. Check: A/B the placement and compare the share of first crafts that weren't for the daily.
3. **F3: Cut the flow to two screens (choose → confirm) and add batch crafting.** Why: ease is what blocks 92% of players. Expected effect: crafting stops feeling like a chore even before it has a better job. Check: instrument drop-off on each of the six screens first, so you know which ones to merge.
4. **F2: Once fix 1 is in, change the daily to "craft one item for your weakest slot", and don't raise the gems.** Why: the reward then points to a real improvement instead of paying for compliance. Check: survey sentiment and how many players keep crafting after the daily is done.
5. **F4: Write down the persona and anti-persona, and update the positioning to match.** For example: "for players who want a weekly co-op ritual with four friends." Why: it gives the team a rule for what to keep and cut. Expected effect: less wasted acquisition, and fewer features trying to please everyone.

## Next steps
1. **Analytics (this week):** Of the 8%, what share craft exactly 3 items a day? Also pull the funnel for each of the six screens and the equip rate of crafted gear. This confirms or refutes F3 and shows what voluntary crafting really looks like.
2. **Design lead (before the next content update):** Decide whether crafting gets a job (fix 1) or gets cut down to a lightweight sink. Run that decision against the written persona from fix 5.
3. **Live test:** A/B the shortened flow plus the new offer placement against the current version. Measure voluntary crafting (crafts beyond the daily's 3), not total crafting, since total crafting includes the gem bribe.

If you want to share this with the team, I can turn it into a page.
