---
title: Connections and databases
slug: /library/api-reference/connections
---

# Connections and databases

## Setup your connection

<TileContainer>
<RefCard href="/library/api-reference/connections/st.experimental_connection" size="half">

<Image pure alt="screenshot" src="/images/api/connection.jpg" />

#### Create a connection

Connect to a data source or API

```python
conn = st.experimental_connection('pets_db', type='sql')
pet_owners = conn.query('select * from pet_owners')
st.dataframe(pet_owners)
```

</RefCard>
</TileContainer>

## Built-in connections

<TileContainer>

<RefCard href="/library/api-reference/connections/st.connections.sqlconnection" size="half">

<Image pure alt="screenshot" src="/images/api/connections.SQLConnection.jpg" />

#### SQLConnection

A connection to a SQL database using SQLAlchemy.

```python
conn = st.experimental_connection('sql')
```

</RefCard>

<RefCard href="/library/api-reference/connections/st.connections.snowparkconnection" size="half">

<Image pure alt="screenshot" src="/images/api/connections.SnowparkConnection.jpg" />

#### SnowparkConnection

A connection to Snowflake Snowpark.

```python
conn = st.experimental_connection('snowpark')
```

</RefCard>
</TileContainer>

## Third-party connections

<TileContainer>
<RefCard href="/library/api-reference/connections/st.connections.experimentalbaseconnection" size="half">

#### Connection base class

Build your own connection with `ExperimentalBaseConnection`.

```python
class MyConnection(ExperimentalBaseConnection[myconn.MyConnection]):
    def _connect(self, **kwargs) -> MyConnection:
        return myconn.connect(**self._secrets, **kwargs)
    def query(self, query):
        return self._instance.query(query)
```

</RefCard>

</TileContainer>
