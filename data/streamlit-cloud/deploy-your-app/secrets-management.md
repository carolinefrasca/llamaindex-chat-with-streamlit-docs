---
title: Secrets management
slug: /streamlit-community-cloud/deploy-your-app/secrets-management
---

# Secrets management

## Introduction

If you are [connecting to data sources](/knowledge-base/tutorials/databases), you will likely need to handle credentials or secrets. It's generally considered bad practice to store unencrypted secrets in a git repository. If your application needs access to sensitive credentials the recommended solution is to store those credentials in a file that is not committed to the repository and to pass them as environment variables.

Secrets management allows you to store secrets securely and access them in your Streamlit app as environment variables.

## How to use Secrets Management

### Deploy an app and set up secrets

1. From your worksapce at <a href="https://share.streamlit.io" target="_blank">share.streamlit.io</a>, click "**New app**".
2. Fill out your app's information and click "**Advanced settings...**"

   ![Access advanced settings when deploying your app](/images/streamlit-community-cloud/deploy-an-app-advanced-settings.png)

3. A modal will appear with an input box for your secrets.

   ![Save your secrets in advanced settings when deploying your app](/images/streamlit-community-cloud/deploy-an-app-advanced.png)

4. Provide your secrets in the "Secrets" field using <a href="https://toml.io/en/latest" target="_blank">TOML</a> format. For example:

   ```toml
   # Everything in this section will be available as an environment variable
   db_username = "Jane"
   db_password = "12345qwerty"

   # You can also add other sections if you like.
   # The contents of sections as shown below will not become environment
   # variables, but they'll be easily accessible from within Streamlit anyway
   # as we show later in this doc.
   [my_cool_secrets]
   things_i_like = ["Streamlit", "Python"]
   ```

### Use secrets in your app

Access your secrets as environment variables or by querying the `st.secrets` dict. For example, if you enter the secrets from the section above, the code below shows you how you can access them within your Streamlit app.

```python
import streamlit as st
import os

# Everything is accessible via the st.secrets dict:
st.write("DB username:", st.secrets["db_username"])
st.write("DB password:", st.secrets["db_password"])
st.write("My cool secrets:", st.secrets["my_cool_secrets"]["things_i_like"])

# And the root-level secrets are also accessible as environment variables:
st.write(
    "Has environment variables been set:",
    os.environ["db_username"] == st.secrets["db_username"],
)
```

<Tip>

You can access `st.secrets` via attribute notation (e.g. `st.secrets.key`) or key notation (e.g. `st.secrets["key"]`) &mdash; just like [`st.session_state`](/library/api-reference/session-state).

</Tip>

You can even use TOML sections to compactly pass multiple secrets as a single attribute.

Consider the following secrets:

```toml
[db_credentials]
username = "my_username"
password = "my_password"
```

Rather than passing each secret as attributes in a function, you can more compactly pass the section to achieve the same result. You can use Python's unpacking notation like the following example which uses the secrets above:

```python
# Verbose version
my_db.connect(username=st.secrets.db_credentials.username, password=st.secrets.db_credentials.password)

# Far more compact version!
my_db.connect(**st.secrets.db_credentials)
```

### Edit your app's secrets

If you need to add or edit your secrets for an app that is already deployed, you can accesss advanced setting from your admin panel.

1. Go to <a href="https://share.streamlit.io" target="_blank">share.streamlit.io</a>.
2. Click the overflow menu icon (<i style={{ verticalAlign: "-.25em" }} className={{ class: "material-icons-sharp" }}>more_vert</i>) for your app.
3. Click "**Settings**".
   ![Access your app settings from your workspace](/images/streamlit-community-cloud/workspace-app-settings.png)
3. A modal will appear. Click "**Secrets**"  on the left.
   ![Access your secrets through your app settings](/images/streamlit-community-cloud/workspace-app-settings-secrets.png)
4. After you edit your secrets, click "**Save**". It might take a minute for the update to be propagated to your app, but the new values will be reflected when the app re-runs.

### Develop locally with secrets

When developing your app locally, add a file called `secrets.toml` in a folder called `.streamlit` at the root of your app repo, and copy/paste your secrets into that file. Further instructions are available in the Streamlit library [Secrets management](/library/advanced-features/secrets-management) documentation.

<Important>

Be sure to add this file to your `.gitignore` so you don't commit your secrets!

</Important>

```bash
your-LOCAL-repository/
├── .streamlit/
│   ├── config.toml
│   └── secrets.toml # Make sure to gitignore this!
├── your_app.py
└── requirements.txt
```
