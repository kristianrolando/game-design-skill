# Publishing and releases

## Publication status

Not published. The folder is not yet a Git repository, nothing is installed globally, and no tag or release exists. The planned public repository is `kristianrolando/game-design-skill`; change it everywhere listed in step 0 if a different name is chosen.

## Publication checklist

Steps marked **(maintainer)** need an explicit decision or approval from the maintainer. The others can be done locally without pushing anything.

### 0. Decisions (maintainer)

- [ ] Confirm the repository name and visibility. Default: public `kristianrolando/game-design-skill`. The name appears in `.github/workflows/release.yml` (publish guard), README install routes and, after publication, `plugin.json`.
- [ ] Confirm the first release version. Default: `v0.1.0`, matching `plugin.json`.
- [ ] Confirm the marketplace. Default: a separate `game-design-tools` catalog, not merged with `cross-agent-tools`.
- [ ] Confirm which hosts README claims. Default: documented routes for the hosts in [hosts.md](hosts.md), with live evidence recorded only where a trial actually ran.

### 1. Repository files (local)

- [x] `.gitignore`, `CONTRIBUTING.md`, `.github/pull_request_template.md`.
- [x] `.github/workflows/ci.yml` (four-job matrix) and `.github/workflows/release.yml` (tag, version and notes checks before publishing).
- [x] `docs/`: architecture, validation, CI, file map, hosts, this runbook, and `releases/v0.1.0.md`.
- [x] README: local and post-publication install routes, compatibility table, documentation table.
- [x] Tests for release notes, workflows, file map and ignore rules.
- [ ] After publication: add `homepage` and `repository` to `plugin.json`, add CI, license and release badges to README, and add a test that the URLs match.
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

- [ ] `git init -b main`, review `git status`, first commit.
- [ ] Create the GitHub repository with the chosen visibility and push `main`. Never force-push.
- [ ] Set topics: `agent-skills`, `claude-code`, `codex`, `game-design`, `ai-agents`.
- [ ] Inspect the first hosted Package checks run and fix actual failures.

### 4. Release (maintainer)

- [ ] In a disposable project, verify the public routes: `/plugin marketplace add kristianrolando/game-design-skill` and `npx skills add kristianrolando/game-design-skill --skill game-design-skill`.
- [ ] Push tag `v0.1.0` on the verified commit. The release workflow checks the tag against `plugin.json`, requires `docs/releases/v0.1.0.md`, runs the tests and creates the GitHub Release.
- [ ] Record the repository, CI run and release links in HANDOFF.md, validation.md and this file.

### 5. Workspace

- [ ] Add the repository URL to the `game-design-skill/` row in the workspace `AGENTS.md`.

## Release workflow

`release.yml` runs only on a pushed `v*` tag or a manual dispatch naming the tag. It validates that the tag is `v` plus the `plugin.json` version and that matching notes exist, runs the test suite and the whitespace check, then publishes with the built-in token. Only the publish job has write permission, and it runs only in the planned repository. An existing release is left unchanged.

For each new version: update `plugin.json`, add `docs/releases/vX.Y.Z.md`, run the checks, then tag. Never move or reuse a published tag.
