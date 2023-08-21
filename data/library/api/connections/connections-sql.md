---
title: st.connections.SQLConnection
slug: /library/api-reference/connections/st.connections.sqlconnection
---

<Important>

This is an experimental feature. Experimental features and their APIs may change or be removed at any time. To learn more, click [here](/library/advanced-features/prerelease#experimental-features).

</Important>

<Tip>

This page only contains on the `st.connections.SQLConnection` API. For a deeper dive into creating and managing data connections within Streamlit apps, read [Connecting to data](/library/advanced-features/connecting-to-data).

</Tip>

<Autofunction function="streamlit.connections.SQLConnection" />

### Basic usage:

```python
import streamlit as st

conn = st.experimental_connection("sql")
df = conn.query("select * from pet_owners")
st.dataframe(df)
```

In case you want to pass a connection URL (or other parameters) directly, it also works:

```python
conn = st.experimental_connection(
    "local_db",
    type="sql",
    url="mysql://user:pass@localhost:3306/mydb"
)
```

Or specify parameters in [secrets](/library/advanced-features/secrets-management):

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
conn = st.experimental_connection("mydb", type="sql", autocommit=True)
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

<Autofunction function="streamlit.connections.SQLConnection.query" />

<Autofunction function="streamlit.connections.SQLConnection.reset" />

<Autofunction function="streamlit.connections.SQLConnection.session" />
