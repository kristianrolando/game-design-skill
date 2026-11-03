# Automated checks

The GitHub Actions workflow at `.github/workflows/ci.yml` runs on pushes, pull requests and manual dispatch, with read-only permissions, no persisted checkout credentials, cancellation of superseded runs, and a ten-minute timeout per job. It has not run yet because the repository is not published.

## Matrix

| Runner | Python | Purpose |
| --- | --- | --- |
| ubuntu-latest | 3.9 | Oldest supported Python for the test suite |
| ubuntu-latest | 3.13 | Newer Python on Linux |
| macos-latest | 3.13 | macOS filesystem behavior |
| windows-latest | 3.13 | Windows paths and line endings |

## Scope

The suite checks skill frontmatter, lens routing and links, the six lens sections, reading budgets, the report template and recorded examples, host-neutral wording, absence of personal paths and keys, plugin and marketplace manifests, license copies, contributor entrypoints, release notes for the manifest version, workflow presence, the file map and ignore rules. The whitespace step compares the committed tree with Git's empty tree, because a plain `git diff --check` has nothing to compare on a fresh checkout.

The overlap test against the reference bundle is skipped in CI, because the bundle lives outside this repository and must not be committed. Run the suite locally inside the workspace to exercise it.

CI does not establish model compliance, host discovery, report quality, or remote link availability. Native plugin validation can be run locally with `claude plugin validate .`.

## Local equivalent

```sh
python3 -m unittest discover -s tests -v
git diff --check
```
