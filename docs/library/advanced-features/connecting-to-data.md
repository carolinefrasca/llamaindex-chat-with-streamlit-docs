---
title: Connecting to data
slug: /library/advanced-features/connecting-to-data
---

# Connecting to data

Most Streamlit apps need some kind of data or API access to be useful - either retrieving data to view or saving the results of some user action. This data or API is often part of some remote service, database, or other data source.

**Anything you can do with Python, including data connections, will generally work in Streamlit**. Streamlit's [tutorials](/knowledge-base/tutorials/databases) are a great starting place for many data sources. However:

- Connecting to data in a Python application is often tedious and annoying.
- There are specific considerations for connecting to data from streamlit apps, such as caching and secrets management.

**Streamlit provides [`st.experimental_connection()`](/library/api-reference/connections/st.experimental_connection) to more easily connect your Streamlit apps to data and APIs with just a few lines of code**. This page provides a basic example of using the feature and then focuses on advanced usage.

For a comprehensive overview of this feature, check out this video tutorial by Joshua Carroll, Streamlit's Product Manager for Developer Experience. You'll learn about the feature's utility in creating and managing data connections within your apps by using real-world examples.

<YouTube videoId="xQwDfW7UHMo" />

## Basic usage

For basic startup and usage examples, read up on the relevant [data source tutorial](/knowledge-base/tutorials/databases) or our [blog post introducing st.experimental_connection](https://blog.streamlit.io/introducing-st-experimental_connection/). Streamlit has built-in connections to SQL dialects and Snowflake Snowpark. We also maintain installable connections for [Cloud File Storage](https://github.com/streamlit/files-connection) and [Google Sheets](https://github.com/streamlit/gsheets-connection).

If you are just starting, the best way to learn is to pick a data source you can access and get a minimal example working from one of the pages above 👆. Here, we will provide an ultra-minimal usage example for using a SQLite database. From there, the rest of this page will focus on advanced usage.

### A simple starting point - using a local SQLite database

A [local SQLite database](https://sqlite.org/index.html) could be useful for your app's semi-persistent data storage.

<Note>

Community Cloud apps do not guarantee the persistence of local file storage, so the platform may delete data stored using this technique at any time.

</Note>

To see the example below running live, check out the interactive demo below:

<Cloud src="https://experimental-connection.streamlit.app/SQL?embed=true" />

#### Step 1: Install prerequisite library - SQLAlchemy

All SQLConnections in Streamlit use SQLAlchemy. For most other SQL dialects, you also need to install the driver. But the [SQLite driver ships with python3](https://docs.python.org/3/library/sqlite3.html), so it isn't necessary.

```bash
pip install SQLAlchemy==1.4.0
```

#### Step 2: Set a database URL in your Streamlit secrets.toml file

Create a directory and file `.streamlit/secrets.toml` in the same directory your app will run from. Add the following to the file.

```toml
# .streamlit/secrets.toml

[connections.pets_db]
url = "sqlite:///pets.db"
```

#### Step 3: Use the connection in your app

The following app creates a connection to the database, uses it to create a table and insert some data, then queries the data back and displays it in a data frame.

```python
# streamlit_app.py

import streamlit as st

# Create the SQL connection to pets_db as specified in your secrets file.
conn = st.experimental_connection('pets_db', type='sql')

# Insert some data with conn.session.
with conn.session as s:
    s.execute('CREATE TABLE IF NOT EXISTS pet_owners (person TEXT, pet TEXT);')
    s.execute('DELETE FROM pet_owners;')
    pet_owners = {'jerry': 'fish', 'barbara': 'cat', 'alex': 'puppy'}
    for k in pet_owners:
        s.execute(
            'INSERT INTO pet_owners (person, pet) VALUES (:owner, :pet);',
            params=dict(owner=k, pet=pet_owners[k])
        )
    s.commit()

# Query and display the data you inserted
pet_owners = conn.query('select * from pet_owners')
st.dataframe(pet_owners)
```

In this example, we didn't set a `ttl=` value on the call to [`conn.query()`](/library/api-reference/connections/st.connections.sqlconnection#sqlconnectionquery), meaning Streamlit caches the result indefinitely as long as the app server runs.

Now, on to more advanced topics! 🚀

## Advanced topics

### Global secrets, managing multiple apps and multiple data stores

Streamlit [supports a global secrets file](/library/advanced-features/secrets-management) specified in the user's home directory, such as `~/.streamlit/secrets.toml`. If you build or manage multiple apps, we recommend using a global credential or secret file for local development across apps. With this approach, you only need to set up and manage your credentials in one place, and connecting a new app to your existing data sources is effectively a one-liner. It also reduces the risk of accidentally checking in your credentials to git since they don't need to exist in the project repository.

For cases where you have multiple similar data sources that you connect to during local development (such as a local vs. staging database), you can define different connection sections in your secrets or credentials file for different environments and then decide which to use at runtime. `st.experimental_connection` supports this with the _`name=env:<MY_NAME_VARIABLE>`_ syntax.

E.g., say I have a local and a staging MySQL database and want to connect my app to either at different times. I could create a global secrets file like this:

```toml
# ~/.streamlit/secrets.toml

[connections.local]
url = "mysql://me:****@localhost:3306/local_db"

[connections.staging]
url = "mysql://jdoe:******@staging.acmecorp.com:3306/staging_db"
```

Then I can configure my app connection to take its name from a specified environment variable

```python
# streamlit_app.py
import streamlit as st

conn = st.experimental_connection("env:DB_CONN", "sql")
df = conn.query("select * from mytable")
# ...
```

Now I can specify whether to connect to local or staging at runtime by setting the `DB_CONN` environment variable.

```bash
# connect to local
DB_CONN=local streamlit run streamlit_app.py

# connect to staging
DB_CONN=staging streamlit run streamlit_app.py
```

### Advanced SQLConnection configuration

The [SQLConnection](/library/api-reference/connections/st.connections.sqlconnection) configuration uses SQLAlchemy `create_engine()` function. It will take a single URL argument or attempt to construct a URL from several parts (username, database, host, and so on) using [`SQLAlchemy.engine.URL.create()`](https://docs.sqlalchemy.org/en/20/core/engines.html#sqlalchemy.engine.URL.create).

Several popular SQLAlchemy dialects, such as Snowflake and Google BigQuery, can be configured using additional arguments to `create_engine()` besides the URL. These can be passed as `**kwargs` to the [st.experimental_connection](/library/api-reference/connections/st.experimental_connection) call directly or specified in an additional secrets section called `create_engine_kwargs`.

E.g. snowflake-sqlalchemy takes an additional [`connect_args`](https://docs.sqlalchemy.org/en/20/core/engines.html#sqlalchemy.create_engine.params.connect_args) argument as a dictionary for configuration that isn’t supported in the URL. These could be specified as follows:

```toml
# .streamlit/secrets.toml

[connections.snowflake]
url = "snowflake://<user_login_name>@<account_identifier>/"

[connections.snowflake.create_engine_kwargs.connect_args]
authenticator = "externalbrowser"
warehouse = "xxx"
role = "xxx"
```

```python
# streamlit_app.py

import streamlit as st

# url and connect_args from secrets.toml above are picked up and used here
conn = st.experimental_connection("snowflake", "sql")
# ...
```

Alternatively, this could be specified entirely in `**kwargs`.

```python
# streamlit_app.py

import streamlit as st

# secrets.toml is not needed
conn = st.experimental_connection(
    "snowflake",
    "sql",
    url = "snowflake://<user_login_name>@<account_identifier>/",
    connect_args = dict(
        authenticator = "externalbrowser",
        warehouse = "xxx",
        role = "xxx",
    )
)
# ...
```

You can also provide both kwargs and secrets.toml values, and they will be merged (typically, kwargs take precedence).

### Connection considerations in frequently used or long-running apps

By default, connection objects are cached without expiration using [`st.cache_resource`](/library/api-reference/performance/st.cache_resource). In most cases this is desired. You can do `st.experimental_connection('myconn', type=MyConnection, ttl=<N>)` if you want the connection object to expire after some time.

Many connection types are expected to be long-running or completely stateless, so expiration is unnecessary. Suppose a connection becomes stale (such as a cached token expiring or a server-side connection being closed). In that case, every connection has a `reset()` method, which will invalidate the cached version and cause Streamlit to recreate the connection the next time it is retrieved

Convenience methods like `query()` and `read()` will typically cache results by default using [`st.cache_data`](/library/api-reference/performance/st.cache_data) without an expiration. When an app can run many different read operations with large results, it can cause high memory usage over time and results to become stale in a long-running app, the same as with any other usage of `st.cache_data`. For production use cases, we recommend setting an appropriate `ttl` on these read operations, such as `conn.read('path/to/file', ttl="1d")`. Refer to [Caching](/library/advanced-features/caching) for more information.

For apps that could get significant concurrent usage, ensure that you understand any thread safety implications of your connection, particularly when using a connection built by a third party. Connections built by Streamlit should provide thread-safe operations by default.

### Build your own connection

Building your own basic connection implementation using an existing driver or SDK is quite straightforward in most cases. However, you can add more complex functionality with further effort. This custom implementation can be a great way to extend support to a new data source and contribute to the Streamlit ecosystem.

Maintaining a tailored internal Connection implementation across many apps can be a powerful practice for organizations with frequently used access patterns and data sources.

Check out the [Build your own Connection page](https://experimental-connection.streamlit.app/Build_your_own) in the st.experimental connection demo app below for a quick tutorial and working implementation. This demo builds a minimal but very functional Connection on top of DuckDB.

<Cloud src="https://experimental-connection.streamlit.app/Build_your_own?embed=true" />

The typical steps are:

1. Declare the Connection class, extending [`ExperimentalBaseConnection`](/library/api-reference/connections/st.connections.experimentalbaseconnection) with the type parameter bound to the underlying connection object:

   ```python
   from streamlit.connections import ExperimentalBaseConnection
   import duckdb

   class DuckDBConnection(ExperimentalBaseConnection[duckdb.DuckDBPyConnection])
   ```

2. Implement the `_connect` method that reads any kwargs, external config/credential locations, and Streamlit secrets to initialize the underlying connection:

   ```python
   def _connect(self, **kwargs) -> duckdb.DuckDBPyConnection:
       if 'database' in kwargs:
           db = kwargs.pop('database')
       else:
           db = self._secrets['database']
       return duckdb.connect(database=db, **kwargs)
   ```

3. Add useful helper methods that make sense for your connection (wrapping them in `st.cache_data` where caching is desired)

### Connection-building best practices

We recommend applying the following best practices to make your Connection consistent with the Connections built into Streamlit and the wider Streamlit ecosystem. These practices are especially important for Connections that you intend to distribute publicly.

1. **Extend existing drivers or SDKs, and default to semantics that makes sense for their existing users.**

   You should rarely need to implement complex data access logic from scratch when building a Connection. Use existing popular Python drivers and clients whenever possible. Doing so makes your Connection easier to maintain, more secure, and enables users to get the latest features. E.g. [SQLConnection](/library/api-reference/connections/st.connections.sqlconnection) extends SQLAlchemy, [FileConnection](https://github.com/streamlit/files-connection) extends [fsspec](https://filesystem-spec.readthedocs.io/en/latest/), [GsheetsConnection](https://github.com/streamlit/gsheets-connection) extends [gspread](https://docs.gspread.org/en/latest/), etc.

   Consider using access patterns, method/argument naming, and return values that are consistent with the underlying package and familiar to existing users of that package.

2. **Intuitive, easy to use read methods.**

   Much of the power of st.experimental_connection is providing intuitive, easy-to-use read methods that enable app developers to get started quickly. Most connections should expose at least one read method that is:

   - Named with a simple verb, like `read()`, `query()`, or `get()`
   - Wrapped by `st.cache_data` by default, with at least `ttl=` argument supported
   - If the result is in a tabular format, it returns a pandas DataFrame
   - Provides commonly used keyword arguments (such as paging or formatting) with sensible defaults - ideally, the common case requires only 1-2 arguments.

3. **Config, secrets, and precedence in `_connect` method.**

   Every Connection should support commonly used connection parameters provided via Streamlit secrets and keyword arguments. The names should match the ones used when initializing or configuring the underlying package.

   Additionally, where relevant, Connections should support data source specific configuration through existing standard environment variables or config / credential files. In many cases, the underlying package provides constructors or factory functions that already handle this easily.

   When you can specify the same connection parameters in multiple places, we recommend using the following precedence order when possible (highest to lowest):

   - Keyword arguments specified in the code
   - Streamlit secrets
   - data source specific configuration (if relevant)

4. **Handling thread safety and stale connections.**

   Connections should provide thread-safe operations when practical (which should be most of the time) and clearly document any considerations around this. Most underlying drivers or SDKs should provide thread-safe objects or methods - use these when possible.

   If the underlying driver or SDK has a risk of stateful connection objects becoming stale or invalid, consider building a low impact health check or reset/retry pattern into the access methods. The SQLConnection built into Streamlit has a good example of this pattern using [tenacity](https://tenacity.readthedocs.io/) and the built-in [Connection.reset()](/library/api-reference/connections/st.connections.sqlconnection#sqlconnectionreset) method. An alternate approach is to encourage developers to set an appropriate TTL on the `st.experimental_connection()` call to ensure it periodically reinitializes the connection object.
