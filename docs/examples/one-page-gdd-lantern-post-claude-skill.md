# Example: one-page design doc for "Lantern Post" in Claude Code

## Trial record

- **Date:** 2026-11-03.
- **Host and model:** Claude Code CLI 2.1.287 in print mode (`claude -p`), model `claude-opus-5-5`, signed in with a claude.ai account.
- **Setup:** a disposable folder outside this repository containing only a copy of `skills/game-design-skill` at `.claude/skills/game-design-skill/`. No plugin flag. Allowed tools: Read, Skill, Glob.
- **Invocation:** the direct skill slash command `/game-design-skill`. The session's init event listed the project skill `game-design-skill`.
- **Files read after the skill loaded:** `references/pitch-gdd.md`, `references/core-loop-pillars.md`, `references/scoping-budget.md`. The run took 4 turns and about 71 seconds.
- **Output:** the final result, reproduced unedited.
- **Limits:** one run of one model. The concept was written for the trial; findings are design reasoning, not playtest evidence.

### Input given to the agent

> /game-design-skill Turn these notes into a one-page design doc.
>
> Lantern Post: a cozy narrative delivery game for Nintendo Switch and PC (controller). For adults who like slow, story-rich games in 30-minute sessions. Stage: concept, solo developer, aiming for a vertical slice in 6 months. You are the night courier in a mountain village. Each night you pick 3-5 letters, plan a route on a hand-drawn map, walk or sled between houses, and choose whether to read letters before delivering. Reading changes how villagers react and unlocks small side stories. Weather changes routes. You upgrade your lantern to reach farther paths. Comparable games: A Short Hike, Spiritfarer.

### Reviewer notes

- First trial of develop mode and of the pitch and GDD and scoping lenses. The one-page document sits under Deliverable, as the router specifies, and follows the lens's section order.
- It marked its own additions as *(proposed)* so the designer can tell them apart from stated decisions.
- Pillars are written as trade-offs, and every key feature names the loop step or pillar it serves, as the lenses require.
- It reported the absence of manipulative patterns explicitly.
- The final sentence offering to publish a shareable page comes from the host environment, not from the skill text.

---

# Game design review: Lantern Post (one-page design doc)

**Context:** Cozy narrative delivery / light exploration · Switch and PC, controller-first · Adults who like slow, story-rich games in 30-minute sessions · Concept stage, solo developer · Reviewed: your concept notes (one paragraph)
**Assumptions:** (1) The doc is for you and a future publisher or collaborator. (2) One in-game night is one play session. (3) There's no fail state; the game is cozy. (4) The vertical slice targets PC first, with the Switch port after the slice. I've marked anything I proposed as *(proposed)* so you can tell it apart from what you decided.
**Lenses:** Pitch and GDD, because a one-pager is the deliverable. Core loop and pillars, because at concept stage the structure comes first. Scoping, because it's a solo developer with a 6-month slice. I skipped FTUE, retention and flow: they're too early before the loop is proven. Social and multiplayer don't apply.

## Summary
Lantern Post is a night-courier game where each session is one night of deliveries through a mountain village. Its best idea is the choice of whether to **read a letter before you deliver it**. It's a small private act with social effects, and none of your comparables has it. The biggest problem is that the notes give nothing a reason to cost something. There's no limit on route planning and no stated downside to reading. So the two decisions that define the game could become "always read" and "any route works". The concept fits a solo developer if the slice is one valley, about 6 villagers and 3 nights. Keep the narrative branching shallow.

## Deliverable

