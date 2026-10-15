# Project Instructions

## Project Overview

Python SDK for the CentralNic Reseller (fka RRPProxy) backend API, successor to the
deprecated Hexonet Python SDK, published to PyPI. Node is present only for the release
tooling, never for product code.

- **Language / runtime:** Python (3.14 in the devcontainer), built with setuptools from
  `pyproject.toml`
- **Package name:** `centralnicreseller.apiconnector`, source in `centralnicreseller/apiconnector/`
- **Default branch:** `master`

## Architecture

- **The version string is written by the release** in `pyproject.toml`,
  `centralnicreseller/apiconnector/__init__.py` (`__version__`) and `apiclient.py`
  (`getVersion()`) — do not edit any of the three by hand.
- **`docs/` is generated pdoc HTML** from `./scripts/documentation.sh` — nothing in the
  release regenerates it (`.releaserc.json` runs only `./scripts/createdistribution.sh`), so
  run the script by hand and commit the result separately; never hand-edit it.
- **`htmlcov/` is release-owned output** — a `@semantic-release/git` asset, tracked despite
  `.gitignore`. `./scripts/coverage.sh` rewrites it, so running the tests locally dirties
  tracked files.
- **`requirements.txt` is generated and git-ignored** — `.devcontainer/post-create.sh`
  compiles it from `pyproject.toml` with `pip-compile`; declare dependencies in
  `pyproject.toml` only.

## Coding Standards

- **Formatting:** Black (`black` in `pyproject.toml`, `ms-python.black-formatter` in the
  devcontainer).
- CI's super-linter Black check filters on `/hexonet/*|/scripts/*|updateVersion.sh|setup.py`,
  which does not match `centralnicreseller/` — run `black` yourself rather than relying on CI.

## Testing

- **Framework:** pytest with pytest-cov, config `[tool.pytest.ini_options]` in
  `pyproject.toml` (`testpaths = ["tests/"]`), coverage config `.coveragerc`.
- **No real API calls in unit tests.** `tests/test_apiclient.py` replaces `urlopen` in
  `centralnicreseller.apiconnector.apiclient` via `monkeypatch` and answers from
  `ResponseTemplateManager.addTemplate(...)` templates.
- `tests/app.py` is the demo, not a test — it calls the live OT&E API with `CNR_TEST_USER` /
  `CNR_TEST_PASSWORD`.

### Running tests

```sh
./scripts/coverage.sh   # pytest + HTML coverage into htmlcov/ — what CI runs
pnpm run test-demo      # python ./tests/app.py — live OT&E API, needs credentials
```

## Build, CI & Policies

- **CI** delegates to
  [rtldev-middleware-shareable-workflows](https://github.com/centralnicgroup-opensource/rtldev-middleware-shareable-workflows)
  (`python-sdk-test.yml` on pull requests, `python-sdk-release.yml` on push to `master`). Do
  not reimplement them in this repository's workflow stubs.
- **CI Python matrix** comes from the `RTLDEV_MW_CI_PYTHON_MATRIX` organisation variable,
  not from this repository.
- **Releases:** semantic-release (`.releaserc.json`) builds the sdist with
  `./scripts/createdistribution.sh`, uploads it with `./scripts/uploaddistribution_live.sh`,
  writes the changelog to `HISTORY.md` and commits it back to `master`.
- **Lockfiles:** `pnpm-lock.yaml` is committed deliberately; `package-lock.json` is
  git-ignored — pnpm only.
- **Supply chain:** `minimumReleaseAge: 1440` in `pnpm-workspace.yaml` is enforced
  workspace-wide — wait out a red build rather than lowering it.
- **Devcontainer:** the frame is in `.devcontainer/`; the shared behaviour comes from the
  `devbase` devcontainer Feature (`devbase:2`) and Python from the `python` Feature. Never
  fork devbase's scripts here — repository-specific setup goes in
  `.devcontainer/post-create.sh`.
- **Runtime version policy:** Node `engines` and `devEngines.packageManager` (pnpm
  `^11.0.0`) in `package.json` cover the release tooling.

## Git Conventions

- **Commit messages:** Conventional Commits with **mandatory scope** —
  `<type>(<scope>): <summary>`. Never append a `Co-Authored-By:` trailer.
- **Commit type selection:** `fix`/`feat` are reserved for source changes — they trigger a
  release. Everything else uses a non-releasing type: `ci` (workflows, devcontainer),
  `build` (build tooling), `chore`, `docs`, `test`, `refactor`.
- **Breaking changes:** add `BREAKING CHANGE: <summary>` to the commit body after a blank
  line, and document the consumer upgrade path in the same change.
- **Branch creation:** before creating a branch, and again after any PR merges,
  run `git checkout master && git pull --ff-only` first — it brings in the
  merged commits and their release tags. Never branch from a stale local
  `master`, from `origin/master` (it becomes the new branch's upstream) or from
  another feature branch.
- **Branch naming:** prefix with the Jira issue ID — `RSRMID-1234-short-description`.
- **Pull requests:** include the Jira issue link in the description; after opening, add the
  PR URL as a comment on the Jira issue.
- **Merging:** rebase-merge (`gh pr merge --rebase`). Squash merges are disabled at the
  repository level.

## Atlassian / JIRA

Work is tracked in **Jira Cloud**, project `RSRMID` — not GitHub Issues. Load the
`jira-conventions` skill before creating, editing or transitioning an issue: it carries the
required fields, this repository's title prefix and component, and the worklog rule for Done and Cancelled.

Two of its rules apply whether or not the skill is loaded:

- Write every Jira issue key as a link to the issue, never bare:
  `[RSRMID-1234](https://centralnic.atlassian.net/browse/RSRMID-1234)`.
  Branch names and commit messages keep the bare key.
- Once an issue's last pull request has merged and its worklog is in, close it
  without asking if nothing is left — the skill lists what counts.

## Do NOT

- Add dependencies without explicit request
- Add `Co-Authored-By:` trailers to commit messages
- Fork the `devbase` devcontainer Feature's scripts into this repository
- Hand-edit `HISTORY.md`, `docs/` or any of the three version strings — the release and
  `./scripts/documentation.sh` own them
- Commit a locally generated `htmlcov/` — the release commits it
- Commit `.env` or display its contents — it is git-ignored for local environment variables
  such as credentials
