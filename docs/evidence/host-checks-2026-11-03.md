# Host checks, 2026-11-03

Local checks on macOS with Claude Code CLI 2.1.287 and Codex CLI 0.166.0-alpha.5.1. Nothing was installed at user scope; disposable folders were created in a temporary scratch directory and are not part of this repository.

## Claude Code

| Check | Command | Result |
| --- | --- | --- |
| Marketplace manifest | `claude plugin validate .` | Passed. |
| Plugin manifest | `claude plugin validate .claude-plugin/plugin.json` | Passed with one warning: root `CLAUDE.md` is not loaded as plugin context. Expected: that file is for contributors to this repository, not for plugin users. |
| Plugin loads from disk without installation | `claude --plugin-dir ./game-design-skill plugin details game-design-skill` | Loaded as `game-design-skill 0.1.0`, one skill (`game-design-skill`), no agents, hooks or servers. Projected cost: about 160 tokens always-on, about 1.7k tokens per invocation. |
| Model run with plugin loaded | `claude -p --plugin-dir ...` | **Blocked**: "OAuth session expired and could not be refreshed". No model call was made. |
| Direct skill discovery from `.claude/skills/` | Disposable project copy | **Blocked**: discovery can only be observed through a model session, which needs sign-in. `claude plugin details` does not cover direct skills. |

## Codex

| Check | Result |
| --- | --- |
| Project-local discovery from `.agents/skills/` | Passed. With only the skill copy present and no path in the prompt, `$game-design-skill` resolved to the project copy. |
| Skill use | Passed. The run read SKILL.md plus two lens files and returned a report in the template. Recorded in [the Ember Pact example](../examples/ftue-review-ember-pact-codex.md). |

## Not covered

Plugin installation through a marketplace, the public install routes (the repository is unpublished), user-scope installs, and the other six hosts in docs/hosts.md.
