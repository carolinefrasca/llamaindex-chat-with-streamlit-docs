---
title: Connect Streamlit to PostgreSQL
slug: /knowledge-base/tutorials/databases/postgresql
---

# Connect Streamlit to PostgreSQL

## Introduction

This guide explains how to securely access a **_remote_** PostgreSQL database from Streamlit Community Cloud. It uses the [psycopg2](https://www.psycopg.org/) library and Streamlit's [Secrets management](/streamlit-community-cloud/deploy-your-app/secrets-management).

## Create a PostgreSQL database

<Note>

If you already have a database that you want to use, feel free
to [skip to the next step](#add-username-and-password-to-your-local-app-secrets).

</Note>

First, follow [this tutorial](https://www.tutorialspoint.com/postgresql/postgresql_environment.htm) to install PostgreSQL and create a database (note down the database name, username, and password!). Open the SQL Shell (`psql`) and enter the following two commands to create a table with some example values:

```sql
CREATE TABLE mytable (
    name            varchar(80),
    pet             varchar(80)
);

INSERT INTO mytable VALUES ('Mary', 'dog'), ('John', 'cat'), ('Robert', 'bird');
```

## Add username and password to your local app secrets

Your local Streamlit app will read secrets from a file `.streamlit/secrets.toml` in your app's root directory. Create this file if it doesn't exist yet and add the name, user, and password of your database as shown below:

```toml
# .streamlit/secrets.toml

[postgres]
host = "localhost"
port = 5432
dbname = "xxx"
user = "xxx"
password = "xxx"
```

<Important>

When copying your app secrets to Streamlit Community Cloud, be sure to replace the values of **host**, **port**, **dbname**, **user**, and **password** with those of your _remote_ PostgreSQL database!

Add this file to `.gitignore` and don't commit it to your GitHub repo!

</Important>

## Copy your app secrets to the cloud

As the `secrets.toml` file above is not committed to GitHub, you need to pass its content to your deployed app (on Streamlit Community Cloud) separately. Go to the [app dashboard](https://share.streamlit.io/) and in the app's dropdown menu, click on **Edit Secrets**. Copy the content of `secrets.toml` into the text area. More information is available at [Secrets management](/streamlit-community-cloud/deploy-your-app/secrets-management).

![Secrets manager screenshot](/images/databases/edit-secrets.png)

## Add psycopg2 to your requirements file

Add the [psycopg2](https://www.psycopg.org/) package to your `requirements.txt` file, preferably pinning its version (replace `x.x.x` with the version you want installed):

```bash
# requirements.txt
psycopg2-binary==x.x.x
```

## Write your Streamlit app

Copy the code below to your Streamlit app and run it. Make sure to adapt `query` to use the name of your table.

```python
# streamlit_app.py

import streamlit as st
import psycopg2

# Initialize connection.
# Uses st.cache_resource to only run once.
@st.cache_resource
def init_connection():
    return psycopg2.connect(**st.secrets["postgres"])

conn = init_connection()

# Perform query.
# Uses st.cache_data to only rerun when the query changes or after 10 min.
@st.cache_data(ttl=600)
def run_query(query):
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()

rows = run_query("SELECT * from mytable;")

# Print results.
for row in rows:
    st.write(f"{row[0]} has a :{row[1]}:")
```

See `st.cache_data` above? Without it, Streamlit would run the query every time the app reruns (e.g. on a widget interaction). With `st.cache_data`, it only runs when the query changes or after 10 minutes (that's what `ttl` is for). Watch out: If your database updates more frequently, you should adapt `ttl` or remove caching so viewers always see the latest data. Learn more in [Caching](/library/advanced-features/caching).

If everything worked out (and you used the example table we created above), your app should look like this:

![Finished app screenshot](/images/databases/streamlit-app.png)
