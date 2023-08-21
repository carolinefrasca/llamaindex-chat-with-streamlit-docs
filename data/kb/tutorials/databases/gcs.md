---
title: Connect Streamlit to Google Cloud Storage
slug: /knowledge-base/tutorials/databases/gcs
---

# Connect Streamlit to Google Cloud Storage

## Introduction

This guide explains how to securely access files on Google Cloud Storage from Streamlit Community Cloud. It uses [Streamlit FilesConnection](https://github.com/streamlit/files-connection), the [gcsfs](https://github.com/fsspec/gcsfs) library and Streamlit's [Secrets management](/library/advanced-features/secrets-management).

## Create a Google Cloud Storage bucket and add a file

<Note>

If you already have a bucket that you want to use, feel free
to [skip to the next step](#enable-the-google-cloud-storage-api).

</Note>

First, [sign up for Google Cloud Platform](https://console.cloud.google.com/) or log in. Go to the [Google Cloud Storage console](https://console.cloud.google.com/storage/) and create a new bucket.

<Flex>
<Image alt="GCS screenshot 1" src="/images/databases/gcs-1.png" />
<Image alt="GCS screenshot 2" src="/images/databases/gcs-2.png" />
</Flex>

Navigate to the upload section of your new bucket:

<Flex>
<Image alt="GCS screenshot 3" src="/images/databases/gcs-3.png" />
<Image alt="GCS screenshot 4" src="/images/databases/gcs-4.png" />
</Flex>

And upload the following CSV file, which contains some example data:

<Download href="/images/databases/myfile.csv">myfile.csv</Download>

## Enable the Google Cloud Storage API

The Google Cloud Storage API is [enabled by default](https://cloud.google.com/service-usage/docs/enabled-service#default) when you create a project through the Google Cloud Console or CLI. Feel free to [skip to the next step](#create-a-service-account-and-key-file).

If you do need to enable the API for programmatic access in your project, head over to the [APIs & Services dashboard](https://console.cloud.google.com/apis/dashboard) (select or create a project if asked). Search for the Cloud Storage API and enable it. The screenshot below has a blue "Manage" button and indicates the "API is enabled" which means no further action needs to be taken. This is very likely what you have since the API is enabled by default. However, if that is not what you see and you have an "Enable" button, you'll need to enable the API:

<Flex>
<Image alt="GCS screenshot 5" src="/images/databases/gcs-5.png" />
<Image alt="GCS screenshot 6" src="/images/databases/gcs-6.png" />
<Image alt="GCS screenshot 7" src="/images/databases/gcs-7.png" />
</Flex>

## Create a service account and key file

To use the Google Cloud Storage API from Streamlit, you need a Google Cloud Platform service account (a special type for programmatic data access). Go to the Service Accounts page and create an account with <b>Viewer</b> permission.

<Flex>
<Image alt="GCS screenshot 8" src="/images/databases/gcs-8.png" />
<Image alt="GCS screenshot 9" src="/images/databases/gcs-9.png" />
<Image alt="GCS screenshot 10" src="/images/databases/gcs-10.png" />
</Flex>

<Note>

If the button **CREATE SERVICE ACCOUNT** is gray, you don't have the correct permissions. Ask the
admin of your Google Cloud project for help.

</Note>

After clicking **DONE**, you should be back on the service accounts overview. Create a JSON key file for the new account and download it:

<Flex>
<Image alt="GCS screenshot 11" src="/images/databases/gcs-11.png" />
<Image alt="GCS screenshot 12" src="/images/databases/gcs-12.png" />
<Image alt="GCS screenshot 13" src="/images/databases/gcs-13.png" />
</Flex>

## Add the key to your local app secrets

Your local Streamlit app will read secrets from a file `.streamlit/secrets.toml` in your app's root directory. Create this file if it doesn't exist yet and add the access key to it as shown below:

```toml
# .streamlit/secrets.toml

[connections.gcs]
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

## Add FilesConnection and gcsfs to your requirements file

Add the [FilesConnection](https://github.com/streamlit/files-connection) and [gcsfs](https://github.com/fsspec/gcsfs) packages to your `requirements.txt` file, preferably pinning the versions (replace `x.x.x` with the version you want installed):

```bash
# requirements.txt
gcsfs==x.x.x
# Direct pypi install coming soon
git+https://github.com/streamlit/files-connection
```

## Write your Streamlit app

Copy the code below to your Streamlit app and run it. Make sure to adapt the name of your bucket and file. Note that Streamlit automatically turns the access keys from your secrets file into environment variables.

```python
# streamlit_app.py

import streamlit as st
from st_files_connection import FilesConnection

# Create connection object and retrieve file contents.
# Specify input format is a csv and to cache the result for 600 seconds.
conn = st.experimental_connection('gcs', type=FilesConnection)
df = conn.read("streamlit-bucket/myfile.csv", input_format="csv", ttl=600)

# Print results.
for row in df.itertuples():
    st.write(f"{row.Owner} has a :{row.Pet}:")
```

See `st.experimental_connection` above? This handles secrets retrieval, setup, result caching and retries. By default, `read()` results are cached without expiring. In this case, we set `ttl=600` to ensure the file contents is cached for no longer than 10 minutes. You can also set `ttl=0` to disable caching. Learn more in [Caching](/library/advanced-features/caching).

If everything worked out (and you used the example file given above), your app should look like this:

![Finished app screenshot](/images/databases/streamlit-app.png)
