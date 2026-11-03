# Example: social design review of "Raft Rally" in Claude Code

## Trial record

- **Date:** 2026-11-03.
- **Host and model:** Claude Code CLI 2.1.287 in print mode (`claude -p`), model `claude-opus-5-5`, signed in with a claude.ai account.
- **Setup:** a disposable empty folder outside this repository, with the plugin loaded for the session only via `--plugin-dir` (not installed). Allowed tools: Read, Skill, Glob. Other plugins already installed for the user were also loaded.
- **Invocation:** the plugin slash command `/game-design-skill:game-design-skill` with the request below. The session's init event listed the skill `game-design-skill:game-design-skill` from plugin `game-design-skill@inline` 0.1.0.
- **Files read after the skill loaded:** `references/multiplayer-social.md`, `references/flow-fairness-failure.md`. The run took 3 turns and about 66 seconds.
- **Output:** the final result, reproduced unedited.
- **Limits:** one run of one model. The concept was written for the trial; findings are design reasoning, not playtest evidence.

### Input given to the agent

> /game-design-skill:game-design-skill Review the social design of my game and tell me what to fix first.
>
> Raft Rally: online co-op survival game for PC, 2-4 players, for groups of friends who play together on weekend evenings. Stage: pre-production, nothing built. Players share one raft, gather floating debris, craft upgrades and fend off sharks. Matchmaking also fills empty slots with strangers through public lobbies. There is open text chat. Any player can dismantle any raft piece. Loot is first come, first served. There are no kick, block or report tools yet.

### Reviewer notes

- First trial of the multiplayer and social lens. It produced the social-feature tier table that the lens's reporting notes ask for, and separated a moderation staffing item as operational, with an owner.
- It named a contradiction between lenses (rules that suit friends but break with strangers) instead of smoothing it over, as the router requires.
- It explained why the fix order differs from the severity order (F3 first: small effort that limits exposure to F1 and F2).
- Every minimal fix has a check; next steps are a decision, a doc change and a test.

---

# Game design review: Raft Rally (social design)

**Context:** Online co-op survival · PC, mouse and keyboard · groups of 2–4 friends playing on weekend evenings · pre-production, nothing built · one-paragraph concept summary
**Assumptions:** (1) The raft persists across sessions, so damage to it carries over. (2) Voice chat is out of scope, so text chat is the only built-in channel. (3) Age rating isn't set yet, so minors may play. (4) No population numbers are available, so any concurrent-player figures are unknown.
**Lenses:** I used **Multiplayer and social** as the main lens because that's what you asked about. I also used **Flow, fairness and failure** for the dismantle and loot rules, because they decide whether losses feel fair. I skipped core loop, motivation and FTUE (first-time user experience). The sharks, debris and crafting loop sounds sound, but how it plays is out of scope here.

## Summary

Raft Rally has a strong social core: one shared raft that everyone builds and defends is a natural shared goal. That suits a friend group's weekend session well. The biggest problem is a mismatch. The rules assume everyone trusts each other: anyone can dismantle anything, loot goes to whoever grabs it first, and there's no kick. Those rules work for friends and break with strangers, and public matchmaking brings strangers in. One stranger can sink a group's raft, and the group has no way to stop it. **Fix first:** decide how public lobbies work. Make random fill opt-in, and use different rules for friends-only and public lobbies. Ship kick, mute and block before any stranger can join.

## Findings by lens

### Multiplayer and social

- **F1 · One stranger can sink everyone's raft** (Inferred): Three stated rules combine into a guaranteed griefing route. Evidence: "Any player can dismantle any raft piece", "fills empty slots with strangers through public lobbies" and "no kick, block or report tools". The raft holds everyone's shared progress, and it's also what keeps players alive. A griefer can delete hours of a group's work in seconds, and the group can only quit. If the raft persists (assumption 1), the damage outlives the session. Player impact: friend groups learn that public lobbies are dangerous and stop using them, or stop playing after their first griefed raft.

- **F2 · Safety basics are missing while risky features ship** (Observed): Your concept includes three high-risk features: open text chat, a raft anyone can damage, and matchmaking with strangers. It has none of the basic tools players expect to answer them. Evidence: "There is open text chat… There are no kick, block or report tools yet."

  | Feature | Tier | Status | Risk |
  | --- | --- | --- | --- |
  | Invite friends | Basic | Not stated | Core to the audience. It must exist. |
  | Kick (by host or vote) | Basic | Missing | There's no answer to a griefer in your session. |
  | Mute and block | Basic | Missing | There's no answer to harassment in chat. |
  | Report | Basic | Missing | It also needs someone to handle reports. That's an operations job, not a design job (owner: producer). |
  | Pings ("debris here", "shark!", "help") | Basic | Missing | Typing in the middle of a shark attack is impractical. Without pings, strangers can't coordinate. |
  | Leaver handling | Basic | Not stated | When a stranger leaves, what happens to their loot? (See F3.) |
  | Open text chat | High risk | Present | Needs defaults: a profanity filter, mute per player, and stricter settings if minors may play (assumption 3). |
  | Free dismantle | High risk | Present | See F1. |

  Player impact: when these tools are missing, players notice and get angry. When they're present, nobody notices. They come before any delighter, such as emotes or celebrations.

