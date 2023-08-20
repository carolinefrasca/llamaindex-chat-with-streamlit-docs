---
title: Authentication without SSO
slug: /knowledge-base/deploy/authentication-without-sso
---

# Authentication without SSO

## Introduction

Want to secure your Streamlit app with passwords, but cannot implement single sign-on? We got you covered! This guide shows you two simple techniques for adding basic authentication to your Streamlit app, using [Secrets management](/streamlit-community-cloud/deploy-your-app/secrets-management).

<Warning>

While this technique adds some level of security, it is **NOT** comparable to proper authentication with an SSO provider.

</Warning>

## Option 1: One global password for all users

This is the easiest option! Your app will ask for a password that's shared between all users. It will be stored in the app secrets using [Secrets management](/streamlit-community-cloud/deploy-your-app/secrets-management). If you want to change this password or revoke a user's access, you will need to change it for everyone. If you want to have one password per user instead, jump to [Option 2 below](/knowledge-base/deploy/authentication-without-sso#option-2-individual-password-for-each-user).

### Step 1: Add the password to your local app secrets

Your local Streamlit app will read secrets from a file `.streamlit/secrets.toml` in your app's root dir. Create this file if it doesn't exist yet and add your password to it as shown below:

```toml
# .streamlit/secrets.toml

password = "streamlit123"
```

<Important>

Be sure to add this file to your `.gitignore` so you don't commit your secrets!

</Important>

### Step 2: Copy your app secrets to the cloud

As the `secrets.toml` file above is not committed to GitHub, you need to pass its content to your deployed app (on Streamlit Community Cloud) separately. Go to the [app dashboard](https://share.streamlit.io/) and in the app's dropdown menu, click on **Edit Secrets**. Copy the content of `secrets.toml` into the text area. More information is available at [Secrets management](/streamlit-community-cloud/deploy-your-app/secrets-management).

![Secrets manager screenshot](/images/databases/edit-secrets.png)

### Step 3: Ask for the password in your Streamlit app

Copy the code below to your Streamlit app, insert your normal app code in the `if` statement at the bottom, and run it:

```python
# streamlit_app.py

import streamlit as st

def check_password():
    """Returns `True` if the user had the correct password."""

    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if st.session_state["password"] == st.secrets["password"]:
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # don't store password
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        # First run, show input for password.
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        return False
    elif not st.session_state["password_correct"]:
        # Password not correct, show input + error.
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        st.error("😕 Password incorrect")
        return False
    else:
        # Password correct.
        return True

if check_password():
    st.write("Here goes your normal Streamlit app...")
    st.button("Click me")
```

If everything worked out, your app should look like this:

![Global passwords](/images/streamlit-community-cloud/auth-without-sso-global.png)

## Option 2: Individual password for each user

This option allows you to set a username and password for each user of your app. Like in [Option 1](#option-1-one-global-password-for-all-users), both values will be stored in the app secrets using [Secrets management](/streamlit-community-cloud/deploy-your-app/secrets-management).

### Step 1: Add usernames & passwords to your local app secrets

Your local Streamlit app will read secrets from a file `.streamlit/secrets.toml` in your app's root dir. Create this file if it doesn't exist yet and add the usernames & password to it as shown below:

```toml
# .streamlit/secrets.toml

[passwords]
# Follow the rule: username = "password"
alice_foo = "streamlit123"
bob_bar = "mycrazypw"
```

<Important>

Be sure to add this file to your `.gitignore` so you don't commit your secrets!

</Important>

Alternatively, you could set up and manage usernames & passwords via a spreadsheet or database. To use secrets to securely connect to Google Sheets, AWS, and other data providers, read our tutorials on how to [Connect Streamlit to data sources](/knowledge-base/tutorials/databases).

### Step 2: Copy your app secrets to the cloud

As the `secrets.toml` file above is not committed to GitHub, you need to pass its content to your deployed app (on Streamlit Community Cloud) separately. Go to the [app dashboard](https://share.streamlit.io/) and in the app's dropdown menu, click on **Edit Secrets**. Copy the content of `secrets.toml` into the text area. More information is available at [Secrets management](/streamlit-community-cloud/deploy-your-app/secrets-management).

![Secrets manager screenshot](/images/databases/edit-secrets.png)

### Step 3: Ask for username & password in your Streamlit app

Copy the code below to your Streamlit app, insert your normal app code in the `if` statement at the bottom, and run it:

```python
# streamlit_app.py

import streamlit as st

def check_password():
    """Returns `True` if the user had a correct password."""

    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if (
            st.session_state["username"] in st.secrets["passwords"]
            and st.session_state["password"]
            == st.secrets["passwords"][st.session_state["username"]]
        ):
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # don't store username + password
            del st.session_state["username"]
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        # First run, show inputs for username + password.
        st.text_input("Username", on_change=password_entered, key="username")
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        return False
    elif not st.session_state["password_correct"]:
        # Password not correct, show input + error.
        st.text_input("Username", on_change=password_entered, key="username")
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        st.error("😕 User not known or password incorrect")
        return False
    else:
        # Password correct.
        return True

if check_password():
    st.write("Here goes your normal Streamlit app...")
    st.button("Click me")
```

If everything worked out, your app should look like this:

![Individual passwords](/images/streamlit-community-cloud/auth-without-sso-individual.png)
