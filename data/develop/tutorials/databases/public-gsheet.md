---
title: Connect Streamlit to a public Google Sheet
slug: /develop/tutorials/databases/public-gsheet
---

# Connect Streamlit to a public Google Sheet

## Introduction

This guide explains how to securely access a public Google Sheet from Streamlit. It uses [st.connection](/develop/api-reference/connections/st.connection), [Streamlit GSheetsConnection](https://github.com/streamlit/gsheets-connection), and Streamlit's [Secrets management](/develop/concepts/connections/secrets-management).

This method requires you to enable link sharing for your Google Sheet. While the sharing link will not appear in your code (and actually acts as sort of a password!), someone with the link can get all the data in the Sheet. If you don't want this, follow the (more complicated) guide to [Connect Streamlit to a private Google Sheet](private-gsheet).

### Prerequisites

This tutorial requires `streamlit>=1.28` and `st-gsheets-connection` in your Python environment.

## Create a Google Sheet and turn on link sharing

If you already have a Sheet that you want to access, feel free to [skip to the next step](#add-the-sheets-url-to-your-local-app-secrets). See Google's documentation on how to [share spreadsheets](https://support.google.com/docs/answer/9331169?hl=en#6.1) for more information.

Create a spreadsheet with this example data and create a share link. The link should have "Anyone with the link" set as a "Viewer."

<div style={{ maxWidth: '200px', margin: 'auto' }}>

| name   | pet  |
| :----- | :--- |
| Mary   | dog  |
| John   | cat  |
| Robert | bird |

</div>

<Flex>
<Image alt="screenshot 1" src="/images/databases/public-gsheet-1.png" />
<Image alt="screenshot 1" src="/images/databases/public-gsheet-2.png" />
</Flex>

## Add the Sheets URL to your local app secrets

Your local Streamlit app will read secrets from a file `.streamlit/secrets.toml` in your app's root directory. Create this file if it doesn't exist yet and add the share link of your Google Sheet to it as shown below:

```toml
# .streamlit/secrets.toml
[connections.gsheets]
spreadsheet = "https://docs.google.com/spreadsheets/d/xxxxxxx/edit#gid=0"
```

<Important>

Add this file to `.gitignore` and don't commit it to your GitHub repo!

</Important>

## Write your Streamlit app

Copy the code below to your Streamlit app and run it.

```python
# streamlit_app.py

import streamlit as st
from streamlit_gsheets import GSheetsConnection

# Create a connection object.
conn = st.connection("gsheets", type=GSheetsConnection)

df = conn.read()

# Print results.
for row in df.itertuples():
    st.write(f"{row.name} has a :{row.pet}:")
```

See `st.connection` above? This handles secrets retrieval, setup, query caching and retries. By default, `.read()` results are cached without expiring. You can pass optional parameters to `.read()` to customize your connection. For example, you can specify the name of a worksheet, cache expiration time, or pass-through parameters for [`pandas.read_csv`](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html) like this:

```python
df = conn.read(
    worksheet="Sheet1",
    ttl="10m",
    usecols=[0, 1],
    nrows=3,
)
```

In this case, we set `ttl="10m"` to ensure the query result is cached for no longer than 10 minutes. You can also set `ttl=0` to disable caching. Learn more in [Caching](/develop/concepts/architecture/caching). We've declared optional parameters `usecols=[0,1]` and `nrows=3` for `pandas` to use under the hood.

If everything worked out (and you used the example table we created above), your app should look like this:

![Finished app screenshot](/images/databases/streamlit-app.png)

## Connecting to a Google Sheet from Community Cloud

This tutorial assumes a local Streamlit app, however you can also connect to Google Sheets from apps hosted in Community Cloud. The main additional steps are:

- [Include information about dependencies](/deploy/streamlit-community-cloud/deploy-your-app/app-dependencies) using a `requirements.txt` file with `st-gsheets-connection` and any other dependencies.
- [Add your secrets](/deploy/streamlit-community-cloud/deploy-your-app/secrets-management#deploy-an-app-and-set-up-secrets) to your Community Cloud app.
