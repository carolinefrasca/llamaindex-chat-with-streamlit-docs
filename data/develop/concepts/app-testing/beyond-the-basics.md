---
title: Beyond the basics of app testing
slug: /develop/concepts/app-testing/beyond-the-basics
---

# Beyond the basics of app testing

Now that you're comfortable with executing a basic test for a Streamlit app let's cover the mutable attributes of [`AppTest`](/develop/api-reference/app-testing/st.testing.v1.apptest):

- `AppTest.secrets`
- `AppTest.session_state`
- `AppTest.query_params`

You can read and update values using dict-like syntax for all three attributes. For `.secrets` and `.query_params`, you can use key notation but not attribute notation. For example, the `.secrets` attribute for `AppTest` accepts `at.secrets["my_key"]` but **_not_** `at.secrets.my_key`. This differs from how you can use the associated command in the main library. On the other hand, `.session_state` allows both key notation and attribute notation.

For these attributes, the typical pattern is to declare any values before executing the app's first run. Values can be inspected at any time in a test. There are a few extra considerations for secrets and Session State, which we'll cover now.

## Using secrets with app testing

Be careful not to include secrets directly in your tests. Consider this simple project with `pytest` executed in the project's root directory:

```none
myproject/
├── .streamlit/
│   ├── config.toml
│   └── secrets.toml
├── app.py
└── tests/
    └── test_app.py
```

```bash
cd myproject
pytest tests/
```

In the above scenario, your simulated app will have access to your `secrets.toml` file. However, since you don't want to commit your secrets to your repository, you may need to write tests where you securely pull your secrets into memory or use dummy secrets.

### Example: declaring secrets in a test

Within a test, declare each secret after initializing your `AppTest` instance but before the first run. (A missing secret may result in an app that doesn't run!) For example, consider the following secrets file and corresponding test initialization to assign the same secrets manually:

Secrets file:

```toml
db_username = "Jane"
db_password = "mypassword"

[my_other_secrets]
things_i_like = ["Streamlit", "Python"]
```

Testing file with equivalent secrets:

```python
# Initialize an AppTest instance.
at = AppTest.from_file("app.py")
# Declare the secrets.
at.secrets["db_username"] = "Jane"
at.secrets["db_password"] = "mypassword"
at.secrets["my_other_secrets.things_i_like"] = ["Streamlit", "Python"]
# Run the app.
at.run()
```

Generally, you want to avoid typing your secrets directly into your test. If you don't need your real secrets for your test, you can declare dummy secrets as in the example above. If your app uses secrets to connect to an external service like a database or API, consider mocking that service in your app tests. If you need to use the real secrets and actually connect, you should use an API to pass them securely and anonymously. If you are automating your tests with GitHub actions, check out their [Security guide](https://docs.github.com/en/actions/security-guides/using-secrets-in-github-actions).

```python
at.secrets["my_key"] = <value provided through API>
```

## Working with Session State in app testing

The `.session_state` attribute for `AppTest` lets you read and update Session State values using key notation (`at.session_state["my_key"]`) and attribute notation (`at.session_state.my_key`). By manually declaring values in Session State, you can directly jump to a specific state instead of simulating many steps to get there. Additionally, the testing framework does not provide native support for multipage apps. An instance of `AppTest` can only test one page. You must manually declare Session State values to simulate a user carrying data from another page.

### Example: testing a multipage app

Consider a simple multipage app where the first page can modify a value in Session State. To test the second page, set Session State manually and run the simulated app within the test:

Project structure:

```none
myproject/
├── pages/
│   └── second.py
├── first.py
└── tests/
    └── test_second.py
```

First app page:

```python
"""first.py"""
import streamlit as st

st.session_state.magic_word = st.session_state.get("magic_word", "Streamlit")

new_word = st.text_input("Magic word:")

if st.button("Set the magic word"):
    st.session_state.magic_word = new_word
```

Second app page:

```python
"""second.py"""
import streamlit as st

st.session_state.magic_word = st.session_state.get("magic_word", "Streamlit")

if st.session_state.magic_word == "Balloons":
    st.markdown(":balloon:")
```

Testing file:

```python
"""test_second.py"""
from streamlit.testing.v1 import AppTest

def test_balloons():
    at = AppTest.from_file("pages/second.py")
    at.session_state["magic_word"] = "Balloons"
    at.run()
    assert at.markdown[0].value == ":balloon:"
```

By setting the value `at.session_state["magic_word"] = "Balloons"` within the test, you can simulate a user navigating to `second.py` after entering and saving "Balloons" on `first.py`.
