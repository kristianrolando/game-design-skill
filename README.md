# Game Design Skill

One router skill for analyzing and developing game designs. Give it a concept, feature spec, pitch deck, GDD, prototype notes or playtest feedback; it gathers missing context, picks the most relevant design lenses, and returns a prioritized report with minimal fixes and next steps.

Works as a Claude Code plugin or direct skill, as a Codex skill, and in other agents that read `SKILL.md` files. The skill text is host-neutral. See [compatibility](#compatibility).

## Quick start

**Before publication** (from a local checkout of this folder):

| Host | Route |
| --- | --- |
| Claude Code, one session without installing | `claude --plugin-dir ./game-design-skill` |
| Claude Code, direct skill | Copy `skills/game-design-skill` to your project's `.claude/skills/` |
| Codex and other `.agents/skills/` hosts | Copy `skills/game-design-skill` to your project's `.agents/skills/` |
| Any agent with file access | Ask it to read `skills/game-design-skill/SKILL.md` and follow it |

**After publication** at `kristianrolando/game-design-skill` (planned, not live yet):

```text
/plugin marketplace add kristianrolando/game-design-skill
/plugin install game-design-skill@game-design-tools
```

```sh
npx skills add kristianrolando/game-design-skill --skill game-design-skill
```

Locations for all hosts, and how to activate the skill in each, are in the [host guide](docs/hosts.md). Use one installation route per host.

### Example prompts

| Host | Prompt |
| --- | --- |
| Claude Code plugin | `/game-design-skill:game-design-skill Audit the core loop of this concept: ...` |
| Claude Code direct skill, Antigravity, Cursor, Cline | `/game-design-skill Review our FTUE script and tell me where players will drop.` |
| Codex | `Use $game-design-skill to turn these notes into a one-page design doc.` |
| Gemini CLI, Copilot, OpenCode | `Use the game-design-skill skill: is this scope realistic for two part-time developers in 9 months?` |

## What it covers

Nine lens families, each loaded only when needed:

| Lens family | Typical questions |
| --- | --- |
| [Emotional direction](skills/game-design-skill/references/emotional-direction.md) | What is the player fantasy? Does the tone hold together? What will players remember? |
| [Player motivation](skills/game-design-skill/references/motivation.md) | Why do players keep going? Who is this for, and who will bounce? Why is a feature unused? |
| [Core loop and pillars](skills/game-design-skill/references/core-loop-pillars.md) | What is the repeatable engine? Which features are orphans? Do the pillars decide anything? |
| [Flow, fairness and failure](skills/game-design-skill/references/flow-fairness-failure.md) | Where is it boring or overwhelming? Why does it feel unfair? Is failure worth retrying? |
| [FTUE and retention](skills/game-design-skill/references/ftue-retention.md) | Does onboarding hook players? Is there always a next goal? Are return reasons healthy? |
| [Multiplayer and social](skills/game-design-skill/references/multiplayer-social.md) | Do players need each other? Are social foundations in place? Is the ladder fair? |
| [Prototyping](skills/game-design-skill/references/prototyping.md) | What is the riskiest assumption? What should we test first, and when do we stop? |
| [Pitch and GDD](skills/game-design-skill/references/pitch-gdd.md) | Write a one-page design doc. Is the GDD healthy? Is the pitch deck convincing? |
| [Scoping and budget](skills/game-design-skill/references/scoping-budget.md) | What do we build first? Which skills are missing? How long and how much, roughly? |

## How it works

1. **Intake**: reads the material and checks genre, platform, target player and production stage. If something missing would change the answer, it asks up to three short questions with defaults; otherwise it states assumptions and continues.
2. **Choose lenses**: one lens for a quick question, two or three for a standard review, up to five for a full audit, ordered structure before polish and matched to the production stage.
3. **Analyze**: findings tied to evidence in the material, each labeled Observed, Inferred or Assumed.
4. **Report**: summary, findings by lens, a priority table (P1 to P3 with effort), minimal-fix recommendations with a way to verify each, and next steps.

Recorded trials, unedited:

- [Core loop audit of a cozy fishing concept](docs/examples/core-loop-audit-night-harbor.md) (Claude subagent), including an intake check.
- [FTUE review of a deckbuilder prototype](docs/examples/ftue-review-ember-pact-codex.md) (Codex CLI, native skill discovery).

## Compatibility

| Host / component | Route | Evidence and limits |
| --- | --- | --- |
| **Claude Code** | Included plugin or direct skill | Plugin and marketplace manifests validate; the plugin loads from disk and exposes the skill (CLI 2.1.287). A model session with the plugin was not observed: the CLI sign-in had expired. A Claude subagent followed the skill via explicit file reads in two trials. |
| **Codex** | Direct skill; optional `agents/openai.yaml` metadata | Codex CLI 0.166 discovered the project-local skill and produced a report in the template. |
| **Antigravity, Cursor, Gemini CLI, GitHub Copilot, OpenCode, Cline** | Direct skill in the [documented folders](docs/hosts.md) | Documented routes only; not exercised for this package. |
| Other filesystem agents | Explicitly read `SKILL.md` | Portable fallback; native discovery not verified. |
| Plain chat | Paste or upload SKILL.md and the relevant lens file | Works as instructions; no on-demand lens loading. |

Details and dates: [validation evidence](docs/validation.md).

## Documentation

| Start here | Go deeper |
| --- | --- |
| [Host installation and activation](docs/hosts.md) | [Architecture and trade-offs](docs/architecture.md) |
| [Recorded trials](docs/examples/core-loop-audit-night-harbor.md) | [Validation evidence and limits](docs/validation.md) |
| [Contributing with any agent](CONTRIBUTING.md) | [File map](docs/file-map.md) |
| [Publication checklist](docs/releasing.md) | [Automated checks](docs/ci.md) |

## Checks

```sh
python3 -m unittest discover -s tests -v
```

The tests validate the skill frontmatter, lens table and links, the six required sections in each lens file, the report format and recorded examples, the plugin manifests, release notes, workflows, license copies, host-neutral wording, and, when the reference bundle is present locally, that no long passage is shared with it.

## Credits and provenance

The design frameworks named in the lenses belong to their authors, including Self-Determination Theory (Deci and Ryan), Flow (Csikszentmihalyi), player types (Bartle), the Fogg Behavior Model (Fogg), attribution theory (Weiner), fast and slow thinking (Kahneman), the Zeigarnik effect and the monomyth (Campbell).

The choice of topics was informed by the Game Design Skills Bundle by Stanislav Stankovic, which is licensed PolyForm Noncommercial 1.0.0. No text from that bundle is included here. This package's instructions, structure and wording are original and licensed under MIT.

## License

[MIT](LICENSE) · Copyright (c) 2026 Kristian Rolando Limantara.
