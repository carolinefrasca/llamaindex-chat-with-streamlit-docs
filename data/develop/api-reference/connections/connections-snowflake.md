---
title: st.connections.SnowflakeConnection
slug: /develop/api-reference/connections/st.connections.snowflakeconnection
---

<Tip>

This page only contains the `st.connections.SnowflakeConnection` class. For a deeper dive into creating and managing data connections within Streamlit apps, read [Connecting to data](/develop/concepts/connections/connecting-to-data).

</Tip>

<Autofunction function="streamlit.connections.SnowflakeConnection" />

### Configuration

{/**
Internal note: This section is deep-linked from the library in 1.28.1 via /st.connections.snowflakeconnection-configuration through a redirect.
Maintain the redirect if moved or modified.
**/}

`st.connection("snowflake")` can be configured using [Streamlit secrets](/develop/concepts/connections/secrets-management) or keyword args just like any other connection. It can also use existing Snowflake connection configuration when available.

Note that [snowflake-snowpark-python](https://pypi.org/project/snowflake-snowpark-python/) must be installed to use this connection.

#### Using Streamlit secrets

For example, if your Snowflake account supports SSO, you can set up a quick local connection for development using [browser-based SSO](https://docs.snowflake.com/en/user-guide/admin-security-fed-auth-use#how-browser-based-sso-works) and `secrets.toml` as follows:

```toml
# .streamlit/secrets.toml

[connections.snowflake]
account = "<ACCOUNT ID>"
user = "<USERNAME>"
authenticator = "EXTERNALBROWSER"
```

Learn more about [account indentifier here](https://docs.snowflake.com/en/user-guide/admin-account-identifier). You could also specify the full configuration and credentials in your secrets file, as in the [example here](/develop/tutorials/databases/snowflake#add-connection-parameters-to-your-local-app-secrets).

#### Using existing Snowflake configuration

Snowflake's python driver also supports a [connection configuration file](https://docs.snowflake.com/en/developer-guide/python-connector/python-connector-example#connecting-using-the-connections-toml-file), which is well integrated with Streamlit `SnowflakeConnection`. If you already have one or more connections configured, all you need to do is pass Streamlit the name of the connection to use. This can be done in several ways:

- Set `connection_name` in your app code, such as `st.connnection("<name>", type="snowflake")`.
- Set `connection_name = "<name>"` in the `[connections.snowflake]` section of your Streamlit secrets.
- Set the environment variable `SNOWFLAKE_DEFAULT_CONNECTION_NAME=<name>`.
- [Set a default connection](https://docs.snowflake.com/en/developer-guide/python-connector/python-connector-example#setting-a-default-connection) in your Snowflake configuration.

When available in [Streamlit in Snowflake](https://docs.snowflake.com/en/developer-guide/streamlit/about-streamlit), `st.connection("snowflake")` will connect automatically using the [app owner role](https://docs.snowflake.com/en/developer-guide/streamlit/owners-rights) and does not require any configuration.

Learn more about setting up connections in the [Connecting Streamlit to Snowflake tutorial](/develop/tutorials/databases/snowflake) and [Connecting to data](/develop/concepts/connections/connecting-to-data).

<Autofunction function="streamlit.connections.SnowflakeConnection.cursor" />

<Autofunction function="streamlit.connections.SnowflakeConnection.query" />

<Autofunction function="streamlit.connections.SnowflakeConnection.raw_connection" />

<Autofunction function="streamlit.connections.SnowflakeConnection.reset" />

<Autofunction function="streamlit.connections.SnowflakeConnection.session" />

<Autofunction function="streamlit.connections.SnowflakeConnection.write_pandas" />
