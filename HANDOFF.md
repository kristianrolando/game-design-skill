# Project handoff

- format: cross-agent-handoff/1
- task_status: in_progress
- handoff: ready
- writer: none

## Project
Game Design Skill: one router skill for analyzing and developing game designs, plus a Claude Code
plugin wrapper. Lives in the Plugin-SKILL-PROJECT workspace as its own subfolder.
Public source: https://github.com/kristianrolando/game-design-skill
Rules: AGENTS.md. Contributor workflow: CONTRIBUTING.md. Claude adapter: CLAUDE.md. User docs: README.md.
Design: docs/architecture.md. Evidence: docs/validation.md. Hosts: docs/hosts.md.
Publication checklist and release history: docs/releasing.md.

## Task
Prepare v0.1.2: make develop requests keep the full report around the requested artifact (Codex returned
the document alone), record regression evidence, then publish when the maintainer approves push and tag.
Checklist: "Next version: v0.1.2" in docs/releasing.md. (v0.1.0 and v0.1.1 are published.)

## State
Public repository on main with topics, plugin URLs, CI, license and release badges. Release v0.1.1 (Latest)
is published from annotated tag v0.1.1 on 35b6daa; v0.1.0 stays on 9c9c2b1. Both tags stay frozen. Later documentation commits on main
record evidence only and do not change the released skill.

Both public install routes were verified in disposable projects: the Skills CLI copied identical skill
folders for Claude Code and Codex, and the GitHub marketplace added, installed and exposed the plugin at
local scope. The trial install was then removed; Claude Code keeps an orphan-marked cache copy it cleans itself.

README was redesigned after the release: responsive banner SVGs in docs/assets (wide and narrow, own
background for light and dark themes), a Mermaid intake flow, a "you bring / it does / you get" summary, lens
icons, a verbatim excerpt from the Night Harbor trial, and a compatibility legend. Technical content is
unchanged. Rendering was checked with GitHub's markdown API plus github-markdown-css at 1024 px and 375 px in
light and dark; the picture source switch was confirmed on the live cross-agent-handoff README.

After the maintainer signed in to the Claude Code CLI, both blocked checks passed: a session with the plugin
via --plugin-dir and a session with the direct skill in .claude/skills (examples Raft Rally and Lantern Post).
The publication checklist has no open items. Three further Claude Code trials (Gravekeeper's Garden, Guild
Forge, Echo Rooms) exercised emotional direction, motivation and prototyping, so all nine lens families have
been loaded. Prompts did not name lenses; the router loaded the intended lens first each time. One deviation:
a diagnosis request produced a Deliverable section (router reserves it for develop requests).

v0.1.1 published: SKILL.md now allows only the template
sections, puts answers to the user's questions in the Summary, and limits Deliverable to artifact requests;
plugin.json is 0.1.1; docs/releases/v0.1.1.md and its file-map row exist. Regression runs:
docs/evidence/regression-v0.1.1-2026-11-03.md. Six Codex runs (v0.1.1 and a v0.1.0 baseline) showed no
Deliverable in diagnose mode under either version. After the Claude Code session limit reset, three Claude
diagnose runs (two v0.1.1, one v0.1.0 baseline) also showed no Deliverable; both v0.1.1 runs answered the
user's questions in the Summary. Neither baseline reproduced the deviation, so the evidence shows no
regression rather than proof of the fix. Codex develop requests return only the document, without the
report, under both versions: a known limit that predates v0.1.1.

On this machine the active gh account is EternalCloverStudio; the repository belongs to kristianrolando.
Use `GH_TOKEN=$(gh auth token --user kristianrolando)` per command rather than switching the active account.
v0.1.2 prepared locally: SKILL.md says every output follows the report structure, develop requests
included; asking for an artifact is not a format switch; the artifact sits under Deliverable with every other
section kept around it. plugin.json is 0.1.2; docs/releases/v0.1.2.md and its file-map row exist. Regression
runs: docs/evidence/regression-v0.1.2-2026-11-03.md. Three Codex develop runs of Lantern Post kept the full
report (previously 0 of 3); one Claude develop run kept it; one diagnose run per host left Deliverable out.
Minor Codex drift: one omitted Lens column, two put lens names inside findings. Committed locally, not pushed.

Nothing installed at user scope. No background writers.

## Evidence
- python3 -m unittest discover -s tests -v: 19 tests passed locally on 2026-11-03, including after the
  v0.1.1 and v0.1.2 changes; git diff --check clean.
- v0.1.1 regression runs: docs/evidence/regression-v0.1.1-2026-11-03.md (Codex CLI 0.166, gpt-6.1-sol;
  Claude Code CLI 2.1.287, claude-opus-5-5).
- Hosted CI passed on all four jobs for 79591ac (run 41560385711) and 9c9c2b1 (run 41560556115).
- Release workflow run 41561103985 passed checks and publish; release v0.1.0 targets 9c9c2b1.
- v0.1.1: hosted CI run 41590763914 passed all four jobs on 35b6daa; release workflow run 41590841216
  passed checks and publish; release v0.1.1 targets 35b6daa and is marked Latest.
- Public routes: docs/evidence/public-routes-2026-11-03.md. Local host checks:
  docs/evidence/host-checks-2026-11-03.md.
- Model trials: two Claude subagent trials, one Codex CLI trial, and five Claude Code CLI trials (plugin,
  direct skill, and three lens trials) in docs/examples. All nine lens families covered.
- v0.1.2 regression runs: docs/evidence/regression-v0.1.2-2026-11-03.md (same hosts and models).
- Limits: single runs; trial concepts are invented; six hosts are documented routes only.

## Next
With maintainer approval: push main, check hosted CI, push annotated tag v0.1.2 on that commit, check the
release workflow, then record links (README badge, releasing.md, validation.md, this file).
Later quality work: review a real design from the maintainer; repeated runs to measure format drift.
Never move a published tag.

## Recent outcomes
- 2026-11-03: Created game-design-skill v0.1.0 with nine lenses, tests and a recorded trial.
- 2026-11-03: Added repository files, CI and release workflows, docs, checklist and host checks.
- 2026-11-03: Published the public repository; first hosted CI passed on all four jobs.
- 2026-11-03: Verified public install routes and published release v0.1.0.
- 2026-11-03: Redesigned the README with responsive banner artwork and a Mermaid flow (19 tests pass).
- 2026-11-03: Claude Code plugin and direct-skill model sessions passed after re-sign-in.
- 2026-11-03: Trials for emotional direction, motivation and prototyping; all nine lenses now exercised.
- 2026-11-03: Prepared v0.1.1 (Deliverable rule) with Codex regression evidence; local commit, not pushed.
- 2026-11-03: Claude Code reruns after the limit reset: no Deliverable in v0.1.1 or baseline.
- 2026-11-03: Published release v0.1.1 from tag v0.1.1 on 35b6daa; CI and release workflow passed.
- 2026-11-03: Prepared v0.1.2 (full report in develop mode); 3 of 3 Codex develop runs kept the report.
