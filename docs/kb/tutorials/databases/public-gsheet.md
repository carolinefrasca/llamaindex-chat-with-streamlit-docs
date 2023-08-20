---
title: Connect Streamlit to a public Google Sheet
slug: /knowledge-base/tutorials/databases/public-gsheet
---

# Connect Streamlit to a public Google Sheet

## Introduction

This guide explains how to securely access a public Google Sheet from Streamlit Community Cloud. It uses the [pandas](https://pandas.pydata.org/) library and Streamlit's [Secrets management](/streamlit-community-cloud/deploy-your-app/secrets-management).

This method requires you to enable link sharing for your Google Sheet. While the sharing link will not appear in your code (and actually acts as sort of a password!), someone with the link can get all the data in the Sheet. If you don't want this, follow the (more complicated) guide [Connect Streamlit to a private Google Sheet](private-gsheet).

## Create a Google Sheet and turn on link sharing

<Note>

If you already have a Sheet that you want to access, feel free to [skip to the next
step](#add-the-sheets-url-to-your-local-app-secrets).

</Note>

<Flex>
<Image alt="screenshot 1" src="/images/databases/public-gsheet-1.png" />
<Image alt="screenshot 1" src="/images/databases/public-gsheet-2.png" />
</Flex>

## Add the Sheets URL to your local app secrets

Your local Streamlit app will read secrets from a file `.streamlit/secrets.toml` in your app's root directory. Create this file if it doesn't exist yet and add the share link of your Google Sheet to it as shown below:

```toml
# .streamlit/secrets.toml

public_gsheets_url = "https://docs.google.com/spreadsheets/d/xxxxxxx/edit#gid=0"
```

<Important>

Add this file to `.gitignore` and don't commit it to your GitHub repo!

</Important>

## Copy your app secrets to the cloud

As the `secrets.toml` file above is not committed to GitHub, you need to pass its content to your deployed app (on Streamlit Community Cloud) separately. Go to the [app dashboard](https://share.streamlit.io/) and in the app's dropdown menu, click on **Edit Secrets**. Copy the content of `secrets.toml` into the text area. More information is available at [Secrets management](/streamlit-community-cloud/deploy-your-app/secrets-management).

![Secrets manager screenshot](/images/databases/edit-secrets.png)

## Write your Streamlit app

Copy the code below to your Streamlit app and run it.

```python
# streamlit_app.py

import pandas as pd
import streamlit as st

# Read in data from the Google Sheet.
# Uses st.cache_data to only rerun when the query changes or after 10 min.
@st.cache_data(ttl=600)
def load_data(sheets_url):
    csv_url = sheets_url.replace("/edit#gid=", "/export?format=csv&gid=")
    return pd.read_csv(csv_url)

df = load_data(st.secrets["public_gsheets_url"])

# Print results.
for row in df.itertuples():
    st.write(f"{row.name} has a :{row.pet}:")
```

See `st.cache_data` above? Without it, Streamlit would run the query every time the app reruns (e.g. on a widget interaction). With `st.cache_data`, it only runs when the query changes or after 10 minutes (that's what `ttl` is for). Watch out: If your database updates more frequently, you should adapt `ttl` or remove caching so viewers always see the latest data. Learn more in [Caching](/library/advanced-features/caching).

If everything worked out (and you used the example table we created above), your app should look like this:

![Finished app screenshot](/images/databases/streamlit-app.png)
