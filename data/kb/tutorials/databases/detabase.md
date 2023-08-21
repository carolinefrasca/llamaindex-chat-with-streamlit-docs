---
title: Connect Streamlit to Deta Base
slug: /knowledge-base/tutorials/databases/deta-base
---

# Connect Streamlit to Deta Base

## Introduction

This guide explains how to securely access and write to a [Deta Base](https://deta.space/docs/en/reference/base/about) database from Streamlit Community Cloud. Deta Base is a fully-managed and fast NoSQL database with a focus on end-user simplicity. The data is stored in your own "personal cloud" on [Deta Space](https://deta.space/developers). This guide uses the [Deta Python SDK](https://github.com/deta/deta-python) for Deta Base and Streamlit's [Secrets management](https://www.notion.so/streamlit-community-cloud/deploy-your-app/secrets-management).

## Create an account and sign in to Deta Space

First, you need to [create a Deta Space account](https://deta.space/signup?dev_mode=true) for using Deta Base. Make sure the "Developer Mode" option is enabled when signing up. Once you have an account, sign in to Deta Space. After signing in, open the Collections app by clicking on it.

[Deta Collections](https://deta.space/manual/features/collections#what-are-collections) is a pre-installed app on Space that stores different types of data that can be connected to other apps or services.
<Image alt="Deta Space Canvas" src="/images/databases/deta-1.png" caption="Deta Space Canvas" />

Now click on the **Get Started** button and then click on the **Create Collection** button after giving your Collection a name.
<Image alt="Create a New Collection" src="/images/databases/deta-2.png" caption="Create a New Collection" />

After that, click on the **Collection Settings** option in the top corner, which will show the modal for creating a **Data Key**. Click on the **Create New Data Key** button, then give your key a name, and click the **Generate** button. Copy the key shown to your clipboard by clicking on the copy button.

[Data Keys](https://deta.space/docs/en/basics/extending_apps#data-keys) allow you to read and manipulate data within your Collections.
<Image alt="Generate Data Key" src="/images/databases/deta-3.png" caption="Generate Data Key" />

Be sure to store your **Data Key** securely. It is shown only once, and you will need it to connect to your Deta Base.

## Add Data Key to your local app secrets

Your local Streamlit app will read secrets from a file `.streamlit/secrets.toml` in your app's root directory. Create this file if it doesn't exist yet and add the **Data Key** (from the previous step) of your Deta Base as shown below:

```toml
# .streamlit/secrets.toml
data_key = "xxx"
```

Replace `xxx` above ☝️ with your **Data Key** from the previous step.

<Important>

Add this file to `.gitignore` and don't commit it to your GitHub repo!

</Important>

## Copy your app secrets to the cloud

As the `secrets.toml` file above is not committed to GitHub, you need to pass its content to your deployed app (on Streamlit Community Cloud) separately. Go to the [app dashboard](https://share.streamlit.io/) and in the app's dropdown menu, click on **Edit Secrets**. Copy the content of `secrets.toml` into the text area. More information is available at [Secrets management](/streamlit-community-cloud/deploy-your-app/secrets-management).

![Secrets manager screenshot](/images/databases/edit-secrets.png)

## Add deta to your requirements file

Add the [deta](https://github.com/deta/deta-python) Python SDK for Deta Base to your `requirements.txt` file, preferably pinning its version (replace `x.x.x` with the version you want installed):

```bash
# requirements.txt
deta==x.x.x
```

## Write your Streamlit app

Copy the code below to your Streamlit app and run it. The example app below writes data from a Streamlit form to a Deta Base database `example-db`.

```python
import streamlit as st
from deta import Deta

# Data to be written to Deta Base
with st.form("form"):
    name = st.text_input("Your name")
    age = st.number_input("Your age")
    submitted = st.form_submit_button("Store in database")


# Connect to Deta Base with your Data Key
deta = Deta(st.secrets["data_key"])

# Create a new database "example-db"
# If you need a new database, just use another name.
db = deta.Base("example-db")

# If the user clicked the submit button,
# write the data from the form to the database.
# You can store any data you want here. Just modify that dictionary below (the entries between the {}).
if submitted:
    db.put({"name": name, "age": age})

"---"
"Here's everything stored in the database:"
# This reads all items from the database and displays them to your app.
# db_content is a list of dictionaries. You can do everything you want with it.
db_content = db.fetch().items
st.write(db_content)
```

If everything worked out (and you used the example we created above), your app should look like this:

![Finished app GIF](/images/databases/deta_app.gif)
