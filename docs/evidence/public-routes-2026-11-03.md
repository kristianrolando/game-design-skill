# Public install routes and release, 2026-11-03

Checks against the public repository at commit `9c9c2b1`, run on macOS in disposable folders outside this repository.

## Skills CLI

`npx -y skills@1.7.6 add kristianrolando/game-design-skill --skill game-design-skill --agent claude-code codex --copy -y` (Node.js 26.11.1) installed the skill at project scope into `.claude/skills/game-design-skill` and `.agents/skills/game-design-skill`. `diff -r` showed both copies identical to `skills/game-design-skill` in this repository, including LICENSE, `references/` and `agents/`. The installer also wrote `skills-lock.json` in the disposable project.

## Claude Code marketplace

With Claude Code CLI 2.1.287, local scope in a disposable project:

1. `claude plugin marketplace add kristianrolando/game-design-skill --scope local` cloned the repository, validated the catalog and added `game-design-tools`.
2. `claude plugin install game-design-skill@game-design-tools -s local` installed and enabled `game-design-skill` 0.1.0.
3. `claude plugin details game-design-skill@game-design-tools` listed one skill, `game-design-skill`.
4. The plugin was then uninstalled and the marketplace removed. Both settings entries are empty again. Claude Code left an orphan-marked cache copy of the public files in its plugin cache, which it cleans up itself.

No Claude model session ran: the CLI sign-in had expired, so invoking the installed plugin remains unobserved.

## Release

Tag `v0.1.0` (annotated) was pushed on `9c9c2b1c9af82920e063d75be632f04e45286201`. [Release workflow run 41561103985](https://github.com/kristianrolando/game-design-skill/actions/runs/41561103985) passed its checks and publish jobs and created the [v0.1.0 release](https://github.com/kristianrolando/game-design-skill/releases/tag/v0.1.0) from `docs/releases/v0.1.0.md`.
