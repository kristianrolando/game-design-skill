# Host checks, 2026-11-03

Local checks on macOS with Claude Code CLI 2.1.287 and Codex CLI 0.166.0-alpha.5.1. Nothing was installed at user scope; disposable folders were created in a temporary scratch directory and are not part of this repository.

## Claude Code

| Check | Command | Result |
| --- | --- | --- |
| Marketplace manifest | `claude plugin validate .` | Passed. |
| Plugin manifest | `claude plugin validate .claude-plugin/plugin.json` | Passed with one warning: root `CLAUDE.md` is not loaded as plugin context. Expected: that file is for contributors to this repository, not for plugin users. |
| Plugin loads from disk without installation | `claude --plugin-dir ./game-design-skill plugin details game-design-skill` | Loaded as `game-design-skill 0.1.0`, one skill (`game-design-skill`), no agents, hooks or servers. Projected cost: about 160 tokens always-on, about 1.7k tokens per invocation. |
| Model run with plugin loaded | `claude -p --plugin-dir ...` | Initially blocked by an expired sign-in. **Passed after the maintainer signed in** (see below). |
| Direct skill discovery from `.claude/skills/` | Disposable project copy | Initially blocked by the same sign-in. **Passed after the maintainer signed in** (see below). |

### After sign-in

Both runs used `claude -p` with `--output-format stream-json`, model `claude-opus-5-5`, allowed tools Read, Skill and Glob, in disposable folders.

| Check | Observed |
| --- | --- |
| Plugin session (`--plugin-dir`, not installed) | Init event listed plugin `game-design-skill@inline` 0.1.0, skill and slash command `game-design-skill:game-design-skill`. The slash command loaded the skill; the model then read `multiplayer-social.md` and `flow-fairness-failure.md` and returned a report in the template. [Raft Rally example](../examples/social-review-raft-rally-claude-plugin.md). |
| Direct skill from `.claude/skills/` | Init event listed project skill and slash command `game-design-skill`. `/game-design-skill` loaded it; the model read `pitch-gdd.md`, `core-loop-pillars.md` and `scoping-budget.md` and returned a one-page design doc under Deliverable. [Lantern Post example](../examples/one-page-gdd-lantern-post-claude-skill.md). |

## Codex

| Check | Result |
| --- | --- |
| Project-local discovery from `.agents/skills/` | Passed. With only the skill copy present and no path in the prompt, `$game-design-skill` resolved to the project copy. |
| Skill use | Passed. The run read SKILL.md plus two lens files and returned a report in the template. Recorded in [the Ember Pact example](../examples/ftue-review-ember-pact-codex.md). |

## Not covered

User-scope installs and the other six hosts in docs/hosts.md. Marketplace installation and the public install routes were checked later, in [public-routes-2026-11-03.md](public-routes-2026-11-03.md).
