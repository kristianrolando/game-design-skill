# File map

| Path | Purpose |
| --- | --- |
| skills/game-design-skill/SKILL.md | Router: trigger description, intake, lens table, analysis rules, ratings, report template |
| skills/game-design-skill/references/*.md | Nine lens families, each with the same six sections, loaded on demand |
| skills/game-design-skill/agents/openai.yaml | Optional Codex interface metadata; ignored by other hosts |
| skills/game-design-skill/LICENSE | MIT license that travels with a standalone copy of the skill |
| .claude-plugin/plugin.json | Claude Code plugin wrapper |
| .claude-plugin/marketplace.json | Local or Git marketplace catalog for the wrapper |
| .github/workflows/ci.yml | Package checks on Linux, macOS and Windows |
| .github/workflows/release.yml | Tag-triggered release with version and notes checks |
| .github/pull_request_template.md | Change, validation and content review template |
| .github/ISSUE_TEMPLATE/*.yml | Bug report and lens or feature request forms; blank issues off, security reports routed privately |
| tests/test_package.py | Standard-library package integrity checks |
| docs/architecture.md | Router design, lens grouping, report format and provenance decisions |
| docs/validation.md | Evidence by kind and what it does not establish |
| docs/ci.md | CI matrix and scope |
| docs/hosts.md | Installation locations and activation per host |
| docs/releasing.md | Publication checklist and release workflow |
| docs/releases/v0.1.0.md | Notes for the first release |
| docs/releases/v0.1.1.md | Notes for the Deliverable-rule fix release |
| docs/releases/v0.1.2.md | Notes for the develop-mode report fix release |
| docs/examples/*.md | Recorded model trials with their inputs and limits |
| docs/evidence/*.md | Host loading, install route and regression checks |
| docs/assets/*.svg | Editable README banner, wide and narrow layouts |
| docs/assets/social-preview.png | 1280×640 repository social preview rendered from the wide banner; uploaded by hand in repository settings |
| AGENTS.md | Canonical contributor rules for any agent |
| CLAUDE.md | Claude Code contributor adapter importing AGENTS.md |
| CONTRIBUTING.md | Shared human and agent contribution workflow |
| SECURITY.md | Supported versions and private vulnerability reporting |
| CODE_OF_CONDUCT.md | Conduct expectations and enforcement contact |
| HANDOFF.md | Current project checkpoint |
| README.md | User-facing overview, installation and credits |
| LICENSE | MIT license for the repository |
| .gitignore | Ignored local artifacts |
