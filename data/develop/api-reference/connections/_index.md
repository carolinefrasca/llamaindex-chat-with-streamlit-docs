---
title: Connections and databases
slug: /develop/api-reference/connections
---

# Connections and databases

## Setup your connection

<TileContainer>
<RefCard href="/develop/api-reference/connections/st.connection" size="half">

<Image pure alt="screenshot" src="/images/api/connection.svg" />

<h4>Create a connection</h4>

Connect to a data source or API

```python
conn = st.connection('pets_db', type='sql')
pet_owners = conn.query('select * from pet_owners')
st.dataframe(pet_owners)
```

</RefCard>
</TileContainer>

## Built-in connections

<TileContainer>

<RefCard href="/develop/api-reference/connections/st.connections.snowflakeconnection" size="half">

<Image pure alt="screenshot" src="/images/api/connections.SnowflakeConnection.svg" />

<h4>SnowflakeConnection</h4>

A connection to Snowflake.

```python
conn = st.connection('snowflake')
```

</RefCard>

<RefCard href="/develop/api-reference/connections/st.connections.sqlconnection" size="half">

<Image pure alt="screenshot" src="/images/api/connections.SQLConnection.svg" />

<h4>SQLConnection</h4>

A connection to a SQL database using SQLAlchemy.

```python
conn = st.connection('sql')
```

</RefCard>
</TileContainer>

## Third-party connections

<TileContainer>
<RefCard href="/develop/api-reference/connections/st.connections.baseconnection" size="half">

<h4>Connection base class</h4>

Build your own connection with `BaseConnection`.

```python
class MyConnection(BaseConnection[myconn.MyConnection]):
    def _connect(self, **kwargs) -> MyConnection:
        return myconn.connect(**self._secrets, **kwargs)
    def query(self, query):
        return self._instance.query(query)
```

</RefCard>

</TileContainer>

## Secrets

<TileContainer>
<RefCard href="/develop/api-reference/connections/st.secrets" size="half">

<h4>Secrets singleton</h4>

Access secrets from a local TOML file.

```python
key = st.secrets["OpenAI_key"]
```

</RefCard>
<RefCard href="/develop/api-reference/connections/secrets.toml" size="half">

<h4>Secrets file</h4>

Save your secrets in a per-project or per-profile TOML file.

```python
OpenAI_key = "<YOUR_SECRET_KEY>"
```

</RefCard>

</TileContainer>

## Deprecated classes

<TileContainer>
<RefCard href="/develop/api-reference/connections/st.connections.snowparkconnection" size="half" deprecated={true}>

<h4>SnowparkConnection</h4>

A connection to Snowflake.

```python
conn = st.connection("snowpark")
```

</RefCard>

</TileContainer>