- **F3 · Public random fill doesn't match your stated audience** (Assumed): Your target player is "groups of friends who play together on weekend evenings", but matchmaking fills empty slots with strangers. The real need is narrower: a group is short one friend tonight, or one friend shows up late. Random fill on by default exposes friend groups to F1 and F2 without being asked. It also assumes enough people will be queuing for a public lobby. A niche co-op indie may not have that population outside peak hours (assumption 4). Player impact: groups get strangers they didn't want, and solo players wait in empty queues.

- **F4 · You haven't defined why players need each other** (Assumed): The concept says players "gather… craft… fend off sharks". It doesn't say whether any task needs two people. If everyone can do everything alone, a 4-player raft becomes four people playing solo side by side. That's tolerable with friends who are chatting anyway, and lonely with strangers. Evidence: the concept has no roles and no task that needs more than one player. Player impact: there's little to create the "we barely saved the raft" moments that friend groups retell.

### Flow, fairness and failure

- **F5 · First-come loot makes teammates compete for items** (Inferred): Evidence: "Loot is first come, first served." The game is co-op on a shared raft, yet floating debris becomes a race between teammates. Among friends this is banter. With strangers it reads as theft, and a stranger can leave and take the materials with them. Crafting upgrades go into the shared raft, so a personal-pickup race works against the game's own shared goal. Player impact: the person who loses the race will blame other players, not the game. That's when people start fights or leave.

- **Contradiction to settle, not smooth over:** For friends, free dismantle and loot races are features. Friends rebuild fast, joke about stolen planks, and enjoy having no permission prompts. For strangers they're attack routes. One rule set can't serve both, so the fix is to set the rules by how much the lobby trusts each other, not to remove the rules.

## Priority issues

| ID | Issue | Lens | Severity | Confidence | Effort |
| --- | --- | --- | --- | --- | --- |
| F1 | A stranger can dismantle the shared raft | Social / Fairness | P1 | Inferred | M |
| F2 | No kick, mute, block, report or pings | Social | P1 | Observed | M |
| F3 | Random fill is on by default for a friend-group audience | Social | P2 | Assumed | S |
| F5 | First-come loot sets teammates against each other | Fairness | P2 | Inferred | S |
| F4 | No interdependence mechanic defined | Social | P2 | Assumed | M |

F3 is only P2 by itself. It comes first in the fixes below because it's a small-effort decision, and it limits how far F1 and F2 can spread while you build their tools.

## Minimal-fix recommendations

1. **F3: Make lobbies friends-only by default, and make public fill opt-in, per session.** Why: limits stranger exposure to groups that choose it. Expected effect: friend groups keep their trusted sessions, and public play becomes a deliberate choice. Check: write it into the lobby flow in the GDD now. After launch, track the share of sessions with fill turned on.
2. **F1: Use different dismantle rules for each lobby type.** In friends-only lobbies, keep free dismantle. In public lobbies, players can dismantle only pieces they placed. Anything else needs the host's approval, or a hold-to-dismantle that teammates can see and cancel. Also add a short log of dismantled pieces with a refund. Why: it removes the one-stranger-ruins-all route without slowing down friends. Expected effect: one bad actor can't wipe the raft. Check: run a greybox playtest with one tester secretly told to grief, once with the rule and once without. Watch whether the group can recover.
3. **F2: Before public lobbies go live, ship host kick (or a vote kick when the host leaves), mute and block per player, and 4–6 context pings.** Report can follow, with an owner for handling reports. Why: players need some answer to every griefing and harassment route. Expected effect: groups can remove a bad stranger instead of quitting. Check: keep a griefing table in the GDD with each route and the tool that answers it. Every route needs at least one tool.
4. **F5: Send crafting materials to a shared raft stash on pickup.** Keep personal pickup only for cosmetics or rare finds, if you want any. Why: the shared goal should get shared resources. Expected effect: grabbing debris helps the team instead of beating a teammate to it, and a stranger who leaves takes nothing. Check: add it to the same playtest. Count arguments and complaints about loot under each rule.
5. **F4: Add one task that needs two people.** For example, a large piece of salvage needs two players to haul it in. Or patching a shark bite while someone else holds the shark off. Why: it creates moments where players need each other. Expected effect: groups talk more and form roles without being assigned them. Check: in the prototype, count how often players coordinate unprompted. Without interdependence, expect mostly parallel play. Treat that as a guess until you've tested it.

## Next steps

1. **Decision (lead designer and producer):** decide whether public matchmaking is in launch scope at all. If it isn't, F1 and F2 drop to P2. You'd still want kick and mute for friend-of-friend sessions. If it is, fixes 1–3 must ship with it.
2. **Doc change (lead designer):** add a "Lobby trust" section to the GDD. It should list each rule (dismantle, loot, chat, kick) for friends-only and public lobbies, plus the griefing table from fix 3.
3. **Test (first greybox milestone):** run a 4-player session with one planted griefer. Compare free and restricted dismantle, and first-come and shared loot. This would confirm or refute F1 and F5 before either system is built for real.
