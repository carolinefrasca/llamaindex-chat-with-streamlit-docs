---
title: Connect Streamlit to AWS S3
slug: /knowledge-base/tutorials/databases/aws-s3
---

# Connect Streamlit to AWS S3

## Introduction

This guide explains how to securely access files on AWS S3 from Streamlit Community Cloud. It uses [Streamlit FilesConnection](https://github.com/streamlit/files-connection), the [s3fs](https://github.com/dask/s3fs) library and optionally Streamlit's [Secrets management](/library/advanced-features/secrets-management).

## Create an S3 bucket and add a file

<Note>

If you already have a bucket that you want to use, feel free
to [skip to the next step](#create-access-keys).

</Note>

First, [sign up for AWS](https://aws.amazon.com/) or log in. Go to the [S3 console](https://s3.console.aws.amazon.com/s3/home) and create a new bucket:

<Flex>
<Image alt="AWS screenshot 1" src="/images/databases/aws-1.png" />
<Image alt="AWS screenshot 2" src="/images/databases/aws-2.png" />
</Flex>

Navigate to the upload section of your new bucket:

<Flex>
<Image alt="AWS screenshot 3" src="/images/databases/aws-3.png" />
<Image alt="AWS screenshot 4" src="/images/databases/aws-4.png" />
</Flex>

And note down the "AWS Region" for later. In this example, it's `us-east-1`, but it may differ for you.

Next, upload the following CSV file, which contains some example data:

<Download href="/images/databases/myfile.csv">myfile.csv</Download>

## Create access keys

Go to the [AWS console](https://console.aws.amazon.com/), create access keys as shown below and copy the "Access Key ID" and "Secret Access Key":

<Flex>
<Image alt="AWS screenshot 5" src="/images/databases/aws-5.png" />
<Image alt="AWS screenshot 6" src="/images/databases/aws-6.png" />
</Flex>

<Tip>

Access keys created as a root user have wide-ranging permissions. In order to make your AWS account
more secure, you should consider creating an IAM account with restricted permissions and using its
access keys. More information [here](https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html).

</Tip>

## Set up your AWS credentials locally

Streamlit FilesConnection and s3fs will read and use your existing [AWS credentials and configuration](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html) if available - such as from an `~/.aws/credentials` file or environment variables.

If you don't already have this set up, or plan to host the app on Streamlit Community Cloud, you should specify the credentials from a file `.streamlit/secrets.toml` in your app's root directory or your home directory. Create this file if it doesn't exist yet and add to it the access key ID, access key secret, and the AWS default region you noted down earlier, as shown below:

```toml
# .streamlit/secrets.toml
AWS_ACCESS_KEY_ID = "xxx"
AWS_SECRET_ACCESS_KEY = "xxx"
AWS_DEFAULT_REGION = "xxx"
```

<Important>

Be sure to replace `xxx` above with the values you noted down earlier, and add this file to `.gitignore` so you don't commit it to your GitHub repo!

</Important>

## Copy your app secrets to the cloud

To host your app on Streamlit Community Cloud, you will need to pass your credentials to your deployed app via secrets. Go to the [app dashboard](https://share.streamlit.io/) and in the app's dropdown menu, click on **Edit Secrets**. Copy the content of `secrets.toml` above into the text area. More information is available at [Secrets management](/streamlit-community-cloud/deploy-your-app/secrets-management).

![Secrets manager screenshot](/images/databases/edit-secrets.png)

## Add FilesConnection and s3fs to your requirements file

Add the [FilesConnection](https://github.com/streamlit/files-connection) and [s3fs](https://github.com/dask/s3fs) packages to your `requirements.txt` file, preferably pinning the versions (replace `x.x.x` with the version you want installed):

```bash
# requirements.txt
s3fs==x.x.x
# Direct pypi install coming soon
git+https://github.com/streamlit/files-connection
```

## Write your Streamlit app

Copy the code below to your Streamlit app and run it. Make sure to adapt the name of your bucket and file. Note that Streamlit automatically turns the access keys from your secrets file into environment variables, where `s3fs` searches for them by default.

```python
# streamlit_app.py

import streamlit as st
from st_files_connection import FilesConnection

# Create connection object and retrieve file contents.
# Specify input format is a csv and to cache the result for 600 seconds.
conn = st.experimental_connection('s3', type=FilesConnection)
df = conn.read("testbucket-jrieke/myfile.csv", input_format="csv", ttl=600)

# Print results.
for row in df.itertuples():
    st.write(f"{row.Owner} has a :{row.Pet}:")
```

See `st.experimental_connection` above? This handles secrets retrieval, setup, result caching and retries. By default, `read()` results are cached without expiring. In this case, we set `ttl=600` to ensure the file contents is cached for no longer than 10 minutes. You can also set `ttl=0` to disable caching. Learn more in [Caching](/library/advanced-features/caching).

If everything worked out (and you used the example file given above), your app should look like this:

![Finished app screenshot](/images/databases/streamlit-app.png)
