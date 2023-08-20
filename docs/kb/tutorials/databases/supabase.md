---
title: Connect Streamlit to Supabase
slug: /knowledge-base/tutorials/databases/supabase
---

# Connect Streamlit to Supabase

## Introduction

This guide explains how to securely access a Supabase instance from Streamlit Community Cloud. It uses the [Supabase Python Client Library](https://github.com/supabase-community/supabase-py) and Streamlit's [Secrets management](/streamlit-community-cloud/deploy-your-app/secrets-management). Supabase is the open source Firebase alternative and is based on PostgreSQL.

## Sign in to Supabase and create a project

First, head over to [Supabase](https://app.supabase.io/) and sign up for a free account using your GitHub.

<Flex>
<Image caption="Sign in with GitHub" src="/images/databases/supabase-1.png" />
<Image caption="Authorize Supabase" src="/images/databases/supabase-2.png" />
</Flex>

Once you're signed in, you can create a project.

<Flex>
<Image caption="Your Supabase account" src="/images/databases/supabase-3.png" />
<Image caption="Create a new project" src="/images/databases/supabase-4.png" />
</Flex>

Your screen should look like this once your project has been created:

<Image src="/images/databases/supabase-5.png" />

<Important>

Make sure to note down your Project API Key and Project URL highlighted in the above screenshot. ☝️

You will need these to connect to your Supabase instance from Streamlit.

</Important>

## Create a Supabase database

Now that you have a project, you can create a database and populate it with some sample data. To do so, click on the **SQL editor** button on the same project page, followed by the **New query** button in the SQL editor.

<Flex>
<Image caption="Open the SQL editor" src="/images/databases/supabase-6.png" />
<Image caption="Create a new query" src="/images/databases/supabase-7.png" />
</Flex>

In the SQL editor, enter the following queries to create a database and a table with some example values:

```sql
CREATE TABLE mytable (
    name            varchar(80),
    pet             varchar(80)
);

INSERT INTO mytable VALUES ('Mary', 'dog'), ('John', 'cat'), ('Robert', 'bird');
```

Click **Run** to execute the queries. To verify that the queries were executed successfully, click on the **Table Editor** button on the left menu, followed by your newly created table `mytable`.

<Flex>
<Image caption="Write and run your queries" src="/images/databases/supabase-8.png" />
<Image caption="View your table in the Table Editor" src="/images/databases/supabase-9.png" />
</Flex>

With your Supabase database created, you can now connect to it from Streamlit!

### Add Supabase Project URL and API key to your local app secrets

Your local Streamlit app will read secrets from a file `.streamlit/secrets.toml` in your app's root directory. Create this file if it doesn't exist yet and add the `supabase_url` and `supabase_key` here:

```toml
# .streamlit/secrets.toml

supabase_url = "xxxx"
supabase_key = "xxxx"
```

Replace `xxxx` above with your Project URL and API key from [Step 1](/knowledge-base/tutorials/databases/supabase#sign-in-to-supabase-and-create-a-project).

<Important>

Add this file to `.gitignore` and don't commit it to your GitHub repo!

</Important>

## Copy your app secrets to the cloud

As the `secrets.toml` file above is not committed to GitHub, you need to pass its content to your deployed app (on Streamlit Community Cloud) separately. Go to the [app dashboard](https://share.streamlit.io/) and in the app's dropdown menu, click on **Edit Secrets**. Copy the content of `secrets.toml` into the text area. More information is available at [Secrets management](/streamlit-community-cloud/deploy-your-app/secrets-management).

![Secrets manager screenshot](/images/databases/edit-secrets.png)

## Add supabase to your requirements file

Add the [`supabase`](https://github.com/supabase-community/supabase-py) Python Client Library to your `requirements.txt` file, preferably pinning its version (replace `x.x.x` with the version you want installed):

```bash
# requirements.txt
supabase==x.x.x
```

## Write your Streamlit app

Copy the code below to your Streamlit app and run it.

```python
# streamlit_app.py

import streamlit as st
from supabase import create_client, Client

# Initialize connection.
# Uses st.cache_resource to only run once.
@st.cache_resource
def init_connection():
    url = st.secrets["supabase_url"]
    key = st.secrets["supabase_key"]
    return create_client(url, key)

supabase = init_connection()

# Perform query.
# Uses st.cache_data to only rerun when the query changes or after 10 min.
@st.cache_data(ttl=600)
def run_query():
    return supabase.table("mytable").select("*").execute()

rows = run_query()

# Print results.
for row in rows.data:
    st.write(f"{row['name']} has a :{row['pet']}:")

```

See `st.cache_data` above? Without it, Streamlit would run the query every time the app reruns (e.g. on a widget interaction). With `st.cache_data`, it only runs when the query changes or after 10 minutes (that's what `ttl` is for). Watch out: If your database updates more frequently, you should adapt `ttl` or remove caching so viewers always see the latest data. Learn more in [Caching](/library/advanced-features/caching).

If everything worked out (and you used the example table we created above), your app should look like this:

![Finished app screenshot](/images/databases/supabase-10.png)

As Supabase uses PostgresSQL under the hood, you can also connect to Supabase by using the connection string Supabase provides under Settings > Databases. From there, you can refer to the [PostgresSQL tutorial](/knowledge-base/tutorials/databases/postgresql) to connect to your database.
