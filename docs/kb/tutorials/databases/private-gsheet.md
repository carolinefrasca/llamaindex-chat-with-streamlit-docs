---
title: Connect Streamlit to a private Google Sheet
slug: /knowledge-base/tutorials/databases/private-gsheet
---

# Connect Streamlit to a private Google Sheet

## Introduction

This guide explains how to securely access a private Google Sheet from Streamlit Community Cloud. It uses the [gsheetsdb](https://github.com/betodealmeida/gsheets-db-api) library and Streamlit's [Secrets management](/streamlit-community-cloud/deploy-your-app/secrets-management).

If you are fine with enabling link sharing for your Google Sheet (i.e. everyone with the link can view it), the guide [Connect Streamlit to a public Google Sheet](/knowledge-base/tutorials/databases/public-gsheet) shows a simpler method of doing this. If your Sheet contains sensitive information and you cannot enable link sharing, keep on reading.

## Create a Google Sheet

<Note>

If you already have a database that you want to use, feel free
to [skip to the next step](#enable-the-sheets-api).

</Note>

![Google sheet screenshot](/images/databases/private-gsheet-1.png)

## Enable the Sheets API

Programmatic access to Google Sheets is controlled through [Google Cloud Platform](https://cloud.google.com/). Create an account or sign in and head over to the [**APIs & Services** dashboard](https://console.cloud.google.com/apis/dashboard) (select or create a project if asked). As shown below, search for the Sheets API and enable it:

<Flex>
<Image alt="GCP screenshot 1" src="/images/databases/private-gsheet-2.png" />
<Image alt="GCP screenshot 2" src="/images/databases/private-gsheet-3.png" />
<Image alt="GCP screenshot 3" src="/images/databases/private-gsheet-4.png" />
</Flex>

## Create a service account & key file

To use the Sheets API from Streamlit Community Cloud, you need a Google Cloud Platform service account (a special account type for programmatic data access). Go to the [**Service Accounts** page](https://console.cloud.google.com/iam-admin/serviceaccounts) and create an account with the **Viewer** permission (this will let the account access data but not change it):

<Flex>
<Image alt="GCP screenshot 5" src="/images/databases/private-gsheet-5.png" />
<Image alt="GCP screenshot 6" src="/images/databases/private-gsheet-6.png" />
<Image alt="GCP screenshot 7" src="/images/databases/private-gsheet-7.png" />
</Flex>

<Note>

The button **CREATE SERVICE ACCOUNT** is gray, you don't have the correct permissions. Ask the admin of your Google Cloud project for help.

</Note>

After clicking **DONE**, you should be back on the service accounts overview. First, note down the email address of the account you just created (**important for next step!**). Then, create a JSON key file for the new account and download it:

<Flex>
<Image alt="GCP screenshot 8" src="/images/databases/private-gsheet-8.png" />
<Image alt="GCP screenshot 9" src="/images/databases/private-gsheet-9.png" />
<Image alt="GCP screenshot 10" src="/images/databases/private-gsheet-10.png" />
</Flex>

## Share the Google Sheet with the service account

By default, the service account you just created cannot access your Google Sheet. To give it access, click on the **Share** button in the Google Sheet, add the email of the service account (noted down in step 2), and choose the correct permission (if you just want to read the data, **Viewer** is enough):

<Flex>
<Image alt="GCP screenshot 11" src="/images/databases/private-gsheet-11.png" />
<Image alt="GCP screenshot 12" src="/images/databases/private-gsheet-12.png" />
</Flex>

## Add the key file to your local app secrets

Your local Streamlit app will read secrets from a file `.streamlit/secrets.toml` in your app's root directory. Create this file if it doesn't exist yet and add the URL of your Google Sheet plus the content of the key file you downloaded to it as shown below:

```toml
# .streamlit/secrets.toml

private_gsheets_url = "https://docs.google.com/spreadsheets/d/12345/edit?usp=sharing"

[gcp_service_account]
type = "service_account"
project_id = "xxx"
private_key_id = "xxx"
private_key = "xxx"
client_email = "xxx"
client_id = "xxx"
auth_uri = "https://accounts.google.com/o/oauth2/auth"
token_uri = "https://oauth2.googleapis.com/token"
auth_provider_x509_cert_url = "https://www.googleapis.com/oauth2/v1/certs"
client_x509_cert_url = "xxx"
```

<Important>

Add this file to `.gitignore` and don't commit it to your GitHub repo!

</Important>

## Copy your app secrets to the cloud

As the `secrets.toml` file above is not committed to GitHub, you need to pass its content to your deployed app (on Streamlit Community Cloud) separately. Go to the [app dashboard](https://share.streamlit.io/) and in the app's dropdown menu, click on **Edit Secrets**. Copy the content of `secrets.toml` into the text area. More information is available at [Secrets management](/streamlit-community-cloud/deploy-your-app/secrets-management).

![Secrets manager screenshot](/images/databases/edit-secrets.png)

## Add gsheetsdb to your requirements file

Add the [gsheetsdb](https://github.com/betodealmeida/gsheets-db-api) package to your `requirements.txt` file, preferably pinning its version (replace `x.x.x` with the version you want installed):

```bash
# requirements.txt
gsheetsdb==x.x.x
```

## Write your Streamlit app

Copy the code below to your Streamlit app and run it.

```python
# streamlit_app.py

import streamlit as st
from google.oauth2 import service_account
from gsheetsdb import connect

# Create a connection object.
credentials = service_account.Credentials.from_service_account_info(
    st.secrets["gcp_service_account"],
    scopes=[
        "https://www.googleapis.com/auth/spreadsheets",
    ],
)
conn = connect(credentials=credentials)

# Perform SQL query on the Google Sheet.
# Uses st.cache_data to only rerun when the query changes or after 10 min.
@st.cache_data(ttl=600)
def run_query(query):
    rows = conn.execute(query, headers=1)
    rows = rows.fetchall()
    return rows

sheet_url = st.secrets["private_gsheets_url"]
rows = run_query(f'SELECT * FROM "{sheet_url}"')

# Print results.
for row in rows:
    st.write(f"{row.name} has a :{row.pet}:")
```

See `st.cache_data` above? Without it, Streamlit would run the query every time the app reruns (e.g. on a widget interaction). With `st.cache_data`, it only runs when the query changes or after 10 minutes (that's what `ttl` is for). Watch out: If your database updates more frequently, you should adapt `ttl` or remove caching so viewers always see the latest data. Learn more in [Caching](/library/advanced-features/caching).

If everything worked out (and you used the example table we created above), your app should look like this:

![Finished app screenshot](/images/databases/streamlit-app.png)
