# composite-run-steps-action-template

This template can be used to quickly start a new custom composite-run-steps action repository.  Click the `Use this template` button at the top to get started.

## Index

- [Inputs](#inputs)
- [Outputs](#outputs)
- [Example](#example)
- [Contributing](#contributing)
  - [Incrementing the Version](#incrementing-the-version)
  - [Source Code Changes](#source-code-changes)
  - [Updating the README.md](#updating-the-readmemd)
- [Code of Conduct](#code-of-conduct)
- [License](#license)

## TODOs

- README.md
  - [x] Update the Inputs section with the correct action inputs
  - [x] Update the Outputs section with the correct action outputs
  - [x] Update the Example section with the correct usage
- action.yml
  - [x] Fill in the correct name, description, inputs and outputs and implement steps
- CODEOWNERS
  - [x] Update as appropriate
- Repository Settings
  - [x] On the *Options* tab check the box to *Automatically delete head branches*
  - [x] On the *Options* tab update the repository's visibility
  - [ ] On the *Branches* tab add a branch protection rule
    - [x] Check *Require pull request reviews before merging*
    - [x] Check *Dismiss stale pull request approvals when new commits are pushed*
    - [x] Check *Require review from Code Owners*
    - [x] Check *Require status checks to pass before merging*
    - [x] Check *Require branches to be up to date before merging*
    - [ ] Add `update-readme` to the list of required status checks.  This will need to be done after the first `auto-update-readme` workflow runs.
    - [x] Check *Do not allow bypassing the above settings*
  - [x] On the *Manage Access* tab add the appropriate groups
- About Section (accessed on the main page of the repo, click the gear icon to edit)
  - [x] The repo should have a short description of what it is for
  - [x] Add one of the following topic tags:
    | Topic Tag       | Usage                                    |
    | --------------- | ---------------------------------------- |
    | az              | For actions related to Azure             |
    | code            | For actions related to building code     |
    | certs           | For actions related to certificates      |
    | db              | For actions related to databases         |
    | git             | For actions related to Git               |
    | iis             | For actions related to IIS               |
    | microsoft-teams | For actions related to Microsoft Teams   |
    | svc             | For actions related to Windows Services  |
    | jira            | For actions related to Jira              |
    | meta            | For actions related to running workflows |
    | pagerduty       | For actions related to PagerDuty         |
    | test            | For actions related to testing           |
    | tf              | For actions related to Terraform         |
  - [x] Add any additional topics for an action if they apply
- Address any remaining TODOs

## Inputs

| Parameter               | Is Required | Default Value       | Description           |
| ----------------------- | ----------- | ------------------- | --------------------- |
| `name`                  | false       | artifact            | The Artifact Name |
| `path`                  | true        | N/A, required value | A file, directory, or wildcard pattern that describes what to upload |
| `if-no-files-found`     | false       | warn                | The action to take if no files are found at the path. Options are `warn`, `error`, or `info`. |
| `retention-days`        | false       | 15                  | The number of days to retain the artifact before it expires. |


## Outputs

This workflow has zero outputs.

## Example

```yml
jobs:
  job1:
    runs-on: [self-hosted, im-linux]
    steps:
      - uses: actions/checkout@v3

      - name: 'Zip and Upload Artifact'
        uses: im-open/zip-upload-artifact@v1.0.0
        with:
          name: ${{ env.CODE_COVERAGE_REPORT_NAME }}
          path: ${{ env.CODE_COVERAGE_DIR }}
```

## Contributing

When creating PRs, please review the following guidelines:

- [ ] The action code does not contain sensitive information.
- [ ] At least one of the commit messages contains the appropriate `+semver:` keywords listed under [Incrementing the Version] for major and minor increments.
- [ ] The README.md has been updated with the latest version of the action.  See [Updating the README.md] for details.

### Incrementing the Version

This repo uses [git-version-lite] in its workflows to examine commit messages to determine whether to perform a major, minor or patch increment on merge if [source code] changes have been made.  The following table provides the fragment that should be included in a commit message to active different increment strategies.

| Increment Type | Commit Message Fragment                     |
|----------------|---------------------------------------------|
| major          | +semver:breaking                            |
| major          | +semver:major                               |
| minor          | +semver:feature                             |
| minor          | +semver:minor                               |
| patch          | *default increment type, no comment needed* |

### Source Code Changes

The files and directories that are considered source code are listed in the `files-with-code` and `dirs-with-code` arguments in both the [build-and-review-pr] and [increment-version-on-merge] workflows.

If a PR contains source code changes, the README.md should be updated with the latest action version.  The [build-and-review-pr] workflow will ensure these steps are performed when they are required.  The workflow will provide instructions for completing these steps if the PR Author does not initially complete them.

If a PR consists solely of non-source code changes like changes to the `README.md` or workflows under `./.github/workflows`, version updates do not need to be performed.

### Updating the README.md

If changes are made to the action's [source code], the [usage examples] section of this file should be updated with the next version of the action.  Each instance of this action should be updated.  This helps users know what the latest tag is without having to navigate to the Tags page of the repository.  See [Incrementing the Version] for details on how to determine what the next version will be or consult the first workflow run for the PR which will also calculate the next version.

## Code of Conduct

This project has adopted the [im-open's Code of Conduct](https://github.com/im-open/.github/blob/main/CODE_OF_CONDUCT.md).

## License

Copyright &copy; 2023, Extend Health, LLC. Code released under the [MIT license](LICENSE).

[git-version-lite]: https://github.com/im-open/git-version-lite
[Incrementing the Version]: #incrementing-the-version
[Updating the README.md]: #updating-the-readmemd
[build-and-review-pr]: ./.github/workflows/build-and-review-pr.yml
[increment-version-on-merge]: ./.github/workflows/increment-version-on-merge.yml
[source code]: #source-code-changes
[usage examples]: #usage-examples
