# Publishing and releases

## Publication status

Public repository: [kristianrolando/game-design-skill](https://github.com/kristianrolando/game-design-skill), created and first pushed by the maintainer on 2026-11-03.
Latest release: [v0.1.0](https://github.com/kristianrolando/game-design-skill/releases/tag/v0.1.0) ([notes](releases/v0.1.0.md)), annotated tag on verified commit `9c9c2b1c9af82920e063d75be632f04e45286201`. Keep the tag frozen there; later documentation updates go on main without moving it. If the repository is ever renamed, update the names listed in step 0.

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
- [ ] Optional: responsive README banner SVGs, as in `cross-agent-handoff/docs/assets/`.

### 2. Local validation

- [x] `python3 -m unittest discover -s tests -v`.
- [x] Whitespace check (`git diff --check` once Git exists).
- [x] `claude plugin validate .`.
- [x] Plugin loading without installation: `claude --plugin-dir . plugin details game-design-skill`.
- [ ] Claude Code model session with the plugin loaded, and direct skill discovery from `.claude/skills/` in a disposable project. **Blocked**: the Claude Code CLI sign-in has expired; the maintainer must sign in again, then rerun the commands in `docs/evidence/host-checks-2026-11-03.md`.
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

- [ ] Claude Code model session with the plugin, and direct skill discovery from `.claude/skills/` (blocked on CLI sign-in; see phase 2).
- [ ] Optional: responsive README banner SVGs.

### 5. Workspace

- [x] Add the repository URL to the `game-design-skill/` row in the workspace `AGENTS.md`.

## Release workflow

`release.yml` runs only on a pushed `v*` tag or a manual dispatch naming the tag. It validates that the tag is `v` plus the `plugin.json` version and that matching notes exist, runs the test suite and the whitespace check, then publishes with the built-in token. Only the publish job has write permission, and it runs only in the planned repository. An existing release is left unchanged.

For each new version: update `plugin.json`, add `docs/releases/vX.Y.Z.md`, run the checks, then tag. Never move or reuse a published tag.
