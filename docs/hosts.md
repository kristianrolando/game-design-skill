# Host installation and activation

Copy the entire `skills/game-design-skill` folder, including LICENSE, `references/` and `agents/`, into **one** supported location per host. Each path below is a parent directory: the entry file is `<parent>/game-design-skill/SKILL.md`. Inspect existing installations before replacing them, and keep every copy on the same version.

The locations come from the host guide in the sibling `cross-agent-handoff` package, reviewed against official documentation on 2026-11-02. They were not rechecked separately for this package, and host features change with versions and settings. Live evidence for this package is listed in [validation.md](validation.md).

| Host | Project skill parent | User skill parent | Activation |
| --- | --- | --- | --- |
| Claude Code | `.claude/skills/` | `~/.claude/skills/` | Direct: `/game-design-skill`. Plugin: `/game-design-skill:game-design-skill`. Does not read `.agents/skills/`. |
| Codex | `.agents/skills/` | `~/.agents/skills/` | `Use $game-design-skill to ...`, or pick it from `/skills`. |
| Google Antigravity | `.agents/skills/` | `~/.gemini/config/skills/` | `/game-design-skill`; run `/skills reload` in the CLI after adding it mid-session. |
| Cursor | `.agents/skills/`, `.cursor/skills/` or `.claude/skills/` | `~/.agents/skills/` or `~/.cursor/skills/` | `/game-design-skill` in Agent chat. |
| Gemini CLI | `.agents/skills/` or `.gemini/skills/` | `~/.agents/skills/` or `~/.gemini/skills/` | Check `/skills list`, request the skill by name and accept the activation prompt. |
| GitHub Copilot | `.github/skills/`, `.agents/skills/` or `.claude/skills/` | `~/.copilot/skills/` or `~/.agents/skills/` | No slash command; name the skill in the request. |
| OpenCode | `.opencode/skills/`, `.agents/skills/` or `.claude/skills/` | `~/.config/opencode/skills/`, `~/.agents/skills/` or `~/.claude/skills/` | Ask it to load `game-design-skill`; check `permission.skill` if hidden. |
| Cline | `.cline/skills/` or `.claude/skills/` | `~/.cline/skills/` | Enable it in the Skills tab, then `/game-design-skill` or request it by name. |

No single folder reaches every host: `.agents/skills/` serves Codex, Antigravity, Cursor, Gemini CLI, Copilot and OpenCode; `.claude/skills/` serves Claude Code, Cursor, Copilot, OpenCode and Cline.

## Claude Code plugin

The repository root is a Claude Code plugin with its own marketplace catalog (`game-design-tools`). Before publication:

```sh
claude --plugin-dir /path/to/game-design-skill
```

loads the plugin for one session without installing it. `/plugin marketplace add /path/to/game-design-skill` followed by `/plugin install game-design-skill@game-design-tools` installs it at user scope. After publication, the marketplace can be added as `kristianrolando/game-design-skill`. The plugin wrapper is Claude-specific; other hosts use the direct skill.

## Installer option

After publication, the public Skills CLI (Node.js 22.20+) can copy the skill into a chosen host's folder:

```sh
npx skills add kristianrolando/game-design-skill --skill game-design-skill
```

Review the destination it reports; if the host does not discover it there, use the manual paths above.

## Fallback

Any agent with file access can use the skill without installation:

```text
Read skills/game-design-skill/SKILL.md and follow it to review this game design.
Load reference files only where it tells you to.
```
