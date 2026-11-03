# Architecture and trade-offs

## Decision

Ship one router skill, `game-design-skill`, with nine lens families as on-demand reference files. The router (SKILL.md) holds everything needed on every use: when to trigger, the intake rules, how to choose lenses, analysis rules, severity and confidence ratings, and the report template. Each lens file holds the detailed checks for one family and is read only when the router selects it.

No scripts, runtime dependencies, APIs or host features are required. The skill is plain Markdown that any agent able to read files can follow.

## Why one router instead of many skills

The reference catalog that informed the topic coverage splits game design into about sixty narrow skills. That granularity has costs for this package:

| Many narrow skills | Effect | Router decision |
| --- | --- | --- |
| Sixty descriptions compete for triggering | Hosts may pick the wrong skill or none, and every description costs context | One description that covers the whole domain |
| Overlapping lenses (flow, attribution, fairness, randomness) live in separate skills | Users must know which framework to ask for | The router maps symptoms ("feels unfair") to a lens family |
| Each skill has its own output shape | Reports from different lenses cannot be compared or combined | One report template with shared severity and confidence ratings |
| Installing and updating sixty folders | Version drift across copies | One folder, one version |

The trade-off is depth per framework: a lens family gives a compact set of checks, not a full method per framework. The lens files can grow, and a family can be split later if one becomes too long to load cheaply. The tests enforce a word budget per file to make that visible.

## Lens families

The nine families follow the categories of the reference catalog: emotional direction, player motivation, core loop and pillars, flow/fairness/failure, FTUE and retention, multiplayer and social, prototyping, pitch and GDD, scoping and budget. Related narrow topics were merged by the question they answer. For example, attribution, perceived randomness, failure loops and friction all answer "why does this feel bad to fail at", so they share one file.

Every lens file has the same six sections (When to use, Gather, Checks, Common problems, Fix menu, Reporting notes). A fixed shape makes files predictable for the model, easy to review, and testable.

## Report format

A single template keeps outputs comparable across lenses and runs:

- **Context, assumptions, lenses** make the basis of the review explicit before any judgment.
- **Confidence labels** (Observed, Inferred, Assumed) separate what the material says from what the reviewer reasons or supposes.
- **Severity** (P1 to P3) with effort (S, M, L) supports ranking by leverage.
- **Minimal fixes** each carry a cheap check, so recommendations lead to tests rather than opinions.

## Intake

Asking too many questions stalls short requests; asking none produces generic reviews. The router asks at most three questions, once, each with a default, and only when the missing context would change the lens or the conclusion. Otherwise it proceeds on stated assumptions.

## Provenance

The reference bundle is licensed PolyForm Noncommercial 1.0.0, which is incompatible with relicensing its text under MIT. It was used only to decide topic coverage and section ideas. All wording here is original, frameworks are credited to their authors in the README, and a local test rejects any 10-word passage shared with the bundle. That test is skipped where the bundle is absent, including CI, so it guards authoring rather than distribution.

## Boundaries

The skill structures expert reasoning; it does not replace playtesting, market research or production estimates from the actual team. Instructions are not enforcement: a host model can still deviate, which is why trials are recorded with their limits in docs/validation.md.
