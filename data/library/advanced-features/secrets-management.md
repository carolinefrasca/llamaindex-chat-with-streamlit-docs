---
title: Secrets management
slug: /library/advanced-features/secrets-management
---

# Secrets management

Storing unencrypted secrets in a git repository is a bad practice. For applications that require access to sensitive credentials, the recommended solution is to store those credentials outside the repository - such as using a credentials file not committed to the repository or passing them as environment variables.

Streamlit provides native file-based secrets management to easily store and securely access your secrets in your Streamlit app.

<Note>

Existing secrets management tools, such as [dotenv files](https://pypi.org/project/python-dotenv/), [AWS credentials files](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html#configuring-credentials), [Google Cloud Secret Manager](https://pypi.org/project/google-cloud-secret-manager/), or [Hashicorp Vault](https://www.vaultproject.io/use-cases/secrets-management), will work fine in Streamlit. We just add native secrets management for times when it's useful.

</Note>

## How to use secrets management

### Develop locally and set up secrets

Streamlit provides two ways to set up secrets locally using [TOML](https://toml.io/en/latest) format:

1. In a **global secrets file** at `~/.streamlit/secrets.toml` for macOS/Linux or `%userprofile%/.streamlit/secrets.toml` for Windows:

   ```toml
   # Everything in this section will be available as an environment variable
   db_username = "Jane"
   db_password = "mypassword"

   # You can also add other sections if you like.
   # The contents of sections as shown below will not become environment variables,
   # but they'll be easily accessible from within Streamlit anyway as we show
   # later in this doc.
   [my_other_secrets]
   things_i_like = ["Streamlit", "Python"]
   ```

   If you use the global secrets file, you don't have to duplicate secrets across several project-level files if multiple Streamlit apps share the same secrets.

2. In a **per-project secrets file** at `$CWD/.streamlit/secrets.toml`, where `$CWD` is the folder you're running Streamlit from. If both a global secrets file and a per-project secrets file exist, _secrets in the per-project file overwrite those defined in the global file_.

<Important>

Add this file to your `.gitignore` so you don't commit your secrets!

</Important>

### Use secrets in your app

Access your secrets by querying the `st.secrets` dict, or as environment variables. For example, if you enter the secrets from the section above, the code below shows you how to access them within your Streamlit app.

```python
import streamlit as st

# Everything is accessible via the st.secrets dict:

st.write("DB username:", st.secrets["db_username"])
st.write("DB password:", st.secrets["db_password"])

# And the root-level secrets are also accessible as environment variables:

import os

st.write(
    "Has environment variables been set:",
    os.environ["db_username"] == st.secrets["db_username"],
)
```

<Tip>

You can access `st.secrets` via attribute notation (e.g. `st.secrets.key`), in addition to key notation (e.g. `st.secrets["key"]`) — like [st.session_state](/library/api-reference/session-state).

</Tip>

You can even compactly use TOML sections to pass multiple secrets as a single attribute. Consider the following secrets:

```toml
[db_credentials]
username = "my_username"
password = "my_password"
```

Rather than passing each secret as attributes in a function, you can more compactly pass the section to achieve the same result. See the notional code below, which uses the secrets above:

```python
# Verbose version
my_db.connect(username=st.secrets.db_credentials.username, password=st.secrets.db_credentials.password)

# Far more compact version!
my_db.connect(**st.secrets.db_credentials)
```

### Error handling

Here are some common errors you might encounter when using secrets management.

- If a `.streamlit/secrets.toml` is created _while_ the app is running, the server needs to be restarted for changes to be reflected in the app.
- If you try accessing a secret, but no `secrets.toml` file exists, Streamlit will raise a `FileNotFoundError` exception:
  <Image alt="Secrets management FileNotFoundError" src="/images/secrets-filenotfounderror.png" clean />
- If you try accessing a secret that doesn't exist, Streamlit will raise a `KeyError` exception:

  ```python
  import streamlit as st

  st.write(st.secrets["nonexistent_key"])
  ```

    <Image alt="Secrets management KeyError" src="/images/secrets-keyerror.png" clean />

### Use secrets on Streamlit Community Cloud

When you deploy your app to [Streamlit Community Cloud](https://streamlit.io/cloud), you can use the same secrets management workflow as you would locally. However, you'll need to also set up your secrets in the Community Cloud Secrets Management console. Learn how to do so via the Cloud-specific [Secrets management](/streamlit-community-cloud/deploy-your-app/secrets-management) documentation.
