# Validation evidence and limits

Evidence is grouped by kind. Automated checks, model trials and host checks prove different things; none of them proves that the skill's advice is correct for a real game.

## Automated checks

`python3 -m unittest discover -s tests -v` passes locally (see HANDOFF.md for the latest count and date). What the suite covers is listed in [ci.md](ci.md). Hosted CI passed on all four jobs (Ubuntu with Python 3.9 and 3.13, macOS, Windows) in the [first run](https://github.com/kristianrolando/game-design-skill/actions/runs/41560385711) on commit `79591ac`. The reference-bundle overlap test is skipped there.

## Model trials

| Date | Host / model | Request | Lenses loaded | Record |
| --- | --- | --- | --- | --- |
| 2026-11-03 | Claude Opus 5.5 subagent, explicit file reads | Core loop audit, full context | Core loop, flow, FTUE | [Night Harbor](examples/core-loop-audit-night-harbor.md) |
| 2026-11-03 | Claude Opus 5.5 subagent, explicit file reads | Core loop question, almost no context | None (asked three questions with defaults) | Intake check in the Night Harbor record |
| 2026-11-03 | Codex CLI 0.166, `gpt-6.1-sol`, native project skill discovery | FTUE review with playtest notes | FTUE, flow | [Ember Pact](examples/ftue-review-ember-pact-codex.md) |

Observed across the trials: the router's intake rule, lens selection, confidence labels, severity table, minimal fixes with checks, and the unprompted ethics flag all appeared as specified. The concepts were written for the trials, so the findings are design reasoning, not evidence about real players. Each trial is a single run.

## Host checks

See [host-checks-2026-11-03.md](evidence/host-checks-2026-11-03.md). Summary:

- Claude Code: plugin and marketplace manifests validate; the plugin loads from disk and exposes the skill. A Claude Code model session could not run because the CLI sign-in had expired, so plugin invocation and direct skill discovery in Claude Code are not yet observed.
- Codex: native discovery from `.agents/skills/` and skill use were observed.
- Antigravity, Cursor, Gemini CLI, GitHub Copilot, OpenCode and Cline: documented routes only ([hosts.md](hosts.md)); not exercised.

## Content provenance

With the reference bundle present locally, the suite confirms no 10-word passage is shared with it. A manual 7-word scan during authoring found five generic phrases, which were reworded. This check does not run in CI.

## Not established

Advice quality on real projects, behavior across many runs or models, marketplace and public install routes, user-scope installs, and hosts not listed above.
