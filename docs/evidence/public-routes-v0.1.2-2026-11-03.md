# Public install, update and removal routes for v0.1.2, 2026-11-03

Checks against the public repository after release v0.1.2 (main at `83273ba`, skill files identical to tag `v0.1.2`), run on macOS in disposable folders outside this repository. They repeat the [v0.1.0 route checks](public-routes-2026-11-03.md) and add update, removal and a model session with the marketplace-installed plugin.

## Skills CLI

Skills CLI 1.7.6 on Node.js 26.11.1, project scope:

1. `npx -y skills@1.7.6 add kristianrolando/game-design-skill --skill game-design-skill --agent claude-code codex --copy -y` installed the skill into `.claude/skills/game-design-skill` and `.agents/skills/game-design-skill`. `diff -r` showed both copies identical to `skills/game-design-skill` at v0.1.2, including the new develop-mode wording in SKILL.md.
2. `npx skills list` showed `game-design-skill` with source `kristianrolando/game-design-skill`.
3. `npx skills update game-design-skill -p -y` fetched the source and reported all project skills up to date.
4. `npx skills remove game-design-skill -y` emptied both skill folders and left `skills-lock.json` with no skills.

## Claude Code marketplace

Claude Code CLI 2.1.287, local scope in a disposable project:

1. `claude plugin marketplace add kristianrolando/game-design-skill --scope local` cloned and validated the catalog and added `game-design-tools`.
2. `claude plugin install game-design-skill@game-design-tools -s local` installed and enabled version 0.1.2. `claude plugin details` listed one skill, `game-design-skill`, with about 224 always-on tokens.
3. **Model session with the installed plugin.** `claude -p --model claude-opus-5-5 --allowedTools Read,Skill,Glob --output-format stream-json` with the prompt below. The init event listed the plugin `game-design-skill@game-design-tools` 0.1.2 from the plugin cache and the skill `game-design-skill:game-design-skill`. The run read `references/ftue-retention.md` from the cached plugin and returned a report with the template headings in order and no Deliverable section (2 turns, about 36 seconds).

   > /game-design-skill:game-design-skill Quick question: in my mobile roguelite concept for commuters, one run lasts about 45 minutes and cannot be paused mid-fight. Is that a problem, and what is the smallest fix? Stage: concept.

4. `claude plugin marketplace update game-design-tools` refreshed the catalog; `claude plugin update game-design-skill@game-design-tools -s local` reported the plugin already at the latest version (0.1.2).
5. `claude plugin uninstall game-design-skill@game-design-tools -s local` and `claude plugin marketplace remove game-design-tools` succeeded. `.claude/settings.local.json` was left with empty `enabledPlugins` and `extraKnownMarketplaces`, and `claude plugin list` no longer showed the plugin.

## Limits

An update was checked only as "already up to date"; moving from an older installed version to a newer one was not exercised, because both routes install from the default branch, which already carries v0.1.2. User-scope (global) installs were not tested, to keep user settings unchanged. One model session, with one quick question.
