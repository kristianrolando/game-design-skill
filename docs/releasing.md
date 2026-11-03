# Publishing and releases

## Publication status

Public repository: [kristianrolando/game-design-skill](https://github.com/kristianrolando/game-design-skill), created and first pushed by the maintainer on 2026-11-03.
Latest release: [v0.1.2](https://github.com/kristianrolando/game-design-skill/releases/tag/v0.1.2) ([notes](releases/v0.1.2.md)), annotated tag on verified commit `328d11bbceeffb84637d75e96824ef4d42fd239f`. Previous: [v0.1.1](https://github.com/kristianrolando/game-design-skill/releases/tag/v0.1.1) on `35b6daa` and [v0.1.0](https://github.com/kristianrolando/game-design-skill/releases/tag/v0.1.0) on `9c9c2b1`. Keep all tags frozen; later documentation updates go on main without moving them. If the repository is ever renamed, update the names listed in step 0.

## Publication checklist

Steps marked **(maintainer)** need an explicit decision or approval from the maintainer. The others can be done locally without pushing anything.

### 0. Decisions (maintainer)

The maintainer accepted these defaults on 2026-11-03 by approving phase 3.

- [x] Repository name and visibility: public `kristianrolando/game-design-skill`. The name appears in `.github/workflows/release.yml` (publish guard), README install routes, docs/hosts.md and `plugin.json`.
- [x] First release version: `v0.1.0`, matching `plugin.json`.
- [x] Marketplace: a separate `game-design-tools` catalog, not merged with `cross-agent-tools`.
- [x] Host claims: documented routes for the hosts in [hosts.md](hosts.md), with live evidence recorded only where a trial actually ran.

### 1. Repository files (local)

- [x] `.gitignore`, `CONTRIBUTING.md`, `.github/pull_request_template.md`.
- [x] `.github/workflows/ci.yml` (four-job matrix) and `.github/workflows/release.yml` (tag, version and notes checks before publishing).
- [x] `docs/`: architecture, validation, CI, file map, hosts, this runbook, and `releases/v0.1.0.md`.
- [x] README: local and post-publication install routes, compatibility table, documentation table.
- [x] Tests for release notes, workflows, file map and ignore rules.
- [x] After publication: `homepage` and `repository` in `plugin.json`, CI and license badges in README, and a test that the URLs match the release guard.
- [x] After the first release: a release badge in README.
- [x] Optional: responsive README banner SVGs, as in `cross-agent-handoff/docs/assets/`.

### 2. Local validation

- [x] `python3 -m unittest discover -s tests -v`.
- [x] Whitespace check (`git diff --check` once Git exists).
- [x] `claude plugin validate .`.
- [x] Plugin loading without installation: `claude --plugin-dir . plugin details game-design-skill`.
- [x] Claude Code model session with the plugin loaded, and direct skill discovery from `.claude/skills/` in a disposable project. Initially blocked by an expired CLI sign-in; done after the maintainer signed in. See `docs/evidence/host-checks-2026-11-03.md`.
- [x] Live trial in Codex with native discovery from `.agents/skills/`, recorded in `docs/examples/` and `docs/evidence/`.

Results and limits are recorded in [validation.md](validation.md).

### 3. Repository (maintainer)

- [x] `git init -b main`, review `git status`, first commit.
- [x] Create the GitHub repository with the chosen visibility and push `main`. Never force-push. Done by the maintainer; the agent session's permission guard refused to create a public repository.
- [x] Set topics: `agent-skills`, `claude-code`, `codex`, `game-design`, `ai-agents`.
- [x] Inspect the first hosted Package checks run and fix actual failures. [Run 41560385711](https://github.com/kristianrolando/game-design-skill/actions/runs/41560385711): all four jobs passed.

### 4. Release (maintainer)

- [x] In a disposable project, verify the public routes: `/plugin marketplace add kristianrolando/game-design-skill` and `npx skills add kristianrolando/game-design-skill --skill game-design-skill`. See [public-routes-2026-11-03.md](evidence/public-routes-2026-11-03.md).
- [x] Push tag `v0.1.0` on the verified commit. The release workflow checks the tag against `plugin.json`, requires `docs/releases/v0.1.0.md`, runs the tests and creates the GitHub Release. [Run 41561103985](https://github.com/kristianrolando/game-design-skill/actions/runs/41561103985) passed.
- [x] Record the repository, CI run and release links in HANDOFF.md, validation.md and this file.

### Still open

Nothing in this checklist. Further work (real-project trials, untested lenses, more hosts) is quality work, not publication.

### Next version: v0.1.1

- [x] Tighten the Deliverable rule in SKILL.md, bump `plugin.json` to 0.1.1, add `docs/releases/v0.1.1.md` and its file-map row.
- [x] Codex regression and baseline runs recorded in [regression-v0.1.1-2026-11-03.md](evidence/regression-v0.1.1-2026-11-03.md); validation.md updated.
- [x] Claude Code reruns of the Gravekeeper's Garden diagnose input after the session limit reset: two under v0.1.1 and a v0.1.0 baseline, none with a Deliverable section. The baseline did not reproduce the deviation, so the evidence shows no regression rather than proof of the fix.
- [x] **(maintainer)** Pushed main; [hosted CI](https://github.com/kristianrolando/game-design-skill/actions/runs/41590763914) passed on all four jobs for `35b6daa`. Pushed annotated tag `v0.1.1` on that commit; [release workflow](https://github.com/kristianrolando/game-design-skill/actions/runs/41590841216) passed checks and publish.
- [x] After publication: README release badge, publication status above, HANDOFF.md and validation.md updated.

### Next version: v0.1.2

- [x] Require the full report around the artifact for develop requests in SKILL.md, bump `plugin.json` to 0.1.2, add `docs/releases/v0.1.2.md` and its file-map row.
- [x] Regression runs recorded in [regression-v0.1.2-2026-11-03.md](evidence/regression-v0.1.2-2026-11-03.md): three Codex develop runs kept the full report, one Claude Code develop run kept it, and both diagnose runs left Deliverable out; validation.md updated.
- [x] **(maintainer)** Pushed main; [hosted CI](https://github.com/kristianrolando/game-design-skill/actions/runs/41601006450) passed on all four jobs for `328d11b`. Pushed annotated tag `v0.1.2` on that commit; [release workflow](https://github.com/kristianrolando/game-design-skill/actions/runs/41601696343) passed checks and publish.
- [x] After publication: README release badge, publication status above, HANDOFF.md and validation.md updated.

### 5. Workspace

- [x] Add the repository URL to the `game-design-skill/` row in the workspace `AGENTS.md`.

## Release workflow

`release.yml` runs only on a pushed `v*` tag or a manual dispatch naming the tag. It validates that the tag is `v` plus the `plugin.json` version and that matching notes exist, runs the test suite and the whitespace check, then publishes with the built-in token. Only the publish job has write permission, and it runs only in the planned repository. An existing release is left unchanged.

For each new version: update `plugin.json`, add `docs/releases/vX.Y.Z.md`, run the checks, then tag. Never move or reuse a published tag.
