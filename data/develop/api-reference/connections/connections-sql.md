---
title: st.connections.SQLConnection
slug: /develop/api-reference/connections/st.connections.sqlconnection
---

<Tip>

This page only contains the `st.connections.SQLConnection` class. For a deeper dive into creating and managing data connections within Streamlit apps, read [Connecting to data](/develop/concepts/connections/connecting-to-data).

</Tip>

<Autofunction function="streamlit.connections.SQLConnection" />

### Basic usage:

[SQLAlchemy](https://pypi.org/project/SQLAlchemy/) and any required drivers must be installed to use this connection.

```python
import streamlit as st

conn = st.connection("sql")
df = conn.query("select * from pet_owners")
st.dataframe(df)
```

In case you want to pass a connection URL (or other parameters) directly, it also works:

```python
conn = st.connection(
    "local_db",
    type="sql",
    url="mysql://user:pass@localhost:3306/mydb"
)
```

Or specify parameters in [secrets](/develop/concepts/connections/secrets-management):

```toml
# .streamlit/secrets.toml
[connections.mydb]
dialect = "mysql"
username = "myuser"
password = "password"
host = "localhost"
database = "mydb"
```

```python
# streamlit_app.py
conn = st.connection("mydb", type="sql", autocommit=True)
```

As described above, some cloud databases use extra `**kwargs` to specify credentials. These can be passed via secrets using the `create_engine_kwargs` section:

```toml
# .streamlit/secrets.toml
[connections.snowflake]
url = "snowflake://<username>@<account>/"

[connections.snowflake.create_engine_kwargs.connect_args]
authenticator = "externalbrowser"
role = "..."
# ...
```

<Autofunction function="streamlit.connections.SQLConnection.connect" />

<Autofunction function="streamlit.connections.SQLConnection.query" />

<Autofunction function="streamlit.connections.SQLConnection.reset" />

<Autofunction function="streamlit.connections.SQLConnection.driver" />

<Autofunction function="streamlit.connections.SQLConnection.engine" />

<Autofunction function="streamlit.connections.SQLConnection.session" />
