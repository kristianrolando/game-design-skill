# Validation evidence and limits

Evidence is grouped by kind. Automated checks, model trials and host checks prove different things; none of them proves that the skill's advice is correct for a real game.

## Automated checks

`python3 -m unittest discover -s tests -v` passes locally (see HANDOFF.md for the latest count and date). What the suite covers is listed in [ci.md](ci.md). Hosted CI passed on all four jobs (Ubuntu with Python 3.9 and 3.13, macOS, Windows) in the [first run](https://github.com/kristianrolando/game-design-skill/actions/runs/41560385711) on commit `79591ac` and for the v0.1.1 release commit `35b6daa` ([run](https://github.com/kristianrolando/game-design-skill/actions/runs/41590763914)). The reference-bundle overlap test is skipped there.

## Model trials

| Date | Host / model | Request | Lenses loaded | Record |
| --- | --- | --- | --- | --- |
| 2026-11-03 | Claude Opus 5.5 subagent, explicit file reads | Core loop audit, full context | Core loop, flow, FTUE | [Night Harbor](examples/core-loop-audit-night-harbor.md) |
| 2026-11-03 | Claude Opus 5.5 subagent, explicit file reads | Core loop question, almost no context | None (asked three questions with defaults) | Intake check in the Night Harbor record |
| 2026-11-03 | Codex CLI 0.166, `gpt-6.1-sol`, native project skill discovery | FTUE review with playtest notes | FTUE, flow | [Ember Pact](examples/ftue-review-ember-pact-codex.md) |
| 2026-11-03 | Claude Code CLI 2.1.287, `claude-opus-5-5`, plugin via `--plugin-dir` | Social design review | Multiplayer and social, flow | [Raft Rally](examples/social-review-raft-rally-claude-plugin.md) |
| 2026-11-03 | Claude Code CLI 2.1.287, `claude-opus-5-5`, direct skill in `.claude/skills/` | One-page design doc (develop mode) | Pitch and GDD, core loop, scoping | [Lantern Post](examples/one-page-gdd-lantern-post-claude-skill.md) |
| 2026-11-03 | Claude Code CLI 2.1.287, `claude-opus-5-5`, direct skill | Emotional direction question | Emotional direction, core loop, prototyping | [Gravekeeper's Garden](examples/emotional-direction-gravekeepers-garden-claude.md) |
| 2026-11-03 | Claude Code CLI 2.1.287, `claude-opus-5-5`, direct skill | Feature adoption and audience question | Motivation, core loop, flow | [Guild Forge](examples/motivation-guild-forge-claude.md) |
| 2026-11-03 | Claude Code CLI 2.1.287, `claude-opus-5-5`, direct skill | What to prototype first | Prototyping, scoping, core loop | [Echo Rooms](examples/prototyping-plan-echo-rooms-claude.md) |

Lens coverage across trials: all nine lens families have been loaded at least once. In the last three trials the prompts described symptoms without naming a lens, and the router loaded the intended lens first each time.

One deviation was observed: in the Gravekeeper's Garden diagnosis, the report added a `Deliverable` section with a proposed tone guide, although the router reserves Deliverable for develop requests. Version 0.1.1 tightens that rule in SKILL.md.

### Regression runs for v0.1.1

See [regression-v0.1.1-2026-11-03.md](evidence/regression-v0.1.1-2026-11-03.md). Six Codex runs and three Claude Code runs reused the Gravekeeper's Garden and Lantern Post inputs under v0.1.1 and, as a baseline, v0.1.0. None of the four v0.1.1 diagnose runs added Deliverable, so no regression was seen, and both Claude runs answered the user's questions in the Summary. The fix is consistent with this but not proven: neither baseline reproduced the deviation, which has appeared once in two v0.1.0 Claude Code runs of this input. In develop mode Codex returned only the requested document, without the surrounding report, under both versions; this predates v0.1.1.

Observed across the trials: the router's intake rule, lens selection, confidence labels, severity table, minimal fixes with checks, develop-mode Deliverable section, and the unprompted ethics flag all appeared as specified. The concepts were written for the trials, so the findings are design reasoning, not evidence about real players. Each trial is a single run.

## Host checks

See [host-checks-2026-11-03.md](evidence/host-checks-2026-11-03.md). Summary:

- Claude Code: plugin and marketplace manifests validate; the plugin loads from disk and exposes the skill. After the maintainer signed in again, a model session invoked the plugin skill, and a separate session discovered and invoked the direct skill from `.claude/skills/`.
- Codex: native discovery from `.agents/skills/` and skill use were observed.
- Antigravity, Cursor, Gemini CLI, GitHub Copilot, OpenCode and Cline: documented routes only ([hosts.md](hosts.md)); not exercised.

## Public install routes and release

See [public-routes-2026-11-03.md](evidence/public-routes-2026-11-03.md). The Skills CLI installed identical copies for Claude Code and Codex; the GitHub marketplace added, installed and exposed the plugin at local scope; tag `v0.1.0` produced the GitHub release through the release workflow, and tag `v0.1.1` produced the v0.1.1 release ([run](https://github.com/kristianrolando/game-design-skill/actions/runs/41590841216)).

## Content provenance

With the reference bundle present locally, the suite confirms no 10-word passage is shared with it. A manual 7-word scan during authoring found five generic phrases, which were reworded. This check does not run in CI.

## Not established

Advice quality on real projects, behavior across many runs or models, how often the Deliverable deviation occurs under either version (single runs cannot show it), report structure in Codex develop mode, a model session with the plugin installed through the marketplace (the session used `--plugin-dir`), user-scope installs, and hosts not listed above.