> ### Lantern Post
> **Logline:** As the night courier of a snowbound mountain village, you carry people's letters through the dark and decide whether their words stay private.
>
> **Genre / platform / player:** Cozy narrative delivery with light exploration · Switch and PC, controller-first · Adults who want a slow, story-rich game in 30-minute sessions
>
> **Player fantasy:** Being the quiet, trusted person who knows everyone's secrets, or chooses not to, and whose care holds the village together.
>
> **Core loop:**
> - *Night (session):* Sort the post → pick 3–5 letters → plan a route on the hand-drawn map → walk or sled to each house → **read or keep sealed** → deliver → the villager reacts → return at dawn → the village changes, a side story advances, lantern progress → next night
> - *Per delivery (minutes):* Travel → arrive → read? → hand over → reaction / new information / new path
> - *Moment to moment (seconds):* Move → the lantern reveals the path → spot a detail or shortcut
>
> **Pillars (each costs something):**
> 1. **Every letter is a person.** We choose fewer, deeper villagers over a bigger village.
> 2. **Choices without verdicts.** Reading changes outcomes but is never scored as good or bad. We accept weaker "right answer" feedback to get that.
> 3. **One night, one sitting.** A night ends in about 30 minutes. We cut anything that needs grinding across nights.
> 4. **Planning is gentle, walking is the reward.** Routes are short and easy to read. We reject optimization puzzles even when they would add depth.
>
> **Key features:**
> - **Read or seal** (the read step; pillars 1 and 2): reading shows what's in the letter and changes the villager's reaction. Keeping it sealed builds trust. *(Proposed: each path unlocks its own content, so neither choice is strictly better.)*
> - **Hand-drawn route map** (the plan step; pillar 4): you draw your route before leaving. *(Proposed: the night has a soft limit, such as lantern oil or dawn, so the order matters. Letters you don't deliver carry over to the next night; nothing fails.)*
> - **Weather** (adds variety between nights): snow, fog or ice opens and closes paths, so the same village plays differently from night to night.
> - **Walk or sled** (the travel step): sledding is the fast way down slopes and walking is the way up. It gives the travel step a small choice of its own.
> - **Side stories** (the reaction step; pillar 1): short arcs that letters and reading choices unlock.
>
> **Progression / meta:** Lantern upgrades reach farther paths, which opens new houses and letters. *(Open question: how you earn upgrades.)*
>
> **Art and audio:** A hand-drawn, warm-light-in-cold-dark look; the map's drawn style sets the art language. *(Proposed: lantern light as the main visual tool, sparse ambient audio with snow, wind and doors, and handwriting fonts for letters.)*
>
> **Comparables and difference:** *A Short Hike* (gentle traversal, a small handcrafted world) and *Spiritfarer* (cozy routines carrying emotional stories). **The difference:** the moral choice of reading private mail, and routes planned around weather.
>
> **Scope:** Solo developer · Vertical slice in 6 months: 1 valley, about 6 villagers, 3 nights, 2 weather states, 1 lantern upgrade.
>
> **Open questions and risks:**
> - What does reading cost, and can villagers tell?
> - What limits a night (time, oil, cold), if anything?
> - How are lantern upgrades earned?
> - Can one person write enough branching reactions?
> - Is sledding needed in the slice?
> - When does Switch porting start?

## Findings by lens

### Core loop and pillars
- **F1 · Reading has no stated cost, so it may become the dominant choice** (Inferred): "Reading changes how villagers react and unlocks small side stories." That describes only upside. If reading only adds content, most players will read every letter, and the defining choice disappears. Evidence: no downside or detection rule in the notes. Player impact: the moral tension behind the fantasy never happens.
- **F2 · Route planning has nothing at stake** (Inferred): "Plan a route on a hand-drawn map" needs a limit to mean anything, but none is stated. With 3–5 stops and no time, light or fatigue limit, every route succeeds, so planning is a step that changes nothing. Evidence: no limit on a night. Player impact: the map becomes a menu chore instead of a calm planning moment.
- **F3 · Lantern progression has no source** (Observed gap): "You upgrade your lantern" doesn't say what pays for upgrades. Evidence: no economy in the notes. Player impact: upgrades can't be tied to deliveries or reading choices, so the meta feels detached from the core.
- **Tension to resolve:** "Cozy" pulls toward never punishing the player, while F1 and F2 need consequences. The fix is consequences that make outcomes *different*, not *worse*. That matches pillar 2.

### Scoping and budget
- **F4 · Branching narrative is the biggest scope driver** (Inferred): each villager reacts to read versus sealed, across nights, and side stories depend on those choices. The writing grows fast: villagers × letters × read state. For one person who is also programming and making art, this grows fastest. Evidence: "Reading changes how villagers react and unlocks small side stories." Player impact: if it isn't capped, content goes thin or the slice slips.
- **F5 · Two traversal modes and two platforms in a 6-month solo slice** (Assumed): sled physics, a weather system that changes routes, and Switch support each add significant work. Evidence: "walk or sled", "weather changes routes", "Switch and PC". Player impact: none directly, but the slice may fail to show the core choice well.

*No manipulative patterns found.* The 30-minute, one-night structure respects players' time.

## Priority issues
| ID | Issue | Lens | Severity | Confidence | Effort |
| --- | --- | --- | --- | --- | --- |
| F1 | Reading has no cost, so it becomes the dominant choice | Core loop | P1 | Inferred | S |
| F2 | Route planning has no limit, so it's a dead step | Core loop | P2 | Inferred | S |
| F4 | Branching writing grows past one person's capacity | Scoping | P2 | Inferred | M |
| F3 | Lantern upgrades have no source | Core loop | P2 | Observed | S |
| F5 | Sled, weather and Switch all in the slice | Scoping | P3 | Assumed | S |

## Minimal-fix recommendations
1. **F1: Give sealed and read letters each their own payoff.** For example, sealed letters build trust and lead to confidences told in person, while reading lets you act on what you learned. Some villagers can tell when a seal was broken. Why: it removes the dominant option without punishing the player. Expected effect: players hesitate before reading, which is the core feeling. Check: in a paper test, see whether 5 testers split their choices instead of reading everything.
2. **F2: Add one soft limit per night.** Lantern oil or dawn works. Letters you don't deliver carry over, with a small change in reaction ("you're late"). Why: it gives the route order a purpose. Expected effect: a calm puzzle that's easy to read. Check: compare testers' routes; if everyone draws the same one, the map isn't asking anything.
3. **F3: Tie upgrades to deliveries.** Use villagers' thanks or gifts, not a currency to grind. Why: it links the meta to the core loop. Check: you can trace each upgrade back to a delivery.
4. **F4: Cap the branching.** Use 2 reaction states per letter (read or sealed), plus one remembered flag per villager. Why: the writing grows in a straight line instead of multiplying. Check: count the lines needed for the slice before writing them.
5. **F5: Make sledding a stretch goal for the slice and plan the Switch work after it.** Why: it protects the core proof. Check: if the slice works without the sled, the sled is polish.

## Next steps
1. **Week 1–2, paper prototype:** 6 villagers, 1 night, letter cards with a "read" side, a drawn map with an oil budget. Test with 3–5 people whether players hesitate before reading and whether routes differ.
2. **Decide and write down** the reading cost and the night limit (F1, F2), then update the doc's open questions.
3. **Grey-box the loop** (walk, map, deliver, react) before any art, aiming to have one full night playable by month 2.

I can also publish this as a shareable doc page if you want to send it to collaborators.
