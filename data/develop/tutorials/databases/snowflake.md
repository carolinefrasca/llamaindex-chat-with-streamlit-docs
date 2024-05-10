---
title: Connect Streamlit to Snowflake
slug: /develop/tutorials/databases/snowflake
---

# Connect Streamlit to Snowflake

## Introduction

This guide explains how to securely access a Snowflake database from Streamlit. It uses [st.connection](/develop/api-reference/connections/st.connection), the [Snowpark library](https://docs.snowflake.com/en/developer-guide/snowpark/python/index) and Streamlit's [Secrets management](/develop/concepts/connections/secrets-management). The below example code **will only work on Streamlit version >= 1.28**, when `st.connection` was added.

## Create a Snowflake database

<Note>

If you already have a database that you want to use, feel free to [skip to the next step](#add-username-and-password-to-your-local-app-secrets).

</Note>

First, [sign up for Snowflake](https://signup.snowflake.com/) and log into the [Snowflake web interface](https://docs.snowflake.com/en/user-guide/connecting.html#logging-in-using-the-web-interface) (note down your username, password, and [account identifier](https://docs.snowflake.com/en/user-guide/admin-account-identifier.html)!):

![](/images/databases/snowflake-1.png)

Enter the following queries into the SQL editor in the Worksheets page to create a database and a table with some example values:

```sql
CREATE DATABASE PETS;

CREATE TABLE MYTABLE (
    NAME            varchar(80),
    PET             varchar(80)
);

INSERT INTO MYTABLE VALUES ('Mary', 'dog'), ('John', 'cat'), ('Robert', 'bird');

SELECT * FROM MYTABLE;
```

Before you execute the queries, first determine which Snowflake UI / web interface you're using. The examples below use [Snowsight](https://docs.snowflake.com/en/user-guide/ui-snowsight). You can also use [Classic Console Worksheets](https://docs.snowflake.com/en/user-guide/ui-worksheet) or any other means of running Snowflake SQL statements.

### Execute queries in a Worksheet

To execute the queries in a Worksheet, highlight or select all the queries with your mouse, and click the play button in the top right corner.

<Image alt="AWS screenshot 1" src="/images/databases/snowflake-4.png" />

<Important>

Be sure to highlight or select **all** the queries (lines 1-10) before clicking the play button.

</Important>

Once you have executed the queries, you should see a preview of the table in the **Results** panel at the bottom of the page. Additionally, you should see your newly created database and schema by expanding the accordion on the left side of the page. Lastly, the warehouse name is displayed on the button to the left of the **Share** button.

<Image alt="AWS screenshot 2" src="/images/databases/snowflake-5.png" />

Make sure to note down the name of your warehouse, database, and schema. ☝️

## Install snowflake-snowpark-python

You can find the instructions and prerequisites for installing `snowflake-snowpark-python` in the [Snowflake Developer Guide](https://docs.snowflake.com/en/developer-guide/snowpark/python/setup#installation-instructions).

```bash
pip install snowflake-snowpark-python
```

## Add connection parameters to your local app secrets

Your local Streamlit app will read secrets from a file `.streamlit/secrets.toml` in your app’s root directory. Learn more about [Streamlit secrets management here](/develop/concepts/connections/secrets-management). Create this file if it doesn’t exist yet and add your Snowflake username, password, [account identifier](https://docs.snowflake.com/en/user-guide/admin-account-identifier.html), and the name of your warehouse, database, and schema as shown below:

```toml
# .streamlit/secrets.toml

[connections.snowflake]
account = "xxx"
user = "xxx"
password = "xxx"
role = "xxx"
warehouse = "xxx"
database = "xxx"
schema = "xxx"
client_session_keep_alive = true
```

If you created the database from the previous step, the names of your database and schema are `PETS` and `PUBLIC`, respectively. Streamlit will also use **Snowflake config and credentials** from a [SnowSQL config file](https://docs.snowflake.com/en/user-guide/snowsql-config#snowsql-config-file) if available.

<Important>

Add this file to `.gitignore` and don't commit it to your GitHub repo!

</Important>

## Write your Streamlit app

Copy the code below to your Streamlit app and run it. Make sure to adapt the query to use the name of your table.

```python
# streamlit_app.py

import streamlit as st

# Initialize connection.
conn = st.connection("snowflake")

# Perform query.
df = conn.query("SELECT * from mytable;", ttl=600)

# Print results.
for row in df.itertuples():
    st.write(f"{row.NAME} has a :{row.PET}:")
```

See `st.connection` above? This handles secrets retrieval, setup, query caching and retries. By default, `query()` results are cached without expiring. In this case, we set `ttl=600` to ensure the query result is cached for no longer than 10 minutes. You can also set `ttl=0` to disable caching. Learn more in [Caching](/develop/concepts/architecture/caching).

If everything worked out (and you used the example table we created above), your app should look like this:

![Finished app screenshot](/images/databases/snowflake-app.png)

### Using a Snowpark Session

The same [SnowflakeConnection](/develop/api-reference/connections/st.connections.snowflakeconnection) used above also provides access to the [Snowpark Session](https://docs.snowflake.com/en/developer-guide/snowpark/reference/python/session.html) for DataFrame-style operations that run natively inside Snowflake. Using this approach, you can rewrite the app above as follows:

```python
# streamlit_app.py

import streamlit as st

# Initialize connection.
conn = st.connection("snowflake")

# Load the table as a dataframe using the Snowpark Session.
@st.cache_data
def load_table():
    session = conn.session()
    return session.table("mytable").to_pandas()

df = load_table()

# Print results.
for row in df.itertuples():
    st.write(f"{row.NAME} has a :{row.PET}:")
```

If everything worked out (and you used the example table we created above), your app should look the same as the screenshot from the first example above.

## Connecting to Snowflake from Community Cloud

This tutorial assumes a local Streamlit app, however you can also connect to Snowflake from apps hosted in Community Cloud. The main additional steps are:

- [Include information about dependencies](/deploy/streamlit-community-cloud/deploy-your-app/app-dependencies) using a `requirements.txt` file with `snowflake-snowpark-python` and any other dependencies.
- [Add your secrets](/deploy/streamlit-community-cloud/deploy-your-app/secrets-management#deploy-an-app-and-set-up-secrets) to your Community Cloud app.
