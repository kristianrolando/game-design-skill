# Contributing

Humans and any filesystem-capable coding agent use the same files, rules, checks and review process. No access to another agent's conversation, account or API is required.

## Start here

1. Read AGENTS.md, then HANDOFF.md for current work and known limits.
2. Read the parts of README.md, docs/architecture.md and the skill files you plan to change.
3. Inspect Git status and diffs, including untracked files. Preserve unrelated work.
4. Keep one writer on overlapping files and on HANDOFF.md. Stop the previous writer before switching agents.
5. Work on the current authorized task. A checkpoint is context, not permission to publish or expand scope.

Claude Code loads AGENTS.md through the `@AGENTS.md` import in CLAUDE.md. For other agents, open this repository and use:

```text
Contribute to this repository. Read AGENTS.md, CONTRIBUTING.md and HANDOFF.md,
then inspect the actual changes and affected files. Continue the authorized
task, preserve existing work, run the checks, and leave an updated handoff.
Do not publish or change global settings unless the current request asks for it.
```

## Changing the skill

- **Router** (`skills/game-design-skill/SKILL.md`): keep it short enough to load on every use. Workflow, lens table, ratings and report template live here; detailed checks do not.
- **Lens files** (`skills/game-design-skill/references/`): each keeps the six sections When to use, Gather, Checks, Common problems, Fix menu, Reporting notes, in that order. A new lens family needs its file, a lens-table row in SKILL.md, a README row and an update to the expected count in the tests.
- **Wording**: write original text. The reference bundle used during design is licensed PolyForm Noncommercial 1.0.0; never copy from it. When the bundle is present at `../refrences/game-design-skills-bundle-master`, the tests reject any 10-word passage shared with it. Cite the authors of frameworks you name in README credits.
- **Host neutrality**: no tool names or features specific to one agent inside the skill folder. Host-specific metadata belongs in adapter files such as `agents/openai.yaml` and `.claude-plugin/`.
- **README artwork** (`docs/assets/`): plain SVG, edited by hand. Keep the wide and narrow files in step, keep the card's own background so it reads on light and dark themes, use system fonts, and add no scripts, embedded images or external resources. Update the README alt text when the content changes.
- **Report format**: changing section names in the template also requires updating the tests and the recorded examples, or the change is a breaking one for users who rely on the format.

## Evidence

Record model or host trials in `docs/examples/` (report outputs) or `docs/evidence/` (host loading checks), stating date, host, model, files read and limits. Never present a hand-written example as a model trial, and keep validation claims in docs/validation.md matched to what actually ran.

## Checks

```sh
python3 -m unittest discover -s tests -v
git diff --check
```

Use `python` where `python3` is unavailable. CI runs the same suite on Linux, macOS and Windows; see docs/ci.md.

## Pull requests

Use a descriptive branch and the pull request template. Releases follow docs/releasing.md and only happen on an explicit maintainer request.
