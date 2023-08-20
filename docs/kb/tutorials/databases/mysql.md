---
title: Connect Streamlit to MySQL
slug: /knowledge-base/tutorials/databases/mysql
---

# Connect Streamlit to MySQL

## Introduction

This guide explains how to securely access a **_remote_** MySQL database from Streamlit Community Cloud. It uses [st.experimental_connection](/library/api-reference/connections/st.experimental_connection) and Streamlit's [Secrets management](/library/advanced-features/secrets-management). The below example code will **only work on Streamlit version >= 1.22**, when `st.experimental_connection` was added.

## Create a MySQL database

<Note>

If you already have a database that you want to use, feel free
to [skip to the next step](#add-username-and-password-to-your-local-app-secrets).

</Note>

First, follow [this tutorial](https://dev.mysql.com/doc/mysql-getting-started/en/) to install MySQL and start the MySQL server (note down the username and password!). Once your MySQL server is up and running, connect to it with the `mysql` client and enter the following commands to create a database and a table with some example values:

```sql
CREATE DATABASE pets;

USE pets;

CREATE TABLE mytable (
    name            varchar(80),
    pet             varchar(80)
);

INSERT INTO mytable VALUES ('Mary', 'dog'), ('John', 'cat'), ('Robert', 'bird');
```

## Add username and password to your local app secrets

Your local Streamlit app will read secrets from a file `.streamlit/secrets.toml` in your app's root directory. Learn more about [Streamlit secrets management here](/library/advanced-features/secrets-management). Create this file if it doesn't exist yet and add the database name, user, and password of your MySQL server as shown below:

```toml
# .streamlit/secrets.toml

[connections.mysql]
dialect = "mysql"
host = "localhost"
port = 3306
database = "xxx"
username = "xxx"
password = "xxx"
```

<Important>

When copying your app secrets to Streamlit Community Cloud, be sure to replace the values of **host**, **port**, **database**, **username**, and **password** with those of your _remote_ MySQL database!

Add this file to `.gitignore` and don't commit it to your GitHub repo!

</Important>

## Copy your app secrets to the cloud

As the `secrets.toml` file above is not committed to GitHub, you need to pass its content to your deployed app (on Streamlit Community Cloud) separately. Go to the [app dashboard](https://share.streamlit.io/) and in the app's dropdown menu, click on **Edit Secrets**. Copy the content of `secrets.toml` into the text area. More information is available at [Secrets management](/streamlit-community-cloud/deploy-your-app/secrets-management).

![Secrets manager screenshot](/images/databases/edit-secrets.png)

## Add dependencies to your requirements file

Add the [mysqlclient](https://github.com/PyMySQL/mysqlclient) and [SQLAlchemy](https://github.com/sqlalchemy/sqlalchemy) packages to your `requirements.txt` file, preferably pinning its version (replace `x.x.x` with the version you want installed):

```bash
# requirements.txt
mysqlclient==x.x.x
SQLAlchemy==x.x.x
```

## Write your Streamlit app

Copy the code below to your Streamlit app and run it. Make sure to adapt `query` to use the name of your table.

```python
# streamlit_app.py

import streamlit as st

# Initialize connection.
conn = st.experimental_connection('mysql', type='sql')

# Perform query.
df = conn.query('SELECT * from mytable;', ttl=600)

# Print results.
for row in df.itertuples():
    st.write(f"{row.name} has a :{row.pet}:")
```

See `st.experimental_connection` above? This handles secrets retrieval, setup, query caching and retries. By default, `query()` results are cached without expiring. In this case, we set `ttl=600` to ensure the query result is cached for no longer than 10 minutes. You can also set `ttl=0` to disable caching. Learn more in [Caching](/library/advanced-features/caching).

If everything worked out (and you used the example table we created above), your app should look like this:

![Finished app screenshot](/images/databases/streamlit-app.png)
