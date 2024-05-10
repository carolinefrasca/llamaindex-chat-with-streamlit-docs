---
title: Automate your tests with CI
slug: /develop/concepts/app-testing/automate-tests
---

# Automate your tests with CI

One of the key benefits of app testing is that tests can be automated using Continuous Integration (CI). By running tests automatically during development, you can validate that changes to your app don't break existing functionality. You can verify app code as you commit, catch bugs early, and prevent accidental breaks before deployment.

There are many popular CI tools, including GitHub Actions, Jenkins, GitLab CI, Azure DevOps, and Circle CI. Streamlit app testing will integrate easily with any of them similar to any other Python tests.

## GitHub Actions

Since many Streamlit apps (and all Community Cloud apps) are built in GitHub, this page uses examples from [GitHub Actions](https://docs.github.com/en/actions). For more information about GitHub Actions, see:

- [Quickstart for GitHub Actions](https://docs.github.com/en/actions/quickstart)
- [GitHub Actions: About continuous integration](https://docs.github.com/en/actions/automating-builds-and-tests/about-continuous-integration)
- [GitHub Actions: Build & test Python](https://docs.github.com/en/actions/automating-builds-and-tests/building-and-testing-python)

## Streamlit App Action

[Streamlit App Action](https://github.com/marketplace/actions/streamlit-app-action) provides an easy way to add automated testing to your app repository in GitHub. It also includes basic smoke testing for each page of your app without you writing any test code.

To install Streamlit App Action, add a workflow `.yml` file to your repository's `.github/workflows/` folder. For example:

```yaml
# .github/workflows/streamlit-app.yml
name: Streamlit app

on:
  push:
    branches: ["main"]
  pull_request:
    branches: ["main"]

permissions:
  contents: read

jobs:
  streamlit:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.11"
      - uses: streamlit/streamlit-app-action@v0.0.3
        with:
          app-path: streamlit_app.py
```

Let's take a look in more detail at what this action workflow is doing.

### Triggering the workflow

```yaml
on:
  push:
    branches: ["main"]
  pull_request:
    branches: ["main"]
```

This workflow will be triggered and execute tests on pull requests targeting the `main` branch, as well as any new commits pushed to the `main` branch. Note that it will also execute the tests on subsequent commits to any open pull requests. See [GitHub Actions: Triggering a workflow](https://docs.github.com/en/actions/using-workflows/triggering-a-workflow) for more information and examples.

### Setting up the test environment

```yaml
jobs:
  streamlit:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.11"
```

The workflow has a `streamlit` job that executes a series of steps. The job runs on a Docker container with the `ubuntu-latest` image.

- `actions/checkout@v4` checks out the current repository code from GitHub and copies the code to the job environment.
- `actions/setup-python@v5` installs Python version 3.11.

### Running the app tests

```yaml
- uses: streamlit/streamlit-app-action@v0.0.3
  with:
    app-path: streamlit_app.py
```

Streamlit App Action does the following:

- Install `pytest` and install any dependencies specified in `requirements.txt`.
- Run the built-in app smoke tests.
- Run any other Python tests found in the repository.

<Tip>

If your app doesn't include `requirements.txt` in the repository root directory, you will need to add a step to install dependencies with your chosen package manager before running Streamlit App Action.

</Tip>

The built-in smoke tests have the following behavior:

- Run the app specified at `app-path` as an AppTest.
- Validate that it completes successfully and does not result in an uncaught exception.
- Do the same for any additional `pages/` of the app relative to `app-path`.

If you want to run Streamlit App Action without the smoke tests, you can set `skip-smoke: true`.

### Linting your app code

Linting is the automated checking of source code for programmatic and stylistic errors. This is done by using a lint tool (otherwise known as a linter). Linting is important to reduce errors and improve the overall quality of your code, especially for repositories with multiple developers or public repositories.

You can add automated linting with [Ruff](https://docs.astral.sh/ruff/) by passing `ruff: true` to Streamlit App Action.

```yaml
- uses: streamlit/streamlit-app-action@v0.0.3
  with:
    app-path: streamlit_app.py
    ruff: true
```

<Tip>

You may want to add a pre-commit hook like [ruff-pre-commit](https://github.com/astral-sh/ruff-pre-commit) in your local development environment to fix linting errors before they get to CI.

</Tip>

### Viewing results

If tests fail, the CI workflow will fail and you will see the results in GitHub. Console logs are available by clicking into the workflow run [as described here](https://docs.github.com/en/actions/using-workflows/about-workflows#viewing-the-activity-for-a-workflow-run).

![](/images/test-results-logs.png)

For higher-level test results, you can use [pytest-results-action](https://github.com/marketplace/actions/pytest-results-actions). You can combine this with Streamlit App Action as follows:

```yaml
# ... setup as above ...
- uses: streamlit/streamlit-app-action@v0.0.3
  with:
    app-path: streamlit_app.py
    # Add pytest-args to output junit xml
    pytest-args: -v --junit-xml=test-results.xml
- if: always()
  uses: pmeier/pytest-results-action@v0.6.0
  with:
    path: test-results.xml
    summary: true
    display-options: fEX
```

![](/images/test-results-summary.png)

## Writing your own actions

The above is just provided as an example. Streamlit App Action is a quick way to get started. Once you learn the basics of your CI tool of choice, it's easy to build and customize your own automated workflows. This is a great way to improve your overall productivity as a developer and the quality of your apps.

## Working example

As a final working example example, take a look at our [`streamlit/llm-examples` Actions](https://github.com/streamlit/llm-examples/actions), defined in [this workflow file](https://github.com/streamlit/llm-examples/blob/main/.github/workflows/app-testing.yml).
