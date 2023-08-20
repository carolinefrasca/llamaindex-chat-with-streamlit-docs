---
title: Connect Streamlit to TiDB
slug: /knowledge-base/tutorials/databases/tidb
---

# Connect Streamlit to TiDB

## Introduction

This guide explains how to securely access a **_remote_** TiDB database from Streamlit Community Cloud. It uses [st.experimental_connection](/library/api-reference/connections/st.experimental_connection) and Streamlit's [Secrets management](/library/advanced-features/secrets-management). The below example code will **only work on Streamlit version >= 1.22**, when `st.experimental_connection` was added.

[TiDB](https://www.pingcap.com/tidb/) is an open-source, MySQL-compatible database that supports Hybrid Transactional and Analytical Processing (HTAP) workloads. [TiDB Cloud](https://www.pingcap.com/tidb-cloud/) is a fully managed cloud database service that simplifies the deployment and management of TiDB databases for developers.

## Sign in to TiDB Cloud and create a cluster

First, head over to [TiDB Cloud](https://tidbcloud.com/free-trial) and sign up for a free account, using either Google, GitHub, Microsoft or E-mail:

![Sign up TiDB Cloud](/images/databases/tidb-1.png)

Once you've signed in, you will already have a TiDB cluster:

![List clusters](/images/databases/tidb-2.png)

You can create more clusters if you want to. Click the cluster name to enter cluster overview page:

![Cluster overview](/images/databases/tidb-3.png)

Then click **Connect** to easily get the connection arguments to access the cluster. On the popup, click **Create password** to set the password.

![Get connection arguments](/images/databases/tidb-4.png)

<Important>

Make sure to note down the password. It won't be available on TiDB Cloud after this step.

</Important>

## Create a TiDB database

<Note>

If you already have a database that you want to use, feel free
to [skip to the next step](#add-username-and-password-to-your-local-app-secrets).

</Note>

Once your TiDB cluster is up and running, connect to it with the `mysql` client(or with **Chat2Query** tab on the console) and enter the following commands to create a database and a table with some example values:

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

Your local Streamlit app will read secrets from a file `.streamlit/secrets.toml` in your app's root directory. Learn more about [Streamlit secrets management here](/library/advanced-features/secrets-management). Create this file if it doesn't exist yet and add host, username and password of your TiDB cluster as shown below:

```toml
# .streamlit/secrets.toml

[connections.tidb]
dialect = "mysql"
host = "<TiDB_cluster_host>"
port = 4000
database = "pets"
username = "<TiDB_cluster_user>"
password = "<TiDB_cluster_password>"
```

<Important>

When copying your app secrets to Streamlit Community Cloud, be sure to replace the values of **host**, **username** and **password** with those of your _remote_ TiDB cluster!

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
conn = st.experimental_connection('tidb', type='sql')

# Perform query.
df = conn.query('SELECT * from mytable;', ttl=600)

# Print results.
for row in df.itertuples():
    st.write(f"{row.name} has a :{row.pet}:")
```

See `st.experimental_connection` above? This handles secrets retrieval, setup, query caching and retries. By default, `query()` results are cached without expiring. In this case, we set `ttl=600` to ensure the query result is cached for no longer than 10 minutes. You can also set `ttl=0` to disable caching. Learn more in [Caching](/library/advanced-features/caching).

If everything worked out (and you used the example table we created above), your app should look like this:

![Finished app screenshot](/images/databases/streamlit-app.png)

## Connect with PyMySQL

Other than [mysqlclient](https://github.com/PyMySQL/mysqlclient), [PyMySQL](https://github.com/PyMySQL/PyMySQL) is another popular MySQL Python client. To use PyMySQL, first you need to adapt your requirements file:

```bash
# requirements.txt
PyMySQL==x.x.x
SQLAlchemy==x.x.x
```

Then adapt your secrets file:

```toml
# .streamlit/secrets.toml

[connections.tidb]
dialect = "mysql"
driver = "pymysql"
host = "<TiDB_cluster_host>"
port = 4000
database = "pets"
username = "<TiDB_cluster_user>"
password = "<TiDB_cluster_password>"
create_engine_kwargs = { connect_args = { ssl = { ca = "<path_to_CA_store>" }}}
```
