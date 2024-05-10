---
title: App testing example
slug: /develop/concepts/app-testing/examples
---

# App testing example

## Testing a login page

Let's consider a login page. In this example, `secrets.toml` is not present. We'll manually declare dummy secrets directly in the tests. To avoid [timing attacks](https://en.wikipedia.org/wiki/Timing_attack), the login script uses `hmac` to compare a user's password to the secret value as a security best practice.

### Project summary

#### Login page behavior

Before diving into the app's code, let's think about what this page is supposed to do. Whether you use test-driven development or you write unit tests after your code, it's a good idea to think about the functionality that needs to be tested. The login page should behave as follows:

- Before a user interacts with the app:
  - Their status is "unverified."
  - A password prompt is displayed.
- If a user types an incorrect password:
  - Their status is "incorrect."
  - An error message is displayed.
  - The password attempt is cleared from the input.
- If a user types a correct password:
  - Their status is "verified."
  - A confirmation message is displayed.
  - A logout button is displayed (without a login prompt).
- If a logged-in user clicks the **Log out** button:
  - Their status is "unverified."
  - A password prompt is displayed.

#### Login page project structure

```none
myproject/
├── app.py
└── tests/
    └── test_app.py
```

#### Login page Python file

The user's status mentioned in the page's specifications are encoded in `st.session_state.status`. This value is initialized at the beginning of the script as "unverified" and is updated through a callback when the password prompt receives a new entry.

```python
"""app.py"""
import streamlit as st
import hmac

st.session_state.status = st.session_state.get("status", "unverified")
st.title("My login page")


def check_password():
    if hmac.compare_digest(st.session_state.password, st.secrets.password):
        st.session_state.status = "verified"
    else:
        st.session_state.status = "incorrect"
    st.session_state.password = ""

def login_prompt():
    st.text_input("Enter password:", key="password", on_change=check_password)
    if st.session_state.status == "incorrect":
        st.warning("Incorrect password. Please try again.")

def logout():
    st.session_state.status = "unverified"

def welcome():
    st.success("Login successful.")
    st.button("Log out", on_click=logout)


if st.session_state.status != "verified":
    login_prompt()
    st.stop()
welcome()
```

#### Login page test file

These tests closely follow the app's specifications above. In each test, a dummy secret is set before running the app and proceeding with further simulations and checks.

```python
from streamlit.testing.v1 import AppTest

def test_no_interaction():
    at = AppTest.from_file("app.py")
    at.secrets["password"] = "streamlit"
    at.run()
    assert at.session_state["status"] == "unverified"
    assert len(at.text_input) == 1
    assert len(at.warning) == 0
    assert len(at.success) == 0
    assert len(at.button) == 0
    assert at.text_input[0].value == ""

def test_incorrect_password():
    at = AppTest.from_file("app.py")
    at.secrets["password"] = "streamlit"
    at.run()
    at.text_input[0].input("balloon").run()
    assert at.session_state["status"] == "incorrect"
    assert len(at.text_input) == 1
    assert len(at.warning) == 1
    assert len(at.success) == 0
    assert len(at.button) == 0
    assert at.text_input[0].value == ""
    assert "Incorrect password" in at.warning[0].value

def test_correct_password():
    at = AppTest.from_file("app.py")
    at.secrets["password"] = "streamlit"
    at.run()
    at.text_input[0].input("streamlit").run()
    assert at.session_state["status"] == "verified"
    assert len(at.text_input) == 0
    assert len(at.warning) == 0
    assert len(at.success) == 1
    assert len(at.button) == 1
    assert "Login successful" in at.success[0].value
    assert at.button[0].label == "Log out"

def test_log_out():
    at = AppTest.from_file("app.py")
    at.secrets["password"] = "streamlit"
    at.session_state["status"] = "verified"
    at.run()
    at.button[0].click().run()
    assert at.session_state["status"] == "unverified"
    assert len(at.text_input) == 1
    assert len(at.warning) == 0
    assert len(at.success) == 0
    assert len(at.button) == 0
    assert at.text_input[0].value == ""
```

See how Session State was modified in the last test? Instead of fully simulating a user logging in, the test jumps straight to a logged-in state by setting `at.session_state["status"] = "verified"`. After running the app, the test proceeds to simulate the user logging out.

### Automating your tests

If `myproject/` was pushed to GitHub as a repository, you could add GitHub Actions test automation with [Streamlit App Action](https://github.com/marketplace/actions/streamlit-app-action). This is as simple as adding a workflow file at `myproject/.github/workflows/`:

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
          app-path: app.py
```
