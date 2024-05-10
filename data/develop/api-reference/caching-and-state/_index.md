---
title: Caching and state
slug: /develop/api-reference/caching-and-state
---

# Caching and state

Optimize performance and add statefulness to your app!

## Caching

Streamlit provides powerful [cache primitives](/develop/concepts/architecture/caching) for data and global resources. They allow your app to stay performant even when loading data from the web, manipulating large datasets, or performing expensive computations.

<TileContainer>

<RefCard href="/develop/api-reference/caching-and-state/st.cache_data" size="half">

<h4>Cache data</h4>

Function decorator to cache functions that return data (e.g. dataframe transforms, database queries, ML inference).

```python
@st.cache_data
def long_function(param1, param2):
  # Perform expensive computation here or
  # fetch data from the web here
  return data
```

</RefCard>

<RefCard href="/develop/api-reference/caching-and-state/st.cache_resource" size="half">

<h4>Cache resource</h4>

Function decorator to cache functions that return global resources (e.g. database connections, ML models).

```python
@st.cache_resource
def init_model():
  # Return a global resource here
  return pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english"
  )
```

</RefCard>

</TileContainer>

## Manage state

Streamlit re-executes your script with each user interaction. Widgets have built-in statefulness between reruns, but Session State lets you do more!

<TileContainer>
<RefCard href="/develop/api-reference/caching-and-state/st.session_state" size="half" >

<h4>Session State</h4>

Save data between reruns and across pages.

```python
st.session_state["foo"] = "bar"
```

</RefCard>
<RefCard href="/develop/api-reference/caching-and-state/st.query_params" size="half">

<h4>Query parameters</h4>

Get, set, or clear the query parameters that are shown in the browser's URL bar.

```python
st.query_params[key] = value
st.query_params.clear()
```

</RefCard>

</TileContainer>

## Deprecated commands

<TileContainer>

<RefCard href="/develop/api-reference/caching-and-state/st.cache" deprecated={true}>

> This command was deprecated in version 1.18.0. Use `st.cache_data` or `st.cache_resource` instead.

<h4>Caching</h4>

Function decorator to memoize function executions.

```python
@st.cache(ttl=3600)
def run_long_computation(arg1, arg2):
  # Do stuff here
  return computation_output
```

</RefCard>

<RefCard href="/develop/api-reference/caching-and-state/st.experimental_memo" deprecated={true}>

> This command was deprecated in version 1.18.0. Use `st.cache_data` instead.

<h4>Memo</h4>

Experimental function decorator to memoize function executions.

```python
@st.experimental_memo
def fetch_and_clean_data(url):
  # Fetch data from URL here, and then clean it up.
  return data
```

</RefCard>

<RefCard href="/develop/api-reference/caching-and-state/st.experimental_singleton" deprecated={true}>

> This command was deprecated in version 1.18.0. Use `st.cache_resource` instead.

<h4>Singleton</h4>

Experimental function decorator to store singleton objects.

```python
@st.experimental_singleton
def get_database_session(url):
  # Create a database session object that points to the URL.
  return session
```

</RefCard>
<RefCard href="/develop/api-reference/caching-and-state/st.experimental_get_query_params" size="half" deprecated={true}>

<h4>Get query parameters</h4>

Get query parameters that are shown in the browser's URL bar.

```python
param_dict = st.experimental_get_query_params()
```

</RefCard>
<RefCard href="/develop/api-reference/caching-and-state/st.experimental_set_query_params" size="half" deprecated={true}>

<h4>Set query parameters</h4>

Set query parameters that are shown in the browser's URL bar.

```python
st.experimental_set_query_params(
  {"show_all"=True, "selected"=["asia", "america"]}
)
```

</RefCard>
</TileContainer>
